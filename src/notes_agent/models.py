from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class PageStatus(StrEnum):
    SCRIPTED = "scripted"
    PROMPT_READY = "prompt_ready"
    GENERATED = "generated"
    APPROVED = "approved"
    REVISION_REQUESTED = "revision_requested"


@dataclass(frozen=True)
class Panel:
    heading: str
    copy: list[str]
    visual: str = ""

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Panel":
        return cls(
            heading=value["heading"],
            copy=list(value["copy"]),
            visual=value.get("visual", ""),
        )


@dataclass(frozen=True)
class PageScript:
    page: int
    module: str
    title: str
    objective: str
    layout: str
    panels: list[Panel]
    code: list[str] = field(default_factory=list)
    flowchart: str = ""
    important: list[str] = field(default_factory=list)
    summary: list[str] = field(default_factory=list)
    interview_checks: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "PageScript":
        return cls(
            page=value["page"],
            module=value["module"],
            title=value["title"],
            objective=value["objective"],
            layout=value["layout"],
            panels=[Panel.from_dict(item) for item in value["panels"]],
            code=list(value.get("code", [])),
            flowchart=value.get("flowchart", ""),
            important=list(value.get("important", [])),
            summary=list(value.get("summary", [])),
            interview_checks=list(value.get("interview_checks", [])),
        )
