<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/resources/ai-workflow-starter-worksheet-2026-07-07 -->

[Champions](/en/public/clubs/champions-ecqup/overview)

[navigation.content](/en/public/clubs/champions-ecqup/content)

# AI workflow starter worksheet

![AI workflow starter worksheet](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/ai-workflow-starter-worksheet-style-thumb-016a94c8-73a4-464d-a5da-817a5395627d-1783448823465.jpeg?fit=scale-down&width=1200)

# Activators

# champions

# Deployment & Adoption

## Choose one real workflow and prepare it for AI-supported scoping

July 7, 2026

![AI workflow starter worksheet](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/ai-workflow-starter-worksheet-style-thumb-016a94c8-73a4-464d-a5da-817a5395627d-1783448823465.jpeg?fit=scale-down&width=1200)

This worksheet is for people who want to make progress on a real workflow rather than talk about AI in the abstract. Use it before a working session, during a lab, or as intake for a Workspace Agent. You do not need perfect detail. The goal is to capture enough context to choose the right next step.

# AI Workflow Candidate

Name the real work you want to improve and identify who is involved before you decide whether AI belongs in the workflow. At the end of this step, you should be able to describe the workflow in a few sentences, name the owner, identify the users, and explain what starts and ends the work.

* Workflow name: Use a short name that describes the work, not the technology.

* Workflow owner: Who is accountable for the result today?

* Intended users: Who performs, receives, reviews, or depends on the output?

* Trigger: What starts the workflow?

* Output: What must be produced, decided, updated, or shared?

## Prioritization Check

Decide whether your AI workflow candidate is a good place to start now, should be narrowed in scope, or should wait until the process, ownership, data, or approvals are clearer.

At the end of this step, you should be able to assign the AI workflow candidate to one of four categories and make a scope decision: keep it as it, narrow it, or choose a different workflow.

* Frequency: How often does this work happen?

* Repeatability: How similar are the steps each time?

* Value: What would improve if this worked better?

* Complexity: What dependencies, approvals, systems, or edge cases make this harder?

* Risk: What could go wrong if the workflow gives a poor output or acts too broadly?

Use value and complexity together to categorize the workflow.

Value is the expected improvement for users or the business.

Complexity is the effort, dependency, risk, process readiness, system access, governance, and exception load required to make the workflow reliable.

|  |  |  |
| --- | --- | --- |
| Value / Complexity | Category | Sequencing / Prioritization |
| High Value + Low Complexity | Quick Win | Deliver immediate, meaningful value and build momentum. Do first. |
| High Value / High Complexity | Strategic Initiative | Delivers meaningful value, but includes high levels of cross-functional coordination, approvals, process readiness, system access, risk, or exception load. Prioritize after momentum and supporting systems are established, or narrow scope to decrease complexity. |
| Low Value / Low Complexity | Nice-to-Have | Capable of scaling quickly, but value delivered is relatively low. Prioritize only after scaling high-value candidates. |
| Low Value / High Complexity | Thankless Task | Value / impact does not justify effort. Avoid. |

Ultimately, you should be able to assign your AI workflow candidate to one of these categories and determine whether to keep it as is, narrow the scope, or prioritize a different candidate.

# Design Notes

Clarify how the workflow should be improved, where AI can help, and where people must remain accountable.

At the end of this step, you should have a clear desired outcome, initial AI/person boundaries, and at least one condition that should cause the AI workflow to stop, ask, or escalate to human judgement.

* Desired outcome: What should become faster, easier, more consistent, safer, or more useful?

* Friction: Where do delay, rework, inconsistency, or ambiguity show up?

* What AI may help with: List repeatable steps AI could complete, prepare, summarize, classify, draft, or check.

* What people must own: List decisions requiring judgment, authority, accountability, approval, or sensitive context.

* Stop, ask, or escalate conditions: What should cause the workflow to pause and involve a person?

# Develop Notes

Define the smallest useful version and the test cases that will validate whether the workflow behaves as expected.

At the end of this step, you should be able to describe the first bounded version of the AI workflow, required inputs, expected outputs, review points and representative test cases.

* Smallest useful version: What is the narrowest version that would still be useful?

* Required inputs or sources: What information, examples, policies, or systems would the workflow need?

* Expected output: What should the workflow produce, and in what structure?

* Human review point: Who reviews the output before it is used, sent, approved, or acted on?

# Scale Notes

Identify requirements to introduce the workflow to its intended users responsibly after it passes testing.

At the end of this step, you should know who will use the workflow first, who the workflow owner is, where users should be routed when they need help, and what evidence should inform the next decision.

* First user group or introduction scope:

* Workflow owner for follow-through and maintenance:

* Support or escalation route: Where should users go with questions, access issues, errors, or sensitive cases?

* Evidence for the next decision: What would show whether this is useful, safe, and worth continuing?

* Next review moment:

﻿

# Companion Prompt

```
Act as an AI workflow coach for a team exploring whether and how to apply AI to a real workflow.

﻿

﻿

Assume you have no prior context. Use only the notes I provide below. Do not invent facts, approvals, systems, evidence, or outcomes.

﻿

﻿

Frameworks to use:

﻿

- Start with the workflow, not the tool.

﻿

- Value means the expected improvement for users or the business.

﻿

- Complexity means process readiness, dependencies, system access, governance, approvals, edge cases, risk, and support burden.

﻿

- Classify the candidate as one of four categories:

﻿

- Quick Win: meaningful value and lower complexity; good candidate to deliver value quickly and build momentum.

﻿

- Strategic Initiative: meaningful value and high complexity; prioritize only after momentum is established and supporting processes and systems are in place, or break down into a smaller first test and involve owners/partners early.

﻿

- Nice-to-Have: lower value and lower complexity; useful for practice or confidence, but not worth heavy investment.

﻿

- Thankless Task: lower value and high complexity; usually avoid.

﻿

- Separate what AI may complete, what AI may prepare for review, and what people must own.

﻿

- Define stop, ask, or escalate conditions for missing, conflicting, sensitive, urgent, high-impact, or out-of-scope cases.

﻿

- Prefer the smallest useful version that can be tested with real users.

﻿

- Adoption means repeated useful behavior and credible evidence of improvement, not an announcement or one-time demo.

﻿

﻿

Your task:

﻿

1. Review my worksheet notes.

﻿

2. Identify what is known, what you are inferring, and what is still unknown.

﻿

3. Classify the workflow as Quick Win, Strategic Initiative, Nice-to-Have, or Thankless Task. Explain the classification briefly.

﻿

4. Recommend whether to keep the scope, narrow it, change workflows, or clarify before building.

﻿

5. Recommend the right next artifact: Design Spec, PRD + test cases, Workflow Package, Adoption Evidence Plan, or more narrowing.

﻿

6. Ask up to five clarifying questions only where the answer would materially improve the next artifact.

﻿

7. After the questions are answered, draft the recommended artifact.

﻿

﻿

In the artifact you draft, keep these visible:

﻿

- workflow owner and intended users

﻿

- desired outcome

﻿

- scope and non-scope

﻿

- required inputs and trusted sources

﻿

- AI/person boundary

﻿

- human review and decision authority

﻿

- stop, ask, or escalate conditions

﻿

- smallest useful version

﻿

- representative tests or evidence needed for the next decision

﻿

- open questions and who should validate them

﻿

﻿

Here are my worksheet notes:

﻿

[paste worksheet notes]

﻿
```

﻿

Like

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

## Popular

Resource

[The AI Champion role](/en/public/clubs/champions-ecqup/resources/the-ai-champion-role)

Resource

[Run an AI hackathon](/en/public/clubs/champions-ecqup/resources/hackathon-playbook-2025-09-15)

[13:00](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Video

[Workflow clip: Automate CRM updates with Codex](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Dive in

## Related

Resource

[AI workflow packager](/en/public/clubs/champions-ecqup/resources/ai-workflow-packager-2026-07-07)

Jul 7th, 2026 • Views 4

Resource

[AI workflow design coach](/en/public/clubs/champions-ecqup/resources/ai-use-case-workflow-scoper-2026-05-05)

May 5th, 2026 • Views 325

Resource

[Evaluate AI workflow readiness](/en/public/clubs/champions-ecqup/resources/ai-use-case-discovery-and-prioritizer-2026-05-07)

May 7th, 2026 • Views 405

Resource

[Prioritize AI workflow opportunities](/en/public/clubs/champions-ecqup/resources/workflow-discovery-and-prioritization-matrix-2026-05-05)

May 5th, 2026 • Views 305

Resource

[AI workflow packager](/en/public/clubs/champions-ecqup/resources/ai-workflow-packager-2026-07-07)

Jul 7th, 2026 • Views 4

Resource

[Evaluate AI workflow readiness](/en/public/clubs/champions-ecqup/resources/ai-use-case-discovery-and-prioritizer-2026-05-07)

May 7th, 2026 • Views 405

Resource

[Prioritize AI workflow opportunities](/en/public/clubs/champions-ecqup/resources/workflow-discovery-and-prioritization-matrix-2026-05-05)

May 5th, 2026 • Views 305

Resource

[AI workflow design coach](/en/public/clubs/champions-ecqup/resources/ai-use-case-workflow-scoper-2026-05-05)

May 5th, 2026 • Views 325
