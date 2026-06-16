#!/usr/bin/env python3
"""PostToolUse hook: validate PM Brain file writes (Braindump Floor gate).

BLOCK (exit 2): new artifact scaffold in 3-Work/ with no user-thinking markers.
WARN (exit 0 + stderr): softer issues (e.g. template path in new file).

Invoked by Cursor with JSON on stdin: {"tool_input": {"file_path": "..."}}
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
WORK_MARKERS = re.compile(
    r"(assumption|hypothesis|know vs|guess|risk|uncomfortable|"
    r"evidence|success criteria|second-order|what if|we assume|i'm guessing)",
    re.I,
)
TEMPLATE_MARKERS = re.compile(
    r"(## Problem Statement|## Success Metrics|## Scope|## Non-Goals|## Requirements|# PRD)",
    re.I,
)
ARTIFACT_PREFIXES = ("3-Work/",)


def read_payload() -> dict:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def is_brain_artifact(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    return rel.startswith(ARTIFACT_PREFIXES) and rel.endswith(".md")


def validate_file(path: Path) -> tuple[int, list[str]]:
    """Return (exit_code, messages). 2 = BLOCK, 0 = WARN or OK."""
    if not path.exists():
        return 0, []

    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        return 0, []

    if not is_brain_artifact(rel):
        return 0, []

    text = path.read_text(encoding="utf-8", errors="replace")
    has_template = bool(TEMPLATE_MARKERS.search(text))
    has_thinking = bool(WORK_MARKERS.search(text))
    is_short = len(text.strip()) < 400

    messages: list[str] = []

    # BLOCK: new template scaffold in 3-Work without thinking markers
    if has_template and not has_thinking and is_short:
        messages.append(
            f"BLOCKING: {rel} looks like a template scaffold without braindump markers. "
            "Braindump Floor: think first — add assumptions, know vs guess, risks before structure."
        )
        return 2, messages

    if has_template and not has_thinking:
        messages.append(
            f"WARNING: {rel} has template sections but no thinking markers (assumptions, risks, etc.)."
        )

    return 0, messages


def main() -> int:
    payload = read_payload()
    file_path = (
        payload.get("tool_input", {}).get("file_path")
        or payload.get("file_path")
        or ""
    )
    if not file_path:
        return 0

    path = Path(file_path)
    if not path.is_absolute():
        path = ROOT / path

    exit_code, messages = validate_file(path)
    for msg in messages:
        print(msg, file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
