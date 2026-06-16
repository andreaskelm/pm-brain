## Context Health — Living Company Docs

This file tracks how **healthy and up-to-date** your key company context docs are, so you and the agent know when to ask: **“Is this still roughly true?”**

- **Who maintains this:** You (humans), by hand.
- **How the agent uses this:** As a hint for when to offer a short, optional freshness check when those docs are used as inputs to real work (roadmaps, OKRs, strategy, PRDs, initiative decisions, politics checks).
- **What this is NOT:** A strict schedule or task list. Cadences and dates are soft guidance; you can always say “assume roughly true and continue” or “treat this as historical”.

### Freshness index for living docs

The table below is the **freshness index** for context docs that act as living inputs.

- **Doc path**: Path from repo root.
- **Role**: How this doc is used in practice (source of truth vs. historical reference).
- **Review cadence**: How often you *roughly* want to sanity-check it (quarterly, per initiative, on major org change, etc.).
- **Rot risk**: Gut feel about how quickly this goes stale (`low` / `medium` / `high`).
- **Maintained?**: `Maintained` (PM actively owns and updates), `Reference` (background context; agent reads but should not suggest updating), or `External` (managed outside PM Brain).
- **Last reviewed**: Optional free-form date/note; update only when you do a *meaningful* review.

#### Core company context

| Doc path | Role | Review cadence | Rot risk | Maintained → | Last reviewed |
|---------|------|----------------|----------|-------------|---------------|
| `1-Context/1-company-vision.md` | Company mission & vision | Yearly or on major strategy shift | medium | Reference | - |
| `1-Context/2-company-strategy.md` | Strategy & priorities (inputs to OKRs, roadmaps) | Quarterly planning cycle | high | Reference | - |
| `1-Context/3-company-product-principles.md` | Product principles | On major strategy shift | low | Reference | - |
| `1-Context/4-company-product-explanation.md` | Product portfolio for PM's team | After significant product changes | high | Maintained | - |
| `1-Context/5-company-roadmap.md` | Company-wide roadmap | Quarterly planning cycle | high | External | - |
| `1-Context/6-company-stakeholders.md` | Stakeholder directory | On major org change | medium | Reference | - |

#### Politics & stakeholders

| Doc path | Role | Review cadence | Rot risk | Maintained → | Last reviewed |
|---------|------|----------------|----------|-------------|---------------|
| `1-Context/1.1-Stakeholder-Avatars/` | Stakeholder avatars (one file per person) | When key stakeholders change role or stance | high | Maintained | - |
| `1-Context/1.2-Organization-Survival/1-power-map.md` | Power map for politics/org-survival flows | On major re-orgs or leadership changes | high | Reference | - |
| `1-Context/1.2-Organization-Survival/2-political-landscape.md` | Political landscape summary for politics-coach flows | On major re-orgs or leadership changes | high | Reference | - |

#### Initiatives

| Doc path | Role | Review cadence | Rot risk | Maintained → | Last reviewed |
|---------|------|----------------|----------|-------------|---------------|
| `3-Work/1-Initiative-Codename/` | Example: active initiative | Per sprint/cycle | high | Maintained | - |

---

### How reminders work (for agents and humans)

When the agent **wakes** context from `1-Context/`, `3-Work/`, or `4-Research/` *and* that doc appears in this table **with medium/high rot risk and an overdue cadence**, it may offer a short, optional prompt **in key flows only**, for example:

- “We’re about to lean on `1-Context/5-company-roadmap.md`, which the context health table marks as likely-stale. Do you want to sanity-check whether it’s still roughly true before we treat it as ground truth?”

Ground rules for these reminders:

- Keep it **short and optional**.
- Offer clear escapes like: “quick sense-check now”, “assume roughly true and continue”, or “treat as historical for this session”.
- **Only** nudge when the doc is feeding into a real decision or artifact (roadmaps, OKRs, strategy docs, PRDs, initiative decisions, politics checks), not just casual browsing.
- **When a doc is `Reference` or `External`:** do NOT suggest updating it, regardless of what the conversation surfaces. Route new findings and learnings to initiative context (`3-Work/`) instead. Only offer to promote to company context if the finding has clear cross-cutting significance across multiple initiatives.

You can extend this file over time with more rows or adjust cadences/risks as you see what actually rots.

