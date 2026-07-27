<!-- source: https://learn.chatgpt.com/use-cases/consolidate-spreadsheets -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Consolidate spreadsheets

Join spreadsheet exports into one refreshable workbook.

Difficulty **Intermediate**

Time horizon **1h**

Give ChatGPT spreadsheet exports, join keys, targets, segment definitions, and reporting rules, then ask it to create a consolidated workbook with cleaned joins, charts, insights, assumptions, refresh instructions, and mismatch review.

## Best for

* Reporting workflows that combine multiple exports into one updateable workbook.
* Pipeline, account, operations, or performance analysis with explicit join keys and targets.
* Teams that need mismatched records and refresh assumptions isolated for review.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/consolidate-spreadsheets/?export=pdf)

Give ChatGPT spreadsheet exports, join keys, targets, segment definitions, and reporting rules, then ask it to create a consolidated workbook with cleaned joins, charts, insights, assumptions, refresh instructions, and mismatch review.

Intermediate

1h

Related links

[OpenAI Academy: Everyday work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)  [Spreadsheet skills](/codex/build-skills)

## Best for

* Reporting workflows that combine multiple exports into one updateable workbook.
* Pipeline, account, operations, or performance analysis with explicit join keys and targets.
* Teams that need mismatched records and refresh assumptions isolated for review.

## Skills & Plugins

* Spreadsheets

  Inspect exports, clean joins, build formulas, and validate the resulting workbook.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read approved spreadsheet sources and reporting templates from Drive.
* Documents

  Add clear assumptions, refresh instructions, and a review summary.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Inspect exports, clean joins, build formulas, and validate the resulting workbook. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read approved spreadsheet sources and reporting templates from Drive. |
| Documents | Add clear assumptions, refresh instructions, and a review summary. |

## Starter prompt

Consolidate the attached spreadsheet exports into one updateable workbook.
Join on [record or account key]. Clean duplicate records, calculate [metrics or views], compare [actuals or pipeline] with [target], and create a dashboard with charts and plain-English insights.
Include:
- assumptions and refresh instructions
- a review section for mismatched keys or records that did not join cleanly
- a short change log
Do not invent join keys or silently merge conflicting records. Preserve the original files and return the consolidated workbook for review.

Consolidate the attached spreadsheet exports into one updateable workbook.
Join on [record or account key]. Clean duplicate records, calculate [metrics or views], compare [actuals or pipeline] with [target], and create a dashboard with charts and plain-English insights.
Include:
- assumptions and refresh instructions
- a review section for mismatched keys or records that did not join cleanly
- a short change log
Do not invent join keys or silently merge conflicting records. Preserve the original files and return the consolidated workbook for review.

## Establish the join and reporting rules

Consolidation is safest when the key, field definitions, target calculations, and duplicate rules are explicit. Give ChatGPT the source exports and ask it to surface records that do not join cleanly instead of guessing.

1. Attach the exports, mapping notes, targets, and reporting requirements.
2. Confirm the join key, duplicate rule, period definitions, and required output views.
3. Run the starter prompt and request an editable workbook with a review section.
4. Inspect formulas, joins, mismatches, assumptions, and refresh instructions.
5. Re-run the checks after any change to the source files or reporting rules.

Keep the original exports unchanged. A useful consolidated workbook makes it easy to tell which rows joined, which were excluded, and which assumptions a future refresh depends on.

## Validate the refresh path

After the first workbook is ready, ask ChatGPT to simulate the next refresh and report which steps are repeatable and which still need a human decision.

Test the refresh process for this consolidated workbook.
Report:
- inputs that can be replaced without changing the workflow
- formulas, joins, and charts that update correctly
- duplicate or mismatched keys
- assumptions that are not documented
- rows that need manual review
- steps that should become a reusable skill or automation
Do not overwrite the source exports or change business definitions.

## Related use cases

[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)[![](/codex/use-cases/business-impact-readout.webp)

### Measure business impact

Give ChatGPT an experiment or launch plan, success metrics, cohort data, dashboard exports...

Data  Knowledge Work](/codex/use-cases/business-impact-readout)[![](/codex/use-cases/scenario-tradeoff-model.webp)

### Model strategic scenarios and tradeoffs

Give ChatGPT a financial model, KPI dashboard, planning docs, market context, stakeholder...

Data  Knowledge Work](/codex/use-cases/scenario-tradeoff-model)
