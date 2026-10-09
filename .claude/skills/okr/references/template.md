# OKR Templates

Four formats. The **objective canvas** for one objective you need to explain to stakeholders, **team OKRs** as the rolling page the team works from, the **weekly check-in** for the 20-minute review, and a **measurement plan** for any KR whose number nobody can find yet. Keep the whole thing to 1–2 pages.

## Objective canvas (one page)

```markdown
# Objective Canvas — O[#] — [YYYY-QN or Rolling]

- **Objective (O#):** [qualitative, outcome-focused; would still make sense if the planned feature got cancelled]
- **Type:** Impact | Enabler (if enabler: the impact it unlocks)
- **Why now:** [what changed; evidence and its tier]
- **Business link:** [KR → team metric → company metric]
- **Owner(s):** [PM | Eng | Data]
- **Stakeholders:** [Risk, Ops, Design, Sales, …]

## Key results (2–4)
1. O#-KR1: [metric] from [baseline] to [target] by [date] (threshold: [minimum])
2. O#-KR2: [metric] from [baseline] to [target] by [date] (threshold: [minimum])
3. O#-KR3: [assumption test]: [method], pass if [threshold], by [date]

## Telemetry & guardrails
- Events/IDs: [source, definition, dashboard]
- Guardrails: [what must not get worse: latency, error rate, cost, CSAT, compliance]

## Dependencies & risks
- Dependencies: [team, owner, by when]
- Risks & mitigations: [top 2–3, including "what if we're wrong about what moves this metric"]

## Decision points
- Mid-cycle: [criteria for double down / pivot / stop]
- Rollback / kill switch: [how]

## The bet (for your own records)
- Confidence that hitting these KRs moves the strategy metric: [%]
- Riskiest assumption + evidence tier: [ ]
- Reopen trigger: [observable signal]
```

## Team OKRs (rolling)

```markdown
# Team OKRs — [Team] — [Cycle]

## Context
- Strategy link: [doc]
- Constraints: [timeline, people, compliance]
- Not now: [objectives we considered and parked, and why]

## O1: [title]  (Impact | Enabler)
- Owner(s): [names]
- O1-KR1: [metric] from [baseline] to [target] by [date] (threshold: …), source: [dashboard]
- O1-KR2: …
- Initiatives contributing: [initiative → KR IDs]
- Evidence: [opportunity, research, PRD]

## O2: [title]
- …

## Cadence & dashboards
- Weekly check-in: [day, time, who]
- Dashboards: [links]

## Decision log (rolling)
| Date | Decision | Evidence | Owner |
|---|---|---|---|
```

## Weekly check-in

```markdown
## OKR Check-in — Week [N]

- O1-KR1: [value vs. target] · confidence [0/1/2] · evidence: [what we saw] · next: [action]
- O1-KR2: …
- O2-KR1: …
- Risks / asks: [what we need, from whom]
- Blockers / dependencies: [owner, date]
- Decisions this week: [anything material → decision log]
```

## KR measurement plan (when the number doesn't exist yet)

```markdown
### O#-KR# — [metric name]

- **Definition:** [exactly what's counted, and what isn't]
- **Source:** [system/event] · **Collection:** [how] · **Frequency:** [how often]
- **Dashboard:** [where] · **Refresh:** [how often]
- **Baseline:** [value, date measured]
- **Target:** [aspirational] · **Threshold:** [minimum that counts as a pass] · **Red line:** [triggers intervention]
```

Example: *Internal-user NPS for the settlement system. Monthly survey, last week of each month. Target 70% promoters, threshold 65%, red line below 50%.*
