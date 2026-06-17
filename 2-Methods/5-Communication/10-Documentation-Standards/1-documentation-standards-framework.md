# Documentation Standards Framework

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "documentation", "doc standards", "decision record", "ADR", "architecture doc", "how do we document", "documentation template", "knowledge base"
- User is discussing: establishing team norms for documentation, capturing decisions, creating technical docs, AI-readiness of documentation
- User is in: `execution_mode` (after braindump) or explicitly requesting documentation scaffolding
- Prerequisite: User has something to document or wants to establish documentation practices

**How to introduce:**

- "You're capturing a decision — let's use the decision record template so it's structured and findable."
- "Before documenting this, let's figure out what TYPE of documentation you need. Different audiences need different things."
- "This looks like an architecture doc. Let me pull the technical documentation template."

**Type dispatch (when the user has source material — transcript, design doc, ticket, chat thread — and wants the doc auto-filled):**

| User signal | Use this template |
|---|---|
| Product / business / cross-cutting decision; audience includes non-engineers | [2-decision-record-template.md](2-decision-record-template.md) (DR) |
| Engineering-internal architectural choice (database, integration pattern, library, service boundary); audience is engineering-only | [4-adr-template.md](4-adr-template.md) (ADR) |
| "How does this system work?" — describing a system, service, or integration | [3-architecture-technical-template.md](3-architecture-technical-template.md) |
| User wants to refresh an existing architecture doc against current system state | [3-architecture-technical-template.md](3-architecture-technical-template.md) → Refresh Prompt |

Each template ships with an **AI Auto-Fill Prompt** and hardwired **Quick Quality Check self-check**. The flow is: load template → load auto-fill prompt → attach source material → agent drafts → agent runs self-check → agent returns ADR/DR/Architecture doc with any unresolved questions for the owner.

**Common mistakes to avoid:**

- Don't let user write a "doc" without identifying the audience and doc type first
- Don't treat all documentation the same — a decision record → a how-to guide → a technical spec
- Don't skip the metadata header — it's what makes docs findable and maintainable
- Don't assume English is always correct — ask about primary audience language when the template prompts it
- Don't auto-fill an ADR/DR without source material; if the user has only a vague idea, stay in `product_sense` until there's something concrete to capture
- Don't silently return an auto-filled doc that has red flags from the self-check; surface unresolved questions to the user

**When NOT to use this framework:**
- User needs a PRD (use PRD framework)
- User needs a one-pager for stakeholder alignment (use One-Pager framework)
- User needs a meeting agenda (use Meeting Agendas framework)
- User is braindumping and not ready to structure yet (stay in product_sense)

---

## Overview

Documentation is infrastructure. Like code infrastructure, it either works for you or works against you — and when it breaks, nobody notices until it's too late. This framework treats documentation as a product: it has users, jobs-to-be-done, quality standards, and a maintenance lifecycle.

The core insight is simple: **there is no such thing as "documentation."** There are decision records, architecture docs, how-to guides, troubleshooting articles, onboarding materials, and runbooks. Each serves a different audience with a different need. Lumping them together is like saying "we need to build software" without specifying what kind.

---

## Step 0: Braindump First (Do this first!)

**Use prompts from:** [system/coaching/prompts.md](../../../system/coaching/prompts.md) — [Golden nuggets](../../../system/coaching/prompts.md#generic-step-0-any-framework). Quick start: Who actually needs this doc, and what job does it do for them → What happens when this information changes → Should an AI agent be able to reason over this → **See prompts file for full list.**

**Documentation structures the knowledge — it doesn't create it.** If you don't have clarity on what you're capturing, no template will save you.

---

## Core Philosophy

### Documentation Standards are NOT a "Write More Docs" Initiative

More docs → better docs. Every doc you create is a commitment to keep it current. Good documentation practice should:

- **Quality over quantity** — 10 well-maintained docs beat 100 stale ones every time.
- **Thinking over formatting** — A perfectly formatted decision record with shallow reasoning is still a bad doc. Templates structure knowledge; they don't create it.
- **Platform-agnostic over tool-specific** — These templates work in Confluence, Notion, markdown repos, or whatever comes next. This isn't a Confluence style guide.
- **Taxonomy over monolith** — Name the doc type before you write. If you can't, you haven't thought it through.

This framework gives you:

- **A taxonomy** — Recognize which kind of documentation you're actually creating.
- **A metadata standard** — Make docs findable by humans AND machines.
- **A set of templates** — Lower the activation energy for creating good docs.
- **A quality bar** — Know when a doc is done and when it needs work.

---

## Documentation Taxonomy

Every document you create falls into one of these types. Name the type BEFORE you start writing.

### Type 1a: Decision Record (DR)

**What it captures:** Why we chose option A over options B and C for a **product, business, or cross-cutting decision**. Context, constraints, alternatives, expected outcomes.

**Primary audience:** Future PMs, stakeholders who weren't in the room, leadership, cross-functional teams.

**Key property:** SNAPSHOT — captures what was true at a point in time. Never updated; new decisions supersede old ones.

**When to create:** Meaningful product or cross-cutting decision where someone will ask "why did we do it this way?" in 6 months. Audience includes non-engineers.

**Template:** `2-decision-record-template.md` (prefix `DR-NNNN`)

### Type 1b: Architecture Decision Record (ADR)

**What it captures:** Why we chose architectural option A over B and C — database, integration pattern, library, service boundary, data model trade-off.

**Primary audience:** Engineers, tech leads, future on-call responders. Co-located with the codebase.

**Key property:** SNAPSHOT, like DR. Tighter and more technical: Status / Context / Decision Drivers / Options / Decision / Consequences / Validation. Higher volume than DRs (one per significant architectural choice).

**When to create:** Engineering-internal architectural choice that affects code. If the audience is exclusively engineering and the decision is about HOW the system is built (not WHAT to build or WHY for the business), it's an ADR.

**Template:** `4-adr-template.md` (prefix `ADR-NNNN`). AI-auto-fill optimized.

**ADR vs DR — quick rule:** Audience includes non-engineers → DR. Audience is engineering-only and the choice is code-level → ADR. When in doubt and the decision affects code architecture, default to ADR.

### Type 2: Architecture / Technical

**What it captures:** How the system works. Component relationships, data flows, integration points, technical constraints, and operational context.

**Primary audience:** Engineers, tech leads, on-call responders, new team members joining the codebase.

**Key property:** It's a LIVING document — it should reflect the current state of the system. When the system changes, the doc must change. This means it needs an owner and a review cadence.

**When to create:** When a system, service, or integration is complex enough that a new engineer couldn't understand it by reading the code alone.

**Template:** `3-architecture-technical-template.md`

### Type 3: How-to / Procedural *(future)*

**What it captures:** Step-by-step instructions for completing a specific task in a system.

**Primary audience:** End users, helpdesk agents, support staff.

**Key property:** It's TASK-oriented — it starts with what the user wants to accomplish and ends when the task is done. It answers "how do I do X?" not "how does X work?"

**When to create:** When users repeatedly ask how to do something, or when a new feature launches that requires user action. Build from feedback patterns — don't pre-write how-to guides for features nobody has asked about.

**Design note:** This is where screenshots and step-by-step MIGHT be appropriate — but only when the audience genuinely needs visual guidance. Consider whether a short text description or a 30-second video would serve better. For AI consumption, structured text with clear step numbering is far more useful than screenshots.

### Type 4: Troubleshooting / Known Issues *(future)*

**What it captures:** Symptoms, diagnoses, and fixes for known problems.

**Primary audience:** Support agents, engineers, advanced users.

**Key property:** It's PATTERN-based — organized by symptom ("user sees error X") not by system component. This is how real humans search for help.

**When to create:** When a bug is found and fixed, when a workaround exists for a known limitation, or when support keeps answering the same question.

### Type 5: Onboarding / Conceptual *(future)*

**What it captures:** What something is, why it exists, and how it fits into the bigger picture.

**Primary audience:** New hires, cross-functional team members, people from other departments who need context.

**Key property:** It's NARRATIVE — it tells a story and builds understanding, not just lists facts. It answers "what is this and why should I care?"

**When to create:** When a domain, system, or initiative is complex enough that new people consistently struggle to understand it.

### Type 6: Runbook / Process *(future)*

**What it captures:** What to do when a specific event occurs. Incident response, deployment procedures, escalation paths.

**Primary audience:** Ops teams, on-call engineers, support escalation.

**Key property:** It's EVENT-driven — triggered by a condition ("when X breaks, do Y"). Needs to be scannable under pressure.

**When to create:** When there's a repeatable process that needs to be executed correctly under time pressure, especially when the person executing it might not be the person who designed it.

---

## The Metadata Standard

Every doc, regardless of type, starts with a structured metadata header. This is the single most impactful thing you can do for both human findability and AI-readiness.

```yaml
---
title: [Clear, descriptive title]
doc-type: decision-record | architecture | how-to | troubleshooting | onboarding | runbook
status: draft | review | approved | current | superseded | archived
audience: [product-team | engineering | support | end-users | leadership | cross-team]
owner: [Name — the person responsible for keeping this doc current]
created: [YYYY-MM-DD]
last-reviewed: [YYYY-MM-DD]
next-review: [YYYY-MM-DD]
language: [en | da — primary language of this document]
supersedes: [link to previous version, if applicable]
superseded-by: [link to newer version, if applicable]
tags: [comma-separated keywords for search and classification]
---
```

### Why Every Field Matters

- **doc-type:** Allows humans and AI to filter by category. "Show me all decision records" becomes a trivial query.
- **status:** Prevents people from acting on stale or superseded docs. The single most common documentation failure is someone following an outdated doc.
- **audience:** Makes it immediately clear whether this doc is for you. A support agent shouldn't waste time reading an architecture doc.
- **owner:** No owner = nobody's responsibility = guaranteed to go stale. Every doc needs exactly one owner.
- **created / last-reviewed / next-review:** The freshness triplet. An AI agent can flag "this doc hasn't been reviewed in 6 months" automatically. A human can decide whether to update or archive.
- **language:** Declares the document language. Defaults to English for new docs; use `da` when the primary audience is exclusively Danish-speaking (e.g., certain end-user guides).
- **supersedes / superseded-by:** Creates a chain of decision history. Critical for decision records — you never delete old decisions, you mark them superseded and link to the new one.
- **tags:** Free-form keywords for search. Keep them honest and useful.

### Metadata Hygiene: What's Actually Realistic

Be honest with yourself. A metadata standard that requires updating 12 fields on every edit will be abandoned within a month. Here's the realistic minimum:

**Must update on every meaningful edit:**
- `last-reviewed` (change the date — this is your signal that someone looked at it)
- `status` (if the doc is no longer current)

**Must set on creation (then rarely changes):**
- `title`, `doc-type`, `audience`, `owner`, `created`, `language`

**Set on creation, review quarterly:**
- `next-review`, `tags`

**Only when applicable:**
- `supersedes`, `superseded-by`

├──

## Language Guidance

### The Default: English

New documentation should default to English unless there's a specific reason to use Danish.

- **AI reasoning quality.** Every major AI tool in 2026-2027 understands, retrieves, and reasons over English significantly better than Danish. This isn't just about translation — it's about the quality of search, summarization, and cross-referencing.
- **Future-proofing.** As teams grow and AI agents become primary consumers of docs alongside humans, English is the lingua franca.
- **Cross-team readability.** External partners, international colleagues, and tools all work better with English.

### When Danish Makes Sense

- **End-user documentation** where the audience is exclusively Danish-speaking users who interact with a Danish-language interface
- **Regulatory or legal documentation** that must be in Danish by requirement
- **Onboarding materials** for roles where Danish is the working language and English would create unnecessary friction

### The Practical Rule

If an AI agent will need to REASON over this doc (search it, summarize it, cross-reference it with other docs, answer questions about it) → write in English.

If the doc is primarily consumed by Danish-speaking humans doing a specific task → Danish is fine, but still use English metadata headers.

### What NOT to Do

- Don't translate existing Danish docs to English just for the sake of it — only translate when the doc is being actively revised anyway.
- Don't write docs half in English, half in Danish. Pick one and stick with it.
- Don't assume "English" means "formal academic English." Write like a human. Clear, direct, conversational.

├──

## AI-Readiness Principles

These are the design principles that make documentation useful for AI agents — not just as a nice-to-have, but as the primary optimization target for 2027 and beyond.

**Structured over narrative:**
- AI agents parse sections, headers, and metadata far better than long prose. Use clear headers (`##`, `###`), short paragraphs, and structured metadata.
- This doesn't mean "no prose" — it means structure your prose.

**Explicit context over assumed context:**
- Humans can infer "this doc is about the payments system" from a Confluence page tree location. AI agents can't — or at least, they're bad at it.
- Put the context IN the doc: what system, what team, what time period.

**Semantic metadata over folder structure:**
- Folder structure helps humans navigate. Tags, doc-type, and audience fields help machines filter.
- Both matter, but if you have to choose, metadata is more portable and more queryable.

**Linked knowledge over duplicated knowledge:**
- Don't copy information from one doc to another. Link to it. Duplication is the #1 cause of contradictory docs.
- When an AI agent encounters two docs that say different things, it can't know which is correct. When one links to the other as the source of truth, the AI can follow the chain.

**Versioned over edited-in-place:**
- For decision records: never edit a past decision. Mark it superseded and create a new one. This preserves the decision trail.
- For living documents (architecture): edit in place, but update the `last-reviewed` date.

**Machine-readable dates and status:**
- Use ISO 8601 dates (`YYYY-MM-DD`), not "last Tuesday" or "Q1 2026."
- Use explicit status values from the enum (`draft | review | approved | current | superseded | archived`), not "this is probably still accurate."

├──

## Quick Quality Checks (Use During Creation)

### Top Red Flags to Watch For

→ **No metadata header** — Doc has no structured frontmatter
→ **Fix:** Add the metadata header. It takes 2 minutes and makes everything else work.

→ **Unnamed audience** — "This doc is for everyone" or no audience specified
→ **Fix:** Name the specific audience. If it's truly for everyone, it's probably for no one — consider splitting it.

→ **No owner** — Nobody is responsible for keeping this doc current
→ **Fix:** Assign an owner. If nobody wants to own it, question whether the doc should exist.

→ **No review date** — Doc has no `next-review` date
→ **Fix:** Set a review date. For decision records: never (they're snapshots). For living docs: 3–6 months.

→ **Mixed languages** — Doc switches between English and Danish mid-content
→ **Fix:** Pick one language. Use English metadata even if content is Danish.

→ **Duplicated content** — Same information exists in multiple docs
→ **Fix:** Choose one golden source and link to it from everywhere else.

→ **Screenshots as sole content** — Doc is nothing but screenshots with minimal text
→ **Fix:** Add structured text that describes what's happening. Screenshots complement text, not replace it. AI agents can't read screenshots.

→ **No context** — Doc assumes the reader knows which system/team/product this is about
→ **Fix:** Add a brief context section at the top. One sentence: "This doc describes [what] for [system/product]."

### Green Flags (What Good Documentation Looks Like)

→ Complete metadata header with all required fields filled
→ Clear audience named — you know exactly who this is for
→ Single language, consistently used throughout
→ Links to related docs instead of duplicating information
→ Owner assigned and review date set
→ Structure matches the doc type (decision records have alternatives, architecture docs have diagrams/descriptions)
→ Written in clear, direct language — no jargon walls
→ AI-readable: structured headers, explicit context, machine-parseable dates

### Quick Product Sense Questions (Ask Yourself)

- If I left the company tomorrow, could a new PM find this doc and understand it without calling me?
- Is there another doc that says something different about the same topic → If so, which one is the source of truth?
- Will anyone actually look at this doc in 6 months → If not, should I even write it?
- Could an AI agent answer a question using this doc, or would it need to "guess" what I meant?
- Am I writing this because it's useful, or because someone told me to?

├──

## Common Antipatterns

### The "Write Everything Down" Trap

**Pattern:** Team decides documentation is important, creates a rule that everything must be documented, produces a mountain of docs that nobody maintains.

**Why it fails:** Documentation has a maintenance cost. Every doc you create is a commitment to keep it current. More is not better — RELEVANT and MAINTAINED is better.

**Fix:** Only document things that pass the "will someone ask about this in 6 months?" test. Be ruthless about archiving.

### The "One Format Fits All" Trap

**Pattern:** Team uses the same template for everything. Decision records look like how-to guides look like architecture docs.

**Why it fails:** Different doc types serve different purposes. A decision record needs to capture alternatives and reasoning. A how-to guide needs to be scannable and task-oriented. Forcing them into the same format makes both bad.

**Fix:** Use the taxonomy. Name the type. Use the right template.

### The "Screenshot Novel" Trap

**Pattern:** Every doc is a 30-page walkthrough with a screenshot of every button click, every dropdown, every confirmation dialog.

**Why it fails:** Takes forever to create, goes stale immediately when the UI changes, and AI agents can't read images. Also, most of the audience doesn't need that level of hand-holding.

**Fix:** Use structured text as the primary content. Add screenshots only when visual context genuinely helps (complex UI layouts, error states). For AI readability, always describe in text what the screenshot shows.

### The "Danish by Default" Trap

**Pattern:** All docs are written in Danish because "that's what we've always done" and "our users are Danish."

**Why it fails in 2027:** AI tools reason significantly better in English. Cross-referencing, summarization, search quality — all degrade with Danish content. Your FUTURE readers include AI agents, not just humans.

**Fix:** Default to English for new docs. Use Danish only when the primary audience requires it (end-user facing, regulatory). Always use English metadata.

### The "No Owner" Trap

**Pattern:** Docs are created and forgotten. Nobody is responsible for reviewing or updating them.

**Why it fails:** Every doc has a half-life. Technical docs degrade as systems evolve. Decision records need to be marked superseded when new decisions are made. Without an owner, docs silently become wrong.

**Fix:** Every doc gets an owner in the metadata. Owner doesn't mean "writes all updates" — it means "responsible for ensuring this stays current or gets archived."

├──

## Best Practices

### Do's
- Name the doc type before you start writing
- Fill in the metadata header first — it forces you to think about audience, ownership, and lifecycle
- Default to English for new documentation
- Link to sources of truth instead of copying content
- Set a review date and actually review when it arrives
- Archive docs that are no longer relevant (don't delete — archive)

### Don'ts
- Treat documentation as a one-time project ("let's document everything this sprint")
- Skip the metadata header because "it's just a quick doc"
- Write for an imaginary audience — be specific about who reads this
- Create docs nobody asked for and nobody will maintain
- Use screenshots as the only content — always add structured text

├──

## AI Collaboration Prompts

Reusable prompts for AI-assisted documentation work. Copy-paste these into your AI tool.

**Identify the right doc type:**
```
I need to document [topic]. Help me figure out which documentation type
fits best. Here's what I'm trying to capture: [describe what you know].
Who will read this → [audience]. What should they be able to do after
reading it → [outcome].
```

**Create a decision record from meeting notes:**
```
Here are my notes from a meeting where we made a decision about [topic].
Please structure this as a Decision Record using our DR template.
Make sure to capture: the context, the decision itself, alternatives
we considered (and why we rejected them), and expected consequences.
Flag anything that's missing or unclear so I can fill it in.

[paste meeting notes]
```

**Create an architecture doc from a brain dump:**
```
I'm going to describe how [system/service] works. It's going to be
messy. Please listen to everything, then structure it into our
Architecture/Technical template. Flag gaps — especially: integrations
I didn't mention, operational context I skipped, and known limitations
I might be forgetting.

[start brain dump]
```

**Audit existing documentation:**
```
Here's an existing doc. Please evaluate it using our documentation
standards evaluation framework (4 steps: gut check, quality flags,
scored rubric, antipattern detection). Give me the score and
top 3 prioritized improvements.

[paste or link doc]
```

**Extract knowledge from a transcript:**
```
Here's a transcript of [person] explaining [topic]. They have 15+
years of domain knowledge. Please extract the key knowledge and
structure it into [decision record / architecture doc / appropriate
type]. Preserve their specific examples and edge cases — that's
where the real value is. Flag anything that seems like tribal
knowledge worth capturing separately.

[paste transcript]
```

---

## Integration with Other Frameworks

| When you're doing this | How this framework helps |
|------------------------|---------------------------|
| Making a product decision | **Decision Record** captures the decision, alternatives, and rationale |
| Onboarding a new engineer | **Architecture/Technical** docs give them system context |
| Writing a PRD | Link to relevant Decision Records for context on prior decisions |
| Creating a one-pager | Reference Decision Records for supporting evidence |
| Running a post-mortem | Create a Decision Record for "what we decided to change" |
| Building a new service | Start an Architecture/Technical doc on day one |

---

## References

- [Decision Record Template](2-decision-record-template.md)
- [Architecture/Technical Template](3-architecture-technical-template.md)
- [5-documentation-standards-evaluation.md](5-documentation-standards-evaluation.md)
- [One-Pagers](../3-One-Pagers/README.md)
- [PRD Framework](../../4-Execution/4-PRD/README.md)
- [Product Sense Entry](../../../system/coaching/README.md)
- [Foundations](../../1-Foundations/README.md)
