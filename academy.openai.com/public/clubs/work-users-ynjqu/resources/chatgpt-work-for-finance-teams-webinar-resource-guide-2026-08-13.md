<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-finance-teams-webinar-resource-guide-2026-08-13 -->

[Work Users](/public/clubs/work-users-ynjqu/overview)

[navigation.content](/public/clubs/work-users-ynjqu/content)

Webinar

August 13, 2026 · Last updated on August 14, 2026

# ChatGPT Work for finance teams: Webinar Resource Guide

![ChatGPT Work for finance teams: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-37--4f02a4be-49f9-4483-8925-612cc4366ce9-1786660485558.jpeg?fit=scale-down&width=1200)

# ChatGPT for Work

# Workplace & Business

# Use Cases

## Follow along with our webinar ChatGPT Work for finance teams

![ChatGPT Work for finance teams: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-37--4f02a4be-49f9-4483-8925-612cc4366ce9-1786660485558.jpeg?fit=scale-down&width=1200)

# ChatGPT Work for finance teams: Webinar Resource Guide

## Follow along with our webinar: ChatGPT Work for finance teams

Finance work rarely starts in one place. Actuals and forecasts may sit in a workbook, timing and risk context in business notes, and leadership questions somewhere else. This webinar shows how Chat and Work complement each other across that work.

You’ll see Chat answer focused questions quickly. Then you’ll see Work compare several sources, create a forecast review workbook, send an update in Slack, and schedule the same review for the next cycle. In the second demo, Work turns a scenario model and supporting notes into an editable presentation for the board and saves the successful presentation method as a reusable skill.

> **Note:** Some exercises require sample files and access to ChatGPT Work, Plugins, Google Workspace, and Slack. Availability depends on your plan and workspace settings. Use only data your organization allows, and review every output before acting on it, sharing it, changing a forecast, or updating a system of record.

## Download the sample files

﻿ [Download the Finance demo files](https://docsend.com/view/s/em8pzfkevbfhbgft)﻿

The download includes the source files for both Finance demos and the presentation template used in Demo 2.

## Resources to bookmark

* ﻿ [Learn ChatGPT](https://learn.chatgpt.com/chatgpt): Product guidance and practical examples for Chat and Work.

* ﻿ [Agents & Workflows course](https://academy.openai.com/public/courses/agents-and-workflows-bieml): Practice delegating larger jobs and building repeatable workflows.

* ﻿ [Data plugin](https://openai.com/business/plugins/data-analytics/): Explore tools for investigating metrics, checking data quality, and creating source-backed reports.

* ﻿ [ChatGPT Work for finance teams](https://openai.com/business/solutions/finance/): See more ways Finance teams can use Work for reporting, forecasting, analysis, and planning.

* ﻿ [Creating and editing files with ChatGPT Work](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work): Learn how to create editable documents, spreadsheets, and presentations.

* ﻿ [Download ChatGPT](https://chatgpt.com/download/): Get the desktop or mobile app.

* ﻿ [Upcoming ChatGPT for Work webinars](https://academy.openai.com/home/events?tag=ChatGPT%2520for%2520Work-6a39cfbcd72d84004e0cae37): Find more live and on-demand sessions.

## Learn: When to use Chat and when to use Work

### Key ideas

* Use Chat when you need a fast answer, want to talk through an idea, or need help with one focused piece of work.

* Use Work when ChatGPT needs to gather context, handle several steps, and create a polished file for you to review.

* Choose based on the job, not the size or type of the file.

* Work can take longer because it is doing more. You can follow along, steer it while it works, or come back when the result is ready.

* You are still responsible for reviewing the numbers, assumptions, recommendations, and any action that affects a forecast or system of record.

## Learn: Find and use the Data plugin

The Data plugin can investigate metrics, check data quality, diagnose changes, and create source-backed reports. In this webinar, it helps Work compare forecast inputs, separate supported findings from unresolved questions, and organize the results for Finance to review.

### Follow along

1. Open **Plugins** from the left sidebar.

2. Search for **Data** and open the plugin. If it is available in your workspace, install it as directed.

3. Review its skills, including **Analyze Data Quality**, **Metric Diagnostics**, and **KPI Reporting**.

4. Install or connect **Google Drive** and **Slack** for the workflow shown in the webinar. If your organization uses SharePoint and Microsoft Teams, use the plugins your workspace supports instead.

5. Return to the conversation, switch to Work, type  `@Data` , and select the plugin.

Workspace administrators control which plugins are available. If you cannot install one you need, contact your IT or workspace administrator.

## Demo 1: Get a quick forecast answer in Chat

Chat is useful when you need one focused answer from a workbook and want it quickly. That answer can help you find where to look, but it is different from a complete forecast review that compares several sources and creates a finished workbook.

### Follow along

From the sample download, use:

* `Q2_Sales_Forecast_Tracking.xlsx`

Start a new Chat, attach the workbook, and use this prompt:

```
Looking at this workbook, which proposed forecast change has the largest downside, and what evidence does the workbook give for it?
```

The workbook points to a potential $5.8 million EMEA downside and two delayed opportunities. That is useful evidence, but it is not enough by itself to change the forecast. Finance still needs the regional context and confirmed timing.

## Demo 1: Create and schedule a forecast review in Work

Work can compare the forecast workbook with the regional notes and review questions, create a new Google Sheet, and send a Slack update with a link. The prompt sets clear boundaries: Work may review the files and draft follow-ups, but it may not modify the source files, change the forecast, or send the owner questions.

### Follow along

From the sample download, add these three files to a connected **Forecast Review** folder:

* `Q2_Sales_Forecast_Tracking.xlsx`

* `Regional_Sales_Notes.docx`

* `Forecast_Review_Questions.txt`

Start a new Work task, invoke  `@Data` , and use this prompt:

```
@Data Use only the latest approved files in the connected Forecast Review folder: the forecast workbook, regional notes, and forecast review questions.

﻿

Review the forecast submissions and create a new Google Sheet called “Q2 Forecast Review - Week 5.”

﻿

Create these tabs, in this order:

﻿

1. Forecast position

Show actual revenue, cumulative forecast, and variance through week five.

﻿

2. Supported findings

Include only findings supported by the available files. Cite the source for each material claim.

﻿

3. Unresolved items

Identify missing inputs, conflicting assumptions, and proposed forecast changes the available evidence does not support. State what is missing and what cannot yet be concluded.

﻿

4. Draft owner follow-ups

Draft the question Finance needs each owner to answer. Do not send these messages.

﻿

5. Sources

Link each material figure and finding to its source.

﻿

Separate actuals, forecasts, assumptions, and recommendations. Do not change the forecast or modify the source files.

﻿

When the workbook is ready, send me a short Slack message with the current cumulative variance, the most important unresolved item, and a link to the new workbook.
```

When the workbook is ready, verify one calculated figure:

```
Show your work for the $1.9 million cumulative variance through week five. Link to the source files and identify the exact worksheet cells used in the calculation.
```

After you review the result, schedule the same workflow:

```
Schedule this workflow to run every Monday at 7:30 a.m. Create a new Google Sheet each time with the same tabs, and send me the Slack update.
```

### What to review

* Does the forecast position reconcile to the source workbook?

* Are supported findings separated from issues that still need evidence?

* Can you trace material figures and findings to the correct files and cells?

* Are missing inputs left unresolved instead of filled with guesses?

* Did Work leave the source files and forecast unchanged?

* Does the Slack message include the current variance, the most important unresolved item, and a working link to the new workbook?

* Does each scheduled run create a new workbook without overwriting earlier reviews?

* Is the connected Forecast Review folder still accessible, and did the first few scheduled runs complete as expected?

## Demo 2: Create a Project for a forecast update for the board

A Project gives Chat and Work the same set of Finance materials. You can ask a quick question or hand off the full presentation without uploading the sources again.

### Follow along

From the sample download, use:

* `scenario_model_inputs.xlsx`

* `planning_assumptions_notes.docx`

* `operating_context_summary.pdf`

* `leadership_questions.txt`

* `Cavenridge Corporate Presentation System`

1. Create a Project called **FY26 Forecast Update for the Board**.

2. Add the four Finance source files and the presentation template.

3. Start a new Chat inside the Project and use this prompt:

```
Based on the approved files, what would have to change for Finance to move away from the base case, and which decisions are still open?
```

Chat gives you a quick answer. Work will use the same source material to create the full presentation.

## Demo 2: Build an editable forecast presentation in Work

The audience matters. A presentation for the board should lead with management’s recommendation, the tradeoffs, and the decisions. A presentation for the CFO might include more detail on assumptions, sensitivities, and model checks. Work can use the same Finance files while changing the level of detail and vocabulary for the people who need to use the presentation.

### Follow along

Start a new Work task inside the Project, type  `@Data` , select the plugin, and use this prompt:

```
Create a Google Slides presentation for a forecast review with our board. Use the presentation template and approved source files in this Project.

﻿

Build six slides: a cover; executive outlook; scenario tradeoffs; key drivers and modeled sensitivities; management recommendation and investment gate; and questions for the discussion with our board.

﻿

Lead with management’s current recommendation. Keep scenarios separate from decisions. Source every material number and claim, flag missing evidence, and label the presentation as a draft for Finance review.
```

When the presentation is ready, verify a material calculation:

```
Show your work for the claim that downside ending cash is $33 million above base. Link to the source and identify the exact worksheet cells.
```

For a small change, edit the native Google Slides presentation directly. For a larger change, return to Work and describe what you want revised.

You can use the same workflow with PowerPoint. Supply a PowerPoint template, ask for a PowerPoint presentation, and use the Presentations plugin just as you would for Google Slides. The presentation remains editable, and the same review rules still apply.

### What to review

* Does the presentation follow the supplied template and remain editable?

* Does the executive outlook lead with management’s current recommendation?

* Are the base, upside, and downside cases presented as scenarios rather than commitments?

* Does the presentation explain the growth, cash, and capacity tradeoffs without burying the audience in model detail?

* Are material numbers and claims linked to supporting sources?

* Are missing evidence and unresolved questions clearly labeled?

* Can you verify the $33 million cash comparison in  `scenario_model_inputs.xlsx` , using cells C6 and E6 on the **Scenario Summary** worksheet?

* Has Finance reviewed the numbers, assumptions, recommendation, and final story before the presentation goes to the board?

## Demo 2: Turn the presentation workflow into a reusable skill

Test the workflow first, then save the version that works. A skill can preserve the presentation template, six-slide structure, sourcing rules, and Finance review expectations without carrying forward the current scenario figures.

After you approve the presentation, use this prompt:

```
Create a skill called forecast-update-for-the-board from this workflow. Save the presentation template, this six-slide structure, and the sourcing and Finance-review rules for future forecast updates.
```

### Find and share the skill

1. Open **Plugins** from the left sidebar and select **Skills**.

2. Open  `forecast-update-for-the-board`  and review the saved instructions, template, structure, sourcing rules, and review checks.

3. Edit the skill if your presentation format or Finance standards change.

4. Share the skill with your workspace when it is ready for others to use.

5. To find skills shared by colleagues, return to **Plugins** and scroll to your workspace. Shared skills appear there.

Sharing a skill gives the Finance team the same starting point. Colleagues do not have to find the template, reconstruct the slide structure, or remember the sourcing rules each time. Finance still reviews the new numbers, assumptions, and recommendation before anything is shared.

## Learn: Chat or Work?

* **I need the three biggest drivers in this monthly variance report before a meeting in five minutes → Chat.** One focused question; one fast answer.

* **Reconcile this close checklist with schedules, flag missing evidence, and build a sign-off package for Finance to review → Work.** Several sources, careful checking, and a complete package for Finance to review.

* **Use budget inputs, actuals, and plans to build a workbook with changes, questions, owners, and next steps → Work.** Several inputs, inconsistencies to resolve, and a structured workbook.

* **Help me explain this forecast change clearly to a leader who doesn’t work in Finance → Chat.** One short explanation with quick back-and-forth on the wording.

## Learn: Where Codex fits

Codex is built for software development and technical work. Work is built for broader knowledge work, including Finance reports, workbooks, and presentations. If you previously used Codex for those Finance tasks, start doing them in Work. If you use Codex for software development, keep using it there.

## Try it: Find your first Work task

You do not need to design the perfect workflow before you begin. Ask Work to suggest a few Finance tasks based on the work you are already doing, then wait for your choice.

```
Based on my recent work, suggest three Finance tasks I could hand off to ChatGPT Work. Tell me what you would create for each one and where I should start. Don’t begin until I choose.
```

## Learn: Use Work across surfaces

Everything in this webinar was demonstrated on  [chatgpt.com](https://chatgpt.com/). You can also use ChatGPT on the desktop app for Mac or Windows and on the mobile app for iOS or Android. Your work stays in sync, so you can start in the browser and check the task later from another device.

## Before you use the output

* Use only approved data and connected sources.

* Confirm the reporting period, currency, units, metric definitions, and scenario assumptions.

* Verify material numbers, calculations, recommendations, and citations before sharing.

* Keep actuals, forecasts, assumptions, scenarios, and recommendations clearly separated.

* Leave missing evidence unresolved until Finance has the information needed to make a call.

* Keep owner follow-ups, forecast changes, and system updates as drafts until a person reviews and approves them.

* Follow your organization’s AI, privacy, security, and records-management policies.

## What to try next

Choose one Finance task that is already on your plate. Give Work the source files, the result you need, and the boundaries it should respect. Review the file it creates and refine the instructions. If the job repeats, schedule it. If the method should stay consistent across the team, save and share it as a skill.

Thanks for joining!

## Popular

Resource

[ChatGPT 101 Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

Resource

[ChatGPT 102 Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide)

Resource

[ChatGPT 101: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide-interactive)

By Juliann Igo

Dive in

## Related

Resource

[ChatGPT Work for sales teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-sales-teams-webinar-resource-guide-2026-08-05)

Aug 6th, 2026 • Views 237

Resource

[Get started with ChatGPT Work: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/get-started-with-chatgpt-work-webinar-resource-guide-2026-08-03)

By Diana Stegall • Aug 4th, 2026 • Views 1K

[40:07](/public/clubs/work-users-ynjqu/videos/chatgpt-work-for-finance-teams-2026-08-13)

Video

[ChatGPT Work for finance teams [Recording]](/public/clubs/work-users-ynjqu/videos/chatgpt-work-for-finance-teams-2026-08-13)

Aug 13th, 2026 • Views 119

Resource

[How finance teams use Codex: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/how-finance-teams-use-codex-webinar-resource-guide-2026-05-19)

May 20th, 2026 • Views 2.8K

Resource

[ChatGPT Work for sales teams: Webinar Resource Guide](/public/clubs/work-users-ynjqu/resources/chatgpt-work-for-sales-teams-webinar-resource-guide-2026-08-05)

Aug 6th, 2026 • Views 237

[40:07](/public/clubs/work-users-ynjqu/videos/chatgpt-work-for-finance-teams-2026-08-13)

Video

[ChatGPT Work for finance teams [Recording]](/public/clubs/work-users-ynjqu/videos/chatgpt-work-for-finance-teams-2026-08-13)

Aug 13th, 2026 • Views 119

Resource

[How finance teams use Codex: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/how-finance-teams-use-codex-webinar-resource-guide-2026-05-19)

May 20th, 2026 • Views 2.8K

Resource

[Get started with ChatGPT Work: Webinar resource guide](/public/clubs/work-users-ynjqu/resources/get-started-with-chatgpt-work-webinar-resource-guide-2026-08-03)

By Diana Stegall • Aug 4th, 2026 • Views 1K
