---
name: discovery-research
description: Support discovery and research workflows using PM Brain’s discovery frameworks (research interviews, continuous discovery, JTBD, segmentation, opportunity assessment, idea validation, problem-solution space, product-market-fit).
---

# Discovery & Research Skill

Use this skill when the user is exploring **what to build** or **why something is happening**, especially when they mention research, interviews, discovery, JTBD, opportunity assessment, validation, or product-market fit.

## When to use this skill

Trigger this skill (in product_sense or execution_mode) when the user:

- Says things like:
  - “I need to talk to users”
  - “I need to plan research / interviews”
  - “I want to understand why users churn / don’t adopt”
  - “I want to validate this idea”
  - “I’m not sure if there’s real demand”
  - “We need to understand problem vs solution space”
  - “Are we at product-market fit yet?”
- Or explicitly mentions:
  - Interviews, discovery, JTBD, opportunity assessment, idea validation

If the user is mostly doing **strategy (where to go)**, use the `strategy-planning` skill instead. If they’re mostly doing **communication to stakeholders**, use `stakeholder-management`.

## Relevant framework locations

Most discovery frameworks live under:

- `02-Methods-and-Tools/2.2-Discovery/`
  - `2.2.1-Research-Interviews/`
  - `2.2.2-Continuous-Discovery-Habits/`
  - `2.2.3-Jobs-To-Be-Done/`
  - `2.2.4-Opportunity-Assessment/`
  - `2.2.5-Idea-Validation/`
  - `2.2.6-Problem-Solution-Space/`
  - `2.2.7-Segmentation/`
  - `2.2.8-Product-Market-Fit/`

Each follows the usual pattern:

- `1-*-framework.md` — guide + “For Agents” section
- `2-*-template.md` — template to fill out (when present)
- `3-*-evaluation.md` — optional evaluation guide (when present)

## Typical flows

### 1. “I have an idea, should we build it?”

1. Stay in **product_sense** first (golden rule: braindump before structure).
2. Ask:
   - What problem do you think this solves, and for whom?
   - What evidence or signals do you already have?
   - What’s at risk if you’re wrong?
3. Then guide to:
   - Problem/Solution separation:
     - `2.2-Discovery/2.2.6-Problem-Solution-Space/1-problem-solution-space-framework.md`
   - Opportunity evaluation:
     - `2.2-Discovery/2.2.4-Opportunity-Assessment/1-opportunity-assessment-framework.md`
4. Only after sufficient braindump, move to **execution_mode**:
   - Use the relevant `2-*-template.md` to structure the opportunity.

### 2. “I need to run user interviews”

1. Clarify:
   - What do you want to learn or decide from these interviews?
   - Who exactly do you want to talk to?
   - What constraints do you have (time, access, volume)?
2. Point to:
   - `2.2-Discovery/2.2.1-Research-Interviews/1-interview-guide.md`
   - `2.2-Discovery/2.2.2-Continuous-Discovery-Habits/README.md` and the snapshot/synthesis steps.
3. Help them:
   - Define a focused research question.
   - Draft 6–10 core interview questions from the framework.
   - Plan what they’ll do with the data (snapshots → synthesis → opportunities).

### 3. “I want to understand product-market fit”

1. Clarify product, segment, and current signals (retention, NPS, qualitative feedback).
2. Point to:
   - `2.2-Discovery/2.2.8-Product-Market-Fit/1-pmf-framework.md`
3. Decide together:
   - Whether to start with qualitative (interviews) or quantitative (surveys, metrics), based on scale and access.

### 4. “I have JTBD job stories; how do I segment?”

1. Clarify: Have they done 15–30+ job interviews? Do they need to decide who to serve first?
2. Point to:
   - `2.2-Discovery/2.2.7-Segmentation/README.md` and `1-segmentation-framework.md`
3. Remind: Segments = strategy (what to build); personas = execution (create personas for priority segments via 2.3.5-Personas).

## Response guidelines

1. **Think, then framework, then template**
   - In product_sense: stay with prompts and braindump before picking discovery frameworks.
   - Use prompts from `2-product-sense-prompts.md` for discovery scenarios.
2. **Tie methods to constraints**
   - Always ask about time, access to users, and tooling before recommending heavy methods.
3. **Be specific**
   - Point to exact files: e.g., “From `02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/1-opportunity-assessment-framework.md`…”
4. **Connect the dots**
   - Cross-reference related frameworks (e.g., interviews → snapshots → opportunity assessment).

## Relation to other skills

- Use `pm-brain-workflow` for **overall routing** (Foundations → Strategy → Discovery → Execution → Communication).
- Use this `discovery-research` skill for the **discovery slice** of that flow.
- Use `strategy-planning` when the main question is direction and goals.
- Use `stakeholder-management` when the main question is communication and alignment.

