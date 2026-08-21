<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-data-teams-webinar-resource-guide-2026-08-19 -->

[Work Users](/public/clubs/work-users-ynjqu/overview)

[navigation.content](/public/clubs/work-users-ynjqu/content)

Webinar

August 20, 2026

# ChatGPT Work for data teams: Webinar Resource Guide

![ChatGPT Work for data teams: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-39--d0679145-a1c0-47c1-94ea-47c30f75b3ce-1787187472761.jpeg?fit=scale-down&width=1200)

# ChatGPT for Work

# Work

# Workplace & Business

# Use Cases

## Follow along with our webinar ChatGPT Work for data teams

![ChatGPT Work for data teams: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-39--d0679145-a1c0-47c1-94ea-47c30f75b3ce-1787187472761.jpeg?fit=scale-down&width=1200)

# ChatGPT Work for data science and analytics teams: Webinar Resource Guide

## Follow along with our webinar: Get started with ChatGPT Work for Data Science and Analytics

Data teams are often asked to turn information from several systems into answers other people can trust. That means checking whether the data is complete and current, reconciling sources that disagree, and explaining what the evidence does and does not support.

This webinar shows how Chat and Work complement each other. You’ll see Chat answer one focused question quickly. Then you’ll see Work review approved Databricks views, create a weekly data-health workbook, post a digest in Slack, and schedule the workflow to run again. In the second demo, Work investigates a metric contradiction, creates an editable one-page Google Doc, and saves the review method as a reusable skill.

> **Note:** The webinar uses the Data plugin, a custom Databricks plugin, Google Drive, Slack, and fictional Blossom Labs data and templates. Availability depends on your plan and workspace settings. Replace the demo sources with data and templates your organization approves, and review every output before using or sharing it.

## What you’ll need

* Access to **ChatGPT Work** and the **Data** plugin.

* An approved connected data source. The webinar uses a custom plugin called **Blossom Labs Databricks MCP**.

* **Google Drive** for the workbook and diagnostic shown in the demos.

* **Slack** if you want Work to post the weekly digest.

* A one-page metric-diagnostic template if you want the second demo to follow your organization’s structure and visual style.

Workspace administrators control which plugins, connections, and actions are available. If you cannot install or connect something you need, contact your IT or workspace administrator.

## Resources to bookmark

* ﻿ [ChatGPT Help Center](https://help.openai.com/en/collections/3742473-chatgpt): Find product guidance and answers to common questions.

* ﻿ [Agents & Workflows course](https://academy.openai.com/public/courses/agents-and-workflows-bieml): Practice delegating larger jobs and building repeatable workflows.

* ﻿ [Data plugin](https://openai.com/business/plugins/data/): Explore tools for investigating metrics, checking data quality, and creating source-backed reports.

* ﻿ [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex): Learn which product to use for different kinds of work.

* ﻿ [Creating and editing files with ChatGPT Work](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work): Learn how to create editable documents, spreadsheets, and presentations.

* ﻿ [Scheduled tasks in ChatGPT](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt): Learn how to create and manage recurring tasks.

* ﻿ [Download ChatGPT](https://chatgpt.com/download/): Get the desktop or mobile app.

* ﻿ [Upcoming ChatGPT for Work webinars](https://academy.openai.com/en/pages/chatgpt-for-work-webinars-1y07zs): Find more live and on-demand sessions.

## Learn: When to use Chat and when to use Work

### Key ideas

* Use Chat when you need a quick answer, want to talk through an idea, or need help with one focused piece of work.

* Use Work when ChatGPT needs to gather context, handle several steps, and create a finished file for you to review.

* Choose based on the job and the result you need, not simply the type or size of the source file.

* Work can take longer because it is doing more. You can follow along, steer it while it works, or come back when the result is ready.

* You still own the validation and judgment. Check the evidence, calculations, limitations, and recommendations before anyone acts on the result.

## Learn: Find and use the Data plugin

The Data plugin can work with spreadsheets, uploaded files, and connected data sources. Its skills can check data quality, investigate metric exceptions, and organize findings into consistent reports. In this webinar, it helps Work compare launch-readiness data, state what the evidence supports, and create materials for the analytics team to review.

### Follow along

1. Open **Plugins** from the left sidebar.

2. Search for **Data** and open the plugin. Install it if it is available in your workspace.

3. Review its skills, including **Analyze Data Quality**, **Metric Diagnostics**, and **KPI Reporting**.

4. Connect the data source and destination tools your workflow needs. The webinar uses a custom Databricks plugin, Google Drive, and Slack.

5. Return to the conversation, switch to **Work**, type  `@Data` , and select the plugin.

6. Invoke your connected data-source plugin when the task needs it. The demo uses a custom data environment for demo purposes.

## Demo 1: Get a quick launch-readiness answer in Chat

Chat is useful when you need one focused answer from a connected source. That answer can point you in the right direction, but it is different from a full review that checks several sources and creates materials for the team.

### Follow along

Start a new Chat with your approved data connection available, then use this prompt:

In the latest available launch-readiness data, what is recorded as the main constraint on build capacity, and which source supports that answer?

In the webinar data, Chat identifies retail packaging as the recorded constraint. That is useful, but it only reports what one source says. It does not establish whether the supporting data is complete, whether another source disagrees, or whether the finding is ready to share.

## Demo 1: Create and schedule a weekly data-health review in Work

Work can review the approved views together, flag issues that need attention, create a consistent Google Sheet, and post a digest for the analytics team. The prompt also sets clear boundaries. Work may inspect and summarize the data, but it may not change the sources, invent thresholds, or make claims the available evidence cannot support.

### Follow along

Start a new Work task, invoke  `@Data`  and your connected data-source plugin, then use this prompt. If you are working outside the webinar environment, replace the three demo view names and destination channel with approved sources and tools from your workspace.

@Data Use only these approved views in the connected Databricks workspace:

- launch_build_gap

- component_readiness

- supplier_scorecard

Review the latest available data and create a new Google Sheet called “Weekly Data Health Review - [run date].”

Create these tabs, in this order:

1. Review summary

Give the overall review status, the highest-priority issues, and what an analyst needs to verify before the findings are shared.

2. Metric exceptions

Include explicit source flags and material inconsistencies across the views. For each item, show the supporting evidence, explain why it was flagged, and state what should be checked next. Do not invent alert thresholds.

3. Data-quality checks

Flag visible missing values, conflicting statuses, and anything whose freshness or coverage cannot be verified. Explain which source is affected and how the issue limits the analysis.

4. Sources and limitations

Identify the views, fields, and records used. Record when the review was run. State clearly what the available data cannot support.

Separate source facts from interpretations and recommendations. Do not imply a trend or a cause unless the data supports it. Do not modify any source data. Do not claim the data is current or complete when that cannot be verified.

When the workbook is ready, post a weekly data-health digest to the analytics team’s Slack channel. Include the overall status, the number of metric exceptions and data-quality issues, the highest-priority analyst check, anything that is not ready to share, and a link to the workbook.

The prompt limits Work to approved sources, defines a repeatable workbook structure, and states what Work must not infer or change.

In the webinar data, Work returns a **Blocked** review status, one critical exception, and six data-quality checks. The main exception is a contradiction: one view identifies retail packaging as the constraint on both products, while another marks the same component green with zero risk and blank inventory fields.

### Verify the material finding

Ask Work to show how it reached the most important finding:

Show your work for the packaging contradiction. Cite the Databricks views and records, and separate confirmed facts from what still needs verification.

The response should trace the contradiction to the supporting records without claiming to know why the sources disagree.

### Schedule the workflow

After you approve the instructions, workbook structure, and Slack digest, use this prompt:

Schedule this workflow to run every Monday at 7:30 a.m.

Each week, use only the three approved Databricks views. Create a new dated Google Sheet with the same four tabs, preserve all earlier weekly workbooks, and post the same data-health digest to the analytics team’s Slack channel.

When a previous weekly workbook is available, compare the saved reviews and label each flagged item as new, ongoing, or no longer present. Base that comparison only on the saved weekly reviews. Do not modify the source data.

Each run should create a new workbook. Comparisons across weeks should use the saved review workbooks, not unsupported history inferred from point-in-time source data.

Open **Scheduled** from the sidebar and select the weekly data-health task. Confirm when it will run next. From there, you can change the instructions or timing, or delete the task when you no longer need it.

### What to review

* Does the workbook contain the four requested tabs in the right order?

* Does the review summary state the overall status, priority issues, and required analyst checks?

* Are source facts separated from interpretations and recommendations?

* Does every material exception show its supporting evidence and next check?

* Are missing values, conflicting statuses, and unverifiable freshness or coverage clearly flagged?

* Does the workbook avoid unsupported thresholds, trends, and causal claims?

* Can an analyst trace the packaging contradiction to the named views and records?

* Does the Slack digest include the status, issue counts, highest-priority check, anything not ready to share, and a working workbook link?

* Did Work leave the source data unchanged?

* Does each scheduled run create a new dated workbook and preserve earlier reviews?

* Are week-over-week labels based only on saved weekly reviews?

* Did the first scheduled runs complete as expected, with the required connections still available?

## Demo 2: Build an editable metric diagnostic in Work

The weekly review tells the team where to look. The second workflow gives analysts a consistent way to investigate what they find.

In the webinar, the assignment is to examine the packaging contradiction and create a formal one-page diagnostic for the analyst and source owner. The template controls the document’s structure and style. The approved Databricks views control what the document may say.

### Follow along

Start a new Work task, invoke the Data and Databricks plugins, and make the **Blossom Labs Metric Diagnostic One-Pager Template** available. If you are adapting the workflow, use an approved template from your organization.

@Data @Blossom Labs Databricks MCP

Using only launch_build_gap, component_readiness, and supplier_scorecard, investigate the packaging contradiction: it is recorded as the build constraint for both products, but its readiness is green with zero risk and missing inventory values.

Create a new one-page Google Doc from the Blossom Labs Metric Diagnostic One-Pager Template for analytics review. Cite supporting records, separate confirmed evidence from open questions, and do not infer trends or causes from these point-in-time views.

This prompt defines the question, approved sources, requested document, audience, and limits of the evidence. Work decides how to perform the comparison and place the findings within the supplied template.

### Optional practice: Verify the material finding

The presenter skips a second live spot-check in this demo. To practice the same review method yourself, choose one material claim and trace it back to the supporting records. For the webinar data, use:

Verify that packaging is recorded as the constraint for both products. Show the supporting Databricks views and records, and separate confirmed facts from what still needs verification.

### What to review

* Is the result a new, editable Google Doc rather than an overwritten template?

* Does it follow the supplied template and stay within one page?

* Does the bottom line state the contradiction without deciding which source is correct?

* Are confirmed facts separated from open questions?

* Does each material claim cite the supporting view and records?

* Does the source trail let an analyst inspect the evidence directly?

* Does the document state that freshness, trends, and causes cannot be confirmed from the available point-in-time views?

* Are missing inventory values left unresolved rather than filled with guesses?

* Does the document give the analyst and source owner specific validation steps?

* Has a person traced at least one material claim back to the source records?

* Is the document framed as an internal analytics review rather than an executive recommendation?

## Demo 2: Turn the metric-diagnostic workflow into a reusable skill

The specific exception will change, but the review standard can stay the same. Test and approve the workflow first. Then save the template, evidence checks, and citation rules without carrying forward the current dataset or conclusion.

Use this prompt:

Create a skill called metric-diagnostic-review from this workflow. Keep the template, evidence checks, and citation rules, but not this dataset or its findings. Ask for the metric, approved sources, and audience each time.

### Find and share the skill

1. Review the proposed skill and install it.

2. Open **Plugins**, select **Skills**, and open  `metric-diagnostic-review` .

3. Confirm that it retains the template, evidence checks, and citation rules.

4. Confirm that it does not retain the packaging dataset or its findings.

5. Confirm that it asks for the metric, approved sources, and audience each time.

6. Edit the skill if your template or review standard changes.

7. Share it with your workspace when it is ready for other analysts to use.

A reusable skill should preserve the review standard, not a previous conclusion. The analytics team still decides whether each new conclusion is sound.

## Learn: Chat or Work?

* **I need to identify the recorded constraint in one source and cite it → Chat.** One focused question and one quick answer.

* **I need to compare approved views, flag exceptions, create a review workbook, and post a digest → Work.** Several sources, multiple steps, and a finished file.

* **I need a one-page diagnostic that follows a template and documents evidence and limitations → Work.** The assignment combines analysis, source tracing, and document creation.

* **I need help explaining one finding more clearly → Chat.** A focused explanation with room for quick back-and-forth.

## Learn: Where Codex fits

Codex is useful when the work itself is technical, such as debugging a data pipeline, refactoring SQL or Python, working in a repository, or building and testing an internal data tool.

Work is a better fit when the assignment spans connected systems and needs to end in a finished business file, such as the weekly review workbook or metric diagnostic shown here.

The simplest way to choose is to look at what you need back. If you need working code or a change to a technical project, start in Codex. If you need ChatGPT to gather context, manage a larger assignment, and create a workbook or document, start in Work.

## Try it: Find your first Work task

You do not need to design the perfect workflow before you begin. Ask Work to suggest a few tasks based on your recent activity, then wait for your choice:

Based on my recent work, suggest three data science or analytics tasks I could hand off to ChatGPT Work. For each one, tell me what you would create and where I should start. Don’t begin until I choose.

## Learn: Use Work across surfaces

The webinar uses  [chatgpt.com](https://chatgpt.com/). You can also use ChatGPT on the desktop app for Mac or Windows and on the mobile app for iOS or Android. Your work stays in sync, so you can start a task in the browser and check it later from another device.

## Before you use the output

* Use only approved data, views, templates, and connected systems.

* Confirm metric definitions, units, reporting scope, dates, freshness, and coverage.

* Trace material claims and calculations back to the supporting records.

* Keep source facts, interpretations, recommendations, and open questions separate.

* Do not infer a trend or cause from point-in-time data.

* Leave missing values and conflicting signals unresolved until a person verifies them.

* Review anything marked ready to share before sending it to a broader audience.

* Keep source data and systems of record unchanged unless a person explicitly approves an update.

* Check that scheduled tasks still have access to the required connections, and review the first few runs.

* Follow your organization’s AI, privacy, security, and records-management policies.

## What to try next

Choose one data science or analytics task already on your plate. Give Work the approved sources, the result you need, and the boundaries it should respect. Review the file it creates and refine the instructions. If the job repeats, schedule it. If the review method should stay consistent across the team, save and share it as a skill.

Thanks for joining!

[ChatGPT 101 Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

[ChatGPT 102 Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide)

[ChatGPT 101: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide-interactive)

[ChatGPT Work for finance teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-finance-teams-webinar-resource-guide-2026-08-13)

Aug 13th, 2026 • Views 215

[How data science teams use Codex: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/how-data-science-teams-use-codex-webinar-resource-guide-2026-05-28)

May 28th, 2026 • Views 1.5K

[ChatGPT Work for sales teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-sales-teams-webinar-resource-guide-2026-08-05)

Aug 6th, 2026 • Views 323

[Get started with ChatGPT Work: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/get-started-with-chatgpt-work-webinar-resource-guide-2026-08-03)

By Diana Stegall • Aug 4th, 2026 • Views 1.2K

[ChatGPT Work for finance teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-finance-teams-webinar-resource-guide-2026-08-13)

Aug 13th, 2026 • Views 215

[ChatGPT Work for sales teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-sales-teams-webinar-resource-guide-2026-08-05)

Aug 6th, 2026 • Views 323

[Get started with ChatGPT Work: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/get-started-with-chatgpt-work-webinar-resource-guide-2026-08-03)

By Diana Stegall • Aug 4th, 2026 • Views 1.2K

[How data science teams use Codex: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/how-data-science-teams-use-codex-webinar-resource-guide-2026-05-28)

May 28th, 2026 • Views 1.5K
