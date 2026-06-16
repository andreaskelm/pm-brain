<!-- TEST SPECIMEN — synthetic input for rubric regression only. Not a real roadmap. -->

# Product Roadmap — Good specimen (rubric regression)

**Team:** Mid-market onboarding | **Horizon:** Q3–Q4 | **Audience:** VP Product, cross-functional leads

## NOW (Q3) — High confidence

### Reduce time-to-first-value for new admin accounts
**Problem:** New ops admins take 14 days on average to invite their first teammate; 68% stall before completing setup. This delays expansion revenue and increases early churn.
**Outcome:** Median days from signup to first successful invite drops from 14 → 7 by end of Q3.
**Success metrics:** Median days to first invite (Mixpanel funnel); % accounts completing setup checklist within 7 days (32% → 55%).
**Scope:** Admin onboarding flow, checklist UX, invite nudges. **Non-scope:** Enterprise SSO, mobile admin app.
**Dependencies:** Analytics team to expose `admin_invite_sent` event by June 15 (delay pushes measurement 2 weeks). Design review with CS by July 1.

## NEXT (Q4) — Medium confidence

### Cut weekly compliance review time without adding headcount
**Problem:** Ops teams spend ~45 min/week manually scanning for changes across tools before weekly reviews.
**Outcome:** Median weekly review session duration falls from 45 min → 20 min.
**Success metrics:** Session duration telemetry; % items actioned within 48h (40% → 60%).
**Dependencies:** Pilot data from 20 accounts (CS) by Oct 1; legal sign-off on digest content format by Sept 15.

## LATER — Low confidence

### Proactive compliance alerts for regulated industries
**Problem:** Regulated customers miss material changes until audit prep, causing rework.
**Outcome:** Reduce audit-prep rework hours per account (baseline TBD after discovery).
**Note:** Requires discovery in Q4 before commitment.

**Strategic alignment:** Supports company goal to grow mid-market NRR through faster time-to-value.
