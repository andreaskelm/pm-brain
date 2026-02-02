# Opportunity Assessment Framework

## Overview

An opportunity assessment helps you structure early thinking about a potential product initiative. It captures what you know, what you assume, and what needs validation before committing resources to build.

**Purpose:** Bridge the gap between initial idea and evidence-based discovery.

## Core Principles

### 1. Document Assumptions Explicitly
- Mark all assumptions with confidence levels (High/Med/Low) - this helps you know what to validate
- Distinguish between facts and hypotheses
- Identify what would change your mind
- **Note:** Confidence here refers to your confidence in the assumption being true, which helps prioritize validation

### 2. Focus on Outcomes, Not Solutions
- Start with the problem/opportunity, not the solution
- Define success metrics before proposing solutions
- Keep solution ideas high-level initially

### 3. Plan Validation Before Building
- Identify key questions to answer
- Define decision criteria (kill/pivot/commit thresholds)
- Link to discovery methods you'll use

### 4. Make It Living
- Update as you learn
- Return after discovery to refine
- Use evidence to replace assumptions

## Framework Structure

### Objective
**What to capture:**
- What outcome are you trying to achieve and why now?
- Business value hypothesis (revenue, risk reduction, cost, speed)
- Time horizon and exit criteria (what "good" looks like)

**Why it matters:** Clarifies the "why" before the "what" or "how"

### Target Customer
**What to capture:**
- Primary customer/user segment and context (JTBD, key workflows)
- Stakeholders impacted (internal/external) and success definition for each
- Where/how you'll reach them (channels, touchpoints)

**Why it matters:** Ensures you know who you're building for before building

### Success Metrics
**What to capture:**
- Leading indicators (early signals of progress)
- Lagging outcomes (ultimate business impact)
- Guardrails (compliance, risk appetite, experience thresholds)

**Why it matters:** Defines how you'll measure success before you start

### What We Know
**What to capture:**
- Facts and evidence (link sources: data, interviews, prior initiatives)
- Constraints (regulatory, technical, operational, capacity)
- Assumptions with confidence level (High/Med/Low)

**Why it matters:** Separates what's certain from what's uncertain

### What We Should Research
**What to capture:**
- Key questions/hypotheses to validate
- Methods (interviews, data analysis, discovery experiments, prototypes)
- Participants, sample size, and timeline
- Decision criteria (what would change your mind; kill/pivot/commit thresholds)

**Why it matters:** Creates a research plan before jumping to solutions

### Solution Ideas
**What to capture:**
- Concept 1: [one-liner] — first slice MVP scope
- Concept 2: [one-liner] — alternative approach
- Out of scope (for now) to protect focus

**Why it matters:** Keeps solution thinking high-level until validated

### Risks and Questions to Validate
**What to capture:**
- Desirability (customer value, adoption risks)
- Viability (commercial model, business impact, go-to-market)
- Feasibility/Tech (integration, scalability, data availability)
- Usability (flow, UX, accessibility)
- Compliance/Legal (market rules, privacy, auditability)
- Dependencies (teams, vendors, data sources, timelines)
- Unknowns/Red flags and how you'll de-risk

**Why it matters:** Identifies risks early so you can plan mitigation

## How to Use This Framework

### Step 1: Initial Assessment
1. Copy the template from `2-opportunity-assessment-template.md`
2. Fill in what you know with current knowledge
3. Mark unknowns explicitly with `[to fill]` or `[unknown]`
4. Identify assumptions and assign confidence levels

### Step 2: Plan Research
1. Use "What we should research" to create a research plan
2. Link to discovery methods you'll use (interviews, validation experiments)
3. Define decision criteria for kill/pivot/commit decisions

### Step 3: Conduct Discovery
1. Use discovery frameworks in this domain (e.g., `../2.2.1-Research-Interviews/`, `../2.2.2-Continuous-Discovery-Habits/`) to validate assumptions
2. Store research artifacts in `03-Research-Artifacts/`
3. Update opportunity assessment as you learn

### Step 4: Make Decisions
1. Use decision criteria to determine next steps
2. Update opportunity assessment with findings
3. Move to PRD/roadmap when validated, or kill/pivot if not

## Common Pitfalls

**Too solution-focused too early**
- Problem: Jumping to solutions before understanding the problem
- Solution: Focus on outcomes and customer needs first

**Not updating with evidence**
- Problem: Opportunity assessment becomes stale
- Solution: Update weekly or after each discovery activity

**Vague assumptions**
- Problem: "We assume customers want this" without confidence level
- Solution: Mark all assumptions with High/Med/Low confidence (your confidence the assumption is true - helps prioritize validation)

**No decision criteria**
- Problem: Never clear when to kill, pivot, or commit
- Solution: Define thresholds upfront (e.g., "If <30% of interviews show need, kill")

## Quick start: self-quiz + AI collaboration

Use this to get unstuck fast, challenge assumptions, and move from thoughts → evidence → decisions.

- How it works:
  - You paste the prompt below into the model.
  - You paste your latest notes.
  - The model quizzes you section-by-section, fills gaps, and challenges assumptions.
  - You iterate until confident enough to move into a PRD/roadmap.

```markdown
Act as a product management coach. Help me think through my opportunity assessment. Your role is to help me think, not to think for me. We'll work iteratively and challenge assumptions. I may switch between multiple languages (e.g. [Primary Language] and English). Keep content, quotes, and context in the original language, but translate important highlights to English when helpful. If I use mixed language, maintain it unless I ask you to standardize.

0) FIRST: Help me braindump (don't structure yet):
- Ask me to dump everything I know about this opportunity - thoughts, concerns, ideas, gut feelings
- Don't ask me to structure it yet. Just get it all out.
- Ask: "What's your product sense telling you? What feels right or wrong?"
- Ask: "What assumptions are you making? List them all."
- Ask: "What biases might be affecting your view?"

1) THEN: Quiz me section-by-section on:
- Objective
- Target customer
- Success metrics
- What we know
- What we should research
- Solution ideas
- Risks and questions to validate

2) For each section:
- DON'T just ask me to paste notes. First ask: "Before looking at your notes, what do you think about [section]? What's your gut feeling?"
- Ask 3–7 sharp questions that make me think
- Challenge my thinking: "What biases might be affecting this? What would someone with different product sense say?"
- Help me use my product sense: "What does your intuition tell you here? What feels off?"
- Only then propose initial draft answers based on my notes; clearly mark gaps as [to fill]
- Challenge assumptions and call out confidence (High/Med/Low)
- Suggest 1–3 fast experiments or research tasks

3) End with:
- Ask me to reflect: "What did you learn? How did your thinking evolve? What surprised you?"
- Updated section summaries
- Top 3 decision points
- Next 3 actions with owners/dates placeholders
- Self-reflection: "What would you do differently? What biases did you catch?"
```

-----

## References

- Opportunity Assessment Template: `2-opportunity-assessment-template.md`
- Research Interviews: `../2.2.1-Research-Interviews/README.md`
- Continuous Discovery Habits: `../2.2.2-Continuous-Discovery-Habits/README.md`
- Jobs To Be Done: `../2.2.3-Jobs-To-Be-Done/README.md`
- Idea Validation: `../2.2.5-Idea-Validation/README.md`
- Problem-Solution Space: `../2.2.6-Problem-Solution-Space/README.md`
- Execution: `../../2.3-Execution/README.md` (PRD Framework)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)

