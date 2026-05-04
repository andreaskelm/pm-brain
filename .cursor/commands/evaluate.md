---
description: Run quality checks on the artifact or conversation we just created.
---

Let’s evaluate the quality of what we just worked on.

1. **Identify what to evaluate**
   - Ask whether we’re evaluating:
     - A specific artifact (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap, etc.),
     - The agent's behavior in this conversation, or
     - The conversation itself as a source of personal capture (decisions, thinking, growth).
   - In practice, run all three dimensions at the end of any substantive session — they take different amounts of time and serve different purposes.

2. **If artifact quality (Level 1)**
   - Find the relevant evaluation file in `02-Methods-and-Tools/` (`3-*-evaluation.md`) and its Quick Quality Checks in `1-*-framework.md`.
   - Walk me through the Quick Quality Checks first, then any deeper questions from `3-*-evaluation.md` if needed.
3. **If agent behavior (Level 2)**
   - Use `.cursor/evals/1-agent-behavior-guide.md` and `.cursor/evals/2-checklist.md` to review this conversation.
   - Match it to a scenario from `.cursor/evals/agent-behavior-scenarios.json` and use the success_indicators / failure_modes to reflect.
   - Flag any repo adjustments needed: rules to update, scenarios to add, ORCHESTRATION gaps, or framework issues.

4. **Personal capture scan (always run at end of any substantive session)**
   - Scan the conversation for content worth routing. Explicitly check:
     - Any decisions made with explicit reasoning → [2-decision-showcase.md](../../00-Meta/0.2-Growth-Portfolio/2-decision-showcase.md)?
     - Any decisions with a stated confidence level → [forecast-log.md](../../00-Meta/0.3-Product-Judgment-Test/forecast-log.md) (PJT)?
     - Any insight about how you think, a bias noticed, an assumption you updated → [1-product-sense-journey.md](../../00-Meta/0.2-Growth-Portfolio/1-product-sense-journey.md)?
     - Any PM Brain friction or agent behavior pattern worth logging → your system learnings folder (e.g. `04-Initiatives/[initiative-name]/`)?
   - Most sessions produce nothing for most targets. The point is asking, not forcing entries.

5. **Log key findings**
   - Suggest a short summary I could add to `.cursor/evals/eval-results/` (using the format from `eval-results/README.md`), focusing on:
     - What worked well,
     - What needs improvement,
     - Which files we should update (AGENTS, ORCHESTRATION, rules, or framework docs),
     - Repo adjustments to make immediately vs. log for later.

