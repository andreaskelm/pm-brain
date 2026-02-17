# Initiatives — Early Thinking & Opportunity Assessment

## Introduction

This directory is your starting point for capturing early initiative thinking before you have evidence. Use the opportunity assessment template (based on the framework in [02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/](../02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/README.md)) to document hypotheses, assumptions, and initial ideas. Once you have enough clarity, move to the discovery frameworks in [02-Methods-and-Tools/2.2-Discovery/](../02-Methods-and-Tools/2.2-Discovery/README.md) to validate your thinking with evidence.

**For agents:** This folder is one of the context sources the PM Brain agent asks about early in product_sense (and when starting execution_mode for non-trivial docs). If the user has not added relevant initiative context, suggest adding or @-mentioning key docs from here (e.g. opportunity assessment, PRD, roadmap for the initiative); having them in context speeds up thinking and keeps answers aligned to active work. 

**Critical agent guidance:** When users share research/discovery insights specific to an initiative, **always guide them to save a document** in `04-Initiatives/[initiative-name]/research/` (e.g. interview snapshots, synthesis summaries, key findings). For raw data (transcripts, recordings, large files), guide users to store externally (Google Drive, SharePoint, Teams) and link to that source from the analysis doc. Paths below are from repo root.

**This is for:** Early ideas, hypotheses, and initial opportunity assessments  
**When ready:** Move to discovery methods in [02-Methods-and-Tools/2.2-Discovery/](../02-Methods-and-Tools/2.2-Discovery/README.md) for evidence-based discovery

## How This Relates to Frameworks

**Early Thinking (This Directory):**
- Capture initial ideas and hypotheses
- Document what you know vs. what needs research
- Identify key questions to validate

**Discovery Frameworks ([02-Methods-and-Tools/2.2-Discovery/](../02-Methods-and-Tools/2.2-Discovery/README.md)):**
- Use [2.2.4-Opportunity-Assessment/](../02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) to structure your opportunity assessment (this template is based on that framework)
- Validate assumptions with user interviews (see [2.2.1-Research-Interviews/](../02-Methods-and-Tools/2.2-Discovery/2.2.1-Research-Interviews/README.md))
- Synthesize patterns from evidence (see [2.2.2-Continuous-Discovery-Habits/](../02-Methods-and-Tools/2.2-Discovery/2.2.2-Continuous-Discovery-Habits/README.md))
- Frame problems as jobs (see [2.2.3-Jobs-To-Be-Done/](../02-Methods-and-Tools/2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md))
- Generate and validate solutions (see [2.2.5-Idea-Validation/](../02-Methods-and-Tools/2.2-Discovery/2.2.5-Idea-Validation/README.md))
- Write PRDs (see [2.3.4-PRD/](../02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/README.md))

**The Flow:**
1. Start here with opportunity assessment (early thinking)
2. Move to discovery frameworks when ready to validate
3. Return here to document your actual initiative as it evolves

## How to Use This Directory

1. Create a new initiative folder when you have an early idea
2. Use the opportunity assessment template to document your thinking
3. Identify what needs validation (move to discovery frameworks)
4. As you learn, update the opportunity assessment
5. When validated, create PRD and roadmap documents

## Quick start: self-quiz + AI collaboration

Use this to get unstuck fast, challenge assumptions, and move from thoughts → evidence → decisions.

- How it works:
  - You paste the prompt below into the model.
  - You paste your latest notes.
  - The model quizzes you section-by-section, fills gaps, and challenges assumptions.
  - You iterate until confident enough to move into a PRD/roadmap.

### Reusable prompt (copy-paste)

```markdown
Act as a product management coach. We'll work iteratively and challenge assumptions. Your role is to help me think, not to think for me. I may switch between multiple languages (e.g. [Primary Language] and English). Keep content, quotes, and context in the original language, but translate important highlights to English when helpful. If I use mixed language, maintain it unless I ask you to standardize.

0) FIRST: Help me braindump (don't structure yet):
- Ask me to dump everything I know about this initiative - thoughts, concerns, ideas, gut feelings
- Don't ask me to structure it yet. Just get it all out.
- Ask: "What's your product sense telling you? What feels right or wrong?"
- Ask: "What assumptions are you making? List them all."
- Ask: "What biases might be affecting your view?" (Confirmation bias? Solution bias? Sunk cost?)

1) THEN: Quiz me section-by-section on:
- Objective
- Target customer
- Success metrics
- What we know
- What we should research
- Solution ideas
- Risks and questions to validate
- Next steps
- Links & artifacts

2) For each section:
- DON'T just ask me to paste notes. First ask: "Before looking at your notes, what do you think about [section]? What's your gut feeling?"
- Ask 3–7 sharp questions that make me think.
- Challenge my thinking: "What biases might be affecting this? What would someone with different product sense say?"
- Help me use my product sense: "What does your intuition tell you here? What feels off?"
- Only then propose initial draft answers based on my notes; clearly mark gaps as [to fill].
- Challenge assumptions and call out confidence (High/Med/Low).
- Suggest 1–3 fast experiments or research tasks with effort/impact.
- Keep answers concise and skimmable.

3) End each pass with:
- Ask me to reflect: "What did you learn? How did your thinking evolve? What surprised you?"
- Updated section summaries
- Top 3 decision points
- Next 3 actions with owners/dates placeholders
- A minimal decision log entry if we made a call
- Self-reflection: "What biases did you catch? What would you do differently?"

I'll paste my notes now. But first, help me braindump.
```

### How to use it
1) Paste the prompt. 2) Paste your current notes. 3) Answer questions; ask for revisions. 4) When stable, copy outputs into this README’s template or `prd.md`.

---

## What to include in each initiative folder

Use a lightweight but consistent structure. Add/remove to fit scope.

```text
pm-brain/04-Initiatives/
  [INIT-CODE]/
    opportunity-assessment.md  # Opportunity assessment (this template)
    summary.md                 # 1-pager exec summary
    prd.md                     # Full PRD (when ready)
    roadmap.md                 # Milestones/timeline
    decisions.md               # Decision log (date, context, decision, owner)
    risks.md                   # Key risks + mitigations
    research/
      interviews/              # Interview snapshots, synthesis, insights (markdown docs)
      data/                    # Analysis summaries, queries, charts (markdown docs)
      experiments/             # Hypotheses, plans, results (markdown docs)
      links.md                 # Links to external raw data (transcripts, recordings in Google Drive/SharePoint/Teams)
    stakeholders/
      insights.md              # Who cares, needs, influence (initiative-level view)
      comms.md                 # Cadence, updates, audiences, and how this initiative shows up in communication and politics
    metrics/
      north-star.md            # Metrics tree, targets, guardrails
      dashboard-links.md       # BI links, definitions
    compliance/                # Regulatory, audit, approvals
    architecture/              # Diagrams, integration points
    retrospective.md           # Post-mortem after major phase
    lessons-learned.md         # Reusable learnings
    assets/                    # Visuals (SVG only)
```

- Recommended docs:
  - opportunity-assessment.md: living opportunity assessment.
  - summary.md: narrative and key numbers for execs.
  - prd.md: scope, requirements, acceptance criteria.
  - roadmap.md: milestones, dependencies, risks.
  - decisions.md: one-line entries; link to context.
  - research/*: **Save analysis as markdown documents** (interview snapshots, synthesis, insights, experiment results). Store raw data (transcripts, recordings, large files) externally (Google Drive/SharePoint/Teams) and link in `research/links.md`.
  - stakeholders/*: stakeholder map, Comms plan, and initiative-level politics notes. Use this together with company-level stakeholders (`01-Company-Context/6-company-stakeholders.md`), stakeholder avatars (`01-Company-Context/1.1-Stakeholder-Avatars/`), and Org Survival docs (`01-Company-Context/1.2-Org-Survival/`) when you're pressure-testing "who gets surprised" and "who can block this".
  - metrics/*: targets, dashboards, definitions.
  - compliance/, architecture/: use as needed.
  - retrospective.md, lessons-learned.md: after major delivery.

---

## How to Use This Template

1. **Start Early**: Create opportunity assessment when you have an initial idea or hypothesis
2. **Document What You Know**: Fill out sections with current knowledge; mark unknowns explicitly
3. **Identify Research Needs**: Use "What we should research" section to plan validation
4. **Move to Discovery**: When ready, use discovery methods in [02-Methods-and-Tools/2.2-Discovery/](../02-Methods-and-Tools/2.2-Discovery/README.md) to validate assumptions. Start with [2.2.4-Opportunity-Assessment/](../02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) (this template is based on that framework)
5. **Update as You Learn**: Return to update opportunity assessment with new evidence
6. **Transition to Execution**: When validated, create PRD using [2.3.4-PRD/](../02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/README.md) and roadmap documents

## How to Maintain

- **Weekly Updates**: Update as you learn new information or make decisions
- **After Discovery**: Update with evidence from interviews and research
- **After Validation**: Update with validation results and next steps
- **Archive**: Move completed initiatives to archive or mark as complete

---

## Opportunity Assessment Template

# [Initiative Working Title]

## Objective
- What outcome are we trying to achieve and why now?
- Business value hypothesis (e.g., revenue, risk reduction, cost, speed).
- Time horizon and exit criteria (what “good” looks like).

## Target customer
- Primary customer/user segment and context (JTBD, key workflows).
- Stakeholders impacted (internal/external) and success definition for each.
- Where/how we’ll reach them (channels, touchpoints).

## Success metrics
- Leading indicators:
  - [Metric] — baseline: [x], target: [y] by [date]
- Lagging outcomes:
  - [Metric] — baseline: [x], target: [y] by [date]
- Guardrails (e.g., compliance, risk appetite, experience thresholds).

## What we know
- Facts and evidence (link sources: data, interviews, prior initiatives).
- Constraints (regulatory, technical, operational, capacity).
- Assumptions with confidence level (e.g., High/Med/Low).

## What we should research
- Key questions/hypotheses to validate.
- Methods (interviews, data analysis, discovery experiments, prototypes).
- Participants, sample size, and timeline.
- Decision criteria (what would change our mind; kill/pivot/commit thresholds).

## Solution ideas
- Concept 1: [one-liner] — first slice MVP scope.
- Concept 2: [one-liner] — alternative approach.
- Out of scope (for now) to protect focus.

## Risks and questions to validate
- Desirability (customer value, adoption risks).
- Viability (commercial model, business impact, go-to-market).
- Feasibility/Tech (integration, scalability, data availability).
- Usability (flow, UX, accessibility).
- Compliance/Legal (market rules, privacy, auditability).
- Dependencies (teams, vendors, data sources, timelines).
- Unknowns/Red flags and how we’ll de-risk.

## Next steps
- [Owner] → [action] by [date]
- [Owner] → [action] by [date]

## Links & artifacts
- Research notes: [...]
- Data/dashboard: [...]
- Stakeholders & communication rhythm: [...]
- Decision log: [...]
