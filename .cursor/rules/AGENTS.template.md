# Custom Agents Template

This file is a **template/guide** for defining custom AI agents (roles) for your workspace. This is **separate** from the root `AGENTS.md` file, which defines the PM Brain Coach agent for navigating this repository.

Use the prompt below to have the AI help you design and fill out your own custom agent definitions.

```markdown
Act as a documentation coach. I want to define one or more AI agents (roles) for my workspace in an `AGENTS.md` file.

1) Ask me:
- What kinds of work I do here (e.g. coding, product, research, writing).
- Which distinct AI "roles" might help (e.g. Product Coach, Code Reviewer, Research Assistant, Writing Partner).

2) For each agent:
- Help me define:
  - **Name** and short description
  - **Primary responsibilities** (what this agent should help with)
  - **Do / Don't** guidelines (tone, level of challenge, when to ask questions)
  - **Inputs** it expects (e.g. "link me to the repo + ticket", "paste your notes")
  - **Outputs** it should produce (e.g. structured plans, code suggestions, critiques)

3) Draft an `AGENTS.md` structure like:
- One section per agent with:
  - Overview
  - Usage examples
  - Prompts I can copy-paste to start a session with that agent.

4) At the end:
- Summarize the agents we defined.
- Suggest 1–2 gaps where an additional agent could be useful.

I'll start by telling you what kind of work I usually do in this repo.
```
