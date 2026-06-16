"""Write harness JSON results and prune older runs."""
from __future__ import annotations

import json
import os
from pathlib import Path


def keep_count() -> int:
    raw = os.environ.get("PM_BRAIN_EVAL_KEEP", "2")
    try:
        return max(0, int(raw))
    except ValueError:
        return 2


def prune_results(results_dir: Path, glob_pattern: str, keep: int) -> list[Path]:
    """Delete oldest matching JSON files, keeping the newest `keep` by mtime."""
    if keep <= 0:
        return []

    matches = sorted(
        results_dir.glob(glob_pattern),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    removed: list[Path] = []
    for path in matches[keep:]:
        path.unlink(missing_ok=True)
        removed.append(path)
    return removed


def write_json_result(
    results_dir: Path,
    filename: str,
    payload: dict,
    *,
    prune_glob: str | None = None,
    keep: int | None = None,
) -> Path:
    results_dir.mkdir(parents=True, exist_ok=True)
    out_path = results_dir / filename
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    if prune_glob is not None:
        prune_results(results_dir, prune_glob, keep if keep is not None else keep_count())

    return out_path
