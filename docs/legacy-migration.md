# Legacy Folder Migration

PM Brain uses a **canonical 1–5 top-level model** plus root bootstrap files and a `system/` agent layer. Older repo versions used **`00–04` decimal-prefixed folders** and scattered meta/agent/thinking files.

**Rule going forward:** Put content in `1-Context/` through `5-Growth/`, agent infrastructure in `system/`, human docs in `docs/`, bootstrap files at repo root. Do not add files to legacy folders.

If your fork still has **both** legacy and canonical trees (common during transition), treat the canonical paths as source of truth and delete legacy folders only after the safe-delete checklist below.

**Already migrated?** If top-level `00–04` folders are gone, skip to [Internal renumbering](#internal-renumbering) and [Safe delete checklist](#safe-delete-checklist) for any remaining decimal subfolders (`0.1-Learning-Log`, eval scenario duplicates, stale markdown links).

---

## Top-level folder mapping

| Legacy folder | Canonical folder | Notes |
|---------------|------------------|-------|
| `00-Meta/` | **`5-Growth/`** (primary) + **`system/`** + **`docs/`** | See [00-Meta split](#00-meta-split) — Meta was mostly personal practice, not agent infra |
| `01-Company-Context/` | `1-Context/` | Company vision, strategy, stakeholders, org survival |
| `02-Methods-and-Tools/` | `2-Methods/` | Frameworks and templates (renumbered — see below) |
| `03-Research-Artifacts/` | `4-Research/` | Research storage |
| `04-Initiatives/` | `3-Work/` | Active initiatives |

**`5-Growth/` is not new** — it is largely the successor to **`00-Meta/`** practice content (logs, PJT, growth portfolio, coaching templates you actually fill in).

---

## 00-Meta split

`00-Meta/` mixed personal practice with agent configuration. The refactor **split it by concern**:

### → `5-Growth/` (personal practice & evidence)

| Legacy (`00-Meta/`) | Canonical (`5-Growth/`) |
|---------------------|-------------------------|
| `0.1-Learning-Log/` | `1-Learning-Log/` |
| `0.2-Growth-Portfolio/` | `2-Growth-Portfolio/` |
| `0.3-Product-Judgment-Test/` | `3-Product-Judgment-Test/` |
| `1-daily-log-YYYY-QX.md` | `1-daily-log-YYYY-QX.md` (root of `5-Growth/`) |
| `2-prioritization-decision-log.md` | `2-prioritization-decision-log.md` |
| `3-research-insight-log.md` | `3-research-insight-log.md` |
| Coaching templates you use | `4-Coaching-Templates/` |

Framework reference for product sense stays in `2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/` — `5-Growth/` holds **your** logs and evidence, not the library.

### → `system/` (agent infrastructure)

| Legacy concern | Canonical |
|----------------|-----------|
| Orchestration, routing, states | `system/ORCHESTRATION.md` |
| Context manifest ("what to wake when") | `system/MEMORY.md` |
| Braindump loop, situation prompts | `system/coaching/` |
| Topic-dispatch skills | `system/skills/` |
| Eval harness, behavior specs, hooks | `system/evals/` |
| Artifact Quick Quality Check rules | `system/EVALUATION.md` |

### → `docs/` (human documentation)

Setup guides, architecture, principles, maintainer references (e.g. `agent-manifest.md`). Not loaded by the agent at runtime except when explicitly referenced.

### → Root bootstrap files (thinking split)

Personal and agent "thinking" used to live in Meta, company context, or scattered thinking files. The refactor **peeled these to root**:

| Concern | Canonical | What moved here |
|---------|-----------|-----------------|
| **Personal context** — name, role, how you work, strengths/challenges, communication prefs | **`USER.md`** | Was often embedded in company context or personal/thinking files |
| **Agent persona** — principles, routing intent, coaching posture, lens summary | **`AGENTS.md`** | Agent/thinking rules distilled from meta and orchestration docs |
| **Always-on enforcement** — voice, expanded lenses, braindump floor, minimal footprint | **`.cursor/rules/pm-brain.mdc`** | Enforcement layer; see [architecture.md](architecture.md#why-pm-brainmdc-exists) |
| **Platform entry points** | **`CLAUDE.md`**, **`.github/copilot-instructions.md`** | Wiring only — point at shared bootstrap |

**`1-Context/` did not go away.** Company vision, strategy, stakeholders, and org survival stay there. Only **personalization** moved to `USER.md` so org docs stay org-scoped.

---

## Internal renumbering

Top-level renames are not enough — subfolders were renumbered too.

### `02-Methods-and-Tools/` → `2-Methods/`

| Legacy | Canonical |
|--------|-----------|
| `2.0-Foundations/` | `1-Foundations/` |
| `2.1-Strategy/` | `2-Strategy/` |
| `2.2-Discovery/` | `3-Discovery/` |
| (execution domain) | `4-Execution/` |
| (communication domain) | `5-Communication/` |

### Inside `5-Growth/` (legacy decimals → canonical)

| Legacy | Canonical |
|--------|-----------|
| `0.1-Learning-Log/` | `1-Learning-Log/` |
| `0.2-Growth-Portfolio/` | `2-Growth-Portfolio/` |
| `0.3-Product-Judgment-Test/` | `3-Product-Judgment-Test/` |

Your fork may still have **both** (e.g. `5-Growth/0.1-Learning-Log/` and `5-Growth/1-Learning-Log/`). Consolidate into the `1-`, `2-`, `3-` paths and delete the `0.x-` copies.

---

## Other moves worth knowing

**Stakeholder avatars (split):**
- **Your avatar instances** → `1-Context/1.1-Stakeholder-Avatars/`
- **Framework + template** → `2-Methods/5-Communication/8-Stakeholder-Avatars/`

**Coaching entry:**
- Product thinking entry → `system/coaching/README.md` (not a top-level `thinking/` folder)
- Deep framework library → `2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/`

**Evals (fork):**
- Legacy pointer → `.cursor/evals/README.md` (redirects to `system/evals/`)
- Executable harness → `system/evals/` + [evals-fork.md](evals-fork.md) (shipped in upstream as of 4.0.0)
- Clean up duplicate scenario folders (e.g. `06-premature-solution/` vs `06-premature-solution-004/`) before deleting legacy eval paths

**Skills:**
- Canonical skills → `system/skills/`
- Platform wrappers may exist under `.cursor/skills/` or `.claude/skills/` — they point at `system/skills/`

---

## Partial migrations

Common during transition — **both** legacy and canonical folders exist:

- **`1-Context/1.2-Organization-Survival/`** may have only a subset while the full set still lives under **`01-Company-Context/1.2-Organization-Survival/`**
- **`00-Meta/`** may still exist alongside populated **`5-Growth/`**
- **`02-Methods-and-Tools/`** may duplicate **`2-Methods/`** content under old numbering

**What to do:** Diff legacy vs canonical, move missing files, update markdown links, then delete legacy folders.

Same logic applies to stakeholder avatars (`1.1-Stakeholder-Avatars/`) and onboarding glossaries (`1.3-Onboarding/`).

---

## Safe delete checklist

Before removing a legacy folder:

1. **Diff contents** — compare `01-Company-Context/` vs `1-Context/`, `00-Meta/` vs `5-Growth/` + `system/`, etc.
2. **Move anything missing** from legacy → canonical
3. **Grep for legacy paths** — search for `00-Meta`, `01-Company-Context`, `02-Methods-and-Tools`, `03-Research-Artifacts`, `04-Initiatives` in markdown links
4. **Check internal decimals** — remove `0.1-`, `0.2-`, `2.x.y` subfolders after consolidating into `N-Name` paths
5. **Update MEMORY triggers** — [system/MEMORY.md](../system/MEMORY.md) should reference canonical paths only
6. **Run link check** — `python system/evals/checks/verify-markdown.py` (if eval stack is present)
7. **Delete legacy folder** only when empty or fully superseded

---

## Numbering convention

The canonical model uses **`N-Name`** at each level (e.g. `2-Methods/3-Discovery/`). Legacy **`0.1-`**, **`2.x.y`**, or other decimal prefixes inside content folders are deprecated. See [architecture.md](architecture.md) → Linking Conventions.

---

## Related

- [setup.md](setup.md) — canonical folder tree and 1–5 model
- [principles.md](principles.md) — where things go
- [architecture.md](architecture.md) — full structure overview and bootstrap design
- [platform-setup.md](platform-setup.md) — per-platform bootstrap wiring
