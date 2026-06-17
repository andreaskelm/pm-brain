# Documentation Standards Framework

## Introduction

Documentation is not one thing. A how-to guide for a helpdesk agent, an architecture decision record for engineering, and a product decision rationale for Confluence are three fundamentally different products serving different audiences with different jobs-to-be-done. Most teams treat "documentation" as a monolith, which is exactly why it goes stale, nobody reads it, and AI tools can't make sense of it.

This framework helps you recognize the different types of documentation, choose the right one, and produce docs that are useful for both humans today AND AI agents tomorrow.

## Files

- `1-documentation-standards-framework.md` — Full framework: documentation taxonomy, AI-readiness principles, language guidance, structured metadata, and the "For Agents" section
- `2-decision-record-template.md` — Template for capturing product and cross-cutting decisions. AI-auto-fill optimized with hardwired Quick Quality Checks.
- `3-architecture-technical-template.md` — Template for documenting how systems work. AI-auto-fill optimized with separate creation and refresh prompts; freshness check hardwired.
- `4-adr-template.md` — Architecture Decision Record (ADR) template, AI-auto-fill optimized; for engineering-internal architectural choices co-located with code.
- `5-documentation-standards-evaluation.md` — Comprehensive evaluation framework with type-specific quality gates (DR, ADR, Architecture/Technical) and AI-runnable self-check prompts.

## Before Using This Framework

⚠️ **Don't jump straight to writing docs.**

### 1. Read the Golden Rule

**See:** [`../../../system/coaching/braindump.md`](../../../system/coaching/braindump.md)

### 2. Braindump First (5–10 min)

Use the prompts: [`../../../system/coaching/prompts.md`](../../../system/coaching/prompts.md) — [Golden nuggets](../../../system/coaching/prompts.md#generic-step-0-any-framework) and situation-specific sections.
Or start from the entry point: [`../../../system/coaching/README.md`](../../../system/coaching/README.md).

Before you write, answer these questions honestly:

- **Who is going to READ this?** (Be specific — "the team" is not an audience.)
- **What job is this doc doing for them?** (Finding an answer → Understanding a decision → Onboarding?)
- **Where will they look for it?** (Confluence → A repo → A helpdesk KB → Slack search?)
- **What happens when this information changes?** (Who updates it → When?)
- **Should an AI agent be able to find and use this?** (Not everything needs to be AI-optimized.)

**Documentation structures the knowledge — it doesn't create it.** If you don't have clarity on what you're capturing, no template will save you.

### 3. Then Use This Framework

After you've answered the questions above, pick the right template based on your documentation type (see taxonomy in `1-documentation-standards-framework.md`).

---

## How to Use This Framework

### Step 1: Identify the Documentation Type

Read the taxonomy in `1-documentation-standards-framework.md` → **Documentation Taxonomy**. Name the type of doc you're creating. If you can't name it, you haven't thought it through.

### Step 2: Choose the Right Template

Use the template that matches your doc type. This framework ships AI-auto-fill optimized templates for Decision Record (DR), Architecture Decision Record (ADR), and Architecture/Technical. Other types (how-to, troubleshooting, onboarding, runbook) can use the same structural principles — metadata header, clear audience, plain language — adapted to their purpose.

### Step 3: Fill in the Metadata Header

Every doc starts with structured metadata. This is what makes docs findable, maintainable, and machine-readable. Don't skip it.

### Step 4: Write the Content (or Auto-Fill It)

Two paths:

- **Manual:** Use the template structure and fill it yourself. Default to English for new docs unless there's a strong reason not to.
- **AI auto-fill:** Each template (`2-`, `3-`, `4-`) ships with an **AI Auto-Fill Prompt**. Paste the template, the prompt, and your source material (transcript, design doc, ticket, chat thread) into your AI agent. The agent drafts the doc, runs the hardwired Quick Quality Check self-check, fixes silent failures from source material, and escalates remaining gaps as questions for the owner. The Architecture/Technical template has a second prompt for **refreshing** existing docs against current system state.

### Step 5: Quality Check

Three levels, in order of effort:

- **Hardwired Quick Quality Checks** (in templates 2/3/5) — fire automatically during/after auto-fill via the self-check prompts. Catches predictable failure modes (hedged decisions, empty Negative consequences, leftover scaffolding, staleness).
- **Type-specific evaluation** (in `5-documentation-standards-evaluation.md`) — deeper red/green flag scan plus antipatterns, with AI self-check prompts that produce verdicts (ACCEPT / REVISE / REJECT / STALE for Architecture).
- **Generic evaluation** (in `5-documentation-standards-evaluation.md`, STEPS 0–4) — weighted rubric for peer review or audits across any doc type.

### Step 6: Publish and Set a Review Date

Every doc needs an owner and a next-review date. No exceptions. Stale docs are worse than no docs. ADRs and DRs are snapshots (`next-review: N/A`); Architecture/Technical docs are living and need a real review date 3–6 months out.

---

## When to Use

- You're creating a new document and want to follow team standards
- You're capturing a product or technical decision
- You're documenting system architecture or technical context
- You need to assess whether existing documentation is fit for purpose
- You're onboarding someone to documentation practices
- You want to show stakeholders what "good documentation" looks like in practice

## The Documentation Taxonomy (Quick Reference)

| Type | Primary Audience | Job-to-be-Done | Template |
|------|-----------------|-----------------|----------|
| **Decision Record (DR)** | Product team, future PMs, stakeholders | Understand why we chose X (product / cross-cutting) | [2-decision-record-template.md](2-decision-record-template.md) |
| **Architecture Decision Record (ADR)** | Engineering, tech leads | Understand why we chose X (architectural / code-level) | [4-adr-template.md](4-adr-template.md) |
| **Architecture / Technical** | Engineering, tech leads, on-call | Understand how the system works | [3-architecture-technical-template.md](3-architecture-technical-template.md) |
| **How-to / Procedural** | End users, helpdesk, support agents | Complete a specific task | *(future — build when user feedback patterns emerge)* |
| **Troubleshooting** | Support, engineering | Diagnose and fix a problem | *(future)* |
| **Onboarding / Conceptual** | New hires, cross-team | Understand what something is and why it exists | *(future)* |
| **Runbook / Process** | Ops, on-call, support escalation | Follow a procedure when X happens | *(future)* |

## How to Maintain

- **Quarterly:** Review all docs in this framework for accuracy
- **On use:** When you create a doc using these templates, note what worked and what didn't
- **On feedback:** When someone says "I couldn't find X" or "this doc was wrong," treat it as a signal — update the doc AND check if the template needs adjustment

## Links

- [Documentation Standards Framework](1-documentation-standards-framework.md)
- [Decision Record Template](2-decision-record-template.md)
- [Architecture/Technical Template](3-architecture-technical-template.md)
- [Documentation Evaluation](5-documentation-standards-evaluation.md)
- [ADR Template (AI-auto-fill optimized)](4-adr-template.md)
- [One-Pagers](../3-One-Pagers/README.md) — for communicating decisions
- [PRD Framework](../../4-Execution/4-PRD/README.md) — for detailed requirements
- [Product Sense](../../../system/coaching/README.md) — braindump first
