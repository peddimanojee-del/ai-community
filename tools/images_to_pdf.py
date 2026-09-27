#!/usr/bin/env python3
"""Assemble JPEG pages into a dependency-free PDF.

Usage: python3 tools/images_to_pdf.py output.pdf page-01.jpg page-02.jpg ...
Images should already share the intended page ratio; each is fitted to A4.
"""
from __future__ import annotations

import sys
from pathlib import Path


def jpeg_size(data: bytes) -> tuple[int, int]:
    if data[:2] != b"\xff\xd8":
        raise ValueError("input is not a JPEG")
    index = 2
    sof = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    while index < len(data):
        if data[index] != 0xFF:
            index += 1
            continue
        while index < len(data) and data[index] == 0xFF:
            index += 1
        marker = data[index]
        index += 1
        if marker in {0xD8, 0xD9}:
            continue
        length = int.from_bytes(data[index:index + 2], "big")
        if marker in sof:
            height = int.from_bytes(data[index + 3:index + 5], "big")
            width = int.from_bytes(data[index + 5:index + 7], "big")
            return width, height
        index += length
    raise ValueError("JPEG dimensions not found")


def pdf_stream(dictionary: str, data: bytes) -> bytes:
    return f"<< {dictionary} /Length {len(data)} >>\nstream\n".encode() + data + b"\nendstream"


def assemble(output: Path, inputs: list[Path]) -> None:
    if not inputs:
        raise ValueError("at least one JPEG page is required")
    objects: dict[int, bytes] = {}
    page_ids = [3 + index * 3 for index in range(len(inputs))]
    objects[1] = b"<< /Type /Catalog /Pages 2 0 R >>"
    kids = " ".join(f"{page_id} 0 R" for page_id in page_ids)
    objects[2] = f"<< /Type /Pages /Count {len(inputs)} /Kids [{kids}] >>".encode()

    for index, path in enumerate(inputs):
        page_id = 3 + index * 3
        image_id = page_id + 1
        content_id = page_id + 2
        image = path.read_bytes()
        width, height = jpeg_size(image)
        objects[page_id] = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
            f"/Resources << /XObject << /Im0 {image_id} 0 R >> >> "
            f"/Contents {content_id} 0 R >>"
        ).encode()
        objects[image_id] = pdf_stream(
            f"/Type /XObject /Subtype /Image /Width {width} /Height {height} "
            "/ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode",
            image,
        )
        objects[content_id] = pdf_stream("", b"q\n595 0 0 842 0 0 cm\n/Im0 Do\nQ")

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for object_id in range(1, max(objects) + 1):
        offsets.append(len(pdf))
        pdf.extend(f"{object_id} 0 obj\n".encode())
        pdf.extend(objects[object_id])
        pdf.extend(b"\nendobj\n")
    xref = len(pdf)
    pdf.extend(f"xref\n0 {len(offsets)}\n".encode())
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode())
    pdf.extend(
        f"trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(pdf)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    assemble(Path(sys.argv[1]), [Path(value) for value in sys.argv[2:]])
