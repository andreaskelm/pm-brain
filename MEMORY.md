# Sleeping Memory — What to Wake When

**What this file is:** The **sleeping memory manifest**: it lists context that lives in the repo but is not in the active prompt until "woken"—loaded when the conversation touches that area. The agent uses this to decide what to load. Orchestration: [ORCHESTRATION.md](ORCHESTRATION.md) → Context Loading Strategy.

**Concept:** Content in 01-Company-Context, 03-Research-Artifacts, 04-Initiatives, and platform-specific config (rules, skills, evals) is **sleeping memory**. The agent wakes it by loading the right files when the user mentions company strategy, an initiative, research, or when personalization/behavior rules are relevant.

**Platform note:** Paths below assume the default repo layout. On **Cursor**, `.cursor/rules/` and `.cursor/skills/` are auto-loaded by the IDE. On **other platforms** (Claude Code, Claude.ai, Replit, etc.), load the referenced content manually when needed — see [docs/setup.md](docs/setup.md) → Platform Setup for how.

---

## When to Wake What

| Trigger (user mentions or topic) | Wake (load or reference) |
|----------------------------------|--------------------------|
| Company, strategy, vision, roadmap, stakeholders, org | [01-Company-Context/](01-Company-Context/README.md) (see below); start with [CONTEXT.md](01-Company-Context/CONTEXT.md) for name/company/team |
| A specific initiative or "my initiative", "current bet" | 04-Initiatives/[initiative-name]/ (see below) |
| Research, interviews, discovery, evidence, user insights | [03-Research-Artifacts/](03-Research-Artifacts/README.md) or 04-Initiatives/[name]/research/ |
| Personalization (who I am, my team, my style) | [01-Company-Context/CONTEXT.md](01-Company-Context/CONTEXT.md), [.cursor/rules/thinking.personal.mdc](.cursor/rules/thinking.personal.mdc) |
| How to evaluate artifacts / when to run evals | [.cursor/rules/evaluation-orchestration.mdc](.cursor/rules/evaluation-orchestration.mdc), [.cursor/evals/](.cursor/evals/README.md) |
| Template finder / which doc to use | [02-Methods-and-Tools/0-template-finder.md](02-Methods-and-Tools/0-template-finder.md) |
| Product sense / braindump / golden rule | [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md), [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md), [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) |
| Repo structure, refactoring, architecture, adding files, reorganizing | [docs/architecture.md](docs/architecture.md) → Design Principles section |

---

## Company Context (01-Company-Context)

**When to wake:** User talks about company direction, strategy, vision, roadmap, stakeholders, BU/team structure, or context check asks for company context.

**Key paths (customize to your structure; may live in BU/team subfolders):**

| Purpose | Path |
|---------|------|
| Personalization (name, company, team/BU) | [01-Company-Context/CONTEXT.md](01-Company-Context/CONTEXT.md) |
| Setup / org structure | [01-Company-Context/SETUP.md](01-Company-Context/SETUP.md) |
| Vision | 01-Company-Context/1-company-vision.md (or BU/team equivalent) |
| Strategy | 01-Company-Context/2-company-strategy.md (or BU/team equivalent) |
| Principles | 01-Company-Context/3-company-product-principles.md |
| Portfolio | 01-Company-Context/4-company-product-explanation.md |
| Roadmap | 01-Company-Context/5-company-roadmap.md |
| Stakeholders | 01-Company-Context/6-company-stakeholders.md |
| Overview | [01-Company-Context/README.md](01-Company-Context/README.md) |

---

## Initiatives (04-Initiatives)

**When to wake:** User mentions working on or thinking about a specific initiative (by name or "my initiative", "current bet").

**Pattern:** One folder per initiative under `04-Initiatives/`. List subfolders to discover initiative names (e.g. `4.1-Initiative-Codename`).

**Suggested files per initiative (load as relevant):**

- README.md — overview
- opportunity-assessment.md
- prd.md
- decisions.md
- roadmap.md
- summary.md
- research/ — initiative-specific research artifacts (if present)

**Index:** See [04-Initiatives/README.md](04-Initiatives/README.md). To list initiatives, use the filesystem or README; paths are `04-Initiatives/<folder-name>/<file>.md`.

---

## Research Artifacts (03-Research-Artifacts)

**When to wake:** User refers to past research, interviews, synthesis, or evidence they want to use in thinking or a doc.

**Structure:**

- [03-Research-Artifacts/README.md](03-Research-Artifacts/README.md) — how research is stored, when to use 03 vs 04-Initiatives/[name]/research/
- 03-Research-Artifacts/3.1-User-Interviews/ — interview-related artifacts
- 03-Research-Artifacts/3.2-Qualitative-Research/ — qualitative research artifacts

Store analysis/snapshots here (or in initiative research/); raw data external with links.

---

## Rules (.cursor/rules)

**When to wake:** Agent needs to know evaluation behavior, template-finder behavior, product-sense behavior, or user's thinking preferences.

| File | Purpose |
|------|---------|
| voice.mdc | Communication style: tone, structure, endings, situational angles (on Cursor: always loaded automatically) |
| evaluation-orchestration.mdc | When to run Quick Quality Checks and full evals during artifact creation |
| template-finder.mdc | When user asks for a specific doc; route to 0-template-finder |
| product-sense.mdc | Golden rule, braindump before structure for product topics |
| thinking.mdc | High-level how the user wants AI to support thinking/work |
| thinking.personal.mdc | Personal working style preferences (depth, pace, etc.) |

---

## Evals

**When to wake:** Agent needs eval functions for transition checks, agent-behavior guide for Level 2 evals, or test cases for replay.

| File | Purpose |
|------|---------|
| .cursor/evals/eval-functions.md | check_braindump_sufficient, check_questions_before_framework, match_scenario_type — used at state transitions |
| .cursor/evals/1-agent-behavior-guide.md | Level 2 agent behavior review: dimensions, reflection checklist, "where to update" map |
| .cursor/evals/2-checklist.md | When to run Level 1/2 evals, ongoing rhythm |
| .cursor/evals/agent-behavior-scenarios.json | Reference scenarios for matching conversation types (agent does not read directly) |
| .cursor/evals/test-generator.md | How to turn scenarios into test cases |
| .cursor/evals/eval-results/ | Log storage for eval results and test cases |

---

## Skills (.cursor/skills)

**When to wake:** User is in product_sense or execution_mode and needs framework selection or workflow guidance.

| Path | Purpose |
|------|---------|
| [.cursor/skills/pm-brain-workflow/SKILL.md](.cursor/skills/pm-brain-workflow/SKILL.md) | Overall PM workflow: Foundations → Strategy → Discovery → Execution → Communication; high-level routing. |
| [.cursor/skills/discovery-research/SKILL.md](.cursor/skills/discovery-research/SKILL.md) | Discovery workflows: research interviews, continuous discovery, JTBD, opportunity assessment, idea validation, problem/solution space, PMF. |
| [.cursor/skills/strategy-planning/SKILL.md](.cursor/skills/strategy-planning/SKILL.md) | Strategy and planning: strategy docs, OKRs, roadmaps, prioritization. |
| [.cursor/skills/stakeholder-management/SKILL.md](.cursor/skills/stakeholder-management/SKILL.md) | Stakeholder comms: one-pagers, newsletters, stakeholder management, saying no, escalation, crisis management. |

---

## Summary

- **Company / strategy / org** → 01-Company-Context (CONTEXT.md first, then vision/strategy/roadmap/stakeholders as needed).
- **Initiative** → 04-Initiatives/[initiative-name]/ (opportunity-assessment, prd, decisions, roadmap, summary).
- **Research / evidence** → 03-Research-Artifacts or 04-Initiatives/[name]/research/.
- **Personalization** → [01-Company-Context/CONTEXT.md](01-Company-Context/CONTEXT.md), [.cursor/rules/thinking.personal.mdc](.cursor/rules/thinking.personal.mdc).
- **Evals / template finder / product sense** → See [ORCHESTRATION.md](ORCHESTRATION.md) and the rules/skills/evals sections above.

Do not load everything at once. Wake only what the conversation needs.
