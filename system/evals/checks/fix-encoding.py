#!/usr/bin/env python3
"""Fix mojibake in markdown files (text-safe; no UTF-8 byte surgery)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Only used when a file is not valid UTF-8
BYTE_REPLACEMENTS: dict[bytes, str] = {
    b"\x96": "\u2013",
    b"\x97": "\u2014",
    b"\x91": "\u2018",
    b"\x92": "\u2019",
    b"\x93": "\u201c",
    b"\x94": "\u201d",
    b"\x95": "\u2022",
}

SKIP_DIRS = {"node_modules", ".git", ".venv", "__pycache__"}

TEXT_REPLACEMENTS: list[tuple[str, str]] = [
    ("Rules auto-load\u2014\u2019", "Rules auto-load?"),
    ("?\u2014\u2019 **", "⚠️ **"),
    ("# ?\u2014\u2019 ", "# 📌 "),
    ("## ?\u2014\u2019 ", "## 📌 "),
    ("?→ **", "⚠️ **"),
    ("# ?→ ", "# 📌 "),
    ("## ?→ ", "## 📌 "),
    ("only?you", "only — you"),
    ("understand?ask", "understand — ask"),
    ("product_sense?execution_mode", "product_sense → execution_mode"),
    ("you?ve", "you've"),
    ("you?re", "you're"),
    ("company?s", "company's"),
    ("don?t", "don't"),
    ("can?t", "can't"),
    ("won?t", "won't"),
    ("it?s", "it's"),
    ("that?s", "that's"),
    ("what?s", "what's"),
    ("isn?t", "isn't"),
    ("doesn?t", "doesn't"),
    ("haven?t", "haven't"),
    ("wouldn?t", "wouldn't"),
    ("couldn?t", "couldn't"),
    ("shouldn?t", "shouldn't"),
    ("?→ Public", "📌 Public"),
    ("?→ Private", "📌 Private"),
    ("?→ Team", "📌 Team"),
    ("- **?→ Missing", "- **⚠️ Missing"),
    (" ?→ ", " → "),
    ("?→ ", "→ "),
    ("{?→ ", "{→ "),
    ("|?→ ", "|→ "),
    ("\u2014\u2019", "\u2192"),
    ("\ufffd\u201d\u2019", "\u2192"),
    ("\ufffd\u201d", "\u2014"),
    ("\ufffd", "\u2014"),
    ("Impact\u2014Effort", "Impact-Effort"),
    ("Value\u2014Effort", "Value-Effort"),
    ("Severity\u2014Frequency", "Severity-Frequency"),
    ("Value\u2014Complexity", "Value-Complexity"),
    ("Dunning\u2014Kruger", "Dunning-Kruger"),
    ("Problem\u2014Solution", "Problem-Solution"),
    ("Shreyas Doshi\u2014style", "Shreyas Doshi-style"),
    ("\u2192 \u2192", "\u2192"),
    ("\u2014\u2018", "-"),
    ("\u2014\u201d", "---"),
]


def load_text(path: Path) -> str:
    data = path.read_bytes()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        for byte, char in BYTE_REPLACEMENTS.items():
            data = data.replace(byte, char.encode("utf-8"))
        return data.decode("utf-8", errors="replace")


def read_markdown(path: Path) -> str:
    return load_text(path)


def fix_text(text: str) -> str:
    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)

    text = re.sub(r"\?\?\?\s*$", "🎯", text, flags=re.MULTILINE)
    text = re.sub(r" \?\?\s*$", " 👋", text, flags=re.MULTILINE)
    text = re.sub(r" \?\?\s", " — ", text)
    text = re.sub(r"^(\s*)\?\? \*\*", r"\1⚠️ **", text, flags=re.MULTILINE)
    text = re.sub(r"^# \?\? ", "# 📌 ", text, flags=re.MULTILINE)
    text = re.sub(r"^## \?\? ", "## 📌 ", text, flags=re.MULTILINE)

    arrow = "\u2192"
    en_dash = "\u2013"
    text = re.sub(r" \? ", f" {arrow} ", text)
    text = re.sub(r"(\d)\?(\d)", lambda m: f"{m.group(1)}{en_dash}{m.group(2)}", text)
    text = re.sub(r"(\w)→ ", lambda m: f"{m.group(1)} → ", text)
    text = re.sub(r"(\d)\u2014(\d)", lambda m: f"{m.group(1)}{en_dash}{m.group(2)}", text)
    text = re.sub(r"(\d\.\d)\u2014(?=\s*\()", r"\1x", text)
    text = re.sub(r"(\d\.\d)\u2014 ", r"\1x ", text)
    text = re.sub(r"(\d)\u2014,", r"\1x,", text)
    text = re.sub(r"\(0\.(\d)\u2014 ", lambda m: f"(0.{m.group(1)} × ", text)
    text = re.sub(r"^—   \+--", "|   +--", text, flags=re.M)
    text = re.sub(r"^[\u2014\u2022]{8,}$", lambda m: "=" * 80, text, flags=re.M)
    text = re.sub(r"^[\u2014]{10,}$", lambda m: "-" * min(len(m.group()), 80), text, flags=re.M)
    text = re.sub(r"🟢/🟡/——", "🟢/🟡/🔴", text)
    text = repair_diagram_blocks(text)

    return text


def repair_diagram_blocks(text: str) -> str:
    """Fix diagram lines corrupted by em-dash substitution (inside fenced blocks only)."""
    parts = re.split(r"(```(?:text|markdown)?\n[\s\S]*?```)", text)
    out: list[str] = []
    for part in parts:
        if part.startswith("```"):
            body = part.split("\n", 1)[1].rsplit("```", 1)[0]
            fence = part.split("\n", 1)[0]
            repaired = _repair_diagram_body(body)
            out.append(f"{fence}\n{repaired}```")
        else:
            # Section headers in template scaffolds (outside fences): —— ALL CAPS
            part = re.sub(
                r"^—— ([A-Z0-9][A-Z0-9 /(),.:;'\"-]+)$",
                r"## \1",
                part,
                flags=re.M,
            )
            out.append(part)
    return "".join(out)


def _repair_diagram_body(body: str) -> str:
    if not re.search(r"[\u2014]{2,}|^## —|^——", body, re.M):
        return body
    lines = body.split("\n")
    fixed: list[str] = []
    for line in lines:
        s = line
        s = re.sub(r"^——— YES", "├── YES", s)
        s = re.sub(r"^---—— NO", "└── NO", s)
        s = re.sub(r"^---—— YES", "├── YES", s)
        s = re.sub(r"^——— NO", "└── NO", s)
        if s.startswith("## ") and (
            "——" in s or s in {"## YES", "## NO", "## —"} or "→" in s
        ):
            s = s[3:]
        s = re.sub(r"—— ——", " ", s)
        s = re.sub(r"——", " ", s)
        s = re.sub(r"^---+", "├──", s)
        s = re.sub(r"^=+$", lambda m: "=" * min(len(m.group()), 80), s)
        s = re.sub(r"  +", " ", s).rstrip()
        fixed.append(s)
    return "\n".join(fixed)


def process_file(path: Path, dry_run: bool = False) -> bool:
    original_text = load_text(path)
    fixed_text = fix_text(original_text)
    if fixed_text == original_text:
        return False
    if not dry_run:
        path.write_text(fixed_text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    changed = 0
    for path in sorted(ROOT.rglob("*")):
        if path.suffix not in {".md", ".mdc"}:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if process_file(path, dry_run=dry_run):
            changed += 1
    print(f"{'Would change' if dry_run else 'Changed'}: {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
