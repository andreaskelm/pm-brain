## `.cursor/rules` – Workspace Rules Overview

This directory contains **rule files** that tell the AI how to behave in this workspace. They are **local to this repo** and can be tailored to your work style and projects.

### What these files are

- `thinking.mdc` – General "how to think with me" instructions for the AI (e.g. coaching style, language handling, focus areas).  
- `thinking.personal.mdc` – **Template** for your personal context: name (or alias), working style, preferences. You should fill this with your own information (or keep it blank) and avoid committing sensitive details to public repos.  
- `product-sense.mdc` – **Golden rule:** When the user is braindumping or thinking through a product decision, apply the rule from `PRODUCT-SENSE-RULES.md` (repo root). Braindump before structure; use prompts from the product-sense template; don't suggest frameworks until after thinking.  
- `AGENTS.template.md` – Template/guide for defining custom AI "agents" (roles) for this workspace. **Note:** This is separate from the root `AGENTS.md` file, which defines the PM Brain Assistant for navigating the repository.

### Flexible Rule Structure

**Consider creating multiple rule files for different purposes:**
- `thinking.mdc` – Core coaching and thinking style (always relevant)
- `thinking.personal.mdc` – Personal preferences (always relevant)
- `thinking.code.mdc` – Code-specific rules (apply when coding)
- `thinking.docs.mdc` – Documentation rules (apply when writing docs)
- `thinking.strategy.mdc` – Strategy/planning rules (apply for strategic work)
- `thinking.review.mdc` – Review/critique rules (apply when reviewing work)

**Benefits of multiple rules:**
- **Context-aware**: Rules apply only when relevant (use `alwaysApply: false` and reference them in prompts)
- **Focused**: Each rule file stays focused on its domain
- **Maintainable**: Easier to update specific areas without touching everything
- **Flexible**: Mix and match rules based on the task at hand

**How to use multiple rules:**
- Set `alwaysApply: false` in rule files you want to invoke selectively
- Reference specific rules in your prompts: "Use the strategy thinking rules for this task"
- Or let the AI suggest which rules are relevant based on the work you're doing  

> **Important:** These files are meant to describe *how* you want the AI to work with you – not to store confidential business data. Keep actual private/company information in regular project files that are not shared publicly.

### When and how rules are applied

- Rules in `thinking.mdc` can be referenced whenever you ask for:
  - Strategic thinking, coaching, or decision support
  - Help structuring work (roadmaps, OKRs, discovery, PRDs, etc.)
  - Help synthesizing notes, research, or stakeholder input
- `thinking.personal.mdc` is used **only** to adapt tone, pacing, and structure to your preferences (e.g. more bullets, slower pacing, more probing questions).
- `AGENTS.template.md` is a guide for creating custom "personas" or roles (e.g. Product Coach, Architect, Research Partner) that you can invoke explicitly in prompts. **Note:** The root `AGENTS.md` file defines the PM Brain Assistant for this repository—use `AGENTS.template.md` to create additional custom agents.
- **Domain-specific rules** (if you create them) should be referenced when working in that domain, or let the AI suggest which rules are relevant.

**Rule evolution:**
- The AI will proactively ask if rules should be updated after insightful conversations
- Rules should evolve as you learn what works best for your workflow
- Keep rules living documents that reflect your current working style

### Quick start: set up your rules

You can use the prompt below to have the AI help you configure these rule files:

```markdown
Act as a workspace setup coach. I want to configure `.cursor/rules` for this repo.

1) Ask me:
- What kind of work I mostly do here (e.g. product, engineering, research, writing, coding).
- How I like to work (e.g. lots of structure vs. loose exploration, written vs. spoken style).
- Any accessibility or neurodiversity considerations I want you to adapt to.

2) Help me fill out or adjust:
- `thinking.mdc`: high-level description of how I want the AI to think and support me.
- `thinking.personal.mdc`: my working preferences and communication style (keeping sensitive details minimal or private).
- `AGENTS.template.md`: 1–3 agents/roles that would be genuinely useful for this repo (separate from the root `AGENTS.md` which defines the PM Brain Assistant).

3) Propose:
- A short checklist for keeping these rules up to date.
- Any safeguards I should consider so private/company information doesn’t leak into public repos.

I'll start by telling you what I use this repo for and how I like to work.
```

### Using these rules across tools

- In **Cursor**, this `.cursor/rules` folder is read automatically; update these files and commit them to keep behavior consistent across collaborators.  
- In other tools (e.g. **Replit**, **VS Code + AI extensions**), you can **reuse the same content** by:
  - Copying relevant sections from `thinking.mdc`, `thinking.personal.mdc`, and the root `AGENTS.md` into those tools' "system prompt" / "instructions" / "workspace settings" areas.  
  - Keeping this folder as the **single source of truth**, and pasting updated snippets into other IDEs when needed.
- If you adopt multiple IDEs, consider adding a short “Where I use these rules” note here with links or notes for each environment (Cursor, Replit, VS Code, etc.).
