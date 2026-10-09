# Engineering and Design Handoff

Use as a prep checklist and meeting agenda. Copy sections into the initiative folder or PRD appendix — don't duplicate the whole PRD.

## What engineering needs (minimum viable clarity)

| Input | PM provides | Good enough looks like |
|---|---|---|
| Problem / outcome | Who struggles, what changes, why now | Two sentences a new engineer understands |
| Scope slice | In / out for this milestone | Bulleted non-goals, not vague "phase 2" |
| Constraints | Legal, perf, platforms, data, SLAs | Explicit "must" vs "nice" |
| Metrics | Primary, guardrails, instrumentation | Event names or dashboard links in repo |
| Decisions | What's locked vs open | Dated decision log entries |
| Rollout | Flags, %, rollback, on-call | Owner named for kill switch |
| Acceptance | Behavioural done, not ticket closed | Testable criteria eng agrees to |

**Ask eng to return:** estimate range + assumptions, top 3 risks, spike list with time boxes, dependencies, operational load (alerts, runbooks, support).

## What design needs (minimum viable clarity)

| Input | PM provides | Good enough looks like |
|---|---|---|
| Job and segment | Situation, frequency, stakes | Not "all users" |
| Constraints | A11y target, platforms, content | WCAG level or explicit exception |
| Business rules | Permissions, pricing, edge cases | Listed even if "eng handles" |
| Success signal | What behaviour proves the design worked | Tied to primary metric |
| Learning appetite | What can ship rough vs must polish pre-launch | Stops infinite polish |

**Ask design to return:** primary flow + error states, prototype plan for riskiest interaction, design system impact, open questions before build starts.

## Tech debt framing (intentional loan)

Use this table in negotiation — fill it before asking eng to "just ship it."

```markdown
## Tech debt decision — [short title]

**Loan taken:** [what we're deferring — refactor, tests, migration, monitoring]
**Benefit now:** [speed, learning, revenue, unblock — be specific]
**Cost later:** [incidents, slower delivery, migration scope — honest range]
**Repay trigger:** [date / metric / next initiative / incident threshold]
**Sponsor:** [EM/PM who agreed]
**Review date:** [when we revisit]
```

If repay trigger is "when we have time", call that out as unmanaged debt — sometimes acceptable, never free.

## Negotiation scripts (adapt, don't recite)

**Scope vs date**
- "The date looks fixed. Which slice still proves [hypothesis] if we cut [area]?"
- "What would you need to believe to call this a two-week spike instead of a quarter project?"

**Feasibility pushback**
- "What's the smallest experiment that retires the biggest unknown?"
- "If we had to fake it manually for ten customers, what would we learn before we build?"

**Design vs eng tension**
- "We're optimizing for [learning / risk / parity]. Given that, which compromise hurts users least?"
- "Can we ship design A behind a flag while we build infra for design B?"

**Stakeholder scope creep**
- "We can add [X] if we drop [Y] or move the date. Which trade does [stakeholder] actually care about?"
- "Parity with [competitor] is a outcome or a checklist? Help me separate must-haves."

**Saying no to debt repayment**
- "I hear the cost. We're consciously delaying because [reason]. Trigger to revisit is [signal]."

**After a vague yes**
- "Can you say that back as assumptions — what has to be true for that estimate?"

## Handoff meeting agenda (45–60 min)

1. **Problem and bet** (5 min) — PM, not slide reading
2. **Scope in/out** (10 min) — argue here, not in sprint planning
3. **Risks and spikes** (10 min) — eng leads, PM captures owners
4. **UX critical path** (10 min) — design walks risky states
5. **Metrics and rollout** (5 min) — guardrails explicit
6. **Asks and dates** (10 min) — estimate, reviews, first milestone
7. **Recap in writing** (5 min) — who sends notes, where they live in repo

## Async handoff packet (when the room is scarce)

Send in one thread or doc section:

- Link to PRD or one-pager
- Decision log since last sync
- Open questions tagged **eng** / **design** / **PM**
- Proposed slice and non-goals
- Request: comments by [date], then 20-min sync only on conflicts

## Post-handoff (first 48 hours)

- Eng: estimate or spike plan committed
- Design: review scheduled or wireframes shared
- PM: update PRD with resolved open questions; no silent scope adds from Slack side quests
