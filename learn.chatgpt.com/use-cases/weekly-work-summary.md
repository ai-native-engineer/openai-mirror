<!-- source: https://learn.chatgpt.com/use-cases/weekly-work-summary -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Write a weekly work summary

Turn a week of activity into a manager-ready update.

Difficulty **Easy**

Time horizon **30m**

Give ChatGPT your calendar, edited documents, sent messages, tracker, and project context, then ask it to summarize completed work, decisions, changes, blockers, follow-ups, and next priorities with source links.

## Best for

* Managers and individual contributors writing a recurring weekly update.
* Teams that need to reconstruct progress from several work surfaces.
* Updates that should distinguish confirmed facts from inference and include source links.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/weekly-work-summary/?export=pdf)

Give ChatGPT your calendar, edited documents, sent messages, tracker, and project context, then ask it to summarize completed work, decisions, changes, blockers, follow-ups, and next priorities with source links.

Easy

30m

Related links

[OpenAI Academy: Everyday work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)  [Agent skills](/codex/build-skills)

## Best for

* Managers and individual contributors writing a recurring weekly update.
* Teams that need to reconstruct progress from several work surfaces.
* Updates that should distinguish confirmed facts from inference and include source links.

## Skills & Plugins

* [Google Calendar](https://github.com/openai/plugins/tree/main/plugins/google-calendar)

  Reconstruct the meetings and milestones that shaped the week.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Review sent messages, decisions, blockers, and follow-ups in the relevant work channels.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read the tracker, project docs, and files that show what changed.
* Documents

  Turn the source review into a clear, editable weekly update.

| Skill | Why use it |
| --- | --- |
| [Google Calendar](https://github.com/openai/plugins/tree/main/plugins/google-calendar) | Reconstruct the meetings and milestones that shaped the week. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Review sent messages, decisions, blockers, and follow-ups in the relevant work channels. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read the tracker, project docs, and files that show what changed. |
| Documents | Turn the source review into a clear, editable weekly update. |

## Starter prompt

I'm writing my weekly update for [week or date range].
Use my calendar, documents I edited, messages I sent in [channels], [main tracker or planning doc], and any other context that is clearly relevant. Write a manager-ready summary covering:
- work completed
- decisions made
- important changes
- blockers
- follow-ups
- next week's priorities
Include source links where possible. Separate confirmed facts from inferences, and do not send or publish the update.

I'm writing my weekly update for [week or date range].
Use my calendar, documents I edited, messages I sent in [channels], [main tracker or planning doc], and any other context that is clearly relevant. Write a manager-ready summary covering:
- work completed
- decisions made
- important changes
- blockers
- follow-ups
- next week's priorities
Include source links where possible. Separate confirmed facts from inferences, and do not send or publish the update.

## Reconstruct the week from source activity

A useful weekly update should not depend on remembering every meeting or message. Point ChatGPT to the tracker, documents, calendar, and work-channel messages that represent the week, then ask it to separate completed work from plans or assumptions.

1. Define the week and the audience for the update.
2. Name the tracker, documents, calendar, and channels that are in scope.
3. Run the starter prompt and ask for source links behind important claims.
4. Check decisions, blockers, and follow-ups against the underlying threads.
5. Revise the length and tone for the destination without publishing it automatically.

Keep inferences visibly separate from confirmed work. This makes it easier for a manager or collaborator to correct the update without rereading every source.

## Prepare the next update

Once the first summary is accurate, ask ChatGPT to reuse its structure for the next reporting period and call out what changed since the prior version.

Use the same structure for the next weekly update.
Compare it with the previous update and identify:
- work newly completed
- decisions that changed
- blockers that remain
- follow-ups that moved owners or dates
- next priorities that are supported by current source context
Keep source links and separate confirmed facts from inferences. Return a draft only.

## Related use cases

[![](/codex/use-cases/new-hire-onboarding.webp)

### Coordinate new-hire onboarding

Use ChatGPT to gather approved new-hire context, stage tracker updates, draft team-by-team...

Integrations  Data](/codex/use-cases/new-hire-onboarding)[![](/codex/use-cases/draft-prds-from-sources.webp)

### Draft PRDs from internal context

Use ChatGPT with the $documents skill and connected plugins such as Linear, Slack, Notion or...

Integrations  Knowledge Work](/codex/use-cases/draft-prds-from-sources)[![](/codex/use-cases/meeting-prep-briefs.webp)

### Prepare meeting briefs

Use ChatGPT with Calendar, Drive, Slack, and Gmail to gather approved sources before a...

Integrations  Knowledge Work](/codex/use-cases/meeting-prep-briefs)
