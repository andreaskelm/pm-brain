# Evals Checklist

Use this checklist to run Level 1 (methods/frameworks) and Level 2 (agent behavior) and to know when to update criteria or rules when you learn something new.

**See also:** [README.md](README.md) for commands and architecture; [1-agent-behavior-guide.md](1-agent-behavior-guide.md) for human transcript review.

---

## Getting started

### Week 1: Level 1 (methods/frameworks)

- [ ] Read the **Level 1** section in [README.md](README.md) (where Quick Quality Checks and `3-*-evaluation.md` live).
- [ ] Pick one artifact you care about (e.g. a PRD, opportunity assessment, North Star, one-pager).
- [ ] Run one full **3-*-evaluation** on that artifact, or run rubric regression: `python system/evals/harness/run_rubric_regression.py --all --dry-run` (then live when [Cursor CLI](../../docs/platform-setup.md#cursor-cli-optional--live-evals) is installed).
- [ ] Note any criteria that feel wrong or missing—those are candidates to update in `1-*-framework.md` (Quick Quality Checks) or `3-*-evaluation.md`.

### Week 2: Level 2 (agent behavior)

- [ ] Read [1-agent-behavior-guide.md](1-agent-behavior-guide.md) (dimensions, reflection checklist, "where to update" map).
- [ ] Pick 2–3 recent product-related conversations (or transcripts).
- [ ] Run the **reflection checklist** in the guide on each, or run harness scenarios: `python system/evals/harness/run_all.py --dry-run --skip-content --plumbing`.
- [ ] Optionally: use the **pasteable prompt (transcript review)** from [README.md](README.md) with an AI; paste your transcript and AGENTS.md, then apply the guide's dimensions and checklist.

### When you learn something new

- [ ] If a **method or framework** check is wrong or the method has evolved → edit the relevant `1-*-framework.md` (Quick Quality Checks) and/or `3-*-evaluation.md`. If the list of frameworks with evaluation support changes, update `../EVALUATION.md`.
- [ ] If **agent behavior** should change (e.g. more questioning, better framework fit, more meta suggestions) → use the **"Where to update"** map in [1-agent-behavior-guide.md](1-agent-behavior-guide.md) and edit [../../AGENTS.md](../../AGENTS.md) or the relevant file (e.g. [../ORCHESTRATION.md](../ORCHESTRATION.md), `../EVALUATION.md`).

---

## Ongoing rhythm

### Weekly (optional)

- [ ] Run the **reflection checklist** (in the Level 2 guide) on 1–2 conversations that mattered.
- [ ] If you spot a pattern (e.g. "agent keeps jumping to template"), use "Where to update" and make one concrete edit.

### Monthly (optional)

- [ ] Run one **3-*-evaluation** on an artifact you care about; adjust Quick Quality Checks or evaluation criteria if your bar has changed.
- [ ] Re-read the Level 2 guide; add a scenario or prompt to [agent-behavior-scenarios.json](agent-behavior-scenarios.json) or the guide if you discovered a new failure mode.

### When adding new frameworks

- [ ] If a new framework gets a `3-*-evaluation.md`, add it to the Level 1 list in [README.md](README.md) and to `../EVALUATION.md` so the agent offers it.

---

## Success looks like

- You know **where** Level 1 and Level 2 live (README + 1-agent-behavior-guide).
- You run the **reflection checklist** or a **3-*-evaluation** when it matters.
- When you learn something new, you **edit the right file** using the "Where to update" map.
- Evals lead to **concrete edits** to AGENTS.md, rules, or framework files—not just scores.

**Evals are a means, not an end.** The goal is a PM Brain that helps people think better. Use this checklist to keep guidance and criteria aligned with what you learn.
