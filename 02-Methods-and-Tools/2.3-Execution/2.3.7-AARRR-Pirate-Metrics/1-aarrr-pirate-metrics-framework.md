# AARRR (Pirate Metrics) Framework

## Goal
Measure and optimize product growth across five key stages: Acquisition, Activation, Retention, Revenue, and Referral. AARRR helps identify funnel bottlenecks and focus optimization efforts on metrics that drive sustainable growth.

> **Before using this framework:** Braindump first! Where are users dropping off most in your funnel? Which stage feels weakest? What would make you say "our funnel is obviously broken" or "our funnel is working well"? Then use this framework to structure your measurement.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `/metrics/aarrr/` or initiative folder
- **Filename:** `aarrr-dashboard-[YYYY-MM-DD].md`

## When to Use

**Use for:**
- Setting up growth analytics and measurement
- Identifying funnel bottlenecks and drop-off points
- Optimizing conversion at each stage systematically
- Growth strategy planning and resource allocation

**Don't use when:**
- Pre-MVP/pre-launch (no users to measure)
- Very early stage (focus on PMF first)
- Enterprise B2B with 2-3 customers (sample too small)

## The Five Stages

### A - Acquisition

**Definition:** How users discover your product

**Key Metrics:**
- Traffic by channel (organic, paid, referral, direct)
- Cost per acquisition (CPA) by channel
- Sign-ups / Registrations
- Quality score by channel (based on downstream conversion)

**Optimization strategies:**
- Identify highest-quality channels (not just volume)
- Reduce CAC through channel mix optimization
- A/B test landing pages and messaging
- Focus on channels where ICP hangs out

**Common mistake:** Optimizing for volume over quality

---

### A - Activation

**Definition:** Users experiencing value and taking meaningful first actions

**Key Metrics:**
- % users reaching activation milestone
- Time to first value
- Onboarding completion rate
- Feature adoption (key features used)
- Activation by acquisition channel

**Define your activation milestone:**
- SaaS: Completed setup + used core feature
- E-commerce: First purchase
- Social: First post/connection
- Content: Consumed X pieces of content

**Optimization strategies:**
- Streamline onboarding to activation
- Guide users to "aha moment" faster
- Remove friction in first-use experience
- Measure time to activation and reduce it

**Common mistake:** Confusing activation with sign-up; users who register and never return were never activated

---

### R - Retention

**Definition:** Users coming back and continuing to engage

**Key Metrics:**
- D1, D7, D30 retention rates by cohort
- Monthly/Weekly active users (MAU/WAU)
- DAU/MAU ratio
- Churn rate
- Cohort retention curves

**Retention benchmarks:**
- D1: 40%+ is good
- D30: 20%+ is good (varies by product)
- Retention curve should flatten, not decay to zero

**Optimization strategies:**
- Deliver repeatable value tied to core use case
- Reduce friction to re-engage (notifications, emails)
- Build habit loops and triggers
- Track why users churn and fix those issues

**Common mistake:** Focusing on acquisition before fixing retention

---

### R - Revenue

**Definition:** Monetizing your user base

**Key Metrics:**
- Conversion rate (free to paid)
- Average Revenue Per User (ARPU)
- Customer Lifetime Value (LTV)
- Monthly Recurring Revenue (MRR) / Annual Recurring Revenue (ARR)
- Revenue churn
- LTV:CAC ratio (target >3:1)

**Optimization strategies:**
- Optimize pricing and packaging
- Improve upgrade flows
- Reduce revenue churn
- Upsell/cross-sell to existing customers
- Time monetization to value delivered

**Common mistake:** Monetizing before proving value (activation/retention)

---

### R - Referral

**Definition:** Users recommending product to others

**Key Metrics:**
- Viral coefficient (K-factor)
- Referral rate (% users who refer)
- Referrals per user
- Conversion rate of referred users
- Cycle time (time from referral to new activation)

**Viral coefficient:**
- K > 1.0 = viral growth (each user brings >1 new user)
- K < 1.0 = need paid acquisition to supplement

**Optimization strategies:**
- Build referral directly into product experience
- Incentivize referrals (but don't over-incentivize)
- Make sharing easy and valuable
- Track and optimize referral conversion

**Common mistake:** Forced referral programs that feel spammy

## Process

1. **Map Your Funnel:** Define what each stage means for your product
2. **Identify Biggest Problem:** Don't start with Acquisition just because it's first
3. **Set Baseline Metrics:** Measure current state for each stage
4. **Focus and Optimize:** Spend 80% effort on refining existing features
5. **Monitor Interdependencies:** Recognize that metrics influence each other

## Key Ratios to Track

**Acquisition → Activation:**
- Target: >30-40% of visitors activate
- If low: onboarding/product-market fit issue

**Activation → Retention:**
- Target: Varies by product, aim for flat retention curve
- If low: product doesn't deliver ongoing value

**Retention → Revenue:**
- Target: >10-20% of retained users monetize
- If low: pricing or value proposition issue

**Revenue → Referral:**
- Target: K > 0.5 for healthy growth
- If low: product isn't remarkable enough

## Common Pitfalls

1. **Measuring vanity metrics**
   - Focus on actionable metrics tied to business outcomes
   - Track conversion rates, not just absolute numbers

2. **Optimizing stages out of order**
   - Fix retention before scaling acquisition
   - Don't pour users into a leaky bucket

3. **Tracking everything**
   - You can't track everything - focus on a few key indicators that matter most
   - Start with 1-2 metrics per stage

4. **Ignoring cohort analysis**
   - Track metrics by cohort (weekly/monthly)
   - Watch for changes over time

5. **Not segmenting by channel**
   - Different channels have different quality
   - Optimize for highest LTV:CAC channels

6. **Treating AARRR as strict sequence**
   - Unlike traditional funnels, stages don't have to be in precise order - referral can help activation, revenue can drive retention

## Integration with Other Frameworks

**AARRR + PMF:**
- Pre-PMF: Focus on activation and retention only
- Post-PMF: Optimize full funnel

**AARRR + Roadmap:**
- Use AARRR to identify which stages need product investment
- Prioritize features that improve weakest stages

**AARRR + OKRs:**
- Set OKRs targeting specific AARRR stages
- Example: "Improve D30 retention from 20% to 30%"

**AARRR + North Star Metric:**
- North Star should capture value across multiple AARRR stages
- AARRR breaks down how to improve North Star

## Quality Checklist

- [ ] Funnel mapped with clear definitions for each stage
- [ ] Baseline metrics established for all five stages
- [ ] Biggest bottleneck identified with data
- [ ] Metrics tracked by cohort and channel
- [ ] Conversion rates between stages calculated
- [ ] Key ratios monitored (Acquisition→Activation, etc.)
- [ ] Optimization plan focused on weakest stage
- [ ] Dashboards set up for regular review

## References

- AARRR Template: `2-aarrr-pirate-metrics-template.md`
- Product Strategy: `../../2.1-Strategy/2.1.1-Strategic-Foundations/README.md`
- PMF Framework: `../../2.2-Discovery/2.2.7-Product-Market-Fit/README.md`
- OKR Framework: `../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md`
- Roadmap Framework: `../../2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/README.md`
- North Star: `../../2.1-Strategy/2.1.2-Strategic-Execution/3-North-Star/README.md`
