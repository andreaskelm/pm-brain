# PM Brain — Human Documentation

Human-facing docs for setup, architecture, and maintenance. **The agent does not load this folder at bootstrap** — agent behavior lives in [AGENTS.md](../AGENTS.md), [`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc), [system/MEMORY.md](../system/MEMORY.md), and [USER.md](../USER.md). Individual docs here (e.g. [principles.md](principles.md), [architecture.md](architecture.md)) load **on demand** when [system/MEMORY.md](../system/MEMORY.md) wake triggers fire.

---

## Start here

| Doc | Audience | Purpose |
|-----|----------|---------|
| [setup.md](setup.md) | New users | Onboarding, 1–5 folder model, privacy modes, first initiative |
| [platform-setup.md](platform-setup.md) | All users | 4-file bootstrap + per-platform wiring (Cursor, Copilot, Claude Code, ChatGPT) |
| [principles.md](principles.md) | All users | Why the repo is designed this way — golden record, think-first, privacy |

---

## Reference

| Doc | Audience | Purpose |
|-----|----------|---------|
| [architecture.md](architecture.md) | Maintainers | Structure, loading layers, eval overview, linking conventions |
| [agent-manifest.md](agent-manifest.md) | Maintainers | Quick reference for entrypoints, states, content clusters (not agent-loaded) |
| [credits.md](credits.md) | Contributors | Framework attributions and external links |

---

## Fork maintainers

| Doc | Audience | Purpose |
|-----|----------|---------|
| [evals-fork.md](evals-fork.md) | Private fork owners | Harness, CI, upstream merge policy, scenario hygiene |
| [legacy-migration.md](legacy-migration.md) | Migrators | `00–04` → `1–5`, Meta→Growth split, bootstrap files, renumbering |

---

## Related (outside `docs/`)

- **Agent bootstrap:** [AGENTS.md](../AGENTS.md) → [pm-brain.mdc](../.cursor/rules/pm-brain.mdc) → [system/MEMORY.md](../system/MEMORY.md) → [USER.md](../USER.md)
- **Routing detail:** [system/ORCHESTRATION.md](../system/ORCHESTRATION.md) (state entry, not bootstrap)
- **Eval harness:** [system/evals/README.md](../system/evals/README.md)
- **Repo overview:** [README.md](../README.md)
