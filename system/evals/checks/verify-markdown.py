#!/usr/bin/env python3
"""L0 repo health: encoding corruption, broken links, eval-spec consistency."""
from __future__ import annotations

import importlib.util
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
ROOT_FILES = {"AGENTS.md", "README.md", "USER.md", "TODO.md"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(
    r"`((?:\.\./)+(?:[0-9]-[^/`]+/)+[^`\s]+\.(?:md|mdc))`"
)
MENTAL_MODELS_PREFIX = Path("2-Methods") / "1-Foundations" / "1-Mental-Models"


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


def check_eval_spec_consistency(errors: list[str]) -> None:
    """Scenario folders are self-describing: each expected.yaml must point at real files."""
    try:
        import yaml  # type: ignore
    except ImportError:
        errors.append("eval-spec: PyYAML not installed (pip install -r system/evals/requirements.txt)")
        return

    scenarios = EVALS_DIR / "scenarios"
    behavior = scenarios / "behavior"
    seen_ids: dict[str, str] = {}
    by_prefix: dict[str, list[str]] = {}

    for folder in sorted(d for d in behavior.iterdir() if d.is_dir()) if behavior.exists() else []:
        by_prefix.setdefault(folder.name.split("-", 1)[0], []).append(folder.name)
        expected = folder / "expected.yaml"
        if not expected.exists():
            errors.append(f"eval-spec: behavior/{folder.name} has no expected.yaml")
            continue
        spec_data = yaml.safe_load(expected.read_text(encoding="utf-8")) or {}
        sid = spec_data.get("scenario_id", "")
        if not sid:
            errors.append(f"eval-spec: behavior/{folder.name} missing scenario_id")
        elif sid in seen_ids:
            errors.append(f"eval-spec: duplicate scenario_id {sid} in {seen_ids[sid]} and {folder.name}")
        else:
            seen_ids[sid] = folder.name

        content_specs = list(spec_data.get("final_state", {}).get("content", []) or [])
        for turn in spec_data.get("turns", []) or []:
            input_name = turn.get("input", "")
            if input_name and not (folder / "inputs" / input_name).exists():
                errors.append(f"eval-spec: behavior/{folder.name} input missing: {input_name}")
            content_specs.extend(turn.get("content", []) or [])
        for judge in content_specs:
            rubric = judge.get("rubric", "")
            if rubric and not (EVALS_DIR / rubric).exists():
                errors.append(f"eval-spec: behavior/{folder.name} judge rubric missing: {rubric}")

    for prefix, names in by_prefix.items():
        if len(names) > 1:
            errors.append(f"eval-spec: duplicate behavior folder prefix {prefix}: {', '.join(names)}")

    for expected in sorted((scenarios / "rubric").glob("*/expected.yaml")):
        spec_data = yaml.safe_load(expected.read_text(encoding="utf-8")) or {}
        rubric_path = spec_data.get("rubric_path", "")
        if rubric_path and not (ROOT / rubric_path).exists():
            errors.append(f"eval-spec: {expected.parent.name} rubric_path missing: {rubric_path}")
        for fixture in spec_data.get("fixtures", []) or []:
            if not (expected.parent / fixture.get("input", "")).exists():
                errors.append(f"eval-spec: {expected.parent.name} fixture missing: {fixture.get('input')}")


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
