## Agent Manifest

**What this file is:** A **reference summary** for humans and maintainers. The agent does **not** load this file—it loads [AGENTS.md](AGENTS.md), [ORCHESTRATION.md](ORCHESTRATION.md), and [MEMORY.md](MEMORY.md) as defined in ORCHESTRATION. Use this doc to quickly see entrypoints, states, and content clusters; for executed behavior, see ORCHESTRATION and AGENTS.

This file summarizes the AGENT assistant’s main capabilities, entrypoints, and canonical specs for the PM Brain repository.

### Orchestration and memory

- **Routing, states, context loading:** [ORCHESTRATION.md](ORCHESTRATION.md) — single source of truth for agent behavior (product_sense, execution_mode, meta_reflection, conversation). [AGENTS.md](AGENTS.md) holds persona and points there.
- **Sleeping memory (what to wake when):** [MEMORY.md](MEMORY.md) — manifest for company context, initiatives, research, rules, skills; use when the conversation touches those areas.

### Entrypoints

- **Product thinking entrypoint**: `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md`
- **Template finder** (when you already know which doc you need): `02-Methods-and-Tools/0-template-finder.md`
- **Workflow / framework map skill**: `.cursor/skills/pm-brain-workflow/SKILL.md`

### Canonical specs

- **Golden rule & braindump workflow**: `PRODUCT-SENSE-RULES.md`
- **Braindump sufficient checklist** (when to leave product_sense): `PRODUCT-SENSE-RULES.md` → "Is the braindump sufficient?"; enforcement and checkpoints in `ORCHESTRATION.md`.
- **Persona & background for product thinking**: `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md` → "Persona & background (for agent)"

### States (see ORCHESTRATION.md for full logic)

- **conversation** (default): General questions, navigation, non-product topics. Re-route when the user message matches product or doc-request triggers.
- **product_sense:** Thinking/braindumping; use 0-start-here + PRODUCT-SENSE-RULES + 2-product-sense-prompts; no frameworks/templates until braindump sufficient.
- **execution_mode:** After braindump sufficient or template-finder path. Use pm-brain-workflow skill + Methods-and-Tools frameworks and templates.
- **meta_reflection:** After substantial product decisions; suggest logging in `00-Meta/`, optionally Level 2 checklist (`.cursor/evals/`), rule updates (`.cursor/rules/thinking.mdc`). Exit → conversation.

**Mode signaling:** One short natural sentence when switching (e.g. "We've got enough to structure this—here's the framework…"). No internal labels.

**Evals:** Separate workflow. Level 1 in `02-Methods-and-Tools/` + Quick Quality Checks per `.cursor/rules/evaluation-orchestration.mdc`; Level 2 in `.cursor/evals/` ([README](.cursor/evals/README.md)). See ORCHESTRATION.md → Eval Checkpoints.

### Content clusters

- **Methods & frameworks**: `02-Methods-and-Tools/` (2.0 Foundations → 2.4 Communication)
- **Personal practice & evidence**: `00-Meta/` (daily log, learning log, growth portfolio, Product Judgment Test)
- **Company context**: `01-Company-Context/` (wake via MEMORY.md when relevant)
- **Research artifacts**: `03-Research-Artifacts/`
- **Active initiatives**: `04-Initiatives/`

