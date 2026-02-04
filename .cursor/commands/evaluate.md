---
description: Run quality checks on the artifact or conversation we just created.
---

Let’s evaluate the quality of what we just worked on.

1. **Identify what to evaluate**
   - Ask whether we’re evaluating:
     - A specific artifact (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap, etc.), or
     - The agent’s behavior in this conversation.
2. **If artifact quality (Level 1)**
   - Find the relevant evaluation file in `02-Methods-and-Tools/` (`3-*-evaluation.md`) and its Quick Quality Checks in `1-*-framework.md`.
   - Walk me through the Quick Quality Checks first, then any deeper questions from `3-*-evaluation.md` if needed.
3. **If agent behavior (Level 2)**
   - Use `.cursor/evals/1-agent-behavior-guide.md` and `.cursor/evals/2-checklist.md` to review this conversation.
   - Match it to a scenario from `.cursor/evals/agent-behavior-scenarios.json` and use the success_indicators / failure_modes to reflect.
4. **Log key findings**
   - Suggest a short summary I could add to `.cursor/evals/eval-results/` (using the format from `eval-results/README.md`), focusing on:
     - What worked well,
     - What needs improvement,
     - Which files we should update (AGENTS, ORCHESTRATION, rules, or framework docs).

