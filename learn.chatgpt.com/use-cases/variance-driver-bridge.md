<!-- source: https://learn.chatgpt.com/use-cases/variance-driver-bridge -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Build a variance driver bridge

Explain movements across actuals, budget, and forecast with source-backed drivers.

Difficulty **Intermediate**

Time horizon **30m**

Give ChatGPT actuals, budget, forecasts, KPI data, thresholds, and owner notes, then ask it to rank the drivers behind material movements and produce an editable bridge with reconciliations, questions, and source citations.

## Best for

* Forecast-to-actual, budget-to-actual, and forecast-to-forecast reviews.
* Analyses spanning revenue, margin, operating expense, cash, or balance-sheet drivers.
* Teams that need ranked drivers, reconciliations, and owner questions in one deliverable.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/variance-driver-bridge/?export=pdf)

Give ChatGPT actuals, budget, forecasts, KPI data, thresholds, and owner notes, then ask it to rank the drivers behind material movements and produce an editable bridge with reconciliations, questions, and source citations.

Intermediate

30m

Related links

[Agent skills](/codex/build-skills)

## Best for

* Forecast-to-actual, budget-to-actual, and forecast-to-forecast reviews.
* Analyses spanning revenue, margin, operating expense, cash, or balance-sheet drivers.
* Teams that need ranked drivers, reconciliations, and owner questions in one deliverable.

## Skills & Plugins

* Spreadsheets

  Reconcile finance inputs, calculate material movements, and create an editable driver bridge with formulas and checks.
* Documents

  Package source-backed driver commentary and owner questions into a reviewable memo when needed.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Reconcile finance inputs, calculate material movements, and create an editable driver bridge with formulas and checks. |
| Documents | Package source-backed driver commentary and owner questions into a reviewable memo when needed. |

## Starter prompt

Use $spreadsheets to explain the [period] movement between [actuals, budget, forecast, or prior forecast].
Use the attached close workbook, budget file, prior forecast, KPI dashboard, operating-expense tracker, cash view, and finance-owner notes. Build an editable variance bridge across the relevant revenue, margin, operating-expense, EBITDA, free-cash-flow, and balance-sheet lines.
Rank material drivers by impact, reconcile source breaks, draft owner questions, and cite the workbook tab, dashboard, tracker, or note behind each driver. Flag movements that are below [threshold] separately. Do not write a definitive explanation when the sources only support a hypothesis.

Use $spreadsheets to explain the [period] movement between [actuals, budget, forecast, or prior forecast].
Use the attached close workbook, budget file, prior forecast, KPI dashboard, operating-expense tracker, cash view, and finance-owner notes. Build an editable variance bridge across the relevant revenue, margin, operating-expense, EBITDA, free-cash-flow, and balance-sheet lines.
Rank material drivers by impact, reconcile source breaks, draft owner questions, and cite the workbook tab, dashboard, tracker, or note behind each driver. Flag movements that are below [threshold] separately. Do not write a definitive explanation when the sources only support a hypothesis.

## Introduction

A variance bridge connects a reported movement to the operational drivers behind it. ChatGPT can reconcile actuals, budget, forecasts, KPI data, and owner notes, then rank the drivers and separate supported explanations from questions that still need an owner.

## Choose the comparison

Define the periods and versions you want to compare, such as forecast to actual, budget to actual, or current forecast to prior forecast. Provide the materiality threshold, sign conventions, and the finance lines that matter for this review.

1. Attach the actuals, budget, forecasts, KPI data, and owner notes.
2. Define the comparison, materiality threshold, and required finance lines.
3. Run the starter prompt and ask for an editable bridge workbook.
4. Review source breaks, sign conventions, and driver rankings.
5. Continue in the same chat to resolve owner questions and prepare commentary.

## Challenge the explanations

Driver commentary should follow the evidence. Ask ChatGPT to label hypotheses clearly when the source files show a movement but do not establish its cause.

Challenge the explanations in the variance bridge.
For each material driver, show:
- the calculated impact and sign
- the source file, tab, dashboard, tracker, or note
- whether the explanation is supported, inferred, or still open
- any reconciliation break
- the owner question needed to close the gap
Re-rank the bridge by absolute impact and keep unsupported explanations out of the executive summary.

## Related use cases

[![](/codex/use-cases/finance-model-cleanup.webp)

### Clean and review a financial model

Give ChatGPT a financial model and its supporting sources, then ask it to make safe cleanup...

Data  Knowledge Work](/codex/use-cases/finance-model-cleanup)[![](/codex/use-cases/cash-flow-forecast.webp)

### Forecast cash flow

Give ChatGPT cash-flow inputs and model constraints, then ask it to create an editable...

Data  Knowledge Work](/codex/use-cases/cash-flow-forecast)[![](/codex/use-cases/dcf-model.webp)

### Model a DCF valuation

Attach historical financials, valuation assumptions, and modeling notes, then ask ChatGPT...

Data  Knowledge Work](/codex/use-cases/dcf-model)
