# Skills and the methods library

How PM Brain splits **agent workflows** (`.claude/skills/`) from the **framework library** (`2-Methods/`). Read this before changing skills or deleting framework folders.

## Three layers

| Layer | Role | Typical load |
|--------|------|----------------|
| **Skill `SKILL.md`** | When to run, preflight, routing, org reality, where to save work | On “help me write X” / matching user phrase |
| **`2-Methods/`** | Canonical `1-*-framework.md`, `2-*-template.md`, `3-*-evaluation.md` | When drafting sections, filling templates, or running **full** artifact eval |
| **`system/EVALUATION.md`** | Shared eval math and output format | Full scored review (with `3-*-evaluation.md`) |

**Rule:** Skills coach and route; they do not replace the methods library in this repo.

## Load order (agents)

1. Matching `SKILL.md` (preflight, braindump floor).
2. Canonical **template** from `2-Methods/.../2-*-template.md` (not an alternate shape in the skill unless explicitly marked portable-only).
3. **Quick check** while drafting: skill `references/criteria.md` red/green flags.
4. **Full evaluation** on request: `2-Methods/.../3-*-evaluation.md` + `system/EVALUATION.md`.

## Artifact map

| Skill | Framework | Template | Full evaluation | Quick check |
|--------|-----------|----------|-----------------|-------------|
| `opportunity-assessment` | `3-Discovery/4-Opportunity-Assessment/1-opportunity-assessment-framework.md` | `.../2-opportunity-assessment-template.md` | `.../3-opportunity-assessment-evaluation.md` | `opportunity-assessment/references/criteria.md` |
| `write-prd` | `4-Execution/4-PRD/1-prd-framework.md` | `.../2-prd-template.md` | `.../3-prd-evaluation.md` | `write-prd/references/criteria.md` |
| `okr` | `2-Strategy/.../1-OKR/1-okr-framework.md` | `.../2-okr-template.md` | `.../3-okr-evaluation.md` | `okr/references/criteria.md` |
| `roadmap` | `2-Strategy/.../2-Roadmap/1-roadmap-framework.md` | `.../2-roadmap-template.md` | `.../3-roadmap-evaluation.md` | `roadmap/references/criteria.md` |
| `north-star` | `2-Strategy/.../3-North-Star/1-north-star-framework.md` | `.../2-north-star-template.md` | `.../3-north-star-evaluation.md` | `north-star/references/criteria.md` |
| `stakeholder-comms` (one-pager) | `5-Communication/3-One-Pagers/1-one-pager-framework.md` | `.../2-one-pager-templates.md` | `.../3-one-pager-evaluation.md` | `stakeholder-comms/references/criteria-one-pager.md` |
| `discovery-synthesis` | `3-Discovery/*` (per topic) | per framework folder | (varies) | skill `references/` = summary only |
| `prioritize` | `2-Strategy/.../4-Prioritization/` + `4-Execution/3-Backlog-Prioritization/` | per method | — | `prioritize/references/criteria.md` |
| `strategy` | GSBS, Playing to Win under `2-Strategy/1-Strategic-Foundations/` | per framework | — | `strategy/references/criteria.md` |

L1 rubric regressions (`system/evals/scenarios/rubric/`) use **`3-*-evaluation.md`** as `rubric_path`.

## Alignment status (private repo)

| Area | Status |
|------|--------|
| Opportunity assessment skill | **Aligned** — template/sections match `2-Methods`; removed alternate “four risks only” doc shape |
| Eval wiring (`EVALUATION.md`, `evaluate-artifact`, rubric regressions) | **Aligned** — full rubrics in `2-Methods/` |
| PRD skill template | **Synced** — `references/template.md` copied from `2-Methods` |
| Discovery synthesis | **Routed** — SKILL points at `2-Methods`; thin `references/` kept for portable installs |
| OKR / roadmap / north-star skill templates | **Synced** — `references/template.md` copied from `2-Methods`; SKILL points at canonical paths |
| `0-writing-a-skill.md` | **Rewritten** — see that file |

## Portable upstream vs this fork

Public skill packs may ship slim `references/` for offline use. **This repo** treats `2-Methods/` as source of truth; skills link to it explicitly.

## Maintainer checklist (new or changed skill)

- [ ] `SKILL.md` names canonical `2-Methods/` paths for framework, template, and `3-*-evaluation` if applicable
- [ ] Skill template matches `2-*-template.md` OR skill says “load canonical only” with no competing shape
- [ ] `references/criteria.md` = quick check only; full eval unchanged in `2-Methods/`
- [ ] `system/EVALUATION.md` table updated
- [ ] Rubric regression `rubric_path` → `3-*-evaluation.md` when scored eval exists
- [ ] `2-Methods/0-index.md` skill ↔ folder map updated
