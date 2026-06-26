<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/resources/ai-use-case-discovery-and-prioritizer-2026-05-07 -->

[Champions](/en/public/clubs/champions-ecqup/overview)

[navigation.content](/en/public/clubs/champions-ecqup/content)

# Evaluate AI workflow readiness

![Evaluate AI workflow readiness](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Evaluate-AI-workflow-readiness-style-thumb-dc9c0392-1dde-4b71-9af6-42e6f6d4248c-1781279990702.jpeg?fit=scale-down&width=1200)

# Deployment & Adoption

# Workplace & Business

# Activators

# Leaders & Admins

# Codex for Work

# Use Cases

## Turn a real workflow problem into a clear recommendation to test now, validate further, sequence later, or avoid for now.

May 7, 2026 · Last updated on June 12, 2026

![Evaluate AI workflow readiness](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Evaluate-AI-workflow-readiness-style-thumb-dc9c0392-1dde-4b71-9af6-42e6f6d4248c-1781279990702.jpeg?fit=scale-down&width=1200)

# Purpose

This resource gives Champions a consistent way to identify, evaluate, and compare AI workflow opportunities inside their organization.

Instead of beginning with a broad idea such as “we should use AI for this,” it begins with a real workflow problem and helps determine whether the opportunity is valuable, feasible, and ready to move forward.

## Why It Matters

Teams often prioritize AI ideas based on enthusiasm, visibility, or technical possibility rather than the quality of the underlying workflow opportunity.

A stronger evaluation looks at:

* how often the workflow occurs

* how many people or teams it affects

* what friction, delay, rework, or risk exists today

* whether the process is understood and stable enough to improve

* what systems, approvals, data, or teams are involved

* whether the likely value justifies the effort required

This helps organizations avoid spending time on highly visible but low-value ideas while overlooking smaller workflow improvements that could create meaningful adoption momentum.

## How to Use It

### For Leaders

Compare opportunities across teams, identify where investment or sponsorship may be needed, and decide which workflows should be tested, sequenced, or deprioritized.

Use the output to explain why one opportunity should move forward before another and what conditions must be met before a larger initiative begins.

### For Activators

Turn a specific team frustration into a better-scoped workflow opportunity.

Use the output to identify a practical first test, surface hidden dependencies, and bring a more complete recommendation to Leaders, functional owners, Workspace Admins, or technical partners.

# What makes a strong workflow opportunity?

A strong opportunity is grounded in an observable problem, not only an interesting AI idea.

Useful evidence may include:

* a task that happens frequently or affects many people

* repeated delays, handoffs, or manual workarounds

* avoidable rework, errors, or inconsistent outputs

* a process that employees regularly ask for help completing

* a measurable amount of time spent on repetitive work

* a workflow that prevents a team from acting on information quickly

* a clear user group willing to test a different approach

Statements such as “AI could probably save time” or “this would make a good demo” are not sufficient on their own.

# The evaluation framework

### 1. Potential value

Assess:

* **Frequency:** How often does the workflow occur?

* **Reach:** How many people, teams, or customers are affected?

* **Friction:** What time, effort, delay, rework, or risk exists today?

* **Repeatability:** Could a successful approach be reused by others?

* **Relevance:** Does improving this workflow support a meaningful team or business priority?

### 2. Complexity and effort

Assess:

* **Process complexity:** Is the workflow clear and consistent, or highly variable?

* **Readiness:** Do the users, owner, and process exist to support a test?

* **Governance and approvals:** Are security, legal, policy, or functional approvals required?

* **System dependencies:** Does the workflow require access to tools, data, APIs, or connected systems?

* **Cross-functional dependencies:** How many teams, decisions, or handoffs are involved?

* **Change effort:** How much behavior, training, or process change would be required?

### 3. Hidden workflow complexity

The evaluator should also surface:

* upstream and downstream dependencies

* manual workarounds

* unclear ownership

* duplicated steps

* approval bottlenecks

* places where people compensate for gaps in the process

* parts of the workflow that should be fixed before AI is introduced

Common Failure Mode: Do not use this resource to justify a predetermined AI solution. If the workflow problem is unclear, the process is unstable, or the expected value is based only on assumptions, the correct recommendation may be to investigate the workflow further before designing or testing an AI solution.

# Skill Spec

```
Act as an AI workflow opportunity evaluator.

Your job is to help a Leader or Activator turn a real workflow problem into a clear, evidence-based recommendation about whether to:

Test now

Validate further

Sequence later

Avoid for now

Base the evaluation only on the information provided. Do not invent business impact, user demand, technical feasibility, ROI, or organizational readiness.

What to optimize for

* Start with the workflow problem, not the proposed AI solution.

* Distinguish observed evidence from assumptions.

* Identify hidden process and organizational complexity.

* Make the reasoning understandable to business, functional, and technical partners.

* Recommend the smallest useful next step.

* Avoid labeling an opportunity a “quick win” if meaningful approvals, dependencies, or behavior change are unresolved.

* Do not assume every workflow problem should be solved with AI.

Inputs I will provide

* Role using this evaluator: Leader or Activator

* Workflow or process

* Users and teams involved

* How often the workflow occurs

* Current steps

* Current pain points

* Manual workarounds

* Time, quality, risk, or experience impact

* Evidence supporting the problem

* Desired outcome

* Existing owner

* Upstream and downstream dependencies

* Systems, tools, and data involved

* Governance, security, legal, or policy considerations

* Functional approvals required

* User readiness

* Technical readiness

* Known constraints

* Proposed AI approach, if one already exists

* Other opportunities being considered

Return the output in this structure

Executive summary

Provide four to six bullets covering:

* the workflow problem

* the strongest evidence of potential value

* the largest source of complexity

* the current readiness level

* the recommended action

* the most important next step

Workflow definition

Summarize:

* who performs the workflow

* what they are trying to accomplish

* where the current process breaks down

* what a better outcome would look like

If the workflow is too broad or unclear to evaluate, say so and provide the questions needed to narrow it.

Evidence and assumptions

Separate the input into:

* Known

* Direct observations, data, user feedback, or confirmed process facts

* Inferred

* Reasonable interpretations that still require validation

* Unknown

* Missing information that could change the recommendation

Potential value assessment

Assess each dimension as Low, Medium, or High and explain why:

* Frequency

* Reach

* Current friction

* Repeatability

* Connection to a meaningful team or business priority

Do not combine these into a precise numerical ROI estimate unless sufficient validated data is provided.

Complexity and effort assessment

Assess each dimension as Low, Medium, or High and explain why:

Process complexity

* Cross-functional dependencies

* System and data dependencies

* Governance and approvals

* Change and enablement effort

* Technical effort

* Ownership clarity

Readiness assessment

Assess whether the opportunity has:

* a clear workflow

* a defined user group

* a willing test group

* a process owner

* sufficient access to tools and data

* the necessary approvals

* a measurable first outcome

Rate overall readiness as:

* Ready to test

* Needs validation

* Not ready yet

Hidden complexity and workflow risks

Identify:

* handoffs

* workarounds

* unclear ownership

* upstream and downstream dependencies

* process issues that AI may conceal rather than solve

* risks that could make a successful demo difficult to adopt in real work

Recommendation

Choose one:

* Test now: Use when the workflow has credible potential value, manageable complexity, a clear owner, real users, and enough readiness for a limited test.

* Validate further: Use when the opportunity may be valuable but important assumptions about the workflow, users, evidence, or solution still need to be tested.

* Sequence later: Use when the opportunity may be valuable but depends on significant approvals, systems, process changes, ownership decisions, or other work that should happen first.

* Avoid for now: Use when the likely value is low, the problem is poorly defined, the effort is disproportionate, or AI is unlikely to address the real source of friction.

Explain the recommendation in plain language.

Recommended next step

Provide:

* the smallest useful next action

* who should own it

* who should be involved

* what question the next step should answer

* what evidence would justify moving forward

If testing is recommended, define a lightweight first test:

* Test group

* Workflow boundary

* Capability or approach to test

* Duration

* Evidence to collect

* Success signal

* Stop or reconsider signal

Comparison table

If multiple opportunities are provided, return a table containing:

* Opportunity

* Potential value

* Complexity

* Readiness

* Key dependency

* Recommendation

* Rationale

Champion notes

Include:

* what the Leader or Activator should validate before sharing the recommendation

* which partners should be involved next

* what claims should not yet be made

* what would need to change for the opportunity to move into a different recommendation category

```

### ﻿

# Input template

```
Role using this evaluator:
[Leader or Activator]

Workflow or process:
[Describe the specific workflow, not only the proposed AI solution.]

Users and teams involved:
[Who performs, owns, supports, or is affected by the workflow?]

How often the workflow occurs:
[Daily, weekly, monthly, occasionally, or another frequency.]

Current steps:
[Describe the major steps, handoffs, and approvals.]

Current pain points:
[Where does the workflow create delay, rework, confusion, inconsistency, risk, or poor experience?]

Manual workarounds:
[What are people doing today to compensate for problems in the process?]

Evidence supporting the problem:
[Include available data, observations, user feedback, time spent, error patterns, repeated requests, or other direct evidence.]

Desired outcome:
[What should become faster, easier, safer, clearer, or more consistent?]

Existing owner:
[Who owns the workflow or outcome today?]

Upstream and downstream dependencies:
[What must happen before and after this workflow?]

Systems, tools, and data involved:
[What access or integrations may be required?]

Governance, security, legal, or policy considerations:
[What requirements or sensitivities may apply?]

Functional approvals required:
[Who must approve a change to the workflow?]

User readiness:
[Are real users willing and able to test a new approach?]

Technical readiness:
[Are the needed capabilities, data, and systems available?]

Known constraints:
[Include timing, capacity, policy, technology, or process constraints.]

Proposed AI approach:
[Optional. Describe an existing idea without assuming it is the correct solution.]

Other opportunities being considered:
[Optional. Include these if you want a comparison.]
```

# Step-by-Step guide

1. Choose one real workflow problem to evaluate.

2. Gather the clearest evidence available about frequency, reach, friction, and current workarounds.

3. Identify the people, systems, approvals, and dependencies involved.

4. Complete the input template.

5. Paste the Skill Spec and completed inputs into ChatGPT.

6. Review the known, inferred, and unknown information before accepting the recommendation.

7. Validate the output with the workflow owner and relevant functional, admin, or technical partners.

8. Use the recommendation to decide whether to test, investigate further, sequence the work, or stop.

# Expected outcome

A strong evaluation should produce:

* a clearly defined workflow problem

* a grounded view of potential value

* a realistic picture of complexity and readiness

* visibility into hidden dependencies and ownership gaps

* a specific recommendation

* a practical next step

* clearer reasoning for why the opportunity should move forward now, later, or not at all

The output should help Champions make better sequencing and investment decisions and bring better-scoped, more credible workflow opportunities to the people who can support them.

Like

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

Table Of Contents

[The AI Champion role](/en/public/clubs/champions-ecqup/resources/the-ai-champion-role)

[Run an AI hackathon](/en/public/clubs/champions-ecqup/resources/hackathon-playbook-2025-09-15)

[Build and grow a network of local AI Activators](/en/public/clubs/champions-ecqup/resources/grow-a-network-of-internal-champions)

[Prioritize AI workflow opportunities](/en/public/clubs/champions-ecqup/resources/workflow-discovery-and-prioritization-matrix-2026-05-05)

May 5th, 2026 • Views 244

[Debug AI adoption blockers](/en/public/clubs/champions-ecqup/resources/chatgpt-adoption-playbook-from-activation-to-value-realization-2026-03-24)

Apr 20th, 2026 • Views 517

[13:00](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Video

[Workflow clip: Automate CRM updates with Codex](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Jun 18th, 2026 • Views 56

[11:00](/en/public/clubs/champions-ecqup/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

Video

[Workflow clip: Proactively monitor accounts with Codex](/en/public/clubs/champions-ecqup/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

Jun 12th, 2026 • Views 79

[Prioritize AI workflow opportunities](/en/public/clubs/champions-ecqup/resources/workflow-discovery-and-prioritization-matrix-2026-05-05)

May 5th, 2026 • Views 244

[13:00](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Video

[Workflow clip: Automate CRM updates with Codex](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Jun 18th, 2026 • Views 56

[11:00](/en/public/clubs/champions-ecqup/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

Video

[Workflow clip: Proactively monitor accounts with Codex](/en/public/clubs/champions-ecqup/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12)

Jun 12th, 2026 • Views 79

[Debug AI adoption blockers](/en/public/clubs/champions-ecqup/resources/chatgpt-adoption-playbook-from-activation-to-value-realization-2026-03-24)

Apr 20th, 2026 • Views 517
