# PM Brain skills

Native Agent Skills for Cursor, Claude Code, and VS Code. Each folder is one skill; the agent loads `SKILL.md` when the user’s request matches the `description` in frontmatter.

**Index (skills + reference docs):** [2-Methods/0-index.md](../../2-Methods/0-index.md)

| Skill | Purpose |
|--------|---------|
| braindump | Product sense coaching before structure |
| weekly-review | Week plan + drift sweep + draft `5-Growth/weekly/` note |
| evaluate-artifact | Score drafts via `system/EVALUATION.md` + criteria files |
| brain-review | File/folder freshness and repo health (slash-only) |
| write-prd | PRD / spec / JTBD variant / user stories |
| prioritize | RICE, ICE, MoSCoW, Kano, backlog |
| opportunity-assessment | Go / no-go before a PRD |
| discovery-synthesis | Interviews, CDH, JTBD, OST, PMF, personas |
| okr | Objectives and key results |
| roadmap | Now / Next / Later |
| north-star | North Star metric + input tree + AARRR |
| strategy | GSBS, Playing to Win, team strategy doc |
| stakeholder-comms | One-pagers, updates, escalation, decision records |
| politics-coach | Power, politics, stakeholder simulation |

Subagents (not skills): `.claude/agents/` — `context-scout`, `artifact-reviewer`, `stakeholder-simulator`.
