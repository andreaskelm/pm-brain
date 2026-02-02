# Evals Checklist

Use this checklist to run Level 1 (methods/frameworks) and Level 2 (agent behavior) and to know when to update criteria or rules when you learn something new. No scripts—guidance only.

**See also:** [README.md](README.md) for Level 1/2 index and pasteable prompts; [1-agent-behavior-guide.md](1-agent-behavior-guide.md) for the full Level 2 guide.

---

## Getting started

### Week 1: Level 1 (methods/frameworks)

- [ ] Read the **Level 1** section in [README.md](README.md) (where Quick Quality Checks and `3-*-evaluation.md` live).
- [ ] Pick one artifact you care about (e.g. a PRD, opportunity assessment, North Star, one-pager).
- [ ] Run one full **3-*-evaluation** on that artifact (use the `3-*-evaluation.md` in the relevant framework folder). Work through the steps: product sense gut check, quality check, antipattern detector, improvement generator.
- [ ] Note any criteria that feel wrong or missing—those are candidates to update in `1-*-framework.md` (Quick Quality Checks) or `3-*-evaluation.md`.

### Week 2: Level 2 (agent behavior)

- [ ] Read [1-agent-behavior-guide.md](1-agent-behavior-guide.md) (dimensions, reflection checklist, "where to update" map).
- [ ] Pick 2–3 recent product-related conversations (or transcripts).
- [ ] Run the **reflection checklist** in the guide on each. For each failure, use the **"Where to update"** map to note which file/section to edit.
- [ ] Optionally: use the **pasteable prompt (transcript review)** from [README.md](README.md) with an AI; paste your transcript and AGENTS.md, then apply the guide's dimensions and checklist.

### When you learn something new

- [ ] If a **method or framework** check is wrong or the method has evolved → edit the relevant `1-*-framework.md` (Quick Quality Checks) and/or `3-*-evaluation.md`. If the list of frameworks with evaluation support changes, update `.cursor/rules/evaluation-orchestration.mdc`.
- [ ] If **agent behavior** should change (e.g. more questioning, better framework fit, more meta suggestions) → use the **"Where to update"** map in [1-agent-behavior-guide.md](1-agent-behavior-guide.md) and edit [AGENTS.md](../AGENTS.md) or the relevant `.cursor/rules` file (e.g. template-finder.mdc, evaluation-orchestration.mdc, thinking.mdc).

---

## Ongoing rhythm (guidance-only)

### Weekly (optional)

- [ ] Run the **reflection checklist** (in the Level 2 guide) on 1–2 conversations that mattered.
- [ ] If you spot a pattern (e.g. "agent keeps jumping to template"), use "Where to update" and make one concrete edit.

### Monthly (optional)

- [ ] Run one **3-*-evaluation** on an artifact you care about; adjust Quick Quality Checks or evaluation criteria if your bar has changed.
- [ ] Re-read the Level 2 guide; add a scenario or prompt to [agent-behavior-scenarios.json](agent-behavior-scenarios.json) or the guide if you discovered a new failure mode.

### When adding new frameworks

- [ ] If a new framework gets a `3-*-evaluation.md`, add it to the Level 1 list in [README.md](README.md) and to `.cursor/rules/evaluation-orchestration.mdc` so the agent offers it.

---

## Success looks like

- You know **where** Level 1 and Level 2 live (README + 1-agent-behavior-guide).
- You run the **reflection checklist** or a **3-*-evaluation** when it matters.
- When you learn something new, you **edit the right file** using the "Where to update" map.
- Evals lead to **concrete edits** to AGENTS.md, rules, or framework files—not just scores.

**Evals are a means, not an end.** The goal is a PM Brain that helps people think better. Use this checklist to keep guidance and criteria aligned with what you learn.
