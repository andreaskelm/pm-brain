# Scenario 08 — Transcript to Snapshot

Two turns. Turn 1: a transcript pasted with "make me the snapshot". The coach should ask for the user's read first (braindump, CDH step 0) and write nothing yet. Turn 2: the user's read, plus a save path. The snapshot should follow the Continuous Discovery template, keep quotes verbatim, and handle the seeded traps: an interviewer-led framing the participant hedged, a forecast, a "not started yet", an off-record request, an `[inaudible]` word, and the user's own hypothesis that the participant never said.

**Why it exists:** the real transcript workflow was once run on a lower-tier model, which invented its own template, per-interview quote ledgers and a claim register, and let hedges and analyst labels drift into quotes. This is the regression guard for that.

**Checks:** turn 1 — questions asked, no file in `3-Work/`. Turn 2 — snapshot created; every quote in it appears verbatim in the transcript (deterministic, via `verify-quotes.py` logic); no new template/ledger/register files; the LLM judge covers the traps that need reading.

**spec_owner on failure:** [discovery-synthesis](../../../../../.claude/skills/discovery-synthesis/SKILL.md); [AGENTS.md](../../../../../AGENTS.md) → Principle 6 and Principle 4
