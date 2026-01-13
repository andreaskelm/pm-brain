# Kano Model Framework

## Overview

The Kano model is a theory for product development and customer satisfaction developed in the 1980s by Noriaki Kano. This framework helps product managers understand how different features impact customer satisfaction emotionally, not just functionally, enabling teams to prioritize features that will truly delight customers.

## Step 0: Braindump & Product Sense (Do this first!)

**Before classifying features, braindump:**
- What features are you considering? List everything - don't categorize yet.
- What does your product sense tell you? Which features feel like table stakes vs. game-changers?
- What assumptions are you making about customer expectations? Are they truly basic needs or just loud requests?
- What biases might affect your categorization? (Status quo? Competitive copying? Squeaky wheel?)
- What would great product sense look like here? What would customers expect vs. what would make them say "wow"?

**Product sense exercise:**
- If you could only ship features that prevent dissatisfaction, which would they be? (These are likely must-haves)
- Which features would make customers choose you over competitors? (These might be performance or delighters)
- Which features would customers not even know to ask for? (These could be delighters)
- What would make you say "this categorization is obviously wrong"?

## Core Philosophy

### Customer Satisfaction is Emotional, Not Linear

The Kano model was revolutionary in the 1980s because it showed that customer satisfaction is emotional, not linear. Not all features impact satisfaction the same way - some must exist to prevent dissatisfaction, others create proportional satisfaction, and some create disproportionate delight.

The model should:

- **Reveal emotional impact** - Understand which features drive delight vs. prevent dissatisfaction
- **Guide balanced investment** - Allocate resources across feature types strategically
- **Enable differentiation** - Identify opportunities to exceed expectations
- **Inform MVP definition** - Clarify minimum viable vs. competitive vs. exceptional

### The Critical Understanding

Not all features are equal in the way they drive satisfaction, so they shouldn't be treated as equal on the outcome-based roadmap. Understanding feature categories helps teams:
- Invest appropriately in basics without over-engineering
- Create competitive advantage through performance features
- Differentiate through strategic delighters
- Avoid wasting resources on indifferent features

## The Five Categories

### Must-Have (Basic/Threshold Quality)

**Definition:** Requirements that customers expect and are taken for granted. When done well, customers are just neutral, but when done poorly, customers are very dissatisfied.

**Key characteristics:**
- Expected and assumed to exist
- Absence causes strong dissatisfaction
- Presence doesn't increase satisfaction
- Price of entry into market
- Often unspoken expectations

**Examples:**
- Banking app: Secure login, account balance display
- E-commerce: Shopping cart, checkout process
- Hotel: Clean room, working WiFi
- SaaS: Data security, uptime
- Car: Working brakes, functioning engine

**Strategic implications:**
- Must be present and working well
- Don't over-invest beyond "good enough"
- Monitor to prevent deterioration
- Baseline for product competitiveness

### Performance (One-Dimensional/Satisfiers)

**Definition:** Features where satisfaction scales linearly - customers will be satisfied when fulfilled and dissatisfied when not fulfilled.

**Key characteristics:**
- Spoken and explicitly requested
- "More is better" dynamic
- Direct correlation between quality and satisfaction
- Customers compare these across competitors
- Often form competitive battlefield

**Examples:**
- Banking app: Transaction speed, number of supported banks
- E-commerce: Shipping speed, number of payment options
- Hotel: Room size, breakfast variety
- SaaS: Processing speed, storage capacity, feature breadth
- Car: Fuel efficiency, trunk space

**Strategic implications:**
- Area for competitive differentiation
- Investment yields proportional returns
- Balance investment with ROI
- Monitor competitor performance levels
- Can become must-haves over time

### Attractive (Delighters/Exciters)

**Definition:** Features that create disproportionate satisfaction when present but don't cause dissatisfaction when absent - customers don't expect them.

**Key characteristics:**
- Unspoken and unexpected
- Create "wow" moments
- Absence doesn't disappoint
- Presence creates strong positive reaction
- Opportunity for differentiation

**Examples:**
- Banking app: AI-powered spending insights, personalized financial advice
- E-commerce: Surprise gift with order, unexpected free upgrade
- Hotel: Personalized welcome note, complimentary room upgrade
- SaaS: Smart feature recommendations, delightful animations
- Car: Heads-up display, advanced driver assistance

**Strategic implications:**
- Opportunity to exceed expectations
- High impact per resource investment
- Can create brand loyalty and advocacy
- Become performance features over time
- Select strategically - can't do everything

### Indifferent (Neutral)

**Definition:** Features that neither increase satisfaction nor cause dissatisfaction - customers don't care about them.

**Key characteristics:**
- No impact on customer perception
- Often internal technical considerations
- Customers unaware or unconcerned
- Resources better spent elsewhere
- May be necessary for other reasons (technical, regulatory)

**Examples:**
- Banking app: Specific encryption algorithm (customers care about security, not method)
- E-commerce: Backend inventory system architecture
- Hotel: Thickness of wax coating on disposable cups
- SaaS: Specific database technology used
- Technical implementation details invisible to users

**Strategic implications:**
- Minimize investment unless necessary
- Focus on cost efficiency if required
- Don't market these features
- May be important for operations but not satisfaction
- Redirect resources to impactful features

### Reverse (Dissatisfiers)

**Definition:** Features where presence actually decreases satisfaction - not all customers want everything.

**Key characteristics:**
- Causes dissatisfaction when present
- Different customer segments have different preferences
- Often "too much" of something
- Can indicate poor customer understanding
- Suggests feature should be optional or removed

**Examples:**
- Banking app: Overly complex features for basic users, excessive notifications
- E-commerce: Too many promotional emails, forced account creation
- Hotel: Overly attentive service for privacy-seeking guests
- SaaS: Overwhelming feature set for simple use cases
- Car: Too many screens and controls for minimalist buyers

**Strategic implications:**
- Identify and remove or make optional
- Understand customer segments - may be reverse for some, attractive for others
- Use for product tiering (basic vs. advanced)
- Can indicate over-engineering
- Listen to complaints about "too much"

## When to Use Kano

### Kano Works Best For:

- **Feature prioritization** when building product roadmap
- **MVP definition** to identify true must-haves vs. nice-to-haves
- **Competitive analysis** to understand where to differentiate
- **Customer research** to uncover unspoken expectations and delight opportunities
- **Stakeholder alignment** to justify feature decisions with data
- **Product strategy** to balance basics, performance, and delighters
- **Resource allocation** to invest appropriately across feature types

### Kano May Not Be Ideal For:

- **Very early discovery** before features are even conceptualized
- **B2B with few customers** where survey sample size is too small
- **Technical prioritization** where customer perception isn't primary driver
- **When you need objective scoring** across many similar features (use RICE instead)
- **Real-time tactical decisions** - Kano requires survey time
- **When categories are obvious** - may be overkill for simple products

## Step-by-Step Process

### 1. Identify Features to Evaluate (Pre-Work)

**Generate feature list:**
- Features from product backlog
- Customer requests from sales/support
- Competitive feature analysis
- Innovation brainstorms
- Technical team proposals

**Prepare features for survey:**
- Write clear, jargon-free descriptions
- Focus on customer-facing capabilities
- Avoid technical implementation details
- Ensure features are independent enough
- Keep list manageable (10-20 features ideal)

### 2. Design Kano Questionnaire

Kano proposes a standardized questionnaire where participants answer two questions for each product feature - one functional (formulated in a positive way) and one dysfunctional (formulated in a negative way).

**Functional question format:**
"If [feature] were present/available, how would you feel?"

**Dysfunctional question format:**
"If [feature] were NOT present/available, how would you feel?"

**Standard five-point response scale:**
1. I like it / I would enjoy it
2. I expect it / I must have it
3. I am neutral / I don't care
4. I can live with it / I can tolerate it
5. I dislike it / I would dislike it

**Questionnaire best practices:**
- Keep feature descriptions consistent between functional/dysfunctional
- Use neutral, non-leading language
- Randomize feature order to reduce bias
- Include attention check questions
- Keep survey under 20 minutes
- Provide context about product vision

**Example questions:**

**Feature: Real-time collaboration**
- Functional: "If our product allowed you to collaborate with teammates in real-time, how would you feel?"
- Dysfunctional: "If our product did NOT allow you to collaborate with teammates in real-time, how would you feel?"

**Feature: Dark mode**
- Functional: "If our product offered a dark mode theme, how would you feel?"
- Dysfunctional: "If our product did NOT offer a dark mode theme, how would you feel?"

### 3. Survey Your Customers

**Determine sample size:**
- Minimum: 20-30 responses per feature
- Ideal: 100+ responses for statistical confidence
- More needed for diverse customer segments
- Consider running pilot with 10-15 users first

**Select participants:**
- Target current customers who use product regularly
- Include potential customers/evaluators
- Ensure representation across customer segments
- Consider both power users and casual users
- Include churned customers for balanced view

**Distribution methods:**
- Email survey (scalable, cost-effective)
- In-app survey (higher response rate, engaged users)
- User interviews (qualitative insights, small sample)
- Customer advisory board sessions
- Usability testing combined with Kano questions

### 4. Analyze Results

**Step 4a: Categorize individual responses**

Use the Kano Evaluation Table to map each response pair to a category:

**Kano Evaluation Table:**

| | Dysfunctional: I like it | I expect it | I'm neutral | I can live with it | I dislike it |
|---|---|---|---|---|---|
| **Functional: I like it** | Questionable | Attractive | Attractive | Attractive | Performance |
| **I expect it** | Reverse | Indifferent | Indifferent | Indifferent | Must-Have |
| **I'm neutral** | Reverse | Indifferent | Indifferent | Indifferent | Must-Have |
| **I can live with it** | Reverse | Indifferent | Indifferent | Indifferent | Must-Have |
| **I dislike it** | Reverse | Reverse | Reverse | Reverse | Questionable |

**Example:**
- Functional response: "I like it"
- Dysfunctional response: "I dislike it"
- Result: **Performance feature**

**Step 4b: Aggregate across participants**

**Discrete analysis (most common):**
- Count frequency of each category for each feature
- Use mode (most frequent category) as primary classification
- Note secondary categories if close split

**Example results for "Real-time collaboration":**
- Must-Have: 45%
- Performance: 30%
- Attractive: 20%
- Indifferent: 5%
- **Classification: Must-Have** (modal category)

**Step 4c: Calculate satisfaction coefficients (optional)**

Satisfaction coefficients measure the impact on satisfaction and dissatisfaction. CS+ coefficient ranges from 0 to 1 (closer to 1 means higher satisfaction impact), while CS- coefficient ranges from 0 to -1 (closer to -1 means higher dissatisfaction if absent).

**Formulas:**
- **CS+ (Satisfaction)** = (Attractive + Performance) / (Attractive + Performance + Must-Have + Indifferent)
- **CS- (Dissatisfaction)** = -1 × (Must-Have + Performance) / (Attractive + Performance + Must-Have + Indifferent)

Higher absolute values indicate stronger impact on satisfaction or dissatisfaction.

### 5. Visualize and Interpret

**Create visualizations:**
- Stacked bar charts showing category distribution per feature
- Scatter plot with CS+ on Y-axis, CS- on X-axis
- Simple table with dominant category per feature

**Interpretation guidelines:**
- **Must-Haves (high |CS-|, low CS+):** Essential - address first
- **Performance (high CS+, high |CS-|):** Competitive differentiators
- **Attractive (high CS+, low |CS-|):** Delight opportunities
- **Indifferent (low CS+, low |CS-|):** Consider dropping
- **Mixed responses:** Segment analysis needed

**Watch for:**
- Features with split categorization (may need segmentation)
- Surprisingly high must-haves (validate with qualitative)
- Questionable responses (review question clarity)
- Reverse features (understand why)

### 6. Apply to Prioritization

**Prioritization strategy:**

**Phase 1: Must-Haves**
- Address all must-haves with high dissatisfaction scores
- Ensure these are "good enough" - don't over-invest
- Monitor continuously to prevent degradation

**Phase 2: High-Impact Performance**
- Invest in performance features with highest CS+ and strategic value
- Focus on areas where competitors are weak
- Balance investment with ROI

**Phase 3: Strategic Delighters**
- Select 1-3 attractive features that align with brand/strategy
- Choose those with highest CS+ and reasonable implementation cost
- Use for differentiation and brand building

**Phase 4: Defer or Drop**
- Defer indifferent features unless strategically necessary
- Remove or make optional reverse features
- Revisit in future as expectations evolve

### 7. Monitor Evolution Over Time

**Feature categories drift:**
What is a delighter today often becomes a performance expectation tomorrow and a basic requirement later on.

**Re-survey periodically:**
- Annually for stable markets
- Quarterly for fast-moving markets
- After major competitor launches
- When entering new market segments

**Watch for category drift:**
- Attractive → Performance (customers now expect it)
- Performance → Must-Have (baseline expectation)
- Track competitor feature launches
- Monitor support requests and complaints

## Common Pitfalls and Solutions

### Pitfall 1: Survey Fatigue and Low Quality Responses

**Warning signs:**
- High drop-off rates
- Inconsistent responses (Questionable category)
- Very fast completion times
- Straight-lining (same answer repeatedly)

**Solutions:**
- Keep surveys under 15-20 features
- Include attention checks
- Filter speeders in analysis
- Provide incentives for thoughtful completion
- Use clear, simple language
- Test questions with small group first

### Pitfall 2: Misinterpreting Results

**Warning signs:**
- Treating modal category as absolute
- Ignoring significant secondary categories
- Not understanding customer segments
- Overlooking satisfaction coefficients

**Solutions:**
- Review full distribution, not just mode
- Segment analysis for diverse customer bases
- Combine quantitative with qualitative insights
- Use satisfaction coefficients for nuanced view
- Validate surprising results with follow-up research

### Pitfall 3: Over-Reliance on Quantitative Data

Survey responses yield lots of categories and numbers, which are unlikely to illuminate why users feel the way they do. Qualitative research is still needed to understand users' true motivations.

**Warning signs:**
- Can't explain why feature is must-have
- Missing context behind categorization
- Unexpected results with no hypothesis
- Mechanical application without understanding

**Solutions:**
- Combine Kano with user interviews
- Follow up on surprising results
- Include open-ended questions in survey
- Use Kano to validate qualitative insights
- Don't treat Kano as sole input

### Pitfall 4: Ignoring Implementation Costs

**Warning signs:**
- Prioritizing all attractive features equally
- Not considering ROI
- Ignoring technical feasibility
- Building delighters before must-haves

**Solutions:**
- Weigh features according to two competing criteria: their potential to satisfy customers and the investment needed to implement them
- Use value vs. effort matrix alongside Kano
- Prioritize "low-hanging fruit" attractive features
- Balance quick wins with strategic bets
- Consider using RICE for detailed prioritization

### Pitfall 5: Static Categorization

**Warning signs:**
- Using years-old Kano data
- Ignoring market changes
- Not tracking category evolution
- Surprised by competitor moves

**Solutions:**
- Schedule regular re-surveys
- Monitor competitor feature launches
- Track support tickets for emerging must-haves
- Watch for social media feature requests
- Build category drift tracking into product ops

### Pitfall 6: Not Segmenting Customers

**Warning signs:**
- High distribution across all categories
- Reverse features in results
- Contradictory feedback
- One-size-fits-all approach

**Solutions:**
- Segment by user persona, use case, or company size
- Run separate analysis per segment
- Consider product tiers for different segments
- Make reverse features optional/configurable
- Understand that features can be attractive for some, reverse for others

## Integration with Other Frameworks

### Kano + MoSCoW

**How they complement:**
- Kano must-haves → MoSCoW must-haves
- Kano performance features → MoSCoW should-haves
- Kano attractive features → MoSCoW could-haves
- Use Kano to validate MoSCoW categorization

**When to use both:**
- Kano for customer-facing features
- MoSCoW for all requirements (including technical)
- Kano to inform MoSCoW decisions

### Kano + RICE

**How they complement:**
- Kano determines feature type
- RICE scores within each type
- Use Kano CS+ to inform RICE Impact score
- Prioritize high-RICE must-haves first, then high-RICE performance features

**Workflow:**
1. Run Kano to categorize features
2. Apply RICE within each category
3. Build roadmap prioritizing must-haves, then high-RICE performance and attractive features

### Kano + Value vs. Effort

**How they complement:**
- Kano identifies value type (satisfaction impact)
- Value vs. Effort identifies quick wins
- Focus on low-effort attractive features for quick differentiation
- Ensure all high-effort must-haves are truly necessary

**2x2 matrix with Kano overlay:**
- High Value + Low Effort: Prioritize attractive features here
- High Value + High Effort: Focus on must-haves and strategic performance features
- Low Value + Low Effort: Maybe - if attractive and brand-aligned
- Low Value + High Effort: Avoid unless must-have

### Kano + Roadmap

**Integration:**
- Must-haves in NOW section (high confidence)
- Performance features in NOW/NEXT based on strategic priority
- Attractive features in NEXT/LATER (lower confidence, innovation)
- Re-categorize as features drift from attractive → performance → must-have

**Roadmap communication:**
- "These must-haves prevent dissatisfaction"
- "These performance features drive competitive advantage"
- "These delighters exceed expectations and create loyalty"

## Best Practices

### Do's

- **Start with qualitative research** - Understand context before surveying
- **Keep surveys focused** - 10-20 features maximum
- **Use standard question format** - Functional and dysfunctional pairs with five-point scale
- **Sample broadly** - Include diverse customer segments
- **Combine with other methods** - Use Kano alongside RICE, MoSCoW, etc.
- **Invest strategically** - Don't over-invest in must-haves beyond "good enough"
- **Choose delighters wisely** - Select 1-3 strategic attractive features
- **Monitor category drift** - Re-survey periodically
- **Segment your analysis** - Different customers have different needs
- **Balance portfolio** - Include mix of must-haves, performance, and attractive features

### Don'ts

- **Don't survey without preparation** - Identify features and understand context first
- **Don't ignore qualitative insights** - Numbers alone don't explain why
- **Don't treat results as permanent** - Categories evolve over time
- **Don't build all attractive features** - Select strategically based on resources and brand
- **Don't over-engineer must-haves** - "Good enough" is sufficient
- **Don't ignore implementation costs** - Balance satisfaction impact with effort
- **Don't apply universally** - Segment analysis for diverse customer bases
- **Don't skip validation** - Verify surprising results with follow-up research
- **Don't use Kano as only input** - Combine with business strategy, technical feasibility, competitive analysis
- **Don't forget basics** - Must-haves must work flawlessly even if not exciting

## Metrics for Success

Track these metrics to evaluate Kano effectiveness:

### Process Metrics

- **Survey completion rate** - Target >30% for emails, >50% for in-app
- **Response quality** - Low questionable responses (<5%)
- **Segmentation coverage** - Representation across customer types
- **Time to analysis** - Days from survey close to actionable insights

### Outcome Metrics

- **Customer satisfaction** - NPS, CSAT improvement after implementing Kano-prioritized features
- **Feature adoption** - Usage rates of newly launched features
- **Competitive differentiation** - Win rates, customer feedback on unique features
- **Resource efficiency** - Reduced waste on indifferent features

### Learning Metrics

- **Category prediction accuracy** - Did features perform as categorized?
- **Evolution tracking** - How quickly do features drift across categories?
- **Segment differences** - How much do categories vary by customer type?
- **Surprising insights** - Features that didn't match assumptions

## Advanced Techniques

### Continuous Kano

Instead of one-time surveys, integrate Kano questions into:
- Post-feature launch surveys
- Quarterly product satisfaction surveys
- User interview scripts
- Beta testing feedback

### Kano for Different Stages

**Early stage (pre-product):**
- Focus on must-haves for MVP
- Validate assumptions about basics
- Identify potential delighters for differentiation

**Growth stage:**
- Balance must-haves, performance, and attractive
- Use for competitive positioning
- Monitor category evolution

**Mature stage:**
- Prevent feature bloat with indifferent identification
- Find new delighters as old ones become expected
- Segment for product tiering

### Predictive Kano

Use historical data to predict future drift:
- Track how long features stay in each category
- Identify patterns in competitive feature adoption
- Anticipate which attractive features will become must-haves
- Plan roadmap accordingly

---

## References

- Kano Template: `2-kano-template.md`
- Product Strategy: `../2.1.1-Product-Strategy/README.md`
- OKR Framework: `../2.1.2-OKR/README.md`
- PRD Framework: `../2.1.4-PRD/README.md`
- Prioritization: `../2.1.7-Prioritization/README.md`
- Roadmap Framework: `../2.1.3-Roadmap/README.md`
- MoSCoW Framework: `../2.1.8-MoSCoW-Prioritization/README.md`
- Self-Reflection: `../../2.9-Other/2.9.2-Self-Reflection/README.md`