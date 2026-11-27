#!/usr/bin/env python3
"""Unit tests for validate_write.py hook (subprocess, deterministic)."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HOOK = Path(__file__).resolve().parents[2] / "hooks" / "validate_write.py"


def invoke_hook(workdir: Path, file_path: Path) -> tuple[int, str]:
    payload = json.dumps({"tool_input": {"file_path": str(file_path)}})
    proc = subprocess.run(
        [sys.executable, str(HOOK)],
        input=payload,
        cwd=workdir,
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.returncode, proc.stderr


def git_init(workdir: Path) -> None:
    subprocess.run(
        ["git", "init"],
        cwd=workdir,
        capture_output=True,
        check=True,
    )


def git_track(workdir: Path, rel_path: str) -> None:
    subprocess.run(
        ["git", "add", rel_path],
        cwd=workdir,
        capture_output=True,
        check=True,
    )


def test_blocks_template_scaffold_without_thinking() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        artifact = workdir / "3-Work" / "test-init" / "prd.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text(
            "# PRD\n\n## Problem Statement\nTBD\n\n## Success Metrics\nTBD\n",
            encoding="utf-8",
        )
        code, err = invoke_hook(workdir, artifact)
        assert code == 2, f"expected BLOCK, got {code}: {err}"


def test_allows_artifact_with_thinking_markers() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        artifact = workdir / "3-Work" / "test-init" / "prd.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text(
            "# PRD\n\n## Assumptions\nUsers batch weekly.\n\n## Problem Statement\nReduce triage time.\n",
            encoding="utf-8",
        )
        code, err = invoke_hook(workdir, artifact)
        assert code == 0, f"expected OK, got {code}: {err}"


def test_ignores_non_work_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        doc = workdir / "docs" / "note.md"
        doc.parent.mkdir(parents=True)
        doc.write_text("# PRD\n\n## Problem Statement\nTBD\n", encoding="utf-8")
        code, err = invoke_hook(workdir, doc)
        assert code == 0, f"expected OK, got {code}: {err}"


def test_empty_stdin_exits_zero() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        proc = subprocess.run(
            [sys.executable, str(HOOK)],
            input="",
            cwd=tmp,
            capture_output=True,
            text=True,
            check=False,
        )
        assert proc.returncode == 0


def test_warns_untracked_template_structure_in_initiative() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        git_init(workdir)
        artifact = workdir / "3-Work" / "test-init" / "_foo-template.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("# Foo\n\nPlaceholder.\n", encoding="utf-8")
        code, err = invoke_hook(workdir, artifact)
        assert code == 0, f"expected WARN only (exit 0), got {code}: {err}"
        assert "looks like a new template or structure" in err


def test_silent_untracked_template_under_legacy() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        git_init(workdir)
        artifact = workdir / "3-Work" / "test-init" / "_legacy" / "_foo-template.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("# Legacy template\n", encoding="utf-8")
        code, err = invoke_hook(workdir, artifact)
        assert code == 0, f"expected OK, got {code}: {err}"
        assert "looks like a new template or structure" not in err


def test_silent_ordinary_untracked_notes_in_initiative() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        git_init(workdir)
        artifact = workdir / "3-Work" / "test-init" / "notes.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("# Notes\n\nJust thinking.\n", encoding="utf-8")
        code, err = invoke_hook(workdir, artifact)
        assert code == 0, f"expected OK, got {code}: {err}"
        assert "looks like a new template or structure" not in err


def test_silent_git_tracked_file_with_template_in_name() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        git_init(workdir)
        artifact = workdir / "3-Work" / "test-init" / "old-template.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("# Canonical copy\n", encoding="utf-8")
        git_track(workdir, "3-Work/test-init/old-template.md")
        code, err = invoke_hook(workdir, artifact)
        assert code == 0, f"expected OK, got {code}: {err}"
        assert "looks like a new template or structure" not in err


def main() -> int:
    tests = [
        test_blocks_template_scaffold_without_thinking,
        test_allows_artifact_with_thinking_markers,
        test_ignores_non_work_files,
        test_empty_stdin_exits_zero,
        test_warns_untracked_template_structure_in_initiative,
        test_silent_untracked_template_under_legacy,
        test_silent_ordinary_untracked_notes_in_initiative,
        test_silent_git_tracked_file_with_template_in_name,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
            print(f"PASS {test.__name__}")
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
    print(f"\n{passed}/{len(tests)} cases passed")
    return 0 if passed == len(tests) else 1


if __name__ == "__main__":
    raise SystemExit(main())
