<!-- source: https://learn.chatgpt.com/use-cases/analyze-data-export -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Query tabular data

Ask a question about a CSV, spreadsheet, export, or data folder.

Difficulty **Easy**

Time horizon **30m**

Use ChatGPT with a CSV, spreadsheet, dashboard export, Google Sheet, or local data file to answer a question, create a browser visualization, and save the result.

## Best for

* Questions that can be answered through a quick calculation, chart, table, or short summary.
* Roles that need to analyze data and create visualizations.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/analyze-data-export/?export=pdf)

Use ChatGPT with a CSV, spreadsheet, dashboard export, Google Sheet, or local data file to answer a question, create a browser visualization, and save the result.

Easy

30m

Related links

[File inputs](/api/docs/guides/file-inputs)  [Agent skills](/codex/build-skills)

## Best for

* Questions that can be answered through a quick calculation, chart, table, or short summary.
* Roles that need to analyze data and create visualizations.

## Skills & Plugins

* Spreadsheet

  Inspect tabular data, run calculations, and create charts or tables.
* [Google Sheets](/codex/plugins)

  Analyze approved Google Sheets when the data lives in a shared spreadsheet.

| Skill | Why use it |
| --- | --- |
| Spreadsheet | Inspect tabular data, run calculations, and create charts or tables. |
| [Google Sheets](/codex/plugins) | Analyze approved Google Sheets when the data lives in a shared spreadsheet. |

## Starter prompt

Analyze @sales-export.csv
Question: Which customer segment changed the most last quarter?
Please:
- inspect the columns before analyzing
- answer the question from the data
- create a simple browser visualization as an HTML file
- start a local preview so I can open it in the built-in browser

Analyze @sales-export.csv
Question: Which customer segment changed the most last quarter?
Please:
- inspect the columns before analyzing
- answer the question from the data
- create a simple browser visualization as an HTML file
- start a local preview so I can open it in the built-in browser

## Analyze the data

Use ChatGPT when you have a CSV, spreadsheet, dashboard export, Google Sheet, or local data file and want to answer a question from it. Start with the file and the question. ChatGPT can inspect the columns, run the analysis, and create a browser visualization you can open in the ChatGPT desktop app.

[ 
Your browser does not support the video tag.
](https://cdn.openai.com/codex/docs/developers-website/use-cases/data-analysis-fraud-spike.mp4)

1. Attach the file or mention the connected data source.
2. Ask the question you want answered.
3. Have ChatGPT inspect the columns, run the calculation, and create an HTML visualization.
4. Open the local preview in the built-in browser, then continue in the same chat to adjust the chart or slice the data another way.

Use `@` to attach the CSV or mention the Google Sheet. If the data came from a dashboard, export the rows first so ChatGPT can inspect the raw columns.

## Follow-up analysis

After ChatGPT gives you the first answer, ask for the next comparison you would normally check.

Use the same data and compare the result by [region, cohort, product, week, model version, or account type].
Update the browser visualization for that comparison.

You can keep going in the same chat: clean a column, exclude a test segment, compare two time windows, make the chart easier to read, or turn the result into a short note for a meeting.

## Related use cases

[![](/codex/use-cases/feedback-synthesis.webp)

### Turn feedback into actions

Connect ChatGPT to multiple data sources such as Slack, GitHub, Linear, or Google Drive to...

Data  Integrations](/codex/use-cases/feedback-synthesis)[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)[![](/codex/use-cases/clean-messy-data.webp)

### Clean and prepare messy data

Drag in or mention a messy CSV or spreadsheet, describe the problems you see, and ask...

Data  Knowledge Work](/codex/use-cases/clean-messy-data)
