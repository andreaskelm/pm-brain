## Agent Manifest

**What this file is:** A **reference summary** for humans and maintainers. The agent does **not** load this file. Bootstrap (read every conversation): [AGENTS.md](../AGENTS.md) → [`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc) → [system/MEMORY.md](../system/MEMORY.md) → [USER.md](../USER.md). [system/ORCHESTRATION.md](../system/ORCHESTRATION.md) loads at **state entry**, not bootstrap. Use this doc to quickly see entrypoints, states, and content clusters; for executed behavior, see ORCHESTRATION and AGENTS.

This file summarizes the AGENT assistant's main capabilities, entrypoints, and canonical specs for the PM Brain repository.

### Platform entry points

| Platform | Entry point | Bootstrap wiring |
|----------|-------------|------------------|
| Cursor | `.cursor/rules/pm-brain.mdc` (auto-injected) | Four-file bootstrap; mdc enforced via `alwaysApply` |
| Claude Code | [CLAUDE.md](../CLAUDE.md) | Compliance checklist → read full bootstrap including mdc |
| GitHub Copilot | [.github/copilot-instructions.md](../.github/copilot-instructions.md) | Same |
| ChatGPT / Claude.ai | Manual paste | Bootstrap block from [platform-setup.md](platform-setup.md) |

Full per-platform setup: [platform-setup.md](platform-setup.md).

### Orchestration and memory

- **Routing, states, context loading:** [system/ORCHESTRATION.md](../system/ORCHESTRATION.md) — single source of truth for agent behavior (product_sense, execution_mode, meta_reflection, conversation). Loads at state entry, not bootstrap. [AGENTS.md](../AGENTS.md) holds persona and points there.
- **Sleeping memory (what to wake when):** [system/MEMORY.md](../system/MEMORY.md) — manifest for company context, initiatives, research, rules, skills; use when the conversation touches those areas.

### Entrypoints

- **Product thinking entrypoint**: `system/coaching/README.md`
- **Template finder** (when you already know which doc you need): `2-Methods/0-template-finder.md`
- **Workflow / framework map skill**: `system/skills/pm-brain-workflow/SKILL.md`

### Canonical specs

- **Golden rule & braindump workflow**: `system/coaching/braindump.md`
- **Braindump sufficient checklist** (when to leave product_sense): `system/coaching/braindump.md` → "Is the braindump sufficient?"; enforcement and context-health rules in `system/ORCHESTRATION.md`.
- **Persona for product thinking**: [AGENTS.md](../AGENTS.md)
- **Coaching workflow entry**: [system/coaching/README.md](../system/coaching/README.md)

### States (see system/ORCHESTRATION.md for full logic)

**Default posture:** **product_sense** — develop product sense through braindump unless there's an explicit doc request or non-product navigation.

- **product_sense:** Default; thinking/braindumping; use system/coaching/README.md + braindump.md + prompts.md; no frameworks/templates until braindump sufficient.
- **execution_mode:** After braindump sufficient or template-finder path. Use pm-brain-workflow skill + `2-Methods/` frameworks and templates.
- **meta_reflection:** After substantial product decisions; suggest logging in `5-Growth/`, optionally Level 2 checklist (`system/evals/`), rule updates.
- **conversation:** Navigation, non-product topics. Re-route when product or doc-request triggers appear.

**Mode signaling:** One short natural sentence when switching (e.g. "We've got enough to structure this—here's the framework—"). No internal labels.

**Evals:** Separate workflow. Artifact QQC in `2-Methods/` + [system/EVALUATION.md](../system/EVALUATION.md); coaching enforcement via `pm-brain.mdc` on all platforms (Cursor auto-injects, others read explicitly). Agent behavior evals in `system/evals/` ([README](../system/evals/README.md)). Fork maintainers: [evals-fork.md](evals-fork.md). See system/ORCHESTRATION.md → Eval Checkpoints.

### Content clusters

- **Methods & frameworks**: `2-Methods/` (1-Foundations through 5-Communication)
- **Personal practice & evidence**: `5-Growth/` (daily log, learning log, growth portfolio, Product Judgment Test)
- **Company context**: `1-Context/` (wake via MEMORY.md when relevant)
- **Research artifacts**: `4-Research/`
- **Active initiatives**: `3-Work/`
