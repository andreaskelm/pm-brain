# Experimentation Criteria

Flags-only checklist for experiment design and readouts. Name the flag, ask one question, suggest the fix.

## Red flags

- **No clear decision** — running a test without knowing what ship/kill/pivot means
- **Hypothesis missing or solution-only** — describes UI change, not expected user behaviour or metric move
- **No primary metric** — multiple "success" metrics with no pre-declared winner
- **Primary metric too far from outcome** — optimizes clicks or vanity while business risk sits elsewhere
- **No baseline or MDE** — can't say what lift would matter or how long to run
- **Underpowered timeline ignored** — planned duration obviously too short for stated MDE
- **No guardrails** — revenue or engagement chase with no pause/stop rules on harm
- **Dirty assignment** — cross-device, partial exposure, or non-random cohorts without acknowledgment
- **Peeking without plan** — daily checks with optional stopping but classical thresholds
- **Post-hoc segment fishing** — "it won for power users" without pre-registration
- **Ship decision pre-made** — experiment labelled as validation after the fact
- **Inconclusive hand-waving** — no rule for extend, revert, or qualitative follow-up

## Green flags

- One-sentence hypothesis with mechanism and segment
- Single primary metric with definition, baseline, and minimum effect you'd act on
- Guardrails with pause vs stop thresholds
- Sample/duration sanity-checked with data partner or explicit assumptions
- Clean assignment, flag ownership, and tested rollback
- Decision criteria (ship/kill/pivot) written before launch
- Peeking policy agreed or fixed horizon stated
- Operational log for ramps, incidents, and external events
- Readout ties practical significance to the decision, not just p-values
