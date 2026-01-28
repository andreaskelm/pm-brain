# PM-Brain Mode Selection Guide

**Choose how you want to use PM-Brain: Public, Private, or Team.**

This guide helps you select the right mode for your needs and shows you how to switch between modes.

-----

## The Three Modes

### 🌍 Public Mode (Default)

**Philosophy:** Your growth is your proof. Share it openly.

**What's tracked in git:**
- ✓ Daily learning logs (`00-Meta/1-daily-log-*.md`)
- ✓ Weekly reflections (`00-Meta/0.1-Learning-Log/*/week-*.md`)
- ✓ Monthly syntheses (`00-Meta/0.1-Learning-Log/*/monthly-*.md`)
- ✓ Growth portfolio (`00-Meta/0.2-Growth-Portfolio/*.md`)
- ✓ Self-assessments (if you choose to commit `00-Meta/self-assessment-*.md`)
- ✓ Company context (`01-Company-Context/`)
- ✓ Research artifacts (`03-Research-Artifacts/`)
- ✓ Active initiatives (`04-Initiatives/`)
- ✓ All templates and frameworks

**What's ignored:**
- Only truly sensitive data (secrets, credentials, explicit private notes)

**Best for:**
- Building a public learning portfolio
- Creating blog content or portfolio pieces
- Demonstrating systematic improvement publicly
- Open source contribution and sharing
- Personal branding and thought leadership

**Example use case:**
> "I'm a PM building my portfolio. I want to showcase my product thinking journey, decision-making process, and systematic growth. I'll sanitize company-specific details but share my learning process openly."

-----

### 🔒 Private Mode

**Philosophy:** All learning stays private. Share only frameworks.

**What's tracked in git:**
- ✓ Templates and frameworks (canonical versions in `02-Methods-and-Tools/`)
- ✓ Framework documentation (`02-Methods-and-Tools/`)
- ✓ README files and guides
- ✓ Practice exercise descriptions

**What's ignored:**
- ✗ Daily logs (private practice)
- ✗ Weekly/monthly reflections (private learning)
- ✗ Growth portfolio (private journey)
- ✗ Self-assessments (private evaluation)
- ✗ Company context (confidential)
- ✗ Research artifacts (proprietary)
- ✗ Active initiatives (company work)

**Best for:**
- Company-specific work with confidential information
- Personal learning you don't want to share
- Sensitive product strategy or research
- Risk-averse organizations
- Starting out and not ready to share

**Example use case:**
> "I work at a company where product strategy is confidential. I want to use PM-Brain for my growth, but I can't share any company context, user research, or active work. I'll keep all personal content private."

-----

### 👥 Team Mode

**Philosophy:** Share frameworks and templates. Keep personal learning private.

**What's tracked in git:**
- ✓ Templates and frameworks (for team use)
- ✓ Framework documentation (shared knowledge)
- ✓ README files and guides (help the team)
- ✓ Practice exercise descriptions (team can use)
- ✓ Example templates (anonymized references)

**What's ignored:**
- ✗ Daily logs (your private practice)
- ✗ Weekly/monthly reflections (your private learning)
- ✗ Growth portfolio (your private journey)
- ✗ Self-assessments (your private evaluation)
- ✗ Company context (team-specific)

**Best for:**
- Collaborative template development
- Sharing PM frameworks across team
- Building a team knowledge base
- Balancing personal privacy with team sharing
- Internal team repositories

**Example use case:**
> "Our PM team wants to share frameworks and templates. We're collaborating on improving our PRD template, braindump prompts, and prioritization frameworks. But our personal learning logs, self-assessments, and company context should stay private."

-----

## Decision Tree

Use this flowchart to choose your mode:

```
Are you using this for work at a company?
│
├─ NO → Do you want to build a public portfolio?
│        │
│        ├─ YES → PUBLIC MODE 🌍
│        │        (Share your growth journey)
│        │
│        └─ NO → PRIVATE MODE 🔒
│                 (Personal learning only)
│
└─ YES → Does your company allow sharing sanitized learnings?
         │
         ├─ NO → PRIVATE MODE 🔒
         │        (Keep everything confidential)
         │
         └─ YES → Are you working solo or with a team?
                  │
                  ├─ SOLO → Can you sanitize company details?
                  │         │
                  │         ├─ YES → PUBLIC MODE 🌍
                  │         │        (Sanitize and share)
                  │         │
                  │         └─ NO → PRIVATE MODE 🔒
                  │                  (Keep it private)
                  │
                  └─ TEAM → TEAM MODE 👥
                            (Share frameworks, private logs)
```

-----

## Quick Comparison

| Feature | Public 🌍 | Private 🔒 | Team 👥 |
|---------|-----------|------------|---------|
| **Daily logs** | ✓ Tracked | ✗ Ignored | ✗ Ignored |
| **Weekly reflections** | ✓ Tracked | ✗ Ignored | ✗ Ignored |
| **Growth portfolio** | ✓ Tracked | ✗ Ignored | ✗ Ignored |
| **Self-assessments** | ✓ Tracked | ✗ Ignored | ✗ Ignored |
| **Templates** | ✓ Tracked | ✓ Tracked | ✓ Tracked |
| **Frameworks** | ✓ Tracked | ✓ Tracked | ✓ Tracked |
| **Company context** | ✓ Tracked* | ✗ Ignored | ✗ Ignored |
| **Research** | ✓ Tracked* | ✗ Ignored | Optional |
| **Active work** | ✓ Tracked* | ✗ Ignored | Optional |

*Sanitize company-specific details before committing

-----

## How to Switch Modes

### Interactive Setup (Recommended)

Run the setup script and follow prompts:

```bash
bash 00-Meta/SETUP.sh
```

The script will:
1. Ask which mode you want
2. Update your `.gitignore` accordingly
3. Configure git commit template
4. Verify directory structure
5. Create starter files

### Manual Setup

If you prefer manual configuration:

#### Switch to Private Mode

```bash
# Append private patterns to .gitignore
cat .gitignore.private >> .gitignore

# Commit the change
git add .gitignore
git commit -m "setup: Switch to private mode"

# Optional: Remove already-tracked personal files
git rm --cached 00-Meta/1-daily-log-*.md
git rm --cached -r 00-Meta/0.1-Learning-Log/*/
git rm --cached -r 00-Meta/0.2-Growth-Portfolio/
# ... etc
git commit -m "setup: Remove personal content from tracking"
```

#### Switch to Team Mode

```bash
# Append team patterns to .gitignore
cat .gitignore.team >> .gitignore

# Commit the change
git add .gitignore
git commit -m "setup: Switch to team mode"

# Optional: Remove already-tracked personal files (same as private)
```

#### Switch Back to Public Mode

```bash
# Remove private/team patterns from .gitignore
# (Manually edit .gitignore to remove the appended sections)

# Re-add files to tracking
git add 00-Meta/
git add 01-Company-Context/
git add 03-Research-Artifacts/
git add 04-Initiatives/

git commit -m "setup: Switch to public mode"
```

-----

## What Happens to Existing Files When You Switch?

### Switching FROM Public TO Private/Team

**Already-tracked files remain tracked** until you explicitly remove them.

To remove personal files from git history:

```bash
# Stop tracking but keep locally
git rm --cached 00-Meta/1-daily-log-*.md
git rm --cached -r 00-Meta/0.1-Learning-Log/*/
git rm --cached -r 00-Meta/0.2-Growth-Portfolio/
git commit -m "setup: Remove personal content from tracking"

# Push to remove from remote
git push
```

**Note:** Files will still exist in git history. To completely remove them, you'd need to rewrite history (not recommended unless necessary).

### Switching FROM Private/Team TO Public

**Previously ignored files become untracked.**

To add them to git:

```bash
# Stage previously ignored files
git add 00-Meta/1-daily-log-*.md
git add 00-Meta/0.1-Learning-Log/*/
git add 00-Meta/0.2-Growth-Portfolio/

git commit -m "setup: Add personal content to public portfolio"
git push
```

-----

## Common Scenarios

### Scenario 1: Starting Fresh with PM-Brain

**Recommendation:** Start with **PUBLIC MODE** if you're comfortable sharing, or **PRIVATE MODE** if you're not sure yet.

**Why:** It's easier to switch from public to private (just add ignore patterns) than from private to public (need to backfill history).

**Action:**
```bash
# If unsure, start private
bash 00-Meta/SETUP.sh
# Select "Private Mode"

# When ready to share, switch to public
# Edit .gitignore, remove private patterns
# Add files and commit
```

### Scenario 2: Forking PM-Brain for Team Use

**Recommendation:** **TEAM MODE**

**Why:** Your team can collaborate on frameworks and templates, but personal learning stays private.

**Action:**
```bash
# After forking
bash 00-Meta/SETUP.sh
# Select "Team Mode"

# Invite team to fork and contribute
# Personal logs stay on individual machines
```

### Scenario 3: Building a Public Portfolio

**Recommendation:** **PUBLIC MODE**

**Why:** You want to demonstrate systematic growth publicly.

**Action:**
```bash
# Already in public mode by default
# Just start practicing and committing

# Sanitize company details:
# - Change company name to "Acme Corp"
# - Anonymize user research quotes
# - Remove proprietary metrics
# - Keep learning process intact
```

### Scenario 4: Working at Confidential Company

**Recommendation:** **PRIVATE MODE**

**Why:** Company policy prohibits sharing any work details publicly.

**Action:**
```bash
bash 00-Meta/SETUP.sh
# Select "Private Mode"

# Use PM-Brain for personal growth
# Share only frameworks (not work examples)
# Consider separate public repo for portfolio
```

### Scenario 5: Mid-Career PM Building Portfolio

**Recommendation:** **PUBLIC MODE** with sanitization

**Why:** You want to showcase growth but can't share proprietary details.

**Action:**
```bash
# Use public mode (default)

# Sanitization strategy:
# 1. Replace company name → "TechCo"
# 2. Anonymize products → "Product X"
# 3. Change metrics → percentages not absolute numbers
# 4. Remove customer names → "Enterprise customer"
# 5. Abstract features → "Feature enabling workflow Y"

# Keep decision-making process and learnings intact
```

-----

## FAQs

### Can I use different modes for different repositories?

**Yes!** You might have:
- Personal PM-Brain fork in **PUBLIC MODE** for your portfolio
- Company team PM-Brain in **TEAM MODE** for shared frameworks
- Confidential project PM-Brain in **PRIVATE MODE** for sensitive work

Each repo can use a different mode.

### Can I change modes later?

**Yes!** You can switch modes at any time. Just run the setup script or manually update `.gitignore`.

**Caveat:** Files already committed to git remain in history unless you explicitly remove them.

### What if I accidentally commit sensitive data in public mode?

**Immediate action:**

```bash
# Remove from latest commit
git rm --cached path/to/sensitive-file.md
git commit --amend -m "Remove sensitive file"
git push --force

# If already pushed and others pulled, you need to rewrite history
# (More complex - consult git documentation or ask for help)
```

**Prevention:**
- Review diffs before committing
- Use `.gitignore` patterns for sensitive files
- Consider using `git-secrets` or similar tools

### Do I need to pick one mode forever?

**No!** Your needs change. You might:
- Start **PRIVATE** while learning the system
- Switch to **PUBLIC** when ready to share
- Use **TEAM** when you join a team repo
- Switch back to **PRIVATE** for a new confidential project

**Be flexible. Change modes as your context changes.**

### Can I mix modes (some files public, some private)?

**Sort of.** The three modes are presets, but you can customize:

```bash
# Start with a mode
bash 00-Meta/SETUP.sh

# Then manually edit .gitignore to tweak
vim .gitignore

# Example: Team mode but also share growth portfolio
# Remove growth portfolio from ignore patterns
```

**Recommendation:** Start with a preset, customize only if needed.

-----

## Validation

After switching modes, verify your setup:

```bash
# Run validation script
bash 00-Meta/validate-setup.sh

# Check what's tracked vs ignored
git status

# See what patterns are active
cat .gitignore
```

-----

## Summary

**Choose your mode based on:**
1. **Who you're sharing with** (public, team, or no one)
2. **Company policy** (what you're allowed to share)
3. **Your goals** (portfolio, team collab, or personal growth)

**Default recommendation:**
- Unsure? Start **PRIVATE**, switch to **PUBLIC** later
- Team? Use **TEAM MODE**
- Portfolio? Use **PUBLIC MODE**

**Remember:** You can always change. Pick what feels right now.

-----

## Quick Reference Commands

```bash
# Interactive mode selection
bash 00-Meta/SETUP.sh

# Manual switch to private
cat .gitignore.private >> .gitignore

# Manual switch to team
cat .gitignore.team >> .gitignore

# Validate setup
bash 00-Meta/validate-setup.sh

# Check current mode
cat .gitignore | grep "PM-Brain:"
```

-----

**Questions?** See `00-Meta/README.md` or review `.gitignore` comments for more details.

**Ready to choose?** Run `bash 00-Meta/SETUP.sh` now.
