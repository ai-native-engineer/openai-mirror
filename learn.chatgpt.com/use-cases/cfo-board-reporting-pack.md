<!-- source: https://learn.chatgpt.com/use-cases/cfo-board-reporting-pack -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Prepare a leadership reporting pack

Turn company progress, financial metrics, and owner updates into a source-backed reporting pack.

Difficulty **Intermediate**

Time horizon **1h**

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs, leadership notes, and owner commentary, then ask it to build an editable company or board update with a clear through-line, validated proof points, risks, milestones, and review flags.

## Best for

* Recurring company, leadership, CFO, or board updates built from a stable template.
* Reporting cycles that combine initiative progress, metrics, charts, narrative, and owner inputs.
* Teams that need a clear record of changed figures, risks, next milestones, and unresolved assumptions.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/cfo-board-reporting-pack/?export=pdf)

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs, leadership notes, and owner commentary, then ask it to build an editable company or board update with a clear through-line, validated proof points, risks, milestones, and review flags.

Intermediate

1h

Related links

[OpenAI Academy: Business operations teams](https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex/)  [Plugins](/codex/plugins)  [Agent skills](/codex/build-skills)

## Best for

* Recurring company, leadership, CFO, or board updates built from a stable template.
* Reporting cycles that combine initiative progress, metrics, charts, narrative, and owner inputs.
* Teams that need a clear record of changed figures, risks, next milestones, and unresolved assumptions.

## Skills & Plugins

* Slides

  Update an editable PowerPoint deck, preserve its visual system, and render slides for layout review.
* Spreadsheets

  Validate updated metrics and deltas against the latest forecast, KPI, and cash source files.
* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read approved prior packs, progress trackers, forecast files, dashboards, leadership notes, and owner inputs from exact Drive locations.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Read approved owner updates and open-question threads that should inform the pack.

| Skill | Why use it |
| --- | --- |
| Slides | Update an editable PowerPoint deck, preserve its visual system, and render slides for layout review. |
| Spreadsheets | Validate updated metrics and deltas against the latest forecast, KPI, and cash source files. |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read approved prior packs, progress trackers, forecast files, dashboards, leadership notes, and owner inputs from exact Drive locations. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Read approved owner updates and open-question threads that should inform the pack. |

## Starter prompt

Use $slides and $spreadsheets to prepare the [company, leadership, CFO, or board] reporting pack for [period or topic].
Use the prior pack or progress outline, initiative trackers, metric snapshots, latest forecast model, KPI dashboard, cash view, leadership notes, owner commentary, and open questions I provide. If any sources are in connected plugins, use only the exact @google-drive files or @slack threads I name.
Identify the through-line across workstreams, then update the narrative, proof points, key metrics, deltas, charts, risks, and next milestones while preserving the existing deck's visual system. Return an editable .pptx file and a short pack summary covering what changed, which figures do not tie to a source, what still needs owner input, which assumptions remain open, and which slides need leadership review. Render the deck and fix clipping, overflow, or layout issues before delivery. Do not share it.

Use $slides and $spreadsheets to prepare the [company, leadership, CFO, or board] reporting pack for [period or topic].
Use the prior pack or progress outline, initiative trackers, metric snapshots, latest forecast model, KPI dashboard, cash view, leadership notes, owner commentary, and open questions I provide. If any sources are in connected plugins, use only the exact @google-drive files or @slack threads I name.
Identify the through-line across workstreams, then update the narrative, proof points, key metrics, deltas, charts, risks, and next milestones while preserving the existing deck's visual system. Return an editable .pptx file and a short pack summary covering what changed, which figures do not tie to a source, what still needs owner input, which assumptions remain open, and which slides need leadership review. Render the deck and fix clipping, overflow, or layout issues before delivery. Do not share it.

## Build the narrative from the reporting record

Company and board reporting needs a narrative that connects initiative progress, financial and operating metrics, risks, and next steps. ChatGPT can use the prior pack for structure and approved source files for facts while preserving the deck’s visual system and keeping unresolved assumptions visible.

## Refresh from approved sources

Provide the prior pack or progress outline, initiative trackers, latest forecast, KPI dashboard, cash view, leadership notes, and owner commentary. Tell ChatGPT which slides are in scope, which sources are authoritative, and which parts of the template must remain unchanged.

1. Attach the prior pack and the latest approved source files.
2. Identify the reporting period, audience, in-scope workstreams, and review owners.
3. Ask ChatGPT to find the through-line across progress, proof points, risks, and next milestones.
4. Run the starter prompt and request an editable `.pptx` file.
5. Review the source tie-out for every changed claim, metric, and chart.
6. Inspect the rendered slides for clipping, overflow, and layout drift, then resolve owner inputs in the same chat.

## Review what changed

The reporting pack should make it easy to distinguish updated facts from open questions. Ask ChatGPT to keep a change summary and owner checklist alongside the deck so reviewers can focus on material differences without rewriting the whole update.

Audit the refreshed reporting pack against the prior pack and source files.
List:
- slides with changed metrics, charts, or commentary
- claims, proof points, risks, and milestone dates that need verification
- figures that tie to the forecast, KPI dashboard, or cash view
- figures that do not have a clear source
- assumptions and owner inputs that remain open
- slides that need leadership review
- clipping, overflow, or inconsistent formatting found in the rendered deck
Fix safe layout issues, but do not invent or silently replace missing claims or metrics. Keep unresolved items grouped by owner.

## Related use cases

[![](/codex/use-cases/monthly-business-review-narrative.webp)

### Prepare a business review

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior...

Data  Integrations](/codex/use-cases/monthly-business-review-narrative)[![](/codex/use-cases/research-to-decision-memo.webp)

### Turn research into a decision memo

Give ChatGPT research, planning documents, models, dashboards, stakeholder context, and...

Data  Integrations](/codex/use-cases/research-to-decision-memo)[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)
