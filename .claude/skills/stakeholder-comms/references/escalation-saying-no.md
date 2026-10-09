# Escalation and Saying No

Two sides of the same skill: making trade-offs explicit and putting the decision with the person who actually owns it.

## Escalation

**Escalate when you lack authority, information, or resources to resolve it. Not when it's just hard or uncomfortable.** Three questions, in order: Do I have the authority to decide this? Do I have enough information? Do I have the resources to execute? Three yeses means handle it yourself.

Before escalating, check you've done the groundwork: you understand the problem, you've talked to everyone involved, you've tried at least one fix yourself, and you can name the trade-offs. If not, that's the work, and escalating now will bounce straight back.

**SIOR: Situation, Impact, Options, Recommendation (plus the Request)**

```markdown
Subject: [DECISION NEEDED by date] [specific topic]

**Situation:** [2–3 sentences, facts only, no adjectives about people]
**What I've tried:** [action → outcome]
**Impact if unresolved:** [customer / business / timeline, specific]
**Options:**
1. [A]: [what it costs, who it affects]
2. [B]: [what it costs, who it affects]
**Recommendation:** [A], because [deciding factor].
**Request:** decision between A and B by [date], because [what happens after that date].
I'll communicate the outcome to [affected parties].
```

What changes by scenario:

- **Cross-team conflict** — present both positions fairly, in terms the other side would sign. Escalate when positions are valid but incompatible and it's hitting commitments, not over implementation details. Best done jointly: "We disagree and need a tiebreak."
- **Feasibility pushback** — engineering says it's impossible, the business says it's critical. Ask the eng manager or CTO for options, not a verdict, and state the trade-off space up front: phasing, reduced scope, a different approach, a later date.
- **Resources or budget** — commitment vs. what you have vs. the gap. Show the alternatives you considered (cut scope, move the date, drop other work) so the request isn't the only option on the table.
- **Priority conflict between two stakeholders** — lay out both requests side by side (what, why, deadline, effort) and what choosing each costs the other. Offer to deliver the decision to both, so the escalation doesn't look like you picking sides.

After escalating: follow up if there's no response in 24–48 hours, write down the decision, tell affected people, execute it, and don't relitigate.

## Saying no

"No" isn't rejection, it's prioritization, and prioritization is the job. The PMs who earn trust aren't the ones who say yes to everything, they're the ones who protect the roadmap and make trade-offs visible. Before you say no, check whether there's a yes you're missing: what's the real need behind the request?

**Formula:** acknowledge why it matters → name the constraint or trade-off → offer what you'd say yes to.

> "I can see why this matters for the Nordea renewal. Right now we're on billing migration because of the contract deadline in June; taking this on would push that by about four weeks. What I could do: a CSV export in two weeks as a workaround, or put the full version up for Q3 planning. Would either work?"

Scripts by request type:

- **Feature request** — not now, here's when: "Adding this means delaying [X] by [time]. What if we capture the requirements now and revisit after [X] ships?" Or not this, but this: offer a smaller version, a workaround with existing features, or a different solution to the same goal.
- **Conditional yes** — "We can do it if we drop [Y], or move the date to [Z], or get [extra person]. Which trade-off fits your priorities?"
- **Priority change** — ask what's driving the urgency first. Then show what slips: "Your item moves to Q3, [current priority] slips to Q4, which affects [who]. Worth it? If yes, I'll update everyone."
- **Scope creep** — "Adding this costs about [X weeks]. Options: extend the date, cut [other feature], or take it in the next phase. What matters more, the date or this?"
- **Borrowing your people** — show their actual load, then offer advisory hours, a different person, or delaying your own lower-priority work.
- **Meeting or analysis request** — offer async review, a teammate who can represent product, or a 15-minute follow-up.
- **Sales wants a feature to close a deal** — make the business case visible: deal value and probability, effort, what gets delayed, ongoing maintenance. Ask how many other customers need it. If it's truly strategic, pull in whoever owns that call.

**To someone more senior:** restate what you heard, name your concerns as trade-offs, ask what's driving it (they may know something you don't), give your recommendation, then commit: "If you still want to go this way, I'll make it happen and tell the affected teams what moves."

**Not now, with the door open:**

```markdown
**Status: not now.** Why: [tied to strategy, capacity or priority]
Revisit: [trigger or date] · What would change our mind: [e.g. 10+ customers asking; current priority ships]
Meanwhile: [workaround] · You'll hear from: [who, how]
```

**Common lines and answers:**

- "It'll only take five minutes." → "Five to discuss, or five to build? If it's really five, let's do it now. If it's a day, it goes through the backlog like everything else."
- "The competitor has it." → "Are we losing deals over it? How many, how much? Let's quantify before we decide."
- "Can we just…" → "Let's unpack 'just': full scope, who it's for, how we'd know it worked, who maintains it. 'Just' features rarely are."

After a no: log it in the backlog with the reason, follow up if the situation changes, and look after the relationship. Practice on low-stakes nos (optional meetings, nice-to-haves) before the big ones.
