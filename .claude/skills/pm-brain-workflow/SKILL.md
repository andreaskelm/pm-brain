---
name: pm-brain-workflow
description: Guide product managers through PM workflows using the PM Brain framework library. Use when working on product management tasks, braindumping ideas, assessing opportunities, writing PRDs, conducting research, or planning strategy. Supports thinking-first approach before jumping to templates.
---

# PM Brain Workflow Assistant

This skill helps you navigate and apply product management frameworks from the PM Brain repository following a natural product development flow.

## Core Principle: Think First, Template Later

Before jumping to templates, help users:
1. **Braindump** - Get all raw thoughts out
2. **Structure thinking** - Use framework prompts to organize
3. **Template** - Only then apply formal templates

## Framework Flow

The PM Brain follows a natural product development sequence:

```
1-Foundations → 2-Strategy → 3-Discovery → 4-Execution → 5-Communication
(HOW TO THINK) (WHERE TO GO?) (WHAT TO BUILD?) (BUILD & SHIP) (KEEP ALIGNED)
```

**When user is:**
- Early/exploring → Point to **1-Foundations** and **2-Strategy**
- Has a problem → Guide to **3-Discovery**
- Ready to build → Move to **4-Execution**
- Throughout → Support with **5-Communication**

## Quick Framework Locations

### 1-Foundations (How to Think)
- Mental Models: `2-Methods/1-Foundations/1-Mental-Models/`
- Bias Awareness: `2-Methods/1-Foundations/2-Bias/`
- Self-Reflection: `2-Methods/1-Foundations/3-Self-Reflection/`

### 2-Strategy (Where are we going?)
- Strategic Foundations: `2-Methods/2-Strategy/1-Strategic-Foundations/`
- OKRs: `2-Methods/2-Strategy/2-Strategic-Execution/1-OKR/`
- Roadmaps: `2-Methods/2-Strategy/2-Strategic-Execution/2-Roadmap/`
- North Star: `2-Methods/2-Strategy/2-Strategic-Execution/3-North-Star/`
- Prioritization: `2-Methods/2-Strategy/2-Strategic-Execution/4-Prioritization/`

### 3-Discovery (What to build?)
- Research Interviews: `2-Methods/3-Discovery/1-Research-Interviews/`
- Continuous Discovery: `2-Methods/3-Discovery/2-Continuous-Discovery-Habits/`
- Jobs-to-be-Done: `2-Methods/3-Discovery/3-Jobs-To-Be-Done/`
- Opportunity Assessment: `2-Methods/3-Discovery/4-Opportunity-Assessment/`
- Problem-Solution Space: `2-Methods/3-Discovery/6-Problem-Solution-Space/`

### 4-Execution (Build, ship, measure)
- Daily Rituals: `2-Methods/4-Execution/1-Daily-Execution-And-Rituals/`
- User Stories: `2-Methods/4-Execution/2-User-Stories/`
- PRDs: `2-Methods/4-Execution/4-PRD/`
- Personas: `2-Methods/4-Execution/5-Personas/`
- Metrics: `2-Methods/4-Execution/6-Metrics/`

### 5-Communication (Keep aligned)
- Newsletters: `2-Methods/5-Communication/1-Newsletter/`
- One-Pagers: `2-Methods/5-Communication/3-One-Pagers/`
- Stakeholder Management: `2-Methods/5-Communication/7-Stakeholder-Management/`
- Saying No: `2-Methods/5-Communication/6-Saying-No/`
- Politics & organization survival: use the `politics-coach` skill with `1-Context/1.1-Stakeholder-Avatars/` (person-level avatars) and `1-Context/1.2-Organization-Survival/` (system-level politics: power map, alliances, red flags) when stakeholder problems are clearly political, not just about message shape.

## Typical File Patterns

Most framework folders follow this structure:
- `1-*-framework.md` - Guide explaining the framework
- `2-*-template.md` - Template to fill out
- `3-*-evaluation.md` - Assessment criteria

## Braindumping Workflow

When a user wants to work on something or is thinking/braindumping (the agent is in **product_sense**): **apply the golden rule from `coaching/braindump.md`** (braindump before structure), including the "braindump sufficient" checklist. Use prompts from `../../coaching/prompts.md` for the relevant context (PRD, prioritization, strategy, research, stuck).

1. **Listen and probe**
   - Ask if the user has added (or should add) relevant context from [1-Context/](../../../1-Context/README.md), [4-Research/](../../../4-Research/README.md), or [3-Work/](../../../3-Work/README.md); having it in the conversation speeds up thinking.
   - What's the core problem or opportunity?
   - What stage are they at → (ideation, validation, building, shipping)
   - What constraints exist?

2. **Guide exploration** (do not suggest templates yet)
   - Use prompts from `coaching/prompts.md` to surface assumptions and blind spots
   - Ask clarifying questions from the relevant framework
   - Help organize scattered thoughts only after raw thinking is out

3. **Suggest framework** (only after braindump / when leaving product_sense into execution_mode)
   - Match their need to the right framework location
   - Show the framework guide first (1-*-framework.md)
   - Only then point to the template (2-*-template.md)

## Modes & evals

Routing, state transitions, and when to load context live in [ORCHESTRATION.md](../../ORCHESTRATION.md). This skill is the **framework-library navigation layer** — use it to find the right folder and file for a given topic; use ORCHESTRATION.md to know which mode you're in and what to do next.

## Common Scenarios

### "I have an idea"
→ Start with **Discovery** (use `discovery-research` skill):
- Problem-Solution Space to separate problem from solution
- Jobs-to-be-Done to understand user needs
- Opportunity Assessment to evaluate viability

### "I need to prioritize features"
→ Go to **Strategy** (use `strategy-planning` skill):
- Prioritization frameworks (RICE, Value/Effort, MoSCoW)
- Strategic Foundations for alignment with goals

### "I need to write a PRD"
→ Check in **Execution**:
- Before touching templates, ask **2–3 lightweight preflight questions** (why this/why now, know vs guess, who it’s for) and a **context/memory check**, for example:
  - "Why this, why now?"
  - "What do you already know vs what are you guessing?"
  - "Who is this primarily for to read and approve?"
  - "Do you want to anchor this in any existing strategy/initiative/research, or keep this PRD self-contained for now?"
- PRD templates and guides
- User Stories for requirements
- Metrics for success criteria

### "How do I convince stakeholders?"
→ Look in **Communication** (use `stakeholder-management` skill; add `politics-coach` when dynamics are clearly political):
- One-Pagers for executive summaries
- Stakeholder Management strategies
- Saying No frameworks for managing requests

### "I'm stuck / not sure how to think about this"
→ Start with **Foundations**:
- Mental Models for frameworks
- Bias awareness for blind spots
- Self-Reflection for clarity

### "I'm overwhelmed with requests"
→ Treat this as an **overwhelm / paralysis** case:
- First, acknowledge the feeling and keep cognitive load low.
- Ask **at most 1–2 gentle questions** to narrow, for example: "What’s one thing that, if you made a bit of progress on it this week, would make you feel less stuck?"
- Help the user choose a **tiny, concrete next step** (e.g. "open the first onboarding email and jot 3 bullets on what feels off") instead of introducing mini-frameworks.
- Make explicit that **they choose**: "You choose the smallest step that feels doable; I’ll help you shape it."

### "Am I improving → / How do I track my judgment?"
→ Point to **5-Growth**:
- **Product Judgment Test**: `5-Growth/3-Product-Judgment-Test/` — log forecasts (prediction + confidence %) *before* shipping, resolve when data is in, track Weighted Brier Score for calibration
- Learning log and growth portfolio: `5-Growth/1-Learning-Log/`, `5-Growth/2-Growth-Portfolio/`

## Response Guidelines

1. **Always cite source paths** - e.g., "From `2-Methods/4-Execution/4-PRD/2-prd-template.md`"

2. **Read files before suggesting** - Don't guess what's in a framework; read it first

3. **Think → Structure → Template** - Never jump straight to templates

4. **Follow the flow** - Respect the natural progression (Foundations → Strategy → Discovery → Execution → Communication)

5. **Cross-reference related frameworks** - PMs benefit from connecting concepts

6. **Be actionable** - Point to specific next steps, not just information

## Storage Locations

- **Personal practice & evidence**: `5-Growth/` (daily log, learning log, growth portfolio, Product Judgment Test)
- **Company context**: `1-Context/`
- **Methods & frameworks**: `2-Methods/`
- **Research artifacts**: `4-Research/`
- **Active initiatives**: `3-Work/`

## Example Interactions

**User:** "I want to assess if we should build a new feature"
**Response:**
1. Ask: What problem does it solve → For whom?
2. Guide to: `2-Methods/3-Discovery/4-Opportunity-Assessment/`
3. Read framework guide first, then suggest template
4. Cross-reference: Problem-Solution Space, JTBD

**User:** "Help me write a PRD"
**Response:**
1. Before template, ask: What have you learned from discovery → What metrics matter?
2. Point to: `2-Methods/4-Execution/4-PRD/`
3. Also reference: User Stories, Personas, Metrics

**User:** "I'm overwhelmed with requests"
**Response:**
1. Explore the situation
2. Point to: `2-Methods/5-Communication/6-Saying-No/`
3. Cross-reference: Prioritization frameworks, Stakeholder Management

## Notes

- This repository is git-versioned - changes are tracked
- Templates are starting points, not rigid requirements
- Frameworks are tools for thinking, not bureaucracy
- The best PMs adapt frameworks to their context
