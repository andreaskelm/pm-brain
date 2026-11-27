#!/usr/bin/env python3
"""Unit tests for quotes_verbatim structural assertion (deterministic)."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HARNESS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HARNESS))
from checks.structural import run_assertion  # noqa: E402

JONAS_TRANSCRIPT = """\
Here's the transcript from my call with Jonas, a logistics lead at a mid-size distributor. Make me the interview snapshot for it.

Interviewer: Walk me through the last time a delivery went out late.

Jonas: Last month, a big retail order, about forty pallets. It left the warehouse three days after the date sales had given the customer.

Interviewer: So the real issue is that sales promises dates the warehouse can't hit?

Jonas: Maybe. I wouldn't put it like that. I think it depends on the week.

Interviewer: What changed in how you plan since then?

Jonas: Honestly, not a lot yet. We talked about a weekly check between sales and the warehouse, but I don't think anyone has started it.
"""


def run_quotes_verbatim(
    workdir: Path,
    scenario_dir: Path,
    snapshot_rel: str,
    snapshot_body: str,
    transcript_name: str = "inputs/turn-01-user.md",
) -> tuple[bool, str]:
    snap = workdir / snapshot_rel
    snap.parent.mkdir(parents=True, exist_ok=True)
    snap.write_text(snapshot_body, encoding="utf-8")
    (scenario_dir / "inputs").mkdir(parents=True, exist_ok=True)
    (scenario_dir / transcript_name).write_text(JONAS_TRANSCRIPT, encoding="utf-8")
    assertion = {
        "type": "quotes_verbatim",
        "arg": transcript_name,
        "snapshot": snapshot_rel,
    }
    result = run_assertion(
        workdir,
        assertion,
        before={},
        after={},
        scenario_dir=scenario_dir,
    )
    return result.passed, result.message


def test_verbatim_participant_quote_with_hedge() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        body = '# Snapshot\n\n«Maybe. I wouldn\'t put it like that»\n'
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert passed, msg


def test_shortened_quote_drops_hedge_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        body = (
            "# Snapshot\n\n"
            "«I wouldn't put it like that. Sales promises dates the warehouse can't hit»\n"
        )
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert not passed, f"expected fail, got pass: {msg}"


def test_quote_only_in_interviewer_line_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        body = "# Snapshot\n\n«sales promises dates the warehouse can't hit»\n"
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert not passed, f"expected fail, got pass: {msg}"


def test_ellipsis_join_two_verbatim_turns_passes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        left = "Last month, a big retail order, about forty pallets"
        right = "Maybe. I wouldn't put it like that"
        body = f"# Snapshot\n\n«{left}…{right}»\n"
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert passed, msg


def test_zero_quotes_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        body = "# Snapshot\n\nNo quoted material here.\n"
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert not passed, f"expected fail, got pass: {msg}"
        assert "no quotes" in msg.lower()


def test_missing_snapshot_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        (scenario / "inputs").mkdir(parents=True)
        (scenario / "inputs/turn-01-user.md").write_text(JONAS_TRANSCRIPT, encoding="utf-8")
        assertion = {
            "type": "quotes_verbatim",
            "arg": "inputs/turn-01-user.md",
            "snapshot": "snap/missing.md",
        }
        result = run_assertion(
            workdir,
            assertion,
            before={},
            after={},
            scenario_dir=scenario,
        )
        assert not result.passed
        assert "missing" in result.message.lower()


def test_cdh_blockquote_with_line_ref_passes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        quote = (
            "Honestly, not a lot yet. We talked about a weekly check between sales and the warehouse"
        )
        body = f'# Snapshot\n\n> "{quote}" (L12)\n'
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert passed, msg


def test_guillemet_format_passes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp) / "work"
        scenario = Path(tmp) / "scenario"
        workdir.mkdir()
        scenario.mkdir()
        rel = "snap/snapshot.md"
        body = (
            "# Snapshot\n\n"
            "«about forty pallets. It left the warehouse three days after the date sales had given the customer»\n"
        )
        passed, msg = run_quotes_verbatim(workdir, scenario, rel, body)
        assert passed, msg


def main() -> int:
    tests = [
        test_verbatim_participant_quote_with_hedge,
        test_shortened_quote_drops_hedge_fails,
        test_quote_only_in_interviewer_line_fails,
        test_ellipsis_join_two_verbatim_turns_passes,
        test_zero_quotes_fails,
        test_missing_snapshot_fails,
        test_cdh_blockquote_with_line_ref_passes,
        test_guillemet_format_passes,
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