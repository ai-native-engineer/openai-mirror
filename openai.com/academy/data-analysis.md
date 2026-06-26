<!-- source: https://openai.com/academy/data-analysis/ -->

April 10, 2026

OpenAI Academy

# Analyzing data with ChatGPT

Explore, analyze, and turn data into clear insights and actions in ChatGPT, Excel, or Google Sheets.

ChatGPT can help you move from raw data to useful insights with minimal setup. You can upload a CSV or Excel file directly in ChatGPT, paste in a table, or connect a data source (if supported in your workspace), then start asking questions in plain language. You can also use ChatGPT within Excel and Google Sheets, provided your workspace settings allow it.

Instead of building formulas, pivot tables, or dashboards for every question, you can quickly explore data, clean up tables, generate simple visualizations, and extract key takeaways in a format that's easy to share. It’s especially useful early in the process—when you’re still figuring out what’s in the data, identifying anomalies, and deciding where to dig deeper. It also helps translate findings into summaries others can review and act on.

## Data analysis directly in ChatGPT

1. Start with the decision you’re trying to support. A simple frame is: *“I’m trying to decide \_\_\_, based on \_\_\_.”* This tells ChatGPT what “done” looks like and keeps the analysis focused.
2. Provide your data along with any critical context—definitions, timeframe, and what key columns represent. You can provide data via **file upload**, or by using a **connected app**.
3. Ask for an approach, not just an answer. or example, request an exploratory data analysis (EDA) summary followed by hypotheses to test. This leads to more structured and reliable results than jumping straight to conclusions.
4. If visuals would help, request them explicitly—what to plot, how to segment, and any must-haves like axis labels or units.
5. Ask for outputs you can reuse such as a clean final table or a short executive summary that translates findings into action.

|  |  |  |
| --- | --- | --- |
| **Task** | **Context** | **Expected output** |
| Analyze this data and summarize key insights. | Use the sample dataset from our Shopify store (last 30 days). | Provide structured summary of key insights, including what stands out across channels and products, identification of underperforming areas (e.g., low-converting channels), and notable patterns. Includes 4–6 prioritized observations and 5 specific follow-up analyses or questions to investigate next. |
| Review and analyze our sales funnel data. | Use the data from [Campaign name] from [connected analytics app]. | Produce set of clearly separated sections: (1) key observed patterns in the funnel, (2) hypotheses explaining those patterns (e.g., onboarding as primary driver), and (3) recommended experiments or tests. Insights are ranked by business impact, with emphasis on conversion bottlenecks and leverage points. |
| Identify issues or inefficiencies in a process using data | Review the attached current process document, as well as the support team ticket data CSV. | Output a prioritized list of operational issues and bottlenecks (e.g., escalation delays, repeat ticket drivers), each supported by data signals. Includes clear reasoning for why each issue matters, plus recommended areas for immediate improvement or investigation, grouped into quick wins vs deeper fixes. |

## Data analysis in Excel or Google Sheets

If a lot of your work happens directly in a spreadsheet, [ChatGPT for Excel and Google Sheets⁠(opens in a new window)](https://chatgpt.com/apps/spreadsheets/) gives you a faster way to build, update, and understand that work without leaving the tools you already use. It lives in a sidebar inside your workbook, so you can ask for changes in plain language and review the result directly in the sheet. You can think of ChatGPT for Excel or Google Sheets as an in-product collaborator for spreadsheet mechanics and first-pass analysis.

Please note that in order to use ChatGPT within an Excel workbook or a Google Sheet, you must also enable the plugin on that surface. See installation instructions for [ChatGPT for Excel⁠(opens in a new window)](https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets#excel) and [ChatGPT for Google Sheets⁠(opens in a new window)](https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets#google-sheets).

The better your prompt describes what to preserve, the better the result. In practice, prompts work best when you specify the tabs to use, the tabs to avoid changing, the output you want, and whether ChatGPT should explain its plan before editing.

|  |  |
| --- | --- |
| **Goal** | **Prompt** |
| Clean up a workbook | “Clean up this workbook for executive review. Standardize labels and formatting, remove duplicates, fix broken formulas where possible, and summarize exactly what you changed.” |
| Understand model logic | “Explain how revenue flows through this model into margin and EBITDA. Point me to the key driver cells and call out any unusual assumptions.” |
| Update assumptions | “Update the assumptions on the Inputs tab only. Do not change formatting. Then list every downstream tab that changed and summarize the impact.” |
| Build a KPI pack | “Using the Revenue, Opex, and Headcount tabs, build a monthly KPI summary for leadership with revenue growth, gross margin, EBITDA margin, and department-level variance to plan.” |
| Prepare for review | “Before editing anything, outline your plan. Tell me which tabs you will modify, what formulas you expect to add, and any assumptions you need me to confirm.” |

## Tips for success

* Help ChatGPT help you by sharing what “good” looks like up front including what success metric you care about, the timeframe you’re looking at, and which groups or segments you want to compare.
* If the numbers really matter, you can also ask it to show how it got there including the assumptions it made, any formulas it used to calculate metrics, and quick checks for missing data or unusual spikes.
* It also helps to set a few simple ground rules so the analysis stays trustworthy. For example, you can tell it not to treat correlations as causes, to point out any limitations in the data, and to flag anything that looks off. And before you share results or make a decision, do a quick reality check—pick a couple key numbers and spot-verify them to make sure everything adds up.

**Learn more:**  
[OpenAI Help Center: Data analysis⁠(opens in a new window)](https://help.openai.com/articles/8437071-data-analysis-with-chatgpt)

[OpenAI Help Center: ChatGPT for Excel and Google Sheets⁠(opens in a new window)](https://help.openai.com/en/articles/20001063-chatgpt-for-excel)

[KPI dashboard summary

Analyze this spreadsheet and produce: (1) a KPI table (MoM + YoY), (2) 3 charts, and (3) a 10-bullet exec summary with ‘risks’ and ‘recommended actions’. Data: [upload].

(opens in a new window)](https://chatgpt.com/?prompt=Analyze+this+spreadsheet+and+produce%3A+%281%29+a+KPI+table+%28MoM+%2B+YoY%29%2C+%282%29+3+charts%2C+and+%283%29+a+10-bullet+exec+summary+with+%E2%80%98risks%E2%80%99+and+%E2%80%98recommended+actions%E2%80%99.+Data%3A+%5Bupload%5D.)

[Marketing: campaign performance review

You are a marketing analyst. Using these datasets [upload], identify the top 3 drivers of conversion changes, compute conversion rate by channel, and recommend 5 optimizations. Present results as a table + short narrative.

(opens in a new window)](https://chatgpt.com/?prompt=You+are+a+marketing+analyst.+Using+these+datasets+%5Bupload%5D%2C+identify+the+top+3+drivers+of+conversion+changes%2C+compute+conversion+rate+by+channel%2C+and+recommend+5+optimizations.+Present+results+as+a+table+%2B+short+narrative.)

[Finance: anomaly detection

Scan this export for anomalies (duplicates, unexpected spikes, vendor changes). Flag the rows to review, explain why each is suspicious, and suggest the next check I should run. Data: [upload].

(opens in a new window)](https://chatgpt.com/?prompt=Scan+this+export+for+anomalies+%28duplicates%2C+unexpected+spikes%2C+vendor+changes%29.+Flag+the+rows+to+review%2C+explain+why+each+is+suspicious%2C+and+suggest+the+next+check+I+should+run.+Data%3A+%5Bupload%5D.)

[Operations: forecasting

Using this historical volume data, build a simple forecast for the next 8 weeks. Show the model choice, assumptions, and a confidence range. Then summarize what staffing implication this has. Data: [upload].

(opens in a new window)](https://chatgpt.com/?prompt=Using+this+historical+volume+data%2C+build+a+simple+forecast+for+the+next+8+weeks.+Show+the+model+choice%2C+assumptions%2C+and+a+confidence+range.+Then+summarize+what+staffing+implication+this+has.+Data%3A+%5Bupload%5D.)

[Turn analysis into slides

Convert these findings into 5 slide titles + bullets (audience: exec staff). Include 1 chart per slide and a final ‘decision needed’ slide. Findings: [paste or link].

(opens in a new window)](https://chatgpt.com/?prompt=Convert+these+findings+into+5+slide+titles+%2B+bullets+%28audience%3A+exec+staff%29.+Include+1+chart+per+slide+and+a+final+%E2%80%98decision+needed%E2%80%99+slide.+Findings%3A+%5Bpaste+or+link%5D.)

[KPI dashboard summary

Analyze this spreadsheet and produce: (1) a KPI table (MoM + YoY), (2) 3 charts, and (3) a 10-bullet exec summary with ‘risks’ and ‘recommended actions’. Data: [upload].

(opens in a new window)](https://chatgpt.com/?prompt=Analyze+this+spreadsheet+and+produce%3A+%281%29+a+KPI+table+%28MoM+%2B+YoY%29%2C+%282%29+3+charts%2C+and+%283%29+a+10-bullet+exec+summary+with+%E2%80%98risks%E2%80%99+and+%E2%80%98recommended+actions%E2%80%99.+Data%3A+%5Bupload%5D.)

[Marketing: campaign performance review

You are a marketing analyst. Using these datasets [upload], identify the top 3 drivers of conversion changes, compute conversion rate by channel, and recommend 5 optimizations. Present results as a table + short narrative.

(opens in a new window)](https://chatgpt.com/?prompt=You+are+a+marketing+analyst.+Using+these+datasets+%5Bupload%5D%2C+identify+the+top+3+drivers+of+conversion+changes%2C+compute+conversion+rate+by+channel%2C+and+recommend+5+optimizations.+Present+results+as+a+table+%2B+short+narrative.)

[Finance: anomaly detection

Scan this export for anomalies (duplicates, unexpected spikes, vendor changes). Flag the rows to review, explain why each is suspicious, and suggest the next check I should run. Data: [upload].

(opens in a new window)](https://chatgpt.com/?prompt=Scan+this+export+for+anomalies+%28duplicates%2C+unexpected+spikes%2C+vendor+changes%29.+Flag+the+rows+to+review%2C+explain+why+each+is+suspicious%2C+and+suggest+the+next+check+I+should+run.+Data%3A+%5Bupload%5D.)

[Operations: forecasting

Using this historical volume data, build a simple forecast for the next 8 weeks. Show the model choice, assumptions, and a confidence range. Then summarize what staffing implication this has. Data: [upload].

(opens in a new window)](https://chatgpt.com/?prompt=Using+this+historical+volume+data%2C+build+a+simple+forecast+for+the+next+8+weeks.+Show+the+model+choice%2C+assumptions%2C+and+a+confidence+range.+Then+summarize+what+staffing+implication+this+has.+Data%3A+%5Bupload%5D.)

[Turn analysis into slides

Convert these findings into 5 slide titles + bullets (audience: exec staff). Include 1 chart per slide and a final ‘decision needed’ slide. Findings: [paste or link].

(opens in a new window)](https://chatgpt.com/?prompt=Convert+these+findings+into+5+slide+titles+%2B+bullets+%28audience%3A+exec+staff%29.+Include+1+chart+per+slide+and+a+final+%E2%80%98decision+needed%E2%80%99+slide.+Findings%3A+%5Bpaste+or+link%5D.)

---

## Continue learning with OpenAI Academy

Discover additional guides and resources to help you build practical AI skills.

[View all topics](/academy/)

## Keep reading

![Academy > Writing > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/7cfiyKI1Hz4PtBIZ5yV2Po/53d6f365498046c4596a2b5953039ccb/writing.png?w=3840&q=90&fm=webp)

[Writing with ChatGPT | OpenAI

OpenAI AcademyApr 10, 2026](/academy/writing/)

![Academy > Brainstorming > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/2QucAPrnCRSUoZDbQFyK4P/736e90884baf0e1ebe6cbcdb2ba8beaf/brainstorming.png?w=3840&q=90&fm=webp)

[Brainstorming with ChatGPT | OpenAI

OpenAI AcademyApr 10, 2026](/academy/brainstorming/)

![Academy > Research > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/24Zhocf65q1eBCqPljGtiH/b12cc424af8d1eacd56ee339e8214822/research.png?w=3840&q=90&fm=webp)

[ChatGPT for research | OpenAI

OpenAI AcademyApr 10, 2026](/academy/research/)
