<!-- source: https://learn.chatgpt.com/use-cases/dcf-model -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Model a DCF valuation

Turn financial inputs into an editable valuation workbook.

Difficulty **Intermediate**

Time horizon **30m**

Attach historical financials, valuation assumptions, and modeling notes, then ask ChatGPT for an editable DCF workbook you can inspect and revise in ChatGPT.

## Best for

* Analysts turning historical financials and assumptions into a DCF workbook.
* Finance teams that want to inspect and iterate on the workbook in ChatGPT.
* Teams preparing a valuation model from source files.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/dcf-model/?export=pdf)

Attach historical financials, valuation assumptions, and modeling notes, then ask ChatGPT for an editable DCF workbook you can inspect and revise in ChatGPT.

Intermediate

30m

Related links

[Agent skills](/codex/build-skills)  [File inputs](/api/docs/guides/file-inputs)

## Best for

* Analysts turning historical financials and assumptions into a DCF workbook.
* Finance teams that want to inspect and iterate on the workbook in ChatGPT.
* Teams preparing a valuation model from source files.

## Skills & Plugins

* Spreadsheets

  Create editable spreadsheet workbooks from attached inputs, formulas, and assumptions.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Create editable spreadsheet workbooks from attached inputs, formulas, and assumptions. |

## Starter prompt

Use $spreadsheets to build a DCF workbook for the company in the attached source files.
Include explicit operating drivers for revenue growth, margins, capex, and working capital. Calculate unlevered free cash flow, WACC, terminal value, and enterprise value. If capital structure and diluted share count are provided, bridge to implied equity value and implied equity value per share.
Use any assumptions included in the source files. If an assumption is missing, add a clearly labeled placeholder in the assumptions tab instead of hiding it in a formula. If full balance sheet or cash-flow statement inputs are missing, create the operating forecast needed for unlevered free cash flow and flag the missing statement inputs.
Generate the result as an editable .xlsx workbook.

Use $spreadsheets to build a DCF workbook for the company in the attached source files.
Include explicit operating drivers for revenue growth, margins, capex, and working capital. Calculate unlevered free cash flow, WACC, terminal value, and enterprise value. If capital structure and diluted share count are provided, bridge to implied equity value and implied equity value per share.
Use any assumptions included in the source files. If an assumption is missing, add a clearly labeled placeholder in the assumptions tab instead of hiding it in a formula. If full balance sheet or cash-flow statement inputs are missing, create the operating forecast needed for unlevered free cash flow and flag the missing statement inputs.
Generate the result as an editable .xlsx workbook.

## Introduction

ChatGPT can help you create a fully functional DCF workbook that you can inspect and revise.

It can use multiple files as context, including the historical financials, valuation assumptions, and any modeling notes.
You can provide these files directly, or use file references when the inputs live in Google Drive or another connected source. If so, provide the exact file references, as it will be more effective than asking ChatGPT to search through all of your files.

[ 
Your browser does not support the video tag.
](https://openaiassets.blob.core.windows.net/$web/codex/docs/developers-website/use-cases/create-a-dcf.mp4)

## Create the workbook

1. Attach the historical financials, valuation assumptions, and any modeling notes, or provide exact file references along with the source.
2. Run the starter prompt and ask for an editable `.xlsx` workbook.
3. Open the generated workbook in ChatGPT. Expand it into the full-screen view to inspect the model tabs, formulas, assumptions, and valuation summary.
4. Continue in the same chat to check formula links, change assumptions, add scenarios, or tighten the model.

When the workbook appears in the chat, open it and expand it full-screen. Review the source inputs, forecast drivers, valuation outputs, and sensitivity tables, then ask ChatGPT to revise the same workbook from there.

## Check the valuation

Before using the workbook, ask ChatGPT to review the model like a finance teammate would: source tie-outs, formulas, hardcoded assumptions, and valuation outputs.

Review the DCF workbook before I use it.
Check:
- historicals tied to the source files
- forecast drivers and visible assumptions
- formulas versus hardcoded values
- unlevered free cash flow calculation
- WACC, terminal value, enterprise value, and any equity-value bridge
- sensitivity table formulas
- missing capital structure, diluted share count, or assumptions that need human review
Fix safe formatting or formula issues, then list anything I should review manually.

## Revise one assumption

After reviewing the workbook, ask for targeted revisions in the same chat. Change one driver at a time so the impact is easy to inspect.

Update the DCF model so [revenue growth, EBITDA margin, WACC, terminal growth, or capex] uses [new assumption].
Keep the old assumption visible in a note, update dependent formulas, and tell me which tabs changed.

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
