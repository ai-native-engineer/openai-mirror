<!-- source: https://learn.chatgpt.com/use-cases/monthly-business-review-narrative -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Prepare a business review

Turn recurring KPI, close, and forecast inputs into a sourced performance narrative.

Difficulty **Intermediate**

Time horizon **30m**

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior reviews, and owner notes, then ask it to explain material changes, variances, anomalies, risks, data-quality issues, and follow-ups in a review-ready narrative.

## Best for

* Weekly, monthly, or quarterly business reviews for product, operations, growth, or finance teams.
* Reviews that combine KPI dashboards, workbooks, forecasts, prior reporting, and owner notes.
* Teams that need material changes, anomalies, and every important figure tied to a source before leadership review.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/monthly-business-review-narrative/?export=pdf)

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior reviews, and owner notes, then ask it to explain material changes, variances, anomalies, risks, data-quality issues, and follow-ups in a review-ready narrative.

Intermediate

30m

Related links

[OpenAI Academy: Data science teams](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex/)  [Plugins](/codex/plugins)  [Agent skills](/codex/build-skills)

## Best for

* Weekly, monthly, or quarterly business reviews for product, operations, growth, or finance teams.
* Reviews that combine KPI dashboards, workbooks, forecasts, prior reporting, and owner notes.
* Teams that need material changes, anomalies, and every important figure tied to a source before leadership review.

## Skills & Plugins

* Documents

  Create and verify an editable narrative document with a clear executive structure and source notes.
* Spreadsheets

  Inspect close workbooks and forecast files, validate figures, and trace material numbers to their source tabs.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read approved workbooks, prior reviews, dashboards, and owner notes from exact Drive files or folders.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Read approved finance-close threads and owner context when those messages are part of the review record.

| Skill | Why use it |
| --- | --- |
| Documents | Create and verify an editable narrative document with a clear executive structure and source notes. |
| Spreadsheets | Inspect close workbooks and forecast files, validate figures, and trace material numbers to their source tabs. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read approved workbooks, prior reviews, dashboards, and owner notes from exact Drive files or folders. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Read approved finance-close threads and owner context when those messages are part of the review record. |

## Starter prompt

Use $documents and $spreadsheets to prepare the [weekly, monthly, or quarterly] business review for [business or team].
Use the KPI dashboard, metric definitions, close workbook, revenue and expense tables, forecast update, prior review, and owner notes I provide. If any inputs are in connected plugins, use only the exact @google-drive files or @slack threads I name.
Create an editable document with a short leadership summary, material KPI changes, key variances, anomalies, changes since forecast, risks, data-quality checks, review questions, and follow-ups by owner. Include supporting charts where useful. Cite the workbook tab, dashboard, or source note behind every material number. Do not fill gaps with invented figures; list unsupported claims and missing inputs for review.

Use $documents and $spreadsheets to prepare the [weekly, monthly, or quarterly] business review for [business or team].
Use the KPI dashboard, metric definitions, close workbook, revenue and expense tables, forecast update, prior review, and owner notes I provide. If any inputs are in connected plugins, use only the exact @google-drive files or @slack threads I name.
Create an editable document with a short leadership summary, material KPI changes, key variances, anomalies, changes since forecast, risks, data-quality checks, review questions, and follow-ups by owner. Include supporting charts where useful. Cite the workbook tab, dashboard, or source note behind every material number. Do not fill gaps with invented figures; list unsupported claims and missing inputs for review.

## Build from the recurring review record

A business review should explain what changed, why it changed, and what the team needs to decide. ChatGPT can assemble the first draft from KPI dashboards, metric definitions, close workbooks, forecast updates, prior reviews, and owner notes while keeping the source trail visible.

## Prepare the review sources

Name the exact files, dashboards, and conversations ChatGPT should use. Include the reporting period, audience, materiality thresholds, prior forecast, and any required sections. Avoid broad searches across a connected workspace when the review should rely on a controlled set of approved inputs.

1. Define the review period, audience, and materiality threshold.
2. Attach the KPI dashboard, metric definitions, relevant workbooks, forecast update, prior review, and owner notes.
3. Ask ChatGPT to check data quality and trace material numbers before drafting.
4. Run the starter prompt and review changes, variances, anomalies, risks, assumptions, and follow-ups.
5. Confirm the source links and owner actions before the review enters leadership discussion.

## Review the narrative

A useful draft separates supported conclusions from questions that still need an owner. It should call out material KPI movement and changes since forecast, explain risks in plain language, and make follow-ups easy to assign.

Compare this business review with the prior review and audit the narrative.
Show:
- newly material KPI changes and variances
- anomalies that resolved or worsened
- risks and owner follow-ups that remain open
- metrics whose definitions or sources changed
- unsupported claims or data-quality issues
- questions the team should ask next
Cite the source behind every material comparison, flag uncertainty, and keep unresolved items grouped by owner.

## Related use cases

[![](/codex/use-cases/cfo-board-reporting-pack.webp)

### Prepare a leadership reporting pack

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs...

Data  Integrations](/codex/use-cases/cfo-board-reporting-pack)[![](/codex/use-cases/research-to-decision-memo.webp)

### Turn research into a decision memo

Give ChatGPT research, planning documents, models, dashboards, stakeholder context, and...

Data  Integrations](/codex/use-cases/research-to-decision-memo)[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)
