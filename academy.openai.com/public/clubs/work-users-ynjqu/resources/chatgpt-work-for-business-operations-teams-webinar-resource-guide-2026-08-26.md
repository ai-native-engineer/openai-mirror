<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-business-operations-teams-webinar-resource-guide-2026-08-26 -->

[Communities](/home/clubs)

/

[Work Users](/public/clubs/work-users-ynjqu/overview)

/

[navigation.content](/public/clubs/work-users-ynjqu/content)

Webinar

August 26, 2026 · Last updated on August 27, 2026

# ChatGPT Work for business operations teams: Webinar Resource Guide

![ChatGPT Work for business operations teams: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-42--7ae1e2d3-d4ce-436a-a63c-68ffef457b0a-1787768339053.jpeg?fit=scale-down&width=1200)

# Work

# Workplace & Business

# ChatGPT for Work

# Use Cases

## Follow along with our webinar ChatGPT Work for business operations teams

![Diana Stegall](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/venice-663e9db7-692a-4851-b2c4-19f0d6c9b62c-1776829671335.jpeg?fit=scale-down&width=60)

Diana Stegall

![ChatGPT Work for business operations teams: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-42--7ae1e2d3-d4ce-436a-a63c-68ffef457b0a-1787768339053.jpeg?fit=scale-down&width=1200)

# ChatGPT Work for Business Operations teams: Webinar Resource Guide

## Follow along with our webinar: Get started with ChatGPT Work for Business Operations Teams

Business Operations work rarely starts in one place. Project updates may live in one system, operational data in another, and leadership questions in email, chat, or meeting notes. The job is to bring those inputs together, identify what needs attention, and make the next decision and owner clear.

This webinar shows how Chat and Work complement each other across that work. You’ll see Chat answer one focused question quickly. Then you’ll see Work review approved launch-readiness data, create a weekly operating-review workbook, prepare an update for Slack, and schedule the same workflow for the next cycle. In the second demo, Work turns one blocker into an editable leadership decision brief and saves the successful process as a reusable skill.

> **Note:** The webinar uses the Data plugin, a custom Databricks plugin, Google Drive, Slack, and fictional Blossom Labs data and templates. Availability depends on your plan and workspace settings. Replace the demo sources with data, templates, and connected tools your organization approves. Review every output before assigning work, sharing an update, approving a recommendation, or changing a system of record.

## What you’ll need

﻿ [Download the Business Operations demo files](https://docsend.com/view/s/79ig3mmbaie7pktz)﻿

* Access to **ChatGPT Work** and the **Data** plugin.

* An approved connected data source. The webinar uses a custom demo plugin called **Blossom Labs Databricks MCP**.

* **Google Drive** for the operating-review workbook and leadership decision brief.

* **Slack** if you want Work to prepare and post the stakeholder update.

* A one-page decision-brief template if you want the second demo to follow your organization’s structure and visual style.

Workspace administrators control which plugins, connections, and actions are available. If you cannot install or connect something you need, contact your IT or workspace administrator.

## Resources to bookmark

* ﻿ [Learn ChatGPT](https://learn.chatgpt.com/chatgpt): Find product guidance, practical examples, and prompts for Chat and Work.

* ﻿ [Agents & Workflows course](https://academy.openai.com/public/courses/agents-and-workflows-bieml): Practice delegating larger jobs and building repeatable workflows.

* ﻿ [Data plugin](https://openai.com/business/plugins/data/): Explore tools for investigating metrics, checking data quality, and creating source-backed reports.

* ﻿ [ChatGPT Work for Business Operations](https://openai.com/business/solutions/operations/): See more ways operations teams can use Work for reviews, planning, decisions, and follow-through.

* ﻿ [Creating and editing files with ChatGPT Work](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work): Learn how to create editable documents, spreadsheets, and presentations.

* ﻿ [Scheduled tasks in ChatGPT](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt): Learn how to create and manage recurring tasks.

* ﻿ [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/): Learn how to create, install, edit, and share reusable skills.

* ﻿ [Download ChatGPT](https://chatgpt.com/download/): Get the desktop or mobile app.

* ﻿ [Upcoming ChatGPT for Work webinars](https://academy.openai.com/home/events?tag=ChatGPT%2520for%2520Work-6a39cfbcd72d84004e0cae37): Find more live and on-demand sessions.

## Learn: When to use Chat and when to use Work

### Key ideas

* Use Chat when you need a fast answer, want to talk through an idea, or need help with one focused piece of work.

* Use Work when ChatGPT needs to gather context, handle several steps, and create a finished file for you to review.

* Choose based on the job and the result you need, not simply the type or size of the source material.

* Work can take longer because it is doing more. You can follow along, steer it while it works, or come back when the result is ready.

* Your team still owns the recommendation, assignments, and approvals. Check the sources, assumptions, calculations, and proposed actions before anyone acts on the result.

## Learn: Find and use the Data plugin

The Data plugin can work with spreadsheets, uploaded files, and connected data sources. In this webinar, it helps Work inspect structured launch-readiness inputs and pull out the few signals that affect the operating review. Work then organizes the decisions, owners, and follow-up across the other connected tools.

### Follow along

1. Open **Plugins** from the left sidebar.

2. Search for **Data** and open the plugin. Install it if it is available in your workspace.

3. Review its skills, including **Analyze Data Quality**, **Metric Diagnostics**, and **KPI Reporting**.

4. Connect the source and destination tools your workflow needs. The webinar uses a custom Databricks plugin, Google Drive, and Slack.

5. Return to the conversation, switch to **Work**, type  `@Data` , and select the plugin.

6. Invoke your connected data-source plugin when the task needs it. The demo uses  `@Blossom Labs Databricks MCP` .

The Blossom Labs plugin and data are built for the demo. When you adapt the workflow, use only approved sources and replace the demo view names, template, and Slack channel with your own.

## Demo 1: Get a quick launch-readiness answer in Chat

Chat is useful when you need one focused answer from a connected source. That answer can point you in the right direction, but it is different from a complete operating review that compares sources, frames decisions, creates a workbook, and prepares the follow-up.

### Follow along

Start a new Chat with your approved data connection available, then use this prompt:

```
In the latest available launch-readiness data, what is recorded as the main constraint on build capacity, and which source supports that answer?
```

In the webinar data, Chat identifies retail packaging as the recorded constraint. That is useful, but it only reports what one source says. It does not show whether another source disagrees, what decision is waiting, who owns the next step, or what the team should review together.

## Demo 1: Create and schedule a weekly operating review in Work

Work can review the approved views together, turn them into a consistent operating review, create a new Google Sheet, and draft a stakeholder update. The prompt also sets clear boundaries. Work may organize the evidence and recommend a next step, but it may not modify source data, invent an owner or deadline, or post the update before a person approves it.

### Follow along

Start a new Work task, invoke  `@Data`  and your connected data-source plugin, then use this prompt. Outside the webinar environment, replace the three demo view names and destination channel with approved sources and tools from your workspace.

```
@Data Use only these approved views in the connected Databricks workspace:

- launch_build_gap

- component_readiness

- supplier_scorecard

Prepare the weekly operating review and create a new Google Sheet called “Weekly Launch Readiness Review - [run date].”

Create these tabs, in this order:

1. Operating summary

Summarize the overall status, meaningful progress, top blockers, and decisions needed.

2. Blockers and dependencies

For each item, show the operational impact, supporting source, and next step.

3. Decisions and owners

List each decision or follow-up, its owner, and its due date. Use “Owner needed” or “Date needed” when the sources do not support one.

4. Sources and open questions

List the sources used, assumptions, unresolved questions, and anything that needs confirmation before leadership sees the update.

Separate confirmed facts from assumptions. Do not modify the source data or invent owners, dates, commitments, or approvals.

Draft a concise update for #launch-readiness with the status, top blocker, decision needed, owner follow-ups, and a link to the workbook. Do not post it until I approve.
```

In the webinar, Work creates the four requested tabs and classifies the issue as a critical launch blocker. It reports 87,800 forecast units, zero constrained build, and two models at zero build. It also states that no prior-period data is available, so it does not claim week-over-week progress.

Most importantly, Work keeps a source conflict visible. One view records retail packaging as the constraint on both products. Another marks the same component green while its inventory fields are blank. Work separates the confirmed zero-build result from the cause that still needs validation.

### Verify the material escalation

Before assigning work or sharing the update, ask Work to show the evidence behind the most consequential escalation:

```
Show the evidence behind the packaging escalation, including the source status, operational impact, and proposed next step. Separate confirmed facts from what still needs review.
```

The response should trace the escalation to the build-gap and component-readiness records, explain why the disagreement affects the launch plan, and leave the cause and owner open for review.

### Approve the stakeholder update

Review the drafted  `#launch-readiness`  update before it is posted. Confirm that it includes the status, top blocker, decision needed, owner follow-ups, and a working link to the workbook. Edit the draft if needed, then approve the post.

### Schedule the workflow

Once you approve the instructions, workbook layout, and approval flow, use this prompt:

```
Schedule this workflow to run every Monday at 7:30 a.m.

Each week, use the same approved sources. Create a new dated Google Sheet with the same four tabs, preserve all earlier reviews, and prepare the #launch-readiness update for my approval.

When a previous review is available, compare them and label blockers and actions as new, ongoing, or resolved. Do not modify the sources, invent owners or dates, or post the final update without approval.
```

Each run should create a new workbook and preserve the earlier reviews. Later runs may label blockers and actions as new, ongoing, or resolved by comparing the saved weekly reviews. The final stakeholder update should still wait for approval.

Open **Scheduled** from the sidebar and select the weekly launch-readiness task. Confirm when it will run next. From there, you can change the instructions or timing, or delete the task when you no longer need it.

### What to review

* Does the workbook contain the four requested tabs in the right order?

* Does the operating summary state the overall status, meaningful progress, top blockers, and decisions needed?

* Are confirmed facts separated from assumptions and open questions?

* Does the workbook keep the packaging source conflict visible instead of treating it as resolved?

* Does each blocker show its operational impact, supporting source, and next step?

* Are missing owners and dates labeled  `Owner needed`  and  `Date needed`  rather than filled with guesses?

* Does the evidence check trace the escalation to the correct records and separate facts from the proposed follow-up?

* Did Work leave the approved source data unchanged?

* Did a person review and approve the Slack update before it was posted?

* Does each scheduled run create a new dated workbook without overwriting earlier reviews?

* Are new, ongoing, and resolved labels based on saved prior reviews rather than invented history?

* Does the scheduled stakeholder update still wait for human approval?

* Did the first few scheduled runs complete as expected, with the required connections still available?

## Demo 2: Build an editable leadership decision brief in Work

The weekly operating review tells the team what needs attention. The second workflow turns one unresolved blocker into a formal one-page brief for the decision owner and cross-functional leads.

The template controls the document’s structure and visual style. The approved sources control the facts. Work should make the decision, recommendation, blockers, open questions, owners, and approval explicit without pretending the source conflict is resolved.

### Follow along

Start a new Work task, invoke the Data and Databricks plugins, and make the **Blossom Labs Launch Decision Brief Template** available. If you are adapting the workflow, use an approved template from your organization.

```
@Data @Blossom Labs Databricks MCP

Using only launch_build_gap, component_readiness, and supplier_scorecard, prepare a one-page leadership decision brief about the unresolved packaging blocker.

Use the Blossom Labs Launch Decision Brief Template. Make the decision, recommendation, blockers, open questions, owners, and approval explicit. Separate facts from assumptions, and do not invent commitments, owners, or dates.
```

Work should create a new Google Doc without overwriting the template. The finished brief should lead with the decision and recommendation, cite the supporting records, separate confirmed inputs from assumptions, show the blockers and dependencies, turn unresolved items into actions, and make ownership gaps and the approval gate visible.

The result remains a native, editable Google Doc. Your team can revise the recommendation, add comments, and assign follow-ups after reviewing the draft.

Before sharing the brief, repeat the evidence-check method from Demo 1. Choose one material claim and trace it back to the supporting Databricks records.

### What to review

* Is the result a new, editable Google Doc rather than an overwritten template?

* Does it follow the supplied template and stay within one page?

* Does it lead with the decision and recommendation rather than the raw data?

* Are confirmed inputs separated from assumptions and open questions?

* Does each material claim cite the supporting records?

* Does the source conflict appear as a blocker with a dependent next step?

* Are missing owners and dates left visible rather than filled with guesses?

* Are the actions, owners, conditions, and approval requirement explicit?

* Can a reviewer challenge or revise the recommendation without losing the source trail?

* Has a person traced at least one material claim back to the source records?

* Has the Business Operations team reviewed the recommendation, assignments, and approval before anyone acts?

## Demo 2: Turn the decision-brief workflow into a reusable skill

The blocker, launch, and recommendation will change, but the decision process can stay consistent. Test and approve the workflow first. Then save the template, source checks, decision structure, owner fields, and approval rules without carrying forward the current dataset or recommendation.

Use this prompt:

```
Create a skill called operating-decision-brief from this workflow. Keep the template, source checks, decision structure, owner fields, and approval rules, but not this dataset or recommendation. Ask for the decision, approved sources, audience, and approver each time.
```

### Find and share the skill

1. Review the proposed skill and install it.

2. Open **Plugins**, select **Skills**, and open  `operating-decision-brief` .

3. Confirm that it preserves the template, source checks, decision structure, owner fields, and approval rules.

4. Confirm that it does not retain the packaging dataset or its recommendation.

5. Confirm that it asks for the decision, approved sources, audience, and approver each time.

6. Edit the skill if your template or operating process changes.

7. Share it with your workspace when it is ready for other operators to use.

A reusable skill should preserve the decision process, not a previous answer. Your team still owns the recommendation, assignments, and approval for each new decision.

## Learn: Chat or Work?

* **I need to identify the recorded constraint in one source and cite it → Chat.** One focused question and one quick answer.

* **I need to compare approved sources, surface blockers, frame decisions, create a weekly review, and draft the stakeholder update → Work.** Several inputs, multiple steps, and a finished operating-review workbook.

* **I need a one-page leadership brief that follows a template and makes the recommendation, owners, and approval clear → Work.** The assignment combines source review, decision framing, and document creation.

* **I need help explaining one update more clearly to a stakeholder → Chat.** A focused rewrite with room for quick back-and-forth.

## Learn: Where Codex fits

Codex is useful when the work itself is technical, such as building an internal workflow tool, updating a code-backed dashboard, changing an integration, or working in a repository that supports an operating process.

Work is a better fit when the assignment spans connected systems and needs to end in a finished business file, such as the weekly operating review or leadership decision brief shown here.

The simplest way to choose is to look at what you need back. If you need working code or a change to a technical project, start in Codex. If you need ChatGPT to gather context, manage a larger assignment, and create a workbook or document, start in Work.

## Try it: Find your first Work task

You do not need to design the perfect workflow before you begin. Ask Work to suggest a few Business Operations tasks based on your recent activity, then wait for your choice:

```
Based on my recent work, suggest three Business Operations tasks I could hand off to ChatGPT Work. For each one, tell me what you would create and where I should start. Don’t begin until I choose.
```

## Learn: Use Work across surfaces

The webinar uses  [chatgpt.com](https://chatgpt.com/). You can also use ChatGPT on the desktop app for Mac or Windows and on the mobile app for iOS or Android. Your work stays in sync, so you can start a task in the browser and check it later from another device.

## Before you use the output

* Use only approved data, views, templates, channels, and connected systems.

* Confirm the reporting date, units, definitions, source freshness, and scope.

* Trace material claims, calculations, and recommendations back to their supporting records.

* Keep confirmed facts, assumptions, open questions, and recommendations separate.

* Keep source conflicts visible until a person resolves them.

* Do not claim progress, history, or a trend when the available sources do not support it.

* Leave missing owners, dates, commitments, and approvals unresolved rather than filling them with guesses.

* Review stakeholder messages before posting them and decision briefs before anyone acts on them.

* Keep source data and systems of record unchanged unless a person explicitly approves an update.

* Check that scheduled tasks still have access to the required connections, and review the first few runs.

* Follow your organization’s AI, privacy, security, and records-management policies.

## What to try next

Choose one Business Operations task already on your plate. Give Work the approved sources, the result you need, and the boundaries it should respect. Review the file it creates and refine the instructions. If the job repeats, schedule it. If the decision process should stay consistent across the team, save and share it as a skill.

Thanks for joining!

Resource

[ChatGPT 101 Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

Resource

[ChatGPT 102 Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide)

Resource

[ChatGPT 101: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide-interactive)

By Juliann Igo

Resource

[ChatGPT Work for marketing teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-marketing-teams-webinar-resource-guide-2026-08-26)

By Diana Stegall • Aug 27th, 2026 • Views 149

Resource

[ChatGPT Work for sales teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-sales-teams-webinar-resource-guide-2026-08-05)

Aug 6th, 2026 • Views 416

Resource

[ChatGPT Work for data teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-data-teams-webinar-resource-guide-2026-08-19)

Aug 20th, 2026 • Views 465

Resource

[ChatGPT Work for finance teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-finance-teams-webinar-resource-guide-2026-08-13)

Aug 13th, 2026 • Views 391

Resource

[ChatGPT Work for marketing teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-marketing-teams-webinar-resource-guide-2026-08-26)

By Diana Stegall • Aug 27th, 2026 • Views 149

Resource

[ChatGPT Work for data teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-data-teams-webinar-resource-guide-2026-08-19)

Aug 20th, 2026 • Views 465

Resource

[ChatGPT Work for finance teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-finance-teams-webinar-resource-guide-2026-08-13)

Aug 13th, 2026 • Views 391

Resource

[ChatGPT Work for sales teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-sales-teams-webinar-resource-guide-2026-08-05)

Aug 6th, 2026 • Views 416
