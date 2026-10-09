# One-Pager

A one-pager exists to get a decision or a commitment from someone busy. It's not the PRD and it's not a status report. If you can't name the decision it drives, you're not ready to write it. Ask: "What's blocking you? What would unblock you? That's your decision." If that still doesn't land, the problem needs more thinking first.

It doesn't have to be literally one page. If 1.5 pages is what it takes to be clear, fine. Clarity beats squeezing everything into 9pt font.

## Universal structure

Every type follows the same spine, in this order:

1. **Headline** — the claim or the ask, not a topic label ("Approve MFA for Q2", not "MFA")
2. **TL;DR** — 2–3 sentences: problem, proposal, why it matters, the ask. Write it last, put it first
3. **Problem** — why this matters, with evidence
4. **Proposal** — what you want to do, and what you're explicitly not doing
5. **Why now** — what changes if we wait
6. **Impact** — metric from baseline to target, plus your confidence and what it's based on
7. **Approach** — phases, people, dependencies; just enough to show it's feasible
8. **Trade-offs and risks** — what gets deprioritized, what could go wrong, alternatives rejected
9. **Ask** — the specific decision, by when, and what happens next if it's yes

## Decision one-pager (the one you'll use most)

```markdown
# DECISION NEEDED: [specific title, e.g. "Delay EU launch 4 weeks or ship without SSO?"]

**TL;DR:** [What decision, why now, what you recommend. 2–3 sentences.]
**Decision owner:** [name]   **Needed by:** [date] because [consequence of delay]

## Options
- **A: [name]** — [one line]. Pros: [ ]. Cons: [ ]. Who's affected: [ ]
- **B: [name]** — [one line]. Pros: [ ]. Cons: [ ]. Who's affected: [ ]
- (Optional C, including "do nothing" if it's real)

## Context
[2–3 sentences of current state. Just enough for someone who wasn't in the room.]

## Recommendation
[Option X], because [the deciding factor]. What we give up: [ ].

## What I need from you
☐ Approve [option]   ☐ Need more information on [ ]   ☐ Let's discuss (15 min)
```

## Product one-pager (proposing a new bet)

```markdown
# [Feature]: [headline with the outcome, e.g. "MFA to unblock $500K in enterprise deals"]

**TL;DR:** [problem, proposal, impact, ask]

**Problem:** [customer pain + business impact, quantified] · Evidence: [deals, tickets, interviews; name the tier]
**Proposal:** [1–2 sentences] · Out of scope: [ ] because [ ]
**Why now:** [deal deadline, competitor move, strategy window]
**Impact:** [metric]: [baseline] → [target] by [date] · Confidence: [H/M/L], based on [ ]
**Approach:** [phases + timeline] · Needs: [eng/design/other capacity] · Depends on: [ ]
**Trade-offs:** we'd deprioritize [ ]. Risks: [risk + mitigation]. Rejected: [alternative] because [ ]
**Ask:** [specific approval] by [date]. If yes, next: [first action]
```

Launch and strategy one-pagers follow the same spine. A launch one-pager adds team responsibilities, a dated timeline and a launch checklist; a strategy one-pager swaps "proposal" for priorities and an explicit "what we're not doing" list. For recurring project status, use the status update in [updates](updates.md) instead.

## Tune for the reader

- **Execs** — business case and the recommendation first; decision criteria explicit. Cut the implementation detail: "ML scoring auto-prioritizes alerts; expected 83% less triage time" beats a paragraph on model architecture.
- **Leadership peers** — strategic fit and the trade-offs, stated plainly. They'll look for what you're not saying.
- **Cross-functional teams** — what changes for their work, dependencies, timeline, what you need from them.

## Writing rules that matter

Short paragraphs (3–4 sentences max). 3–5 bullets per section. Define every acronym once. A simple chart beats a table, and a table beats a paragraph of numbers. Don't assume prior context, and don't include everything either: that's what the appendix link is for.

## Before and after sending

Test it on one person from the target audience before it goes wide; ask them what they think you're asking for. After sending, track whether the decision was actually made and which questions came back. Recurring questions tell you what to move up next time.
