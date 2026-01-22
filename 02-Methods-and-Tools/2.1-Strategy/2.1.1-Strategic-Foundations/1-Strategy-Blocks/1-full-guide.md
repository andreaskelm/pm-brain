# Product Strategy — Full Guide (Playbook)

## Before You Start - Prerequisites Checklist

**Essential Requirements:**
- [ ] Company mission/vision clearly defined and accessible
- [ ] Leadership commitment for 8-12 week process
- [ ] Access to user data, analytics, and research
- [ ] Working group availability (minimum 4 people × 2-4 hours/week during prep)
- [ ] Budget for potential user research gaps (optional but recommended)
- [ ] Calendar blocking for strategy sprint week (all working group members)

**Success Indicators:**
- Leadership expresses confusion about "why these projects" over "what to build"
- Team debates are unproductive or circular
- Clear disconnect between mission/vision and day-to-day roadmap decisions

---

## Basics for Newcomers

**Definition:** Strategy bridges mission/vision and plan (roadmap). It forces disciplined choices on where to focus (3–5 pillars), where not to focus (non-goals), and why these choices create maximum impact.

**Purpose:** Deploy scarce resources for maximum impact; reduce unproductive debates; clarify success measures and guardrails; align teams on "why these bets."

**Scope:** 
- **Small "s"**: 2-year present-forward strategy (solving current product problems)
- **Big "S"**: 3/5/10-year future-backward strategy (aspirational futures)

**Key Components of Good Strategy:**
1. **3-5 Strategic Pillars** (focus areas)
2. **Explicit Non-Goals** (what we won't do)
3. **Clear Rationale** (why these choices)
4. **Winning Aspiration** (2-year headline)
5. **Success Measures** (KPIs and guardrails)

---

## Roles & Responsibilities

### Core Strategy Working Group (Required)
- **Product Manager (Owner)**: Process facilitation, document writing, stakeholder alignment
- **Engineering Lead**: Technical constraints, feasibility assessment, implementation perspective
- **Design Lead**: User experience insights, concept illustration, design sprint leadership
- **Data Lead**: Behavioral analysis, metrics baseline, measurement framework

### Extended Team (Optional, based on resources)
- **Product Marketing**: Competitive analysis, market positioning
- **User Research**: Research synthesis, user observation coordination
- **Content Design**: Communication clarity, documentation support

### RACI Matrix
| Activity | PM | Eng Lead | Design Lead | Data Lead | PMM | UXR |
|----------|----|---------|-----------|---------|----|-----|
| Process Facilitation | R/A | C | C | C | C | C |
| Leadership Interviews | R | I | I | I | C | C |
| Data Analysis | C | I | I | R/A | I | C |
| UX Research Synthesis | C | I | R | I | I | A |
| Competitive Analysis | A | C | C | I | R | I |
| Strategy Sprint Facilitation | R/A | C | C | C | C | C |
| Document Writing | R/A | C | C | C | C | I |

**Legend**: R=Responsible, A=Accountable, C=Consulted, I=Informed

---

## Small "s" Strategy (2-year) — Five Steps

### Step 1: Preparation (3–5 weeks, part-time)

#### Week 1: Working Group Setup & Kickoff

**Kickoff Meeting Agenda (90 minutes):**
1. **Context Setting** (20 min): Why strategy now? Current challenges?
2. **Process Overview** (30 min): Walk through 5 steps, timelines, commitments
3. **Role Assignment** (20 min): Who owns what deliverable?
4. **Calendar Planning** (20 min): Book strategy sprint week, key milestones

**Action Items Assignment:**

#### Data Lead Responsibilities
**Deliverable:** Behavioral Insights Pack
**Timeline:** Week 2-4
**Content Requirements:**
- Meta-analysis of past behavioral studies and analytics
- User segment analysis (if available)
- Key usage patterns and pain points
- Performance metrics (reliability, latency, cost)
- Gaps requiring new analysis

**Quality Check:** Can a newcomer understand user behavior patterns from this document alone?

#### Design Lead Responsibilities  
**Deliverable:** UX Research Insights Synthesis
**Timeline:** Week 2-4
**Content Requirements:**
- Meta-analysis of qualitative and quantitative research
- Key user needs, frustrations, and unmet desires
- User journey pain points and moments of delight
- Research gaps and scrappy study recommendations

**Scrappy Studies (if needed):**
- 5-user interview protocol for critical gaps
- Guerrilla usability testing
- Survey to existing user base

#### PM + Working Group Responsibilities
**Deliverable:** Leadership Interview Notes
**Timeline:** Week 2-3 (aim for 2-3 interviews per week)

**Interview Protocol (45-60 minutes each):**

**Opening (5 min):** "We're developing product strategy and want to understand your perspective on success, challenges, and vision."

**Core Questions:**
1. **Success/Failure Vision (10 min)**
   - "What does wild success look like for us in 2 years?"
   - "What would failure look like? What keeps you up at night?"
   - *Follow-up*: "What specific behaviors would you see from users/customers?"

2. **Success Measures (10 min)**
   - "What are the most important metrics of success?"
   - "How would you know we're winning vs. competitors?"
   - *Follow-up*: "What leading indicators would give you confidence?"

3. **Guiding Principles (10 min)**
   - "What principles should guide our product decisions?"
   - "What should we never compromise on?"
   - *Follow-up*: "Can you give me an example of when this principle helped make a tough decision?"

4. **Learning from Past (10 min)**
   - "Why haven't things worked as expected in the past?"
   - "What patterns do you see in our misses vs. hits?"
   - *Follow-up*: "What would you do differently if you could go back?"

5. **Pet Ideas & Vision (10 min)**
   - "What ideas excite you that we should consider?"
   - "What's your most contrarian view about our space?"
   - *Follow-up*: "What would have to be true for that to work?"

**Closing (5 min):** "What questions should I have asked that I didn't?"

**Interview Notes Template:**
```
Leader: [Name, Role]
Date: [Date]
Key Quotes: [Verbatim important statements]
Success Definition: [Their vision of success]
Failure Concerns: [Their biggest worries]
Success Metrics: [How they'd measure progress]
Principles: [Decision-making guidelines]
Past Learnings: [Why things didn't work before]
Pet Ideas: [Their favorite concepts/directions]
Surprises: [Unexpected insights]
```

#### PM or PMM Responsibilities
**Deliverable:** Competitive & Comparables Analysis
**Timeline:** Week 3-4

**Analysis Framework:**

**Competitive Heatmap:**
| Capability | Us | Competitor A | Competitor B | Comparable X | Evaluation Criteria |
|------------|----|--------------|--------------|--------------|--------------------|
| Core Feature Set | 🟡 | 🟢 | 🔴 | 🟢 | Breadth, depth, ease of use |
| User Experience | 🟢 | 🟡 | 🟡 | 🟢 | Intuitive, delightful, accessible |
| Technical Performance | 🟡 | 🟢 | 🔴 | 🟡 | Speed, reliability, scalability |
| Pricing/Value Prop | 🟢 | 🟡 | 🟢 | 🔴 | Cost effectiveness, clear value |

**Legend:** 🟢 Strong, 🟡 Adequate, 🔴 Weak

**Required Analysis Components:**
1. **Feature Comparison Matrix**: Side-by-side capability analysis
2. **Investment Themes**: Where is each competitor focusing their R&D?
3. **Positioning Analysis**: How does each player talk about the problem space?
4. **Feature Deconstructs**: Screenshots and workflows of key differentiators
5. **Roadmap Intelligence**: Public statements about future direction

**Summary Narrative Requirements:**
- **Where NOT to compete**: Areas where others have insurmountable advantages
- **Where WE differentiate**: Our unique strengths and moats
- **White Space Opportunities**: Unmet needs no one is addressing well

#### All Working Group Members
**Deliverable:** User Observation Notes
**Timeline:** Week 3-4
**Requirement:** Each member conducts 1-3 user interviews or observes user sessions

**Purpose:** Build empathy, ground strategy in human needs (not just data)

**Simple Protocol:**
- Ask users to show you how they currently solve the problem your product addresses
- Focus on frustrations, workarounds, and moments of confusion
- Note emotional reactions and language they use
- Don't sell or explain your product—just observe and learn

#### PM + Engineering Lead
**Deliverable:** Constraints & Guardrails Assessment
**Timeline:** Week 4

**Categories to Evaluate:**
1. **Technical Constraints**: Platform limitations, technical debt, performance requirements
2. **Resource Constraints**: Team capacity, budget limitations, skill gaps
3. **Compliance Requirements**: Legal, regulatory, security mandates
4. **Business Constraints**: Brand guidelines, partnership agreements, company priorities
5. **User Experience Guardrails**: Accessibility standards, usability principles

**Output Format:**
```
Constraint Type: [Technical/Resource/Compliance/Business/UX]
Description: [Clear explanation of limitation]
Impact Level: [High/Medium/Low]
Flexibility: [Fixed/Some flexibility/Negotiable]
Workaround Options: [Alternative approaches if any]
```

#### All Team Members
**Deliverable:** Baseline Metrics Collection
**Timeline:** Week 4

**Categories:**
- **Usage Metrics**: DAU, MAU, feature adoption, session length
- **Business Metrics**: Revenue, conversion rates, customer acquisition cost
- **Experience Metrics**: NPS, satisfaction scores, support ticket volume
- **Technical Metrics**: Performance, reliability, error rates

**Quality Check:** Do we have clear baselines to measure strategy impact against?

---

### Step 2: Strategy Sprint (1 week)

**Prerequisites:** 
- All preparation deliverables completed
- Full working group available for 3 days
- Conference room booked with wall space for sticky notes
- Materials: Sticky notes, markers, flip chart paper, voting dots

#### Day 1: Share-outs & Problem Identification

**Morning Session (9 AM - 12 PM): Comprehensive Share-outs**

**Agenda:**
- **9:00-9:30**: Behavioral insights presentation
- **9:30-10:00**: UX research synthesis presentation  
- **10:00-10:15**: Break
- **10:15-10:45**: Leadership interview themes
- **10:45-11:15**: Competitive analysis presentation
- **11:15-11:45**: Constraints & baseline metrics
- **11:45-12:00**: Initial reactions and clarifying questions

**Facilitation Notes:**
- Keep presentations to bullets and key insights—substance over polish
- Encourage questions but defer debate to afternoon
- Each presenter should highlight their top 3 most surprising findings

**Afternoon Session (1 PM - 5 PM): Problem Identification**

**Process:**
1. **Individual Problem Brainstorm (1:00-2:30 PM)**
   - Each person writes problems on sticky notes (one problem per note)
   - Problems should be specific user or business problems, not solutions
   - Focus on problems that prevent product growth or user success
   - Aim for 15-30 problems per person

2. **Problem Sharing (2:30-3:30 PM)**
   - Each person presents their problems (1 minute per problem max)
   - Post all sticky notes on wall
   - No debate—just clarifying questions

3. **Break (3:30-3:45 PM)**

4. **Initial Clustering (3:45-5:00 PM)**
   - Group similar problems together
   - Give each cluster a descriptive name
   - Aim for 10-15 clusters
   - Don't worry about perfect categorization—rough groupings are fine

**End of Day Output:** 50-150 problem statements clustered into 10-15 themes

**Example Problem Statements:**
- "Users can't find the advanced features they need"
- "New users abandon during onboarding at step 3"
- "Enterprise customers can't integrate with their existing tools"
- "Support team spends 60% of time on preventable issues"
- "Competitors are winning deals on price, not features"

#### Day 2: Strategy Selection (Most Critical Day)

**Morning Session (9 AM - 12 PM): Opportunity Framing & Scoring**

**9:00-10:00 AM: Refine Problem Clusters**
- Review yesterday's clusters with fresh eyes
- Merge overlapping clusters, split overly broad ones
- Finalize cluster names and descriptions
- Target: 8-12 opportunity areas

**10:00-10:15 AM: Break**

**10:15-11:15 AM: Flip Problems to Opportunities**
Each cluster becomes an opportunity area:
- "Users can't find features" → "Discovery & Findability"
- "New user abandonment" → "Onboarding & Activation" 
- "Enterprise integration gaps" → "Platform & Extensibility"

**11:15 AM-12:00 PM: Scoring Framework Review**

**The 4 Scoring Dimensions (1-5 scale each):**

1. **Expected Impact (1-5)**
   - 5: Affects majority of users frequently with high pain/value
   - 4: Affects many users regularly with moderate-high pain/value  
   - 3: Affects some users regularly OR many users occasionally
   - 2: Affects some users occasionally with moderate pain/value
   - 1: Affects few users infrequently with low pain/value

2. **Certainty of Impact (1-5)**
   - 5: Strong evidence from multiple sources (data + research + user feedback)
   - 4: Good evidence from 2+ sources with some validation
   - 3: Moderate evidence from 1-2 sources 
   - 2: Limited evidence but logical hypothesis
   - 1: Speculative with minimal supporting evidence

3. **Clarity of Levers (1-5)**
   - 5: Very clear what actions/features would address this
   - 4: Generally clear with a few different promising approaches
   - 3: Some ideas but need experimentation to find right approach
   - 2: Directionally right but unclear on specific actions
   - 1: Problem is clear but solutions are very uncertain

4. **Uniqueness of Levers (1-5)** ⭐ *Often missed but critical*
   - 5: Strong unique advantages (brand, data, technology, partnerships)
   - 4: Some unique advantages that provide differentiation
   - 3: Can differentiate through execution but not structurally unique
   - 2: Slight advantages but mostly playing on level field
   - 1: No clear advantages—would be playing catch-up

**Afternoon Session (1 PM - 5 PM): Scoring & Selection**

**1:00-3:00 PM: Individual Scoring**
- Each working group member scores each opportunity area on all 4 dimensions
- Use provided scoring rubric and evidence from preparation phase
- No discussion during individual scoring

**3:00-3:15 PM: Break**

**3:15-4:30 PM: Group Discussion & Consensus Scoring**
- Share individual scores and discuss significant differences
- For each opportunity area, reach consensus on each dimension
- Document key evidence/reasoning behind scores
- Calculate total scores (simple sum: 4-20 points possible)

**4:30-5:00 PM: Pillar Selection**
- Rank opportunity areas by total score
- Top 3-5 become strategic pillars
- Quick sanity check: Do these feel right as a portfolio?
- Name each pillar with a compelling, memorable title

**Scoring Template:**
| Opportunity Area | Expected Impact | Certainty | Clarity of Levers | Uniqueness | Total | Evidence Notes |
|------------------|------------------|-----------|-------------------|------------|-------|----------------|
| Discovery & Findability | 4 | 3 | 4 | 2 | 13 | High user pain (research), unclear differentiation |
| Onboarding & Activation | 5 | 4 | 3 | 3 | 15 | Clear business impact, some unique data advantages |

#### Day 3: Winning Aspiration & Pillar Development

**Morning Session (9 AM - 12 PM): Winning Aspiration Creation**

**9:00-9:15 AM: Creative Exercise Setup**
"Imagine it's 2 years from now. We've made significant progress on all our strategic pillars. A journalist is writing a story about our success. What's the headline?"

**9:15-10:00 AM: Individual Headline Creation**
Each person writes 3-5 potential headlines focusing on:
- How users' lives are better
- How the business has grown  
- What makes this remarkable/noteworthy

**10:00-10:15 AM: Break**

**10:15-11:15 AM: Headline Sharing & Synthesis**
- Share all headlines (no judgment)
- Identify common themes and powerful language
- Look for elements that capture both user value and business success
- Blend best elements into 2-3 candidate aspirations

**11:15 AM-12:00 PM: Final Aspiration Selection**
- Test each candidate: Does it inspire? Is it believable? Does it connect to our pillars?
- Select final 2-year winning aspiration
- Refine language for clarity and impact

**Example Winning Aspirations:**
- "TechCorp becomes the platform teams choose first for rapid product development, with 90% of users activating core features within their first week"
- "EduApp transforms from a content library to the primary workspace where teachers plan, deliver, and assess student learning across 10,000+ schools"

**Afternoon Session (1 PM - 5 PM): Pillar Development**

**For Each Strategic Pillar:**

**1:00-2:30 PM: "How Might We" Generation**
For each pillar, generate 3-5 "How Might We" statements:
- "How might we make advanced features more discoverable?"
- "How might we reduce cognitive load during onboarding?"  
- "How might we turn feature discovery into a delightful experience?"

**2:30-2:45 PM: Break**

**2:45-4:00 PM: Success Metrics Brainstorm**
For each pillar, identify:
- **Primary Metrics**: Direct measures of pillar success
- **Secondary Metrics**: Supporting indicators
- **Guardrail Metrics**: What we can't break while improving primary metrics

**4:00-5:00 PM: Risk & Assumption Documentation**
For each pillar, capture:
- **Key Assumptions**: What has to be true for this to work?
- **Biggest Risks**: What could prevent success?
- **Early Tests**: How could we validate assumptions quickly?

**End of Day Output:**
- 3-5 strategic pillars with scores and rationale
- 2-year winning aspiration  
- "How Might We" statements for each pillar
- Initial success metrics and guardrails
- Key risks and assumptions per pillar

---

### Step 3: Design Sprint (1 week)

**Goal:** Create illustrative concepts that make each strategic pillar tangible and understandable

**Inputs:** Strategic pillars, "How Might We" statements, winning aspiration

**Team:** Design lead facilitates, full working group participates

#### Pre-Sprint Preparation (Design Lead)
- Choose design sprint methodology (recommend modified Google Ventures approach)
- Prepare concept sketching materials
- Set up workspace with wall space for posting concepts
- Brief team on "illustrative concepts" vs "build-ready specs" distinction

#### Day-by-Day Design Sprint Structure

**Day 1: Alignment & Divergent Ideation**
- Morning: Review strategic pillars and HMW statements
- Afternoon: Individual concept sketching for each pillar

**Day 2: Concept Development** 
- Morning: Refine and develop most promising concepts
- Afternoon: Create simple storyboards or user journey maps

**Day 3: Concept Articulation**
- Morning: Create before/after scenarios showing pillar impact
- Afternoon: Develop low-fidelity mockups or system diagrams

**Day 4-5: Artifact Creation**
- Refine concepts into presentable artifacts
- Prepare concept narrative for each pillar
- Create readout presentation

**Design Sprint Outputs:**
- 1-2 illustrative concepts per strategic pillar
- Before/after user journey comparisons  
- Low-fidelity mockups or system sketches
- Concept narratives explaining how each pillar comes to life

**Quality Check:** Can someone unfamiliar with your strategy process understand what each pillar means by looking at the concepts?

---

### Step 4: Document Writing (1–2 weeks)

**Owner:** Product Manager (primarily solo work)

**Writing Approach:** Combine all inputs into coherent narrative that tells the complete strategy story

#### Document Structure & Content Guidelines

**1. Executive Summary (1 page)**
- Context: Why strategy now?
- Pillars: 3-5 focus areas in 1-2 sentences each
- Aspiration: Our 2-year winning vision
- Bottom line: What this means for the business

**2. Context / Why Now (1-2 pages)**
- Current situation assessment
- Key challenges and opportunities identified
- Why these choices make sense at this moment
- Connection to company mission/vision

**3. Strategic Pillars (2-3 pages per pillar)**

**For Each Pillar:**
- **Definition**: What this pillar means
- **Rationale**: Why this is strategically important (evidence from prep phase)
- **Success Vision**: What good looks like in 2 years
- **Illustrative Concepts**: How this might come to life (design sprint outputs)
- **Key Metrics**: How we'll measure progress
- **Major Risks**: What could prevent success

**4. Non-Goals (1 page)**
- Explicit areas we will NOT focus on
- Rationale for each non-goal
- What we'll stop/deprioritize to focus on pillars

**5. 2-Year Winning Aspiration (0.5 pages)**
- Our inspirational 2-year vision
- Connection to how this advances company mission
- Success metrics that would validate aspiration

**6. Success Measurement (1 page)**
- Key metrics definitions and current baselines
- Success targets where possible
- Measurement cadence and review process
- Dashboard/reporting approach

**7. Dependencies & Risks (1 page)**  
- Critical dependencies on other teams/functions
- Technology or resource dependencies
- Major risks and mitigation strategies
- Key assumptions that need validation

**8. Guardrails & Principles (0.5 pages)**
- Decision-making principles
- What we won't compromise on
- Quality and experience standards

**9. Next Steps & Decision Criteria (0.5 pages)**
- Immediate next steps post-strategy approval  
- How we'll make prioritization decisions within pillars
- Roadmap planning approach

**Appendix: Evidence Base**
- Links to all preparation phase deliverables
- Leadership interview summary themes
- Competitive analysis details
- User research insights
- Data analysis findings

#### Writing Quality Checks

**Clarity Test:** Can someone unfamiliar with the process understand:
- Why these pillars were chosen?
- What success looks like?
- How this connects to business objectives?

**Defensibility Test:** For each pillar:
- Is the rationale clear and evidence-based?
- Would a skeptical stakeholder be convinced?
- Are the tradeoffs explicitly acknowledged?

**Actionability Test:**
- Can teams build roadmaps from this strategy?
- Are the success metrics measurable?
- Is it clear what we're NOT doing?

---

### Step 5: Rollout (2–3 weeks)

**Goal:** Secure alignment and operationalize strategy across organization

#### Week 1: Gatekeeper Alignment

**Gatekeeper Identification:**
- CEO/Founders (always)
- Direct manager/VP of Product
- Key functional leaders (Engineering, Design, Data)
- Major customer stakeholders (Sales, Customer Success for B2B)

**1:1 Review Process:**
- **Pre-meeting**: Send strategy document 2 days in advance
- **Meeting Duration**: 60-90 minutes per gatekeeper
- **Agenda**: 
  - 15 min: Context and process overview
  - 30 min: Walk through pillars and rationale
  - 30 min: Discussion, concerns, adjustments
  - 15 min: Next steps and expectations

**Common Gatekeeper Concerns & Responses:**
- **"These pillars feel too broad/narrow"** → Show scoring rationale and evidence
- **"What about [pet project]?"** → Explain how it fits (or doesn't) within pillars or non-goals
- **"Timeline feels aggressive"** → Walk through capacity planning and dependency analysis
- **"How do we know this will work?"** → Share measurement plan and early validation approach

**Adjustment Guidelines:**
- **Minor language/framing changes**: Acceptable and expected
- **Pillar priority ordering**: Can adjust based on compelling new information
- **Major pillar changes**: Requires strong evidence and working group reconvening
- **New pillar additions**: Generally avoid—dilutes focus

#### Week 2: Group Review & Stakeholder Alignment

**Stakeholder Group Review Meeting (2 hours):**

**Attendees:**
- All gatekeepers
- Functional leaders (Engineering, Design, Data, Marketing, etc.)
- Adjacent team leads whose work intersects
- Key IC representatives from implementation teams

**Meeting Structure:**
- **20 min**: Strategy overview and process recap
- **60 min**: Deep dive into pillars (15 min each for 4 pillars)
- **20 min**: Non-goals discussion and clarification
- **15 min**: Measurement and success criteria  
- **15 min**: Next steps and timeline
- **10 min**: Final questions and concerns

**Facilitation Notes:**
- Focus on clarification, not re-debating pillar selection
- Document action items and concerns for follow-up
- Aim for explicit commitment: "Can you support this direction?"

#### Week 3: Team Roadshows & Operationalization

**Team Roadshow Format:**
- **Group Size**: 8-10 people maximum per session
- **Duration**: 60 minutes  
- **Sessions Needed**: Typically 3-5 sessions to cover all teams

**Roadshow Agenda:**
- **10 min**: Why we did strategy work now
- **25 min**: Pillar walkthrough with Q&A
- **15 min**: What this means for day-to-day work
- **10 min**: How to use strategy for decision-making

**Feedback Collection:**
- **Clarity Check**: What's confusing or unclear?
- **Practical Questions**: How does this affect my current projects?
- **Missing Pieces**: What important context is missing?

**Operationalization Tasks:**

**1. OKR Mapping:**
- Map each strategic pillar to relevant OKRs  
- Ensure Key Results align with pillar success metrics
- Update OKR documentation with pillar references

**2. Roadmap Seeding:**
- Identify current roadmap items that support each pillar
- Flag items that don't clearly connect to any pillar
- Begin discovery planning for pillar-supporting initiatives

**3. Communication Plan:**
- Monthly newsletter updates on strategy progress
- Quarterly strategy review meetings
- Strategy document publication (internal wiki/docs)

**4. Decision Framework:**
- Create simple template: "How does this support our strategic pillars?"
- Train teams on using strategy for prioritization decisions
- Establish escalation process for off-strategy requests

#### Rollout Success Metrics

**Alignment Indicators:**
- All gatekeepers explicitly commit to strategy direction
- No fundamental disagreements on pillar selection  
- Teams can articulate how their work connects to pillars

**Operationalization Indicators:**
- OKRs clearly map to strategic pillars
- Project requests reference pillar alignment
- Teams use strategy document for prioritization decisions

---

## Big "S" Strategy (3/5/10-year) — Five Steps

*[Big S strategy section would continue with similar level of detail...]*

**Note:** Big "S" strategy is typically led by senior design leadership and takes 4-6 months. This is complementary to small "s" strategy and focuses on aspirational futures rather than current product problems.

---

## Workshop Kits & Templates

### Enhanced Pillar Scorecard

| Pillar | Expected Impact (1-5) | Certainty of Impact (1-5) | Clarity of Levers (1-5) | Uniqueness of Levers (1-5) | Total Score | Evidence Summary |
|--------|------------------------|----------------------------|--------------------------|------------------------------|-------------|------------------|
| Example: Discovery | 4 | 3 | 4 | 2 | 13 | High user pain in research, feature usage data shows discovery issues, but limited competitive differentiation |

**Scoring Rubric:**
- **Expected Impact**: Consider user base size affected × frequency of issue × severity of pain/value
- **Certainty of Impact**: Strength and diversity of supporting evidence  
- **Clarity of Levers**: How clear the solution approaches are
- **Uniqueness of Levers**: Competitive advantages that enable differentiation

---

## Anti-Patterns & Common Pitfalls

**Strategy Selection Anti-Patterns:**
- ❌ **Function-shaped pillars**: "Improve mobile experience" 
- ✅ **Choice-shaped pillars**: "Enable discovery of advanced features"

- ❌ **Pillars without rationale**: Just listing focus areas
- ✅ **Evidence-based pillars**: Clear scoring and supporting data

- ❌ **No explicit non-goals**: Everything feels like priority
- ✅ **Clear non-goals**: Explicit choices about what not to focus on

**Process Anti-Patterns:**
- ❌ **Skipping user observation**: Strategy becomes abstract
- ✅ **Grounding in user reality**: Direct exposure to user problems

- ❌ **No visual communication**: Strategy document is text-heavy
- ✅ **Illustrated concepts**: Design sprint makes pillars tangible

- ❌ **Poor stakeholder sequencing**: Surprising gatekeepers
- ✅ **Structured rollout**: 1:1s → group review → team roadshows

**Measurement Anti-Patterns:**
- ❌ **Vanity metrics focus**: Measuring activity vs. outcomes
- ✅ **Impact-focused metrics**: Measuring user and business value

- ❌ **No baseline measurement**: Can't track progress
- ✅ **Clear baselines**: Know where you're starting from

---

## [Company]-Specific Integration

**Traceability Requirements:**
- Map pillars → OKR Objective and Key Result IDs
- Link to company strategy document: `../../01-Company-Context/2-company-strategy.md`
- Include pillar progress in monthly newsletters
- Connect to quarterly business reviews

**Communication Channels:**
- Strategy announcements via monthly newsletters
- Progress updates in all-hands meetings
- Detailed documentation in internal wiki
- OKR dashboards show pillar-level progress

**Decision Integration:**
- Use pillar alignment as project approval criteria
- Reference strategy in resource allocation discussions
- Include strategy context in quarterly planning

---

## Quality Assurance Checklist

**Before Strategy Sprint:**
- [ ] All preparation deliverables completed and reviewed
- [ ] Working group familiar with scoring framework
- [ ] Leadership interviews captured key insights
- [ ] User observation provided empathy grounding

**After Strategy Sprint:**
- [ ] 3-5 strategic pillars with clear rationale
- [ ] Explicit non-goals defined
- [ ] 2-year winning aspiration inspires and focuses
- [ ] Success metrics identified for each pillar

**Before Document Writing:**
- [ ] Design sprint produced illustrative concepts
- [ ] All evidence gathered and organized
- [ ] Key stakeholder feedback incorporated

**Before Rollout:**
- [ ] Strategy document is clear and compelling
- [ ] Gatekeeper list identified and prioritized
- [ ] Team communication plan prepared
- [ ] Operationalization approach defined

Workshop kits (see templates)
- Pillar scorecard (ICT)  • Leadership interview guide  • Competitive heatmap
- Design sprint brief  • Strategy document template  • Rollout plan

Diagrams (SVG)
- Pillars → plan: `./assets/pillars-to-plan.svg`
- Small “s” vs Big “S”: `./assets/smallS-vs-bigS.svg`
- Rollout flow: `./assets/rollout-flow.svg`

Source: https://www.lennysnewsletter.com/p/strategy-blocks-an-operators-guide
