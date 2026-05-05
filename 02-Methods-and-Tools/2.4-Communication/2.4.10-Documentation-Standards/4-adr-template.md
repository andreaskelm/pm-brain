# Architecture Decision Record (ADR) Template

## Overview

Use this template when capturing an **architectural** decision — which database, which integration pattern, which service boundary, which library, which trade-off between two valid technical paths. ADRs are tightly scoped, engineering-internal, and live next to the code.

ADRs are **snapshots**, not living docs. Once approved, you don't rewrite them — you supersede them with a new ADR.

For framework-level guidance (when ADR vs Decision Record, taxonomy, philosophy), see [1-documentation-standards-framework.md](1-documentation-standards-framework.md). For quality assessment, see [5-documentation-standards-evaluation.md](5-documentation-standards-evaluation.md).

**Language guidance:** ADRs default to English. Code, APIs, and technologies are already in English; mixing prose around them creates friction for AI tooling and search. Metadata is always in English.

---

## ADR Template

The template below is designed for AI auto-fill. The inline `<!-- AI-FILL: ... -->` comments are instructions to the agent populating the template — they are NOT content for the final document and should be stripped when the ADR is finished.

```markdown
---
title: "ADR-NNNN: [Concise decision title — what was decided]"
doc-type: adr
status: proposed | accepted | deprecated | superseded
audience: engineering
owner: "[Name — single accountable person]"
decision-makers: ["Name 1", "Name 2"]
consulted: ["Name or role"]
informed: ["Name or role"]
created: YYYY-MM-DD
last-reviewed: YYYY-MM-DD
next-review: N/A  # ADRs are snapshots; supersede rather than update
language: en
system: "[System / service / repo this decision applies to]"
component: "[Component, layer, or domain]"
supersedes: "ADR-NNNN | none"
superseded-by: "ADR-NNNN | none"
related-adrs: ["ADR-NNNN"]
related-decisions: ["DR-NNNN"]
tags: [database, integration, security, performance, cost]
---

# ADR-NNNN: [Decision Title]

## Status

<!-- AI-FILL: One of proposed | accepted | deprecated | superseded.
     If superseded/deprecated, add one-line reason and link to successor. -->

[Status]

## Context

<!-- AI-FILL: 3–6 sentences. What system, what problem, what triggered
     this now? Include constraints (technical, time, team, budget) verbatim
     from input. Reference related docs by link, not duplication. -->

[Context]

## Decision Drivers

<!-- AI-FILL: 3–7 bullets. Specific, testable forces shaping the decision
     (latency, cost, team skill, security, time-to-market). No platitudes.
     If only one option was considered, flag it here. -->

- [Driver 1]
- [Driver 2]
- [Driver 3]

## Considered Options

<!-- AI-FILL: Minimum 2 options. If input names only one, ask the user
     "What else was considered, even briefly?" Each option needs pros, cons,
     effort (S/M/L/XL), and risk (low/medium/high) with a one-line rationale. -->

### Option 1: [Name]

**Description:** [What this option means concretely, 2–3 sentences]

- **Pros:** [Tied to drivers]
- **Cons:** [Tied to drivers]
- **Effort:** [S | M | L | XL]
- **Risk:** [low | medium | high — one-line rationale]

### Option 2: [Name]

[Same structure]

## Decision

<!-- AI-FILL: 1–3 sentences. State the decision unambiguously. Name the
     chosen option. No hedging. -->

We will [decision]. **Chosen option:** Option [N] — [Name].

## Rationale

<!-- AI-FILL: Why THIS option over the others? Tie back to Decision Drivers.
     Name the decisive factor. Address: which drivers this satisfies best,
     which trade-offs we're accepting, what we're betting on. -->

[Rationale]

## Consequences

### Positive

<!-- AI-FILL: 2–5 bullets — what gets better. Be concrete. -->

- [Positive consequence]

### Negative

<!-- AI-FILL: 2–5 bullets. MUST be non-empty. If input doesn't name a
     downside, ask: "What's the trade-off you're least happy about?" -->

- [Negative consequence]

### Neutral

<!-- AI-FILL: Optional. Side effects worth flagging that aren't clearly
     good or bad. Skip if nothing applies. -->

- [Neutral consequence]

## Validation

<!-- AI-FILL: How will we know this was correct? Concrete signals — not
     "we'll see how it goes." If input is silent, ask: "What's the first
     signal we'd be wrong?" -->

- **Success signal:** [What proves this worked]
- **Failure signal:** [What would cause us to supersede this ADR]
- **Review trigger:** [Concrete event, e.g. "Re-evaluate at 5K req/s"]

## Links and References

<!-- AI-FILL: Source docs, related ADRs, related DRs, external references. -->

- [Source: design doc / ticket / thread]
- [Related ADR-NNNN — one-line summary]
- [Related DR-NNNN — one-line summary]
```

---

## AI Auto-Fill Prompt

Paste this prompt into your agent along with the template above and the source material (design doc, transcript, PR description, ticket, chat thread).

```text
You are filling out an Architecture Decision Record (ADR) using the template above.

Rules:
1. Populate every section. If a field isn't covered by the source material,
   write "[TBD: <what's missing>]". Never invent.
2. Status defaults to "proposed" unless the source clearly states otherwise.
3. At least 2 options must appear. If only one is named, flag it in
   Decision Drivers and ask: "What else was considered, even briefly?"
4. Decision Drivers must be specific and testable, tied to source constraints.
5. Consequences → Negative must be non-empty. If silent, end your response
   with: "Question for owner: what's the trade-off you're least happy about?"
6. Quote source material verbatim for technical specifics (numbers, names).
7. Translate Danish to English for the body. Preserve original-language
   quotes inline if they're load-bearing.
8. Strip all <!-- AI-FILL: ... --> comments from the final output. They are
   instructions to you, not content.
9. Output a single Markdown document starting with the YAML frontmatter.
10. After drafting, run the Quick Quality Check self-check (next section
    below). Fix any red flags before returning. If a red flag requires user
    input, append the unresolved questions at the end of your response under
    "Questions for owner before this ADR can be accepted:".

Source material follows.
```

---

## Quick Quality Checks (run after auto-fill)

These checks are designed to run **automatically** — by the AI agent immediately after filling the template, or by a human reviewer in under 2 minutes. They catch the predictable failure modes of auto-filled ADRs (hedged decisions, empty Negative consequences, strawman alternatives, leftover scaffolding).

For comprehensive peer review, audits, or quality gates, use the full evaluation in [5-documentation-standards-evaluation.md](5-documentation-standards-evaluation.md) → **ADR-Specific Evaluation**.

### Red Flags (each one is a hard fail — fix before marking `accepted`)

❌ **Hedged decision** — Decision section uses "we will probably / leaning toward / planning to" instead of stating the choice
❌ **Empty Negative consequences** — Section is missing, blank, or only lists "none"
❌ **Single option** — Only one option in Considered Options, with no flag in Decision Drivers explaining why
❌ **Strawman alternative** — Alternatives are obviously bad on every dimension; no real trade-off was evaluated
❌ **Platitude drivers** — Decision Drivers like "we want it to be fast" or "scalable" without specific, testable thresholds
❌ **Restated rationale** — Rationale section just rephrases the Decision; doesn't tie back to drivers or name the decisive factor
❌ **Leftover scaffolding** — `[TBD: ...]` markers in critical fields (`owner`, `decision-makers`, `Decision`, `Rationale`) OR uncleaned `<!-- AI-FILL: -->` comments in the output
❌ **Vague validation** — "We'll see how it goes" / "monitor performance" instead of concrete success and failure signals
❌ **Wrong template** — Audience includes non-engineers, or the decision is product/business-level → should be a Decision Record, not an ADR
❌ **Title is a noun phrase** — "Database choice" or "Auth approach" instead of "Use X for Y" / "Adopt X" / "Replace X with Y"

### Green Flags (signals the ADR is doing its job)

✅ **Decision is one declarative sentence** — Names the chosen option, no hedging
✅ **Drivers tie to specific numbers or constraints** — Latency thresholds, cost ceilings, named team skills, deadline dates
✅ **At least 2 real options** — Each with pros/cons that connect to drivers, plus effort and risk sized
✅ **Negative consequences are concrete** — Specific failure modes, not generic "added complexity"
✅ **Validation has measurable success AND failure signals** — Both, not just success
✅ **Source material is linked** — Design doc, ticket, or thread is referenced
✅ **Rationale names the decisive driver** — "The deciding factor was X because Y"

### AI Self-Check Prompt (run after auto-fill, before returning ADR)

After populating the template using the auto-fill prompt above, run this self-check **before returning the ADR to the user**. If any red flag is present, fix it or escalate to the user with a specific question.

```text
You have just auto-filled an ADR. Before returning it, run this self-check:

1. Is the Decision section a single declarative sentence naming the chosen option,
   with no hedging language ("probably", "leaning toward", "planning to")?
2. Is the Negative consequences section non-empty and concrete (not "added
   complexity" or generic platitudes)?
3. Are there at least 2 real options in Considered Options, with each option
   having pros and cons tied to the Decision Drivers — OR is the single-option
   case explicitly flagged in Decision Drivers?
4. Are the Decision Drivers specific and testable (numbers, named constraints,
   thresholds), not platitudes ("fast", "scalable", "robust")?
5. Does the Rationale name the decisive driver and tie back to drivers, rather
   than just restating the Decision?
6. Is Validation populated with BOTH a concrete success signal AND a concrete
   failure signal — not "we'll monitor"?
7. Are there any leftover `[TBD: ...]` markers in critical fields (owner,
   decision-makers, Decision, Rationale)? Critical fields cannot be TBD.
8. Are there any leftover `<!-- AI-FILL: ... -->` HTML comments in the output?
   They must be removed.
9. Is the title a verb phrase ("Use X for Y", "Adopt X", "Replace X with Y"),
   not a noun phrase ("Database choice")?
10. Is the audience engineering-only? If non-engineers are in the audience, this
    should be a Decision Record (DR), not an ADR — flag this to the user.

For each red flag found:
- If it can be fixed from existing source material, fix it.
- If it requires user input (e.g., empty Negative consequences with no source
  material to draw from), append a question block to your response:
    "Before this ADR can be marked accepted, please answer:
     - [Specific question per red flag]"
- Do NOT silently return an ADR with red flags present.
```

---

## How to Use This Template

### Numbering

Use `ADR-NNNN` (zero-padded, sequential per repo). Numbers are never reused — superseded ADRs keep their number.

### Status Lifecycle

`proposed` → `accepted` → (`deprecated` or `superseded`). Don't edit the body of an ADR after `accepted`. The only fields that change post-acceptance are `status` and `superseded-by`.

### Superseding an ADR

1. Create a new ADR with the next number.
2. Set the new ADR's `supersedes` to the old number.
3. Set the old ADR's `status` to `superseded` and `superseded-by` to the new number.
4. Both stay in the repo. The chain is the history.

### When to Use This vs. the Decision Record Template

Use this ADR template for **engineering-internal architectural choices** (database, integration pattern, library, service boundary). Use [2-decision-record-template.md](2-decision-record-template.md) for **product or cross-cutting decisions** where the audience includes non-engineers. Full distinction in [1-documentation-standards-framework.md](1-documentation-standards-framework.md).

---

## Links

- [Documentation Standards Framework](1-documentation-standards-framework.md) — when to use ADR vs DR, taxonomy, philosophy
- [Decision Record Template](2-decision-record-template.md) — for product/cross-cutting decisions
- [Architecture/Technical Template](3-architecture-technical-template.md) — for documenting how a system works
- [Documentation Evaluation](5-documentation-standards-evaluation.md) — quality assessment
