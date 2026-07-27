<!-- source: https://learn.chatgpt.com/use-cases/prioritize-accounts -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Prioritize accounts

Rank accounts by risk, upside, urgency, and next action.

Difficulty **Intermediate**

Time horizon **30m**

Give ChatGPT account records, customer conversations, usage signals, renewal or growth context, and review rules, then ask it to produce a ranked account brief with rationale, risks, next actions, source links, and follow-up drafts.

## Best for

* Account managers and sales teams planning which accounts deserve attention first.
* Renewal, expansion, or pipeline reviews that combine CRM, conversations, usage, and account plans.
* Teams that want next actions grounded in sources rather than a score with no explanation.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/prioritize-accounts/?export=pdf)

Give ChatGPT account records, customer conversations, usage signals, renewal or growth context, and review rules, then ask it to produce a ranked account brief with rationale, risks, next actions, source links, and follow-up drafts.

Intermediate

30m

Related links

[OpenAI Academy: Everyday work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)  [Plugins](/codex/plugins)

## Best for

* Account managers and sales teams planning which accounts deserve attention first.
* Renewal, expansion, or pipeline reviews that combine CRM, conversations, usage, and account plans.
* Teams that want next actions grounded in sources rather than a score with no explanation.

## Skills & Plugins

* Spreadsheets

  Inspect account exports, score fields, and usage or pipeline signals.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read account plans, renewal notes, and approved customer context.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Find recent deal, renewal, or account context in approved threads.
* [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

  Check customer email context when it is part of the review record.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Inspect account exports, score fields, and usage or pipeline signals. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read account plans, renewal notes, and approved customer context. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Find recent deal, renewal, or account context in approved threads. |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | Check customer email context when it is part of the review record. |

## Starter prompt

I'm planning my week for [renewal, growth, or pipeline] accounts.
Use the account export, recent call transcripts, open customer email threads, usage dashboard, account plans, and the review rules I provide. Rank the [number] accounts I should focus on first.
For each account, include:
- why it matters now
- the main risk or upside
- the recommended next action
- source links
- stale or missing context
Draft follow-up notes only where the next step is clear. Do not update CRM records or contact customers.

I'm planning my week for [renewal, growth, or pipeline] accounts.
Use the account export, recent call transcripts, open customer email threads, usage dashboard, account plans, and the review rules I provide. Rank the [number] accounts I should focus on first.
For each account, include:
- why it matters now
- the main risk or upside
- the recommended next action
- source links
- stale or missing context
Draft follow-up notes only where the next step is clear. Do not update CRM records or contact customers.

## Bring the signals together

Account priority is more useful when it explains why an account matters now. Give ChatGPT the account list, recent conversations, usage or renewal signals, plans, and review rules, then ask for a ranked brief rather than an unexplained score.

1. Define the account segment, time window, and priority criteria.
2. Attach or name the CRM export, calls, emails, usage dashboard, plans, and review rules.
3. Run the starter prompt and ask for rationale, sources, stale context, and next actions per account.
4. Review any recommended customer follow-up before using it.
5. Hand approved actions to the system of record manually or through a separately reviewed workflow.

Keep risk, upside, urgency, and missing context visible as separate fields. This prevents a high-level ranking from hiding the evidence an account owner needs to make a judgment.

## Tune the priority list

Once the first ranking is useful, test how it changes under a different review rule, such as renewal date, expansion potential, activity gap, or customer risk.

Re-rank the account list using [priority rule].
Compare it with the original ranking and show:
- accounts that moved the most
- the source signals behind each move
- accounts with stale or missing context
- actions that remain the same across both rankings
- follow-up drafts that still need owner review
Do not update CRM records or contact customers.

## Related use cases

[![](/codex/use-cases/forecast-risk-review.webp)

### Review forecast risk

Give ChatGPT forecast snapshots, opportunity records, call notes, deal threads, email...

Data  Integrations](/codex/use-cases/forecast-risk-review)[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)[![](/codex/use-cases/consolidate-spreadsheets.webp)

### Consolidate spreadsheets

Give ChatGPT spreadsheet exports, join keys, targets, segment definitions, and reporting...

Data  Knowledge Work](/codex/use-cases/consolidate-spreadsheets)
