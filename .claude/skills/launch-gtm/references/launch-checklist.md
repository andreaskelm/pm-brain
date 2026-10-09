# Launch checklist

Use this as a working list, not a ceremony. Skip rows that don't apply; never skip the row that names your rollback owner or your success metric readout. Success definition should already live in the product spec from the **write-prd** skill: primary metric (baseline → target), success threshold, and guardrail. This checklist only adds *launch timing*, *owners*, and *comms* — it does not replace those numbers.

---

## Phase 1 — Pre-launch readiness

### Product & engineering

- [ ] Shippable scope frozen for this launch tier (beta vs GA); P0 list matches what comms will claim
- [ ] Feature flags / rollout controls documented; default state defined for each environment
- [ ] Rollback or mitigation path tested (not just written)
- [ ] Release notes draft matches actual behavior; known limitations listed honestly
- [ ] In-product copy, empty states, and onboarding aligned with external promise
- [ ] Performance and capacity sanity check for expected launch traffic (or explicit limits published)
- [ ] Security, privacy, compliance sign-off if the launch changes data handling, billing, or contracts

### Success metrics (tie to write-prd)

- [ ] Primary metric named — same wording as PRD Goals & Success Metrics
- [ ] Baseline captured *before* launch (or explicit plan to measure from day 0 with caveats)
- [ ] Target and threshold for "this launch worked" agreed with leadership
- [ ] Guardrail metric identified — what must not regress (latency, churn, support CSAT, etc.)
- [ ] Dashboard or query exists; owner who reads it on a fixed cadence
- [ ] Beta exit criteria written (if beta): what must be true to call GA

### Internal readiness

- [ ] Launch DRI named (one throat to choke for go/no-go)
- [ ] Runbook: deploy steps, flag flips, verification checklist, escalation tree
- [ ] Support playbook: top 5 user questions, troubleshooting, when to escalate to eng
- [ ] Support and success briefed *before* sales or marketing blast
- [ ] Internal FAQ: what's new, for whom, what's not included, where to send feedback
- [ ] Engineering on-call rotation confirmed for launch window

### Enablement (scale to launch type)

- [ ] **Sales-led:** demo environment stable; talk track; objection handling; pricing/packaging sheet; implementation expectations
- [ ] **Self-serve:** help center articles; short loom or walkthrough for CS; upgrade/migration path if replacing old flow
- [ ] **Partner/channel:** same as above, plus co-marketing rules if applicable

### Comms prep (drafts approved, not sent)

| Audience | Internal vs external | Typical channel | Owner | Approve by |
|---|---|---|---|---|
| Exec / leadership | Internal | Email or brief doc | | |
| Company all-hands | Internal | Slack / town hall | | |
| Customer success / support | Internal | Slack + doc | | |
| Sales | Internal | Enablement session + one-pager | | |
| Existing customers (affected) | External | Email, in-app | | |
| Prospects / market | External | Blog, social, paid | | |
| Developers / API consumers | External | Changelog, docs | | |

- [ ] Single sentence value prop per audience — no contradictions between rows
- [ ] "Say this / don't say this" for customer-facing teams
- [ ] Holding statement drafted if launch goes sideways (status page language, customer email skeleton)

For message craft and templates, use the **stakeholder-comms** skill; this table is the calendar and ownership layer.

---

## Phase 2 — Launch day

### Go / no-go (same day)

- [ ] P0 verification complete on production (or pilot cohort)
- [ ] Rollback owner reachable; comms owner reachable
- [ ] Metrics pipeline live — you can see guardrail within hours, not weeks
- [ ] No undeclared dependency (billing, legal, third-party API) blocking core flow

### Execution sequence (default order)

1. **Internal:** "It's live" — what shipped, for whom, link to FAQ, feedback channel, war-room channel
2. **Customer-facing:** segmented sends (affected users first, then broader base)
3. **Market:** only after support confirms stable and P0 paths work

### Launch day operations

- [ ] War room or standing check-in times (even 15 minutes) for first 24–48 hours
- [ ] Monitor: errors, latency, signup/activation funnel, support queue volume, social mentions
- [ ] Log incidents and user verbatim quotes — raw material for post-launch review
- [ ] Freeze non-critical changes unless rollback; hotfix path pre-agreed

### If something breaks

- [ ] Trigger defined: error rate, failed payments, data integrity, SLA breach
- [ ] Rollback or feature-off decision maker named
- [ ] Customer comms path: status update, email, in-app banner — owner assigned
- [ ] Internal comms before external correction when possible

---

## Phase 3 — Post-launch metrics

Read metrics in PRD order — primary first, guardrail second. Launch week is for learning velocity, not for declaring victory on day two.

### Cadence

| Window | Focus | Audience |
|---|---|---|
| Day 0–1 | Stability, guardrails, support load | DRI + eng + support |
| Day 2–7 | Activation, primary metric early signal | Product + leadership snapshot |
| Week 2–4 | Target vs baseline; cohort behavior | Decision on expand, iterate, or pause |
| Day 30+ | PRD target horizon (as defined in spec) | Retro + roadmap input |

### Checklist

- [ ] Primary metric vs baseline documented (even if "too early to tell" — say why)
- [ ] Guardrail checked; regressions investigated before scaling comms or rollout %
- [ ] Segment cuts: new vs existing, plan tier, geography — surprises often hide here
- [ ] Support tag analysis: top issues match known gaps or reveal new ones
- [ ] Rollout expansion criteria met (if phased): metrics + qualitative bar from beta exit

### Scale or stop

- [ ] **Expand:** increase % traffic, widen audience, turn on marketing spend — only if guardrail holds
- [ ] **Iterate:** fast follows prioritized from data + feedback, not from loudest stakeholder
- [ ] **Pause / roll back:** explicit decision recorded with reason and customer comms if needed

---

## Phase 4 — Feedback loop

Launch isn't over when the blog post goes out; it's over when you've decided what to do with what you learned.

### Intake

- [ ] Single feedback channel (form, Slack, tagged support queue) — avoid scattered DMs
- [ ] Triage rules: bug vs UX friction vs feature request vs education gap
- [ ] Weekly synthesis: themes, quotes, frequency — not a dump of every ticket

### Closing the loop

- [ ] Customers who reported blockers get a direct follow-up when fixed (even if "not planned")
- [ ] Internal retro scheduled within 2 weeks: what we assumed vs what happened
- [ ] PRD open questions updated; assumptions promoted or killed based on evidence
- [ ] Roadmap / prioritize input: one page — "launch taught us X, recommend Y next"

### Retro prompts (short)

- What did we promise that we didn't deliver?
- What broke that we didn't war-game?
- Which metric moved (or didn't) and what's the leading hypothesis?
- What would we do differently for the next launch tier?

### Handoff

- [ ] Launch doc archived with final metrics snapshot and decision record
- [ ] Ongoing owner for the product area — not the launch DRI forever
- [ ] If success threshold missed: written plan (iterate, pivot scope, or sunset) — no silent drift

---

## Quick reference: internal vs external comms

**Internal** builds confidence and coordination. It can name risks, slips, and P1 backlog. It goes to employees and GTM teams first.

**External** sets expectation and trust. It claims only what works today; it links to docs; it segments so you don't spam uninterested users.

Never let external copy run ahead of internal truth. If sales and support learn from the blog post, you launched backwards.
