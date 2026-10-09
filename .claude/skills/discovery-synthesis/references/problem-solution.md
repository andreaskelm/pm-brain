# Problem–solution space, Double Diamond, OST

Separate **problem understanding** from **solution creation**. Exploration is not indecision—it's insurance against building the wrong thing.

## Two spaces

| Problem space | Solution space |
|---------------|----------------|
| Needs, pains, jobs, constraints | How we might address opportunities |
| Discover → Define (Diamond 1) | Develop → Deliver (Diamond 2) |

## Double Diamond (focused sprint, ~6–12 weeks)

1. **Discover (diverge):** 8–15 interviews, data, journey map, themes—no solution pitch.
2. **Define (converge):** problem statement, success metrics, 10–15 HMW questions, pick focus opportunity.
3. **Develop (diverge):** 20+ ideas, 3–5 concepts, assumptions per concept.
4. **Deliver (converge):** prototype tests, RAT, MVP, measure against Define metrics.

Timebox phases; 70% confidence to move is often enough. Cycle back when learning demands it.

**Artifact:** initiative exploration doc or `3-Work/[initiative]/research/` phase log.

## Opportunity Solution Tree (continuous)

Living structure (Teresa Torres):

```
Desired outcome (measurable)
├── Opportunity (customer need, their words)
│   ├── Solution A, B, C (3+ per opportunity)
│   │   └── Experiment (tests riskiest assumption)
```

**Rules:**

- Outcome = metric you can influence—not a ship list.
- Opportunities from **customer interviews** primarily; need-based, not "better UI."
- **3+ diverse solutions** per opportunity before committing—"what else?"
- Experiments on **riskiest** assumptions first ([validation](validation.md)).

**Weekly rhythm (ideal):** interviews → snapshot → synthesis update → adjust tree → plan tests.

**Tree health:** recent interviews, multiple opportunities, parallel solutions, active experiments, evidence links. **Unhealthy:** single solution, no interviews, stale tree.

## Supporting moves

- **HMW:** "How might we [action] so that [benefit]?" — solution-neutral, ideation fuel.
- **Five whys:** symptoms → root cause before Define.
- **JTBD:** frame opportunities as jobs ([jtbd](jtbd.md)).

## Combining DD + OST

OST = continuous map; Double Diamond = deep sprint on one branch. Sprint outputs update the tree; tree supplies sprint focus.

## Good vs bad framing

| Good problem/opportunity | Bad (solution disguised) |
|--------------------------|---------------------------|
| New users don't reach first value in session | Add onboarding tutorial |
| Checkout abandonment when shipping cost unclear | Redesign checkout |
| HMW help users see value in under 5 minutes | Build recommendation engine |

## Stakeholder lines

- "No time to explore" → cost of wrong build vs 2–4 weeks Discover.
- "We already know the solution" → treat as one option; generate two more.
- "VP's feature" → what opportunity does it serve; what else addresses that opportunity?

## Credits

Double Diamond — UK Design Council. Opportunity Solution Tree — Teresa Torres.
