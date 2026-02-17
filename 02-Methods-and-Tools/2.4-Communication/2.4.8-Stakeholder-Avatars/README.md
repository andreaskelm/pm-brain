# Stakeholder Avatars (Brainfeed Cast)

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "set up my stakeholder brainfeed", "create stakeholder avatars", "who should I add to my brainfeed", "help me map my manager/peers for feedback"
- User is in: **conversation** or **product_sense** when they want to configure recurring people for later simulation
- Prerequisites: User wants a reusable cast of people (manager, Eng lead, designer, etc.) so the agent can simulate "what would X say?" when those people aren't in the room
- Output: Guided quiz → write/update [01-Company-Context/1.1-Stakeholder-Avatars/](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) (one file per avatar: N-name-role.md; see that folder's README for naming)

**How to introduce:**  
"We can set up your stakeholder brainfeed cast so I can later simulate how they'd react to plans or Comms. I'll ask you about 3–7 key people and, for each, a short set of questions about their goals, fears, tone, and how they've worked with you. The result lives in your company context so we can use it whenever you ask 'what would my manager say?' or run a politics check. Ready to pick the first person?"

**Common mistakes:**
- Running the quiz in the middle of a product_sense braindump (offer it after or in a separate pass).
- Filling avatars with vague traits; push for concrete phrases and examples.

**When NOT to use:**  
User only wants a one-off "what would X say?" and has no interest in saving avatars → do a lightweight inline simulation if you have enough context, and optionally suggest setting up avatars for next time.

---

## Introduction

This framework helps you build and maintain a **global cast of stakeholder and peer avatars** — structured profiles of real people you work with (manager, Eng lead, designer, VP, etc.). Those profiles are used to:

- Simulate how they’d react when they’re not in the room ("what would my manager say about this?").
- Run politics checks on plans, PRDs, and roadmaps before you share them.
- Sequence conversations and anticipate objections.

The **method** (quiz questions, template, when to update) lives here in 02-Methods-and-Tools. The **data** — your actual avatars — lives in [01-Company-Context/1.1-Stakeholder-Avatars/](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) (one file per person; see that folder's README for file naming). The agent uses the [politics-coach skill](../../../.cursor/skills/politics-coach/SKILL.md) to know when to run this framework or to simulate from existing avatars.

## Files

- `1-stakeholder-avatars-framework.md` — Full methodology: how to pick the cast, the quiz questions per stakeholder, and how to maintain avatars
- `2-avatar-template.md` — Copy-paste template for one avatar (schema only; fill via quiz or by hand)

## How to Use This Framework

1. **Read the framework** — Open `1-stakeholder-avatars-framework.md` to understand the cast, quiz, and naming.
2. **Pick the cast** — Choose 3–7 people (manager, Eng lead, design, etc.) and run the per-person quiz from the framework.
3. **Create one file per person** — In [01-Company-Context/1.1-Stakeholder-Avatars/](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md), create `N-name-role.md` (e.g. `1-jane-manager.md`). Use the structure in `2-avatar-template.md` and fill from the quiz answers.
4. **Refresh when needed** — After big 1:1s or role changes, update the relevant avatar file.

## When to Use

- Once per role (or after a major organization change) to define your core 3–7 people.
- When you want "what would X say?" or politics checks but don’t yet have avatars.
- Quarterly or after big conversations: refresh an avatar with new evidence.

## How to Maintain

- After important 1:1s or decisions, add a note to the relevant avatar file (e.g. new phrase, new fear, or updated relationship).
- If someone’s incentives or role change, update their file so simulations stay grounded.

## Links

- Stakeholder Management (mapping, Comms): [2.4.7-Stakeholder-Management/](../2.4.7-Stakeholder-Management/README.md)
- Politics-coach skill (when to use avatars): [.cursor/skills/politics-coach/SKILL.md](../../../.cursor/skills/politics-coach/SKILL.md)
- Product sense (braindump first): [2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md](../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md)
