---
name: weekly-review
description: Plan or close the week using PM cadence rituals, draft the weekly note (YYYY-Www.md), resolve due decisions, and run the Friday drift sweep across decisions, live assumptions, initiatives, and context. Use when the user says "weekly review", "plan my week", "Friday wrap", "drift sweep", or invokes week planning.
---

# Weekly review

Week-over-week execution only compounds if someone closes the loop: what shipped, what you believed, what drifted. The agent **drafts**; the user owns honesty — especially "what am I avoiding?" Never fill that in for them.

**Cadence reference:** `2-Methods/4-Execution/1-Daily-Execution-And-Rituals/2-weekly-cadence.md` (Monday plan, Wednesday check, Friday close).

## Step 0 — Which moment is this?

Ask or infer:

- **Monday** — last-week retro, this-week priorities, team sync sketch, calendar gardening (~60 min).
- **Wednesday** — progress vs week goal, course correct, team pulse (~30 min).
- **Friday** — retrospective, **drift sweep**, stakeholder update draft, prep next week (~55 min); **draft the weekly note**.

If they only want one slice, do that slice. Friday close should include drift sweep + weekly note unless they explicitly skip.

## Step 1 — Load context

Read as needed:

- `5-Growth/weekly/` — prior note(s), especially **live assumptions**
- `5-Growth/decisions.md` — open rows, resolve-by dates, reopen triggers
- This week's threads and `3-Work/[initiative]/` (decisions, status)
- `1-Context/` if strategy or stakeholder context may have shifted

Use current ISO week for the filename: `5-Growth/weekly/YYYY-Www.md` per `5-Growth/weekly/README.md`.

## Step 2 — Monday output (when planning)

Produce:

- **Week theme** — one line.
- **Primary goal** — the ONE thing that must happen.
- **Key deliverables** — due day, owner if known.
- **Meetings / decisions** — outcome wanted, not just calendar.
- **Stakeholder commitments** — what you promised / what they expect.
- **Watch items** — risks, dependencies.
- **Success criteria** — measurable by Friday.
- **Focus blocks** — 2–3 protected slots if they want calendar gardening.

Pull language from cadence doc templates; keep it their words where possible.

## Step 3 — Wednesday output (when mid-week)

- Week goal status: on track / at risk / behind.
- Deliverable checklist with done / in progress / blocked.
- Blockers + one concrete unblock action each.
- If at risk: scope cut, deadline push, or help — pick one, don't list options forever.
- Team pulse: morale, wins, course correction (brief).

## Step 4 — Friday retrospective (before drift)

Draft retro sections:

- **Shipped** — changed in the world, not activity.
- **Learned** — what worked / didn't.
- **Second-order** — predictions to check later (with confidence); surprises missed.
- **Carried over** — what moves and why.
- **Metrics** — only if they track weekly; don't invent numbers.
- **Next week preview** — one focus, one decision coming.

Optional: **"PM Brain This Week"** block — used / frustrated / missing / one small action (repo + agent feedback).

## Step 5 — Friday drift sweep (~10 min)

Brain-wide scan before the weekly note is final. Detail checklist: [references/drift-sweep.md](references/drift-sweep.md).

**Scan**

- `5-Growth/decisions.md` — unresolved past resolve-by; reopen triggers that may have fired this week
- Last weekly note — **live assumptions** table
- Relevant `3-Work/[initiative]/` decision files
- `1-Context/` and new `4-Research/` or initiative research if beliefs or strategy shifted

**Flag (3–5 bullets max)**

1. **Fired reopen triggers** — stored "what would change my mind" conditions new evidence may satisfy
2. **Stale beliefs** — live assumptions unchallenged 3+ weeks; forecasts/decisions not revisited 6+ weeks
3. **Contradictions** — this week's signals vs prior logged decisions or forecasts
4. **Weak evidence** — load-bearing claims on verbal/hunch/industry only where documented was expected

**Output:** what's solid, what needs revisiting, **one recommended action**. Route findings into the weekly note **Drift sweep** section.

## Step 6 — Draft `YYYY-Www.md`

Use the template in `5-Growth/weekly/README.md`:

- Shipped / moved
- Decisions (new in decisions.md, resolved this week)
- Live assumptions (3–5 max; evidence tier; last challenged; what would change my mind)
- Drift sweep (from step 5)
- What I learned
- **What am I avoiding?** — leave blank or prompt the user; do not answer for them
- Next week — one focus, one decision coming

Skip creating a file if nothing happened and they prefer a thin week — offer a minimal note instead of a stuffed template.

## Step 7 — decisions.md hygiene

Offer explicitly:

- **Resolve** rows past resolve-by — outcome, surprise, link to weekly note
- **Add** new decisions from the week with confidence + reopen trigger
- **Update** live assumptions table when drift sweep fired a belief

User confirms before writing to `5-Growth/decisions.md`.

## Org reality

- **No Friday bandwidth.** Drift sweep alone is still worth 10 minutes; ship 3 bullets, not a novel.
- **Fake weekly syncs.** The note is for *them*; stakeholder update can be shorter than the internal retro.
- **Assumptions rot in slides.** Live assumptions in the weekly file beat a strategy deck nobody updates.
- **Agent drafts ≠ truth.** They correct shipped list and metrics; you don't argue.

## References

- `5-Growth/weekly/README.md` — note template and ownership
- `2-Methods/4-Execution/1-Daily-Execution-And-Rituals/2-weekly-cadence.md` — full ritual scripts
- [references/drift-sweep.md](references/drift-sweep.md) — drift sweep checklist
