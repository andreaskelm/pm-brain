# Product Prioritization Template

## Disclaimer

This prioritization reflects our current strategy and understanding. Priorities will evolve as we learn, as market conditions change, and as new opportunities emerge.

**Last prioritization:** [Date]
**Next review:** [Date]
**Method used:** [RICE / ICE / Impact-Effort / Other]
**Decision owner:** [Name/Role]

-----

## 📋 Prioritization Backlog

### Initiative Scoring (RICE Method)

|Initiative|Reach |Impact |Confidence|Effort |RICE Score |Priority|Status |
|----------|-----------|--------|----------|---------------|------------|--------|--------|
|[Name] |[#/quarter]|[0.25-3]|[50-100%] |[person-months]|[calculated]|[rank] |[Status]|
| | | | | | | | |
| | | | | | | | |

**Example:**

|Initiative |Reach |Impact|Confidence|Effort|RICE Score|Priority|Status |
|--------------------------------|-------|------|----------|------|----------|--------|-----------|
|Multi-factor auth for enterprise|5,000 |3.0 |100% |4 |**3,750** |1 |In Progress|
|Redesign onboarding flow |4,500 |2.0 |80% |3 |**2,400** |2 |Next |
|Dark mode |80,000 |1.0 |80% |2 |**32,000**|3 |Backlog |
|AI recommendations |150,000|2.0 |50% |6 |**25,000**|4 |Backlog |

---

## 🧠 Product Sense Check (Use with Top Initiatives)

For the few initiatives that actually drive your roadmap, run this **before** you treat the RICE score as truth. For each top item, consider adding a short entry to:

- `00-Meta/prioritization-decision-log.md`

Use these prompts:

- Who specifically is this initiative for? (Name the real segment/persona.)
- What job/pain/behavior are we really prioritizing, beyond the feature label?
- What evidence do we have that this matters (stories + metrics)? Where is it weak?
- What’s the opportunity cost of doing this now?
- What could go catastrophically wrong if we are wrong on this bet? (Second-order effects.)

Only then treat the score as one input into the decision, not the decision itself.

-----

## 📊 Initiative Deep-Dive Template

For each top-priority initiative, document detailed scoring rationale:

### Initiative: [Name]

**One-liner:** [Concise description of what this is]

**Problem:** [What customer/business problem does this solve?]

**Solution:** [High-level approach]

-----

#### RICE Scoring Detail

**Reach: [Number per time period]**

- Data source: [Where this number comes from]
- Calculation: [Show your math]
- Assumptions: [What we’re assuming]

**Example:**

- **Reach: 5,000 enterprise users per quarter**
- Data source: Customer segmentation analysis
- Calculation: 50 enterprise accounts × 100 avg users/account = 5,000
- Assumptions: 90% adoption based on similar security features

**Impact: [0.25 to 3.0]**

- Metric affected: [Which metric this moves]
- Expected change: [How much it will move]
- Why this score: [Rationale]

**Example:**

- **Impact: 3.0 (Massive)**
- Metric affected: Enterprise churn rate
- Expected change: Reduces churn from 15% to 8%
- Why this score: MFA is #1 requested feature; blocke 3 deals last quarter

**Confidence: [50-100%]**

- Evidence: [What gives you confidence]
- Risks/unknowns: [What could change]
- How to increase: [What would raise confidence]

**Example:**

- **Confidence: 100%**
- Evidence: Customer interviews (20), contract requirements (3), competitive analysis
- Risks/unknowns: None - this is table stakes for enterprise
- How to increase: N/A - already high

**Effort: [Person-months]**

- Breakdown: [PM, Design, Eng, QA time]
- Dependencies: [External factors]
- Risk factors: [What could increase effort]

**Example:**

- **Effort: 4 person-months**
- Breakdown: PM (0.5), Design (1), Engineering (2), QA (0.5)
- Dependencies: Security audit required (included in estimate)
- Risk factors: Third-party integration complexity (mitigated by vendor partnership)

-----

**RICE Score:** [Calculated value]

**Priority Rank:** [Position in backlog]

**Decision:** [Prioritize / Deprioritize / Defer]

**Rationale:** [Why this decision given the score]

-----

## 🎯 Portfolio Balance

### Current Distribution

|Quadrant |# of Initiatives|% of Total Effort|Target %|Gap |
|-----------------------------------------|----------------|-----------------|--------|-----|
|Quick Wins (High Impact, Low Effort) |[count] |[%] |40% |[+/-]|
|Major Projects (High Impact, High Effort)|[count] |[%] |40% |[+/-]|
|Fill-Ins (Low Impact, Low Effort) |[count] |[%] |10% |[+/-]|
|Money Pits (Low Impact, High Effort) |[count] |[%] |0% |[+/-]|
|Innovation/Exploration |[count] |[%] |10% |[+/-]|

### Actions Needed

Based on portfolio analysis:

- **Overweighted in:** [Which quadrant]
- **Action:** [What to do about it]
- **Underweighted in:** [Which quadrant]
- **Action:** [What to do about it]

-----

## 👥 RACI Matrix

### For Key Initiatives

|Initiative / Task|Product|Engineering|Design|Marketing|Legal|Customer Success|
|-----------------|-------|-----------|------|---------|-----|----------------|
|[Initiative 1] |A,R |R |C |I |C |I |
|[Sub-task 1] |A |R |R |- |- |I |
|[Sub-task 2] |C |A,R |C |I |- |I |
| | | | | | | |

**Example: Multi-Factor Authentication Launch**

|Task |Product|Engineering|Design|Marketing|Legal|Support|
|------------------------|-------|-----------|------|---------|-----|-------|
|Feature specification |A,R |C |C |- |C |C |
|Technical implementation|C |A,R |- |- |- |- |
|UI/UX design |C |C |A,R |- |- |C |
|Security audit |A |R |- |- |C |- |
|Go-to-market plan |C |I |I |A,R |- |C |
|Customer documentation |C |C |C |C |- |A,R |
|Launch communication |I |I |I |A |I |R |

**Key:**

- **R** = Responsible (does the work)
- **A** = Accountable (owns the outcome) - ONE per task
- **C** = Consulted (provides input)
- **I** = Informed (kept in loop)

-----

## 📅 Prioritization Timeline

### Now (Q[X] 20XX)

**Committed Work:**

|Initiative |RICE Score|Team |Expected Completion|Success Criteria |
|------------|----------|------|-------------------|-----------------|
|[Initiative]|[Score] |[Team]|[Date] |[Metric movement]|
| | | | | |

### Next (Q[X+1] 20XX)

**Planned Work:**

|Initiative |RICE Score|Team |Tentative Start|Dependencies|
|------------|----------|------|---------------|------------|
|[Initiative]|[Score] |[Team]|[Date] |[Blockers] |
| | | | | |

### Later (Q[X+2] 20XX & Beyond)

**Future Considerations:**

|Initiative |RICE Score|Strategic Value |What We Need to Learn |
|------------|----------|------------------|------------------------|
|[Initiative]|[Score] |[Why this matters]|[To increase confidence]|
| | | | |

-----

## 🔄 Deprioritization Log

**Track what we’re NOT doing and why:**

|Initiative|RICE Score|Why Deprioritized|Revisit When |
|----------|----------|-----------------|----------------|
|[Name] |[Score] |[Rationale] |[Condition/Date]|
| | | | |

**Example:**

|Initiative |RICE Score|Why Deprioritized |Revisit When |
|---------------|----------|---------------------------------------------------------------|---------------------------------------------|
|Social sharing |450 |Low RICE score; narrow reach (500 users); 6 months effort |Q3 when we reach 5K users |
|Custom branding|200 |Nice-to-have; not tied to key metric; 3 months effort |Enterprise accounts >25% of revenue |
|Mobile app |800 |High effort (12 months); unproven demand; strategic uncertainty|After web product achieves product-market fit|

-----

## 🎯 Decision Framework

### Decision Criteria Weighting

**What matters most in our prioritization?** (Total = 100%)

|Criterion |Weight|How We Evaluate |
|-------------------|------|----------------------------------------------------|
|Strategic Alignment|[%] |Does this support our North Star and strategy? |
|Customer Value |[%] |Does this solve a real, validated customer problem? |
|Business Impact |[%] |Does this move our key business metrics? |
|Feasibility |[%] |Can we realistically build and ship this? |
|Market Timing |[%] |Is now the right time (competitive, seasonal, etc.)?|

**Example:**

|Criterion |Weight|How We Evaluate |
|-------------------|------|--------------------------------------------------------|
|Strategic Alignment|30% |Does this support enterprise expansion (our #1 goal)? |
|Customer Value |30% |Is this a top-3 requested feature with validated demand?|
|Business Impact |25% |Does this reduce churn or increase expansion revenue? |
|Feasibility |10% |Can we ship within one quarter? |
|Market Timing |5% |Does this match buying cycles or competitive landscape? |

-----

## 📈 Prioritization Health Metrics

### Track These Over Time

|Metric |Current|Target |Trend|Notes |
|----------------------------|-------|-------|-----|------------------------------------------------|
|**Delivery Accuracy** |[%] |80% |[↑↓→]|% of prioritized items actually completed |
|**Value Realization** |[%] |70% |[↑↓→]|% of shipped features moving target metrics |
|**Team Alignment** |[%] |90% |[↑↓→]|% of team who can explain top 3 priorities |
|**Decision Speed** |[days] |<7 days|[↑↓→]|Avg time from idea to priority decision |
|**Score Accuracy** |[%] |60% |[↑↓→]|Actual impact vs. predicted impact score |
|**Stakeholder Satisfaction**|[1-5] |4.0 |[↑↓→]|Survey: “Do you understand priority trade-offs?”|

-----

## 💡 Scoring Workshop Template

### 90-Minute Prioritization Session

**Pre-work (Before Meeting):**

- [ ] List all initiatives to prioritize
- [ ] Gather available data (analytics, customer feedback, estimates)
- [ ] Share framework overview with participants

**Agenda:**

**Part 1: Alignment (15 min)**

- Review business goals and strategy
- Confirm decision criteria and weights
- Set context for prioritization

**Part 2: Individual Scoring (20 min)**

- Each participant scores initiatives independently
- Use RICE or chosen framework
- Document assumptions

**Part 3: Discussion (40 min)**

- Compare scores for each initiative
- Discuss major discrepancies
- Challenge assumptions
- Reach consensus on scores

**Part 4: Prioritization (15 min)**

- Rank by score
- Apply decision criteria
- Agree on top 3-5 priorities
- Document deprioritization decisions

**Outputs:**

- Scored and ranked backlog
- Top priorities with owners
- Deprioritization rationale
- Next steps and timeline

-----

## ⚠️ Common Prioritization Anti-Patterns

### Anti-Pattern #1: HiPPO-Driven Priorities

**What it looks like:**

- Highest Paid Person’s Opinion overrides scoring
- “Because the CEO wants it” ends debate
- Team scores initiatives but leadership ignores them

**Why it’s harmful:**

- Demotivates team
- Poor accountability (can’t say no)
- Builds wrong features

**Solution:**

- Leadership scores alongside team
- Scores are starting point, not end point
- Require data-backed overrides

### Anti-Pattern #2: Analysis Paralysis

**What it looks like:**

- Spending weeks perfecting RICE scores
- Endless debates over 0.5 vs 1.0 impact
- Never making a decision

**Why it’s harmful:**

- Slows progress
- Opportunity cost of delay
- Perfect is enemy of good

**Solution:**

- Set time limits (1 hour per initiative max)
- Use T-shirt sizes before detailed scoring
- Make decision with 70% confidence

### Anti-Pattern #3: Score Gaming

**What it looks like:**

- Inflating impact scores for pet projects
- Deflating effort estimates
- Cherry-picking data

**Why it’s harmful:**

- Destroys framework trust
- Leads to poor decisions
- Creates political environment

**Solution:**

- Collaborative scoring with diverse perspectives
- Track actual vs. predicted outcomes
- Reward accuracy, not optimism

### Anti-Pattern #4: The “Everything is High Priority” Trap

**What it looks like:**

- All initiatives marked as “critical”
- Unable to say no to anything
- Team constantly context-switching

**Why it’s harmful:**

- Nothing gets finished
- Team burnout
- Low-value work dilutes impact

**Solution:**

- Force-rank everything
- Use portfolio targets (70-20-10 rule)
- Accept trade-offs explicitly

### Anti-Pattern #5: Set-and-Forget Prioritization

**What it looks like:**

- Prioritize once at year/quarter start
- Never revisit despite new information
- Ignore changing conditions

**Why it’s harmful:**

- Waste effort on obsolete work
- Miss timely opportunities
- Lose competitive advantage

**Solution:**

- Regular review cadence (bi-weekly minimum)
- Trigger-based re-prioritization
- Build learning into process

-----

## References

- RICE/ICE Framework: `1-RICE-ICE-scoring-framework.md`
- RICE/ICE Template: `2-RICE-ICE-scoring-template.md`
- Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
- OKR Framework: `../1-OKR/README.md`
- Roadmap: `../2-Roadmap/README.md`
- North Star: `../3-North-Star/README.md`
