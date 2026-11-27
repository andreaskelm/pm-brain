---
name: discovery-synthesis
description: Turn interview transcripts into snapshots, synthesize across interviews, build opportunities and an Opportunity Solution Tree, map jobs and segments, and test the riskiest assumption — by routing to the canonical Continuous Discovery files in 2-Methods/3-Discovery/. Use when the user pastes or files an interview transcript, or says "synthesize interviews", "make the snapshot", "what did we learn from research", "turn notes into opportunities", "opportunity solution tree", "OST", "patterns from users", "segment by job", "test our riskiest assumption", "plan user interviews", "interview guide", or has raw transcripts/notes and needs structured insight — not a PRD yet. Braindump before any template. For go/no-go on a specific bet, route to opportunity-assessment.
---

# Discovery synthesis

This skill is a **router, not a method**. The method lives in `2-Methods/3-Discovery/`. The skill's job is to detect what you're doing, get the thinking out of the user first, load the right canonical file, and keep the agent from inventing structure.

The failure modes I see most: synthesis that confirms what you already believed, opportunities that are feature requests in a costume, and — with transcripts — an agent that quietly rewrites what people said. A tidy quote nobody said is worse than no quote.

## Hard rules (every flow)

1. **Canonical file first.** If `2-Methods/3-Discovery/` has a template or procedure for the job, use it as written. Don't create a new template, ledger, register, codebook, or folder structure. If something truly doesn't fit, **leave that section out** (don't rewrite it) and say which. Inventing structure needs an explicit statement and the user's OK.
2. **Braindump before structure.** Transcript or notes arrive → ask the user for their read first (CDH snapshot Step 0): what stood out, what surprised them, what they expected to hear, what they'd say in two minutes. 2–3 questions, not a form. Never fill the user's debrief, nerves, or surprise for them — mark `[GAP: user]`.
3. **Quotes are verbatim.** Contiguous text from the transcript, original language, hedges kept, with the transcript line. Never stitch across turns or across a gap, never shorten so a hedge disappears, never clean up. Text from the interviewer's turn, the user's chat summary, or a recorder's AI summary is **not** the participant's evidence — say who introduced a framing and what the participant actually answered. Forecasts ("we will…", "I'd guess…") are not practice; label them.
4. **Mark damaged text.** Speech-to-text garbles words. Flag the load-bearing ones as `[ASR: audio first]` and never build a claim on a guessed word.
5. **Respect consent.** Off-record requests and naming conditions go in the follow-up section. Don't use off-record material without asking.
6. **Verify before done.** Run the quote check on every snapshot written: `python system/evals/checks/verify-quotes.py --snapshot <path> --strict`. Fix every not-found, stitched, or crosses-interviewer quote; repeat until clean. Quotes use `> "…" (L123)` so the checker finds them.
7. **One interview per snapshot.** No cross-interview comparison inside a snapshot — that's synthesis, and it contaminates how you read the next interview.

**Model tier.** Coding a transcript is judgment work. Run it at mid tier or above, never fast tier ([model tiers](../../../docs/platform-setup.md#model-tiers)). Mechanical parts (quote verification, link fixes, file moves) can go to a fast subagent — but verify the result.

## Route by situation

| Situation | Load |
|-----------|------|
| Plan or debrief interviews | `2-Methods/3-Discovery/1-Research-Interviews/1-interview-guide.md` |
| **Transcript pasted/filed → snapshot** | `2-Continuous-Discovery-Habits/1-create-interview-snapshot.md` (+ rules above) |
| Several snapshots → patterns | `2-Continuous-Discovery-Habits/2-synthesize-interview-snapshots.md` |
| Patterns → opportunities | `2-Continuous-Discovery-Habits/3-create-opportunities.md` |
| Opportunities → solutions, OST | `2-Continuous-Discovery-Habits/4-generate-solutions.md`, `6-Problem-Solution-Space/` |
| Jobs, forces, segments | `3-Jobs-To-Be-Done/`, `7-Segmentation/` |
| Test the riskiest assumption | `5-Idea-Validation/1-idea-validation.md` |
| PMF signals | `8-Product-Market-Fit/` |

Portable summaries only: [references/](references/). In PM Brain, load the canonical files.

**Check the initiative first.** `3-Work/[initiative]/research/README.md` may declare study-specific deltas (e.g. Produktland: an org study that stops at synthesis and leaves out the needs/opportunities sections). Follow the deltas; they adapt the canonical method, they don't replace it. Check `4-Research/`, existing snapshots and `1-Context/` before asking the user for written facts.

## Flow A — Transcript → snapshot

1. Confirm scope in one line (which interview, which study, where it saves).
2. Braindump (rule 2).
3. Say your plan in a few lines (CDH step 0): what you'll capture, what you'll leave out and why.
4. Extract **all** specific stories (situation, actions, outcome, emotion) — behavior over generalization. Tag evidence strength: story-specific, stated practice, general belief, forecast, rehearsed, prompted by the interviewer.
5. Write the snapshot from the CDH template. Omit sections that don't fit, per the initiative.
6. Verify quotes (rule 6). Fix, re-run.
7. Hand back: what's strong, what's weak, what you couldn't verify, and one question about the user's own read vs what the transcript holds.

## Flow B — Snapshots → synthesis → opportunities → OST

1. **Synthesis:** patterns with evidence strength (3+ independent stories = stronger); include disconfirming evidence and what was prompted.
2. **Opportunities:** customer-need framing ("How might we…"), not solutions; multiple customers per opportunity. Skip for studies that aren't product discovery.
3. **OST:** one measurable outcome → opportunity branches → 3+ solutions per target opportunity → experiments on the riskiest assumptions.
4. Push back if they skip synthesis with "we already know" — ask what would change their mind.

## Flow C — Test the riskiest assumption (RAT)

List assumptions across desirability, usability, feasibility, viability. Pick the one that kills the initiative if wrong — not the easiest to test. Pre-register metric, threshold, sample, duration; prefer revealed behavior over stated intent. Decide proceed / pivot / re-test / stop; link back to the OST node.

## Red flags

- **Solution-first opportunities** ("need an AI dashboard") — reframe to need.
- **Single-interview patterns** treated as truth — label weak; plan more interviews.
- **Generalizations and hypotheticals** presented as behavior — "we always…", "users would love…".
- **Output as outcome** — "ship onboarding v2" on the tree.
- **A claim with no number or result** presented as a change that worked — ask what moved.
- **Synthesis without decisions** — end with "so we will / won't / need to learn X."
- **Validation theater** — tests without thresholds.
- **Research hoarding** — insights only in chat; save to `4-Research/` or the initiative's `research/`.
- **The agent adding structure nobody asked for** — new template, register, ledger. Stop and ask.

Name the flag, one question, suggested fix — don't silently "fix" their thinking.

## Before calling it done

- Quotes verified (rule 6). Gaps marked `[GAP: …]` — never invent quotes, counts, or numbers.
- **Gut check:** "If a skeptical reader had only this snapshot, what would they say is still guesswork?"
- **Log the bet:** if the user stated confidence in a pattern, offer a row in `5-Growth/decisions.md` with a reopen trigger.
- **Altitude check:** findings that change strategy or who you serve → flag for `1-Context/` or the initiative's `decisions.md`.
- **Handoff:** strong opportunity + validation → `opportunity-assessment` or `write-prd`; ranking many bets → `prioritize`.

## Org reality

- **No time for weekly interviews.** Batch 5–8 focused interviews and synthesize anyway; don't pretend continuous discovery without cadence.
- **Research as theater.** If stakeholders want a report to bless a chosen roadmap, still write synthesis with evidence tiers; separate "what people said" from "what we're doing anyway."
- **PM-only interviews.** Name the cost: shared understanding suffers. Offer a trio synthesis session.
- **"Just send a survey."** Surveys supplement stories; they rarely replace them for new problems.

## References

[interviews](references/interviews.md) · [continuous-discovery](references/continuous-discovery.md) · [jtbd](references/jtbd.md) · [problem-solution](references/problem-solution.md) · [validation](references/validation.md) · [segmentation-personas](references/segmentation-personas.md) · [pmf](references/pmf.md)
