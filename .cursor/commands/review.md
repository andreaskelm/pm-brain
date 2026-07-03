---
description: Review a file, folder, or set of artifacts in the PM Brain repository for quality, freshness, consistency, and alignment.
---

Let's do a review. Before starting, ask or clarify:

1. **What are we reviewing?**
   - A specific file or artifact (e.g. stakeholder avatar, opportunity assessment, roadmap, initiative folder)
   - A folder or cluster (e.g. all of 1-Context, the full 3-Work/[initiative-folder])
   - Company context freshness and accuracy
   - PM Brain system health (rules, frameworks, ORCHESTRATION, MEMORY alignment)

2. **What kind of review?**

   **Quality review** — Is this artifact good?
   - Load the relevant `3-*-evaluation.md` and `1-*-framework.md` Quick Quality Checks from `2-Methods/`
   - Work through: gut check, quality flags (red/green), scored rubric if applicable
   - Flag what's missing, stale, inconsistent, or at odds with decisions captured elsewhere

   **Freshness review** — Is this still current?
   - Check `lastUpdated` metadata against recent weekly logs and daily log entries
   - Flag anything that contradicts newer decisions, observations, or context captured since the file was written
   - Cross-check reopen triggers in `5-Growth/3-Product-Judgment-Test/forecast-log.md` and `5-Growth/2-prioritization-decision-log.md` — flag if current content would fire a stored trigger
   - Reference `1-Context/CONTEXT-HEALTH.md` for company context freshness signals

   **Consistency review** — Does this align with the rest of the repo?
   - Cross-check with related initiative files, stakeholder avatars, strategy docs, and OKRs
   - Flag contradictions between files (e.g. avatar says one thing, initiative notes say another)
   - Check for link rot or orphaned references

   **System health review** — Is PM Brain working well?
   - Review your system learnings folder (e.g. `3-Work/[initiative-name]/`) for open gaps and pending fixes
   - Check `system/ORCHESTRATION.md` and `.cursor/rules/pm-brain.mdc` for any known inconsistencies or TODOs
   - Review `system/evals/eval-results/` for patterns not yet addressed in rules or scenarios
   - Check `system/evals/agent-behavior-scenarios.json` for missing scenario types identified in eval logs

3. **Output**
   - Summarise findings: what's solid, what needs updating, what's stale or broken
   - Give specific, actionable recommendations — name the file and the change, don't be vague
   - If fixes are small and clear, offer to implement them in-session
   - If fixes are large or require decisions, log as an open item in your system learnings folder or the relevant initiative file

4. **Capture routing (always run before closing a review session)**
   - Before finishing, ask: did the review surface anything worth routing to the growth portfolio?
     - A decision that shows good judgment → [2-decision-showcase.md](../../5-Growth/2-Growth-Portfolio/2-decision-showcase.md)?
     - A pattern in how you think or what you missed → [1-product-sense-journey.md](../../5-Growth/2-Growth-Portfolio/1-product-sense-journey.md)?
     - A system gap or agent behavior miss → your system learnings folder?
   - Keep it brief — one question, one pass. Most reviews produce nothing for the portfolio; the point is not skipping the check.

**Related:** Use `/evaluate` for quality checks on a specific freshly-created artifact or this conversation's agent behavior. Use `/meta` for PM Brain system improvement conversations. Use `/navigate` to find what's in the repo.
