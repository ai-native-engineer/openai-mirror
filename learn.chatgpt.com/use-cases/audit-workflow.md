<!-- source: https://learn.chatgpt.com/use-cases/audit-workflow -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Audit a workflow

Turn a messy process into a clear audit and automation plan.

Difficulty **Intermediate**

Time horizon **1h**

Give ChatGPT trackers, process docs, handoff notes, dashboards, ticket history, team discussions, and constraints, then ask it to map the current workflow, identify stuck points, and draft an automation-ready process spec.

## Best for

* Operational workflows with repeated manual steps, unclear ownership, or frequent handoff failures.
* Teams deciding whether a process is ready for automation.
* Audits that need current steps, stuck points, missing data, and outdated sources documented together.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/audit-workflow/?export=pdf)

Give ChatGPT trackers, process docs, handoff notes, dashboards, ticket history, team discussions, and constraints, then ask it to map the current workflow, identify stuck points, and draft an automation-ready process spec.

Intermediate

1h

Related links

[OpenAI Academy: Everyday work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)  [Scheduled tasks](/codex/automations)  [Agent skills](/codex/build-skills)

## Best for

* Operational workflows with repeated manual steps, unclear ownership, or frequent handoff failures.
* Teams deciding whether a process is ready for automation.
* Audits that need current steps, stuck points, missing data, and outdated sources documented together.

## Skills & Plugins

* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read process documentation, trackers, handoff notes, and source artifacts.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Review team discussion, repeated questions, and decisions that explain how the process runs.
* Spreadsheets

  Inspect workflow trackers, timestamps, ownership, and KPI data.
* Documents

  Produce the audit brief, updated process document, and automation spec.

| Skill | Why use it |
| --- | --- |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read process documentation, trackers, handoff notes, and source artifacts. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Review team discussion, repeated questions, and decisions that explain how the process runs. |
| Spreadsheets | Inspect workflow trackers, timestamps, ownership, and KPI data. |
| Documents | Produce the audit brief, updated process document, and automation spec. |

## Starter prompt

Audit the [workflow] before [deadline or next cohort].
Use the current tracker, process documentation, handoff notes, KPI dashboard, ticket history, team discussion, and workflow constraints I provide. Create:
- a workflow audit brief with current steps, owners, stuck points, repeated questions, and missing data
- an updated process document
- a short automation spec for the two most repetitive manual steps
Flag outdated or conflicting sources. Keep the automation proposal narrow, and do not implement or publish changes.

Audit the [workflow] before [deadline or next cohort].
Use the current tracker, process documentation, handoff notes, KPI dashboard, ticket history, team discussion, and workflow constraints I provide. Create:
- a workflow audit brief with current steps, owners, stuck points, repeated questions, and missing data
- an updated process document
- a short automation spec for the two most repetitive manual steps
Flag outdated or conflicting sources. Keep the automation proposal narrow, and do not implement or publish changes.

## Map the current process

Workflow automation is easier to evaluate when the current process is explicit. Give ChatGPT the tracker, process docs, handoff notes, tickets, metrics, and discussions that show how work actually moves.

1. Define the workflow boundary, users, inputs, outputs, and review date.
2. Attach the current process document, tracker, handoff notes, tickets, and KPI context.
3. Ask ChatGPT to reconcile the documented process with observed discussion and tracker state.
4. Run the starter prompt to produce the audit brief, process document, and narrow automation spec.
5. Review permissions, exception paths, irreversible actions, and ownership before implementation.

Keep the automation proposal separate from the process description. A good audit explains what should remain manual, what can be verified automatically, and what evidence the new workflow must produce.

## Choose the smallest useful automation

After the audit, ask ChatGPT to compare candidate steps by repetition, risk, data quality, and verification cost.

Rank the automation candidates from this workflow audit.
For each candidate, show:
- current manual effort and repetition
- required inputs and permissions
- failure and exception paths
- verification artifact
- reversibility and human approval point
- reason to defer or automate
Recommend only the smallest safe first step. Do not implement it or change the source process document.

## Related use cases

[![](/codex/use-cases/launch-campaign-kit.webp)

### Build a launch campaign kit

Give ChatGPT launch plans, product notes, trackers, page links, team discussion, creative...

Automation  Integrations](/codex/use-cases/launch-campaign-kit)[![](/codex/use-cases/daily-work-brief.webp)

### Create a daily work brief

Give ChatGPT the sources behind your day, then ask it to identify priorities, meeting...

Automation  Integrations](/codex/use-cases/daily-work-brief)[![](/codex/use-cases/zoom-meeting-follow-ups.webp)

### Turn meetings into follow-ups

Use ChatGPT with Zoom transcripts and AI Companion summaries to draft customer follow-up...

Automation  Integrations](/codex/use-cases/zoom-meeting-follow-ups)
