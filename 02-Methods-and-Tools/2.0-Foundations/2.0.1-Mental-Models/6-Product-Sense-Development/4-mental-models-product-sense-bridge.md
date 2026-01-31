# Mental Models ↔ Product Sense Bridge

**Purpose:** Connect the mental models in this folder to product sense so you know *when* and *how* to use each one during braindumps and product decisions.

Product sense isn't magic—it's the disciplined application of mental models to product decisions. This doc bridges [1-Decision-Making](../1-Decision-Making/) and [2-Product-Thinking](../2-Product-Thinking/) to the braindump prompts in [2-product-sense-prompts.md](2-product-sense-prompts.md) and the golden rule in [PRODUCT-SENSE-RULES.md](../../../../../PRODUCT-SENSE-RULES.md).

---

## How to Use This Bridge

- **Before a braindump:** Pick 1–2 mental models that fit your situation (see "When product sense uses this" and "When to use in the repo" below).
- **During a braindump:** Use the core question from that model; don't just answer the template prompts mechanically.
- **After a braindump:** Check whether you actually applied the model (e.g. did you ask "and then what?" twice?).
- **When opening a framework:** Use the "When to use in the repo" links so the right mental model is in mind before you fill a PRD, prioritization, or strategy doc.

---

## Core Mental Models for Product Sense

### 1. Second-Order Thinking ("And then what?")

**What it is:** Thinking beyond the immediate effect to "And then what happens?"—for users, the product, the team, or the business.

**Why it matters for product sense:** Core to anticipating unintended consequences; separates good PMs from exceptional ones. The braindump template's "If this works, what second-order effects…?" is this model in action.

**How to apply (example):**
```
Decision: Add "export to CSV" feature
├─ First-order: Users can export their data
├─ Second-order: Users might use Excel instead of our analytics
├─ Third-order: We lose visibility into their workflows
└─ Fourth-order: Product development slows because we lack usage data
```

**When product sense uses this:**
- Before launching features (what systemic effects?)
- When setting strategy (what does this unlock or block?)
- During discovery (what happens if users adopt this behavior?)

**In this repo:** No standalone doc; it's baked into [2-product-sense-prompts.md](2-product-sense-prompts.md) (Always-Ask Core Prompts, Problem Clarity, Future Vision) and the 30-second pre-flight in [PRODUCT-SENSE-RULES.md](../../../../../PRODUCT-SENSE-RULES.md).

**When to use in the repo:** Before [PRD](../../../2.3-Execution/2.3.4-PRD/README.md) (Problem Clarity, second-order effects); before [Strategy/OKR](../../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md) (what does this unlock or block?); before [Opportunity Assessment](../../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) (if users adopt this, then what?).

**Practice:** For any decision today, ask "and then what?" at least twice. Write: immediate effect → behavioral change → systemic impact. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/) or use [JUDGE-1: Make a Prediction](templates/1-daily-practice-exercises.md) (predict outcome, check in 3 months).

---

### 2. Inversion ("What could go wrong?")

**What it is:** Instead of "How do I succeed?", ask "How could I fail?" to surface edge cases and assumptions.

**Why it matters for product sense:** Primary tool for identifying edge cases and revealing assumptions you're making. Forces defensive thinking before offense.

**How to apply (example):**
```
Normal: "How do we make onboarding great?"
Inversion: "How could we make new users quit immediately?"
↓
Reveals: Confusing navigation, unclear value prop, friction points, fear of breaking something
```

**When product sense uses this:**
- Before writing PRDs (what could go wrong?)
- During design reviews (how could users break this?)
- In pre-mortems before launch

**In this repo:** [Pre-mortems](../1-Decision-Making/1-pre-mortems.md) — imagine the project has failed and work backward (Tigers, Paper Tigers, Elephants).

**When to use in the repo:** Before [PRD](../../../2.3-Execution/2.3.4-PRD/README.md) (what could go wrong?); during design reviews; before launch—run a formal pre-mortem using [Pre-mortems](../1-Decision-Making/1-pre-mortems.md). [TEAR-2: "Why This Sucks"](templates/1-daily-practice-exercises.md) practices inversion on existing products.

**Practice:** For any feature, list 5 ways it could fail. Which are preventable? Design to prevent the top 2. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/).

---

### 3. First Principles

**What it is:** Break the problem down to fundamental truths; question assumptions and conventions; rebuild from scratch.

**Why it matters for product sense:** Connects to "Product Motivation" (why does this exist?); helps avoid cargo-culting competitor features; reveals when frameworks don't apply.

**How to apply (example):**
```
Surface question: "Should we add dark mode?"
First principles:
├─ What problem are we solving? (Eye strain, preference, accessibility)
├─ What are true constraints? (Engineering cost, design consistency)
├─ What are just conventions? (Everyone has dark mode)
└─ What would we do if we started fresh?
```

**When product sense uses this:**
- Evaluating feature requests (what's the real need?)
- Avoiding cargo-culting competitor features
- When "how we've always done it" is blocking a better solution

**In this repo:** [First Principles](../1-Decision-Making/4-first-principles.md).

**When to use in the repo:** Before [Opportunity Assessment](../../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) (what's the real need?); when evaluating feature requests for [PRD](../../../2.3-Execution/2.3.4-PRD/README.md); before [JTBD](../../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md) (go five whys deep). [TEAR-1: Feature Forensics](templates/1-daily-practice-exercises.md) practices first principles on one feature.

**Practice:** For a feature request, ask "Why does the user want this?" five levels deep. What fundamental need does this serve? **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/).

---

### 4. One-Way vs Two-Way Doors

**What it is:** Match decision speed to reversibility. Two-way doors = reversible, decide fast. One-way doors = hard to undo, slow down and align.

**Why it matters for product sense:** Stops overthinking reversible bets and underthinking irreversible ones. The template's "Is this reversible? If yes, bias toward action" is this model.

**When product sense uses this:**
- Prioritization (is this reversible? bias toward action if yes)
- When stuck (if reversible, try something and set a review date)
- Before big bets (architecture, partnerships, strategy)

**In this repo:** [One-Way vs Two-Way Doors](../1-Decision-Making/2-one-way-two-way-doors.md).

**When to use in the repo:** Before [Prioritization](../../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/README.md) (reversible? bias toward action); when using [3-product-sense-evaluation.md](3-product-sense-evaluation.md) (stuck); before [Roadmap](../../../2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/README.md) (which bets are one-way?). [JUDGE-3: Fast Prioritization Drill](templates/1-daily-practice-exercises.md) — rank 5 ideas in 5 min, name one-way vs two-way.

**Practice:** For your next decision, name it: one-way or two-way? If two-way, set a "decide by" date and move. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/) or [2-prioritization-decision-log](../../../../../00-Meta/2-prioritization-decision-log.md).

---

### 5. Pre-mortems (Inversion in a process)

**What it is:** Assume the project has failed; work backward to find what went wrong. Surfaces Tigers (real threats), Paper Tigers (perceived but not dangerous), Elephants (unspoken truths).

**Why it matters for product sense:** Inversion turned into a repeatable process. Use before launch or big bets to surface what you're not saying out loud.

**When product sense uses this:**
- Early in a project or before major commitments
- When the team is overly optimistic
- Before launches or high-stakes decisions

**In this repo:** [Pre-mortems](../1-Decision-Making/1-pre-mortems.md).

**When to use in the repo:** Early in [Opportunity Assessment](../../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) or before [PRD](../../../2.3-Execution/2.3.4-PRD/README.md) commitment; before [Roadmap](../../../2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/README.md) big bets. Run the full process in [Pre-mortems](../1-Decision-Making/1-pre-mortems.md) (Tigers, Paper Tigers, Elephants).

**Practice:** Before a key decision, ask: "Imagine this failed in 6 months—what went wrong?" Prioritize mitigating Tigers first. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/).

---

### 6. Opportunity Cost

**What it is:** The value of the best alternative you give up when you choose something. "What are we NOT doing if we do this?"

**Why it matters for product sense:** The template's "What are we NOT doing if we do this?" and "Who loses from this?" are opportunity-cost lenses. Every yes is a no somewhere else.

**When product sense uses this:**
- Prioritization (what are we not doing? what's the second-best option?)
- Strategy (what doors does this open or close?)
- Tradeoff discussions (who loses? what do we sacrifice?)

**In this repo:** [Opportunity Cost](../1-Decision-Making/5-opportunity-cost.md).

**When to use in the repo:** Before [Prioritization](../../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/README.md) (what are we NOT doing?); in [Strategy](../../../2.1-Strategy/2.1.1-Strategic-Foundations/) (what doors does this open or close?); in braindump "Before Making a Prioritization Decision" in [2-product-sense-prompts.md](2-product-sense-prompts.md).

**Practice:** For any "yes," name the single best "no" and why you're okay with that tradeoff. **Log in:** [00-Meta/2-prioritization-decision-log](../../../../../00-Meta/2-prioritization-decision-log.md) for big bets.

---

### 7. Regret Minimization

**What it is:** Choose the path that minimizes long-term regret. "1 year from now, which option would I regret NOT trying?"

**Why it matters for product sense:** Unsticks high-stakes or irreversible choices. The decision diagnostic's "Which failure would I be okay with?" is this lens.

**When product sense uses this:**
- High-stakes or irreversible choices
- When you're stuck between safe vs. bold
- Career or strategy decisions with uncertain outcomes

**In this repo:** [Regret Minimization](../1-Decision-Making/6-regret-minimization.md).

**When to use in the repo:** When stuck—use [3-product-sense-evaluation.md](3-product-sense-evaluation.md) ("Regret Minimization" and "Two-Way Door" sections); before [Strategy](../../../2.1-Strategy/2.1.1-Strategic-Foundations/) or [OKR](../../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md) (1 year from now, which would I regret NOT trying?). [JUDGE-1: Make a Prediction](templates/1-daily-practice-exercises.md) + follow-up builds regret-minimization muscle.

**Practice:** For a hard decision, ask: "Which failure would I be okay with (learned something)? Which would I not be okay with (negligent)?" **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/) or decision showcase in [0.2-Growth-Portfolio](../../../../../00-Meta/0.2-Growth-Portfolio/2-decision-showcase.md).

---

### 8. Assumptions Framework

**What it is:** When two people disagree about product strategy, they have different assumptions. Pause solution debate; surface and align on assumptions (users, market, constraints) before revisiting solutions.

**Why it matters for product sense:** The braindump prompt "What assumptions am I making? What don't I actually know yet?" is this model. Aligning on assumptions creates genuine conviction, not checkbox agreement.

**When product sense uses this:**
- During braindumps (list assumptions explicitly; which are critical? test those first)
- When stakeholders disagree (what assumptions lead each person to their view?)
- Before building roadmaps (ensure shared foundation)

**In this repo:** [Assumptions Framework](../1-Decision-Making/3-assumptions-framework.md).

**When to use in the repo:** In every braindump—[2-product-sense-prompts.md](2-product-sense-prompts.md) "What assumptions am I making?"; when stakeholders disagree—[Assumptions Framework](../1-Decision-Making/3-assumptions-framework.md) (align on beliefs before solutions); before [Roadmap](../../../2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/README.md) (shared foundation). [Alignment Check](../5-Team-Dynamics/1-alignment-check.md) combines with this for team decisions.

**Practice:** Before a key decision, write down your recommendation and list 5–10 assumptions. For each: How do I know? What would falsify it? Which are critical? Test those before deciding. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/).

---

### 9. Outcome vs Output

**What it is:** Output = what you build (features, releases). Outcome = what you achieve (behavior change, metrics moved, value delivered). Favor outcomes first; then choose outputs that drive them.

**Why it matters for product sense:** Stops feature-factory thinking. The template's "What metrics actually change if this succeeds?" and "What job is this doing for them?" are outcome lenses.

**When product sense uses this:**
- Defining success (are we measuring output or outcome?)
- Before PRDs (what outcome does this serve?)
- Prioritization (what outcome per dollar/hour?)

**In this repo:** [Outcome vs Output](../2-Product-Thinking/1-outcome-vs-output.md); [Feature Factory](../2-Product-Thinking/3-feature-factory.md) (diagnostic when output-heavy).

**When to use in the repo:** Before [OKR](../../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md) (outcome-based goals); before [PRD](../../../2.3-Execution/2.3.4-PRD/README.md) (what outcome does this serve?); in [Prioritization](../../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/README.md) (outcome per dollar/hour). Braindump "What metrics actually change if this succeeds?" in [2-product-sense-prompts.md](2-product-sense-prompts.md).

**Practice:** For any feature, state the outcome first ("Increase X by Y") then the output ("Ship Z"). If you can't state the outcome, don't ship yet. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/).

---

### 10. Jobs vs Features

**What it is:** Reframe from "ship this feature" to "what job is the user hiring this for?" Job = desired progress in context. Feature requests are signals of underlying jobs; multiple solutions can serve one job.

**Why it matters for product sense:** The template's "What job is this doing for them?" is this model. Prevents solution-first thinking; surfaces the real need.

**When product sense uses this:**
- Before PRDs (what job are they hiring this feature to do?)
- Discovery (what progress are they trying to make?)
- Roadmap (organize by jobs, not feature list)

**In this repo:** [Jobs vs Features](../2-Product-Thinking/5-jobs-vs-features.md).

**How to apply (example):** Stakeholders ask for "export to CSV." Reframe: "When analysts share results, they want reusable outputs to avoid rework." Solutions: exports, shared views, email digests. Test the one that best serves the job.

**When to use in the repo:** Before [PRD](../../../2.3-Execution/2.3.4-PRD/README.md) ("What job are they hiring this feature to do?"); in [Opportunity Assessment](../../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) and [JTBD](../../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md); in [Research Interviews](../../../2.2-Discovery/2.2.1-Research-Interviews/README.md) (what progress are they trying to make?). [OBS-3: JTBD Spotting](templates/1-daily-practice-exercises.md) and [TEAR-1: Feature Forensics](templates/1-daily-practice-exercises.md) practice this.

**Practice:** For any feature request, write: "When I [situation], I want to [progress], so I can [result]." Then list 3 different solutions that could serve that job. **Log in:** [00-Meta/1-daily-log](../../../../../00-Meta/) or [3-research-insight-log](../../../../../00-Meta/3-research-insight-log.md).

---

## Practice Exercises: Where to Do the Reps

| Goal | Where in the repo |
|------|-------------------|
| **Daily 10-min reps** | [templates/1-daily-practice-exercises.md](templates/1-daily-practice-exercises.md) — Observation (OBS), Teardown (TEAR), Cross-Domain (CROSS), Pattern (PATTERN), Judgment (JUDGE) |
| **Log insights** | [00-Meta/1-daily-log-YYYY-QX.md](../../../../../00-Meta/1-daily-log-YYYY-QX.md) — one folder up from repo root |
| **Prioritization decisions** | [00-Meta/2-prioritization-decision-log.md](../../../../../00-Meta/2-prioritization-decision-log.md) |
| **Research/discovery learnings** | [00-Meta/3-research-insight-log.md](../../../../../00-Meta/3-research-insight-log.md) |
| **Decision showcase (evidence)** | [00-Meta/0.2-Growth-Portfolio/2-decision-showcase.md](../../../../../00-Meta/0.2-Growth-Portfolio/2-decision-showcase.md) |
| **Weekly reflection** | [templates/3-weekly-reflection-template.md](templates/3-weekly-reflection-template.md) → copy into [00-Meta/0.1-Learning-Log](../../../../../00-Meta/0.1-Learning-Log/) |
| **Combining models (structured)** | Use the three exercises in "Combining Models" below; log in daily log or decision showcase |

**Which exercise practices which model?**

- **Second-order:** JUDGE-1 (Make a Prediction), JUDGE-2 (Disagree with Popular Opinion)
- **Inversion:** TEAR-2 ("Why This Sucks"), Pre-mortem in [1-pre-mortems.md](../1-Decision-Making/1-pre-mortems.md)
- **First principles:** TEAR-1 (Feature Forensics), OBS-3 (JTBD Spotting)
- **One-way / two-way:** JUDGE-3 (Fast Prioritization Drill), [3-product-sense-evaluation.md](3-product-sense-evaluation.md)
- **Opportunity cost:** JUDGE-3, braindump "Before Making a Prioritization Decision"
- **Regret minimization:** JUDGE-1 + 3-month check-in, [3-product-sense-evaluation.md](3-product-sense-evaluation.md)
- **Assumptions:** Every braindump; [3-assumptions-framework.md](../1-Decision-Making/3-assumptions-framework.md) when disagreeing
- **Outcome vs output:** PATTERN-1 (Principle Hunting), OKR/roadmap work
- **Jobs vs features:** OBS-3 (JTBD Spotting), TEAR-1 (Feature Forensics), [JTBD](../../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md)

---

## Combining Models

Product sense is rarely one model; it's layering them.

**Exercise 1: Second-order + Inversion**
Pick one product decision. (1) Ask "and then what?" twice (second-order). (2) Ask "how could this fail?" and list 5 ways (inversion). (3) Which failure is most likely? Design to prevent it.

**Exercise 2: One-way door + Regret minimization**
For a decision you're stuck on: (1) Is it one-way or two-way? If two-way, set a "decide by" date and move. (2) If one-way, ask: "1 year from now, which option would I regret NOT trying?" Choose that.

**Exercise 3: Jobs + First principles**
For a feature request: (1) State the job ("When I… I want to… so I can…"). (2) Ask "why does the user want this?" five levels deep (first principles). (3) What fundamental need does this serve? (4) What's the smallest output that would validate that outcome?

---

## Situation → Mental Model Map

| Situation      | Mental models to lean on |
|----------------|---------------------------|
| **Strategy**   | Second-order thinking, Opportunity cost, First principles, Outcome vs output |
| **Design**     | Inversion (what could go wrong?), Second-order effects, Jobs (what job does this serve?) |
| **Prioritization** | One-way vs two-way doors, Opportunity cost, Regret minimization, Outcome vs output |
| **Discovery**  | First principles (real need?), Jobs (what job?), Second-order (if users adopt this…), Assumptions |
| **Stuck**      | One-way vs two-way (if reversible, try something), Regret minimization, Assumptions (what am I assuming?) |
| **Crisis**     | Inversion / Pre-mortem (what went wrong?), Second-order (what else could break?) |
| **Stakeholder disagreement** | Assumptions Framework (align on beliefs before solutions) |

---

## Links

- **Start here (entry point):** [0-start-here-product-thinking.md](0-start-here-product-thinking.md)
- **Braindump prompts:** [2-product-sense-prompts.md](2-product-sense-prompts.md)
- **Decision diagnostic (when stuck):** [3-product-sense-evaluation.md](3-product-sense-evaluation.md)
- **Daily practice exercises:** [templates/1-daily-practice-exercises.md](templates/1-daily-practice-exercises.md) — OBS, TEAR, CROSS, PATTERN, JUDGE
- **Where to log:** [00-Meta/](../../../../../00-Meta/) — daily log, prioritization log, research log, growth portfolio
- **Golden rule:** [PRODUCT-SENSE-RULES.md](../../../../../PRODUCT-SENSE-RULES.md)
- **Decision-Making mental models:** [1-Decision-Making/README.md](../1-Decision-Making/README.md)
- **Product-Thinking mental models:** [2-Product-Thinking/README.md](../2-Product-Thinking/README.md)
- **Feature Factory (output-heavy diagnostic):** [3-feature-factory.md](../2-Product-Thinking/3-feature-factory.md) — use when asking "are we measuring output or outcome?"
- **Repo methods (when to use which):** [PRD](../../../2.3-Execution/2.3.4-PRD/README.md) · [Prioritization](../../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/README.md) · [OKR](../../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md) · [Opportunity Assessment](../../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md) · [JTBD](../../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md) · [Strategy](../../../2.1-Strategy/2.1.1-Strategic-Foundations/README.md)
- **Mental Models overview:** [../README.md](../README.md)
