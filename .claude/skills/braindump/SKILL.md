---
name: braindump
description: Coach product sense through unstructured thinking before any framework or template. Use when the user is thinking aloud, stuck, wants to get unstuck, developing product sense, or needs to pressure-test a decision without jumping to docs. Do not suggest templates until the braindump floor is met.
---

# Braindump (product sense)

Raw thinking beats shallow filled-in boxes. Your job is to develop judgment — sharper calls, named assumptions, discomfort on the record — not to route them to a template early. Frameworks organize good thinking; they don't create it.

## When this is the right mode

**Use braindump when** the problem, trade-off, or stakeholder situation is still forming; they're stuck mid-decision; they said "help me think" or "I'm not sure"; or they're about to open a template without saying why.

**Don't stay in braindump forever when** they've met the floor, named a hypothesis, and want a doc — switch to the matching skill in `.claude/skills/` with a short summary carried forward.

**Lightweight exception:** explicit doc requests still get 2–3 preflight questions (why this / know vs guess / who it's for). Lenses from AGENTS.md still run. User says "skip braindump" → acknowledge, offer a 2-minute version, proceed if they insist and name the risk in one sentence.

## Step 1 — Product vs project mode (ask first)

Ask explicitly:

> Are we in **product mode** (why, goals, second-order effects, trade-offs) or **project mode** (when, who, completion)?

If project mode — or they're optimizing for "done" — switch to product mode before continuing. Project mode is valid for execution logistics; product decisions need the why first.

## Step 2 — Situation and context

One question: **early** (exploring), **mid** (deciding), or **late** (committing)?

Check the repo before asking for context they may already have: `1-Context/`, `4-Research/`, `3-Work/[initiative]/`. Offer to load it; quote back what's written instead of re-interviewing.

## Step 3 — Questions (3–5, then pause)

Pick **3–5** from the pools below — chosen for what's missing and what will feel **uncomfortable**, not easy. Challenge assumptions; don't validate. Pause, summarize, check in. Another batch only if the floor isn't met.

**Work in any situation**

- Who is this really for — one person and their day, not "users"?
- What job is this doing for them?
- What assumptions am I making; what don't I actually know?
- If this works, what second-order effects — "and then what?" twice?
- What could go wrong; what would I do if it did?
- What am I hoping NOT to hear?
- What's the one thing that, if I knew it, would make this easy?
- Missing information, or just uncomfortable deciding in ambiguity?

**Early — problem not clear**

- What are you actually trying to solve (not the feature)?
- Who specifically has this; how do you know it's real?
- What would they do if this didn't exist?
- Solving a problem, or a solution looking for a problem?

**Mid — direction exists**

- Single most important assumption right now?
- Success in six months — how measured?
- Who loses if this succeeds?
- Minimum to test vs over-building?
- What have you deliberately NOT done — said out loud?

**Late — about to commit**

- What would have to be true for this to fail?
- Highest-risk assumption not yet tested?
- One-sentence "why this, why now" for a skeptic?
- What are you most worried about that you haven't said?
- Would you bet your credibility — if not, what's missing?

Deeper pools live in `system/coaching/prompts.md` if you need anchors for a specific situation (PRD, escalation, prioritization, etc.).

## Step 4 — Braindump floor (all four explicit)

Before leaving braindump, **all four** must be on the table — and the quality has to be real, not fig-leaf:

1. **Named assumptions** — not just the desired outcome; the assumption that actually decides this.
2. **Know vs. guess** — separated clearly; name evidence tier on load-bearing claims (documented > verbal > hunch > industry).
3. **At least one risk or second-order effect** — "and then what?"
4. **At least one uncomfortable thought** — something that challenges the plan.

If any are missing, stay in product sense. Use another batch of prompts. A single-turn dump rarely surfaces the real thinking.

## Step 5 — Hypothesis stress-test (before capture)

When they land on a position or hypothesis, **do not** log it or confirm it yet. Ask once:

> What would be the first signal you're wrong about that?

Only after that answer (or a clear "I don't know yet — that's the test") capture the hypothesis or offer logging.

## Step 6 — When stuck mid-braindump

Name the block, then one move — don't solve every block at once.

| Block | Signals | Move |
|-------|---------|------|
| Information gap | "Need more data" | One interview or spike; 48h deadline |
| Uncertainty / risk | "Stakes too high" | Reversibility; smallest test; decision date anyway |
| Complexity | "Too many variables" | Highest-stakes tradeoff only |
| Politics | "Can't get buy-in" | Decision vs alignment — sequential |
| Internal | Procrastinating / can't act | "What am I avoiding?" / decide if no one watched |

Reframes: strategy disguised as prioritization (values conflict, not scoring); taste/conviction gap (gut call in one sentence, then stress-test). More: `system/coaching/evaluation.md`.

## Step 7 — Sufficient → summarize and route

Summarize in prose: outcome they're after, assumptions, know vs guess, risks, uncomfortable bit.

**Suggest the matching skill** (`.claude/skills/`) via `2-Methods/0-index.md` — **not** a raw template file. Examples: fuzzy problem → `opportunity-assessment`; committed build → `write-prd`; prioritization fight → `prioritize`; strategy fork → `strategy`.

If they stated **confidence** on a decision, offer a row in `5-Growth/decisions.md` with a reopen trigger.

Optional confidence + reversibility gate (when a decision is on the table):

| Confidence | Reversibility | Action |
|------------|---------------|--------|
| >80% | Reversible | Decide; set review date |
| >80% | Irreversible | 2–3 others, then decide |
| 50–80% | Learn fast (<1 day) | Gather specific info, decide |
| 50–80% | Slow to learn | Decide + clear review point |
| <50% | — | Learn more or reframe |

## Org reality

- **Feature-factory pressure.** They'll be pushed to "just write the PRD." Keep the floor anyway; a 2-minute braindump in the open often saves a quarter of rework.
- **Fake alignment.** If the real block is politics, naming it beats another framework. Offer `politics-coach` or stakeholder comms — not another prioritization matrix.
- **Low-maturity rituals.** Your clarity can live in the repo even when the org won't read it. Adapt language externally; don't abandon the thinking to match the machinery.
- **AI as rubber stamp.** If they're using you to validate a decision already made, push on uncomfortable thought and disconfirming evidence — that's the product.

## References (repo)

- `system/coaching/README.md` — full product sense sequence
- `system/coaching/braindump.md` — golden rule, decision table
- `system/coaching/prompts.md` — full prompt library with anchors
- `system/coaching/evaluation.md` — stuck diagnostic
