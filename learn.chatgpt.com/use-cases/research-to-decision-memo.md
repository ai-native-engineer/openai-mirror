<!-- source: https://learn.chatgpt.com/use-cases/research-to-decision-memo -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Turn research into a decision memo

Combine evidence, tradeoffs, and open questions into one recommendation.

Difficulty **Intermediate**

Time horizon **1h**

Give ChatGPT research, planning documents, models, dashboards, stakeholder context, and unresolved questions, then ask it to separate evidence from interpretation and draft a sourced decision memo that is ready for leadership review.

## Best for

* Decisions that combine internal evidence, external research, budget, and tradeoffs.
* Planning or investment questions where the recommendation needs an explicit evidence trail and decision log.
* Teams that want alternatives, owner confirmations, and unresolved risks visible before a leadership review.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/research-to-decision-memo/?export=pdf)

Give ChatGPT research, planning documents, models, dashboards, stakeholder context, and unresolved questions, then ask it to separate evidence from interpretation and draft a sourced decision memo that is ready for leadership review.

Intermediate

1h

Related links

[OpenAI Academy: Everyday work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)  [OpenAI Academy: Business operations teams](https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex/)  [Plugins](/codex/plugins)

## Best for

* Decisions that combine internal evidence, external research, budget, and tradeoffs.
* Planning or investment questions where the recommendation needs an explicit evidence trail and decision log.
* Teams that want alternatives, owner confirmations, and unresolved risks visible before a leadership review.

## Skills & Plugins

* [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

  Read approved recaps, planning docs, models, and source material.
* [Notion](https://github.com/openai/plugins/tree/main/plugins/notion)

  Check decision history, research notes, and project context when they live in Notion.
* [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

  Review stakeholder debate, comments, and unresolved questions from approved channels or threads.
* Spreadsheets

  Validate financial, KPI, or scenario inputs behind the recommendation.
* Documents

  Produce a concise, editable decision memo and review-ready pre-read with source notes.

| Skill | Why use it |
| --- | --- |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | Read approved recaps, planning docs, models, and source material. |
| [Notion](https://github.com/openai/plugins/tree/main/plugins/notion) | Check decision history, research notes, and project context when they live in Notion. |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | Review stakeholder debate, comments, and unresolved questions from approved channels or threads. |
| Spreadsheets | Validate financial, KPI, or scenario inputs behind the recommendation. |
| Documents | Produce a concise, editable decision memo and review-ready pre-read with source notes. |

## Starter prompt

I'm deciding whether [team or company] should [decision].
Use these sources:
- prior recaps and research: [files or links]
- planning docs, models, and dashboards: [files or links]
- audience, account, or market context: [files or links]
- stakeholder comments and meeting notes: [files, channels, or thread links]
- budget guardrails: [files or links]
- decision criteria: [criteria]
If I ask for web research, keep external findings separate from internal evidence. Write a concise decision memo with a recommendation, supporting evidence, alternatives and tradeoffs, costs, risks, a decision log, open questions, owner confirmations, and source links.
If the audience needs a pre-read, organize the memo and supporting analysis into a review-ready packet while keeping the memo as the source of truth. Flag assumptions and do not make the decision or share the output.

I'm deciding whether [team or company] should [decision].
Use these sources:
- prior recaps and research: [files or links]
- planning docs, models, and dashboards: [files or links]
- audience, account, or market context: [files or links]
- stakeholder comments and meeting notes: [files, channels, or thread links]
- budget guardrails: [files or links]
- decision criteria: [criteria]
If I ask for web research, keep external findings separate from internal evidence. Write a concise decision memo with a recommendation, supporting evidence, alternatives and tradeoffs, costs, risks, a decision log, open questions, owner confirmations, and source links.
If the audience needs a pre-read, organize the memo and supporting analysis into a review-ready packet while keeping the memo as the source of truth. Flag assumptions and do not make the decision or share the output.

## Define the decision before gathering evidence

Decision work becomes clearer when ChatGPT knows the choice, constraints, audience, decision date, and approval boundary. Attach internal context first, then identify any outside research that needs to be completed separately.

1. State the decision, decision maker, timing, and criteria.
2. Attach recaps, planning docs, models, dashboards, budget guardrails, stakeholder comments, and meeting notes.
3. Ask ChatGPT to inventory internal evidence, source gaps, unresolved debate, and requested web research.
4. Run the starter prompt and review the recommendation, alternatives, tradeoffs, risks, decision log, and missing information.
5. Verify each material claim and owner confirmation before the memo enters leadership review.

Keep internal evidence, external research, and interpretation in separate sections. If a cost, date, or market fact cannot be confirmed, leave it as an explicit open item. When the audience needs a longer pre-read, keep the decision memo as the source of truth and place supporting analysis in an appendix instead of hiding uncertainty in polished slides.

## Pressure-test the recommendation and review packet

Use a follow-up pass to challenge the preferred option, expose which assumptions would change the recommendation, and anticipate the questions decision makers will ask.

Pressure-test the decision memo.
Show:
- the assumptions that drive the recommendation
- the strongest case for each alternative
- evidence that is internal versus external
- costs, risks, and missing information that could change the decision
- claims, numbers, and owner confirmations that still need review
- questions a skeptical decision maker is likely to ask
- the smallest additional analysis needed to reduce uncertainty
Keep the original memo unchanged, cite the relevant source for each finding, and mark every proposed revision for review.

## Related use cases

[![](/codex/use-cases/monthly-business-review-narrative.webp)

### Prepare a business review

Give ChatGPT KPI dashboards, close workbooks, metric definitions, forecast updates, prior...

Data  Integrations](/codex/use-cases/monthly-business-review-narrative)[![](/codex/use-cases/cfo-board-reporting-pack.webp)

### Prepare a leadership reporting pack

Give ChatGPT the prior pack, progress outline, initiative trackers, KPI and forecast inputs...

Data  Integrations](/codex/use-cases/cfo-board-reporting-pack)[![](/codex/use-cases/kpi-root-cause-analysis.webp)

### Analyze KPI root causes

Give ChatGPT KPI dashboards, metric definitions, exports, segment cuts, launch context, and...

Data  Integrations](/codex/use-cases/kpi-root-cause-analysis)
