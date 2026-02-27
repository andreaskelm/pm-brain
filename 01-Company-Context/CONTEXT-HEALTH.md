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
- **Last reviewed**: Optional free-form date/note; update only when you do a *meaningful* review.

#### Core company context

| Doc path | Role | Review cadence | Rot risk | Last reviewed |
|---------|------|----------------|----------|---------------|
| `01-Company-Context/1-company-vision.md` | Company mission & vision (directional north star) | Yearly or on major strategy shift | medium | - |
| `01-Company-Context/2-company-strategy.md` | Current strategy & priorities (inputs to OKRs, roadmaps) | Quarterly planning cycle | high | - |
| `01-Company-Context/5-company-roadmap.md` | Company-wide roadmap used in PM artifacts | Quarterly planning cycle | high | - |
| `01-Company-Context/6-company-stakeholders.md` | Canonical stakeholder directory for PM work | On major org change | high | - |

#### Politics & stakeholders

| Doc path | Role | Review cadence | Rot risk | Last reviewed |
|---------|------|----------------|----------|---------------|
| `01-Company-Context/1.1-Stakeholder-Avatars/README.md` | Index + guidance for stakeholder avatars used in politics checks | When adding/removing key stakeholders | medium | - |
| `01-Company-Context/1.1-Stakeholder-Avatars/0-example-director-engineering.md` | Example / seed avatar; adapt or replace with real cast | When real avatars are added | medium | - |
| `01-Company-Context/1.2-Organization-Survival/1-power-map.md` | Power map used in organization-survival / politics flows | On major re-orgs or leadership changes | high | - |
| `01-Company-Context/1.2-Organization-Survival/2-political-landscape.md` | Political landscape summary used for politics-coach flows | On major re-orgs or leadership changes | high | - |

#### Initiatives

| Doc path | Role | Review cadence | Rot risk | Last reviewed |
|---------|------|----------------|----------|---------------|
| `04-Initiatives/4.1-Initiative-Codename/roadmap.md` | Example initiative roadmap used in initiative-level planning | Per initiative planning cycle | medium | - |

---

### How reminders work (for agents and humans)

When the agent **wakes** context from `01-Company-Context/`, `04-Initiatives/`, or `03-Research-Artifacts/` *and* that doc appears in this table **with medium/high rot risk and an overdue cadence**, it may offer a short, optional prompt **in key flows only**, for example:

- “We’re about to lean on `01-Company-Context/5-company-roadmap.md`, which the context health table marks as likely-stale. Do you want to sanity-check whether it’s still roughly true before we treat it as ground truth?”

Ground rules for these reminders:

- Keep it **short and optional**.
- Offer clear escapes like: “quick sense-check now”, “assume roughly true and continue”, or “treat as historical for this session”.
- **Only** nudge when the doc is feeding into a real decision or artifact (roadmaps, OKRs, strategy docs, PRDs, initiative decisions, politics checks), not just casual browsing.

You can extend this file over time with more rows or adjust cadences/risks as you see what actually rots.

