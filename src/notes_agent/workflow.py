from __future__ import annotations

from datetime import datetime, timezone
from math import ceil
from pathlib import Path

from .models import PageStatus
from .prompts import compile_prompt
from .repository import ROOT, load_pages, load_state, load_style, save_state


BATCH_SIZE = 10
SCRIPT_DECISIONS = {"approved", "revision_requested", "review_pending"}


def _event(action: str, **details) -> dict:
    return {"at": datetime.now(timezone.utc).isoformat(), "action": action, **details}


def initialize_state() -> dict:
    total_pages = len(load_pages())
    state = {
        "script": {"status": "review_pending", "edition": "Beginner-friendly 65-page edition"},
        "current_batch": 1,
        "pages": {str(number): {"status": PageStatus.SCRIPTED} for number in range(1, total_pages + 1)},
        "history": [_event("scripts_created", pages=total_pages)],
    }
    save_state(state)
    return state


def batch_count() -> int:
    return ceil(len(load_pages()) / BATCH_SIZE)


def batch_pages(batch_number: int):
    pages = load_pages()
    total_batches = ceil(len(pages) / BATCH_SIZE)
    if batch_number not in range(1, total_batches + 1):
        raise ValueError(f"Batch must be from 1 through {total_batches}")
    start = (batch_number - 1) * BATCH_SIZE
    return pages[start : start + BATCH_SIZE]


def _assert_batch_unlocked(state: dict, batch_number: int) -> None:
    if state.get("script", {}).get("status") != "approved":
        raise ValueError("The complete written script needs human approval before image prompts can be compiled")
    if batch_number > 1:
        previous = range((batch_number - 2) * BATCH_SIZE + 1, (batch_number - 1) * BATCH_SIZE + 1)
        blocked = [page for page in previous if state["pages"].get(str(page), {}).get("status") != PageStatus.APPROVED]
        if blocked:
            raise ValueError(
                f"Batch {batch_number} is locked until every page in the prior batch is approved; blocked pages: {blocked}"
            )


def record_script_decision(decision: str, note: str = "") -> None:
    if decision not in SCRIPT_DECISIONS - {"review_pending"}:
        raise ValueError("Script decision must be approved or revision_requested")
    state = load_state()
    state.setdefault("script", {})
    state["script"].update({"status": decision, "note": note})
    state["history"].append(_event("script_" + decision, note=note))
    save_state(state)


def write_batch_prompts(batch_number: int) -> Path:
    state = load_state()
    _assert_batch_unlocked(state, batch_number)
    style = load_style()
    pages = batch_pages(batch_number)
    target = ROOT / "generated" / "prompts" / f"batch-{batch_number:02d}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    parts = [f"# Image Prompts — Batch {batch_number}\n"]
    for page in pages:
        parts.extend([f"## Page {page.page:02d} — {page.title}\n", "```text", compile_prompt(page, style), "```\n"])
    target.write_text("\n".join(parts), encoding="utf-8")

    for page in pages:
        state["pages"].setdefault(str(page.page), {})
        state["pages"][str(page.page)]["status"] = PageStatus.PROMPT_READY
    state["history"].append(_event("prompts_compiled", batch=batch_number))
    save_state(state)
    return target


def record_decision(page_numbers: list[int], decision: str, note: str = "") -> None:
    allowed = {PageStatus.APPROVED, PageStatus.REVISION_REQUESTED, PageStatus.GENERATED}
    status = PageStatus(decision)
    if status not in allowed:
        raise ValueError(f"Decision must be one of: {', '.join(map(str, allowed))}")
    state = load_state()
    total_pages = len(load_pages())
    for page in page_numbers:
        if page not in range(1, total_pages + 1):
            raise ValueError(f"Invalid page: {page}")
        state["pages"].setdefault(str(page), {})
        state["pages"][str(page)].update({"status": status, "note": note})
    state["history"].append(_event(str(status), pages=page_numbers, note=note))
    save_state(state)
