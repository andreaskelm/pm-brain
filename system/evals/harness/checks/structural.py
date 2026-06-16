"""Deterministic structural assertions for PM Brain eval harness."""
from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

FORECAST_LOG = Path("5-Growth/3-Product-Judgment-Test/forecast-log.md")


@dataclass
class AssertionResult:
    assertion_type: str
    arg: Any
    passed: bool
    message: str
    spec_owner: str = ""


def _glob_paths(workdir: Path, pattern: str) -> list[Path]:
    pattern = pattern.replace("\\", "/")
    matches: list[Path] = []
    for path in workdir.rglob("*"):
        rel = path.relative_to(workdir).as_posix()
        if fnmatch.fnmatch(rel, pattern):
            matches.append(path)
    return matches


def _read_forecast_rows(workdir: Path) -> int:
    path = workdir / FORECAST_LOG
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    # Count table data rows (lines starting with | and not header separator)
    rows = 0
    for line in text.splitlines():
        if line.strip().startswith("|") and "---" not in line and "Date" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells and cells[0] and not cells[0].startswith("-"):
                rows += 1
    return rows


def snapshot_files(workdir: Path, prefixes: tuple[str, ...] | None = None) -> dict[str, float]:
    snap: dict[str, float] = {}
    for path in workdir.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(workdir).as_posix()
        if prefixes and not any(rel.startswith(p) for p in prefixes):
            continue
        if ".git" in path.parts:
            continue
        snap[rel] = path.stat().st_mtime
    return snap


def files_created(before: dict[str, float], after: dict[str, float]) -> set[str]:
    return {p for p in after if p not in before}


def files_modified(before: dict[str, float], after: dict[str, float]) -> set[str]:
    modified: set[str] = set()
    for p, mtime in after.items():
        if p in before and before[p] != mtime:
            modified.add(p)
    modified |= files_created(before, after)
    return modified


def run_assertion(
    workdir: Path,
    assertion: dict[str, Any],
    *,
    before: dict[str, float],
    after: dict[str, float],
    agent_response: str = "",
) -> AssertionResult:
    atype = assertion.get("type", assertion.get("assertion", ""))
    arg = assertion.get("arg", assertion.get("path", ""))
    spec_owner = assertion.get("spec_owner", "")

    try:
        if atype == "file_exists":
            path = workdir / str(arg)
            ok = path.exists()
            return AssertionResult(atype, arg, ok, f"file_exists {arg}: {ok}", spec_owner)

        if atype == "file_exists_glob":
            matches = _glob_paths(workdir, str(arg))
            ok = len(matches) > 0
            return AssertionResult(
                atype, arg, ok, f"file_exists_glob {arg}: {len(matches)} match(es)", spec_owner
            )

        if atype == "file_not_created_glob":
            created = files_created(before, after)
            bad = [p for p in created if fnmatch.fnmatch(p, str(arg))]
            ok = len(bad) == 0
            return AssertionResult(
                atype,
                arg,
                ok,
                f"file_not_created_glob {arg}: created={bad or 'none'}",
                spec_owner,
            )

        if atype == "file_modified":
            rel = str(arg).replace("\\", "/")
            ok = rel in files_modified(before, after)
            return AssertionResult(atype, arg, ok, f"file_modified {arg}: {ok}", spec_owner)

        if atype == "file_modified_or_created":
            rel = str(arg).replace("\\", "/")
            exists = (workdir / rel).exists()
            ok = exists or rel in files_created(before, after)
            return AssertionResult(
                atype, arg, ok, f"file_modified_or_created {arg}: {ok}", spec_owner
            )

        if atype == "question_count_at_least":
            n = int(arg)
            count = agent_response.count("?")
            ok = count >= n
            return AssertionResult(
                atype, arg, ok, f"question_count_at_least {n}: found {count}", spec_owner
            )

        if atype == "forecast_log_row_added":
            before_rows = _read_forecast_rows(workdir)  # approximate via snapshot diff
            # Re-read: compare line count in file if modified
            rel = FORECAST_LOG.as_posix()
            if rel not in files_modified(before, after) and rel not in files_created(before, after):
                ok = False
                msg = "forecast_log_row_added: file not modified"
            else:
                rows = _read_forecast_rows(workdir)
                ok = rows >= 1
                msg = f"forecast_log_row_added: rows={rows}"
            return AssertionResult(atype, None, ok, msg, spec_owner)

        if atype == "response_contains":
            needle = str(arg)
            ok = needle.lower() in agent_response.lower()
            return AssertionResult(
                atype, arg, ok, f"response_contains '{needle}': {ok}", spec_owner
            )

        if atype == "response_not_contains":
            needle = str(arg)
            ok = needle.lower() not in agent_response.lower()
            return AssertionResult(
                atype, arg, ok, f"response_not_contains '{needle}': {ok}", spec_owner
            )

        if atype == "response_not_links_template":
            template_link = re.compile(
                r"(?:\]\(|`|\b)(2-Methods/[^\s\)`]*(?:template|2-[^/\s]+-template)[^\s\)`]*)",
                re.I,
            )
            matches = template_link.findall(agent_response)
            ok = len(matches) == 0
            return AssertionResult(
                atype,
                None,
                ok,
                f"response_not_links_template: {matches or 'none found'}",
                spec_owner,
            )

        if atype == "all_internal_links_valid":
            touched = files_modified(before, after)
            md_touched = {p for p in touched if p.endswith(".md")}
            if not md_touched:
                return AssertionResult(
                    atype,
                    None,
                    True,
                    "all_internal_links_valid: no markdown files modified; skipped",
                    spec_owner,
                )
            errors: list[str] = []
            for rel in sorted(md_touched):
                path = workdir / rel
                if not path.exists():
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
                for match in LINK_RE.finditer(text):
                    target = match.group(2).strip().split("#")[0]
                    if not target or target.startswith(("http://", "https://", "mailto:", "#", "<")):
                        continue
                    resolved = (path.parent / target).resolve()
                    if not resolved.exists():
                        errors.append(f"{rel} -> {target}")
            ok = len(errors) == 0
            return AssertionResult(
                atype,
                None,
                ok,
                f"all_internal_links_valid: {len(errors)} broken in modified files"
                if errors
                else f"all links valid ({len(md_touched)} file(s) checked)",
                spec_owner,
            )

        if atype == "no_duplicate_content":
            # Warn-level: file should link to source, not embed full duplicate
            rel = str(arg).replace("\\", "/")
            path = workdir / rel
            if not path.exists():
                return AssertionResult(atype, arg, True, "no_duplicate_content: file absent", spec_owner)
            text = path.read_text(encoding="utf-8", errors="replace")
            links = LINK_RE.findall(text)
            ok = len(links) >= 1 or len(text) < 500
            return AssertionResult(
                atype, arg, ok, f"no_duplicate_content: links={len(links)}", spec_owner
            )

        return AssertionResult(atype, arg, False, f"unknown assertion type: {atype}", spec_owner)
    except Exception as exc:  # noqa: BLE001
        return AssertionResult(atype, arg, False, f"error: {exc}", spec_owner)


def run_assertions(
    workdir: Path,
    assertions: list[dict[str, Any]],
    *,
    before: dict[str, float],
    after: dict[str, float],
    agent_response: str = "",
) -> list[AssertionResult]:
    return [
        run_assertion(
            workdir, a, before=before, after=after, agent_response=agent_response
        )
        for a in assertions
    ]
