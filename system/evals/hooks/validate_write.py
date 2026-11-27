#!/usr/bin/env python3
"""PostToolUse hook: validate PM Brain file writes (Braindump Floor gate).

BLOCK (exit 2): new artifact scaffold in 3-Work/ with no user-thinking markers.
WARN (exit 0 + stderr): softer issues — template sections without thinking markers,
or new template/structure filenames in initiative folders (check 2-Methods/ first).

Invoked by Cursor with JSON on stdin: {"tool_input": {"file_path": "..."}}
"""
from __future__ import annotations

import json
import re
import subprocess
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
STRUCTURE_FILENAME = re.compile(
    r"(template|register|ledger|frame|taxonomy|codebook)",
    re.I,
)
ARTIFACT_PREFIXES = ("3-Work/",)

NEW_STRUCTURE_WARNING = (
    "WARNING: {rel} looks like a new template or structure. "
    "Check 2-Methods/ for a canonical one first (AGENTS.md Principle 6). "
    "If you are deliberately deviating, say so and get the user's OK before continuing."
)

SANCTIONED_INITIATIVES = frozenset({"signals", "hypotheses"})


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


def is_exempt_initiative_path(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    if "/_legacy/" in f"/{rel}/":
        return True
    if rel.startswith("3-Work/signals/") or rel.startswith("3-Work/hypotheses/"):
        return True
    return False


def is_initiative_work_path(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    if not rel.startswith("3-Work/"):
        return False
    if is_exempt_initiative_path(rel):
        return False
    parts = rel.split("/")
    if len(parts) < 3:
        return False
    if parts[1] in SANCTIONED_INITIATIVES:
        return False
    return True


def looks_like_template_structure_filename(name: str) -> bool:
    if name.startswith("_"):
        return True
    return bool(STRUCTURE_FILENAME.search(name))


def is_git_untracked(rel: str) -> bool:
    """True if path exists on disk but is not in the git index; False if git absent."""
    rel_posix = rel.replace("\\", "/")
    try:
        in_repo = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=ROOT,
            capture_output=True,
            check=False,
        )
        if in_repo.returncode != 0:
            return False
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", rel_posix],
            cwd=ROOT,
            capture_output=True,
            check=False,
        )
        return tracked.returncode != 0
    except (OSError, FileNotFoundError):
        return False


def new_template_structure_warnings(path: Path, rel: str) -> list[str]:
    if path.suffix.lower() not in (".md", ".py"):
        return []
    if not is_initiative_work_path(rel):
        return []
    if not looks_like_template_structure_filename(path.name):
        return []
    if not is_git_untracked(rel):
        return []
    return [NEW_STRUCTURE_WARNING.format(rel=rel.replace("\\", "/"))]


def validate_file(path: Path) -> tuple[int, list[str]]:
    """Return (exit_code, messages). 2 = BLOCK, 0 = WARN or OK."""
    if not path.exists():
        return 0, []

    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        return 0, []

    messages: list[str] = []
    messages.extend(new_template_structure_warnings(path, rel))

    if not is_brain_artifact(rel):
        return 0, messages

    text = path.read_text(encoding="utf-8", errors="replace")
    has_template = bool(TEMPLATE_MARKERS.search(text))
    has_thinking = bool(WORK_MARKERS.search(text))
    is_short = len(text.strip()) < 400

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
