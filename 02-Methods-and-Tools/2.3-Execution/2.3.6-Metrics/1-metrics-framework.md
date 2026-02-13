# Product Metrics Framework

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "metrics", "KPIs", "what should I measure", "success metrics", "how do I track progress", "product metrics"
- User is in: `execution_mode` (after braindump) or when user asks to define metrics
- Prerequisites: User has product/feature/initiative they want to measure
- User has: Some understanding of what outcomes matter (may need help articulating)

**How to introduce:**
- "You want to define metrics that drive action and learning. Let's use the Metrics Framework to distinguish meaningful metrics from vanity metrics."
- "Based on your thinking about [product/feature], let's structure your metrics using this framework to ensure you're measuring what actually matters."

**Common mistakes to avoid:**
- Don't suggest Metrics if user needs a single strategic metric (suggest North Star Framework instead)
- Don't create vanity metrics (focus on actionable, outcome-focused metrics)
- Don't suggest Metrics if user doesn't have clear outcomes (help them define outcomes first)
- Don't skip braindump - metrics frameworks organize measurement thinking, they don't create it
- Don't create too many metrics (focus on 3-5 key metrics)

**When NOT to use Metrics Framework:**
- User needs a single strategic alignment metric (use North Star Framework - one metric for alignment)
- User is defining strategy (use Strategic Foundations - metrics come after strategy)
- User is exploring opportunities (use Opportunity Assessment - metrics come after validation)
- User needs feature-level metrics for PRD (suggest Metrics section within PRD framework)

**Distinction from North Star:**
- **Metrics Framework:** Multiple metrics for different purposes (leading/lagging, input/output, feature/product level)
- **North Star Framework:** Single strategic metric that aligns the entire team (one metric for alignment)
- **When to use Metrics Framework:** Need multiple metrics, feature-level tracking, comprehensive measurement strategy
- **When to use North Star:** Need single strategic alignment metric, team alignment around one number

**Cross-reference:** Metrics often feed into OKRs (metrics → key results) and PRDs (metrics → success criteria). If user has defined metrics, they may be ready for OKRs or PRD.

---

## Overview

This framework helps product teams distinguish between meaningful metrics and misleading ones, ensuring you measure what actually drives your product and business forward. Metrics are NOT status symbols—they're strategic tools for decision-making.

## Step 0: Braindump & Think First (Critical!)

**Use prompts from:** [2-product-sense-prompts.md](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) → [Generic Step 0 (any framework)](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#generic-step-0-any-framework). Quick start: What outcomes? What metrics feel meaningful? What assumptions about what to measure? What biases might affect your metric choices? **See prompts file for full list.**

## Core Philosophy

### Metrics are NOT Magic

Good metrics should:

- **Drive action over appearance** - Make you do something, not just feel good
- **Predict outcomes over report history** - Look forward, not just backward
- **Connect work to results** - Show how daily efforts impact business goals
- **Enable learning over confirmation** - Challenge assumptions, don’t just validate them

### Understanding the Metric Spectrum

Metrics exist on several spectrums:

- **VANITY ←→ ACTIONABLE** - Impressive vs. Useful
- **LAGGING ←→ LEADING** - Results vs. Predictors
- **OUTPUT ←→ OUTCOME** - Activity vs. Impact
- **QUANTITATIVE ←→ QUALITATIVE** - Numbers vs. Stories

## Framework Structure

### 1. Header Section

Always include:

- **Disclaimer** - “Metrics reflect our current understanding and will evolve”
- **Metric tier** - Which level of metric is this?
- **Last reviewed date**
- **Review owner**

### 2. Metric Classification

**Vanity Metrics (Avoid These)**

- Look impressive but lack context
- Don’t inform strategy
- Can’t be acted upon
- Not reproducible

**Actionable Metrics (Focus Here)**

- Connected to business decisions
- Reproducible through specific actions
- Provide clear next steps
- Auditable and accessible

### 3. Metric Timing

**Leading Indicators (Predictive)**

- Predict future outcomes
- Teams can directly influence
- Short feedback loops (days/weeks)
- Enable course correction

**Lagging Indicators (Historical)**

- Report past results
- Validate strategy success
- Long feedback loops (months/quarters)
- Confirm business impact

### 4. Metric Purpose

**Health Metrics**

- Monitor system stability
- Track performance
- Ensure product quality

**Growth Metrics**

- Drive acquisition
- Increase engagement
- Measure retention

**Business Metrics**

- Revenue and profitability
- Market position
- Customer value

## Writing Guidelines

### Metric Names

- ✅ “Trial-to-paid conversion rate”
- ✅ “Weekly active users completing core action”
- ✅ “Time to first value realization”
- ❌ “Total users”
- ❌ “Page views”
- ❌ “Engagement”

### Metric Definitions

- ✅ “% of free trial users who upgrade to paid within 14 days”
- ✅ “Count of users who complete at least 3 tasks in a 7-day period”
- ❌ “Users who are engaged with the product”
- ❌ “People who like the feature”

### Why This Metric Matters

- ✅ “Predicts 6-month retention with 85% accuracy”
- ✅ “Moves 72 hours before revenue changes, enabling proactive intervention”
- ❌ “It’s what competitors track”
- ❌ “Leadership asked for it”

## Review Schedule

### Daily Check-ins (Health Metrics)

- System performance
- Error rates
- Critical user flows
- Immediate blockers

### Weekly Reviews (Leading Indicators)

- Progress against targets
- Trend identification
- Early warning signals
- Quick wins and blockers

### Monthly Deep-Dives (Lagging + Leading)

- Business metric review
- Cohort analysis
- Strategic adjustments
- Experiment results

### Quarterly Audits (Full Portfolio)

- Metric relevance check
- Sunset obsolete metrics
- Add new strategic metrics
- Validate measurement accuracy

### Annual Strategy Reviews

- Align metrics with strategy shifts
- Market positioning assessment
- Competitive landscape changes

## Stakeholder Communication

### For Leadership

- Focus on business and lagging metrics
- Show leading indicators that predict results
- Highlight strategic trade-offs and bets
- Connect metrics to revenue and growth

### For Product Teams

- Emphasize leading indicators they can influence
- Show how daily work moves metrics
- Provide context on why metrics matter
- Celebrate metric movement, not just targets

### For Engineering Teams

- Health and performance metrics
- Technical quality indicators
- Deployment and reliability metrics
- Clear correlation to user impact

### For Data Teams

- Measurement methodology
- Data quality and accuracy
- Instrumentation requirements
- Analysis and insights process

## Common Challenges and Solutions

### “Why aren’t we tracking [popular metric]?”

**Response pattern:**
“Let’s evaluate it. Can we act on this metric? Does it predict outcomes we care about? If we move this metric up, does our business definitely improve? What decision would this metric help us make?”

### “Our metrics look great but business results don’t”

**Response pattern:**
“This signals a vanity metric problem. Let’s audit: Are we measuring outputs or outcomes? Are these leading or lagging? What’s the connection between what we’re measuring and what we’re trying to achieve?”

### “We have too many metrics to track”

**Response pattern:**
“Quality over quantity. Let’s apply the 5-3-1 rule: 5 key metrics per team, 3 North Star inputs for the product, 1 North Star Metric company-wide. If a metric doesn’t drive decisions, cut it.”

### “This metric is gaming our behavior”

**Response pattern:**
“Good catch—this is Goodhart’s Law in action. When a measure becomes a target, it ceases to be a good measure. Let’s add counterbalance metrics or reframe this as an input to a more holistic outcome.”

## Best Practices

### Do’s

- Start with business goals, work backward to metrics
- Mix leading and lagging indicators
- Choose 3-5 key metrics per team (not 20)
- Make metrics accessible to everyone
- Review and refine metrics regularly
- Tell stories behind the numbers
- Use ratios over raw numbers (percentages, rates, averages)

### Don’ts

- Track metrics just because competitors do
- Rely solely on lagging indicators
- Create metrics without clear ownership
- Ignore qualitative data
- Set metrics and forget them
- Use cumulative charts for everything
- Track what’s easy vs. what matters

## Metrics for Metric Success

Track these to know if your metric framework is working:

- **Decision velocity** - Are decisions faster with clear metrics?
- **Strategic alignment** - Do metrics connect to business goals?
- **Team autonomy** - Can teams make local decisions with metric insights?
- **Learning rate** - How quickly do insights translate to action?
- **Metric coverage** - Do we have balanced leading/lagging indicators?

## Metric Quality Checklist

Before adopting any metric, validate it passes these tests:

- [ ] **Actionable Test** - Can we take specific actions to improve this metric?
- [ ] **Accessible Test** - Can everyone understand what this metric means?
- [ ] **Auditable Test** - Can we trace this metric back to raw data?
- [ ] **Aligned Test** - Does this connect to business goals?
- [ ] **Predictive Test** - Does this help us see what’s coming?
- [ ] **Comparative Test** - Can we benchmark this over time or against others?
- [ ] **Simple Test** - Can someone explain this in 30 seconds?

-----

# Product Metrics Template

## Disclaimer

This metrics framework reflects our current product strategy. Metrics will evolve as we learn what drives real outcomes vs. what just looks good.

**Updated on:** [Date]
**Next review:** [Date]
**Framework owner:** [Name/Role]

-----

## 🎯 Primary Business Goals

Before defining metrics, state what you’re trying to achieve:

1. **Business Goal 1:** [e.g., Grow revenue by 40% YoY]
1. **Business Goal 2:** [e.g., Improve gross retention to 95%]
1. **Business Goal 3:** [e.g., Expand into enterprise market]

-----

## 📊 Metric Hierarchy

### Tier 1: North Star Metric (Company-Level)

The one metric that best captures customer value and predicts sustainable growth.

|Element |Details |
|--------------------|--------------------------------|
|**Metric Name** |[Your North Star] |
|**Classification** |Leading / Lagging / Both |
|**Definition** |[Precise measurement method] |
|**Why It Matters** |[Connection to value and growth]|
|**Current Value** |[Baseline] |
|**Target** |[Goal] |
|**Review Frequency**|[Weekly/Monthly] |
|**Owner** |[Name/Team] |

**Example:**

|Element |Details |
|--------------------|---------------------------------------------------------------------------|
|**Metric Name** |Weekly Active Users (WAU) completing core action |
|**Classification** |Leading indicator |
|**Definition** |Count of users who complete at least one analysis in a 7-day rolling window|
|**Why It Matters** |Predicts 30-day retention (r²=0.87) and expansion revenue within 90 days |
|**Current Value** |42,500 WAU |
|**Target** |55,000 WAU by Q2 |
|**Review Frequency**|Weekly |
|**Owner** |Chief Product Officer |

-----

### Tier 2: Input Metrics (Product Team Level)

The 3-5 metrics that drive your North Star Metric.

#### Input Metric #1

|Element |Details |
|---------------------------|--------------------------|
|**Metric Name** |[Action-oriented name] |
|**Classification** |Leading / Lagging |
|**Definition** |[How you measure it] |
|**Type** |Vanity / Actionable |
|**Why It Matters** |[Connection to North Star]|
|**Current Value** |[Baseline] |
|**Target** |[Goal] |
|**Review Frequency** |[Cadence] |
|**Owner** |[Team/Person] |
|**Actions if Above Target**|[What we do] |
|**Actions if Below Target**|[What we do] |

**Example:**

|Element |Details |
|---------------------------|------------------------------------------------------------------------|
|**Metric Name** |New user activation rate |
|**Classification** |Leading indicator |
|**Definition** |% of new signups who complete setup and run first analysis within 7 days|
|**Type** |Actionable |
|**Why It Matters** |Activated users are 3.2x more likely to become WAU within 30 days |
|**Current Value** |42% |
|**Target** |55% |
|**Review Frequency** |Weekly |
|**Owner** |Growth Product Team |
|**Actions if Above Target**|Document what’s working; scale successful patterns |
|**Actions if Below Target**|Run onboarding experiments; improve time-to-value |

#### Input Metric #2

[Repeat structure]

#### Input Metric #3

[Repeat structure]

-----

### Tier 3: Feature/Initiative Metrics

Specific metrics for experiments, features, or initiatives.

|Initiative|Metric |Type |Target|Result |Learning |
|----------|--------|---------------|------|---------|-----------------|
|[Name] |[Metric]|Leading/Lagging|[Goal]|[Outcome]|[What we learned]|
| | | | | | |

**Example:**

|Initiative |Metric |Type |Target |Result |Learning |
|---------------------|----------------------------------------|-------|--------------------|----------------|-----------------------------------------------|
|Redesigned onboarding|Time to first analysis |Leading|< 5 min (from 8 min)|4.2 min achieved|Removing account setup step was key driver |
|Smart recommendations|% users discovering personalized content|Leading|50% (from 35%) |48% achieved |Algorithm accuracy mattered more than placement|
|Team collaboration |Analyses shared per user |Leading|2.5 (from 1.8) |2.1 achieved |Need better sharing triggers, not just features|

-----

## 🎨 Metric Classification Matrix

Map your metrics to understand portfolio balance:

### Vanity vs. Actionable

|Vanity Metrics (Eliminate)|Why It’s Vanity |Actionable Alternative |
|--------------------------|--------------------------------|---------------------------|
|Total registered users |Doesn’t show engagement or value|Weekly/Monthly Active Users|
|Page views |Doesn’t indicate value or goals |Task completion rate |
|Social media followers |No revenue correlation |Qualified leads from social|
|Total downloads |Doesn’t show actual usage |Daily/Weekly Active Users |
| | | |

### Leading vs. Lagging Balance

**Current Portfolio:**

- Leading Indicators: [Count/List]
- Lagging Indicators: [Count/List]
- **Ratio:** [X:Y] (Target: 70% leading, 30% lagging)

### Output vs. Outcome

|Output Metrics (Activity)|Better Outcome Alternative|
|-------------------------|--------------------------|
|Features shipped |User problems solved |
|Experiments run |Validated learnings |
|Stories completed |Customer value delivered |
| | |

-----

## 📈 Metric Relationships (Belief Tree)

Map how you believe metrics connect:

```
Business Goal: [e.g., 40% revenue growth]
↑
|
Lagging: [Revenue, MRR]
↑
|
North Star: [Weekly Active Users]
↑
|
┌───┴───┬───────┬───────┐
│ │ │ │
Input 1 Input 2 Input 3 Input 4
(Activation) (Engagement) (Retention) (Referral)
│ │ │ │
└───┬───┴───┬───┴───┬───┘
│ │ │
Feature Feature Feature
Metrics Metrics Metrics
```

**Describe your belief chain:**

1. We believe [Input 1: Activation] drives [North Star: WAU] because [activated users return 3x more frequently]
1. We believe [Input 2: Engagement] drives [North Star: WAU] because [engaged users create habits and perceive more value]
1. We believe [North Star: WAU] drives [Lagging: Revenue] because [historical correlation of 0.85 and 60-day lag time]

-----

## 📅 Review Cadence & Rituals

### Daily (5-10 min standup check)

**Metrics:**

- Critical health metrics
- Error rates
- System performance

**Format:** Quick dashboard review, flag anomalies only

### Weekly (30-60 min team review)

**Metrics:**

- All leading indicators
- Feature/initiative progress
- Early trends

**Format:**

- What moved? Why?
- What’s trending? Implications?
- What needs attention?
- Quick wins to try?

### Monthly (90 min cross-functional)

**Metrics:**

- North Star + all inputs
- Lagging business metrics
- Cohort analysis

**Format:**

- Deep dive on 1-2 metrics
- Experiment results review
- Strategic adjustments
- Resource allocation decisions

### Quarterly (Half-day workshop)

**Metrics:**

- Full portfolio audit
- Metric relevance check
- New metric proposals

**Format:**

- Strategy alignment check
- Sunset obsolete metrics
- Add new strategic metrics
- Validate measurement methods

-----

## 🔬 Metric Validation & Testing

### Vanity Metric Test

Ask these questions. If you answer “No” to 2+, it’s likely vanity:

- [ ] Can we take specific actions to improve this metric?
- [ ] Does improving this metric definitely improve business outcomes?
- [ ] Can we reproduce the results intentionally?
- [ ] Does this metric tell us something we didn’t already know?
- [ ] Would this metric reveal bad news if things were going poorly?

### Leading Indicator Validation

Test if your leading indicator actually predicts your lagging outcome:

|Leading Metric|Lagging Metric|Correlation|Time Lag|Confidence |
|--------------|--------------|-----------|--------|------------|
|[Input 1] |[North Star] |[r² = 0.XX]|[X days]|High/Med/Low|
|[Input 2] |[North Star] |[r² = 0.XX]|[X days]|High/Med/Low|
|[North Star] |[Revenue] |[r² = 0.XX]|[X days]|High/Med/Low|

**Example:**

|Leading Metric |Lagging Metric |Correlation|Time Lag|Confidence|
|----------------|-------------------------|-----------|--------|----------|
|Activation rate |Weekly Active Users |r² = 0.82 |14 days |High |
|WAU |Monthly Recurring Revenue|r² = 0.87 |60 days |High |
|Feature adoption|Upgrade rate |r² = 0.45 |30 days |Medium |

-----

## 🎯 Metric-Driven Decision Making

### Decision Framework

**For each metric, define:**

1. **Green Zone (Above Target):**
- What this means: [Interpretation]
- What we do: [Actions]
- Who decides: [Owner]
1. **Yellow Zone (Near Target):**
- What this means: [Interpretation]
- What we do: [Actions]
- Who decides: [Owner]
1. **Red Zone (Below Target):**
- What this means: [Interpretation]
- What we do: [Actions]
- Who decides: [Owner]

**Example: New User Activation Rate**

1. **Green Zone (>60%):**
- What this means: Onboarding is working well; focus on scale
- What we do: Document success patterns; invest in acquisition
- Who decides: Growth Team Lead
1. **Yellow Zone (50-60%):**
- What this means: Acceptable but room for improvement
- What we do: Run small experiments; monitor closely
- Who decides: Growth Team Lead
1. **Red Zone (<50%):**
- What this means: Critical issue; impacts North Star
- What we do: Stop all new work; focus on activation fixes
- Who decides: VP Product (escalation)

-----

## 🚨 Metric Red Flags

Watch for these warning signs:

### Gaming Signals

- [ ] Metric improves but customer satisfaction decreases
- [ ] Teams optimize for metric in ways that hurt other areas
- [ ] Metric movement doesn’t correlate with qualitative feedback
- [ ] Unusual spikes that can’t be explained by product changes

### Vanity Metric Indicators

- [ ] Metric always goes up (even when things are bad)
- [ ] No clear action emerges from metric changes
- [ ] Leadership loves it but teams don’t use it
- [ ] Can’t explain causation, only correlation

### Metric Fatigue Symptoms

- [ ] More than 10 metrics per team
- [ ] Metrics haven’t been reviewed in 6+ months
- [ ] No one can explain why we track certain metrics
- [ ] Dashboards are ignored in meetings

-----

## 🔄 Metric Evolution Log

Track major changes to your metrics framework:

|Date |Change |Reason |Impact |Owner |
|------|--------------|-------------------|---------------|-------------|
|[Date]|[What changed]|[Why we changed it]|[What happened]|[Who decided]|
| | | | | |

**Example:**

|Date |Change |Reason |Impact |Owner |
|-------|---------------------------------------------------|-------------------------------------------------------|---------------------------------------------|----------|
|2024-Q2|Changed from “Total Users” to “Weekly Active Users”|Total users was vanity; didn’t predict retention |Better alignment; teams focused on engagement|CPO |
|2024-Q3|Added “Time to first value” as input metric |Realized activation timing matters more than completion|30% improvement in retention |Growth PM |
|2024-Q4|Sunset “NPS score” as primary metric |Lagging and not actionable; moved to quarterly survey |Freed team to focus on behavioral metrics |VP Product|

-----

## 📚 Metric Definitions Library

Maintain clear definitions for all metrics:

### [Metric Name 1]

**Definition:** [Precise formula or measurement method]

**Calculation:** [Numerator / Denominator × 100] or [Specific counting method]

**Data Source:** [Where the data comes from]

**Frequency:** [How often it’s calculated]

**Owner:** [Who’s responsible]

**Related Metrics:** [Metrics that influence or are influenced by this one]

**Example:**

```
Weekly Active Users (WAU)

Definition: Unique count of users who complete at least one core action
within a rolling 7-day window.

Calculation: COUNT(DISTINCT user_id) WHERE action_type IN
('create_analysis', 'share_insight', 'export_data') AND
action_timestamp >= CURRENT_DATE - 7

Data Source: events.user_actions table

Frequency: Calculated daily, reported weekly

Owner: Growth Product Manager

Related Metrics:
- Influenced by: Activation Rate, Feature Adoption
- Influences: Monthly Recurring Revenue, Retention Rate
```

-----

## 🎓 Metric Education

### For New Team Members

**Week 1 Onboarding:**

- [ ] Review metric framework document
- [ ] Attend weekly metric review
- [ ] Shadow metric owner for one review cycle

**Key Concepts to Understand:**

1. The difference between vanity and actionable metrics
1. How leading indicators predict lagging outcomes
1. Our North Star Metric and why we chose it
1. The 3-5 input metrics and how work connects to them

### Ongoing Learning

**Monthly “Metric Moments”:**

- 15-minute session on one metric
- Why it matters
- Recent trends
- How teams can influence it

**Quarterly Deep-Dives:**

- Full framework review
- Case studies of decisions driven by metrics
- Anti-patterns and what to avoid

-----

## ✅ Quick Reference: Good vs. Bad Metrics

### Actionable vs. Vanity

|❌ Vanity Metric |✅ Actionable Alternative |Why It’s Better |
|----------------------|---------------------------------|------------------------|
|Total users |Weekly/Monthly Active Users |Shows actual engagement |
|Page views |Pages per session or time to task|Shows value realization |
|Downloads |Daily Active Users (DAU) |Shows actual usage |
|Email subscribers |Email click-through rate |Shows engagement quality|
|Social media followers|Conversion rate from social |Shows business impact |
|Server uptime % |Error rate affecting users |Shows user impact |

### Leading vs. Lagging

|📊 Lagging (Results) |⚡ Leading (Predictors) |Time Advantage|
|---------------------|------------------------------|--------------|
|Revenue |Qualified pipeline |30-60 days |
|Churn rate |Product engagement score |14-30 days |
|Customer satisfaction|Support ticket resolution time|7-14 days |
|Market share |New user acquisition rate |60-90 days |
|Retention rate |Activation rate |30-60 days |

-----

## 🔧 Tools & Resources

### Recommended Reading

- “Lean Analytics” by Alistair Croll & Benjamin Yoskovitz
- “The Lean Startup” by Eric Ries (Chapter on Vanity Metrics)
- Amplitude’s “North Star Playbook”
- John Cutler’s work on product metrics

### Dashboard Tools

- Amplitude (product analytics)
- Mixpanel (behavioral analytics)
- Looker/Tableau (business intelligence)
- Mode Analytics (SQL-based analysis)

### Metric Templates

- North Star Metric Canvas
- Metric Definition Template
- Weekly Metric Review Template
- Quarterly Metric Audit Checklist

-----

## References

- Strategy: `../../2.1-Strategy/README.md` (North Star, OKRs, Roadmap)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
