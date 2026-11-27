#!/usr/bin/env python3
"""Zero-token check: «…» quotes in snapshots and synthesis vs transcripts.

Splits each quote on ellipses, then looks up every segment in the
interview transcript. No model calls. Statuses:

  matched    — segment is in the transcript after whitespace/case fold
  fuzzy      — best window is close but not exact (speech-to-text drift,
               a dropped hedge, or a small edit)
  not-found  — no close window

A quote whose segments land more than a few lines apart is flagged
stitched. If a "Me:" turn sits between those lines, it is flagged
crosses-interviewer.

Also treats blockquote lines (CDH style): a line starting with ``> `` that
contains straight or curly double-quoted text of at least 12 characters.

Usage (from repo root):

  python system/evals/checks/verify-quotes.py --snapshot PATH [--transcript PATH] [--no-report] [--strict]
  python system/evals/checks/verify-quotes.py --study PATH/TO/research [--no-report] [--strict]
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

QUOTE_RE = re.compile(r"«([^»]+)»", re.DOTALL)
CDH_QUOTE_RE = re.compile(
    r'"([^"]{12,})"|\u201c([^\u201d]{12,})\u201d',
)
ELLIPSIS_RE = re.compile(r"(?:\.\.\.|…)+")
SPEAKER_RE = re.compile(r"^(Me|[^:]+):\s*(.*)$")

MIN_SEGMENT = 12
FUZZY_RATIO = 0.72
STITCH_GAP = 4

def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path(__file__).resolve()).parent
    for _ in range(32):
        if (cur / "AGENTS.md").is_file():
            return cur
        parent = cur.parent
        if parent == cur:
            break
        cur = parent
    raise SystemExit("Could not find repo root (no AGENTS.md walking up from script).")


def report_script_link() -> str:
    return "[verify-quotes.py](../../../../system/evals/checks/verify-quotes.py)"


def fold(text: str) -> str:
    text = text.replace("\u00a0", " ").replace("\u2011", "-")
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def fold_loose(text: str) -> str:
    text = fold(text)
    text = text.replace("«", "").replace("»", "")
    text = re.sub(r"[^\wæøå\s-]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


@dataclass
class Transcript:
    path: Path
    interview_id: str
    speakers: list[str]
    folded: list[str]
    loose: list[str]

    @classmethod
    def load(cls, path: Path) -> "Transcript":
        raw = path.read_text(encoding="utf-8-sig").splitlines()
        speakers: list[str] = []
        folded: list[str] = []
        loose: list[str] = []
        for line in raw:
            match = SPEAKER_RE.match(line.strip())
            if match and not line.startswith("#"):
                speakers.append(match.group(1).strip())
                body = match.group(2)
            else:
                speakers.append("")
                body = line
            folded.append(fold(body))
            loose.append(fold_loose(body))
        interview_id = path.stem.removeprefix("transcript-")
        return cls(path, interview_id, speakers, folded, loose)


@dataclass
class Hit:
    status: str
    line: int | None
    ratio: float
    window: str = ""


@dataclass
class SegmentResult:
    text: str
    hit: Hit


@dataclass
class QuoteResult:
    source: Path
    source_line: int
    raw: str
    interview_id: str
    segments: list[SegmentResult] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)

    @property
    def worst(self) -> str:
        order = {"not-found": 0, "fuzzy": 1, "short": 2, "matched": 3}
        statuses = [s.hit.status for s in self.segments] or ["not-found"]
        return min(statuses, key=lambda s: order.get(s, 0))


def joined(lines: list[str], start: int, width: int) -> str:
    return " ".join(lines[start : start + width])


def exact_line(transcript: Transcript, needle: str, loose: str) -> int | None:
    for width in (1, 2, 3):
        for idx in range(len(transcript.folded)):
            if needle and needle in joined(transcript.folded, idx, width):
                return idx + 1
            if loose and loose in joined(transcript.loose, idx, width):
                return idx + 1
    return None


def locate(transcript: Transcript, segment: str) -> Hit:
    needle = fold(segment)
    loose = fold_loose(segment)
    if len(loose) < MIN_SEGMENT:
        return Hit("short", None, 1.0)

    found = exact_line(transcript, needle, loose)
    if found is not None:
        return Hit("matched", found, 1.0)

    # Fuzzy only on lines that share a long word with the segment.
    anchors = sorted((w for w in loose.split() if len(w) >= 6), key=len, reverse=True)[:3]
    candidate_idx: set[int] = set()
    for idx, hay in enumerate(transcript.loose):
        if any(word in hay for word in anchors):
            candidate_idx.add(idx)
    if not candidate_idx:
        return Hit("not-found", None, 0.0)

    best_ratio = 0.0
    best_line = 1
    best_window = ""
    seg_words = loose.split()
    span = min(len(seg_words) + 3, 24)
    for idx in candidate_idx:
        hay_words = joined(transcript.loose, idx, 2).split()
        if not hay_words:
            continue
        if len(hay_words) <= span:
            chunks = [" ".join(hay_words)]
        else:
            step = max(span // 3, 1)
            chunks = [
                " ".join(hay_words[start : start + span])
                for start in range(0, len(hay_words) - span + 1, step)
            ]
        for chunk in chunks:
            ratio = SequenceMatcher(None, loose, chunk).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_line = idx + 1
                best_window = chunk

    if best_ratio >= FUZZY_RATIO:
        return Hit("fuzzy", best_line, best_ratio, best_window)
    return Hit("not-found", None, best_ratio, best_window)


def stitch_flags(transcript: Transcript, segments: list[SegmentResult]) -> list[str]:
    lines = [s.hit.line for s in segments if s.hit.line is not None]
    flags: list[str] = []
    # A quote that matches the interviewer's own words is not the participant's quote.
    for line_no in lines:
        speaker = transcript.speakers[line_no - 1] if line_no - 1 < len(transcript.speakers) else ""
        if speaker == "Me":
            flags.append("interviewer-line")
            break
    if len(lines) >= 2 and max(lines) > min(lines):
        if max(lines) - min(lines) > STITCH_GAP:
            flags.append(f"stitched:{min(lines)}-{max(lines)}")
        # An interviewer turn between two segments means the quote joins two answers,
        # however close together they sit (short interviewer turns are the common case).
        for line_no in range(min(lines), max(lines) + 1):
            speaker = transcript.speakers[line_no - 1] if line_no - 1 < len(transcript.speakers) else ""
            if speaker == "Me":
                flags.append("crosses-interviewer")
                break
    return flags


def interview_for_snapshot(path: Path) -> str:
    return path.stem.removeprefix("snapshot-")


def transcript_path_for_snapshot(snapshot: Path) -> Path:
    research = snapshot.parent.parent
    interview_id = interview_for_snapshot(snapshot)
    return research / "transcripts" / f"transcript-{interview_id}.md"


def extract_quotes(path: Path) -> list[tuple[int, str]]:
    quotes: list[tuple[int, str]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        for match in QUOTE_RE.finditer(line):
            quotes.append((line_no, match.group(1).strip()))
        if line.startswith("> "):
            for match in CDH_QUOTE_RE.finditer(line):
                text = match.group(1) if match.group(1) is not None else match.group(2)
                quotes.append((line_no, text.strip()))
    return quotes


def best_transcript(transcripts: list[Transcript], segments: list[str]) -> Transcript:
    """Pick a transcript by exact hits only. Fuzzy runs later, once."""

    def score(transcript: Transcript) -> int:
        total = 0
        for segment in segments:
            loose = fold_loose(segment)
            if len(loose) < MIN_SEGMENT:
                continue
            if exact_line(transcript, fold(segment), loose) is not None:
                total += 3
            elif any(word in " ".join(transcript.loose) for word in loose.split() if len(word) >= 7):
                total += 1
        return total

    return max(transcripts, key=score)


def check_file(
    path: Path,
    transcripts: list[Transcript],
    by_id: dict[str, Transcript],
    snapshots_dir: Path,
    forced_transcript: Transcript | None = None,
) -> list[QuoteResult]:
    forced: Transcript | None = forced_transcript
    if forced is None and path.parent == snapshots_dir and path.name.startswith("snapshot-"):
        forced = by_id.get(interview_for_snapshot(path))

    results: list[QuoteResult] = []
    for line_no, raw in extract_quotes(path):
        parts = [part.strip(" \t-–—") for part in ELLIPSIS_RE.split(raw)]
        parts = [part for part in parts if part]
        transcript = forced
        if transcript is None:
            transcript = best_transcript(transcripts, parts)
        result = QuoteResult(path, line_no, raw, transcript.interview_id)
        for part in parts:
            result.segments.append(SegmentResult(part, locate(transcript, part)))
        result.flags = stitch_flags(transcript, result.segments)
        results.append(result)
    return results


def tally(results: list[QuoteResult]) -> tuple[dict[str, int], int, int]:
    counts = {"matched": 0, "fuzzy": 0, "not-found": 0, "short": 0}
    stitched = 0
    crosses = 0
    for result in results:
        counts[result.worst] = counts.get(result.worst, 0) + 1
        if any(flag.startswith("stitched") for flag in result.flags):
            stitched += 1
        if "crosses-interviewer" in result.flags:
            crosses += 1
    return counts, stitched, crosses


def render(results: list[QuoteResult]) -> str:
    counts, stitched, crosses = tally(results)

    lines = [
        "# Quote verify",
        "",
        f"**Run:** {date.today().isoformat()}  ",
        f"**Script:** {report_script_link()} — no model, transcript text only.",
        "",
        "| Status | Quotes |",
        "|--------|--------|",
        f"| matched (worst segment) | {counts['matched']} |",
        f"| fuzzy | {counts['fuzzy']} |",
        f"| not-found | {counts['not-found']} |",
        f"| short-only | {counts['short']} |",
        f"| stitched (segments land far apart) | {stitched} |",
        f"| crosses an interviewer turn | {crosses} |",
        f"| matches an interviewer line (not the participant's words) | {sum(1 for r in results if 'interviewer-line' in r.flags)} |",
        "",
        "A quote counts as its worst segment. Stitched quotes can still be matched: the words are in the transcript, but they were joined across a gap.",
        "",
        "**Limits of this run.** A short leading fragment can anchor on an earlier line that merely contains the same word (`produktteams` at L33 vs the real sentence at L272), so a stitch flag can be a false alarm. Synthesis quotes with no exact hit are assigned to whichever transcript shares a long word; check the snapshot row before treating that assignment as attribution. Site labels in «» (for example «Outcome i dele af huset») are not participant speech and will show as not-found.",
        "",
    ]

    def section(title: str, picked: list[QuoteResult]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not picked:
            lines.append("None.")
            lines.append("")
            return
        for result in picked:
            rel = result.source.name
            lines.append(f"### {rel}:{result.source_line} → `{result.interview_id}`")
            lines.append("")
            lines.append(f"> «{result.raw}»")
            lines.append("")
            if result.flags:
                lines.append("Flags: " + ", ".join(f"`{flag}`" for flag in result.flags))
                lines.append("")
            for segment in result.segments:
                hit = segment.hit
                where = f"L{hit.line}" if hit.line else "—"
                extra = f" ratio={hit.ratio:.2f}" if hit.status == "fuzzy" else ""
                snippet = segment.text.replace("\n", " ")
                if len(snippet) > 180:
                    snippet = snippet[:177] + "…"
                lines.append(f"- **{hit.status}** {where}{extra}: {snippet}")
            lines.append("")

    problems = [r for r in results if r.worst in {"not-found", "fuzzy"}]
    stitched_ok = [
        r
        for r in results
        if r.worst == "matched" and any(f.startswith("stitched") for f in r.flags)
    ]
    section("Not found or fuzzy", problems)
    section("Matched, but stitched", stitched_ok)
    lines.append("## Matched and contiguous")
    lines.append("")
    lines.append(
        f"{sum(1 for r in results if r.worst == 'matched' and not any(f.startswith('stitched') for f in r.flags))} quotes. Not listed."
    )
    lines.append("")
    return "\n".join(lines)


def print_tally(results: list[QuoteResult], report_name: str | None) -> None:
    worst: dict[str, int] = {}
    for result in results:
        worst[result.worst] = worst.get(result.worst, 0) + 1
    suffix = f"  wrote {report_name}" if report_name else ""
    print(
        f"{len(results)} quotes → "
        + ", ".join(f"{k}={v}" for k, v in sorted(worst.items()))
        + suffix
    )


def strict_violation(results: list[QuoteResult]) -> bool:
    for result in results:
        if result.worst == "not-found":
            return True
        if any(flag.startswith("stitched") for flag in result.flags):
            return True
        if "crosses-interviewer" in result.flags or "interviewer-line" in result.flags:
            return True
    return False


def resolve_path(root: Path, path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (root / path).resolve()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify snapshot/synthesis quotes against interview transcripts (no model)."
    )
    parser.add_argument(
        "--snapshot",
        type=Path,
        help="Verify only this snapshot file (infers transcript from filename).",
    )
    parser.add_argument(
        "--transcript",
        type=Path,
        help="Transcript to use with --snapshot (overrides filename inference).",
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Print the full report to stdout; do not write quote-verify-latest.md.",
    )
    parser.add_argument(
        "--study",
        type=Path,
        help="Batch mode: research folder with snapshots/ and transcripts/ (optional synthesis.md).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any quote is not-found, stitched, crosses-interviewer, or matches an interviewer line.",
    )
    return parser.parse_args(argv)


def report_path_for_study(research: Path) -> Path:
    analysis = research / "analysis" / "quote-verify-latest.md"
    if analysis.parent.is_dir():
        return analysis
    return research / "quote-verify-latest.md"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.snapshot is None and args.study is None:
        raise SystemExit(
            "Specify --snapshot <file> or --study <research-folder>. "
            "Example: python system/evals/checks/verify-quotes.py --snapshot 4-Research/foo/snapshots/snapshot-x.md --strict"
        )
    root = find_repo_root()

    if args.snapshot is not None:
        snapshot = resolve_path(root, args.snapshot)
        if not snapshot.is_file():
            raise SystemExit(f"Snapshot not found: {snapshot}")
        if args.transcript is not None:
            tpath = resolve_path(root, args.transcript)
        else:
            tpath = transcript_path_for_snapshot(snapshot)
        if not tpath.is_file():
            raise SystemExit(f"Transcript not found: {tpath}")
        transcripts = [Transcript.load(tpath)]
        by_id = {transcripts[0].interview_id: transcripts[0]}
        forced = transcripts[0]
        sources = [snapshot]
        snap_dir = snapshot.parent
        report = report_path_for_study(snapshot.parent.parent)
    else:
        research = resolve_path(root, args.study)
        snapshots = research / "snapshots"
        transcripts_dir = research / "transcripts"
        synthesis = research / "synthesis.md"
        report = report_path_for_study(research)
        transcripts = [Transcript.load(path) for path in sorted(transcripts_dir.glob("transcript-*.md"))]
        by_id = {t.interview_id: t for t in transcripts}
        sources = sorted(snapshots.glob("snapshot-*.md"))
        if synthesis.exists():
            sources.append(synthesis)
        forced = None
        snap_dir = snapshots

    results: list[QuoteResult] = []
    for source in sources:
        results.extend(check_file(source, transcripts, by_id, snap_dir, forced_transcript=forced))

    report_name: str | None = None
    if args.no_report:
        print(render(results))
    else:
        report.write_text(render(results), encoding="utf-8")
        report_name = report.name

    print_tally(results, report_name)

    if args.strict and strict_violation(results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
