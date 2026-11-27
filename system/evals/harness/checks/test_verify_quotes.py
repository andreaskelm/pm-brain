#!/usr/bin/env python3
"""Regression tests for system/evals/checks/verify-quotes.py in --snapshot --strict mode.

Each case writes a tiny transcript + snapshot to a temp dir and checks the exit code.
Run: python system/evals/harness/checks/test_verify_quotes.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / "system" / "evals" / "checks" / "verify-quotes.py"

TRANSCRIPT = """# Transcript: Test — Acme — 2026-12-01

Me: Walk me through the last late delivery.

Test Person: Last month a big order left three days after the promised date. I rang the warehouse and we pulled two people off another job.

Me: So sales promises dates the warehouse cannot hit?

Test Person: Maybe. I wouldn't put it like that. I think it depends on the week.

Test Person: Next quarter we will move to a new routing tool. That is the plan anyway.
"""


def run(snapshot_body: str, *, bom: bool = False) -> int:
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "transcripts").mkdir()
        (d / "snapshots").mkdir()
        (d / "transcripts" / "transcript-test-acme-2026-12-01.md").write_text(TRANSCRIPT, encoding="utf-8")
        snap = d / "snapshots" / "snapshot-test-acme-2026-12-01.md"
        snap.write_bytes((b"\xef\xbb\xbf" if bom else b"") + snapshot_body.encode("utf-8"))
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--snapshot", str(snap), "--no-report", "--strict"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        return proc.returncode


def case_good_verbatim() -> None:
    body = (
        "# H\n"
        '> "Last month a big order left three days after the promised date." (L5)\n'
        '> "Maybe. I wouldn\'t put it like that. I think it depends on the week." (L9)\n'
    )
    assert run(body) == 0


def case_good_quote_on_first_line_with_bom() -> None:
    assert run('> "Next quarter we will move to a new routing tool." (L11)\n', bom=True) == 0


def case_bad_interviewer_words() -> None:
    assert run('# H\n> "So sales promises dates the warehouse cannot hit?" (L7)\n') == 1


def case_bad_hedge_dropped() -> None:
    body = '# H\n> "Sales promises dates the warehouse cannot hit, it depends on the week." (L9)\n'
    assert run(body) == 1


def case_bad_stitched_across_interviewer_turn() -> None:
    body = (
        "# H\n"
        '> "I rang the warehouse and we pulled two people off another job ... '
        'Maybe. I wouldn\'t put it like that." (L5)\n'
    )
    assert run(body) == 1


def case_bad_invented_words() -> None:
    assert run('# H\n> "We completely rebuilt our planning process last spring." (L5)\n') == 1


def main() -> int:
    cases = [v for k, v in sorted(globals().items()) if k.startswith("case_")]
    failed = 0
    for fn in cases:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError:
            failed += 1
            print(f"FAIL {fn.__name__}")
    print(f"{len(cases) - failed}/{len(cases)} cases passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
