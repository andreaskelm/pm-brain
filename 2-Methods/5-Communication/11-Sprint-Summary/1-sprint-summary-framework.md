# Sprint Summary Framework

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "sprint summary", "sprint update", "sprint communication", "what we shipped", "what we're focusing on next sprint", "send an update after sprint"
- User is in: `execution_mode` or explicitly asking to draft a communication artifact
- Prerequisites: Sprint has ended or is ending; user needs to inform stakeholders without scheduling a meeting
- User has: A sprint board they can screenshot and a rough sense of what was delivered and what's next

**How to introduce:**
- "You need to communicate the sprint transition to your stakeholders. Let's draft a sprint summary — it covers [last sprint delivery], [new sprint focus], and [expected outcomes] in one short async message."
- "The right artifact here is a sprint summary brief. Want me to help you draft it?"

**Common mistakes to avoid:**
- Don't conflate this with a sprint review agenda — this is a written async artifact, not a meeting structure
- Don't help the user write a polished PR piece — tone should be factual and direct
- Don't suggest this replaces a sprint review meeting; it complements it

**When NOT to use:** See [When to Use / When NOT to Use](#when-to-use--when-not-to-use) below.

---

## Step 0: Braindump & Product Sense (Do this first!)

⚠️ **Don't jump straight to the template.** See [braindump.md](../../../system/coaching/braindump.md) for why this step matters.

Before filling in the sprint summary, spend 2–3 minutes on these questions:

- What was the real focus of this sprint, in one sentence → (Not the sprint number — what problem or outcome were you chasing?)
- What actually moved the needle → (Separate the 2–3 things that mattered from everything else that got done.)
- Is there anything that didn't land that stakeholders should know about → (Name it before deciding whether to include it.)
- What's the real goal of the new sprint — and why is this the right focus *right now*→ (Not just "continued work on X" — what's the actual outcome you're aiming for?)

**Then proceed** to fill in the template.

---

## Overview

A sprint summary is a short async communication sent at every sprint transition. It covers what the team focused on, what was actually delivered, what the new sprint is targeting, and what outcomes you expect by the end.

**Purpose:** Keeps delivery leads and senior stakeholders informed at sprint boundaries without requiring a meeting — while giving the team visibility into how their work is being described externally.

**Core Value:** Builds stakeholder trust through consistent, factual communication — and gives the team a safety valve to flag anything that's being framed incorrectly.

---

## Core Philosophy

### A Sprint Summary is NOT a Sprint Review

A sprint review is a live meeting — demos, feedback collection, stakeholder Q&A. A sprint summary is an async written artifact that travels without you. Don't conflate them. The summary can accompany or reduce the need for the review, but they serve different functions.

**Common misconceptions:**
- ❌ "It's just a status report" — A status report tracks work. A sprint summary communicates outcomes and intent. The framing matters.
- ❌ "It replaces the sprint review" — It can complement or reduce the need for one, but a written summary can't replicate live demo feedback and stakeholder reaction.

### Core Principles

**Factual, not performative.** Write what happened, not the best version of it. Stakeholders who are paying attention can tell the difference between honest communication and spin. Plain language and one honest line about what didn't ship builds more trust than a flawless summary that papers over problems.

**The board is the detail layer.** Include a screenshot of the sprint board rather than trying to capture every item in prose. The written summary covers the goal and the key outcomes; the board screenshot handles the rest.

**Outcomes, not tickets.** When describing what was delivered, explain what it does or why it matters — not just the ticket name. "Reduced manual reconciliation steps in the month-end flow" is more meaningful than "Completed US-1234."

**Expected, not promised.** Use "aiming to deliver" or "expect to have done," not "will deliver." Sprint planning is forecasting, not commitment. Stakeholders with the right mental model will not be surprised when things shift.

**Team transparency by design.** Send it to the team too. If the framing is off — wrong emphasis, something they'd push back on — they need to see it and feel safe flagging it. This isn't about getting approval; it's about keeping the external narrative accurate.

---

## Structure

A sprint summary has two blocks. Keep it short enough to read in 90 seconds.

### Block 1: Last sprint close
- Sprint goal or theme (1–2 sentences on what the team focused on and why)
- What was delivered (3–5 outcomes, written as impact not ticket titles)
- Board screenshot (actual state, not curated)
- What didn't land (include only if something material slipped — one line per item, honest explanation)

### Block 2: New sprint open
- Sprint goal or theme (1–2 sentences on what the team is moving into and why now)
- Expected outcomes by end of sprint (3–5 items, tied to user or business value where possible)
- Board screenshot (planned sprint items)

### Closing
- Invitation to ask questions or flag anything that needs adjusting
- Short and open — not a corporate sign-off

---

## Writing Guidelines

**Do:**
- Lead with the sprint goal, not with meta-commentary about the update itself
- Write outcomes as "we delivered X" not "the team worked on X"
- Be specific — name the flow, the user group, the metric where relevant
- Keep each outcome to one line
- Include both screenshots even if the board looks messy — that's the point

**Don't:**
- Use ticket IDs or sprint board jargon as the only description ("Completed US-1234")
- Pad the completed list with items that were already done before the sprint started
- Over-explain what didn't ship — one honest sentence is enough
- Use passive voice to distance from bad news ("some items were not completed")
- End with corporate sign-off language

---

## Common Pitfalls

❌ **Writing a polished PR piece instead of a factual update**
✅ Write what happened. Stakeholders who are paying attention will notice the difference. Trust is built by being straight, not by looking polished.

❌ **Listing ticket names instead of outcomes**
✅ "Completed US-1234" tells stakeholders nothing. "Fixed the balance carry-over that was misaligning multi-farm accounts" tells them what changed and why it matters.

❌ **Hiding what didn't land**
✅ Omitting slippage doesn't make it go away — it just means stakeholders find out later with less context. One honest line is always better than silence.

❌ **Writing "will deliver" for new sprint items**
✅ Use "aiming to have done" or "expect to deliver." Sprint planning is a forecast. Set the right expectations before something changes, not after.

❌ **Not sending it to the team**
✅ The team should see exactly how their work is being described externally. If the framing is off, they're the ones who'll catch it — but only if they see it.

---

## When to Use / When NOT to Use

### Use this when:
- ✅ Sprint has ended and a new one is starting
- ✅ Your delivery leads or senior stakeholders don't have daily visibility into the sprint board
- ✅ You want the team to see how their work is being communicated externally
- ✅ You're running async-first and want to replace or complement a sprint review meeting

### Don't use this when:
- ❌ You need a **meeting structure** — use [Meeting Agendas](../2-Meeting-Agendas/) instead
- ❌ You need a **monthly stakeholder narrative** across multiple topics — use [Newsletter](../1-Newsletter/) instead
- ❌ You need to **communicate a major decision or proposal** — use [One-Pagers](../3-One-Pagers/) instead
- ❌ The team has **daily standups with stakeholders** already — the summary adds noise, not value

---

## Quality Checklist

- [ ] Sprint goal is stated in plain language (not just sprint number)
- [ ] Completed items describe outcomes, not ticket names
- [ ] Board screenshot included for last sprint
- [ ] Board screenshot included for new sprint
- [ ] Expected outcomes for new sprint are tied to value, not just activity
- [ ] Anything that slipped is mentioned (or deliberately omitted with a reason)
- [ ] Language is "aiming to" / "expect to" — not "will deliver"
- [ ] Short enough to read in 90 seconds
- [ ] Team has visibility (and knows they can flag wording)

---

## Cadence & Ownership

- **Frequency:** Every sprint transition — ideally within 24 hours of close/start
- **Owner:** PM/PO
- **Channel:** Async (Teams message, email, Slack — whatever stakeholders actually read)
- **Archive:** No formal archiving needed; save if you want a history of sprint goals

---

## References

- Sprint Summary Template: `2-sprint-summary-template.md`
- Meeting Agendas (for the sprint review meeting itself): `../2-Meeting-Agendas/`
- Newsletter (for monthly stakeholder narrative): `../1-Newsletter/`
- Stakeholder Management: `../7-Stakeholder-Management/`
