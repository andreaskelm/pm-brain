# Writing a PM Brain skill

PM Brain skills are **workflow owners**: they tell the agent when to fire, what to ask first, how to produce the artifact, and how to judge quality. Reference material humans read for depth stays in `2-Methods/`; skills stay portable (no markdown links outside the skill folder).

## Folder layout

```
.claude/skills/<name>/
  SKILL.md              # Required; keep under ~200 lines
  references/
    template.md         # Fill-in artifact (when applicable)
    criteria.md         # Red/green flags, dimensions, antipatterns, rewrites
    …                   # Method-specific refs (scoring, scripts, etc.)
```

## SKILL.md frontmatter

```yaml
---
name: <folder-name>   # must match folder
description: <what it does + trigger phrases users actually say>
disable-model-invocation: true   # optional; slash-only skills (e.g. brain-review)
---
```

The `description` is how Cursor/Claude **decide to load** the skill. Pack it with user phrases, not internal jargon.

## Body (opinionated structure)

1. **Opening** — what this is for, and the main failure mode you’ve seen.
2. **Is this the right thing?** — when *not* to use it; route to another skill by **name**.
3. **Preflight** — 2–3 questions; check repo paths as plain backticks before asking.
4. **Steps** — outcome-first, org-aware, not a textbook reprint.
5. **Red flags** — point to `references/criteria.md`.
6. **Before calling it done** — gut check, optional `artifact-reviewer`, `5-Growth/decisions.md` row when it’s a bet.
7. **Org reality** — 3–4 situations where the textbook version breaks.
8. **References** — only files inside this folder.

## criteria.md

Trimmed from the old `3-*-evaluation.md` files. Include: shared-process pointer to `system/EVALUATION.md`, red/green flags, weighted dimensions (if scored), antipatterns with quotes, 2–3 before/after rewrites. Flags-only is fine for process artifacts (e.g. prioritization).

## Voice

Same as [AGENTS.md](../AGENTS.md): direct, experienced, concrete. Stakeholder-facing **artifacts** the skill helps draft should stay clear and professional even when the coaching voice is casual.

## Repo-coupled vs portable

- **Artifact skills** (`write-prd`, `okr`, …): no links outside the folder; repo paths only as plain text when needed for logging.
- **Workflow skills** (`braindump`, `weekly-review`, …): may name `system/coaching/*`, `5-Growth/`, `1-Context/` as plain paths.

## Checklist before merge

- [ ] `name` matches folder; description has triggers
- [ ] SKILL.md &lt; ~200 lines
- [ ] criteria.md exists for scored artifact types
- [ ] [0-index.md](0-index.md) lists the skill
- [ ] [system/EVALUATION.md](../system/EVALUATION.md) criteria table updated
- [ ] Rubric regression `rubric_path` updated if criteria moved
- [ ] Old duplicate framework under `2-Methods/` removed or reduced to reference-only

Exemplars: `.claude/skills/write-prd/`, `.claude/skills/prioritize/`.
