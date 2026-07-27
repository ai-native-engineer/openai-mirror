<!-- source: https://learn.chatgpt.com/use-cases/budget-vs-actuals-review -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Review budget vs. actuals

Turn plan, actuals, and close notes into a variance workbook.

Difficulty **Easy**

Time horizon **30m**

Give ChatGPT a budget, actuals export, and close notes, then ask it to map actuals to plan, calculate variances, flag reconciliation issues, and separate supported explanations from open finance questions.

## Best for

* Month-end reviews that compare budget plans with actual spend exports.
* Finance teams preparing leadership commentary from GL, spend, or department actuals.
* Workbooks where category mapping, tie-outs, and unsupported explanations need review.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/budget-vs-actuals-review/?export=pdf)

Give ChatGPT a budget, actuals export, and close notes, then ask it to map actuals to plan, calculate variances, flag reconciliation issues, and separate supported explanations from open finance questions.

Easy

30m

Related links

[Agent skills](/codex/build-skills)

## Best for

* Month-end reviews that compare budget plans with actual spend exports.
* Finance teams preparing leadership commentary from GL, spend, or department actuals.
* Workbooks where category mapping, tie-outs, and unsupported explanations need review.

## Skills & Plugins

* Spreadsheets

  Inspect spreadsheet inputs, clean and map rows, create variance tables, and produce reviewable workbook outputs.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Inspect spreadsheet inputs, clean and map rows, create variance tables, and produce reviewable workbook outputs. |

## Starter prompt

Use $spreadsheets to update the budget vs. actuals review from the attached files.
Compare actuals to plan, map actuals to the right budget categories, summarize the major variances, and prepare a clean review view as an editable .xlsx workbook.
Preserve the raw inputs, use formulas for dollar and percentage variance calculations, and flag categories that do not map cleanly instead of forcing a match. Use account type to determine favorable or unfavorable variance: revenue above plan is favorable, while expense above plan is unfavorable.

Use $spreadsheets to update the budget vs. actuals review from the attached files.
Compare actuals to plan, map actuals to the right budget categories, summarize the major variances, and prepare a clean review view as an editable .xlsx workbook.
Preserve the raw inputs, use formulas for dollar and percentage variance calculations, and flag categories that do not map cleanly instead of forcing a match. Use account type to determine favorable or unfavorable variance: revenue above plan is favorable, while expense above plan is unfavorable.

## Introduction

If you’re working on a budget and want to review the variances or inspect any issues, ChatGPT can help you create a fully functional review workbook you can work with.

Attach the budget plan, actuals export, and close notes, then ask ChatGPT for an editable review workbook. ChatGPT can preserve the raw inputs, map actuals to plan, calculate variances, and create a summary view you can inspect in the chat.

[ 
Your browser does not support the video tag.
](https://openaiassets.blob.core.windows.net/$web/codex/docs/developers-website/use-cases/budgets-vs-actuals.mp4)

## Create the review workbook

1. Attach the budget plan, actuals export, and close notes, or provide exact file references along with the source.
2. Run the starter prompt and ask for an editable `.xlsx` workbook.
3. Open the workbook in ChatGPT. Expand it into the full-screen view to inspect the raw inputs, mappings, variance formulas, and summary tab.
4. Continue in the same chat to fix category mappings, add department cuts, or draft the finance summary.

If the source files are in a connected plugin, mention the exact files or folder. Avoid asking ChatGPT to search a broad Drive or workspace when the review should use specific finance sources. When the workbook appears in the chat, open it and expand it full-screen to review the raw inputs, mappings, variance formulas, and summary tab before asking for revisions.

## Check the variances

Before sharing the workbook, ask ChatGPT to audit the categories, formulas, and variance explanations.

Check the budget vs. actuals review before I share it.
List:
- the most material unfavorable variances by dollar impact
- the most material favorable variances by dollar impact
- categories that may be mapped incorrectly
- accounts where the favorable or unfavorable sign convention is unclear
- explanations supported by the close notes
- explanations that need human review
- formula or tie-out issues in the workbook
Fix safe formatting or formula issues, then list anything finance should resolve before leadership review.

## Related use cases

[![](/codex/use-cases/variance-driver-bridge.webp)

### Build a variance driver bridge

Give ChatGPT actuals, budget, forecasts, KPI data, thresholds, and owner notes, then ask it...

Data  Knowledge Work](/codex/use-cases/variance-driver-bridge)[![](/codex/use-cases/finance-model-cleanup.webp)

### Clean and review a financial model

Give ChatGPT a financial model and its supporting sources, then ask it to make safe cleanup...

Data  Knowledge Work](/codex/use-cases/finance-model-cleanup)[![](/codex/use-cases/cash-flow-forecast.webp)

### Forecast cash flow

Give ChatGPT cash-flow inputs and model constraints, then ask it to create an editable...

Data  Knowledge Work](/codex/use-cases/cash-flow-forecast)
