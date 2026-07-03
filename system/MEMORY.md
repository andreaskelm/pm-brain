# Sleeping Memory — What to Wake When

**What this file is:** On-demand context manifest. Bootstrap: [AGENTS.md](../AGENTS.md) + [`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc) + this file + [USER.md](../USER.md). Routing detail: [ORCHESTRATION.md](ORCHESTRATION.md).

Do not load everything at once. Wake only what the conversation needs.

---

## Bootstrap vs Sleeping Memory

**Bootstrap (not sleeping):**
- [AGENTS.md](../AGENTS.md) — persona, principles, lenses, routing intent
- [`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc) — enforcement (voice, lenses, braindump floor)
- [MEMORY.md](MEMORY.md) — this file
- [USER.md](../USER.md) — personal context (optional if unfilled)

**Sleeping memory:**
- [ORCHESTRATION.md](ORCHESTRATION.md) — full routing, states, context loading table
- [coaching/README.md](coaching/README.md) — product sense coaching entry + braindump process
- [EVALUATION.md](EVALUATION.md) — artifact QQC rules
- [skills/](skills/) — topic-dispatch skills
- [evals/](evals/) — behavior eval infrastructure
- `1-Context/` — company, stakeholders, org survival
- `2-Methods/` — frameworks and templates
- `3-Work/` — initiatives
- `4-Research/` — research artifacts
- `5-Growth/` — learning log, PJT, portfolio

---

## When to Wake What

| Trigger | Wake |
|---------|------|
| Company, strategy, vision, roadmap, stakeholders | [1-Context/](../1-Context/README.md) |
| Initiative, "my bet", current project | `3-Work/[name]/` |
| Research, interviews, evidence | [4-Research/](../4-Research/README.md) or `3-Work/[name]/research/` |
| Product thinking / braindump / coaching session | [coaching/README.md](coaching/README.md) |
| Deep product sense / thinking quality stall | [2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/](../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/README.md) |
| Doc request / template / framework | [2-Methods/0-template-finder.md](../2-Methods/0-template-finder.md) + ORCHESTRATION.md |
| Roadmap, OKRs, strategy skill | [skills/strategy-planning/SKILL.md](skills/strategy-planning/SKILL.md) |
| Discovery, JTBD, OA, research skill | [skills/discovery-research/SKILL.md](skills/discovery-research/SKILL.md) |
| Stakeholder comms skill | [skills/stakeholder-management/SKILL.md](skills/stakeholder-management/SKILL.md) |
| Politics skill | [skills/politics-coach/SKILL.md](skills/politics-coach/SKILL.md) |
| PM workflow navigation | [skills/pm-brain-workflow/SKILL.md](skills/pm-brain-workflow/SKILL.md) |
| Artifact QQC / eval during creation | [EVALUATION.md](EVALUATION.md) |
| Agent behavior eval | [evals/behavior-assertions.md](evals/behavior-assertions.md), [evals/1-agent-behavior-guide.md](evals/1-agent-behavior-guide.md) |
| Learning log, daily log, week wrap | [5-Growth/](../5-Growth/README.md) |
| meta_reflection, substantial decision pause | [5-Growth/README.md](../5-Growth/README.md) |
| End-of-week wrap, Friday close | [5-Growth/1-Learning-Log/](../5-Growth/1-Learning-Log/) |
| Decision + confidence level (PJT trigger) | [5-Growth/3-Product-Judgment-Test/forecast-log.md](../5-Growth/3-Product-Judgment-Test/forecast-log.md) |
| PJT, forecast, calibration | [5-Growth/3-Product-Judgment-Test/](../5-Growth/3-Product-Judgment-Test/) |
| Repo philosophy / golden record | [docs/principles.md](../docs/principles.md) |
| Repo structure / architecture | [docs/architecture.md](../docs/architecture.md) |
| Context freshness | [1-Context/CONTEXT-HEALTH.md](../1-Context/CONTEXT-HEALTH.md) |
| Bias deep-dive | [2-Methods/1-Foundations/2-Bias/](../2-Methods/1-Foundations/2-Bias/1-bias-framework.md) |
| Evidence strength / know vs. guess | [2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/7-evidence-strength.md](../2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/7-evidence-strength.md) |
| Contradiction vs logged decision | forecast-log, prioritization-decision-log, ORCHESTRATION.md cross-cutting |
| Friday drift sweep | `/week` Friday, [2-weekly-cadence.md](../2-Methods/4-Execution/1-Daily-Execution-And-Rituals/2-weekly-cadence.md) |
| Four risks | [2-Methods/1-Foundations/1-Mental-Models/2-Product-Thinking/4-four-risks.md](../2-Methods/1-Foundations/1-Mental-Models/2-Product-Thinking/4-four-risks.md) |
| Team alignment | [2-Methods/1-Foundations/1-Mental-Models/5-Team-Dynamics/1-alignment-check.md](../2-Methods/1-Foundations/1-Mental-Models/5-Team-Dynamics/1-alignment-check.md) |

Check filesystem before asking user whether context exists.

---

## Company Context (1-Context/)

| Purpose | Path |
|---------|------|
| Personalization | [USER.md](../USER.md) |
| Vision / strategy / roadmap | `1-Context/1-company-vision.md` etc. |
| Stakeholder avatars | [1-Context/1.1-Stakeholder-Avatars/](../1-Context/1.1-Stakeholder-Avatars/README.md) |
| Org survival | [1-Context/1.2-Organization-Survival/](../1-Context/1.2-Organization-Survival/README.md) |
| Context health | [1-Context/CONTEXT-HEALTH.md](../1-Context/CONTEXT-HEALTH.md) |

Before updating numbered company docs, check `Maintained?` in CONTEXT-HEALTH.md. Reference/External → route to `3-Work/` or avatar.

---

## Initiatives (3-Work/)

One folder per initiative. Typical files: README.md, opportunity-assessment.md, prd.md, decisions.md, roadmap.md, research/ — see [3-Work/README.md](../3-Work/README.md) for the full exemplar layout.

---

## Evals (system/evals/)

| File | Purpose |
|------|---------|
| [eval-functions.md](evals/eval-functions.md) | Pointer to harness checks (`structural.py`, hooks) |
| [harness/](evals/harness/) | `run_scenario.py`, `run_rubric_regression.py`, `run_all.py` |
| [behavior-assertions.md](evals/behavior-assertions.md) | Principle → scenario → pass/fail |
| [1-agent-behavior-guide.md](evals/1-agent-behavior-guide.md) | Level 2 review |
| [agent-behavior-scenarios.json](evals/agent-behavior-scenarios.json) | Behavior scenario index (harness_path) |
| [evals/eval-results/](evals/eval-results/) | Eval run history |

---

## Skills (system/skills/)

Load on topic signal — see ORCHESTRATION.md skills dispatch table.
