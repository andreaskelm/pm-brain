---
name: discovery-synthesis
description: Plan customer discovery, turn interview snapshots into synthesis and evidence-based opportunities, build or update an Opportunity Solution Tree, map jobs and segments, and design RAT tests for the riskiest assumption. Use when the user says "synthesize interviews", "what did we learn from research", "turn notes into opportunities", "opportunity solution tree", "OST", "affinity map", "patterns from users", "cluster job stories", "segment by job", "test our riskiest assumption", "design a fake door", "plan user interviews", "interview guide", "save research artifacts", or has raw transcripts/notes and needs structured insight—not a PRD yet. Runs preflight before any template. For go/no-go on a specific bet, route to opportunity-assessment; this skill is learning and structure.
---

# Discovery synthesis

Discovery synthesis is the work between "we talked to people" and "we know what to build." The failure mode I see most isn't bad note-taking—it's synthesis that confirms what you already believed, or opportunities that are really feature requests wearing a costume. So the thinking comes first; snapshots, synthesis docs, and trees are where it lands.

**This skill is for:** turning research into durable artifacts (snapshots, synthesis, opportunities, OST, job/segment docs, validation plans).

**Route elsewhere when:**
- The question is "should we pursue this?" with a kill/go call → `opportunity-assessment` skill.
- The problem is validated and you need requirements → `write-prd` skill.
- The question is ranking a backlog → `prioritize` skill.

## Is synthesis the right move?

**Yes when** you have (or will soon have) customer evidence, decisions are blocked on "what users actually do," or stakeholders need a shared map of outcomes → opportunities → tests.

**Not yet when** you only have an idea and no learning plan—start with preflight and an interview plan. **Overkill when** a sub-week experiment suffices—use a one-page validation note (see [validation](references/validation.md)).

Before asking questions, check the repo: `4-Research/`, `3-Work/[initiative]/research/`, existing snapshots/synthesis, `1-Context/`. Quote what's already there; don't re-interview the user for written facts.

## Step 1 — Preflight (always)

Pick 2–3 for what's missing:

- **What decision will this research unblock?** If "general learning," narrow it—or you'll drown in notes.
- **Who exactly?** Segment, role, situation—not "users."
- **What do you know vs. guess?** Name evidence tier on load-bearing claims: documented (snapshots) > verbal (Sales) > hunch.
- **What would disconfirm your current story?** One uncomfortable hypothesis to hunt for in interviews.
- **Where will artifacts live?** Initiative-specific → `3-Work/[initiative]/research/`; reusable → `4-Research/` (analysis in repo; raw transcripts external with links).

If they've braindumped in chat or an initiative folder, one confirming question is enough. If they insist on skipping: one-sentence risk, then draft with `[GAP: …]`—never invent quotes or interview counts.

## Step 2 — Route to the right reference

| Situation | Reference |
|-----------|-----------|
| Plan or debrief interviews; biases; question types | [interviews](references/interviews.md) |
| Snapshot → synthesis → opportunities; weekly cadence | [continuous-discovery](references/continuous-discovery.md) |
| Job stories, forces, ODI outcomes, job files | [jtbd](references/jtbd.md) |
| Double Diamond, OST, HMW, problem vs solution | [problem-solution](references/problem-solution.md) |
| Hypotheses, RAT, experiments, thresholds | [validation](references/validation.md) |
| Job-based segments + personas (execution) | [segmentation-personas](references/segmentation-personas.md) |
| PMF survey, retention, scale vs iterate | [pmf](references/pmf.md) |

Default path for messy qualitative data: **interviews** → **continuous-discovery** → **problem-solution** (OST) → **validation** for the riskiest assumption.

## Step 3 — Three common flows

### Flow A — Plan interviews (before the calls)

1. Lock one primary research question and who qualifies.
2. Draft a guide: past behavior, stories, jobs—not hypotheticals or pitches ([interviews](references/interviews.md)).
3. Plan outputs: snapshot per participant within 24h; link to external recording/transcript.
4. Name the assumption you'll try to falsify in this batch.

### Flow B — Snapshots → synthesis → opportunities → OST

1. **Snapshots:** behavioral stories with quotes; resist generalizations ([continuous-discovery](references/continuous-discovery.md)).
2. **Synthesis:** patterns with evidence strength (3+ independent stories = stronger); include disconfirming evidence.
3. **Opportunities:** customer-need framing ("How might we…"), not solutions; multiple customers per opportunity.
4. **OST:** one measurable outcome → opportunity branches → 3+ solutions per target opportunity → experiments on riskiest assumptions ([problem-solution](references/problem-solution.md)).
5. Optional: cluster jobs into segments before over-building personas ([segmentation-personas](references/segmentation-personas.md)).

Push back if they skip synthesis with "we already know"—ask what would change their mind.

### Flow C — Test the riskiest assumption (RAT)

1. List assumptions across desirability, usability, feasibility, viability ([validation](references/validation.md)).
2. Pick the one that kills the initiative if wrong—not the easiest to test.
3. Pre-register metric, threshold, sample, duration; prefer revealed behavior over stated intent.
4. Decide proceed / pivot / re-test / stop; link results back to the OST experiment node or opportunity doc.

## Step 4 — Red flags as artifacts take shape

- **Solution-first opportunities** ("need AI dashboard")—reframe to need or mark as unvalidated solution idea.
- **Single-interview patterns** treated as truth—label evidence weak; plan more interviews.
- **Hypothetical quotes** or "users would love"—strip or replace with past-behavior stories.
- **No outcome on the OST**—outputs disguised as outcomes ("ship onboarding v2").
- **Synthesis without decisions**—every synthesis should end with "so we will / won't / need to learn X."
- **Personas before segments**—demographic cardboard; segment by job first ([segmentation-personas](references/segmentation-personas.md)).
- **Validation theater**—tests without thresholds, or building to learn what a fake door could answer.
- **Research hoarding**—insights only in chat; insist on saving analysis to `4-Research/` or initiative `research/`.

Name the flag, one question, suggested fix—don't silently "fix" their thinking.

## Step 5 — Before calling it done

- **Save paths:** Analysis markdown in `4-Research/` (e.g. `1-User-Interviews/snapshots|synthesis|opportunities/`) or `3-Work/[initiative]/research/`; raw data external with links in the analysis doc (see `4-Research/README.md`).
- **Gut check:** "If a skeptical eng read only the synthesis, what would they say is still guesswork?"
- **Log the bet:** If they stated confidence in an opportunity or segment choice, offer a row in `5-Growth/decisions.md` with a reopen trigger (e.g. "three interviews contradict pattern X").
- **Altitude check:** Findings that change who you serve, company strategy, or OKRs—flag for `1-Context/` or initiative `decisions.md`, don't bury in interview footnotes.
- **Handoff:** Strong opportunity + validation → `opportunity-assessment` or `write-prd`; ranking many bets → `prioritize`.

## Org reality

- **No time for weekly interviews.** Honest minimum: batch 5–8 focused interviews, synthesize anyway—don't pretend continuous discovery without cadence.
- **Research as theater.** Stakeholders want a report to bless a roadmap already chosen. Still write synthesis with evidence tiers; separate "what customers said" from "what we're doing anyway."
- **PM-only interviews.** Name the cost: shared understanding suffers. Offer trio synthesis session or shared snapshot template.
- **"Just send a survey."** Surveys supplement stories; they rarely replace switch/context interviews for new problems.
- **Legal won't let you talk to customers.** Proxy evidence (support logs, sales calls, churn interviews)—label tier; plan the smallest compliant customer touch.

## References

- [references/interviews.md](references/interviews.md) — planning, conducting, debriefing interviews
- [references/continuous-discovery.md](references/continuous-discovery.md) — snapshots, synthesis, opportunities
- [references/jtbd.md](references/jtbd.md) — jobs, forces, outcomes, job files
- [references/problem-solution.md](references/problem-solution.md) — Double Diamond, OST, HMW, divergence/convergence
- [references/validation.md](references/validation.md) — RAT, experiments, evidence strength
- [references/segmentation-personas.md](references/segmentation-personas.md) — job-based segments, personas for execution
- [references/pmf.md](references/pmf.md) — PMF signals, survey, retention, scale vs iterate
