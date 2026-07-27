<!-- source: https://learn.chatgpt.com/use-cases/forecast-risk-review -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Review forecast risk

Decide which deals belong in commit, upside, or pull.

Difficulty **Intermediate**

Time horizon **30m**

Give ChatGPT forecast snapshots, opportunity records, call notes, deal threads, email context, support or legal status, usage signals, and owner notes, then ask it to produce a sourced forecast risk review with deal-by-deal rationale.

## Best for

* Sales leaders preparing a weekly or monthly forecast call.
* Deal reviews where commit position depends on customer urgency, blockers, and close path.
* Teams that need sourced facts separated from inferred risk and owner follow-ups.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/forecast-risk-review/?export=pdf)

Give ChatGPT forecast snapshots, opportunity records, call notes, deal threads, email context, support or legal status, usage signals, and owner notes, then ask it to produce a sourced forecast risk review with deal-by-deal rationale.

Intermediate

30m

Related links

[OpenAI Academy: Sales teams](https://openai.com/academy/codex-for-work/how-sales-teams-use-codex/)  [Prioritize accounts](/codex/use-cases/prioritize-accounts)

## Best for

* Sales leaders preparing a weekly or monthly forecast call.
* Deal reviews where commit position depends on customer urgency, blockers, and close path.
* Teams that need sourced facts separated from inferred risk and owner follow-ups.

## Skills & Plugins

* Spreadsheets

  Compare forecast snapshots, opportunity data, activity, and deal-level metrics.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read forecast files, account plans, and approved deal context.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Review deal threads, support context, and current blockers.
* [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

  Check customer or internal email context that affects forecast position.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Compare forecast snapshots, opportunity data, activity, and deal-level metrics. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read forecast files, account plans, and approved deal context. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Review deal threads, support context, and current blockers. |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | Check customer or internal email context that affects forecast position. |

## Starter prompt

Review [accounts or deals] for the [forecast period] forecast call.
Use the CRM opportunity export, forecast snapshots, call notes, email threads, Slack deal context, support escalations, legal or procurement status, usage signals, and owner notes I provide.
Recommend what should stay in commit, move to upside, or get pulled. Separate sourced facts from inferred risk, explain the rationale by deal, list blockers and missing context, and end with owner follow-ups. Do not update CRM records or change the forecast.

Review [accounts or deals] for the [forecast period] forecast call.
Use the CRM opportunity export, forecast snapshots, call notes, email threads, Slack deal context, support escalations, legal or procurement status, usage signals, and owner notes I provide.
Recommend what should stay in commit, move to upside, or get pulled. Separate sourced facts from inferred risk, explain the rationale by deal, list blockers and missing context, and end with owner follow-ups. Do not update CRM records or change the forecast.

## Review the forecast from the deal record outward

Forecast risk is easier to assess when the forecast position is checked against opportunity details, recent customer activity, blockers, and the close path. Give ChatGPT the full review record and require a rationale for every recommendation.

1. Define the forecast period, teams or deals in scope, and commit vocabulary.
2. Attach the CRM export, forecast snapshots, calls, emails, deal threads, support, legal, procurement, usage, and owner notes.
3. Ask ChatGPT to separate sourced facts from inferred risk.
4. Run the starter prompt and inspect each deal’s rationale, blocker, and next owner action.
5. Confirm recommendations with the sales owner before changing the forecast system.

Do not infer confidence from stage alone. A useful review shows the evidence, missing context, customer urgency, and close-path risk behind each commit, upside, or pull recommendation.

## Prepare for the forecast call

Use a follow-up pass to turn the review into a short call agenda with the fewest questions needed to resolve uncertainty.

Turn this forecast review into a call agenda.
Group deals by:
- commit risk
- missing evidence
- customer or legal blocker
- decision needed from leadership
- owner follow-up
For each deal, write the one question that would most reduce uncertainty. Do not change the forecast or send the agenda.

## Related use cases

[![](/codex/use-cases/prioritize-accounts.webp)

### Prioritize accounts

Give ChatGPT account records, customer conversations, usage signals, renewal or growth...

Data  Integrations](/codex/use-cases/prioritize-accounts)[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)[![](/codex/use-cases/consolidate-spreadsheets.webp)

### Consolidate spreadsheets

Give ChatGPT spreadsheet exports, join keys, targets, segment definitions, and reporting...

Data  Knowledge Work](/codex/use-cases/consolidate-spreadsheets)
