# Team Strategy Doc: Pillars and Non-Goals

The format teams actually plan against for 1–2 years: 3–5 strategic pillars (where we focus), explicit non-goals (where we won't), the evidence behind each, and a winning aspiration. It sits between the vision and the roadmap. Run the kernel check on it before it ships: the Context section is your diagnosis, the pillars and non-goals are the guiding policy, and the initiatives under each pillar are the actions.

**Pillars must be choice-shaped, not function-shaped.** "Improve the mobile experience" is a department. "Make advanced features discoverable so users reach the value they're paying for" is a choice.

## Template

```markdown
# [Team/Product] Strategy — [period, e.g. 2026–2027]

## Executive summary (one page; the only part most people read)
**Why we wrote this:** [catalyst: circular roadmap debates, a plateau, a competitor move]
**Pillars:** over the next [period] we focus on:
1. **[Pillar]** — [one sentence on what it means]
2. **[Pillar]** — [ ]
3. **[Pillar]** — [ ]
**Winning aspiration:** by [date]: "[the headline a journalist would write if this works]"
**Bottom line:** this will [business outcome] by [mechanism]. Leading signal by [date]: [ ]. Lagging result by [date]: [ ].
**What changes:** product teams [ ] · engineering [ ] · leadership tracks [ ]

## Context / why now (the diagnosis)
[Current situation with numbers. What research, data and leadership interviews converged on. Market dynamics creating urgency. The hard problem, stated plainly.]

## Pillar: [name]
**What it means:** [ ]
**In scope:** [ ]   **Out of scope:** [ ]
**Why it matters:** user impact [ ] · business impact [ ] · our unfair advantage here [ ]
**Evidence:** [data, research, support analysis; name the strength]
**Success in [period]:** [behavior change we'll see]
**Metrics:** primary [ ] · secondary [ ] · guardrail (what must not get worse) [ ] · baseline → target [ ]
**What would have to be true:** [key assumptions]
**Risks:** [risk] · mitigation [ ] · early warning signal [ ]
**Illustrative concepts:** [1–2 sketches that make the pillar tangible; not specs]

## Non-goals
| Non-goal | Why not now | What we'll stop doing |
|---|---|---|
| [area someone will ask for] | [reason tied to the diagnosis] | [named project or request type] |

## Dependencies and risks across pillars
[Cross-functional, external, hiring/budget, platform. Owners.]

## How we'll use this
**Before starting any initiative:** which pillar does it support? How will we measure it? What assumption does it test? What does it displace?
**Off-strategy requests:** [who decides, how to escalate]
**Review:** [cadence; what would reopen a pillar]
```

**Non-goals are the section that does the work.** A good one is something a reasonable person in the org wants: "No price-matching projects against cheaper competitors; our differentiation is depth, not cost." A bad one is something nobody was going to do anyway.

## Pillar scorecard (when choosing pillars from a longer list)

Cluster the problems you found into 8–12 opportunity areas, flip each into an opportunity ("users can't find features" → "Discovery & Findability"), then score each 1–5 on four dimensions. Score individually first, then discuss the 2+ point gaps; the disagreements are where the hidden assumptions live.

| Dimension | 5 looks like | 1 looks like |
|---|---|---|
| **Expected impact** | Most users, daily, high pain or value | Very few users, rarely, minor |
| **Certainty of impact** | Research, usage data and customer feedback all point the same way | Mostly speculation or anecdotes |
| **Clarity of levers** | Clear path forward, team agrees on the approach | Problem is clear, solutions are a mystery |
| **Uniqueness of levers** | Structural advantage competitors can't easily copy (data, brand, network, talent) | Playing catch-up |

Uniqueness is the dimension teams skip, and it's the one that separates a strategy from a to-do list. A pillar that scores 5/5/5/1 is real work, but you'll win it only if you out-execute everyone, so say that out loud.

| Opportunity area | Impact | Certainty | Clarity | Uniqueness | Total | Rationale |
|---|---|---|---|---|---|---|
| Discovery & Findability | 5 | 4 | 4 | 3 | 16 | 85% of users miss advanced features; design team is a real edge |
| Onboarding & Activation | 4 | 4 | 4 | 3 | 15 | 45% drop at onboarding step 3, confirmed in 8/10 interviews |
| Platform & Extensibility | 3 | 3 | 4 | 4 | 14 | Cited in 60% of lost enterprise deals |
| Performance & Reliability | 4 | 4 | 3 | 2 | 13 | Matters, but commoditized: hygiene, not a pillar |
| Advanced Analytics | 3 | 2 | 3 | 2 | 10 | Uncertain demand, competitors ahead |

The totals inform the choice; they don't make it. After ranking, ask: do the top 3–5 work together as a portfolio, and can we defend them to a skeptical stakeholder? Areas that score high but miss the cut (like Performance above) often belong in the doc as explicit non-goals or as baseline commitments, so nobody thinks they were forgotten.

## Quality checks before sharing

- **Clarity:** could someone outside the process explain why these pillars?
- **Defensibility:** is each rationale evidence-based, with trade-offs acknowledged?
- **Actionability:** can teams build roadmaps from it, and is it obvious what's NOT happening?
