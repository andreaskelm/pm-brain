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
2.0 Foundations → 2.1 Strategy → 2.2 Discovery → 2.3 Execution → 2.4 Communication
(HOW TO THINK)  (WHERE TO GO?)  (WHAT TO BUILD?) (BUILD & SHIP)  (KEEP ALIGNED)
```

**When user is:**
- Early/exploring → Point to **2.0 Foundations** and **2.1 Strategy**
- Has a problem → Guide to **2.2 Discovery**
- Ready to build → Move to **2.3 Execution**
- Throughout → Support with **2.4 Communication**

## Quick Framework Locations

### 2.0 Foundations (How to Think)
- Mental Models: `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/`
- Bias Awareness: `02-Methods-and-Tools/2.0-Foundations/2.0.2-Bias/`
- Self-Reflection: `02-Methods-and-Tools/2.0-Foundations/2.0.3-Self-Reflection/`

### 2.1 Strategy (Where are we going?)
- Strategic Foundations: `02-Methods-and-Tools/2.1-Strategy/2.1.1-Strategic-Foundations/`
- OKRs: `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/`
- Roadmaps: `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/`
- North Star: `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/3-North-Star/`
- Prioritization: `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/`

### 2.2 Discovery (What to build?)
- Research Interviews: `02-Methods-and-Tools/2.2-Discovery/2.2.1-Research-Interviews/`
- Continuous Discovery: `02-Methods-and-Tools/2.2-Discovery/2.2.2-Continuous-Discovery-Habits/`
- Jobs-to-be-Done: `02-Methods-and-Tools/2.2-Discovery/2.2.3-Jobs-To-Be-Done/`
- Opportunity Assessment: `02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/`
- Problem-Solution Space: `02-Methods-and-Tools/2.2-Discovery/2.2.6-Problem-Solution-Space/`

### 2.3 Execution (Build, ship, measure)
- Daily Rituals: `02-Methods-and-Tools/2.3-Execution/2.3.1-Daily-Execution-And-Rituals/`
- User Stories: `02-Methods-and-Tools/2.3-Execution/2.3.2-User-Stories/`
- PRDs: `02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/`
- Personas: `02-Methods-and-Tools/2.3-Execution/2.3.5-Personas/`
- Metrics: `02-Methods-and-Tools/2.3-Execution/2.3.6-Metrics/`

### 2.4 Communication (Keep aligned)
- Newsletters: `02-Methods-and-Tools/2.4-Communication/2.4.1-Newsletter/`
- One-Pagers: `02-Methods-and-Tools/2.4-Communication/2.4.3-One-Pagers/`
- Stakeholder Management: `02-Methods-and-Tools/2.4-Communication/2.4.7-Stakeholder-Management/`
- Saying No: `02-Methods-and-Tools/2.4-Communication/2.4.6-Saying-No/`

## Typical File Patterns

Most framework folders follow this structure:
- `1-*-framework.md` - Guide explaining the framework
- `2-*-template.md` - Template to fill out
- `3-*-evaluation.md` - Assessment criteria

## Braindumping Workflow

When a user wants to work on something or is thinking/braindumping (the agent is in **product_sense_mode**): **apply the golden rule from `PRODUCT-SENSE-RULES.md`** (braindump before structure), including the \"braindump sufficient\" checklist. Use prompts from `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md` for the relevant context (PRD, prioritization, strategy, research, stuck).

1. **Listen and probe**
   - What's the core problem or opportunity?
   - What stage are they at? (ideation, validation, building, shipping)
   - What constraints exist?

2. **Guide exploration** (do not suggest templates yet)
   - Use prompts from `2-product-sense-prompts.md` to surface assumptions and blind spots
   - Ask clarifying questions from the relevant framework
   - Help organize scattered thoughts only after raw thinking is out

3. **Suggest framework** (only after braindump / when leaving product_sense_mode into execution_mode)
   - Match their need to the right framework location
   - Show the framework guide first (1-*-framework.md)
   - Only then point to the template (2-*-template.md)

## Common Scenarios

### "I have an idea"
→ Start with **Discovery** frameworks:
- Problem-Solution Space to separate problem from solution
- Jobs-to-be-Done to understand user needs
- Opportunity Assessment to evaluate viability

### "I need to prioritize features"
→ Go to **Strategy**:
- Prioritization frameworks (RICE, Value/Effort, MoSCoW)
- Strategic Foundations for alignment with goals

### "I need to write a PRD"
→ Check in **Execution**:
- PRD templates and guides
- User Stories for requirements
- Metrics for success criteria

### "How do I convince stakeholders?"
→ Look in **Communication**:
- One-Pagers for executive summaries
- Stakeholder Management strategies
- Saying No frameworks for managing requests

### "I'm stuck / not sure how to think about this"
→ Start with **Foundations**:
- Mental Models for frameworks
- Bias awareness for blind spots
- Self-Reflection for clarity

### "Am I improving? / How do I track my judgment?"
→ Point to **00-Meta**:
- **Product Judgment Test**: `00-Meta/0.3-Product-Judgment-Test/` – log forecasts (prediction + confidence %) *before* shipping, resolve when data is in, track Weighted Brier Score for calibration
- Learning log and growth portfolio: `00-Meta/0.1-Learning-Log/`, `00-Meta/0.2-Growth-Portfolio/`

## Response Guidelines

1. **Always cite source paths** - e.g., "From `02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/2-prd-template.md`"

2. **Read files before suggesting** - Don't guess what's in a framework; read it first

3. **Think → Structure → Template** - Never jump straight to templates

4. **Follow the flow** - Respect the natural progression (Foundations → Strategy → Discovery → Execution → Communication)

5. **Cross-reference related frameworks** - PMs benefit from connecting concepts

6. **Be actionable** - Point to specific next steps, not just information

## Storage Locations

- **Personal practice & evidence**: `00-Meta/` (daily log, learning log, growth portfolio, Product Judgment Test)
- **Company context**: `01-Company-Context/`
- **Methods & frameworks**: `02-Methods-and-Tools/`
- **Research artifacts**: `03-Research-Artifacts/`
- **Active initiatives**: `04-Initiatives/`

## Example Interactions

**User:** "I want to assess if we should build a new feature"
**Response:**
1. Ask: What problem does it solve? For whom?
2. Guide to: `2.2-Discovery/2.2.4-Opportunity-Assessment/`
3. Read framework guide first, then suggest template
4. Cross-reference: Problem-Solution Space, JTBD

**User:** "Help me write a PRD"
**Response:**
1. Before template, ask: What have you learned from discovery? What metrics matter?
2. Point to: `2.3-Execution/2.3.4-PRD/`
3. Also reference: User Stories, Personas, Metrics

**User:** "I'm overwhelmed with requests"
**Response:**
1. Explore the situation
2. Point to: `2.4-Communication/2.4.6-Saying-No/`
3. Cross-reference: Prioritization frameworks, Stakeholder Management

## Notes

- This repository is git-versioned - changes are tracked
- Templates are starting points, not rigid requirements
- Frameworks are tools for thinking, not bureaucracy
- The best PMs adapt frameworks to their context
