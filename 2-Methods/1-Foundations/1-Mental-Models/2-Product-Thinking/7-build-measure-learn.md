# Build-Measure-Learn

## What It Is
The Lean Startup loop (Eric Ries): build the smallest thing that tests an assumption, measure what users actually do, learn whether to persevere, pivot, or stop. The unit of progress is **validated learning**, not shipped features.

## How to Think With It
Run the loop backwards when planning: **Learn → Measure → Build.** Start with the assumption you need to learn about, decide what evidence would change your mind, and only then decide the cheapest thing to build that produces that evidence. Most teams run it forwards — build first, then go looking for a metric that makes it look good.

The loop is only as fast as its slowest step. In most orgs that is not Build — it's Learn: nobody owns the decision that should follow the data, so the loop stalls after Measure.

## When to Apply
- Before committing engineering time to an untested assumption
- When a roadmap item is really a hypothesis dressed up as a commitment
- When the team ships steadily but nobody can say what they learned last quarter

## Org Reality
In a feature-factory org, "MVP" often means "version 1 with fewer features" rather than "smallest test of an assumption." You can't always fix that vocabulary. What you can do is privately name the assumption each item tests and the signal you'd watch — then report learning alongside delivery. That's the bridge between the loop and an org that only counts output.

Watch for **success theater**: the measure is picked after the build, the threshold is never written down, and every result counts as "learning." If you can't name in advance what result would make you stop, you're not running the loop.

## PM Example
A team wants to build a full reporting dashboard. Backwards loop: *Learn* — do managers actually act on weekly numbers? *Measure* — % of managers who open a weekly summary and click through to a team member. *Build* — a plain weekly email with three numbers and a link. If under 20% click through after four weeks, the dashboard is solving the wrong problem.

## Combines With
- [Outcome vs Output](1-outcome-vs-output.md) — the loop measures outcomes
- [Assumptions Framework](../1-Decision-Making/3-assumptions-framework.md) — pick which assumption the loop tests
- [Evidence Strength](../1-Decision-Making/7-evidence-strength.md) — what counts as "learned"
- [Idea Validation](../../../3-Discovery/5-Idea-Validation/README.md)

## Further Reading
- *The Lean Startup* — Eric Ries
