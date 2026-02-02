## Agent Manifest

This file summarizes the AGENT assistant’s main capabilities, entrypoints, and canonical specs for the PM Brain repository.

### Entrypoints

- **Product thinking entrypoint**: `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md`
- **Template finder** (when you already know which doc you need): `02-Methods-and-Tools/0-template-finder.md`
- **Workflow / framework map skill**: `.cursor/skills/pm-brain-workflow/SKILL.md`

### Canonical specs

- **Golden rule & braindump workflow**: `PRODUCT-SENSE-RULES.md`
- **Braindump sufficient checklist** (when to leave product_sense_mode): `PRODUCT-SENSE-RULES.md` → \"Is the braindump \"sufficient\"?\"
- **Persona & background for product thinking**: `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md` → \"Persona & background (for agent)\"

### Modes

- **product_sense_mode**: Thinking/braindumping about product, stakeholders, org, strategy, roadmap, prioritization, discovery, execution, or \"help me think through something\". Use 0-start-here + PRODUCT-SENSE-RULES + 2-product-sense-prompts; no frameworks/templates until braindump is sufficient.
- **execution_mode**: After braindump is sufficient (or when using the template-finder path for a specific doc). Use pm-brain-workflow skill + Methods-and-Tools frameworks and templates.
- **meta_mode**: After substantial product decision conversations. Suggest logging in `00-Meta/` and, when appropriate, evolving rules (see `.cursor/rules/thinking.mdc`).

### Content clusters

- **Methods & frameworks**: `02-Methods-and-Tools/` (2.0 Foundations → 2.4 Communication)
- **Personal practice & evidence**: `00-Meta/` (daily log, learning log, growth portfolio, Product Judgment Test)
- **Company context**: `01-Company-Context/`
- **Research artifacts**: `03-Research-Artifacts/`
- **Active initiatives**: `04-Initiatives/`

