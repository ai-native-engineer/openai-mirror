<!-- source: https://learn.chatgpt.com/use-cases/stalled-deal-diagnosis -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Diagnose a stalled deal

Find the real blocker and the next customer-facing move.

Difficulty **Intermediate**

Time horizon **30m**

Give ChatGPT stage history, closed activities, call transcripts, emails, deal threads, security or procurement notes, and account context, then ask it to explain the blocker, prior attempts, escalation path, and next action.

## Best for

* Deals that have stopped moving despite recent activity.
* Sales teams separating a real customer blocker from internal process or follow-up gaps.
* Escalation reviews that need a clear next customer-facing move and owner.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/stalled-deal-diagnosis/?export=pdf)

Give ChatGPT stage history, closed activities, call transcripts, emails, deal threads, security or procurement notes, and account context, then ask it to explain the blocker, prior attempts, escalation path, and next action.

Intermediate

30m

Related links

[OpenAI Academy: Sales teams](https://openai.com/academy/codex-for-work/how-sales-teams-use-codex/)  [Turn meetings into follow-ups](/codex/use-cases/zoom-meeting-follow-ups)

## Best for

* Deals that have stopped moving despite recent activity.
* Sales teams separating a real customer blocker from internal process or follow-up gaps.
* Escalation reviews that need a clear next customer-facing move and owner.

## Skills & Plugins

* Spreadsheets

  Trace stage history, activity, and timing signals from CRM exports.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read account context, security or procurement notes, and prior deal plans.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Review deal threads and internal escalation context.
* [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

  Check customer and internal email history that explains the stall.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Trace stage history, activity, and timing signals from CRM exports. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read account context, security or procurement notes, and prior deal plans. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Review deal threads and internal escalation context. |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | Check customer and internal email history that explains the stall. |

## Starter prompt

Diagnose why [deal or account] is stalled.
Use the opportunity stage history, closed activities, call transcripts, email threads, deal threads, security, legal, or procurement notes, and account context I provide.
Return:
- the most likely blocker and supporting evidence
- prior attempts and what changed
- customer, technical, legal, or procurement dependencies
- escalation path and owners
- the next customer-facing move
- missing context and risks
Separate sourced facts from inference. Draft follow-up language only; do not send it or update CRM records.

Diagnose why [deal or account] is stalled.
Use the opportunity stage history, closed activities, call transcripts, email threads, deal threads, security, legal, or procurement notes, and account context I provide.
Return:
- the most likely blocker and supporting evidence
- prior attempts and what changed
- customer, technical, legal, or procurement dependencies
- escalation path and owners
- the next customer-facing move
- missing context and risks
Separate sourced facts from inference. Draft follow-up language only; do not send it or update CRM records.

## Trace the stall across the full deal history

The visible stage is rarely the whole blocker. Give ChatGPT stage history, closed activities, calls, emails, deal threads, security or procurement notes, and account context so it can distinguish customer, technical, legal, and internal process issues.

1. Define the deal, time window, and decision the diagnosis should support.
2. Attach stage history, activity, transcripts, email, threads, security or procurement notes, and account context.
3. Ask ChatGPT to build a timeline before naming a root cause.
4. Run the starter prompt and review evidence, prior attempts, dependencies, escalation path, and next move.
5. Have the deal owner approve any customer-facing follow-up before sending it.

Keep the diagnosis factual and time-bounded. If the blocker is uncertain, list the smallest customer or internal check that would distinguish the competing explanations.

## Turn diagnosis into a recovery plan

After the blocker is agreed, ask ChatGPT to create a narrow recovery plan with owners, dependencies, and a proof point for each step.

Create a recovery plan for this stalled deal.
Include:
- confirmed blocker and supporting evidence
- one or two hypotheses still to test
- customer-facing next step
- internal dependency and owner
- escalation path
- target date and proof of progress
- follow-up language for review
Do not send the message, update CRM, or promise a date that the sources do not support.

## Related use cases

[![](/codex/use-cases/strategic-account-plan.webp)

### Refresh a strategic account plan

Give ChatGPT account and opportunity records, calls, threads, emails, usage notes, product...

Integrations  Knowledge Work](/codex/use-cases/strategic-account-plan)[![](/codex/use-cases/new-hire-onboarding.webp)

### Coordinate new-hire onboarding

Use ChatGPT to gather approved new-hire context, stage tracker updates, draft team-by-team...

Integrations  Data](/codex/use-cases/new-hire-onboarding)[![](/codex/use-cases/draft-prds-from-sources.webp)

### Draft PRDs from internal context

Use ChatGPT with the $documents skill and connected plugins such as Linear, Slack, Notion or...

Integrations  Knowledge Work](/codex/use-cases/draft-prds-from-sources)
