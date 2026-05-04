# Decision Record Template

## Overview

Use this template when a meaningful product or technical decision has been made and needs to be captured—the kind where someone will ask "why did we do it this way?" in 6 months.

Decision records are **snapshots**. They capture what was true and what was decided at a point in time. Don't update them when the world changes—create a new decision record that supersedes the old one.

**Language guidance:** Default to English. Use Danish only if the primary audience for this specific decision is exclusively Danish-speaking and will never need AI summarization or cross-referencing. Metadata should always be in English regardless of content language.

---

## Decision Record Template

The template below is designed for AI auto-fill. The inline `<!-- AI-FILL: ... -->` comments are instructions to the agent populating the template — they are NOT content for the final document and should be stripped when the DR is finished.

```markdown
---
title: "DR-NNNN: [Clear, descriptive title — what was decided]"
doc-type: decision-record
status: draft | review | approved | current | superseded
audience: [product-team | engineering | leadership | cross-team]
owner: "[Name — single accountable person]"
decision-makers: ["Name 1", "Name 2"]
consulted: ["Name or role"]
informed: ["Name or role"]
created: YYYY-MM-DD
last-reviewed: YYYY-MM-DD
next-review: N/A  # DRs are snapshots; supersede rather than update
language: en
supersedes: "DR-NNNN | none"
superseded-by: "DR-NNNN | none"
related-decisions: ["DR-NNNN"]
related-adrs: ["ADR-NNNN"]
tags: [relevant keywords]
---

# DR-NNNN: [Decision Title]

## Context

<!-- AI-FILL: 3–6 sentences. What situation requires this decision? What
     problem are we solving? Include enough background for someone unfamiliar
     with the project to understand why this matters. Be specific about
     which system, team, users, timeframe. Reference related docs by link,
     not duplication. -->

[Context]

## Decision

<!-- AI-FILL: 1–3 sentences. State the decision unambiguously. No hedging
     ("we will probably / leaning toward / planning to"). Name the specific
     choice and what's affected. -->

We will [decision].

## Alternatives Considered

<!-- AI-FILL: Minimum 2 alternatives. If only one was considered, that's a
     red flag — flag it explicitly here ("Only one alternative considered
     because [reason]"). Each alternative needs description, pros, cons, and
     a specific rejection reason tied to the constraints. -->

### Alternative A: [Name]

[Brief description, 2–3 sentences]

- **Pros:** [What's good about this option]
- **Cons:** [What's problematic]
- **Why rejected:** [Specific reason — tie to a constraint or driver]

### Alternative B: [Name]

[Same structure]

## Rationale

<!-- AI-FILL: Why THIS decision over the alternatives. Name the decisive
     factor(s). What constraints shaped the choice? What tradeoffs are we
     accepting? "We chose A because B" is NOT enough — explain the REASONING,
     not just the conclusion. This is the most important section of the DR. -->

[Rationale]

## Consequences

### Expected Outcomes

<!-- AI-FILL: 2–5 bullets. What do we expect to happen as a result?
     Be specific and checkable — in 6 months, could a reader say
     "this played out as expected" or "this didn't"? Vague aspirations
     ("things will be better") are not consequences. -->

- [Expected outcome 1]

### Risks and Tradeoffs

<!-- AI-FILL: 2–5 bullets. MUST be non-empty. What are we giving up? What
     could go wrong? What are we betting on? If the input names no risks,
     ask: "What's the trade-off you're least happy about?" Empty section = bad DR. -->

- [Risk or tradeoff 1]

### Dependencies

<!-- AI-FILL: What does this decision depend on (other decisions, external
     events, capacity, approvals)? What other decisions does it affect? -->

- [Dependency 1]

## Stakeholders

<!-- AI-FILL: Name everyone explicitly. Decision-maker is required. If
     consulted/informed are unknown from input, mark as [TBD: who was consulted?]
     rather than leaving blank or guessing. -->

| Role | Name | Input / Sign-off |
|------|------|------------------|
| Decision maker | [Name] | [Approved / Pending] |
| Consulted | [Name(s)] | [Input received] |
| Informed | [Name(s)] | [Notified] |

## Related Documents

<!-- AI-FILL: Source materials (one-pager, PRD, transcript, ticket), related
     DRs, related ADRs (architectural decisions implementing this DR),
     external references. -->

- [Source: one-pager / PRD / ticket / thread]
- [Related DR-NNNN — one-line summary]
- [Related ADR-NNNN — one-line summary]
```

---

## AI Auto-Fill Prompt

Paste this prompt into your agent along with the template above and the source material (one-pager, PRD, meeting transcript, ticket, chat thread).

```text
You are filling out a Decision Record (DR) using the template above.

Rules:
1. Populate every section. If a field isn't covered by the source material,
   write "[TBD: <what's missing>]". Never invent.
2. Status defaults to "draft" unless the source clearly states the decision is
   already approved or in effect.
3. At least 2 alternatives must appear. If only one is named, flag it
   explicitly in the Alternatives section: "Only one alternative considered
   because [reason from input, or TBD]."
4. Decision must be one declarative sentence — no hedging.
5. Risks and Tradeoffs must be non-empty. If silent, end your response with:
   "Question for owner: what's the trade-off you're least happy about?"
6. Stakeholders table: decision-maker is required. If consulted/informed are
   unknown, mark as "[TBD: who else weighed in?]".
7. Quote source material verbatim for specific commitments, numbers, names.
8. Translate Danish to English for the body. Preserve original-language
   quotes inline if they're load-bearing.
9. Strip all <!-- AI-FILL: ... --> comments from the final output. They are
   instructions to you, not content.
10. Output a single Markdown document starting with the YAML frontmatter.
11. After drafting, run the Quick Quality Check self-check (next section
    below). Fix any red flags before returning. If a red flag requires user
    input, append the unresolved questions at the end of your response under
    "Questions for owner before this DR can be approved:".
12. **Wrong-template check:** If the decision is engineering-internal
    architectural (database choice, integration pattern, library, service
    boundary) and the audience is engineering-only, STOP and tell the user:
    "This looks like an architectural decision — use the ADR template
    (4-adr-template.md) instead of the DR template."

Source material follows.
```

---

## Quick Quality Checks (run after auto-fill)

These checks run **automatically** — by the AI agent after filling the template, or by a human reviewer in under 2 minutes. They catch the predictable failure modes of auto-filled DRs.

For comprehensive peer review, audits, or quality gates, use the full evaluation in [5-documentation-standards-evaluation.md](5-documentation-standards-evaluation.md) → **DR-Specific Evaluation**.

### Red Flags (each one is a hard fail — fix before marking `approved`)

❌ **Hedged decision** — Decision section uses "we will probably / leaning toward / planning to"
❌ **No alternatives** — Single option with no explanation of why others weren't considered
❌ **Empty Risks and Tradeoffs** — Section blank, missing, or "no major risks"
❌ **Shallow rationale** — Just "we chose A because A is good"; doesn't name the decisive factor or address what's being given up
❌ **Vague Expected Outcomes** — Can't be checked in 6 months ("things will be better", "improved alignment")
❌ **Missing decision-maker** — Stakeholders table has no named decision-maker
❌ **Leftover scaffolding** — `[TBD: ...]` markers in critical fields (`owner`, `decision-makers`, `Decision`, `Rationale`) OR uncleaned `<!-- AI-FILL: -->` comments
❌ **Wrong template** — Decision is engineering-internal architectural → should be an ADR ([4-adr-template.md](4-adr-template.md))
❌ **Two decisions tangled** — DR captures what's actually two separate decisions; rationale gets confused between them
❌ **Title is a noun phrase** — "Pricing model" instead of "Adopt usage-based pricing for X"

### Green Flags (signals the DR is doing its job)

✅ **Decision is one declarative sentence** — Names the choice, no hedging
✅ **At least 2 real alternatives with explicit rejection reasons**
✅ **Rationale names the decisive factor** — "The deciding factor was X because Y"
✅ **Risks and Tradeoffs are concrete** — Specific failure modes, not generic concerns
✅ **Expected Outcomes are checkable** — Measurable enough to revisit in 6 months
✅ **Stakeholder table fully populated** — Decision-maker, consulted, informed all named
✅ **Source material is linked** — One-pager, PRD, ticket, or thread referenced

### AI Self-Check Prompt (run after auto-fill, before returning DR)

```text
You have just auto-filled a DR. Before returning it, run this self-check:

1. Is the Decision section a single declarative sentence with no hedging
   ("probably", "leaning toward", "planning to")?
2. Are there at least 2 alternatives in Alternatives Considered, OR is the
   single-alternative case explicitly flagged with a reason?
3. Is each alternative's "Why rejected" tied to a specific constraint or driver,
   not generic ("not as good")?
4. Is the Rationale doing more than restating the Decision? Does it name the
   decisive factor and address what we're giving up?
5. Is Risks and Tradeoffs non-empty and concrete (not "no major risks" and
   not generic "added complexity")?
6. Are Expected Outcomes checkable in 6 months — specific enough to verify?
7. Is the Stakeholders table populated with at least a named decision-maker?
8. Are there any leftover `[TBD: ...]` markers in critical fields (owner,
   decision-makers, Decision, Rationale)?
9. Are there any leftover `<!-- AI-FILL: ... -->` HTML comments in the output?
10. Is the title a verb phrase ("Adopt X", "Use X for Y", "Replace X with Y"),
    not a noun phrase ("Pricing model", "Vendor choice")?
11. Is this actually an architectural/engineering-internal decision? If yes,
    flag to the user: "This should be an ADR, not a DR. See 4-adr-template.md."
12. Does this DR capture exactly ONE decision? If two are tangled together,
    flag to the user: "This looks like two decisions. Should we split it?"

For each red flag found:
- If it can be fixed from existing source material, fix it.
- If it requires user input, append a question block to your response:
    "Before this DR can be approved, please answer:
     - [Specific question per red flag]"
- Do NOT silently return a DR with red flags present.
```

---

## How to Use This Template

### Numbering Convention

Use `DR-NNNN` (Decision Record + sequential number) as the identifier. This makes decision records searchable and referenceable. Example: `DR-0001`, `DR-0042`.

For **engineering-internal architectural decisions** (database choice, integration pattern, library selection), use the dedicated [ADR template](4-adr-template.md) with the `ADR-NNNN` prefix instead of this one. The ADR template is tighter, AI-auto-fill optimized, and follows the Nygard / MADR convention engineers expect to find next to code. Use this Decision Record template for product, business, or cross-cutting decisions where the audience includes non-engineers.

### When to Create a New DR vs. Update an Old One

**Create a new DR when:**
- A previous decision is being reversed or significantly changed
- New information fundamentally changes the rationale
- A new constraint or requirement makes the old decision invalid

**Never do:**
- Edit the "Decision" or "Rationale" of an existing DR after it's been approved
- Delete an old DR because the decision changed

**Instead:** Create a new DR, set the old one's status to `superseded`, and fill in the `superseded-by` field with the new DR's number.

### How Detailed Should Alternatives Be?

Detailed enough that a reader can understand WHY they were rejected. One sentence per alternative is too little. A full page per alternative is too much. 3-5 bullet points covering pros, cons, and rejection reason is the sweet spot.

### When You Only Considered One Option

If there are no alternatives in your decision record, either:
- You didn't consider alternatives (bad — go back and think about this)
- There genuinely was only one viable option (rare, but it happens — document why)

Either way, the absence of alternatives is worth noting.
