---
name: strategy-planning
description: Support strategy, OKR, roadmap, and prioritization work using PM Brain’s strategy frameworks.
---

# Strategy & Planning Skill

Use this skill when the user is deciding **where to go** and **what bets to make**: vision, strategy docs, OKRs, roadmaps, prioritization, and strategic tradeoffs.

## When to use this skill

Trigger this skill (usually in product_sense or execution_mode) when the user:

- Says things like:
  - “I need to write a strategy doc”
  - “I’m planning H2 / next year”
  - “I need to create OKRs / a roadmap”
  - “I’m not sure which bets to prioritize”
  - “I’m stuck between these 2–3 big directions”
- Or explicitly mentions:
  - Strategy, OKRs, roadmap, north star, prioritization

If their main question is **discovery / research**, use `discovery-research`. If it’s mainly about **communication and buy-in**, use `stakeholder-management`.

## Relevant framework locations

Most strategy frameworks live under:

- `02-Methods-and-Tools/2.1-Strategy/`
  - `2.1.1-Strategic-Foundations/`
    - Strategy foundations, good-strategy/bad-strategy, Playing to Win
  - `2.1.2-Strategic-Execution/`
    - `1-OKR/` (OKRs)
    - `2-Roadmap/` (roadmaps)
    - `3-North-Star/` (north star metrics)
    - `4-Prioritization/` (RICE, value/effort, MoSCoW, Kano)

## Typical flows

### 1. “I need a strategy doc”

1. In **product_sense**, clarify:
   - What kind of strategy (growth, market entry, pivot, annual plan)?
   - Who is the audience (execs, peers, team)?
   - What decisions should this doc help them make?
2. Use:
   - `2.1-Strategy/2.1.1-Strategic-Foundations/README.md`
   - And, if helpful, a specific framework like:
     - `2.1.1-Strategic-Foundations/2-Good-Strategy-Bad-Strategy/1-good-strategy-bad-strategy-framework.md`
     - `2.1.1-Strategic-Foundations/3-Playing-To-Win/1-playing-to-win-framework.md`
3. Transition to **execution_mode**:
   - Propose a structure that fits the context (e.g., context → choices → actions).
   - Pull from the user’s braindump to outline the sections.

### 2. “Help me set OKRs”

1. Clarify:
   - Timeframe and scope (team vs org, quarter vs half).
   - How OKRs will be used (alignment vs strict commitment).
2. Point to:
   - `2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/1-okr-framework.md`
3. Then:
   - In **execution_mode**, use `2-okr-template.md` to structure objectives and key results.
   - Use `3-okr-evaluation.md` for a quick quality check before sharing.

### 3. “I need a roadmap”

1. Clarify:
   - Purpose (alignment vs commitment vs exploration).
   - Audience (execs, team, cross-functional partners).
2. Point to:
   - `2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/1-roadmap-framework.md`
3. Help choose:
   - A simple starting format (now/next/later, or quarters with themes).
   - Then use `2-roadmap-template.md` and `3-roadmap-evaluation.md` as needed.

### 4. “I need to prioritize features / bets”

1. Explore:
   - What constraints matter most (capacity, risk, revenue, learning)?
   - Whether they need a **lightweight** or **more rigorous** approach.
2. Use:
   - `2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/decision-tree.md` to pick an approach.
   - RICE, value/effort, MoSCoW, or Kano from that folder as appropriate.

## Response guidelines

1. **Stay in product_sense until the problem is clear**
   - Ask about goals, audience, decisions, and constraints before suggesting frameworks.
2. **Match framework to situation**
   - Use `when-to-use-which.md` in Strategic Foundations where helpful.
3. **Anchor to company context**
   - When relevant, wake:
     - `01-Company-Context/2-company-strategy.md`
     - `01-Company-Context/5-company-roadmap.md`
   - So strategy artifacts align with existing direction.
4. **Be explicit about tradeoffs**
   - When comparing options, help them define decision criteria, not just pick a framework.

## Relation to other skills

- `pm-brain-workflow` decides **where** in the Foundations → Strategy → Discovery → Execution → Communication flow you are.
- `strategy-planning` deepens the **Strategy** slice: strategy docs, OKRs, roadmaps, prioritization.
- Use `discovery-research` when the main need is learning and evidence.
- Use `stakeholder-management` when the main need is alignment and communication.

