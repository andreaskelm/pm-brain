# Writing a PM Brain skill (this repo)

Skills are **workflow routers**: when to fire, preflight, coaching steps, org reality, and **paths into `2-Methods/`**. They are not a second copy of the framework library.

Architecture: [docs/skills-and-methods.md](../docs/skills-and-methods.md).

## Folder layout

```
.claude/skills/<name>/
  SKILL.md              # Required; aim for ~80–120 lines of coaching + routing
  references/
    criteria.md         # Quick red/green only (optional)
    template.md         # Optional portable copy; must match 2-Methods or point to it
    …                   # Short summaries only when needed for npx skills install
```

## SKILL.md frontmatter

```yaml
---
name: <folder-name>   # must match folder
description: <what it does + trigger phrases users actually say>
disable-model-invocation: true   # optional; slash-only skills (e.g. brain-review)
---
```

## Body

1. **Canonical paths table** — `2-Methods/.../1-framework`, `2-template`, `3-evaluation` when the artifact has them.
2. **Is this the right thing?** — route to other skills by name.
3. **Preflight** — 2–3 questions; check `3-Work/`, `4-Research/`, `1-Context/` first.
4. **Steps** — follow the **section order of the canonical template**, not a reinvented outline.
5. **Red flags** — quick check file or framework “Quick Quality Checks”.
6. **Before calling it done** — quick check vs full eval (`3-*-evaluation.md`); `artifact-reviewer`; `5-Growth/decisions.md` when it’s a bet.
7. **Org reality** — a few real failure modes.

## criteria.md (quick check only)

Excerpt red/green flags aligned with the framework. Point to `2-Methods/.../3-*-evaluation.md` for full scored eval. Shared process: `system/EVALUATION.md`.

Do **not** trim the full evaluation into criteria and treat it as canonical.

## Templates

- **PM Brain private repo:** agents load `2-Methods/.../2-*-template.md`.
- If `references/template.md` exists, keep it identical to `2-Methods` or start with “use canonical path” and paste the same content.

## Checklist before merge

- [ ] `name` matches folder; description has triggers
- [ ] Canonical `2-Methods/` paths in `SKILL.md`
- [ ] No competing artifact shape (template sections match methods)
- [ ] [0-index.md](0-index.md) and [docs/skills-and-methods.md](../docs/skills-and-methods.md) updated if needed
- [ ] [system/EVALUATION.md](../system/EVALUATION.md) quick vs full table
- [ ] Rubric regression `rubric_path` → `3-*-evaluation.md` when applicable

Exemplar after alignment: `.claude/skills/opportunity-assessment/`.
