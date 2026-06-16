#!/usr/bin/env python3
"""L0 repo health: encoding corruption, broken links, eval-spec consistency."""
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EVALS_DIR = ROOT / "system" / "evals"

spec = importlib.util.spec_from_file_location(
    "fix_encoding", EVALS_DIR / "checks" / "fix-encoding.py"
)
fix_encoding = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(fix_encoding)

ACTIVE_PREFIXES = {
    "2-Methods",
    "1-Context",
    "3-Work",
    "4-Research",
    "5-Growth",
    "system",
    "docs",
    ".cursor",
    ".claude",
}
ROOT_FILES = {"AGENTS.md", "README.md", "USER.md", "TODO.md", "CLAUDE.md"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(
    r"`((?:\.\./)+(?:[0-9]-[^/`]+/)+[^`\s]+\.(?:md|mdc))`"
)
MENTAL_MODELS_PREFIX = Path("2-Methods") / "1-Foundations" / "1-Mental-Models"
SCENARIO_ID_RE = re.compile(r"`([a-z0-9_]+_\d{3})`")


def under_mental_models(rel: Path) -> bool:
    prefix = MENTAL_MODELS_PREFIX.parts
    return len(rel.parts) >= len(prefix) and rel.parts[: len(prefix)] == prefix


def in_scope(rel: Path) -> bool:
    if not rel.parts:
        return False
    if rel.name in ROOT_FILES and len(rel.parts) == 1:
        return True
    return rel.parts[0] in ACTIVE_PREFIXES


def check_encoding(text: str, rel: str, errors: list[str]) -> None:
    if "\ufffd" in text:
        errors.append(f"{rel}: contains U+FFFD replacement character")
    if "\u2014\u2019" in text:
        errors.append(f"{rel}: contains corrupted arrow sequence (—')")
    if "\u2014\u2018" in text:
        errors.append(f"{rel}: contains corrupted compound dash (—')")
    if "\u2014\u201d" in text:
        errors.append(f"{rel}: contains corrupted tree corner (—\")")
    if "??" in text:
        errors.append(f"{rel}: contains ?? (likely lost emoji)")
    if "?→" in text:
        errors.append(f"{rel}: contains corrupted ?→ sequence")

    scrubbed = re.sub(r"\[([^\]]*)\]\([^)]+\)", "", text)
    scrubbed = re.sub(r"https?://[^\s)]+", "", scrubbed)
    if re.search(r"[a-zA-Z]\?[a-z]", scrubbed):
        errors.append(f"{rel}: contains ? inside word (likely lost apostrophe)")
    if re.search(r"\d\.\d— ", scrubbed):
        errors.append(f"{rel}: contains corrupted multiplier (e.g. 1.0—)")
    if scrubbed.count("\u2014\u2014") > 5:
        errors.append(f"{rel}: contains excessive —— runs (likely lost ASCII art)")


def check_links(path: Path, text: str, errors: list[str]) -> None:
    rel = str(path.relative_to(ROOT))
    for match in LINK_RE.finditer(text):
        target = match.group(2).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#")[0]
        if not target or target.startswith("<"):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{rel}: broken link -> {target}")

    for match in BACKTICK_PATH_RE.finditer(text):
        if not under_mental_models(path.relative_to(ROOT)):
            continue
        target = match.group(1).strip()
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{rel}: broken backtick path -> {target}")


HARNESS_ONLY_IDS: set[str] = set()


def iter_behavior_expected() -> list[Path]:
    behavior = EVALS_DIR / "scenarios" / "behavior"
    if not behavior.exists():
        return []
    return sorted(behavior.glob("*/expected.yaml"))


def check_eval_spec_consistency(errors: list[str]) -> None:
    scenarios_path = EVALS_DIR / "agent-behavior-scenarios.json"
    assertions_path = EVALS_DIR / "behavior-assertions.md"

    if not scenarios_path.exists() or not assertions_path.exists():
        errors.append("eval-spec: missing agent-behavior-scenarios.json or behavior-assertions.md")
        return

    data = json.loads(scenarios_path.read_text(encoding="utf-8"))
    defined_ids = {s["scenario_id"] for s in data.get("scenarios", [])} | HARNESS_ONLY_IDS
    harness_paths = {s["scenario_id"]: s.get("harness_path", "") for s in data.get("scenarios", [])}

    assertions_text = assertions_path.read_text(encoding="utf-8")
    referenced_ids = set(SCENARIO_ID_RE.findall(assertions_text))

    missing = sorted(referenced_ids - defined_ids)
    if missing:
        errors.append(
            f"eval-spec: behavior-assertions.md references undefined scenario IDs: {', '.join(missing)}"
        )

    for expected in iter_behavior_expected():
        try:
            import yaml  # type: ignore
        except ImportError:
            return
        content = yaml.safe_load(expected.read_text(encoding="utf-8"))
        if not content:
            continue
        if content.get("type") == "rubric_regression":
            continue
        sid = content.get("scenario_id")
        if sid not in defined_ids:
            errors.append(
                f"eval-spec: {expected.relative_to(ROOT)} scenario_id "
                f"{sid} not in agent-behavior-scenarios.json"
            )
        rel_path = f"behavior/{expected.parent.name}"
        if sid in harness_paths and harness_paths[sid] and harness_paths[sid] != rel_path:
            errors.append(
                f"eval-spec: {sid} harness_path {harness_paths[sid]!r} != {rel_path!r}"
            )

    check_behavior_folder_uniqueness(errors, harness_paths)


def check_behavior_folder_uniqueness(
    errors: list[str], harness_paths: dict[str, str]
) -> None:
    behavior = EVALS_DIR / "scenarios" / "behavior"
    if not behavior.exists():
        return

    indexed_paths = {p for p in harness_paths.values() if p}
    folders = sorted(d for d in behavior.iterdir() if d.is_dir())
    folder_names = [d.name for d in folders]

    # Orphan folders: on disk but not in JSON index
    for folder in folders:
        rel = f"behavior/{folder.name}"
        if rel not in indexed_paths:
            errors.append(f"eval-spec: orphan behavior folder not in JSON index: {rel}")

    # Duplicate NN-prefix folders (e.g. 03-foo and 03-foo-001)
    by_prefix: dict[str, list[str]] = {}
    for name in folder_names:
        prefix = name.split("-", 1)[0] if "-" in name else name
        by_prefix.setdefault(prefix, []).append(name)
    for prefix, names in by_prefix.items():
        if len(names) > 1:
            errors.append(
                f"eval-spec: duplicate behavior folder prefix {prefix}: {', '.join(names)}"
            )

    # JSON paths pointing at missing folders
    for sid, rel_path in harness_paths.items():
        if not rel_path:
            continue
        target = EVALS_DIR / "scenarios" / rel_path.replace("/", os.sep)
        if not target.is_dir():
            errors.append(f"eval-spec: {sid} harness_path missing on disk: {rel_path}")


def main() -> int:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if path.suffix not in {".md", ".mdc"}:
            continue
        rel = path.relative_to(ROOT)
        if not in_scope(rel):
            continue
        text = fix_encoding.load_text(path)
        rel_str = str(rel)
        check_encoding(text, rel_str, errors)
        check_links(path, text, errors)

    check_eval_spec_consistency(errors)

    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for err in errors:
            print(err)
        return 1

    print("OK: no encoding, link, or eval-spec issues in scoped paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
