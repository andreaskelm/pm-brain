---
name: launch-gtm
description: Plan, tighten, or review a product launch and go-to-market motion: rollout phases, beta and GA readiness, sales enablement, marketing launch, and release comms (internal and external). Use when the user says "launch plan", "go-to-market", "GTM", "rollout", "beta launch", "GA", "general availability", "sales enablement", "marketing launch", "release comms", "how do we ship this", or "what do we need before we flip the switch". Runs preflight on launch type, audience, and success definition before structuring anything.
---

# Launch & GTM

Shipping is the easy part. What I've generally seen kill launches isn't a missing banner ad — it's nobody agreed what "launched" means, sales is demoing something support can't explain, and the metric you care about has no baseline the week you go live. A launch plan is the handoff from build to adoption: who hears what, when, with what proof, and how you'll know if it worked. If you can't point at the success metrics from the write-prd skill (baseline, target, guardrail), you're not ready to name a date; you're ready to learn.

## Is a launch plan even the right thing?

**Plan one when** the thing is real enough to put in a customer's hands (beta or GA), more than one function has to move (eng, support, sales, marketing, legal), and someone outside the team will notice if you get it wrong.

**Don't, and say so, when:**
- **The problem or solution is still fuzzy.** That's opportunity assessment territory, not a rollout calendar.
- **It's a dark launch or internal-only flag.** You need a short release note and an owner, not a GTM program.
- **It's a fix or a tiny change** with no positioning shift. A changelog entry and a Slack post may be enough.
- **You're being asked for a date before there's a shippable slice.** Push back on the date; offer a beta scope and learning goals instead.

## Step 1 — Preflight (always, even when they say "just make a checklist")

Ask 2–3 of these, picked for what's actually missing:

- **What kind of launch is this?** Private beta, open beta, phased rollout, big-bang GA, sales-led only, self-serve only. Each has a different comms and enablement bar.
- **Who must succeed for this launch to count?** One named customer segment or internal champion, not "users."
- **What does "done" look like in numbers?** Pull from the PRD's Goals & Success Metrics if they exist: baseline → target → guardrail. If those aren't written, stop and use write-prd thinking first — you can't evaluate launch week without them.
- **Who owns the narrative?** Product, marketing, or a exec sponsor — and who approves customer-facing language?
- **What's the worst realistic launch day?** Outage, wrong pricing, broken onboarding, sales overpromising. Name one; that's your readiness test.
- **What do you know vs. guess?** Especially adoption, support volume, and sales pipeline lift. Name the evidence tier where it's load-bearing.

Before asking, check what's already in the conversation or initiative folder. Quote it back instead of re-asking. Routine beta with an obvious audience: one scoping question is enough. If they insist on skipping: name the risk in one sentence, then draft with `[GAP: …]` markers. Never invent metrics or launch dates to make a plan look finished.

## Step 2 — Map the motion

| Launch type | Typical bar | Comms emphasis |
|---|---|---|
| **Internal / dogfood** | Runbook, support playbook draft, rollback | Internal only; no external promises |
| **Private beta** | Known customers, feedback channel, success criteria for exit | Invitation + expectation-setting; no broad marketing |
| **Open beta / early access** | Scale limits, known gaps documented, support staffed | "Works for X, not yet Y"; guardrails on who should join |
| **GA / general availability** | SLAs, billing, security/compliance if relevant, full enablement | Clear value prop, migration path, what changed for existing users |
| **Enterprise / sales-led** | Demo path, security pack, objection handling, implementation guide | Sales enablement before marketing air cover |

Full phased checklist (readiness, launch day, post-launch, feedback): [launch-checklist](references/launch-checklist.md).

For written stakeholder messages (exec brief, status, customer email, internal all-hands blurb), use the stakeholder-comms skill — this skill owns *what* ships and *when*, not every sentence.

## Step 3 — Build the plan: readiness before air cover

Work in order. Marketing before support is ready is how you buy a week of angry tickets.

1. **Anchor on PRD success metrics.** Every launch goal should trace to something already in write-prd form: the primary metric, the threshold that means "keep going," and the guardrail (what must not get worse). Launch adds *when* you read each metric and *who* watches it — not new vanity stats.
2. **Define launch tiers.** What's in beta vs GA; what's P0 for day one vs "fast follow." If everything is day one, nothing is.
3. **Internal readiness.** Runbook, rollback, on-call, feature flags, docs for support, FAQ for known gaps. Train support and success before sales hears "it's live."
4. **External readiness.** Positioning one-liner, release notes, in-product what's new, pricing/billing if it changes. Legal/compliance review if you need it — not the night before.
5. **Enablement.** For sales-led: talk track, demo script, competitive notes, "say this / don't say this." For self-serve: onboarding path and empty states that match what marketing promised.
6. **Comms calendar.** Internal first (so nobody is surprised), then customers, then market. Each message: audience, channel, owner, approve-by date, and the single sentence they must hear.
7. **Launch day and T+1.** Who is in the war room, what gets monitored, what triggers rollback or a hotfix comms. First 24 hours are operations, not strategy.
8. **Post-launch rhythm.** Daily metric check the first week, then weekly; feedback triage; decision on expand vs fix vs pause. Schedule the retro before everyone forgets.

While drafting, flag gaps without blocking: *"You're planning a GA blog post but success metrics still say 'TBD.' Lock the guardrail or call this a beta."*

## Red flags while it takes shape

A launch date with no rollback story. External comms before internal ones. Sales enabled before support. Success metrics that aren't in the PRD (or that have no baseline). "Awareness" as the only goal. Beta without exit criteria. GA with a public roadmap of unfinished P0s. One big email instead of segmented messages. No owner for feedback. Launch day with no named DRI. When one shows up: name it, ask one question, suggest the fix. Don't silently fix it.

## Before calling it done

- **War-game launch day:** "Support gets 3x tickets. Sales promises a feature that's P1. The flag is at 50%. What's the comms and who decides?" If nobody can answer, the plan isn't done.
- **Metric rehearsal:** "How will you pull baseline, target, and guardrail on day 7? Who owns the readout?" Tie explicitly back to write-prd success metrics — if the dashboard doesn't exist, that's pre-launch work.
- **Skeptical reader test:** Run the stakeholder-comms two-minute test on the customer-facing blurb and the internal "it's live" note.
- **Politics check:** if a named exec or big customer is in the blast radius, offer the politics-coach skill before the announcement goes wide.
- **Log the bet:** if they're stating confidence that launch hits the target, offer a forecast with a reopen trigger (what would make you pause rollout or roll back).

## Org reality

- **Marketing wants a date; eng wants "when it's ready."** You're not picking sides — you're naming the scope that matches the date. Smaller launch with honest limits beats a GA label on a beta body.
- **Sales already told customers it's shipped.** Happens constantly. Plan a "reset" comms path: what's true today, what's coming, how to set expectations without throwing sales under the bus.
- **Feature factory launch.** Sometimes "launch" is a checkbox for leadership. Still write the one-page internal brief: what changed, for whom, and how we'll know by Friday. That protects the team when nobody reads the deck.
- **Silent launch.** Valid for risk reduction. Document it anyway so support and success don't learn from Twitter.

## References

- [references/launch-checklist.md](references/launch-checklist.md) — pre-launch readiness, launch day, post-launch metrics, feedback loop; internal vs external comms; PRD metric tie-in
