<!-- source: https://learn.chatgpt.com/use-cases/daily-work-brief -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Create a daily work brief

Turn calendar, messages, email, and project context into a focused plan.

Difficulty **Easy**

Time horizon **5m**

Give ChatGPT the sources behind your day, then ask it to identify priorities, meeting preparation, reply needs, decisions owed, and useful FYIs in one reviewable brief that can improve through feedback and recurring checks.

## Best for

* People whose priorities are spread across calendar, email, Slack, docs, and follow-up lists.
* Workdays with several meetings, decisions, and reply-worthy messages to triage.
* Teams that want a short source-backed brief they can refine and run on a schedule.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/daily-work-brief/?export=pdf)

Give ChatGPT the sources behind your day, then ask it to identify priorities, meeting preparation, reply needs, decisions owed, and useful FYIs in one reviewable brief that can improve through feedback and recurring checks.

Easy

5m

Related links

[OpenAI Academy: Everyday work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)  [Scheduled tasks](/codex/automations)  [Plugins](/codex/plugins)

## Best for

* People whose priorities are spread across calendar, email, Slack, docs, and follow-up lists.
* Workdays with several meetings, decisions, and reply-worthy messages to triage.
* Teams that want a short source-backed brief they can refine and run on a schedule.

## Skills & Plugins

* [Google Calendar](https://github.com/openai/plugins/tree/main/plugins/google-calendar)

  Review the day's meetings, timing, and preparation needs.
* [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

  Find recent email that needs a reply or changes today's priorities.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Find direct messages, mentions, decisions, and follow-ups that need attention.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read the approved running notes, trackers, or planning docs behind the day's work.

| Skill | Why use it |
| --- | --- |
| [Google Calendar](https://github.com/openai/plugins/tree/main/plugins/google-calendar) | Review the day's meetings, timing, and preparation needs. |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | Find recent email that needs a reply or changes today's priorities. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Find direct messages, mentions, decisions, and follow-ups that need attention. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read the approved running notes, trackers, or planning docs behind the day's work. |

## Starter prompt

Build my work brief for [date].
Review my calendar, unread direct messages and mentions from the last 24 hours, unread email from the last 24 hours, open follow-ups, and the project notes or trackers I name. If a prior brief is available, call out what changed. Create a short brief with:
- top priorities
- meeting preparation
- messages that need replies
- decisions I owe
- useful FYIs
- missing access or uncertain context
Keep confirmed facts separate from inference. Do not send messages, change documents, or create tasks.

Build my work brief for [date].
Review my calendar, unread direct messages and mentions from the last 24 hours, unread email from the last 24 hours, open follow-ups, and the project notes or trackers I name. If a prior brief is available, call out what changed. Create a short brief with:
- top priorities
- meeting preparation
- messages that need replies
- decisions I owe
- useful FYIs
- missing access or uncertain context
Keep confirmed facts separate from inference. Do not send messages, change documents, or create tasks.

## Start with the context behind today

ChatGPT is most useful when it can see the calendar, messages, email, follow-ups, and notes that shape the day. Give it the sources it is allowed to use and ask it to distinguish urgent work from useful context.

[ 
Your browser does not support the video tag.
](https://cdn.openai.com/codex/docs/developers-website/use-cases/proactive-teammate-v2.mp4)

1. Name the date, working hours, and sources ChatGPT may review.
2. Ask it to inventory access gaps before drawing conclusions.
3. Run the starter prompt to create priorities, meeting preparation, replies, decisions, and FYIs.
4. Review the source links, move uncertain items into an open-questions list, and tell ChatGPT which items were useful or noisy.
5. Continue in the same chat when a priority needs a draft, a deeper source review, or a recurring check.

Keep the brief short enough to use at the start of the day. Do not give ChatGPT permission to send messages or update source systems until you have reviewed the proposed actions.

## Make the brief recurring

Start with one manual brief. After the structure reliably surfaces the right priorities, schedule a task from the same chat so ChatGPT can return to the approved sources each morning and compare the new brief with the previous one. Keep correcting the chat when it overweights noise or misses an important source.

Schedule a task from this chat to prepare my daily work brief every weekday morning at [time].
Check the same approved sources, compare the result with the previous brief, and only surface new or materially changed priorities, meetings, replies, decisions, and blockers.
Do not send messages, edit source files, or create tasks.

## Review what changed

Ask ChatGPT to compare a new pass with the previous brief so you can focus on newly arrived messages, changed meetings, and follow-ups that now need attention.

Compare today's brief with the previous brief.
List:
- new priorities or decisions
- meeting changes
- new messages that need a reply
- follow-ups that are now blocked or overdue
- items that no longer need attention
- source gaps or uncertain conclusions
Do not send messages or change any source files.

## Related use cases

[![](/codex/use-cases/audit-workflow.webp)

### Audit a workflow

Give ChatGPT trackers, process docs, handoff notes, dashboards, ticket history, team...

Automation  Integrations](/codex/use-cases/audit-workflow)[![](/codex/use-cases/launch-campaign-kit.webp)

### Build a launch campaign kit

Give ChatGPT launch plans, product notes, trackers, page links, team discussion, creative...

Automation  Integrations](/codex/use-cases/launch-campaign-kit)[![](/codex/use-cases/zoom-meeting-follow-ups.webp)

### Turn meetings into follow-ups

Use ChatGPT with Zoom transcripts and AI Companion summaries to draft customer follow-up...

Automation  Integrations](/codex/use-cases/zoom-meeting-follow-ups)
