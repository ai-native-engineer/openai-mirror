<!-- source: https://learn.chatgpt.com/use-cases/kpi-root-cause-analysis -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Analyze KPI root causes

Explain an unexpected metric movement with evidence and next actions.

Difficulty **Intermediate**

Time horizon **1h**

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and stakeholder threads, then ask it to separate confirmed drivers from hypotheses in a source-backed root-cause brief.

## Best for

* Product, growth, or operations teams investigating an unexpected KPI movement.
* Root-cause questions that require segment, cohort, channel, geography, or product cuts.
* Reviews where confirmed drivers must stay separate from plausible hypotheses.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/kpi-root-cause-analysis/?export=pdf)

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and stakeholder threads, then ask it to separate confirmed drivers from hypotheses in a source-backed root-cause brief.

Intermediate

1h

Related links

[OpenAI Academy: Data science teams](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex/)  [Query tabular data](/codex/use-cases/analyze-data-export)

## Best for

* Product, growth, or operations teams investigating an unexpected KPI movement.
* Root-cause questions that require segment, cohort, channel, geography, or product cuts.
* Reviews where confirmed drivers must stay separate from plausible hypotheses.

## Skills & Plugins

* Spreadsheets

  Inspect metric exports, calculate cuts, and create supporting charts.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read metric definitions, dashboards, launch context, and approved source files.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Check relevant stakeholder context and recent changes.
* Documents

  Package the analysis as a reviewable brief with sources and caveats.

| Skill | Why use it |
| --- | --- |
| Spreadsheets | Inspect metric exports, calculate cuts, and create supporting charts. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read metric definitions, dashboards, launch context, and approved source files. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Check relevant stakeholder context and recent changes. |
| Documents | Package the analysis as a reviewable brief with sources and caveats. |

## Starter prompt

Explain why [KPI] changed during [time window].
Use the KPI dashboard, metric definition, source exports, segment cuts, launch or campaign context, and stakeholder threads I provide. Break down the movement by relevant segment, cohort, channel, geography, and product surface.
Return a root-cause brief with:
- charts and material changes
- confirmed drivers
- hypotheses to investigate
- caveats and data-quality issues
- source links
- open questions
- recommended actions
Do not treat correlation as proof, and do not change the source data.

Explain why [KPI] changed during [time window].
Use the KPI dashboard, metric definition, source exports, segment cuts, launch or campaign context, and stakeholder threads I provide. Break down the movement by relevant segment, cohort, channel, geography, and product surface.
Return a root-cause brief with:
- charts and material changes
- confirmed drivers
- hypotheses to investigate
- caveats and data-quality issues
- source links
- open questions
- recommended actions
Do not treat correlation as proof, and do not change the source data.

## Define the metric before explaining movement

Root-cause work starts with a stable definition, comparison window, and source-of-truth data. Give ChatGPT the KPI definition, dashboard, exports, and context around launches or campaigns before asking it to explain the change.

1. State the KPI, comparison period, expected direction, and decision the analysis should support.
2. Attach the dashboard, metric definition, exports, segment cuts, and relevant context.
3. Ask ChatGPT to inspect data quality and propose the most useful breakdowns.
4. Run the starter prompt and review confirmed drivers separately from hypotheses.
5. Validate the recommended actions with the metric owner before changing a dashboard or process.

Use charts to make the movement inspectable, but do not treat a segment correlation as proof of cause. Keep source links, caveats, and open questions with the brief.

## Challenge the root cause

Ask ChatGPT to look for counterevidence and alternative explanations before the brief goes to leadership.

Challenge the root-cause brief.
For each confirmed driver or hypothesis, list:
- supporting source and calculation
- counterevidence or alternative explanation
- segment or cohort where it does not hold
- data-quality limitation
- next check that would increase confidence
Revise the recommendation only when the evidence supports it, and keep all changes visible.

## Related use cases

[![](/codex/use-cases/monthly-business-review-narrative.webp)

### Prepare a business review

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior...

Data  Integrations](/codex/use-cases/monthly-business-review-narrative)[![](/codex/use-cases/cfo-board-reporting-pack.webp)

### Prepare a leadership reporting pack

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs...

Data  Integrations](/codex/use-cases/cfo-board-reporting-pack)[![](/codex/use-cases/strategic-initiative-health-update.webp)

### Prepare an initiative health update

Give ChatGPT the tracker, initiative docs, KPI changes, prior briefs, owner notes, decision...

Data  Integrations](/codex/use-cases/strategic-initiative-health-update)
