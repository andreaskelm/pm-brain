# Kano Model Analysis Template

## Project Context

**Product/Project Name:** [Your product name]  
**Analysis Date:** [Date]  
**Product Stage:** [Pre-launch MVP / Growth / Mature]  
**Target Customers:** [Who you surveyed]  
**Sample Size:** [Number of responses]

**Analysis Objectives:**
- [Objective 1: e.g., Prioritize features for Q2 roadmap]
- [Objective 2: e.g., Identify differentiation opportunities]
- [Objective 3: e.g., Define MVP feature set]

---

## Features Analyzed

List all features evaluated in this Kano analysis:

| # | Feature Name | Brief Description |
|---|--------------|-------------------|
| 1 | [Feature name] | [One-line description] |
| 2 | [Feature name] | [One-line description] |
| 3 | [Feature name] | [One-line description] |

### Example:
| # | Feature Name | Brief Description |
|---|--------------|-------------------|
| 1 | Real-time collaboration | Multiple users can edit documents simultaneously |
| 2 | Dark mode | Alternative dark color theme for the interface |
| 3 | Advanced search filters | Filter results by date, type, status, tags |
| 4 | Email notifications | Receive email alerts for important updates |
| 5 | Two-factor authentication | Additional security layer beyond password |

---

## Kano Questionnaire Template

Use this format for each feature in your survey:

### Feature: [Feature Name]

**Functional Question:**  
"If [product] had [feature], how would you feel?"

**Dysfunctional Question:**  
"If [product] did NOT have [feature], how would you feel?"

**Response Options (same for both questions):**
1. I like it / I would enjoy it
2. I expect it / I must have it
3. I am neutral / I don't care
4. I can live with it / I can tolerate it
5. I dislike it / I would dislike it

---

### Example: Real-time Collaboration

**Functional Question:**  
"If our project management tool allowed you to collaborate with teammates in real-time on documents, how would you feel?"

**Dysfunctional Question:**  
"If our project management tool did NOT allow you to collaborate with teammates in real-time on documents, how would you feel?"

**Response Options:**
- [ ] I like it / I would enjoy it
- [ ] I expect it / I must have it
- [ ] I am neutral / I don't care
- [ ] I can live with it / I can tolerate it
- [ ] I dislike it / I would dislike it

---

## Kano Evaluation Table

Use this table to map response pairs to categories:

| | **Dysfunctional →** | **I like it** | **I expect it** | **I'm neutral** | **I can live with it** | **I dislike it** |
|---|---|---|---|---|---|---|
| **Functional ↓** | | | | | | |
| **I like it** | | Questionable | Attractive | Attractive | Attractive | Performance |
| **I expect it** | | Reverse | Indifferent | Indifferent | Indifferent | Must-Have |
| **I'm neutral** | | Reverse | Indifferent | Indifferent | Indifferent | Must-Have |
| **I can live with it** | | Reverse | Indifferent | Indifferent | Indifferent | Must-Have |
| **I dislike it** | | Reverse | Reverse | Reverse | Reverse | Questionable |

**How to use:**
1. Find the functional response in the left column
2. Find the dysfunctional response in the top row
3. The intersection shows the Kano category

**Example:** Functional = "I like it", Dysfunctional = "I dislike it" → **Performance**

---

## Analysis Results

### Feature Classification Summary

| Feature | Must-Have | Performance | Attractive | Indifferent | Reverse | Questionable | **Primary Category** |
|---------|-----------|-------------|------------|-------------|---------|--------------|---------------------|
| [Feature 1] | 45% | 30% | 20% | 5% | 0% | 0% | Must-Have |
| [Feature 2] | 10% | 15% | 60% | 15% | 0% | 0% | Attractive |

### Example:
| Feature | Must-Have | Performance | Attractive | Indifferent | Reverse | Questionable | **Primary Category** |
|---------|-----------|-------------|------------|-------------|---------|--------------|---------------------|
| Real-time collaboration | 45% | 30% | 20% | 5% | 0% | 0% | **Must-Have** |
| Dark mode | 5% | 10% | 35% | 45% | 3% | 2% | **Indifferent** |
| Advanced search filters | 20% | 50% | 25% | 5% | 0% | 0% | **Performance** |
| Email notifications | 15% | 35% | 40% | 8% | 2% | 0% | **Attractive** |
| Two-factor authentication | 60% | 25% | 10% | 5% | 0% | 0% | **Must-Have** |

---

## Satisfaction Coefficients

Calculate impact on satisfaction and dissatisfaction:

**Formulas:**
- **CS+ (Satisfaction)** = (Attractive + Performance) / (Attractive + Performance + Must-Have + Indifferent)
- **CS- (Dissatisfaction)** = -1 × (Must-Have + Performance) / (Attractive + Performance + Must-Have + Indifferent)

| Feature | CS+ (Satisfaction) | CS- (Dissatisfaction) | Interpretation |
|---------|-------------------|----------------------|----------------|
| [Feature 1] | 0.53 | -0.79 | High dissatisfaction if absent; moderate satisfaction if present |
| [Feature 2] | 0.47 | -0.16 | Moderate satisfaction if present; low dissatisfaction if absent |

### Example:
| Feature | CS+ | CS- | Interpretation |
|---------|-----|-----|----------------|
| Real-time collaboration | 0.53 | -0.79 | **Critical:** High dissatisfaction if absent; moderate satisfaction if present → Must-Have |
| Dark mode | 0.47 | -0.16 | **Low impact:** Moderate satisfaction if present; low dissatisfaction if absent → Nice-to-have |
| Advanced search filters | 0.79 | -0.74 | **High impact:** Strong satisfaction if present; high dissatisfaction if absent → Performance |
| Email notifications | 0.79 | -0.53 | **Delight opportunity:** Strong satisfaction if present; moderate dissatisfaction if absent → Attractive |
| Two-factor authentication | 0.37 | -0.89 | **Critical:** High dissatisfaction if absent; low satisfaction if present → Must-Have |

---

## Prioritization Matrix

### Must-Have Features (Prevent Dissatisfaction)

Features with high |CS-| scores that customers expect:

| Feature | CS- | Implementation Effort | Priority | Rationale |
|---------|-----|---------------------|----------|-----------|
| [Feature name] | -0.89 | Medium | P0 | [Why this is critical] |

#### Example:
| Feature | CS- | Implementation Effort | Priority | Rationale |
|---------|-----|---------------------|----------|-----------|
| Two-factor authentication | -0.89 | Medium | **P0** | Security baseline expectation; 60% categorized as must-have; high dissatisfaction risk |
| Real-time collaboration | -0.79 | Large | **P0** | Core competitive feature; 45% must-have; users expect it from project management tools |

**Action:** Build all must-haves to "good enough" quality. Don't over-invest beyond baseline.

---

### Performance Features (Drive Competitive Advantage)

Features with high CS+ and CS- scores that scale satisfaction:

| Feature | CS+ | CS- | Implementation Effort | Strategic Value | Priority | Rationale |
|---------|-----|-----|---------------------|----------------|----------|-----------|
| [Feature name] | 0.79 | -0.74 | Medium | High | P1 | [Why this matters] |

#### Example:
| Feature | CS+ | CS- | Effort | Strategic Value | Priority | Rationale |
|---------|-----|-----|--------|----------------|----------|-----------|
| Advanced search filters | 0.79 | -0.74 | Medium | High | **P1** | Direct correlation with satisfaction; competitors have basic search; 50% performance categorization |
| Processing speed | 0.82 | -0.68 | Large | High | **P1** | "More is better" dynamic; key comparison point vs. competitors; directly impacts daily experience |

**Action:** Invest strategically in 2-3 high-impact performance features. Focus on areas where competitors are weak.

---

### Attractive Features (Create Delight & Differentiation)

Features with high CS+ but low |CS-| scores that exceed expectations:

| Feature | CS+ | Implementation Effort | Brand Alignment | ROI Estimate | Priority | Rationale |
|---------|-----|---------------------|----------------|--------------|----------|-----------|
| [Feature name] | 0.79 | Low | High | High | P2 | [Why this delights] |

#### Example:
| Feature | CS+ | Effort | Brand Alignment | ROI | Priority | Rationale |
|---------|-----|--------|----------------|-----|----------|-----------|
| Email notifications | 0.79 | Low | High | High | **P2** | 40% attractive; unexpected value-add; low effort for high satisfaction; supports "helpful" brand positioning |
| AI-powered insights | 0.85 | Large | High | Medium | **P3** | Strong delight potential; cutting-edge positioning; defer until basics are solid |
| Celebration animations | 0.72 | Low | High | Medium | **P2** | Unexpected delight; reinforces positive moments; quick win for brand personality |

**Action:** Select 1-3 strategic attractive features. Prioritize low-effort / high-CS+ items. Use for differentiation and brand building.

---

### Indifferent Features (Low Priority)

Features with low CS+ and CS- scores that don't impact satisfaction:

| Feature | CS+ | CS- | Recommendation | Rationale |
|---------|-----|-----|----------------|-----------|
| [Feature name] | 0.47 | -0.16 | Defer or drop | [Why customers don't care] |

#### Example:
| Feature | CS+ | CS- | Recommendation | Rationale |
|---------|-----|-----|----------------|-----------|
| Dark mode | 0.47 | -0.16 | **Defer** | 45% indifferent; low impact on satisfaction; resources better spent on performance features; reconsider if market shifts |
| Custom keyboard shortcuts | 0.35 | -0.12 | **Drop** | Power user feature with minimal adoption; <10% would use; not worth maintenance burden |

**Action:** Defer or drop unless strategically necessary. Redirect resources to impactful features.

---

### Reverse Features (Create Dissatisfaction)

Features that decrease satisfaction when present:

| Feature | Reverse % | Customer Segment | Recommendation | Rationale |
|---------|-----------|------------------|----------------|-----------|
| [Feature name] | 15% | [Which segment dislikes] | [Make optional / Remove] | [Why it causes dissatisfaction] |

#### Example:
| Feature | Reverse % | Segment | Recommendation | Rationale |
|---------|-----------|---------|----------------|-----------|
| Automated suggestions | 12% | Privacy-conscious users | **Make optional** | Some users find proactive AI intrusive; make opt-in with clear controls |
| Gamification badges | 8% | Enterprise users | **Remove from enterprise tier** | Professional users find badges juvenile; keep for consumer tier only |

**Action:** Make optional, segment-specific, or remove. Understand why it's reverse for some customers.

---

## Roadmap Implications

### Immediate (0-3 months) - Must-Haves

Features to build now to prevent dissatisfaction:

| Feature | Category | Timeline | Notes |
|---------|----------|----------|-------|
| [Feature] | Must-Have | Q1 2025 | [Implementation notes] |

#### Example:
| Feature | Category | Timeline | Notes |
|---------|----------|----------|-------|
| Two-factor authentication | Must-Have | Q1 2025 | Security baseline; required for enterprise sales; build to industry standard |
| Real-time collaboration | Must-Have | Q1 2025 | Core MVP feature; 45% must-have; build basic version first, enhance later |

---

### Near-term (3-6 months) - Performance Features

Features to drive competitive advantage:

| Feature | Category | Timeline | Strategic Rationale |
|---------|----------|----------|---------------------|
| [Feature] | Performance | Q2 2025 | [Why this matters competitively] |

#### Example:
| Feature | Category | Timeline | Strategic Rationale |
|---------|----------|----------|---------------------|
| Advanced search filters | Performance | Q2 2025 | Competitors have basic search; 50% performance category; direct satisfaction driver |
| Processing speed optimization | Performance | Q2 2025 | "More is better" dynamic; #1 complaint about competitors; measurable competitive advantage |

---

### Medium-term (6-12 months) - Attractive Features

Features to create delight and differentiation:

| Feature | Category | Timeline | Brand Alignment |
|---------|----------|----------|-----------------|
| [Feature] | Attractive | H2 2025 | [How this supports brand positioning] |

#### Example:
| Feature | Category | Timeline | Brand Alignment |
|---------|----------|----------|-----------------|
| Email notifications | Attractive | Q3 2025 | Supports "helpful" brand; 40% attractive; low effort after core features solid |
| Celebration animations | Attractive | Q3 2025 | Reinforces "delightful" brand personality; unexpected positive moments; quick win |

---

## Segmentation Analysis (If Applicable)

Break down results by customer segment if significant differences exist:

### Segment: [Enterprise Customers]

| Feature | Must-Have | Performance | Attractive | Primary Category |
|---------|-----------|-------------|------------|------------------|
| [Feature] | 65% | 25% | 10% | Must-Have |

### Segment: [SMB Customers]

| Feature | Must-Have | Performance | Attractive | Primary Category |
|---------|-----------|-------------|------------|------------------|
| [Feature] | 20% | 30% | 45% | Attractive |

**Key Insights:**
- [Insight 1: e.g., Enterprise customers have higher must-have expectations]
- [Insight 2: e.g., SMB customers more delighted by certain features]
- [Insight 3: e.g., Consider product tiering based on segment differences]

---

## Key Insights & Recommendations

### Top Insights

1. **[Insight 1]**
   - [Supporting data]
   - [Implication for product strategy]

2. **[Insight 2]**
   - [Supporting data]
   - [Implication for product strategy]

3. **[Insight 3]**
   - [Supporting data]
   - [Implication for product strategy]

### Example:
1. **Security is non-negotiable baseline**
   - Two-factor authentication: 60% must-have, CS- = -0.89
   - Without security basics, product won't be considered by 60% of target market
   - **Action:** Prioritize security must-haves as P0, even before collaboration features

2. **Search is competitive battlefield**
   - Advanced search filters: 50% performance, CS+ = 0.79, CS- = -0.74
   - Competitors have basic search; opportunity to differentiate with advanced capabilities
   - **Action:** Invest in search as primary performance differentiator in Q2

3. **Low-effort delighters exist**
   - Email notifications: 40% attractive, CS+ = 0.79, low implementation effort
   - Celebration animations: Quick win for brand personality
   - **Action:** Include 2-3 low-effort attractive features in each release for delight

---

## Assumptions & Limitations

**Assumptions:**
- [Assumption 1: e.g., Survey sample is representative of target market]
- [Assumption 2: e.g., Features are independent and don't overlap]
- [Assumption 3: e.g., Customer expectations won't shift significantly in next 6 months]

**Limitations:**
- [Limitation 1: e.g., Sample size of 50 may not capture full diversity]
- [Limitation 2: e.g., Survey doesn't capture "why" behind categorizations]
- [Limitation 3: e.g., Missing certain customer segments in sample]

**Next Steps:**
- [Next step 1: e.g., Conduct follow-up interviews for must-have features]
- [Next step 2: e.g., Validate with competitive analysis]
- [Next step 3: e.g., Re-survey in 6 months to track category drift]

---

## Category Evolution Tracking

Monitor how features move between categories over time:

| Feature | Current Category | Previous Category (Date) | Trend | Action |
|---------|-----------------|-------------------------|-------|--------|
| [Feature] | Performance | Attractive (Q1 2024) | Drifting to must-have | Monitor closely; becoming baseline |

### Example:
| Feature | Current Category | Previous (6mo ago) | Trend | Action |
|---------|-----------------|-------------------|-------|--------|
| Real-time collaboration | Must-Have | Performance (Q3 2024) | Drift to must-have | Competitors launched; now expected; invest in reliability over features |
| AI recommendations | Attractive | Indifferent (Q3 2024) | Rising interest | Market education working; continue as delighter |

**Watch for:**
- Attractive → Performance (customers now expect it)
- Performance → Must-Have (baseline expectation)
- Track competitor launches and market shifts

---

## Communication Plan

### For Leadership
**Key Messages:**
- Must-haves identified: [X features] required to prevent dissatisfaction
- Performance opportunities: [Y features] for competitive differentiation
- Delight potential: [Z features] for brand building and loyalty

**Resource Request:**
- [Budget/headcount needs based on must-haves and strategic performance features]

---

### For Engineering
**Technical Priorities:**
- Must-haves: [List with CS- scores] - these prevent customer loss
- Performance features: [List with CS+ scores] - these drive satisfaction linearly
- Attractive features: [List] - low effort / high delight opportunities

**Quality Expectations:**
- Must-haves: Good enough, reliable, no need for polish beyond baseline
- Performance features: Scalable, measurable, invest in optimization
- Attractive features: Polished, delightful, create "wow" moments

---

### For Sales/Marketing
**Positioning:**
- **Must-haves:** "We meet industry standards with [list features]"
- **Performance features:** "We excel at [list features] better than competitors"
- **Attractive features:** "We delight customers with [list features] they don't expect"

**Competitive Messaging:**
- [Feature X] is our performance differentiator vs. [Competitor]
- [Feature Y] is our unexpected delight that creates loyalty
- [Feature Z] is baseline - don't oversell

---

## Review Schedule

- **Immediately:** Validate top insights with qualitative research
- **Monthly:** Monitor feature adoption and satisfaction for launched features
- **Quarterly:** Quick pulse check on category stability
- **Annually:** Full Kano re-survey to track category evolution

---

## Related Templates & Frameworks

- Kano Framework: `1-kano-framework.md`
- Prioritization Methods (RICE, ICE, Impact-Effort, MoSCoW, Kano): `../4-Prioritization/README.md`
- MoSCoW Template: `../3-MoSCoW/2-moscow-prioritization-template.md`
- Roadmap Template: `../2-Roadmap/2-roadmap-template.md`
- Execution: `../../2.3-Execution/README.md` (PRD Template)

---

**Notes:**
- This is a living document - update as priorities and categories evolve
- Not all sections need to be filled out - adapt to your needs
- Combine Kano with qualitative research for full picture
- Re-survey periodically as customer expectations evolve
- Use satisfaction coefficients (CS+/CS-) for nuanced prioritization decisions
