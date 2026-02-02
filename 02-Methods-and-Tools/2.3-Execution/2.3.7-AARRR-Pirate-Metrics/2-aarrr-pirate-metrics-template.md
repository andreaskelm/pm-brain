# AARRR Metrics Templates

## Introduction

This document provides ready-to-use templates for tracking and optimizing AARRR (Pirate Metrics). Choose the template that fits your needs: Quick Funnel Health Check for rapid assessment, Full AARRR Dashboard for comprehensive tracking, or Stage-Specific Analysis for deep dives.

## How to Use These Templates

1. **Quick Funnel Health Check**: Use for weekly/bi-weekly rapid assessment (10-15 minutes)
2. **Full AARRR Dashboard**: Use for comprehensive monthly tracking
3. **Stage-Specific Analysis**: Use when optimizing individual stages

## How to Maintain

- **Weekly**: Quick Funnel Health Check
- **Monthly**: Update Full AARRR Dashboard
- **Quarterly**: Deep dive on weakest stage with Stage-Specific Analysis
- **As Needed**: Run A/B tests based on identified bottlenecks

---

## Quick Funnel Health Check

```markdown
# AARRR Health Check — [Date]

## Product Context
- Product: [Name]
- Stage: [Early growth / Growth / Scale]
- Focus this month: [Which stage you're optimizing]

## Funnel Overview (Past 30 Days)

| Stage | Metric | Current | Last Month | Status |
|-------|--------|---------|------------|--------|
| **Acquisition** | Total visitors | [N] | [N] | 🟢/🟡/🔴 |
| **Activation** | % activated | [X%] | [X%] | 🟢/🟡/🔴 |
| **Retention** | D30 retention | [X%] | [X%] | 🟢/🟡/🔴 |
| **Revenue** | LTV:CAC | [X:1] | [X:1] | 🟢/🟡/🔴 |
| **Referral** | K-factor | [X] | [X] | 🟢/🟡/🔴 |

## Biggest Bottleneck
[Which stage has worst conversion or biggest drop-off?]

## One Action This Week
[What's the #1 thing you're doing to improve the bottleneck?]

## Next Review: [Date]
```

---

## Full AARRR Dashboard

```markdown
# AARRR Dashboard — [Month/Quarter]

## Product Context
- Product: [Name]
- Period: [Date range]
- Total users: [N]
- New users this period: [N]

---

## 📊 Acquisition

**How users find us**

### Key Metrics

| Channel | Visitors | Sign-ups | CPA | Quality Score* |
|---------|----------|----------|-----|----------------|
| Organic Search | [N] | [N] | $[X] | 🟢/🟡/🔴 |
| Paid Search | [N] | [N] | $[X] | 🟢/🟡/🔴 |
| Social Media | [N] | [N] | $[X] | 🟢/🟡/🔴 |
| Referral | [N] | [N] | $[X] | 🟢/🟡/🔴 |
| Direct | [N] | [N] | $[X] | 🟢/🟡/🔴 |
| **Total** | **[N]** | **[N]** | **$[X]** | |

*Quality score based on activation + retention rates

### Analysis

**Best performing channel:** [Channel name]
- Why: [Low CPA, high quality, etc.]

**Worst performing channel:** [Channel name]
- Issue: [High CPA, poor quality, etc.]
- Action: [Pause, optimize, or iterate]

**Acquisition → Activation conversion:** [X%]
- Target: >30-40%
- Status: 🟢/🟡/🔴

### Actions
- [ ] [Action 1 with owner]
- [ ] [Action 2 with owner]

---

## ⚡ Activation

**Users experiencing value**

### Activation Definition
**Our activation milestone:** [e.g., "User completes onboarding + creates first project"]

### Key Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Activation rate | [X%] | >40% | 🟢/🟡/🔴 |
| Time to activation | [X hours/days] | [Target] | 🟢/🟡/🔴 |
| Onboarding completion | [X%] | >70% | 🟢/🟡/🔴 |
| Users reaching "aha moment" | [X%] | [Target] | 🟢/🟡/🔴 |

### Activation by Channel

| Channel | Activation Rate | Notes |
|---------|----------------|-------|
| Organic | [X%] | [Insight] |
| Paid | [X%] | [Insight] |
| Referral | [X%] | [Insight] |

### Drop-off Analysis

| Step | % Completed | Drop-off |
|------|-------------|----------|
| Sign-up | 100% | - |
| Email verification | [X%] | [X%] |
| Profile setup | [X%] | [X%] |
| First action (activation) | [X%] | [X%] |

**Biggest drop-off:** [Which step] ([X%] drop)

### Analysis

**What's working:**
- [Insight 1]

**What's not working:**
- [Insight 1]

**Activation → Retention conversion:** [X%]

### Actions
- [ ] [Action 1 with owner]
- [ ] [Action 2 with owner]

---

## 🔄 Retention

**Users coming back**

### Key Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| D1 retention | [X%] | >40% | 🟢/🟡/🔴 |
| D7 retention | [X%] | >25% | 🟢/🟡/🔴 |
| D30 retention | [X%] | >20% | 🟢/🟡/🔴 |
| DAU/MAU ratio | [X%] | >20% | 🟢/🟡/🔴 |
| Monthly churn | [X%] | <5% | 🟢/🟡/🔴 |

### Cohort Retention

| Cohort | D1 | D7 | D30 | D90 | Curve Status |
|--------|----|----|-----|-----|--------------|
| [Month 1] | [X%] | [X%] | [X%] | [X%] | 🟢/🟡/🔴 |
| [Month 2] | [X%] | [X%] | [X%] | [X%] | 🟢/🟡/🔴 |
| [Month 3] | [X%] | [X%] | [X%] | - | 🟢/🟡/🔴 |

**Retention curve:** [ ] Flattening 🟢 [ ] Slowing decay 🟡 [ ] Decaying to zero 🔴

### Analysis

**Why users stick around:**
- [Reason 1 from user research]
- [Reason 2]

**Why users churn:**
- [Reason 1 from churn surveys]
- [Reason 2]

**Power user profile:** [What makes them different?]

### Actions
- [ ] [Action 1 with owner]
- [ ] [Action 2 with owner]

---

## 💰 Revenue

**Monetizing users**

### Key Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Conversion rate (free→paid) | [X%] | [Y%] | 🟢/🟡/🔴 |
| ARPU | $[X] | $[Y] | 🟢/🟡/🔴 |
| LTV | $[X] | $[Y] | 🟢/🟡/🔴 |
| CAC | $[X] | $[Y] | 🟢/🟡/🔴 |
| LTV:CAC ratio | [X:1] | >3:1 | 🟢/🟡/🔴 |
| MRR | $[X] | $[Y] | 🟢/🟡/🔴 |
| Revenue churn | [X%] | <5% | 🟢/🟡/🔴 |

### Revenue by Plan

| Plan | Users | ARPU | Revenue | % Total |
|------|-------|------|---------|---------|
| Free | [N] | $0 | $0 | - |
| Basic | [N] | $[X] | $[X] | [X%] |
| Pro | [N] | $[X] | $[X] | [X%] |
| Enterprise | [N] | $[X] | $[X] | [X%] |

### Conversion Funnel

| Stage | Users | Conversion |
|-------|-------|------------|
| Active free users | [N] | 100% |
| Viewed pricing | [N] | [X%] |
| Started checkout | [N] | [X%] |
| Completed payment | [N] | [X%] |

**Biggest drop-off:** [Which step]

### Analysis

**What drives upgrades:**
- [Reason 1]
- [Reason 2]

**What prevents upgrades:**
- [Objection 1]
- [Objection 2]

### Actions
- [ ] [Action 1 with owner]
- [ ] [Action 2 with owner]

---

## 🔗 Referral

**Users recommending us**

### Key Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Referral rate (% users who refer) | [X%] | [Y%] | 🟢/🟡/🔴 |
| Referrals per user | [X] | [Y] | 🟢/🟡/🔴 |
| K-factor (viral coefficient) | [X] | >0.5 | 🟢/🟡/🔴 |
| Referred user activation rate | [X%] | [Y%] | 🟢/🟡/🔴 |
| Referral cycle time | [X days] | [Y days] | 🟢/🟡/🔴 |

### Referral Program Performance

| Source | Referrals | Activated | Conversion Rate |
|--------|-----------|-----------|-----------------|
| In-app prompt | [N] | [N] | [X%] |
| Email campaign | [N] | [N] | [X%] |
| Incentive program | [N] | [N] | [X%] |
| Organic sharing | [N] | [N] | [X%] |

### Analysis

**What drives referrals:**
- [Insight 1]
- [Insight 2]

**Referral quality:** [Are referred users better than average?]

**K-factor interpretation:**
- K = [X]
- [ ] K > 1.0: Viral growth (each user brings >1 new user)
- [ ] K < 1.0: Need paid acquisition to supplement

### Actions
- [ ] [Action 1 with owner]
- [ ] [Action 2 with owner]

---

## 🎯 Overall Funnel Health

### Conversion Between Stages

| From → To | Conversion Rate | Benchmark | Status |
|-----------|----------------|-----------|--------|
| Acquisition → Activation | [X%] | >30% | 🟢/🟡/🔴 |
| Activation → Retention (D30) | [X%] | >50% | 🟢/🟡/🔴 |
| Retention → Revenue | [X%] | >10% | 🟢/🟡/🔴 |
| Revenue → Referral | [X%] | >20% | 🟢/🟡/🔴 |

### Biggest Bottleneck
**Stage with worst conversion:** [Stage name]
**Impact:** [How it affects overall growth]
**Root cause hypothesis:** [Your best guess]

### Top 3 Priorities

1. **[Stage]:** [Specific optimization]
   - Current: [X%]
   - Target: [Y%]
   - Timeline: [Deadline]
   - Owner: [Name]

2. **[Stage]:** [Specific optimization]
   - Current: [X%]
   - Target: [Y%]
   - Timeline: [Deadline]
   - Owner: [Name]

3. **[Stage]:** [Specific optimization]
   - Current: [X%]
   - Target: [Y%]
   - Timeline: [Deadline]
   - Owner: [Name]

## Next Review: [Date]
```

---

## Stage-Specific Deep Dive

```markdown
# [Stage] Deep Dive — [Date]

## Context
- Stage: [Acquisition / Activation / Retention / Revenue / Referral]
- Why this stage: [Why you're focusing here]
- Current metric: [X%]
- Target metric: [Y%]

## Current State Analysis

### Quantitative Data

[Key metrics specific to this stage - use relevant section from Full Dashboard]

### Qualitative Insights

**User interviews (past month):** [Number]

**Common themes:**
1. [Theme 1]
2. [Theme 2]
3. [Theme 3]

**User quotes:**
- "[Relevant user quote]"
- "[Relevant user quote]"

### Behavioral Data

**Session recordings reviewed:** [Number]
**Key observations:**
- [Observation 1]
- [Observation 2]

## Problem Hypothesis

**What we think is broken:**
[Your hypothesis about why this stage is underperforming]

**Evidence supporting hypothesis:**
1. [Evidence 1]
2. [Evidence 2]

## Proposed Solution

**What we'll change:**
[Specific change to test]

**Expected impact:**
- Metric will improve from [X%] to [Y%]

**How we'll measure:**
- Primary metric: [Metric name]
- Secondary metrics: [Other metrics to watch]
- Guardrail metrics: [Metrics that shouldn't get worse]

## Experiment Plan

**Experiment type:** [ ] A/B test [ ] Multivariate test [ ] Rollout

**Variants:**
- Control: [Current experience]
- Variant A: [Changed experience]
- (Variant B: [If multivariate])

**Sample size needed:** [N users per variant]
**Expected runtime:** [X days/weeks]
**Success criteria:** [What defines success]

## Results

[Fill in after experiment completes]

**Experiment duration:** [Start] to [End]
**Sample size:** [N users per variant]

**Results:**
| Variant | Primary Metric | Change | Statistical Significance |
|---------|---------------|--------|-------------------------|
| Control | [X%] | - | - |
| Variant A | [X%] | [+/-X%] | [p-value] |

**Decision:** [ ] Ship variant [ ] Iterate [ ] Abandon

**Learnings:**
- [Learning 1]
- [Learning 2]

**Next experiment:** [What to test next]
```

---

## References

- AARRR Framework: `1-aarrr-pirate-metrics-framework.md`
- Strategy: `../../2.1-Strategy/README.md` (Strategic Foundations, OKR Framework, Roadmap Framework, North Star)
- Discovery: `../../2.2-Discovery/README.md` (PMF Framework)
