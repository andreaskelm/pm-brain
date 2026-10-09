# Roadmap Template

Now/Next/Later with confidence. Specificity drops as you move right: Now holds initiatives, Next holds outcome targets, Later holds themes. Keep it to what a stakeholder can read in five minutes.

```markdown
# [Product / Team] Roadmap

**This roadmap is not a commitment.** It reflects current priorities and will change as we learn from customers, the market, and our own results.

**Updated:** [date]   **Next review:** [date]   **Owner:** [name]
**This roadmap serves:** [the strategy goal or OKR, one line]

## NOW — [quarter, e.g. Q1] — High confidence (70–90%)

| Initiative (problem-first) | Target outcome | Success metric (baseline → target) | Confidence | Dependencies (what, from whom, by when) |
|---|---|---|---|---|
| | | | High | |

## NEXT — [half-year range, e.g. Q2–Q3] — Medium confidence (40–70%)

| Initiative | Target outcome | Success metric | Confidence | Key assumption we're betting on |
|---|---|---|---|---|
| | | | Medium | |

## LATER — [year or beyond] — Low confidence (10–40%)

| Theme | Strategic goal | Potential outcomes | Confidence | Research needed |
|---|---|---|---|---|
| | | | Low | |

## Not on this roadmap

| Request | From | Why not now | What would change our mind |
|---|---|---|---|
| | | | |

## What changed since last version
- [Item] moved [Next → Now / Now → Next / off the roadmap] because [evidence or decision]

## How to read this roadmap
- **High confidence (70–90%):** well-defined scope, clear requirements, few dependencies, capacity allocated.
- **Medium confidence (40–70%):** direction is clear, scope still uncertain, dependencies manageable.
- **Low confidence (10–40%):** exploring; high uncertainty, research needed before we commit to anything.
- **Now** is 0–3 months with concrete deliverables. **Next** is 3–9 months with outcome targets. **Later** is 9–18+ months with strategic direction only. No specific dates beyond Now.
```

## Examples

**Now**

| Initiative | Target outcome | Success metric | Confidence | Dependencies |
|---|---|---|---|---|
| New accounts drop off at signup step 2 | More new accounts reach activation | Signup → activation conversion +20%; step-2 drop-off −15% | High | Design for the revised flow by mid-Jan; analytics events for step 2 live before launch |
| Finance reconciles invoices by hand every day | Fewer billing errors, less finance workload | 95% of invoices matched automatically; 2 hours/day back for the finance team | High | Billing system API access from Finance Eng by end of Jan; sign-off from the Finance lead |

**Next**

| Initiative | Target outcome | Success metric | Confidence | Key assumption |
|---|---|---|---|---|
| CSMs find out about at-risk accounts too late | CSMs act on risk before renewal | Surprise churn −40%; proactive outreach +25% | Medium | Usage, NPS and ticket volume reliably predict churn |
| Common support tickets take too long to resolve | Faster resolution for repeat issues | Median resolution time −30%; support CSAT up | Medium | Most repeat issues can be solved with standard flows and macros |

**Later**

| Theme | Strategic goal | Potential outcomes | Confidence | Research needed |
|---|---|---|---|---|
| Users never find features they'd pay for | Help users find and adopt underused features | Higher feature adoption, expansion revenue, fewer "how do I" tickets | Low | Research on discovery pain points; experiments with in-app guidance |
| Pricing doesn't track the value customers get | Align pricing with usage and value | New revenue streams, less pricing friction, better retention in key segments | Low | Willingness-to-pay study; billing and usage analysis; plan experiments |

## Writing the cells

- **Initiative:** problem or action, not a project label. "Improve onboarding for new teams", not "Onboarding project".
- **Outcome:** business value. "Reduce onboarding time by 20%", not "Make onboarding nicer".
- **Metric:** measurable, not binary. "Weekly active teams +15%", not "Better engagement" and not "Shipped".

## Variants

- **Outcome-led:** one block per outcome, initiatives listed under it. "Reduce enterprise onboarding time by 50%" → streamline signup, automated provisioning, self-service configuration.
- **Theme-based:** replace the Now/Next initiatives with themes ("Enterprise security & compliance") and keep the initiative list in a backlog underneath.
- **Scenario-based:** 2–3 versions keyed to the external factor. Market grows → expansion work; market contracts → retention work; regulation lands → compliance work. State which scenario you're currently planning against.
- **Rolling:** no quarterly reset. Completed items leave, new ones enter Next, items move to Now when confidence rises. Always shows the next 3, 6 and 12 months.
