<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/resources/turn-updates-into-review-ready-leadership-decks-2026-07-23 -->

* [Home](/en)
* [Events](/en/public/events)
* [Courses](https://academy.openai.com/pages/courses)
* [Content](/en/public/content)
* [Communities](/en/public/clubs)
* [What's new](https://academy.openai.com/public/collections/whats-new?linkMenu=What%27s%2520New)
* Stories
* [Work](https://academy.openai.com/pages/ai-at-work-bcx7td)
* Education
* [Small business](https://academy.openai.com/public/clubs/small-business-ipf4m)
* [Nonprofits](https://academy.openai.com/public/clubs/nonprofits-8kc1e/overview?linkMenu=Nonprofits)
* [Government](https://academy.openai.com/public/clubs/government-25yzc/overview?linkMenu=Government)
* [News organizations](https://academy.openai.com/public/clubs/news-organizations-b9osl/overview)
* Help

[Communities](/en/home/clubs)

/

[Champions](/en/public/clubs/champions-ecqup/overview)

/

[navigation.content](/en/public/clubs/champions-ecqup/content)

# Turn updates in review-ready leadership decks

![Turn updates in review-ready leadership decks](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/turn-updates-into-review-ready-leadership-decks-style-thumb-4677c5c8-09a6-4f31-888b-a2caca6ec619-1784825980110.jpeg?fit=scale-down&width=1200)

# Activators

# Champions

# Deployment & Adoption

## Update recurring presentations with source control, traceability, and human review.

July 23, 2026

![Turn updates in review-ready leadership decks](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/turn-updates-into-review-ready-leadership-decks-style-thumb-4677c5c8-09a6-4f31-888b-a2caca6ec619-1784825980110.jpeg?fit=scale-down&width=1200)

This workflow can help support teams that regularly update leadership or executive presentations from changing source materials.

This example uses finance materials from *Make Work Flow: Automating Finance presentations with Codex*, but the workflow pattern can be adapted to any teams with a similar workflow:

1. New data arrives, owner notes change, status updates shift, or source documents get refreshed.

2. Someone has to update a deck without losing track of what changed, where it came from, and who approved it.

﻿

Codex inspects approved source files, proposes a slide update plan, flags discrepancies, updates a presentation only after approval, and produces a reconciliation log so reviewers can trace the changes before the deck is shared.

# The AI Workflow

Business problem: Teams often update recurring executive presentations from several source files: dashboards, reports, spreadsheets, notes, prior decks, status trackers, customer updates, project plans, or forecast materials. Manual updates can leave stale metrics, mismatched commentary, hidden assumptions, hardcoded numbers, unclear sources, or edits that reviewers cannot easily trace.

Workflow description: A Codex or ChatGPT Work project uses durable instructions, approved source files, and staged prompts to refresh a deck in a controlled way. Codex first inspects the sources and produces a slide-by-slide update plan. An accountable reviewer confirms the plan and resolves discrepancies. After approval, Codex updates the deck, preserves the template and editable objects, and creates a reconciliation/change log that ties each material change back to a source file, sheet, page, section, range, or review note.

AI workflow build: Start with Codex or ChatGPT Work. Point it to approved files. Provide instructions (in this example, an .md file was used) that define source hierarchy, no-edit-before-plan behavior, output rules, review checks, and preservation of original files. Build the first version as a file-based, review-first workflow before considering connectors, scheduled refreshes, writeback, or automated publishing.

Suggested inputs: Prior executive deck; updated source files; baseline or prior-state files; dashboard exports; spreadsheet reports; owner notes; supporting commentary; status trackers; presentation template or brand guidance; source hierarchy; target slides; review check rules; approval owner; output folder. In the session example, these inputs were finance files: actual results, forecast comparison, finance owner notes, variance commentary, a baseline model, an updated model, and a prior executive readout.

Expected output: Updated editable presentation; slide-by-slide reconciliation/change log; source map for key metrics or messages; validation report; list of open assumptions or discrepancies; captions, speaker notes, or talking points if needed for the readout.

Human responsibilities: Confirm which files are approved for use, define the source hierarchy, review the slide-update plan, resolve conflicting sources, approve the build, validate key facts and numbers, review visual changes, decide whether the deck is ready to share, and approve circulation.

Probably stakeholders: Presentation owner; business or function owner; source-system or data owner; subject-matter experts; IT or workspace admin; security/privacy; legal/compliance if regulated, confidential, customer, employee, or material business data is involved; executive communications or brand/design owner if the deck is leadership- or external-facing.

Suggested pilot scope: One recurring internal deck, one update cycle, approved or synthetic source files, and a small number of affected slides. For example: refresh a monthly business review deck, customer account review, project status readout, pipeline review, product launch update, or finance readout using only approved source materials and requiring owner review before sharing.

Permissions/access considerations: Use only files approved for this workflow. Confirm who may access source data, notes, dashboards, customer or employee context, and presentation outputs. Keep the first build file-based if source-system connectors are not approved. Restrict the project folder, output folder, and any generated deck or change log according to your organization's policies.

Governance considerations: Treat executive presentations as decision-support artifacts. Keep source accuracy separate from readiness to share. Flag hardcoded values, source conflicts, stale assumptions, unsupported claims, sensitive data, and unresolved owner questions. Do not publish or circulate the updated deck until the accountable owner approves it.

﻿

# What to Customize Before You Paste

The copy/paste spec below is intentionally opinionated so a non-technical Activator can get started quickly. Change these items first:

﻿

|  |  |
| --- | --- |
| What to replace | Details |
| Team and readout context | * [TEAM NAME]  * [READOUT NAME]  * [LINE OF BUSINESS OR FUNCTION]  * [CADENCE] |
| Source files | Replace the sample file names with your team's approved files. |
| Source hierarchy | Define which file, system export, dashboard, owner-approved note, or report wins when sources conflict. |
| Review checks | Replace the sample checks with the source tie-outs, metric rules, narrative checks, approval criteria, and visual-review criteria your team uses. |
| Template guidance | Add your prior deck, brand guideline deck, design notes, approved screenshots, or presentation skill instructions. |
| Output location | Replace `[OUTPUT FOLDER]` with a restricted folder your reviewers can access. |
| Review owners | Replace `[REVIEWERS AND APPROVERS]` with the business, IT, security/privacy, legal/compliance, and brand/design reviewers needed for your workflow. |
| Data policy | Replace `[DATA ELIGIBILITY RULES]` with what your organization allows in Codex or ChatGPT Work. |
| Default setup | The spec defaults to a file-based Codex Project or ChatGPT Work project. If your team later wants connectors, scheduled runs, writeback, or automated publishing, add those only after the right owners approve them. |
| Additional placeholders to complete | [SUCCESS SIGNALS] |

﻿

# Copy/Paste Workflow Spec

Paste this into Codex in Plan Mode or into ChatGPT Work. Fill in the bracketed fields first if you can. If you are not sure about a field, leave it bracketed and ask Codex to help you define it.

```
Project name: Executive Deck Refresh Assistant

﻿

Context:

- Team or function: [TEAM NAME]

- Line of business or function: [LINE OF BUSINESS OR FUNCTION, for example finance, sales, customer success, operations, marketing, product, support, enablement, or strategy]

- Recurring presentation or readout: [READOUT NAME]

- Cadence: [CADENCE, for example monthly business review, quarterly review, weekly forecast review, launch review, account review, executive status update]

- Workflow scope: Update one approved deck from one approved source packet and produce a reviewer-ready reconciliation log.

- Approved source files: [SOURCE FILES]

- Source hierarchy: [SOURCE HIERARCHY, for example the latest approved dashboard export is the source of truth for metrics; owner notes provide qualitative context; the prior deck establishes the previously communicated view; unresolved conflicts must be flagged]

- Review checks: [REVIEW CHECKS, for example key metrics tie to source files, owner notes support the narrative, status changes are traceable, dates and units are consistent, no unsupported claims are added, repeated numbers match after rounding]

- Presentation/template rules: [TEMPLATE OR BRAND RULES, for example preserve prior deck structure, editable objects, source lines, units, slide numbering, and brand style]

- Output folder: [OUTPUT FOLDER]

- Reviewers and approvers: [REVIEWERS AND APPROVERS]

- Data eligibility rules: [DATA ELIGIBILITY RULES]

- Share-readiness rule: [SHARE-READINESS RULE, for example owner must approve before the deck is circulated]

﻿

Operating rules:

- Use a restricted project folder that contains only files approved for this workflow.

- Start with a file-based workflow. Do not connect to live systems, cloud drives, ERP, CRM, data warehouses, BI tools, project-management systems, support systems, or publishing tools unless I explicitly confirm that the required approvals are complete.

- Preserve originals. Do not overwrite the prior deck, source files, reports, notes, trackers, exports, or supporting materials.

- Do not edit any output files until you have inspected the sources and returned a slide-by-slide update plan for my approval.

- After approval, create new outputs in the output folder with distinct filenames.

- Preserve the deck's structure, theme, source lines, units, slide sequence, and editable objects unless I explicitly approve a design change.

- Keep source accuracy separate from readiness to share. A source-backed draft can still require owner confirmation before a deck is circulated.

- Use synthetic examples if I have not provided approved files.

﻿

Goal:

Help me refresh a recurring executive presentation from approved source files. Identify which slides need updates, show the source for each material change, flag discrepancies or open assumptions, update the presentation only after I approve the plan, and produce a reconciliation/change log that a reviewer can inspect before circulation.

﻿

Run this workflow:

﻿

1. Inspect the source packet.

- Read the prior deck, approved source files, owner notes, reports, trackers, exports, and template guidance.

- Identify the reporting period or update cycle.

- Apply the source hierarchy.

- Do not change any files yet.

﻿

2. Return a slide-by-slide update plan for approval.

For each slide that may need changes, include:

- Slide number and title

- What should change

- Prior value, wording, status, chart, or message

- Proposed updated value, wording, status, chart, or message

- Source file and exact location, such as sheet/range, page, section, record, or link

- Any discrepancy, missing evidence, or judgment call

- Whether the change is ready, needs reviewer input, or should be left unchanged

﻿

3. Wait for approval.

- Do not update the deck until I approve the plan or tell you what to revise.

- If sources conflict, ask which source should govern.

- If a change would introduce sensitive, confidential, regulated, customer, employee, or approval-required content, flag it before editing.

﻿

4. Update the deck after approval.

- Create a new editable presentation in the output folder.

- Preserve the original deck's structure, theme, source lines, units, slide sequence, and editable objects.

- Update only the slides and elements approved in the plan.

- Keep unsupported or unresolved items visible as open questions instead of silently resolving them.

﻿

5. Create the reconciliation/change log.

Include one row for each material deck change with:

- Slide number

- Slide title

- Metric, message, status, decision, chart, table, or slide element

- Prior value or prior wording

- Updated value or updated wording

- Delta or nature of change

- Source file or system export

- Sheet, range, page, section, record, or link

- Review note

- Status: Ready for review, Needs input, Left unchanged, or Blocked

- Reviewer or accountable owner

- Open question, if any

﻿

6. Create a short validation report.

Include:

- Files created

- Slides changed

- Slides left unchanged

- Source checks completed

- Repeated metrics, dates, statuses, or messages checked for consistency

- Visual checks completed, such as clipping, overlap, readability, broken charts, and missing source lines

- Items that still require reviewer approval

- Items that were blocked because the source, permission, or approval was missing

﻿

Governance and safe-use requirements:

- Use only approved files and approved source context.

- Do not use confidential business data, customer data, employee data, personal data, material nonpublic information, regulated data, or internal-only strategy unless I confirm it is approved for this workflow.

- Do not claim the deck is ready to share unless the accountable owner approves it.

- Do not silently resolve source conflicts. Flag them and ask for authority.

- Do not hide hardcoded values, source conflicts, unsupported claims, stale assumptions, or missing approvals.

- Do not enable connectors, live-system access, scheduled refreshes, writeback, external sharing, or automated publishing without explicit approval from the right stakeholders.

- Preserve a practical audit trail through source lines, reconciliation logs, reviewer notes, file versions, and validation reports.

﻿

How I want you to work:

- Start by inspecting the files and producing the slide-by-slide update plan.

- Ask clarifying questions only if they block a safe update. Otherwise make reasonable default choices and clearly label assumptions.

- Do not edit source files.

- Before updating the deck, show the slide-by-slide update plan and wait for my approval.

- After approval, create the updated deck, reconciliation/change log, and validation report.

- Keep language understandable for non-technical business reviewers.

- Clearly separate what is ready to use from what requires validation or approval
```

﻿

Like

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

## Popular

Resource

[The AI Champion role](/en/public/clubs/champions-ecqup/resources/the-ai-champion-role)

Resource

[OpenAI Academy courses: Champion deployment guide](/en/public/clubs/champions-ecqup/resources/openai-academy-courses-champion-deployment-guide-2026-06-11)

Resource

[Run an AI hackathon](/en/public/clubs/champions-ecqup/resources/hackathon-playbook-2025-09-15)

Dive in

## Related

Resource

[Turn scattered account updates into shared team context](/en/public/clubs/champions-ecqup/resources/turn-scattered-account-updates-into-shared-team-context-2026-06-12)

Jun 12th, 2026 • Views 220

[26:00](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automation-finance-presentation-updates-with-codex-2026-07-22)

Video

[[RECORDING] Make Work Flow: Automation Finance presentation updates with Codex](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automation-finance-presentation-updates-with-codex-2026-07-22)

Jul 22nd, 2026 • Views 87

[13:00](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Video

[Workflow clip: Automate CRM updates with Codex](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Jun 18th, 2026 • Views 225

[31:00](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

Video

[Recording: Make Work Flow: Automate CRM Updates with Codex](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

Jun 18th, 2026 • Views 404

Resource

[Turn scattered account updates into shared team context](/en/public/clubs/champions-ecqup/resources/turn-scattered-account-updates-into-shared-team-context-2026-06-12)

Jun 12th, 2026 • Views 220

[13:00](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Video

[Workflow clip: Automate CRM updates with Codex](/en/public/clubs/champions-ecqup/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Jun 18th, 2026 • Views 225

[31:00](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

Video

[Recording: Make Work Flow: Automate CRM Updates with Codex](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automate-crm-updates-with-codex-2026-06-18)

Jun 18th, 2026 • Views 404

[26:00](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automation-finance-presentation-updates-with-codex-2026-07-22)

Video

[[RECORDING] Make Work Flow: Automation Finance presentation updates with Codex](/en/public/clubs/champions-ecqup/videos/recording-make-work-flow-automation-finance-presentation-updates-with-codex-2026-07-22)

Jul 22nd, 2026 • Views 87
