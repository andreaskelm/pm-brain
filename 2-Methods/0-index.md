# Methods index

**Think first:** [system/coaching/README.md](../system/coaching/README.md). **Evaluate an artifact:** [system/EVALUATION.md](../system/EVALUATION.md) and the `evaluate-artifact` skill.

**Agent Skills** (`.claude/skills/`) own the step-by-step workflow when you ask an agent to help. **`2-Methods/`** keeps the full framework library — guides, templates, evaluations — plus mental models and long-form reference (e.g. Strategy Blocks). On doc requests: load the skill first; drill into `2-Methods/` when you need the complete framework or a human-readable template.

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
| AI features, agents, AI evals / HITL | `ai-product-management` |
| A/B tests, experiments, rollout | `experimentation` |
| Eng/design handoff, tech debt | `eng-design-collab` |
| Launch, GTM, rollout comms | `launch-gtm` |

Install path for upstream: `npx skills add andreaskelm/pm-brain` (skills ship in `.claude/skills/`).

---

## Full framework library (browse by domain)

| Domain | README |
|--------|--------|
| Topic → framework map | [1-frameworks-by-topic.md](1-frameworks-by-topic.md) |
| How to think (mental models, bias) | [1-Foundations/](1-Foundations/README.md) → [0-index](1-Foundations/0-index.md) |
| Strategy choices + execution | [2-Strategy/](2-Strategy/README.md) |
| Discovery & research | [3-Discovery/](3-Discovery/README.md) |
| PRDs, metrics, rituals | [4-Execution/](4-Execution/README.md) |
| Stakeholder comms & docs | [5-Communication/](5-Communication/README.md) |
| Repo / initiative templates | [0-Template-Structure/](0-Template-Structure/README.md) |
| Writing a new PM Brain skill | [0-writing-a-skill.md](0-writing-a-skill.md) |

**Also reference-only (no separate skill workflow):** [Strategy Blocks full guide](2-Strategy/1-Strategic-Foundations/1-Strategy-Blocks/1-full-guide.md), [Crisis Management](5-Communication/4-Crisis-Management/), [Stakeholder Management](5-Communication/7-Stakeholder-Management/), [10 Things workshop](4-Execution/8-10-Things-Workshop/).

---

## Topics → skill or reference

| Topic | Use |
|--------|-----|
| Bias | [1-Foundations/2-Bias/](1-Foundations/2-Bias/) |
| Decision-making, pre-mortems, assumptions | [1-Foundations/1-Mental-Models/1-Decision-Making/](1-Foundations/1-Mental-Models/1-Decision-Making/) |
| Discovery / research | `discovery-synthesis` skill → [3-Discovery/](3-Discovery/README.md) |
| Opportunity assessment | `opportunity-assessment` skill → [4-Opportunity-Assessment/](3-Discovery/4-Opportunity-Assessment/) |
| PRD / user stories | `write-prd` skill → [4-PRD/](4-Execution/4-PRD/), [User Stories](4-Execution/2-User-Stories/) |
| Prioritization / backlog | `prioritize` skill → [4-Prioritization/](2-Strategy/2-Strategic-Execution/4-Prioritization/), [Backlog](4-Execution/3-Backlog-Prioritization/) |
| OKRs / roadmap / North Star | `okr`, `roadmap`, `north-star` skills → [2-Strategic-Execution/](2-Strategy/2-Strategic-Execution/README.md) |
| Metrics / AARRR | `north-star` skill → [6-Metrics/](4-Execution/6-Metrics/), [AARRR](4-Execution/7-AARRR-Pirate-Metrics/) |
| Strategy doc | `strategy` skill → [GSBS](2-Strategy/1-Strategic-Foundations/2-Good-Strategy-Bad-Strategy/), [Playing to Win](2-Strategy/1-Strategic-Foundations/3-Playing-To-Win/); org process → Strategy Blocks guide |
| Stakeholder comms | `stakeholder-comms` skill → [One-pagers](5-Communication/3-One-Pagers/), [Agendas](5-Communication/2-Meeting-Agendas/), [Newsletter](5-Communication/1-Newsletter/) |
| Escalation / saying no | `stakeholder-comms` skill → [5-Escalation/](5-Communication/5-Escalation/), [6-Saying-No/](5-Communication/6-Saying-No/) |
| Product sense coaching | [system/coaching/](../system/coaching/README.md) |

---

**Agent note:** On doc requests, load the matching skill’s `SKILL.md` first. Preflight: 2–3 questions from [system/coaching/prompts.md](../system/coaching/prompts.md) unless the user already braindumped. Criteria for scoring live in each skill’s `references/criteria.md` (or `criteria-one-pager.md` for one-pagers).
