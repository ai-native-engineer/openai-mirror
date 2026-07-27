<!-- source: https://learn.chatgpt.com/use-cases/analytics-request-agent -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Scope an analytics request

Turn an ambiguous stakeholder ask into a validated analysis plan.

Difficulty **Intermediate**

Time horizon **30m**

Give ChatGPT the stakeholder request, business context, metric glossary, source exports, dashboard links, and request threads, then ask it to scope the question, identify missing inputs, run a first pass, and prepare a reviewable answer.

## Best for

* Analytics requests that arrive as broad questions without clear metric definitions or scope.
* Analysts who need to identify source gaps before committing to an answer.
* Stakeholder-ready analysis that should include charts, validation notes, and open questions.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/analytics-request-agent/?export=pdf)

Give ChatGPT the stakeholder request, business context, metric glossary, source exports, dashboard links, and request threads, then ask it to scope the question, identify missing inputs, run a first pass, and prepare a reviewable answer.

Intermediate

30m

Related links

[OpenAI Academy: Data science teams](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex/)  [Query tabular data](/codex/use-cases/analyze-data-export)

## Best for

* Analytics requests that arrive as broad questions without clear metric definitions or scope.
* Analysts who need to identify source gaps before committing to an answer.
* Stakeholder-ready analysis that should include charts, validation notes, and open questions.

## Skills & Plugins

* Spreadsheets

  Inspect source exports, test joins, and run the first-pass calculations.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Find metric glossaries, dashboards, source files, and prior analysis.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Read the original request and surrounding stakeholder context.
* Documents

  Turn the scoped analysis into a stakeholder-ready answer with review notes.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Inspect source exports, test joins, and run the first-pass calculations. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Find metric glossaries, dashboards, source files, and prior analysis. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Read the original request and surrounding stakeholder context. |
| Documents | Turn the scoped analysis into a stakeholder-ready answer with review notes. |

## Starter prompt

Turn this request into a scoped analysis: [paste request or link to source context].
Identify the business question, required metric definitions, source exports, relevant dashboards, and recent product or business context. Draft an analysis plan, run a first-pass analysis using the available data, validate the outputs, and prepare a stakeholder-ready answer with charts, caveats, source links, and open questions for analyst review.
Do not assume metric definitions, join logic, or missing values. List every input or decision you need confirmed before the analysis is final.

Turn this request into a scoped analysis: [paste request or link to source context].
Identify the business question, required metric definitions, source exports, relevant dashboards, and recent product or business context. Draft an analysis plan, run a first-pass analysis using the available data, validate the outputs, and prepare a stakeholder-ready answer with charts, caveats, source links, and open questions for analyst review.
Do not assume metric definitions, join logic, or missing values. List every input or decision you need confirmed before the analysis is final.

## Turn the ask into an analysis contract

Stakeholder requests often mix the business question, a preferred chart, and an assumed metric definition. Give ChatGPT the original request and surrounding context, then ask it to identify the question, definitions, sources, joins, and decisions before it analyzes.

1. Attach the request thread, metric glossary, dashboards, exports, and relevant context.
2. Ask ChatGPT to list what is known, ambiguous, missing, or out of scope.
3. Confirm the metric definitions, join logic, time window, and intended audience.
4. Run the starter prompt for a first-pass analysis and stakeholder-ready answer.
5. Have an analyst review the calculations, charts, caveats, and open questions.

Do not let a confident answer hide an undefined metric or unverified join. The analysis plan is part of the deliverable because it makes the next iteration faster to review.

## Close the loop with the requester

After the analysis is reviewed, ask ChatGPT to turn the open questions into a short confirmation note without sending it.

Turn the open questions into a requester review note.
Include:
- the business question I answered
- definitions and filters used
- source files and joins
- the main result and caveats
- questions that need confirmation
- the next analysis I can run after confirmation
Keep unsupported claims out and return a draft only.

## Related use cases

[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)[![](/codex/use-cases/monthly-business-review-narrative.webp)

### Prepare a business review

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior...

Data  Integrations](/codex/use-cases/monthly-business-review-narrative)[![](/codex/use-cases/cfo-board-reporting-pack.webp)

### Prepare a leadership reporting pack

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs...

Data  Integrations](/codex/use-cases/cfo-board-reporting-pack)
