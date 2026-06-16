# Crisis Management Framework

## Overview

This framework helps product teams and organizations prepare for, respond to, and recover from crises. Crisis management is NOT about preventing all problems—it's about responding effectively when the unexpected happens.

## Step 0: Braindump & Assess (Critical!)

**Use prompts from:** [system/coaching/prompts.md](../../../system/coaching/prompts.md) → [When Something Goes Wrong (Crisis / Incident)](../../../system/coaching/prompts.md#when-something-goes-wrong-crisis--incident). Quick start: What's happening → How serious → What assumptions → What don't you know → What biases → **See prompts file for full list.**

**Product sense exercise:**
- If this were happening to a competitor, how would you assess it?
- What would make you say "this is obviously a crisis"?
- What would make you say "this is just an incident"?

## Core Philosophy

### Crises are NOT Predictable

Effective crisis management should:

- **Enable rapid response over perfect planning** - Act decisively with imperfect information
- **Foster resilience over prevention** - Bounce back quickly when things go wrong
- **Drive learning over blame** - Improve systems, don’t punish people
- **Create clarity over chaos** - Provide structure when everything feels uncertain

### Understanding Crisis vs. Incident

**INCIDENT (Operational Issue)**

- Routine operational problem
- Handled by standard procedures
- Limited scope and impact
- Tactical response by operational teams

**CRISIS (Existential Threat)**

- Unexpected, high-impact event
- Threatens organization’s reputation or viability
- Wide-reaching consequences
- Strategic response by leadership

**Key Difference:** A crisis requires a whole-of-organization response and poses an existential threat to reputation, operations, or viability.

-----

## 📌 Crisis Definition

**A crisis is:**

> An event with low probability of occurring but, if it does occur, has vastly negative impact on the organization. It threatens strategic objectives, reputation, and viability, and requires immediate response.

**Examples of Crises:**

- Major security breach exposing customer data
- Product defect causing harm or death
- Key leader misconduct/scandal
- Natural disaster disrupting operations
- Regulatory violation with legal consequences
- Major service outage affecting millions
- Supply chain collapse
- Public relations disaster going viral
- Financial fraud or bankruptcy threat

**Examples of Incidents (NOT Crises):**

- Bug affecting small user segment
- Brief service degradation (under 1 hour)
- Single customer complaint
- Minor security vulnerability
- Routine production issue

-----

## 📌 Crisis Management Framework Structure

### 1. Five Phases of Crisis Management

**Phase 1: ANTICIPATE** (Pre-Crisis)

- Identify potential threats
- Assess likelihood and impact
- Monitor warning signals

**Phase 2: PREPARE** (Pre-Crisis)

- Develop response plans
- Train crisis management team
- Conduct drills and simulations

**Phase 3: RESPOND** (During Crisis)

- Activate crisis management plan
- Make rapid decisions
- Execute response actions

**Phase 4: RECOVER** (Post-Crisis)

- Restore normal operations
- Implement business continuity
- Support affected stakeholders

**Phase 5: LEARN** (Post-Crisis)

- Conduct post-mortem analysis
- Document lessons learned
- Update plans and procedures

-----

## 📌 Crisis Severity Levels

### Level 1: Minor Crisis (Yellow)

**Impact:** Single team/product, limited customer impact
**Response Time:** Within 4 hours
**Leadership:** Product/Team Lead
**Example:** Feature bug affecting 5% of users

**Response:**

- Product team handles with standard escalation
- Regular stakeholder updates
- Fix and monitor

-----

### Level 2: Major Crisis (Orange)

**Impact:** Multiple teams, significant customer impact
**Response Time:** Within 1 hour
**Leadership:** VP Product/Engineering
**Example:** Service degradation affecting 25% of users for 2+ hours

**Response:**

- Assemble incident response team
- Hourly executive updates
- Customer communication plan
- All-hands-on-deck until resolved

-----

### Level 3: Severe Crisis (Red)

**Impact:** Company-wide, existential threat
**Response Time:** Immediate (minutes)
**Leadership:** CEO + Crisis Management Team
**Example:** Major data breach, safety incident, public scandal

**Response:**

- Activate full Crisis Management Team (CMT)
- Establish command center
- Legal, PR, communications activated
- Board notification
- Potential media/regulatory response

-----

## 📌 Crisis Management Team (CMT)

### Core Roles

**Crisis Manager (Usually CEO or COO)**

- Final decision authority
- Owns overall response
- Interfaces with board

**Crisis Coordinator (Usually Chief of Staff)**

- Coordinates all crisis activities
- Manages command center
- Tracks action items
- Facilitates communication

**Technical Lead (CTO or VP Engineering)**

- Assesses technical impact
- Coordinates technical response
- Provides technical guidance

**Communications Lead (VP Communications)**

- Internal and external messaging
- Media relations
- Stakeholder communications

**Legal Counsel (General Counsel)**

- Legal implications
- Regulatory compliance
- Liability assessment

**People Lead (VP HR)**

- Employee communications
- Workforce impact
- Safety and wellbeing

### Specialist Teams (Activated as Needed)

**Incident Response Team**

- Technical resolution
- System recovery
- Root cause analysis

**Customer Response Team**

- Customer support surge
- Customer communications
- Impact assessment

**Business Continuity Team**

- Operations continuity
- Alternative processes
- Vendor management

-----

## 📌 Crisis Management Plan Template

```
├──
CRISIS MANAGEMENT PLAN
├──

Version: [X.X]
Last Updated: [Date]
Next Review: [Date]
Owner: [Name, Role]

├──
SECTION 1: CRISIS IDENTIFICATION
├──

CRISIS DEFINITION:
An event is a crisis if it meets 2+ of these criteria:
→ Threatens organizational reputation
→ Disrupts critical business operations
→ Poses safety risk to employees/customers
→ Has significant financial impact (>$X)
→ Requires immediate executive decisions
→ May result in regulatory/legal consequences
→ Generates significant negative media attention

SEVERITY ASSESSMENT:
• Level 1 (Yellow): [Define criteria]
• Level 2 (Orange): [Define criteria]
• Level 3 (Red): [Define criteria]

├──
SECTION 2: CRISIS MANAGEMENT TEAM
├──

CORE TEAM (Always Activated):

Crisis Manager: [Name]
• Primary: [Name, phone, email]
• Backup: [Name, phone, email]
• Responsibilities: Final decisions, board communication

Crisis Coordinator: [Name]
• Primary: [Name, phone, email]
• Backup: [Name, phone, email]
• Responsibilities: Coordinate response, track actions

Technical Lead: [Name]
• Primary: [Name, phone, email]
• Backup: [Name, phone, email]
• Responsibilities: Technical assessment and resolution

Communications Lead: [Name]
• Primary: [Name, phone, email]
• Backup: [Name, phone, email]
• Responsibilities: All internal/external communications

Legal Counsel: [Name]
• Primary: [Name, phone, email]
• Backup: [Name, phone, email]
• Responsibilities: Legal guidance, regulatory

People Lead: [Name]
• Primary: [Name, phone, email]
• Backup: [Name, phone, email]
• Responsibilities: Employee impact and communications

EXTENDED TEAM (Activated as Needed):
• Security Lead: [Name, contact]
• Finance Lead: [Name, contact]
• Operations Lead: [Name, contact]
• Customer Success Lead: [Name, contact]

ESCALATION PATH:
1. Incident detected → Incident Response Team
2. Meets crisis criteria → Notify Crisis Coordinator
3. Crisis Coordinator assesses → Activate CMT
4. Crisis Manager convenes → Execute response

├──
SECTION 3: COMMUNICATION PROTOCOLS
├──

CRISIS COMMUNICATION CHANNELS:

Primary: [Slack channel #crisis-response]
Backup: [Phone bridge: XXX-XXX-XXXX, PIN: XXXX]
Command Center: [Physical location / Zoom room]

NOTIFICATION SEQUENCE (Within 15 minutes):
1. Crisis Coordinator → Crisis Manager
2. Crisis Manager → Core CMT members
3. Crisis Coordinator → Extended team as needed
4. Communications Lead → Prepare stakeholder communication

INTERNAL COMMUNICATIONS:
• All-hands: [How/when to communicate to employees]
• Department heads: [Update frequency]
• Board: [Who communicates, when]

EXTERNAL COMMUNICATIONS:
• Customers: [Email, in-app, status page]
• Media: [Spokesperson, holding statements]
• Regulators: [Legal counsel coordinates]
• Partners: [Account management coordinates]

COMMUNICATION PRINCIPLES:
• Be fast: First communication within 1 hour
• Be factual: Only communicate confirmed information
• Be transparent: Acknowledge what you don't know
• Be empathetic: Show concern for those affected
• Be consistent: Single source of truth

├──
SECTION 4: RESPONSE PROCEDURES
├──

IMMEDIATE ACTIONS (First 30 Minutes):

→ Assess severity using criteria
→ Notify Crisis Coordinator
→ Activate appropriate CMT members
→ Establish command center
→ Begin situation log (who, what, when)
→ Identify immediate safety concerns
→ Initiate technical response if applicable

FIRST HOUR ACTIONS:

→ CMT convenes (in-person or virtual)
→ Situation assessment complete
→ Initial decisions documented
→ Internal notification sent (employees)
→ External notification prepared (if applicable)
→ Action plan created with owners
→ Resource needs identified
→ Regular update cadence established

ONGOING RESPONSE:

→ Execute action plan
→ Regular CMT updates (every 2-4 hours)
→ Update situation log continuously
→ Monitor media/social sentiment
→ Adjust response based on developments
→ Document all decisions and rationale
→ Maintain stakeholder communications

RESOLUTION CRITERIA:

→ Immediate threat neutralized
→ Systems/operations stable
→ Customer impact mitigated
→ No additional escalation needed
→ Transition to recovery phase approved

├──
SECTION 5: CRISIS-SPECIFIC PLAYBOOKS
├──

Each crisis type has a specific playbook:

1. SECURITY BREACH / DATA EXPOSURE
→ See Appendix A

2. MAJOR SERVICE OUTAGE
→ See Appendix B

3. PRODUCT SAFETY ISSUE
→ See Appendix C

4. FINANCIAL CRISIS
→ See Appendix D

5. LEADERSHIP MISCONDUCT
→ See Appendix E

6. NATURAL DISASTER
→ See Appendix F

7. REGULATORY VIOLATION
→ See Appendix G

8. PUBLIC RELATIONS CRISIS
→ See Appendix H

├──
SECTION 6: RECOVERY PROCEDURES
├──

IMMEDIATE RECOVERY (Days 1-7):

→ Restore normal operations
→ Implement temporary workarounds
→ Continue monitoring for recurrence
→ Maintain elevated support levels
→ Daily stakeholder updates

SHORT-TERM RECOVERY (Weeks 1-4):

→ Implement permanent fixes
→ Rebuild customer trust
→ Address any ongoing concerns
→ Return to normal operations
→ Weekly stakeholder updates

LONG-TERM RECOVERY (Months 1-6):

→ Complete post-mortem analysis
→ Implement systemic improvements
→ Update crisis management plan
→ Conduct refresher training
→ Monitor for lasting impacts

├──
SECTION 7: POST-CRISIS REVIEW
├──

POST-MORTEM PROCESS (Within 1 Week):

1. Gather all documentation (logs, decisions, communication)
2. Interview key participants
3. Create timeline of events
4. Identify what went well
5. Identify what needs improvement
6. Create action plan for improvements
7. Share learnings with organization

POST-MORTEM TEMPLATE:

• Crisis Overview: [What happened]
• Timeline: [Key events with timestamps]
• Response Assessment: [What worked well]
• Gaps Identified: [What didn't work]
• Root Causes: [Why it happened]
• Lessons Learned: [Key takeaways]
• Action Items: [Improvements with owners]

METRICS TO TRACK:

• Detection Time: How long to identify crisis?
• Response Time: How long to activate CMT?
• Resolution Time: How long to resolve?
• Communication Timeliness: How fast were stakeholders notified?
• Customer Impact: How many affected?
• Financial Impact: Cost of crisis?
• Reputation Impact: Media sentiment, NPS change?

├──
SECTION 8: MAINTENANCE & TESTING
├──

PLAN MAINTENANCE:

• Review: Quarterly
• Update: After any crisis or major change
• Owner: Crisis Coordinator
• Approver: Crisis Manager

TRAINING REQUIREMENTS:

• CMT Training: Annually
• Department Training: Annually
• New Employee Orientation: Within 30 days

CRISIS SIMULATION EXERCISES:

• Tabletop Exercise: Semi-annually
• Full Crisis Drill: Annually
• Format: [Describe simulation approach]
• Debrief: Document learnings, update plan

├──
APPENDICES
├──

A. Security Breach Playbook
B. Major Outage Playbook
C. Product Safety Playbook
D. Financial Crisis Playbook
E. Leadership Misconduct Playbook
F. Natural Disaster Playbook
G. Regulatory Violation Playbook
H. Public Relations Crisis Playbook
I. Communication Templates
J. Contact Lists
K. Decision Logs

├──
```

-----

## 📌 Crisis Playbook: Security Breach

```
├──
SECURITY BREACH CRISIS PLAYBOOK
├──

CRISIS TYPE: Data Breach / Unauthorized Access
SEVERITY: Typically Level 2 or 3
CMT ACTIVATION: Immediate

├──
IMMEDIATE ACTIONS (First 30 Minutes)
├──

TECHNICAL RESPONSE:
→ Isolate affected systems
→ Stop the breach (block access, shutdown if needed)
→ Preserve evidence (logs, forensics)
→ Assess scope: What data was accessed?
→ Identify attack vector

CMT ACTIVATION:
→ Notify Crisis Manager + Crisis Coordinator
→ Activate Security Lead, Technical Lead, Legal
→ Establish command center
→ Begin incident log

INITIAL ASSESSMENT:
→ What data was compromised?
→ How many users/customers affected?
→ Was data exfiltrated or just accessed?
→ Is attack ongoing or contained?
→ Any regulatory notification requirements?

├──
FIRST HOUR ACTIONS
├──

LEGAL & REGULATORY:
→ Legal counsel assesses notification requirements
→ Identify breach notification laws (GDPR, CCPA, etc.)
→ Determine notification timeline requirements
→ Prepare for potential law enforcement contact

TECHNICAL CONTAINMENT:
→ Complete system isolation
→ Change all credentials
→ Implement additional monitoring
→ Begin forensic analysis
→ Engage external security firm if needed

INTERNAL COMMUNICATION:
→ Notify executive team
→ Brief support team (prepare for customer inquiries)
→ Inform relevant department heads
→ Issue internal holding statement

CUSTOMER COMMUNICATION PREP:
→ Draft customer notification (Legal approval)
→ Prepare FAQ for support team
→ Set up dedicated communication channel
→ Prepare status page update

├──
NOTIFICATION REQUIREMENTS
├──

REGULATORY (Legal Determines Timeline):
→ GDPR: 72 hours to regulator, immediate to users
→ CCPA: Without unreasonable delay
→ State laws: Varies by jurisdiction
→ Industry-specific: HIPAA, PCI-DSS, etc.

CUSTOMER NOTIFICATION:
Timeline: [As soon as legally permitted]
Channel: [Email primary, in-app secondary]
Content Must Include:
• What happened (facts only)
• What data was compromised
• What we're doing about it
• What customers should do
• How to get more information
• Our commitment to making it right

MEDIA/PUBLIC RESPONSE:
• Designated spokesperson only
• Holding statement ready
• FAQ for common questions
• Social media monitoring
• No speculation or blame

├──
CUSTOMER SUPPORT RESPONSE
├──

IMMEDIATE PREP:
→ Surge support staffing (3-5x normal)
→ Extended hours (24/7 for first week)
→ Create detailed FAQ
→ Prepare response scripts
→ Set up dedicated phone/email
→ Monitor social media channels

SUPPORT SCRIPT KEY POINTS:
• Acknowledge concern and apologize
• Provide factual information only
• Explain steps we've taken
• Offer credit monitoring if applicable
• Document all interactions

├──
ONGOING RESPONSE (Days/Weeks)
├──

TECHNICAL REMEDIATION:
→ Complete forensic investigation
→ Identify and patch vulnerability
→ Implement additional security controls
→ Third-party security audit
→ Penetration testing

CUSTOMER REMEDIATION:
→ Offer credit monitoring (12-24 months)
→ Provide identity theft protection
→ Consider financial compensation if warranted
→ Regular updates on investigation

REGULATORY COMPLIANCE:
→ File required breach notifications
→ Cooperate with investigations
→ Implement corrective action plan
→ Document all remediation steps

├──
RECOVERY PHASE
├──

TRUST REBUILDING:
→ Transparency report published
→ Security improvements communicated
→ Third-party certification obtained
→ Regular security updates to customers
→ Customer advisory board input

INTERNAL IMPROVEMENTS:
→ Security training for all employees
→ Enhanced security controls
→ Improved monitoring and alerting
→ Updated incident response procedures
→ Regular security audits

├──
POST-MORTEM (1-2 Weeks Post-Resolution)
├──

KEY QUESTIONS:
• How did the breach occur?
• What was the root cause?
• What early warning signs did we miss?
• How effective was our response?
• What would we do differently?
• What systemic changes are needed?

DELIVERABLES:
→ Detailed timeline
→ Root cause analysis
→ Lessons learned document
→ Action plan with owners
→ Updated security procedures
→ Crisis plan improvements

├──
```

-----

## 📌 Crisis Communication Templates

### Internal Communication Template (All-Employees)

```
Subject: [Important] Company Update - [Brief Description]

Team,

I'm writing to inform you about [brief description of situation].

WHAT HAPPENED:
[2-3 sentences with facts only, no speculation]

CURRENT STATUS:
[What we know right now, what's under control]

WHAT WE'RE DOING:
[Actions being taken, who's leading response]

WHAT THIS MEANS FOR YOU:
[How it affects employees, any changes to operations]

WHAT YOU SHOULD DO:
• [Specific action if any]
• [Where to get updates]
• [Who to contact with questions]

We'll provide updates [frequency]. Thank you for your patience and professionalism as we work through this.

[Name]
[Title]
```

-----

### External Communication Template (Customers)

```
Subject: Important Update About [Issue]

Dear [Customer Name],

We're writing to inform you about [brief issue description] that may have affected your account.

WHAT HAPPENED:
[Clear,factual description in plain language]

WHAT DATA WAS AFFECTED:
[Specific types of information, be transparent]

WHAT WE'RE DOING:
• [Action 1]
• [Action 2]
• [Action 3]

WHAT YOU SHOULD DO:
[Clear, actionable steps for customers]

WHAT WE'RE OFFERING:
[Any remediation: credit monitoring, compensation, etc.]

HOW TO GET HELP:
• Visit: [URL]
• Email: [dedicated email]
• Phone: [dedicated hotline]

We sincerely apologize for this incident. Your trust is paramount to us, and we're committed to making this right.

[Name]
[Title]
[Company]
```

-----

### Media Holding Statement Template

```
HOLDING STATEMENT
For Immediate Release

[Company] is aware of [incident description]. We are actively investigating the situation and taking immediate steps to address it.

The safety and security of our [customers/employees/users] is our top priority. We are working closely with [relevant authorities/experts] to understand the full scope and impact.

We will provide updates as we have more information to share.

For more information:
[Spokesperson Name]
[Title]
[Email]
[Phone]
```

-----

## 📌 Crisis Management Anti-Patterns

### Anti-Pattern #1: “We Don’t Need a Plan”

**What it looks like:**

- “We’ll figure it out when something happens”
- No documented procedures
- No trained crisis team

**Why it’s harmful:**

- Chaos and confusion during actual crisis
- Slow response costs time and trust
- Legal/regulatory penalties

**Solution:**

- Create basic plan now (doesn’t need to be perfect)
- Identify crisis team
- Run one tabletop exercise
- Review and improve quarterly

-----

### Anti-Pattern #2: Hiding the Crisis

**What it looks like:**

- Delayed or no external communication
- Minimizing severity
- “It’s not that bad”

**Why it’s harmful:**

- Makes crisis worse when truth emerges
- Destroys trust permanently
- Legal liability increases

**Solution:**

- Communicate early, even with incomplete information
- Acknowledge what you don’t know
- Commit to updates
- Own the problem

-----

### Anti-Pattern #3: Playing the Blame Game

**What it looks like:**

- Looking for who to punish
- Defensive posture
- Protecting reputation over doing what’s right

**Why it’s harmful:**

- Delays resolution
- Creates culture of fear
- Misses systemic improvements

**Solution:**

- Focus on resolution, not blame
- Blameless post-mortems
- Fix systems, not people
- Learn and improve

-----

### Anti-Pattern #4: No One in Charge

**What it looks like:**

- Unclear decision-making authority
- Too many cooks
- Decision paralysis

**Why it’s harmful:**

- Delayed decisions make crisis worse
- Conflicting communications
- Wastes critical time

**Solution:**

- Designate Crisis Manager
- Clear escalation path
- Defined decision rights
- Single source of truth

-----

### Anti-Pattern #5: “The Crisis is Over” Too Soon

**What it looks like:**

- Declaring victory prematurely
- Disbanding team before recovery complete
- Skipping post-mortem

**Why it’s harmful:**

- Crisis can reignite
- Miss learning opportunities
- Don’t implement improvements

**Solution:**

- Formal recovery phase
- Defined closure criteria
- Mandatory post-mortem
- Action plan follow-through

-----

## → Crisis Preparedness Checklist

### Foundation (Do These First)

- [ ] Crisis management plan documented
- [ ] Crisis Management Team identified with backups
- [ ] Contact lists current (phone, email, backup)
- [ ] Severity criteria defined
- [ ] Escalation path clear
- [ ] Communication channels established
- [ ] Legal counsel identified

### Playbooks (Create for Top Risks)

- [ ] Security breach playbook
- [ ] Major outage playbook
- [ ] Product safety playbook
- [ ] PR crisis playbook
- [ ] [Your specific risk] playbook

### Training & Exercises

- [ ] CMT trained on their roles
- [ ] Tabletop exercise completed (last 6 months)
- [ ] Full crisis drill completed (last 12 months)
- [ ] All employees know basic crisis procedures
- [ ] New employees trained within 30 days

### Tools & Resources

- [ ] Command center location identified
- [ ] Crisis communication platform ready
- [ ] Document templates prepared
- [ ] Situation log template ready
- [ ] External resources identified (legal, PR, security firms)

### Ongoing Maintenance

- [ ] Plan reviewed quarterly
- [ ] Contact lists updated monthly
- [ ] Post-crisis reviews completed
- [ ] Improvements implemented
- [ ] Regular simulations scheduled

-----

## References

- Escalation: `../5-Escalation/README.md`
- Stakeholder Management: `../7-Stakeholder-Management/README.md`
- Foundations: `../../1-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
