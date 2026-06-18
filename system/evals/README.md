# PM Brain Evals

Evaluation system for the PM Brain **Coach** — specs, harness, judges, hooks.

**Canonical location:** All eval specs, harness, and scenarios live here. [`.cursor/evals/`](../../.cursor/evals/README.md) is a pointer only. CI: [`.github/workflows/evals.yml`](../../.github/workflows/evals.yml). Maintainer guide: [docs/evals-fork.md](../../docs/evals-fork.md).

## Quick mental model

| Layer | What | Where |
|---|---|---|
| **L0** | Repo health | `checks/verify-markdown.py` |
| **L2 behavior** | Agent coaching replay | `scenarios/behavior/` → `run_scenario.py` |
| **L1 rubric** (optional) | Rubric calibration | `scenarios/rubric/<slug>/` → `run_rubric_regression.py` |
| **L3** | Human coaching review | `judges/self_critique_coaching.md`, stop hook |
| **L4** | In-turn write gate | `hooks/validate_write.py` |

L0–L4 are architecture tiers. Folder names describe function (`behavior/`, `rubric/`), not level numbers.

## Quick start

```bash
# L0 — CI
python system/evals/checks/verify-markdown.py

# L2 behavior — structural plumbing (no Cursor CLI)
pip install -r system/evals/requirements.txt
python system/evals/harness/run_all.py --dry-run --skip-content --plumbing

# L2 — single scenario
python system/evals/harness/run_scenario.py system/evals/scenarios/behavior/01-braindump-floor-gate

# L1 rubric regression (optional — dry-run needs no CLI)
python system/evals/harness/run_rubric_regression.py --all --dry-run
```

**Live runs** (real LLM judges) need the [Cursor CLI](../../docs/platform-setup.md#cursor-cli-optional--live-evals): install `agent`, authenticate, set `PM_BRAIN_CURSOR_BIN` if needed, then re-run without `--dry-run` (and without `--skip-content` for L2).

```bash
# Hook unit tests
python system/evals/harness/checks/test_hook_validator.py
```

Harness JSON → `eval-results/` (gitignored, auto-pruned). Not agent memory — see [eval-results/README.md](eval-results/README.md).

## Folder map

| Path | Purpose |
|---|---|
| [scenarios/README.md](scenarios/README.md) | behavior vs rubric scenario types |
| [agent-behavior-scenarios.json](agent-behavior-scenarios.json) | Index only (`scenario_id` → `harness_path`) |
| [expected-yaml-schema.md](expected-yaml-schema.md) | Ground-truth schema |
| [1-agent-behavior-guide.md](1-agent-behavior-guide.md) | Human transcript review |
| `harness/` | Runners |
| `judges/` | Judge contracts (framework rubrics stay in `2-Methods/`) |

**Canonical behavior spec:** each `scenarios/behavior/<slug>/expected.yaml`. The JSON catalog is for discovery and stub generation only.

## Manual transcript review

Match your chat to a `scenario_id` via the JSON index, then read that scenario's `expected.yaml` and README. Log optional notes in `eval-results/` using the template in [eval-results/README.md](eval-results/README.md).

## Self-learning loops

1. **In-turn:** `hooks/validate_write.py` blocks template scaffolds in `3-Work/` without thinking markers.
2. **Stop hook:** queues L3 self-critique in `eval-results/`.
3. **Harness failure:** edit `spec_owner` file → re-run.

Routing: [../ORCHESTRATION.md](../ORCHESTRATION.md).

## Adding scenarios

**Behavior:** create `scenarios/behavior/NN-<slug>/`, add index entry in `agent-behavior-scenarios.json`, run `run_scenario.py`.

**Rubric (optional):** copy `scenarios/rubric/prd/` (or `okr/`, `oa/`, `roadmap/`, `north-star/`, `one-pager/`), set `rubric_path`, edit specimens, run `run_rubric_regression.py`. One folder per rubric you actively maintain — not one per framework preemptively.
