# Methods index

**Think first:** [system/coaching/README.md](../system/coaching/README.md). **Evaluate an artifact:** [system/EVALUATION.md](../system/EVALUATION.md) and the `evaluate-artifact` skill.

Workflows live in **Agent Skills** (`.claude/skills/`). Skills own templates, steps, and quality criteria. What stays under `2-Methods/` is reference you read to think: mental models, org-reality playbooks, and long-form guides (e.g. full Strategy Blocks process).

---

## Agent skills (start here for “help me do X”)

| I need to… | Skill |
|------------|--------|
| Think through a decision, unstuck | `braindump` |
| Weekly plan + drift sweep + draft weekly note | `weekly-review` |
| Score or tighten a draft artifact | `evaluate-artifact` |
| Review repo files for freshness / consistency | `brain-review` (slash-only) |
| Write or tighten a PRD / spec | `write-prd` |
| Prioritize backlog, MVP, ranking | `prioritize` |
| Assess an idea before a PRD | `opportunity-assessment` |
| Interviews, synthesis, JTBD, PMF, personas | `discovery-synthesis` |
| OKRs, check-ins, grading | `okr` |
| Roadmap, Now/Next/Later | `roadmap` |
| North Star, metrics, AARRR | `north-star` |
| Strategy (GSBS, Playing to Win, pillars) | `strategy` |
| One-pagers, updates, escalation, saying no | `stakeholder-comms` |
| Politics, power, simulate a stakeholder | `politics-coach` |

Install path for upstream: `npx skills add andreaskelm/pm-brain` (skills ship in `.claude/skills/`).

---

## Reference only (read in 2-Methods)

| Topic | Where |
|--------|--------|
| Mental models, bias, calibration, self-reflection | [1-Foundations/](1-Foundations/README.md) → [0-index](1-Foundations/0-index.md) |
| Full org strategy process (8–12 weeks) | [Strategy Blocks full guide](2-Strategy/1-Strategic-Foundations/1-Strategy-Blocks/1-full-guide.md) |
| Crisis communication | [5-Communication/4-Crisis-Management/](5-Communication/4-Crisis-Management/) |
| Stakeholder management (narrative + scenarios) | [5-Communication/7-Stakeholder-Management/](5-Communication/7-Stakeholder-Management/) |
| Stakeholder avatars (template) | [5-Communication/8-Stakeholder-Avatars/](5-Communication/8-Stakeholder-Avatars/) |
| Daily / weekly rituals (human cadence) | [4-Execution/1-Daily-Execution-And-Rituals/](4-Execution/1-Daily-Execution-And-Rituals/) |
| 10 Things workshop | [4-Execution/8-10-Things-Workshop/](4-Execution/8-10-Things-Workshop/) |
| Writing a new PM Brain skill | [0-writing-a-skill.md](0-writing-a-skill.md) |

---

## Topics → skill or reference

| Topic | Use |
|--------|-----|
| Bias | [1-Foundations/2-Bias/](1-Foundations/2-Bias/) |
| Decision-making, pre-mortems, assumptions | [1-Foundations/1-Mental-Models/1-Decision-Making/](1-Foundations/1-Mental-Models/1-Decision-Making/) |
| Discovery / research | `discovery-synthesis` skill |
| Opportunity assessment | `opportunity-assessment` skill |
| PRD / user stories | `write-prd` skill |
| Prioritization / backlog | `prioritize` skill |
| OKRs / roadmap / North Star | `okr`, `roadmap`, `north-star` skills |
| Metrics / AARRR | `north-star` skill → `references/metrics.md` |
| Strategy doc | `strategy` skill; org process → Strategy Blocks guide |
| Stakeholder comms | `stakeholder-comms` skill |
| Escalation / saying no | `stakeholder-comms` → `references/escalation-saying-no.md` |
| Product sense coaching | [system/coaching/](../system/coaching/README.md) |

---

**Agent note:** On doc requests, load the matching skill’s `SKILL.md` first. Preflight: 2–3 questions from [system/coaching/prompts.md](../system/coaching/prompts.md) unless the user already braindumped. Criteria for scoring live in each skill’s `references/criteria.md` (or `criteria-one-pager.md` for one-pagers).
