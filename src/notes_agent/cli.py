from __future__ import annotations

import argparse
import json
import sys

from .repository import load_pages, load_state
from .validation import validate_pages
from .workflow import batch_count, initialize_state, record_decision, record_script_decision, write_batch_prompts


def parse_pages(value: str) -> list[int]:
    pages: list[int] = []
    for part in value.split(","):
        if "-" in part:
            start, end = map(int, part.split("-", 1))
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    return sorted(set(pages))


def main() -> None:
    parser = argparse.ArgumentParser(prog="notes-agent")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="validate all 50 scripts and coverage")
    sub.add_parser("status", help="show approval workflow state")
    sub.add_parser("init", help="reset workflow to written-script review")
    script = sub.add_parser("script-decision", help="approve the full script or request revision")
    script.add_argument("--decision", required=True, choices=["approved", "revision_requested"])
    script.add_argument("--note", default="")
    prompts = sub.add_parser("prompts", help="compile one image prompt batch (up to ten pages)")
    prompts.add_argument("--batch", type=int, required=True, choices=range(1, batch_count() + 1))
    decide = sub.add_parser("decide", help="record human approval/revision decisions")
    decide.add_argument("--pages", required=True, help="for example 1-10 or 1,3,8")
    decide.add_argument("--decision", required=True, choices=["generated", "approved", "revision_requested"])
    decide.add_argument("--note", default="")
    args = parser.parse_args()

    try:
        if args.command == "validate":
            errors = validate_pages(load_pages())
            if errors:
                print("Validation failed:")
                print("\n".join(f"- {item}" for item in errors))
                sys.exit(1)
            print("Validation passed: 65 beginner scripts, continuous numbering, coverage and page-level gates OK.")
        elif args.command == "status":
            print(json.dumps(load_state(), indent=2))
        elif args.command == "init":
            print(json.dumps(initialize_state(), indent=2))
        elif args.command == "script-decision":
            record_script_decision(args.decision, args.note)
            print(f"Recorded full-script decision: {args.decision}")
        elif args.command == "prompts":
            print(write_batch_prompts(args.batch))
        elif args.command == "decide":
            record_decision(parse_pages(args.pages), args.decision, args.note)
            print(f"Recorded {args.decision} for {args.pages}")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
