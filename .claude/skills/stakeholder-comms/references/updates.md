# Updates: Status, Sprint Summary, Newsletter

Three recurring formats, one rule: an update earns its place by telling the reader what changed, what it means for them, and whether they need to do anything. A list of activity does none of that. Factual beats performative. Readers who are paying attention can tell spin from straight talk, and one honest line about what slipped builds more trust than a flawless summary that papers over it.

| Format | Reader | Cadence | Length |
|---|---|---|---|
| Status update | Exec, steering group, sponsor | Weekly to monthly, or on request | Half a page |
| Sprint summary | Delivery leads, senior stakeholders, and the team | Every sprint transition, within 24h | Readable in 90 seconds |
| Newsletter | Broad mixed audience across functions | Monthly | Under one page |

## Status update

Lead with the call you need, then the color. If there's no decision needed, say so in the first line so people can stop reading guilt-free.

```markdown
# [Project] status — [date]   Overall: 🟢 on track / 🟡 at risk / 🔴 off track

**Bottom line:** [one sentence: where we are and what it means]
**Decision needed:** [specific decision] by [date] (or "None this period.")

**Changed since last update:** [the 1–3 things that actually moved, as outcomes]
**Risks:** [risk] → impact: [ ] → what we're doing: [ ]
**Timeline:** [on schedule / X weeks behind, because ...]   **Budget:** [on / X% over]
**Next:** [milestone] by [date], owner [name]
```

Keep RAG honest. A project that's been 🟡 for six weeks is 🔴 with good PR. If the status changed, say why in one line.

## Sprint summary

An async brief sent at every sprint transition. It's not a sprint review: the review is a live meeting with demos and feedback, the summary travels without you. It can complement the review, not replace it.

- **Outcomes, not tickets.** "Cut month-end confirmation steps from 7 to 3" means something; "Completed US-1234" doesn't.
- **The board is the detail layer.** Paste a screenshot of the actual board, not a curated view. The prose covers the goal and the key outcomes.
- **Expected, not promised.** "Aiming to have done by the 24th", never "will deliver". Sprint planning is a forecast; set that mental model before something shifts.
- **Send it to the team too.** They should see how their work is described externally and feel safe saying "that's not quite right" before it becomes the record.

```markdown
Sprint [X] closed | Sprint [X+1] starting

**Last sprint: [goal as a sentence, not a label]**
We focused on [what and why it was the right focus].
Delivered:
- [Outcome: what a user or the team can now do, with a number if you have one]
- [Outcome]
[board screenshot]
Didn't land (only if material): [item]: [one honest line, e.g. "pushed to next sprint, the balance fix took longer than estimated"]

**New sprint: [goal as a sentence]**
We're focusing on [what and why now].
Aiming to have done by [date]:
- [Expected outcome tied to user or business value]
[board screenshot]

Questions, or anything that needs adjusting? Reply here or ping me.
```

Don't pad the delivered list with work finished before the sprint started, and don't use passive voice to distance yourself from what slipped. Skip the summary entirely if stakeholders already sit in daily standups.

## Newsletter

For broad audiences who don't follow the work week to week. Most product newsletters die because they're a reformatted changelog. Each section should answer "what" and "so what for you".

1. **Headline + one-line context** — what this edition is about and why now
2. **Focus 1: biggest outcome** — what changed, with a metric, and what it means for readers
3. **Focus 2: a change or strategic initiative** — the why, the trade-off, what it means for them, next steps
4. **Spotlight** — a customer story or team recognition, with a real quote
5. **Learning or look-ahead** — something you learned and what it implies
6. **In progress / next** — max 3 big rocks each, one line and a realistic timing each
7. **One specific call to action** — "Reply with your top onboarding complaint by the 20th", not "feedback welcome"

Tune the angle per reader: business impact for leadership, a little technical context for engineering, customer benefit for commercial teams. Five sections done well beat seven done thin. If you're struggling to fill one, drop it that month.
