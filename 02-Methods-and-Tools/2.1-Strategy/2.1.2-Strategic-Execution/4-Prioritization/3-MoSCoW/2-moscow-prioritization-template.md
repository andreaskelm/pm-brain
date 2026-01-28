# MoSCoW Prioritization Template

## Initiative Context

**Initiative/Release Name:** [Your initiative name]  
**Timeline:** [Q3 2025, Sprint 15, etc.]  
**Created on:** [Date]  
**Last updated:** [Date]  
**Next review:** [Date]

**Initiative Objectives:**
- [Objective 1: e.g., Increase user activation by 20%]
- [Objective 2: e.g., Reduce support tickets by 30%]
- [Objective 3: e.g., Launch in EMEA market]

**Key Constraints:**
- **Time:** [Fixed launch date, sprint cycle, etc.]
- **Resources:** [Team size, budget, technical limitations]
- **Dependencies:** [External teams, integrations, regulatory approvals]

**Success Metrics:**
- [Metric 1: e.g., 20% increase in DAU]
- [Metric 2: e.g., <2% critical bug rate]
- [Metric 3: e.g., 90% stakeholder satisfaction]

---

## MoSCoW Categories

### 🔴 Must Have (Critical - ≤60% of effort)

Items absolutely essential for project success. Without these, we would cancel the release.

| Item | Description | Business Value | Effort Estimate | Dependencies | Rationale |
|------|-------------|----------------|-----------------|--------------|-----------|
| [Feature/Requirement name] | [Brief description] | [Why this matters] | [S/M/L or story points] | [What's needed] | [Why it's a must-have] |

#### Example:
| Item | Description | Business Value | Effort Estimate | Dependencies | Rationale |
|------|-------------|----------------|-----------------|--------------|-----------|
| User authentication | Login/logout, password reset, session management | Legal requirement, security baseline | L (13 pts) | Security review, OAuth integration | Legal requirement for handling user data; product is unusable without this |
| Payment processing | Credit card, PayPal, Stripe integration | Revenue generation, core business model | XL (21 pts) | PCI compliance, payment gateway APIs | No revenue without payments; business model depends on this |
| Core search functionality | Basic keyword search across products | Primary user task, 70% of sessions start with search | M (8 pts) | Search indexing infrastructure | User research shows 70% of users expect search; competitive baseline |

**Total Must-Have Effort:** [X points/days] (**Target: ≤60% of total**)

---

### 🟡 Should Have (Important - ~20% of effort)

Important features that add significant value but aren't critical. We can launch with workarounds if needed.

| Item | Description | Business Value | Effort Estimate | Workaround if Dropped | Dependencies |
|------|-------------|----------------|-----------------|----------------------|--------------|
| [Feature/Requirement name] | [Brief description] | [Why this matters] | [S/M/L or story points] | [How we'd handle absence] | [What's needed] |

#### Example:
| Item | Description | Business Value | Effort Estimate | Workaround if Dropped | Dependencies |
|------|-------------|----------------|-----------------|----------------------|--------------|
| Advanced filters | Filter by price, category, rating, availability | Improved discovery, reduces time-to-purchase | M (8 pts) | Users can browse all results and manually scan | Design system components |
| Email notifications | Order confirmations, shipping updates | Reduces support inquiries, improves satisfaction | S (5 pts) | Users check in-app notifications; support reaches out proactively | Email service provider setup |
| CSV export | Export search results or lists to CSV | Requested by 40% of enterprise customers | S (3 pts) | Users manually copy data or we provide on request | Export library integration |

**Total Should-Have Effort:** [X points/days] (**Target: ~20% of total**)

---

### 🟢 Could Have (Nice-to-Have - ~20% of effort)

Desirable features with small impact if excluded. First to be deprioritized if capacity becomes constrained.

| Item | Description | Business Value | Effort Estimate | Impact if Dropped | Dependencies |
|------|-------------|----------------|-----------------|-------------------|--------------|
| [Feature/Requirement name] | [Brief description] | [Why this would be nice] | [S/M/L or story points] | [Minimal impact] | [What's needed] |

#### Example:
| Item | Description | Business Value | Effort Estimate | Impact if Dropped | Dependencies |
|------|-------------|----------------|-----------------|-------------------|--------------|
| Dark mode | Dark color theme for UI | Nice visual option, trendy feature | M (5 pts) | Minimal - aesthetic preference | Design system update |
| Social sharing | Share products on social media | Potential virality, 5% of users use this | S (3 pts) | Very low - organic sharing still happens | Social media API integration |
| Keyboard shortcuts | Power user shortcuts for common actions | Efficiency for <10% of users | S (2 pts) | None - mouse/touch still works | Documentation update |
| Custom profile themes | Personalized color schemes for profiles | Fun personalization, low usage | M (5 pts) | None - default theme works fine | Design system extension |

**Total Could-Have Effort:** [X points/days] (**Target: ~20% of total**)

---

### ⚪ Won't Have (Out of Scope)

Items explicitly excluded from this release. May be considered for future releases or dropped entirely.

| Item | Description | Reason for Exclusion | Future Consideration? | Stakeholders Informed |
|------|-------------|----------------------|-----------------------|-----------------------|
| [Feature/Requirement name] | [Brief description] | [Why not now] | [Yes/No/TBD + when] | [Yes/No + who] |

#### Example:
| Item | Description | Reason for Exclusion | Future Consideration? | Stakeholders Informed |
|------|-------------|----------------------|-----------------------|-----------------------|
| Mobile app | Native iOS and Android apps | Limited resources; focusing on web first; need web validation before mobile | Yes - Q2 2026 after web launch proven | Yes - Leadership, Sales team |
| AI recommendations | ML-powered product recommendations | Requires data we don't have yet; need 6+ months of user behavior data | Yes - H2 2026 after data collection | Yes - Product team, Data Science |
| Multi-language support | Support for 15+ languages | Only 3% of users are non-English; ROI too low for MVP | TBD - depends on market expansion | Yes - Marketing, Customer Success |
| Advanced analytics | Custom dashboards, data exports | Enterprise feature; not needed for initial launch; adds significant complexity | Yes - Enterprise tier in Q4 2025 | Yes - Sales team, key customers |
| API access | Public API for third-party integrations | Too early; need stable product first; security considerations | Yes - Q3 2026 after product maturity | Yes - Engineering, DevRel |

---

## Effort Distribution Summary

| Category | Effort Points | Percentage | Target % | Status |
|----------|---------------|------------|----------|--------|
| Must Have | [X pts] | [Y%] | ≤60% | 🟢 / 🔴 |
| Should Have | [X pts] | [Y%] | ~20% | 🟢 / 🔴 |
| Could Have | [X pts] | [Y%] | ~20% | 🟢 / 🔴 |
| **Total** | **[X pts]** | **100%** | **100%** | |

**Effort Distribution Check:**
- ✅ Must-haves are ≤60% of effort
- ✅ Sufficient could-have contingency (~20%)
- ✅ Won't-haves clearly documented
- ✅ Stakeholders aligned on priorities

---

## Decision Log

Document key prioritization decisions and rationale:

| Date | Decision | Rationale | Who Decided | Impact |
|------|----------|-----------|-------------|--------|
| [Date] | [What was decided] | [Why] | [PM, Leadership, etc.] | [What changed] |

### Example:
| Date | Decision | Rationale | Who Decided | Impact |
|------|----------|-----------|-------------|--------|
| 2025-01-10 | Moved advanced analytics from Should-Have to Won't-Have | Complexity too high; only 2% of beta users requested it; doesn't support core launch objectives | PM + Engineering Lead | Freed up 13 pts for must-haves; set clear expectation with Sales |
| 2025-01-15 | Promoted CSV export from Could-Have to Should-Have | 40% of enterprise trials requested this; workaround exists but enterprise tier launch depends on this perception | PM + Sales Lead | Added 3 pts to should-haves; still within budget |

---

## Risk & Dependency Tracking

### Critical Dependencies

| Dependency | Type | Status | Impact if Delayed | Mitigation Plan | Owner |
|------------|------|--------|-------------------|-----------------|-------|
| [What you need] | [Team/Vendor/Technical] | [On track/At risk/Blocked] | [Must/Should/Could haves affected] | [What you'll do] | [Who's responsible] |

### Key Risks

| Risk | Likelihood | Impact | Mitigation | Contingency |
|------|------------|--------|------------|-------------|
| [What could go wrong] | [High/Med/Low] | [Must/Should/Could haves affected] | [Prevention plan] | [Backup plan] |

---

## Review Schedule

- **Weekly:** Progress on must-haves, dependency status
- **Bi-weekly:** Review should-haves, adjust could-haves based on capacity
- **Monthly:** Full MoSCoW review, effort distribution check
- **Ad-hoc:** When scope changes, new requirements emerge, or major blockers hit

---

## Stakeholder Communication

### Key Messages

**For Leadership:**
- Must-haves represent [X]% of effort, aligned with business objectives
- Built-in [Y]% contingency through could-haves
- Won't-haves clearly communicated to manage expectations

**For Engineering:**
- Clear prioritization for sprint planning
- Must-haves protected; could-haves provide flexibility
- Dependencies mapped and tracked

**For Sales/Customer Success:**
- Must-haves support key customer needs and launch positioning
- Should-haves add competitive advantage
- Won't-haves explained with future consideration timeline

**For Users/Customers:**
- Focus on core value delivery (must-haves)
- Enhanced experience (should-haves)
- Future roadmap (won't-haves reconsidered later)

---

## Quick Reference Guide

### Category Definitions

| Category | Test Question | When to Use |
|----------|---------------|-------------|
| 🔴 **Must Have** | "Would we cancel the release without this?" | Legal requirements, core functionality, critical business needs |
| 🟡 **Should Have** | "Would this absence hurt badly, but we could launch with a workaround?" | Important features, significant value-add, competitive needs |
| 🟢 **Could Have** | "Would users appreciate this, but hardly notice its absence?" | Nice-to-haves, polish, low-impact enhancements |
| ⚪ **Won't Have** | "Is this a distraction from our core goals right now?" | Out of scope, future consideration, low priority |

### Quick Tips

- ✅ **Must-haves should pass the "cancel release" test** - Be ruthless
- ✅ **Limit must-haves to ≤60% of effort** - Prevents overload
- ✅ **Maintain 20% could-have contingency** - Provides flexibility
- ✅ **Document won't-haves explicitly** - Manages expectations
- ✅ **Review and adjust regularly** - Stay flexible
- ✅ **Involve cross-functional stakeholders** - Get diverse input
- ✅ **Link to business objectives** - Show strategic alignment
- ✅ **Challenge every must-have** - Ensure they're truly critical

---

## Related Templates & Frameworks

- MoSCoW Framework: `1-moscow-prioritization-framework.md`
- Prioritization Methods (RICE, ICE, Impact-Effort, Kano): `../4-Prioritization/README.md`
- Kano Model: `../4-Kano-Model/README.md`
- Roadmap Template: `../2-Roadmap/2-roadmap-template.md`
- OKR Template: `../1-OKR/2-okr-template.md`

---

**Notes:**
- This is a living document - update as priorities change
- Not all items need to be filled out - adapt to your needs
- Use effort estimates that work for your team (story points, t-shirt sizes, hours)
- The key is clarity and shared understanding, not perfect precision
