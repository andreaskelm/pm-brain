# Decision Records and ADRs

Write one when someone will ask "why did we do it this way?" in six months. Not for every call: a mountain of unmaintained records is worse than ten good ones. A decision record is a **snapshot**. It captures what was true and what was decided at the time. When the world changes, you don't edit it; you write a new one that supersedes it, and the chain becomes the history.

**DR or ADR?** Audience includes non-engineers, or the decision is about what to build or why → decision record. Engineering-only and about how the system is built (database, integration pattern, library, service boundary) → ADR, kept next to the code. When in doubt and it affects code architecture, ADR.

## Lightweight decision record

```markdown
# DR-[NNNN]: [Verb phrase: "Adopt usage-based pricing for API tier", not "Pricing model"]

**Status:** draft | approved | superseded by DR-[NNNN]   **Date:** [ ]
**Decision maker:** [one name]   **Consulted:** [names]   **Informed:** [names]
**Source:** [one-pager / PRD / thread / meeting notes]

## Context
[3–6 sentences: what situation forced this, which users/system/team, why now.
Enough for someone who wasn't there.]

## Decision
We will [one declarative sentence, no "probably" or "leaning toward"].

## Alternatives considered
- **[A]:** [what it is] · Pros: [ ] · Cons: [ ] · Rejected because: [tied to a constraint]
- **[B]:** [same]

## Rationale
The deciding factor was [X] because [Y]. We're accepting [trade-off] in exchange for [benefit].

## Consequences
- **Expected:** [checkable in six months: "support tickets on billing drop below 50/month"]
- **Risks and trade-offs:** [never empty: what we give up, what we're betting on]
- **Reopen if:** [signal that would make us revisit]
```

Rationale is the section people come back for. "We chose A because A is better" is a conclusion, not reasoning. Three to five bullets per alternative is the sweet spot: one line is too thin to show why it lost, a page each is too much.

## ADR (engineering-internal)

```markdown
# ADR-[NNNN]: [Use X for Y / Replace X with Y]

**Status:** proposed | accepted | deprecated | superseded by ADR-[NNNN]
**System / component:** [ ]   **Owner:** [ ]   **Deciders:** [ ]   **Date:** [ ]

## Context
[System, problem, trigger, constraints: technical, time, team, budget]

## Decision drivers
- [Specific and testable: "p95 under 200 ms at 5K req/s", not "fast"]

## Considered options
### [Option 1]
[2–3 sentences] · Pros/cons tied to drivers · Effort: S/M/L/XL · Risk: low/med/high, because [ ]
### [Option 2]
[same]

## Decision
We will [decision]. Chosen: [option].

## Rationale
[Which drivers this satisfies best, the decisive one, what we're betting on]

## Consequences
- **Positive:** [ ]
- **Negative:** [never empty]

## Validation
- **Success signal:** [ ]   **Failure signal:** [what would make us supersede this]
- **Review trigger:** [e.g. "re-evaluate at 5K req/s"]
```

Once accepted, only the status and superseded-by fields change. Numbers are never reused.

## Quality flags (check before marking approved or accepted)

- **Hedged decision** — "we will probably…"; rewrite as one declarative sentence
- **Single option** — or strawman alternatives that lose on every dimension; ask "what else was considered, even briefly?" If there genuinely was only one viable option, say why
- **Empty risks or negative consequences** — ask "what's the trade-off you're least happy about?"
- **Restated rationale** — doesn't name the decisive factor or what's being given up
- **Uncheckable outcomes** — "better alignment" can't be verified in six months
- **Platitude drivers** — "scalable", "robust" without thresholds (ADR)
- **No named decision maker** — or `[TBD]` left in decision maker, decision or rationale
- **Two decisions tangled** — the rationale keeps switching subjects; split it
- **Noun-phrase title** — "Vendor choice" instead of "Use Stripe for EU invoicing"

When filling from a transcript or thread: quote commitments, numbers and names verbatim, mark anything missing as `[TBD: …]` instead of inventing it, and end with the open questions for the owner.
