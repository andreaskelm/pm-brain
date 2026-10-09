---
name: write-prd
description: Write, draft, tighten, or restructure a PRD, product spec, requirements doc, or feature spec, including JTBD-style PRDs and user stories with Given/When/Then acceptance criteria. Use when the user says "write the PRD", "spec this out", "draft requirements", "turn this into a PRD", or "help me write up what we're building". Runs preflight questions before any drafting.
---

# Write a PRD

A PRD bridges discovery and execution: it turns a validated opportunity into something a team can build, with success defined *before* the solution. The failure mode I see most often isn't a badly formatted PRD. It's a well-formatted one written for a problem nobody checked. So the thinking comes first, and the document is just where it lands.

## Is a PRD even the right thing?

**Write one when** the solution approach has some validation behind it, more than one function has to execute (design, eng, ops, marketing), it's more than ~2 weeks of engineering, and you can say what success looks like in numbers.

**Don't, and say so, when:**
- The problem is still fuzzy → that's an opportunity assessment, not a PRD.
- It's an experiment under a week → a half-page spec: hypothesis, what we build, how we'll know.
- It's infrastructure or a technical spike → a tech design doc owned by engineering.

## Step 1 — Preflight (always, even when they say "just write it")

Ask 2–3 of these, picked for what's actually missing. Don't run the whole list.

- **Who is this really for?** One actual person and their situation, not a persona label.
- **What job are they hiring this to do,** and what do they do today instead?
- **How will you know it worked?** What number moves, from what to what?
- **What do you know vs. guess?** Which part rests on research, which on a stakeholder's say-so, which on a hunch?
- **Why this, why now?** The one-sentence answer for a skeptical exec.
- **What's explicitly out?**

Before asking, check the repo if it exists: `3-Work/[initiative]/` (opportunity assessment, research, earlier decisions) and `4-Research/`. Don't ask for what's already written down. Quote it back instead.

If they've clearly braindumped already (in this conversation or an initiative folder), one confirming question is enough. If they insist on skipping: name the risk in one sentence, then draft with explicit `[GAP: …]` markers where the thinking is missing. Never invent evidence to fill a box.

## Step 2 — Pick the size and the variant

| Size | When | Sections |
|---|---|---|
| **Minimal (2–3 pages)** | Well-understood problem, clear solution | Summary · Goals & metrics · Core requirements (P0 only) · Scope in/out · Open questions |
| **Standard (5–8 pages)** | Cross-functional, real complexity | + user flows, acceptance criteria, dependencies, risks, phases |
| **Comprehensive (10–15)** | Platform work, high risk, compliance | + architecture, data, security, performance, post-launch plan |

Default to minimal. You can always add; nobody reads the extra ten pages anyway.

**Variant:** [standard template](references/template.md) for most work; [JTBD template](references/template-jtbd.md) when the initiative is framed around a customer job and you want to measure job completion, not feature usage (it includes a compact one-page version). For breaking requirements into buildable stories: [user stories](references/user-stories.md).

## Step 3 — Draft, outcome first

1. **Write Goals & Success Metrics first.** Baseline → target → threshold, plus one guardrail (what must not get worse). If you can't write this section, stop. You're not ready for the rest.
2. **Problem statement in the user's words.** Pull real sentences from the braindump and research. Name the evidence tier where it's load-bearing: "documented (6 interviews)" vs. "verbal (Sales says)".
3. **Requirements as P0 / P1 / P2.** Every P0 gets Given/When/Then acceptance criteria. Push back on P0 inflation. If everything is P0, nothing is.
4. **Out of scope, with reasons.** This is the section that prevents the fight in sprint 4.
5. **Assumptions and risks.** Include the uncomfortable one from the braindump. "What if we're wrong about why they churn?" belongs in the PRD, not just in your head.
6. **Open questions with owners.** An open question without an owner is a future surprise.

While drafting, flag gaps without blocking: *"This assumes setup completion drives retention, but earlier you said you haven't checked that. Leave it as an assumption with a test, or go check first?"*

## Step 4 — Watch for red flags as it takes shape

Missing metrics, vague requirements, no specific user, no baselines, solution-first opening, hidden assumptions, no link to discovery, unbounded scope. Full list, weighted dimensions and rewrite examples: [criteria](references/criteria.md). When one appears: name it, ask one question, suggest the fix. Don't silently fix it, or the user never learns to see it.

## Step 5 — Before calling it done

- **Gut check:** "Explain this PRD to a skeptical engineer in two minutes. What would they poke first?"
- **Quick check** against the red/green flags. Offer the full scored evaluation only if they want it, or before a high-stakes review.
- **Independent review:** if the `artifact-reviewer` subagent is available, offer it, since fresh eyes catch what the author can't. Discuss its findings; don't just paste them.
- **Log the bet:** if they stated (or can state) a confidence that this moves the metric, offer a row in `5-Growth/decisions.md` with a reopen trigger.

## Org reality

- **The PRD-as-contract org.** Some places use PRDs to assign blame later, so people pad them defensively. Keep the real thinking (bets, assumptions, kill criteria) in the doc anyway. A short "what would make us stop" section protects the team better than 40 pages of requirements.
- **"Leadership wants a 20-page spec."** Write the minimal PRD, then add an appendix. The people who need the depth will find it; the rest read page one.
- **PRD written after the build started.** Common, and not a crime. Be honest in the doc: mark which decisions were made upfront and which are retroactive, and use the PRD to lock scope from here.
- **Engineering ignores PRDs.** Usually because they arrive finished. Bring the tech lead in at the goals-and-problem stage. A PRD they shaped is one they read.

## References

- [references/template.md](references/template.md) — standard PRD template
- [references/template-jtbd.md](references/template-jtbd.md) — JTBD PRD, plus a compact one-page format
- [references/user-stories.md](references/user-stories.md) — stories, splitting, INVEST
- [references/criteria.md](references/criteria.md) — red/green flags, weighted dimensions, antipatterns, rewrites
