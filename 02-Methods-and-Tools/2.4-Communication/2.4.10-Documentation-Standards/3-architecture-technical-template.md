# Architecture / Technical Documentation Template

## Overview

Use this template when documenting how a system, service, or integration works. This is for the engineer who joins the team next month, the on-call responder at 2 AM, or the tech lead evaluating whether to build on top of your service.

Architecture docs are **living documents**. Unlike decision records (which are snapshots), these must reflect the current state of the system. That means they need an owner who updates them when the system changes.

**Language guidance:** Technical documentation should default to English. Code, API names, and system components are already in English. Writing the surrounding context in Danish creates unnecessary language switching. Metadata should always be in English.

---

## Architecture / Technical Documentation Template

```
---
title: [System/Service Name — Technical Overview]
doc-type: architecture
status: draft | review | current | archived
audience: [engineering | cross-team]
owner: [Name — the person who keeps this doc current]
created: [YYYY-MM-DD]
last-reviewed: [YYYY-MM-DD]
next-review: [YYYY-MM-DD — set 3-6 months out]
language: [en | da]
tags: [system name, domain, technology stack keywords]
---

# [System/Service Name] — Technical Overview

## Purpose

[What does this system/service do? Why does it exist? 2-3 sentences max.
Write for someone who has never heard of this system.

Example: "The Settlement Service calculates and distributes payments
to advisors based on completed consultations. It runs nightly,
processes ~15K transactions per batch, and feeds into the finance
reporting pipeline."]


## Context and Boundaries

[Where does this system sit in the broader architecture? What does it
own vs. what does it delegate to other systems?]

### System Boundary

[Define clearly what is IN scope and OUT of scope for this system.
What does it do? What does it explicitly NOT do?]

### Key Integrations

| System | Direction | Protocol | What it does |
|--------|-----------|----------|-------------|
| [System A] | Inbound | [REST/Events/DB] | [Brief description] |
| [System B] | Outbound | [REST/Events/DB] | [Brief description] |
| [System C] | Bidirectional | [Protocol] | [Brief description] |


## Architecture Overview

[High-level description of the architecture. If you have a diagram,
reference it here — but ALWAYS include a text description alongside it.
AI agents can't read diagrams; future engineers might not have access
to the diagramming tool.]

### Components

| Component | Responsibility | Technology |
|-----------|---------------|------------|
| [Component A] | [What it does] | [Tech stack] |
| [Component B] | [What it does] | [Tech stack] |
| [Component C] | [What it does] | [Tech stack] |

### Data Flow

[Describe how data moves through the system. Use a numbered sequence
when possible:

1. [Source] sends [what] via [how]
2. [Component A] processes [what] by [doing what]
3. [Component B] stores [what] in [where]
4. [Output] is sent to [destination] via [how]]


## Data Model

[Key entities, their relationships, and where they live.
You don't need to document every column — focus on the entities
and relationships that matter for understanding the system.]

### Key Entities

| Entity | Description | Storage | Retention |
|--------|------------|---------|-----------|
| [Entity A] | [What it represents] | [DB/Cache/File] | [How long kept] |
| [Entity B] | [What it represents] | [DB/Cache/File] | [How long kept] |


## Operational Context

### Infrastructure

[Where does this run? Cloud/on-prem? What environment(s)?
What are the deployment characteristics?]

### Monitoring and Alerting

[How do you know if this system is healthy? What alerts exist?
Where do you look when something goes wrong?]

### Performance Characteristics

[Rough numbers: throughput, latency, typical load.
Not exact benchmarks — just enough to set expectations.

Example: "Handles ~500 req/s at p95 < 200ms. Batch jobs process
~15K records in ~45 minutes. Peak load is Monday mornings."]


## Known Limitations and Technical Debt

[Be honest. What doesn't work well? What would you fix if you had
time? What workarounds exist?

This section is incredibly valuable for new team members — it saves
them from discovering these the hard way.]

- [Limitation 1: description and impact]
- [Limitation 2: description and impact]
- [Known debt: what it is, why it exists, rough effort to fix]


## Decision History

[Link to relevant Decision Records (DR-NNNN) that shaped this
system's architecture. Don't duplicate the reasoning — just
link and provide a one-line summary.]

| Decision | Summary | Link |
|----------|---------|------|
| [DR-NNNN] | [One-line summary] | [Link] |
| [DR-NNNN] | [One-line summary] | [Link] |


## Getting Started (for new team members)

[Quick pointers to get a new engineer productive:

- Where is the code? [repo link]
- How do you run it locally? [brief or link to setup guide]
- How do you deploy? [brief or link to deployment guide]
- Who should I talk to? [team/person]]


## Related Documents

- [Link to API documentation]
- [Link to runbooks / incident playbooks]
- [Link to related architecture docs]
- [Link to Confluence pages, Jira boards, etc.]
```

---

## AI Auto-Fill Prompts

Architecture/Technical docs have **two** auto-fill workflows: **initial creation** (drafting from a design doc, codebase exploration, or onboarding interview) and **refresh** (updating an existing doc against current system state). Use the prompt that matches your workflow.

### Initial Creation Prompt

Paste this prompt into your agent along with the template above and the source material (design doc, README, repo tour notes, onboarding interview transcript, codebase summary).

```text
You are filling out an Architecture/Technical document using the template above.

This is a LIVING document — it must reflect the CURRENT state of the system,
not its design intent or aspirational state.

Rules:
1. Populate every section. If a field isn't covered by the source material,
   write "[TBD: <what's missing>]". Never invent.
2. status defaults to "draft" unless the source clearly states otherwise.
3. owner is REQUIRED. If unknown, ask the user before drafting.
4. next-review must be set 3–6 months from created. Don't leave blank.
5. Known Limitations and Technical Debt section MUST be non-empty. If silent,
   end your response with: "Question for owner: what doesn't work well in
   this system right now? What would you fix if you had time?"
6. Decision History: link related ADRs and DRs that shaped this architecture.
   If you can identify them from the source, populate the table. If not,
   mark "[TBD: link related ADRs/DRs]".
7. Pair every diagram reference with a text description. If only diagrams
   are available, write the equivalent text description.
8. Quote source material verbatim for technical specifics (component names,
   technology versions, throughput numbers, integration protocols).
9. Translate Danish to English for the body. Preserve original-language
   quotes inline if they're load-bearing.
10. Output a single Markdown document starting with the YAML frontmatter.
11. After drafting, run the Quick Quality Check self-check (next section
    below). Fix any red flags before returning.
```

### Refresh Prompt (for existing docs)

When the source material is the existing architecture doc PLUS evidence that the system has changed (new ADRs, recent PRs, code diffs, deployment changes), use this prompt instead.

```text
You are refreshing an existing Architecture/Technical document against the
current state of the system.

Inputs:
- Current doc: [paste below]
- Evidence of changes: [recent ADRs, PRs, deployment changes, etc.]

Rules:
1. Compare the current doc against the evidence. For each section, identify
   whether it's still accurate, partially accurate, or out of date.
2. Update only what's actually changed. Do NOT rewrite accurate sections.
3. Update last-reviewed to today's date. Update next-review 3–6 months out.
4. If a major change is detected (component added/removed, technology
   migration, integration replaced), check whether an ADR exists for it.
   If yes, link it in Decision History. If no, flag to the user:
   "Major change detected without an ADR — should we capture this as ADR-NNNN?"
5. Update the Known Limitations section to reflect what's currently true —
   resolved limitations should be removed; new ones should be added.
6. Output a unified diff or annotated version showing what changed and why.
7. Run the Quick Quality Check after refresh. Surface freshness signals
   prominently.
```

---

## Quick Quality Checks (run after auto-fill or refresh)

These checks run **automatically** — by the AI agent after filling/refreshing the template, or by a human reviewer in under 2 minutes. They catch the predictable failure modes of architecture docs (especially staleness, since this is a living doc).

For comprehensive peer review, audits, or quality gates, use the full evaluation in [5-documentation-standards-evaluation.md](5-documentation-standards-evaluation.md) → **Architecture/Technical-Specific Evaluation**.

### Red Flags (each one is a hard fail)

❌ **No owner** — `owner` field empty or pointing to someone who left the team
❌ **No next-review** — Date missing or in the past
❌ **Empty Known Limitations** — Section blank, missing, or "none" — every system has warts
❌ **Diagram-only architecture** — Architecture explained primarily through images with no text equivalent (AI-unreadable, version-control unfriendly)
❌ **Stale by evidence** — `last-reviewed` is more than 6 months ago AND new ADRs/major PRs exist for this system since
❌ **Missing data flow** — Integrations listed but no description of how data actually moves end-to-end
❌ **No operational context** — Missing monitoring, alerts, or "where to look when things break"
❌ **Code walkthrough** — Doc reads as a function-by-function summary instead of system context
❌ **Aspirational state** — Describes how the system is DESIGNED to work, not how it actually works (the "Marketing Doc" antipattern)
❌ **Leftover scaffolding** — `[TBD: ...]` markers in critical fields (`owner`, `Purpose`, `System Boundary`, `Known Limitations`)

### Green Flags (signals the doc is doing its job)

✅ **Owner is current and accountable** — Named person actively maintains it
✅ **Recent review** — `last-reviewed` within the past quarter
✅ **Diagrams paired with text** — Every diagram has an equivalent text description
✅ **Known Limitations is honest** — Specific tech debt, workarounds, gotchas listed
✅ **Data flow described as numbered sequence** — Reader can trace a request end-to-end
✅ **Operational context populated** — Monitoring, alerts, performance numbers, where to look
✅ **Decision History links ADRs/DRs** — Architectural choices traceable to their reasoning
✅ **Getting Started works today** — A new engineer could actually use it now

### AI Self-Check Prompt (run after auto-fill or refresh, before returning doc)

```text
You have just auto-filled or refreshed an Architecture/Technical document.
Before returning it, run this self-check:

1. Is `owner` populated with a current, named person (not "[TBD]" and not
   someone who has left the team)?
2. Is `next-review` set 3–6 months from `last-reviewed`, and not in the past?
3. Is the Known Limitations section non-empty AND concrete (not "none" and
   not "to be determined")?
4. Is every diagram reference paired with a text description? Could an AI
   agent (or a screen reader user) understand the architecture from text alone?
5. Is the Data Flow section a numbered sequence a reader can follow end-to-end?
6. Does the doc describe how the system ACTUALLY works (current state), or
   how it was designed to work (aspirational)? Flag any aspirational language.
7. Is there operational context — monitoring, alerts, performance, where to
   look when things break?
8. Are major architectural choices linked to their ADRs/DRs in Decision History?
9. Are there any leftover `[TBD: ...]` markers in critical fields (owner,
   Purpose, System Boundary, Known Limitations)?
10. **Freshness check:** Is `last-reviewed` within the past 6 months? If
    longer, AND any new ADRs exist for this system since `last-reviewed`,
    flag prominently: "This doc is likely STALE — recent ADRs suggest the
    system has changed. Recommend full refresh before relying on it."

For each red flag found:
- If it can be fixed from existing source material, fix it.
- If it requires user input, append a question block to your response:
    "Before this doc can be marked current, please answer:
     - [Specific question per red flag]"
- Do NOT silently return an architecture doc with red flags present.
```

---

## How to Use This Template

### Living Doc Maintenance

This is a living document. The deal is simple: **when you change the system, update the doc.** The `owner` in the metadata header is responsible for enforcing this.

Practical tips:
- Add "update architecture doc" as a checklist item in your PR template or definition of done
- Review the doc during sprint planning when the team picks up work in this system's area
- Set the `next-review` date 3-6 months out and actually review when it arrives

### On Diagrams

Diagrams are valuable but insufficient alone. Always pair a diagram with a text description that covers the same information.

- **AI agents can't read diagrams.** They can read text descriptions.
- **Diagrams go stale.** Updating a Mermaid/draw.io diagram has higher friction than updating text.
- **Accessibility.** Not everyone can view images in every context.

If you use Mermaid, Markdown-rendered diagrams, or ASCII art — those are better than image files because they're version-controlled, diff-able, and text-searchable.

### How Deep Should You Go?

Deep enough that a new engineer can understand the system without reading all the code. Not so deep that the doc becomes a line-by-line code walkthrough. The test: if an engineer reads this doc and then opens the codebase, do they have enough context to navigate it effectively?

### The "Known Limitations" Section Is NOT Optional

This is often the most valuable section in the entire doc. Every system has warts, tech debt, and workarounds. Documenting them openly:
- Saves new team members from costly surprises
- Creates visibility for prioritizing tech debt work
- Prevents the same problems from being rediscovered repeatedly

If this section is empty, either the system is perfect (unlikely) or the author skipped it (fix this).
