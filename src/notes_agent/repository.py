from __future__ import annotations

import json
from pathlib import Path

from .models import PageScript


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTENT = ROOT / "content" / "pages.json"
DEFAULT_STATE = ROOT / "state" / "workflow.json"


def load_pages(path: Path = DEFAULT_CONTENT) -> list[PageScript]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [PageScript.from_dict(item) for item in payload["pages"]]


def load_style() -> dict:
    return json.loads((ROOT / "content" / "style-profile.json").read_text(encoding="utf-8"))


def load_state(path: Path = DEFAULT_STATE) -> dict:
    if not path.exists():
        return {"current_batch": 1, "pages": {}, "history": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(value: dict, path: Path = DEFAULT_STATE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
