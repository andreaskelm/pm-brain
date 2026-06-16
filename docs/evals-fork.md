# Evals — Fork Maintainer Guide

This guide is for **private forks** that ship the executable eval stack under [`system/evals/`](../system/evals/README.md) and CI in [`.github/workflows/evals.yml`](../.github/workflows/evals.yml). Upstream [andreaskelm/pm-brain](https://github.com/andreaskelm/pm-brain) ships prose eval guides under `.cursor/evals/` only — no harness.

---

## Upstream vs fork

| Location | Upstream | This fork |
|----------|----------|-----------|
| Prose guides | `.cursor/evals/` | `system/evals/*.md` |
| Harness | None | `system/evals/harness/` |
| Scenarios | None | `system/evals/scenarios/` |
| CI | None | `.github/workflows/evals.yml` |
| Hooks | None | `system/evals/hooks/`, `.cursor/hooks/` |

**Merge policy:** When pulling upstream, reconcile prose changes into `system/evals/` manually. Do **not** blind-overwrite harness files, scenarios, or workflow YAML.

---

## Harness tiers (L0–L4)

These are **architecture tiers** — not the same as artifact Quick Quality Checks in `2-Methods/` (sometimes called "Level 1" in framework docs).

| Tier | What | Command / location |
|------|------|-------------------|
| **L0** | Repo health — markdown links, scenario index consistency | `python system/evals/checks/verify-markdown.py` |
| **L1** | Rubric regression (artifact eval fixtures) | `python system/evals/harness/run_rubric_regression.py --all --dry-run` |
| **L2** | Agent behavior scenarios | `python system/evals/harness/run_scenario.py <scenario-path>` |
| **L3** | Human coaching review | [1-agent-behavior-guide.md](../system/evals/1-agent-behavior-guide.md), stop hook |
| **L4** | In-turn write gate | `system/evals/hooks/validate_write.py` |

Full reference: [system/evals/README.md](../system/evals/README.md). Human checklist: [2-checklist.md](../system/evals/2-checklist.md).

---

## CI (GitHub Actions)

[`.github/workflows/evals.yml`](../.github/workflows/evals.yml) runs on push/PR to `main`/`master`:

1. **L0** — `verify-markdown.py` (link checks, orphan/duplicate scenario folders)
2. **L4** — `test_hook_validator.py` (hook unit tests)
3. **L1 dry-run** — `run_rubric_regression.py --all --dry-run`
4. **L2 structural dry-run** — `run_all.py --dry-run --skip-content --plumbing`

CI does **not** need the Cursor CLI — dry-run modes use structural checks only.

---

## Local commands

```bash
pip install -r system/evals/requirements.txt

# L0
python system/evals/checks/verify-markdown.py

# L2 plumbing (no agent)
python system/evals/harness/run_all.py --dry-run --skip-content --plumbing

# Single behavior scenario
python system/evals/harness/run_scenario.py system/evals/scenarios/behavior/01-braindump-floor-gate

# L1 rubric dry-run
python system/evals/harness/run_rubric_regression.py --all --dry-run
```

---

## Live runs (Cursor CLI)

Dry-run validates plumbing without calling an LLM. **Live runs** need the headless Cursor agent CLI — not the IDE.

Install, authenticate, and configure per [platform-setup.md → Cursor CLI](platform-setup.md#cursor-cli-optional--live-evals). Then re-run without `--dry-run` (and without `--skip-content` for L2 content judges).

```bash
python system/evals/harness/run_rubric_regression.py --all
python system/evals/harness/run_scenario.py system/evals/scenarios/behavior/01-braindump-floor-gate
```

Set `PM_BRAIN_CURSOR_BIN` if your binary is not `agent`.

---

## Scenario hygiene

**Naming:** Behavior scenarios live under `system/evals/scenarios/behavior/NN-slug/` (e.g. `06-premature-solution/`). The index in [agent-behavior-scenarios.json](../system/evals/agent-behavior-scenarios.json) maps `scenario_id` → `harness_path`.

**Duplicates:** L0 checks flag orphan folders (on disk but not in the index) and duplicate slugs. Remove or consolidate duplicates before merging.

**Ground truth:** Each scenario's `expected.yaml` plus [behavior-assertions.md](../system/evals/behavior-assertions.md) — not the JSON index alone.

---

## When behavior should change

Use the **"Where to update"** map in [1-agent-behavior-guide.md](../system/evals/1-agent-behavior-guide.md):

- Coaching voice, lenses, braindump floor → [`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc) and [AGENTS.md](../AGENTS.md)
- Routing, states, loading → [system/ORCHESTRATION.md](../system/ORCHESTRATION.md)
- Scenario expectations → scenario `expected.yaml` + [behavior-assertions.md](../system/evals/behavior-assertions.md)

After rule changes, run L2 dry-run plumbing, then spot-check one live scenario if you have the CLI installed.

---

## Related

- [platform-setup.md](platform-setup.md) — bootstrap and Cursor CLI install
- [architecture.md](architecture.md) — eval overview and L0–L4 vs artifact QQC
- [setup.md](setup.md) — general onboarding
