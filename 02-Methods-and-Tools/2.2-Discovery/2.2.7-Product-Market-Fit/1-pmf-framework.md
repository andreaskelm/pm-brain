# Product-Market Fit Framework

## Goal
Assess product-market fit status and determine when to scale vs. iterate. Product-market fit is an ongoing state that requires continuous validation, not a one-time achievement.

> **Before using this framework:** Braindump first! What does your product sense tell you? Are you pushing a boulder uphill or chasing one downhill? What would make you say "we obviously have PMF" or "we obviously don't have PMF"? Then use this framework to structure your assessment.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `/assessments/pmf/` or initiative folder
- **Filename:** `pmf-assessment-[YYYY-MM-DD].md`

## When to Use

**Use for:**
- Validating early product hypotheses
- Deciding when to scale vs. iterate
- Assessing readiness for new markets
- Determining investment priorities

**Don't use when:**
- Very early concept stage (before MVP)
- Product is enterprise with 2-3 customers only
- PMF obviously exists (scaling phase)

## Core Signals

### You DON'T Have PMF When
- Customers aren't quite getting value
- Word of mouth isn't spreading
- Usage only grows when you advertise
- Press reviews are lukewarm
- Sales cycles take too long
- Most deals never close
- You're constantly explaining why people need it

### You HAVE PMF When
- Customers buying as fast as you can make it
- Usage growing as fast as you can add servers
- Money piling up in company checking account
- Hiring sales/support as fast as you can
- Reporters calling you (not vice versa)
- Customers become your salespeople
- Product is used even when broken

## Process

1. **Run PMF Survey:** Use the standardized survey question with qualified users
2. **Measure Retention:** Track cohort retention curves and daily active usage
3. **Assess Growth:** Measure organic growth and viral coefficient
4. **Evaluate Engagement:** Track DAU/MAU and power user patterns
5. **Check Monetization:** Calculate LTV/CAC and revenue retention
6. **Gather Qualitative Signals:** Assess customer feedback and behavior patterns
7. **Determine Status:** Classify as No PMF, Weak PMF, Strong PMF, or Lost PMF
8. **Take Action:** Scale if strong, iterate if weak, pivot if none

## PMF Survey Method

**The Question:**
"How would you feel if you could no longer use [product]?"
- Very disappointed
- Somewhat disappointed
- Not disappointed (it really isn't that useful)

**Survey criteria:**
- Users who experienced core product
- Used at least twice
- Used in past 2 weeks
- 40-50 responses minimum

**Threshold:** ≥40% "very disappointed" = PMF signal

**Frequency:** Every 4-6 weeks pre-PMF; quarterly post-PMF

## Key Metrics

### Retention (Most Important)
- Cohort retention curves flattening (not decaying to zero)
- For daily products: 60-70% using 5+ days/week
- D30 retention: 60%+ is exceptional

### Growth
- >50% new users from organic channels
- Viral coefficient >1.0
- Growth continues when marketing stops

### Engagement
- DAU/MAU >20%
- Power users emerging naturally
- High frequency of use

### Monetization
- LTV/CAC ratio >3:1
- Customers willing to pay at sustainable prices
- Net revenue retention >100%

## Before vs. After PMF

### Before PMF (BPMF)

**Primary goal:** Find PMF at all costs

**Do:**
- Talk to users constantly (100+ conversations)
- Iterate rapidly (weekly cycles)
- Focus on retention over acquisition
- Measure everything about user behavior
- Do things that don't scale
- Pivot if retention curves decay to zero

**Don't:**
- Scale marketing/sales
- Hire beyond core team
- Build features for everyone
- Perfect operations
- Optimize efficiency
- Raise too much money

**Filter:** "Does this help us find PMF?"

### After PMF (APMF)

**Primary goal:** Scale efficiently while maintaining PMF

**Do:**
- Scale marketing and sales
- Hire to meet demand
- Standardize processes
- Build infrastructure
- Optimize unit economics
- Expand to adjacent markets

**Don't:**
- Assume PMF is permanent
- Stop talking to customers
- Dilute core value proposition
- Ignore early users
- Chase every opportunity

**Filter:** "Does this help us scale PMF?"

## Common Pitfalls

1. **Confusing funding/press with PMF**
   - Focus on retention, not vanity metrics
   - Check if growth continues without marketing

2. **Building for everyone**
   - Better to delight 10 than satisfy 100
   - Find your core power users first

3. **Premature scaling**
   - Don't scale broken models
   - Keep team small until PMF validated

4. **Ignoring retention**
   - Plot cohort curves by week
   - Fix retention before scaling acquisition

5. **Not talking to users**
   - 5-10 conversations per week minimum
   - Watch them use your product

6. **Treating PMF as binary**
   - PMF exists on spectrum
   - May have PMF in one segment only
   - Requires continuous validation

## Integration with Other Frameworks

**PMF + Roadmap:**
- Pre-PMF: Short-term, experimental, learning focus
- Post-PMF: Longer horizons, strategic features, scale focus

**PMF + OKRs:**
- Pre-PMF: Learning metrics, PMF survey score, retention
- Post-PMF: Growth metrics, revenue, market share

**PMF + MoSCoW:**
- Pre-PMF: Only must-haves that validate PMF
- Post-PMF: Normal prioritization across all categories

**PMF + Kano:**
- Post-PMF only: Use to understand feature types
- Pre-PMF: Focus only on must-haves proving core value

## Quality Checklist

- [ ] PMF survey run with qualified users (40+ responses)
- [ ] Retention curves plotted and analyzed
- [ ] Growth metrics tracked (organic %, viral coefficient)
- [ ] Engagement metrics measured (DAU/MAU, power users)
- [ ] Monetization metrics calculated (LTV/CAC, NRR)
- [ ] Qualitative signals assessed
- [ ] Status clearly classified (No/Weak/Strong/Lost PMF)
- [ ] Actions defined based on status
- [ ] Next assessment scheduled

## References

- PMF Template: `2-pmf-template.md`
- Strategy: `../../2.1-Strategy/README.md` (Strategic Foundations, Roadmap Framework, OKR Framework)
- Discovery: `../README.md` (Opportunity Assessment, Idea Validation)
