<!-- source: https://learn.chatgpt.com/use-cases/manage-your-inbox -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Manage your inbox

Have ChatGPT find the emails that matter and write the replies in your voice.

Difficulty **Easy**

Time horizon **5m**

Use ChatGPT with Gmail to find emails that need attention, draft responses in your voice, pull context from the tools where your work happens, and keep watching for new replies on a schedule.

## Best for

* People who want ChatGPT to find emails that need attention instead of manually sorting them.
* Recurring inbox checks where ChatGPT can create reviewable drafts in the background.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/manage-your-inbox/?export=pdf)

Use ChatGPT with Gmail to find emails that need attention, draft responses in your voice, pull context from the tools where your work happens, and keep watching for new replies on a schedule.

Easy

5m

Related links

[Plugins](/codex/plugins)  [Scheduled tasks](/codex/automations)

## Best for

* People who want ChatGPT to find emails that need attention instead of manually sorting them.
* Recurring inbox checks where ChatGPT can create reviewable drafts in the background.

## Skills & Plugins

* [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

  Search and triage Gmail threads, read the surrounding conversation, create reply drafts, and organize messages when you explicitly ask.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Check team-message context when an email needs the latest decision, owner, asset, or blocker.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read source docs, FAQs, notes, or approved writing examples that should shape the draft.

| Skill | Why use it |
| --- | --- |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | Search and triage Gmail threads, read the surrounding conversation, create reply drafts, and organize messages when you explicitly ask. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Check team-message context when an email needs the latest decision, owner, asset, or blocker. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read source docs, FAQs, notes, or approved writing examples that should shape the draft. |

## Starter prompt

Can you check my @gmail, figure out what I need to respond to, and write drafts in my voice.
Use my recent sent replies or @google-drive [writing examples] for tone.
Use @slack, @google-drive, or other sources where my work happens when the email is missing the latest decision, owner, file, or blocker.

Can you check my @gmail, figure out what I need to respond to, and write drafts in my voice.
Use my recent sent replies or @google-drive [writing examples] for tone.
Use @slack, @google-drive, or other sources where my work happens when the email is missing the latest decision, owner, file, or blocker.

## Review your inbox

Ask ChatGPT to check Gmail, find the messages that deserve a reply, and write drafts in your voice. It can use recent sent mail or approved writing examples for style, then search Slack, docs, project notes, or other tools when the email lacks context on its own.

Use ChatGPT for the first pass over your inbox: find the emails that need your attention, draft the replies, and bring in the work context that explains the bigger picture.

1. Ask ChatGPT to review Gmail for emails that need your attention.
2. Ask it to use Slack, docs, or project notes for context that explains the bigger picture.
3. Tell ChatGPT which drafts were useful and which emails it should ignore next time.
4. Schedule a task from the chat when it becomes useful, and pin the chat if you want fast access later.

Use the Gmail plugin directly. You can give ChatGPT a broad inbox request, a time window, or a label if you already know the scope. If tone matters, ask ChatGPT to look at recent sent replies or a doc with examples before drafting.

Use the starter prompt on this page for the first inbox pass. ChatGPT should return a short queue: drafts for emails that need attention, messages that can wait, and the context it used when the answer depended on more than the email thread.

## Teach ChatGPT your taste

Treat the first pass like calibration. If ChatGPT drafts too many replies, tell it which emails were noise. If it misses something important, tell it why that thread mattered. If the tone is off, correct the draft directly.

Good start. For future passes:
- draft replies for [the kinds of emails that matter]
- ignore [newsletters, FYIs, calendar churn, or other noise]
- sound more like [shorter, warmer, more direct, or less formal]
- use @slack for context when a thread mentions [project, account, or team]

Over time, ChatGPT should get better at deciding what needs a draft and what can stay out of your way.

## Schedule an email triage task inside the chat

You can schedule an inbox check-in task from the same chat. On each scheduled run, ChatGPT checks Gmail and the context sources you named, then posts only when there are emails that need your attention or drafts worth reviewing.

Once the drafts look useful, ask ChatGPT to keep an eye on Gmail. Email triage is a good job to automate: the drafts are reviewable, and you still decide what gets sent.

Can you keep an eye on my @gmail and create drafts for emails that need my attention?
Check [hourly, every weekday morning, or at 4 PM].
Use @slack or @google-drive for context when needed. Skip obvious noise. Do not send anything.

You can [schedule a task inside this chat](/codex/automations#schedule-a-task-inside-a-chat) after the chat has a good sense of your reply patterns. If ChatGPT finds an email that needs a decision it cannot make, it should flag the question instead of guessing.

## Organize your inbox

The Gmail plugin can also help organize your inbox. Keep that as a separate command after you trust the triage.

Archive or label the low-priority emails from this pass.
Only touch the messages you listed as [can wait, newsletter, or already handled].
Do not delete or send anything.

For deletion, make the instruction explicit and narrow. Drafting replies is safe to automate for review; destructive cleanup should stay deliberate.

## Related use cases

[![](/codex/use-cases/audit-workflow.webp)

### Audit a workflow

Give ChatGPT trackers, process docs, handoff notes, dashboards, ticket history, team...

Automation  Integrations](/codex/use-cases/audit-workflow)[![](/codex/use-cases/launch-campaign-kit.webp)

### Build a launch campaign kit

Give ChatGPT launch plans, product notes, trackers, page links, team discussion, creative...

Automation  Integrations](/codex/use-cases/launch-campaign-kit)[![](/codex/use-cases/daily-work-brief.webp)

### Create a daily work brief

Give ChatGPT the sources behind your day, then ask it to identify priorities, meeting...

Automation  Integrations](/codex/use-cases/daily-work-brief)
