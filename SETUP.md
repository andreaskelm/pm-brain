# 🚀 PM Brain Setup Guide

> **Welcome!** This guide will help you get your PM Brain repository configured and ready to use. No technical knowledge required—just follow the steps.

## 📋 Quick Start Checklist

- [ ] Clone or fork the repository
- [ ] Read this SETUP guide
- [ ] Review the main README.md
- [ ] Read [GUIDELINES.md](./GUIDELINES.md) for best practices
- [ ] Customize Company Context (Priority 1)
- [ ] Review AI/Agent configuration (if using Cursor or similar)
- [ ] Try your first framework
- [ ] Set up your first initiative

---

## 🎯 Step 1: Get the Repository

### Option A: Clone (Recommended for Personal Use)

If you want to use this as your personal PM brain:

```bash
git clone https://github.com/andreaskelm/pm-brain.git
cd pm-brain
```

### Option B: Fork (Recommended for Team/Company Use)

If you want to customize this for your team or company:

1. Click "Fork" on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/pm-brain.git
   cd pm-brain
   ```

**Why fork?** You can keep company-specific context private while still pulling updates from the main repository.

---

## 📚 Step 2: Understand the Structure

Before customizing, understand what each folder does:

```
pm-brain/
├── 01-Company-Context/        # 🏢 YOUR company vision, strategy, stakeholders
├── 02-Methods-and-Tools/      # 🧭 Frameworks & templates (mostly ready to use)
├── 03-Research-Artifacts/     # 🔍 Your research notes and findings
└── 04-Initiatives/            # 🚧 Your active product work
```

**Key insight:** 
- `01-Company-Context/` = **YOU MUST CUSTOMIZE THIS** (your company info)
- `02-Methods-and-Tools/` = **READY TO USE** (frameworks work as-is, customize if needed)
- `03-Research-Artifacts/` = **YOUR RESEARCH** (add your interview notes, findings)
- `04-Initiatives/` = **YOUR WORK** (document your active initiatives)

---

## ⚙️ Step 3: Required Customizations (Priority Order)

### Priority 1: Company Context (`01-Company-Context/`)

**This is the most important step.** Replace placeholder content with your actual company information.

#### Files to Update:

1. **`1-company-vision.md`**
   - Your company's vision statement
   - What you're building toward
   - Long-term aspirations

2. **`2-company-strategy.md`**
   - Strategic goals and priorities
   - How you win in the market
   - Key strategic decisions

3. **`3-company-product-principles.md`**
   - Product principles that guide decisions
   - What "good" looks like for your product
   - Non-negotiables

4. **`4-company-product-explanation.md`**
   - What your product does
   - Who it's for
   - How it creates value

5. **`5-company-roadmap.md`**
   - High-level roadmap (if you have one)
   - Major themes and initiatives
   - Timeline overview

6. **`6-company-stakeholders.md`**
   - Key stakeholders and their roles
   - Decision-makers
   - Who to involve when

**How to update:**
- Open each file
- Replace `[Placeholder]` text with your actual content
- Keep the structure, customize the content
- Commit your changes: `git commit -am "Add company context"`

**Time estimate:** 1-2 hours for all files

---

### Priority 2: AI/Agent Configuration (If Using Cursor or Similar IDE)

If you're using **Cursor** (or similar AI-powered IDE), the repository includes agent configuration files.

#### Location: `.cursor/rules/`

**Files:**
- `AGENTS.md` (root) - PM Brain Assistant instructions (source of truth, already configured)
- `.cursor/rules/AGENTS.template.md` - Template/guide for creating custom agents (separate from root `AGENTS.md`)
- `thinking.mdc` - High-level thinking support rules
- `thinking.personal.mdc` - Personal context (you can customize this)

**What to do:**
1. **Review** `AGENTS.md` (root) - Understand how the PM Brain Assistant is configured
2. **Customize** `.cursor/rules/thinking.personal.mdc` - Add your personal context, preferences, working style
3. **Optional:** Use `AGENTS.template.md` to create additional custom agents if needed
4. **Optional:** Add company-specific rules if needed

**Example personal context to add:**
```markdown
# Personal Context

## Working Style
- I prefer detailed explanations
- I like examples with real scenarios
- I want to understand the "why" behind recommendations

## Common Challenges
- I struggle with stakeholder alignment
- I need help prioritizing competing requests
- I want to improve my product sense

## Goals
- Become better at discovery
- Improve my communication with engineering
- Build stronger product intuition
```

**Time estimate:** 15-30 minutes

---

### Priority 3: Optional Customizations

#### Customize Templates (If Needed)

The templates in `02-Methods-and-Tools/` work as-is, but you can customize them for your workflows:

- **PRD Template** (`2.3-Execution/2.3.4-PRD/2-prd-template.md`) - Add company-specific sections
- **Meeting Agendas** (`2.4-Communication/2.4.2-Meeting-Agendas/`) - Add your team's standard agenda items
- **One-Pagers** (`2.4-Communication/2.4.3-One-Pagers/`) - Customize for your communication style

**When to customize:**
- Your team has specific requirements
- You want to add company-specific sections
- You've found a better structure through experience

**When NOT to customize:**
- First time using the framework (try it as-is first)
- You're not sure what to change (use it, then iterate)

---

## 🧪 Step 4: Try Your First Framework

**Don't wait until you need it!** Try a framework now to get familiar with the system.

### Recommended First Framework: PRD

1. **Navigate to:** `02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/`
2. **Read:** `README.md` (overview)
3. **Read:** `1-prd-framework.md` (how to think about PRDs)
4. **Use:** `2-prd-template.md` (copy and fill out)

**Or try:**
- **OKRs:** `2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/` - Great for goal-setting
- **Opportunity Assessment:** `2.2-Discovery/2.2.4-Opportunity-Assessment/` - For evaluating new ideas
- **Meeting Agendas:** `2.4-Communication/2.4.2-Meeting-Agendas/` - For better meetings

**Pro tip:** Use the "braindump first" approach mentioned in each framework. Don't jump straight to templates—think first, structure second.

---

## 📝 Step 5: Set Up Your First Initiative

Create your first initiative folder to see how the system works:

1. **Navigate to:** `04-Initiatives/`
2. **Create a new folder:** `4.2-Your-Initiative-Name/` (or use the example: `4.1-Initiative-Codename/`)
3. **Copy the structure from the example:**
   - `README.md`
   - `summary.md`
   - `opportunity-assessment.md`
   - `prd.md`
   - `roadmap.md`
   - `decisions.md`

4. **Start with:** `summary.md` - Write a brief summary of what you're working on

**This is where you'll do your actual product work!**

---

## 🤖 Step 6: Using with AI Tools

### Option A: Cursor (Recommended for Technical Users)

If you're using **Cursor**:

1. **Open the repository** in Cursor
2. **The AI already knows** about the repository structure (via root `AGENTS.md` which defines the PM Brain Assistant)
3. **Use slash commands** for common workflows:
   - `/start` - Launch a new initiative end-to-end
   - `/review` - Review documentation for issues
   - `/day` - Plan your day with PM rituals
   - `/week` - Plan your week with strategic focus
   - `/focus` - Get help when you're stuck or need focus
   - `/unstuck` - Get unstuck from blockers
   - `/navigate` - Find the right framework for your situation
   - `/bias` - Check for cognitive biases in your thinking
   
   See `.cursor/commands/` for full command documentation.
4. **Ask questions like:**
   - "How do I write a PRD?"
   - "Help me create an opportunity assessment"
   - "What framework should I use for [situation]?"

The AI will reference the correct files and guide you through the process.

### Option B: ChatGPT, Claude, Gemini (Copy-Paste Method)

1. **Browse** to the framework you need
2. **Copy** the README + framework + template files
3. **Paste** into your AI chat with a prompt like:
   ```
   Here's the PRD framework I use. First, help me braindump my thoughts 
   on [feature]. Then help me fill out the template.
   ```

### Option C: Upload to AI Projects

Many AI tools support "Projects" where you can upload files:

- **ChatGPT:** Create a GPT and upload key files
- **Claude:** Use Claude Projects feature
- **GitHub Copilot:** Point it at this repository

---

## ✅ Step 7: Verify Your Setup

Run through this checklist to ensure everything is configured:

- [ ] Company Context files updated with your information
- [ ] Agent rules reviewed (if using Cursor)
- [ ] Tried at least one framework successfully
- [ ] Created your first initiative folder
- [ ] Understand where to store research (`03-Research-Artifacts/`)
- [ ] Know where to document active work (`04-Initiatives/`)

---

## 🆘 Common Questions

### "Do I need to install anything?"

**No!** This is a markdown-based system. You just need:
- A text editor (VS Code, Cursor, Notepad, etc.)
- Git (if you want version control)
- Optional: AI tool (Cursor, ChatGPT, Claude, etc.)

### "What if I make a mistake?"

**No problem!** This is git-versioned:
- `git status` - See what changed
- `git diff` - See exact changes
- `git checkout -- <file>` - Undo changes to a file
- `git log` - See your history

### "Can I use this with my team?"

**Yes!** 
- Fork the repo for your team
- Customize Company Context together
- Share frameworks and templates
- Use git to collaborate

### "How do I keep it updated?"

If you forked from the main repo:
```bash
# Add the original repo as upstream
git remote add upstream https://github.com/andreaskelm/pm-brain.git

# Pull updates (merge carefully!)
git fetch upstream
git merge upstream/main
```

**Be careful:** Only merge framework updates. Don't overwrite your Company Context!

### "What if I don't know what to customize?"

**Start simple:**
1. Update Company Context (Priority 1)
2. Use frameworks as-is
3. Customize only when you discover a need

**Don't optimize prematurely!** Use the system first, then improve it.

---

## 🎓 Next Steps

Once you're set up:

1. **Read the main README.md** - Understand the philosophy
2. **Browse frameworks** - See what's available in `02-Methods-and-Tools/`
3. **Start using it** - Don't wait for perfect setup, start with real work
4. **Iterate** - Customize as you learn what works for you

---

## 📚 Additional Resources

- **Main README:** `README.md` - Overview and philosophy
- **Guidelines:** `GUIDELINES.md` - Best practices for using and maintaining your PM brain (linking to external sources, collaboration, etc.)
- **Agent Configuration:** `AGENTS.md` (root) - PM Brain Assistant instructions. Use `.cursor/rules/AGENTS.template.md` to create additional custom agents if needed
- **Framework Navigation:** `02-Methods-and-Tools/README.md` - Find the right framework
- **Credits:** `CREDITS.md` - Attribution for frameworks and methods

---

## 💡 Pro Tips

1. **Braindump first, structure second** - Every framework encourages this. Don't skip it!
2. **Use git commits** - Commit after each major update. Your git history becomes your thinking log.
3. **Start small** - Don't try to set up everything at once. Use it, then improve it.
4. **Keep it updated** - Company Context should reflect current reality. Update it regularly.
5. **Share learnings** - If you improve a framework, consider contributing back!

---

## 🐛 Troubleshooting

### "I can't find a framework for X"

- Check `02-Methods-and-Tools/README.md` for navigation
- Search the repository for keywords
- Check `TODO.md` to see what's planned

### "The AI assistant doesn't understand my question"

- Make sure you're in the repository directory
- Check that `AGENTS.md` (root) exists (this defines the PM Brain Assistant)
- Try rephrasing your question more specifically

### "I'm overwhelmed by all the files"

- **Start with Company Context** - That's the most important
- **Pick one framework** - Try PRD or OKRs
- **Use it for real work** - You'll learn as you go

---

## ✨ You're Ready!

You've completed the setup. Now go build great products! 🚀

**Remember:** This is a living system. It should evolve with you. Don't be afraid to customize, experiment, and improve it.

---

**Questions?** Check the main `README.md` or explore the framework folders. The system is designed to be self-explanatory as you use it.

**Created by:** [Andreas Kelm](https://github.com/andreaskelm)  
**Last updated:** 13-01-2026
