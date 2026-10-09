---
name: stakeholder-comms
description: Write, tighten, or review written stakeholder communication: one-pagers, exec summaries, decision docs, status updates, newsletters, sprint summaries and sprint review updates, meeting agendas, escalations, saying no or pushing back on a request, decision records and ADRs. Use when the user says "write a one-pager", "draft an exec summary", "write an email to my VP", "I need to send a status update", "summarize the sprint for stakeholders", "set up an agenda", "help me escalate this", "how do I tell them no", "push back on this request", or "write up this decision". Runs a preflight on reader and ask before drafting.
---

# Stakeholder Comms

Clear writing is clear thinking made visible. If you can't say in one sentence what you want from the reader, a template won't fix that. It'll just hide the fuzziness under nice headings. The reader decides in about 30 seconds whether this needs them, and most stop reading right there. What I've generally seen is that the messages that land were written by someone who knew what they wanted before they opened the doc. So we get the reader and the ask straight first, then write: bottom line up top, one message per doc, and no doubt about whether you need a decision or are just keeping people informed.

## Is a document even the right move?

- **Two people actively disagree?** Talk first, then write up what you agreed. A doc fired into a live disagreement reads as a power move.
- **The reader has never heard of this and you need a decision?** Pre-wire with a 10-minute conversation, then send the doc. A decision request landing cold feels like an ambush, and ambushed people say "let's discuss".
- **The bad news is about a person?** Say it in person. Write it down afterwards if it needs a record.
- **A recurring meeting that's only status?** Replace it with a written update and keep the meeting for decisions.

## Step 1 — Preflight (always, even when they say "just write it")

Ask 2–3 of these, picked for what's actually missing:

- **Who actually reads this?** One named person, not "leadership". What's their day like when it lands?
- **What do you want them to do or decide after reading?** If the answer is "be aware", ask whether it needs sending at all, or whether it's an FYI that should ride along with something else.
- **What do they already believe?** About the problem, about the team, about you. You're writing against that, not into a vacuum.
- **What's the one sentence?** If they read nothing else, what must they walk away with?
- **What do you know vs. guess?** Especially the numbers you're about to put in front of an exec. Name the evidence tier where it's load-bearing.
- **What reaction are you dreading?** That's usually the paragraph that's missing.

Before asking, check the repo if it exists. Named reader: look in `1-Context/1.1-Stakeholder-Avatars/` for their priorities, pet peeves and preferred format, and quote it back ("Your avatar says she wants the number first and the risk second, so let's open with that"). Named initiative: `3-Work/[initiative]/` for earlier decisions this message might contradict. Don't ask for what's already written down.

Routine docs (a standing agenda, a sprint summary with an obvious goal): one scoping question is enough. If they insist on skipping: name the risk in one sentence, then draft with `[GAP: …]` markers where the thinking is missing. Never invent numbers to make a doc look finished.

## Step 2 — Pick the format

| Situation | Format | Reference |
|---|---|---|
| You need a yes/no or a choice between options from someone senior | Decision one-pager | [one-pager](references/one-pager.md) |
| Proposing a new bet, need buy-in, budget or headcount | Product one-pager | [one-pager](references/one-pager.md) |
| "Write an email to my VP" | Usually a decision one-pager squeezed into an email, or an escalation. Ask which | [one-pager](references/one-pager.md), [escalation](references/escalation-saying-no.md) |
| "Where are we?" from an exec or steering group | Status update | [updates](references/updates.md) |
| Sprint closed, stakeholders don't live on the board | Sprint summary | [updates](references/updates.md) |
| Monthly update to a broad, mixed audience | Newsletter | [updates](references/updates.md) |
| A meeting has to produce a decision | Decision-first agenda | [agendas](references/agendas.md) |
| Blocked by something beyond your authority, information or resources | Escalation | [escalation and saying no](references/escalation-saying-no.md) |
| A request you can't or shouldn't take on | Saying no | [escalation and saying no](references/escalation-saying-no.md) |
| Decision made, and someone will ask "why did we do this?" in six months | Decision record | [decision records](references/decision-records.md) |
| Engineering-internal architectural choice | ADR | [decision records](references/decision-records.md) |

Not covered here: incident and outage comms (different rhythm entirely), stakeholder mapping, and power and politics. For the politics, use the `politics-coach` skill.

## Step 3 — Draft: the core moves

**Lead with the ask or the bottom line.** The first line carries the conclusion, the ask and the deadline. Compare "Following last week's sync, I wanted to share some thoughts on onboarding…" with "I need a yes by Friday on moving two engineers to onboarding for Q2. Here's why." Write the TL;DR last, put it first.

**One message per doc.** Two asks means two docs, or one ask plus a clearly labelled FYI section. What tends to happen with three asks is the reader answers the easiest one and the important one quietly dies.

**Decision or FYI: say which, up front.** Put it in the subject line: "[Decision needed by Thu]" or "[FYI, no action]". Most status updates fail because one real decision is buried in eight paragraphs of activity.

**Numbers over adjectives.** "Improve triage significantly" says nothing. "Triage from 30 min to 5 min per alert" can be argued with, which is the point.

**Escalation done well.** Escalating isn't tattling. It's asking someone with more authority, information or resources to make a call you can't make yourself. Escalate when you lack one of those three, not when the conversation is just uncomfortable. The shape is facts, options, recommendation, deadline: what's happening (no adjectives about people), what you've tried, two or three options with their cost, what you'd do, and when you need the call and why. "I need a decision between A and B by the 14th; after that we miss the release window. I recommend A." Tell the other party before you send it, ideally with the same text. Once the call is made, execute it and don't relitigate.

**Saying no.** No, plus why, plus what you'd say yes to. A no without a why reads as preference; a no without an alternative reads as obstruction. "We can't take the export feature this quarter. It would push the billing migration past the contract deadline. I'd say yes to a CSV workaround in two weeks, or to revisiting in Q3 once billing ships." The conditional yes ("yes, if we drop X or move the date") hands the trade-off back to the person who owns the priority.

**Write for the reader, not for this chat.** Stakeholder-facing artifacts keep the directness and the clarity but lose the casual phrasing and any profanity. The coaching voice is for our conversation, not your VP's inbox.

While drafting, flag gaps without blocking: *"This asks for budget but doesn't say what happens if they say no. Add the cost of waiting, or is leaving it out deliberate?"*

## Red flags while it takes shape

The ask sits below the fold, or there isn't one. Openers like "just a quick update" or "touching base". Several asks competing. Vague numbers, or numbers with no baseline. A decision request with no deadline. Written for the wrong reader: implementation detail for an exec, strategy abstractions for an engineer. Passive voice hiding bad news ("some items were not completed"). An escalation with adjectives about people in it. A "no" that is only a no. A decision record with one option and an empty risks section. When one shows up: name it, ask one question, suggest the fix. Don't silently fix it, or the user never learns to see it.

## Before calling it done

- **Two-minute skeptical-reader test:** "Read this as [reader], 30 seconds between meetings. What do they think you're asking? What do they push back on first?" If the answer to the first question isn't your one sentence, rewrite the top.
- **One-pagers:** quick check against the red flags. Offer the full scored evaluation in [criteria-one-pager](references/criteria-one-pager.md) before an exec review or if they want it. If the `artifact-reviewer` subagent is available, offer it, since fresh eyes catch what the author can't. Discuss its findings; don't just paste them.
- **Named reader with skin in the game:** suggest the `politics-coach` skill to simulate how that person will react before it goes out.
- **Decisions with a stated confidence:** offer to log the bet with a reopen trigger (forecast log or `3-Work/[initiative]/decisions.md`).

## Org reality

- **The exec who only reads the first line.** Fine. Write for that. The first line carries the ask and the deadline; everything else is for their chief of staff or for later. If they reply with a question you answered in paragraph three, don't point that out. Move that answer up next time.
- **Status updates nobody reads.** Usually because they're long and ask for nothing. Send fewer, and make each one decision-oriented: one thing you need, one risk they should know about, one thing that changed. If nobody notices you skipped a week, that's data too.
- **Escalation is a career risk here.** Some orgs quietly punish people who escalate. Then pre-wire with your own manager first ("I'm thinking of raising this, sanity check?"), frame it as a decision request rather than a problem report, and escalate jointly with the other party: "We disagree and need a tiebreak." A joint escalation is almost impossible to read as tattling.
- **Saying no to someone more senior.** Often you're not really saying no, you're surfacing the trade-off and letting them own it. Ask what's driving it first, since they may have context you don't. Then: "Happy to. That moves billing to May. Do you want to make that call, or should I?" If they still say yes, commit, and write the trade-off down in one line so nobody is surprised in May.

## References

- [references/one-pager.md](references/one-pager.md) — universal structure, decision and product one-pagers, audience tuning
- [references/criteria-one-pager.md](references/criteria-one-pager.md) — red/green flags, weighted dimensions, antipatterns, rewrites
- [references/updates.md](references/updates.md) — status update, sprint summary, newsletter
- [references/agendas.md](references/agendas.md) — should this be a meeting, decision-first agenda, stakeholder meeting templates
- [references/escalation-saying-no.md](references/escalation-saying-no.md) — when to escalate, SIOR template, saying-no scripts by request type
- [references/decision-records.md](references/decision-records.md) — lightweight decision record, ADR, DR vs. ADR, quality flags
