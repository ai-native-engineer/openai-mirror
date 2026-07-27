<!-- source: https://learn.chatgpt.com/use-cases/feedback-synthesis -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Turn feedback into actions

Synthesize feedback from multiple sources into a reviewable artifact.

Difficulty **Easy**

Time horizon **30m**

Connect ChatGPT to multiple data sources such as Slack, GitHub, Linear, or Google Drive to group feedback into a reviewable Google Sheet, Google Doc, Slack update, or recurring feedback check.

## Best for

* Analyzing feedback from Slack channels, issue threads, survey exports, support-ticket CSVs, or research notes.
* Teams that need to turn feedback into actionable insights.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/feedback-synthesis/?export=pdf)

Connect ChatGPT to multiple data sources such as Slack, GitHub, Linear, or Google Drive to group feedback into a reviewable Google Sheet, Google Doc, Slack update, or recurring feedback check.

Easy

30m

Related links

[Plugins](/codex/plugins)  [Scheduled tasks](/codex/automations)  [Agent skills](/codex/build-skills)

## Best for

* Analyzing feedback from Slack channels, issue threads, survey exports, support-ticket CSVs, or research notes.
* Teams that need to turn feedback into actionable insights.

## Skills & Plugins

* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Read approved feedback channels or thread links.
* [GitHub](https://github.com/openai/plugins/tree/main/plugins/github)

  Read issues, PR comments, and discussion threads.
* [Linear](https://github.com/openai/plugins/tree/main/plugins/linear)

  Read bug or feature queues.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read feedback docs, exports, and folders, then create a Google Doc or Sheet.
* [Google Sheets](/codex/plugins)

  Create a feedback sheet the team can sort, comment on, and update.

| Skill | Why use it |
| --- | --- |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Read approved feedback channels or thread links. |
| [GitHub](https://github.com/openai/plugins/tree/main/plugins/github) | Read issues, PR comments, and discussion threads. |
| [Linear](https://github.com/openai/plugins/tree/main/plugins/linear) | Read bug or feature queues. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read feedback docs, exports, and folders, then create a Google Doc or Sheet. |
| [Google Sheets](/codex/plugins) | Create a feedback sheet the team can sort, comment on, and update. |

## Starter prompt

Can you synthesize the beta feedback on [feature or product area] into a @google-sheets review sheet?
Use these sources:
- @slack [feedback channel or thread links]
- @github [issue search or issue links]
- @google-drive [survey export, notes doc, or Drive folder]
In the sheet, group repeated feedback, include source links or IDs, mark confidence, and call out which items need product or engineering follow-up.
Keep names and private quotes out of the visible summary unless I approve them. Do not post, send, create issues, or assign owners.

Can you synthesize the beta feedback on [feature or product area] into a @google-sheets review sheet?
Use these sources:
- @slack [feedback channel or thread links]
- @github [issue search or issue links]
- @google-drive [survey export, notes doc, or Drive folder]
In the sheet, group repeated feedback, include source links or IDs, mark confidence, and call out which items need product or engineering follow-up.
Keep names and private quotes out of the visible summary unless I approve them. Do not post, send, create issues, or assign owners.

When feedback is spread across a Slack channel, a survey export, and a few issue threads, ChatGPT can pull it together into a Google Sheet or Doc that the team can review.

[ 
Your browser does not support the video tag.
](https://cdn.openai.com/codex/docs/developers-website/use-cases/feedback-synthesis-into-gsheets.mp4)

## Create the first version

1. Give ChatGPT the feedback sources and one sentence of context.
2. Ask for a Google Sheet or Doc with themes, evidence links, questions, and follow-ups.
3. Use the same chat to turn the reviewed sheet into a Slack update or issue draft.
4. Pin the chat and schedule a task from it if the feedback source keeps changing.

Use the starter prompt on this page for the first pass. The sources can be plugin links, attached files, or files in Google Drive.

## Turn the sheet into the next draft

Once the sheet exists, use the same chat to make it useful for the next person. Ask ChatGPT to add a column, split a theme, draft a Slack update, or turn a reviewed theme into an issue draft.

Using the reviewed feedback sheet, draft a short Slack update.
Audience: [team or channel]
Include:
- what changed
- the top feedback themes
- link to the sheet
- the decision or follow-up needed
Draft only. Do not post it.

## Keep a feedback channel current

For a Slack channel or issue queue that keeps getting new reports, pin the chat and ask ChatGPT to schedule a task inside it.

Schedule a task from this chat to check this feedback source every [weekday morning / Monday / release day].
Source: [Slack channel, GitHub search, Linear view, or Google Drive folder]
Use this reviewed Sheet or Doc as the running summary: [link]
Only update me when there is a new theme, stronger evidence for an existing theme, or a source you cannot read. Keep the Sheet or Doc current. Do not post, send, create issues, or assign owners.

## Related use cases

[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)[![](/codex/use-cases/monthly-business-review-narrative.webp)

### Prepare a business review

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior...

Data  Integrations](/codex/use-cases/monthly-business-review-narrative)[![](/codex/use-cases/cfo-board-reporting-pack.webp)

### Prepare a leadership reporting pack

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs...

Data  Integrations](/codex/use-cases/cfo-board-reporting-pack)
