# 5-Communication — Methods Overview

This domain contains methods and templates for keeping stakeholders informed, aligned, and trained. Use these frameworks when you need to communicate effectively, manage relationships, handle crises, or create training materials.

## Before Using Any Communication Framework

⚠️ **Don't jump straight to one-pagers or meeting templates.**

### 1. Read the Golden Rule

**See:** [braindump.md](../../system/coaching/braindump.md) (coaching)

### 2. Braindump First (10–15 min)

**Use the prompts:** [system/coaching/prompts.md](../../system/coaching/prompts.md) — [Golden nuggets](../../system/coaching/prompts.md#generic-step-0-any-framework) and situation-specific sections (e.g. stakeholders, crisis).
**Or start from the entry point:** [README.md](../../system/coaching/README.md) (simple prompt for a product-thinking chat).

**Communication frameworks structure the message—they don't replace clarity of thinking.**

### 3. Then Use Communication Frameworks

After your braindump, use the frameworks below to structure your communication.

---

**Who this is for / when you're here**
- **Junior PMs:** Learn structured approaches to stakeholder communication, saying no gracefully, and running effective meetings. Start with Meeting Agendas and Stakeholder Management.
- **Senior PMs:** Quick reference for crisis management, escalation frameworks, and course design. Navigate directly to specific frameworks as needed.

## How this is organized

- `1-Newsletter/`  Framework and template for recurring stakeholder updates (e.g. monthly or weekly product newsletters). **Use when:** You need consistent, scalable communication about progress, risks, and decisions.

- `2-Meeting-Agendas/`  Agenda templates and frameworks for sprint reviews, retrospectives, planning sessions, stakeholder readouts, and other common PM meetings. **Use when:** You need to run effective meetings that drive decisions.

- `3-One-Pagers/`  Framework and templates for narrative one-pagers and lightweight briefs. **Use when:** You need to align leadership and teams on proposals, decisions, and strategy.

- `4-Crisis-Management/`  Communication playbooks and templates for when things go wrong (incidents, outages, serious bugs). **Use when:** You need to communicate quickly and clearly during high-pressure situations.

- `5-Escalation/`  Framework for knowing when and how to escalate issues in large organizations. **Use when:** You need to navigate authority, resources, and decision-making effectively.

- `6-Saying-No/`  Framework for declining requests gracefully without burning bridges. **Use when:** Capacity is limited and you need to say no professionally.

- `7-Stakeholder-Management/`  Framework for identifying, prioritizing, and managing stakeholders. Includes mapping, managing up, and cross-functional alignment guides. **Use when:** You need to build relationships and ensure the right people have the right information.

- `8-Stakeholder-Avatars/`  Framework and template for building a reusable "brainfeed cast" of stakeholder and peer avatars (goals, fears, tone, history). **Use when:** You want to simulate "what would my manager say?" or run politics checks when those people aren't in the room; output lives in [1-Context/1.1-Stakeholder-Avatars/](../../1-Context/1.1-Stakeholder-Avatars/README.md) (one file per avatar; naming: single digit, name, role, optional organization).

- `9-Courses/`  Course design framework and template. **Use when:** You need to structure internal enablement, PM onboarding, or external training materials in a repeatable way.

- `10-Documentation-Standards/`  Documentation taxonomy, metadata standards, and templates for decision records and architecture docs. Designed for AI-readiness in 2027. **Use when:** You need to create documentation that serves a specific audience, follows team standards, and is optimized for both humans and AI agents.

- `11-Sprint-Summary/`  Async sprint transition brief for stakeholders and team. Covers last sprint goal, what was delivered, new sprint goal, and expected outcomes. **Use when:** Sprint closes and you need to communicate what happened and what's next  to delivery leads, execs, and the team simultaneously.

## Typical flows

```
Stakeholder-Management → Newsletter → Meeting-Agendas → One-Pagers
                                                          ?
Crisis-Management → Escalation → Saying-No → (conflict/request)
                                                          ?
Courses (for training and enablement)
```

## When to use what (quick guide)

| Situation | Go to | Why |
|-----------|-------|-----|
| Monthly stakeholder updates | `1-Newsletter/` | Consistent, scalable communication format |
| Running sprint reviews or planning | `2-Meeting-Agendas/` | Structured agendas that drive decisions |
| Proposing new features/strategy | `3-One-Pagers/` | Quick alignment on proposals and decisions |
| Major incident or outage | `4-Crisis-Management/` | Clear communication during high-pressure situations |
| Need executive decision/authority | `5-Escalation/` | Framework for when and how to escalate |
| Too many requests, need to decline | `6-Saying-No/` | Graceful way to say no without burning bridges |
| Starting new initiative | `7-Stakeholder-Management/` | Map and manage stakeholders effectively |
| "What would my manager say?" / politics check | `8-Stakeholder-Avatars/` | Set up or use stakeholder avatars for simulation |
| Creating training materials | `9-Courses/` | Brain-based learning design framework |
| Documenting a decision | `10-Documentation-Standards/` | Decision record with alternatives, rationale, consequences |
| Documenting system architecture | `10-Documentation-Standards/` | Technical overview with components, data flow, operational context |
| Setting documentation standards | `10-Documentation-Standards/` | Taxonomy, metadata, AI-readiness principles |
| Sprint transition update to stakeholders + team | `11-Sprint-Summary/` | Sprint summary framework |

## Related domains / cross-links

- **Product sense (braindump first):** [README.md](../../system/coaching/README.md)  entry point for product thinking; use before one-pagers/meeting templates
- **Foundations (../1-Foundations/README.md):** Mental models, bias awareness, and self-reflection support communication
- **Strategy (../2-Strategy/README.md):** Newsletter references OKRs and roadmaps
- **Discovery (../3-Discovery/README.md):** Stakeholder interviews and research
- **Execution (../4-Execution/README.md):** Daily execution uses communication frameworks
- **Template Structure:** `../0-Template-Structure/` (for creating new frameworks)

## AI collaboration prompt

```
Act as a product coach. I'm in the Communication area. My goal: [your communication goal].
Help me braindump first, then suggest where to start in this domain. Challenge my assumptions and bias.
```

## Maintenance notes
- Keep "How this is organized" and "When to use what" current.
- Update flows when frameworks are added/removed.
- Add/remove "Before using" prompts if the domain needs them.


