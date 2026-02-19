# Company Context - Personalization

> **Purpose:** This file stores your personal and organizational context to personalize AI assistance and make documents more relevant. Update this file as your organization evolves.

**For AI agents:** This file provides key context about the user, company, and organizational structure. Reference this when personalizing responses and when suggesting document structures. Also check `.cursor/rules/thinking.personal.mdc` for personal working style preferences.

**For teams:** This file can be shared with team members to ensure consistent naming and context across the PM Brain repository.

**Git tracking by mode:**
- **Public mode:** Tracked (sanitize sensitive company details if needed)
- **Private mode:** Ignored (kept private)
- **Team mode:** Ignored by default, but can be optionally tracked for team consistency (see `.gitignore.team` comments)

**Relationship to other personalization files:**
- **`CONTEXT.md`** (this file) = Organizational context (company name, teams, BUs, your role in the organization)
- **`.cursor/rules/thinking.personal.mdc`** = Personal working style and preferences (how you like to work, communication style, cognitive preferences)
- Both files may include your name - keep them consistent. This file focuses on organizational context; `thinking.personal.mdc` focuses on how you work.

---

## Personal Information

**Your Name:** [Your Name or Alias]

**Your Role:** [Your Title / Role, e.g., "Senior Product Manager", "Head of Product"]

**Your Team(s):** [List teams you work with, e.g., "Platform Team", "Consumer Product Team"]

---

## Company Information

**Company Name:** [Your Company Name]

> **Note:** This name will replace `[Company]` placeholders throughout your PM Brain documents. Use the official company name.

**Company Size:** [ ] Startup (< 50) [ ] Mid-size (50-500) [ ] Enterprise (500+)

**Industry:** [Your Industry, e.g., "SaaS", "E-commerce", "Healthcare Technology"]

---

## Organizational Structure

### Business Units

**Do you have business units?** [ ] Yes [ ] No

**If yes, list relevant business units:**
- [Business Unit 1 Name, e.g., "Consumer Products"]
- [Business Unit 2 Name, e.g., "Enterprise Solutions"]
- [Business Unit 3 Name, e.g., "Platform & Infrastructure"]
- [Add more as needed]

> **Note:** These names will be used when creating BU folders (e.g., `1.1-Consumer-Products/`). Only list BUs relevant to your work.

### Teams

**List teams you work with regularly:**
- [Team 1 Name, e.g., "Platform Engineering"]
- [Team 2 Name, e.g., "Data Science"]
- [Team 3 Name, e.g., "Design"]
- [Add more as needed]

---

## How to Use This File

### For Personal Use
- Fill in your information
- Reference this when creating documents (use company name instead of `[Company]`)
- Update when your role or organization changes

### For Team Use
- Share this file with team members
- Ensure consistent naming across the repository
- Update when organizational structure changes

### For AI Agents
- AI agents will reference this file to personalize responses
- Company name will be used to replace placeholders
- Team/BU names help suggest appropriate folder structures

---

## Maintenance

**Update this file when:**
- You change roles or teams
- Company name changes
- New business units are created
- Team structure changes
- Organizational reorganization occurs

**Frequency:** Review quarterly or when organizational changes occur.

---

## Example

```markdown
## Personal Information

**Your Name:** Sarah Chen

**Your Role:** Senior Product Manager

**Your Team(s):** Platform Team, Data Infrastructure Team

## Company Information

**Company Name:** TechCorp Inc.

**Company Size:** [X] Mid-size (50-500)

**Industry:** SaaS - Customer Relationship Management

## Organizational Structure

### Business Units

**Do you have business units?** [X] Yes [ ] No

**If yes, list relevant business units:**
- Consumer Products
- Enterprise Solutions
- Platform & Infrastructure

### Teams

**List teams you work with regularly:**
- Platform Engineering
- Data Science
- Design Systems
```
