<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/how-business-operations-teams-use-codex-webinar-resource-guide-2026-06-17 -->

[Work Users](/en/public/clubs/work-users-ynjqu/overview)

[navigation.content](/en/public/clubs/work-users-ynjqu/content)

Webinar

June 18, 2026

# How business operations teams use Codex: Webinar resource guide

![How business operations teams use Codex: Webinar resource guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-12--8bb4144f-6b68-495b-aa18-2f27525b4162-1781756968064.jpeg?fit=scale-down&width=1200)

# Codex for Work

## Follow along with our webinar: How business operations teams use Codex

![How business operations teams use Codex: Webinar resource guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-12--8bb4144f-6b68-495b-aa18-2f27525b4162-1781756968064.jpeg?fit=scale-down&width=1200)

## Follow along with the webinar: How business operations teams use Codex

If you work in business operations, you probably know this moment: a leadership meeting is coming up, and the raw material is everywhere. There is a dashboard, a tracker, a planning doc, and a Slack thread that has somehow become part of the source material.

That is the work this webinar focuses on. You will see how Codex can help business operations teams pull together context, check it against data, and create the first version of the deliverable the team needs next: a cleaned initiative summary, a weekly bookings dashboard, a team update, a leadership decision deck, and a repeatable workflow.

Use the files linked below to follow along with the demos. These are sample materials with dummy business data, fictional operating context, and practice assets.

## Download the demo files

Download these files to follow along: [Download here](https://docsend.com/view/s/nqprjf7xxisxrmha/f/2v2mm9bg5scqri27)﻿

## Resources to bookmark:

* ﻿[Download Codex for Mac or Windows](https://openai.com/codex/)﻿

* ﻿[Learn the basics about Codex for work](https://openai.com/academy/codex-for-work/)﻿

* ﻿[Explore how business operations teams use Codex](https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex/)﻿

* ﻿[Explore the top 10 use cases for Codex at work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)﻿

* ﻿[Learn about plugins and skills](https://openai.com/academy/codex-plugins-and-skills/)﻿

## Before you try the demos

For the business operations workflows in this webinar, make sure Codex is installed. Some demos also use the Data Analytics plugin and connected tools such as Databricks, Slack, documents, spreadsheets, or local project files. Your organization controls which plugins and connected tools are available in your workspace, so your exact setup may look different from the webinar.

The sample files are designed for practice. Before using any Codex output in a real operating review, leadership update, or stakeholder message, review the source details, metric definitions, assumptions, caveats, and owner follow-ups.

## Mini-demo: Clean and align operating files

The first example starts small. Codex uses two messy CSV files, an initiative tracker and a KPI export, to clean the inputs, compare initiative status, and create a reviewable Word summary.

Use this prompt in Codex:

```
Use the two CSV files in this folder. Clean and align them so the initiatives can be compared. Normalize initiative names, owners, statuses, and dates. Identify where the tracker status and KPI status disagree. Create new cleaned CSVs and a Word document called weekly_initiative_status_summary.docx with the key findings and follow-ups.
```

After Codex creates the files, open the cleaned CSVs and the Word document. Check whether the initiatives line up, whether the status disagreements make sense, and whether the follow-ups are clear enough for a weekly operating review.

## Main demo: Build a weekly bookings review dashboard

The first main demo shows how Codex can help move from raw data and working context to a dashboard the team can inspect. Codex uses the Data Analytics plugin, Databricks bookings data, stakeholder context, and files in the project folder to build a weekly bookings review dashboard.

Start the dashboard workflow:

```
@Data Analytics build a weekly bookings review dashboard using this folder, the bookings data from Databricks, and stakeholder context from #wanderbricks-marketplace-health. Show what changed, what needs attention, and what follow-up is needed. Include source notes and data caveats.
```

Once Codex creates the first version, open the dashboard and inspect it. Look for the weekly readout, supporting metrics, source notes, and caveats. This is where you should check whether the dashboard is organized around the right operating questions.

Then validate the revenue metric before using it in a weekly readout:

```
Before I use this in the weekly readout, validate the revenue metric in the executive summary. I want completed payment value to be the primary revenue outcome, not payment coverage or gross bookings. Check the Databricks tables and fields that support the calculation, call out exclusions or caveats, and update the local HTML dashboard if the current metric is leading with the wrong thing.
```

After Codex updates the dashboard, review the metric logic. Check which tables and fields support the calculation, what exclusions or caveats matter, and whether the dashboard now leads with the right revenue outcome.

Next, refine the dashboard for the weekly business review:

```
Refine the dashboard for a weekly business review. Make the executive summary more action-oriented. Highlight only the items that changed, failed, or need a decision. Make owner follow-ups and data caveats easy to see.
```

This is the step where the dashboard becomes more useful as an operating readout. It should lead with what needs attention, what decision is needed, and what the team should follow up on.

Then turn the dashboard readout into a weekly update:

```
Using this dashboard readout, draft a weekly team update. Include the top operating signals, decisions needed, owner follow-ups, and any data caveats the team should know.
```

Review the update before sharing it. Look for the top operating signals, decision asks, owner follow-ups, and caveats. The goal is a strong first pass that you can check, edit, and share with confidence.

## Make the weekly update repeatable

If this is a workflow you run every week, Codex can help turn it into an automation.

Use this prompt:

```
Create a weekly automation that runs every Monday morning after this dashboard is refreshed. Use the dashboard findings to generate 3-5 key bullet point takeaways for the week, including any decisions needed, owner follow-ups, and data caveats. Send the text update to me in Slack for review before I share it with the team.
```

The automation is not just a reminder. It prepares a weekly set of takeaways in Slack so you can review the update before sharing it more broadly.

## Main demo: Create a leadership decision deck

The second main demo starts from the dashboard readout. The dashboard helps the team understand what changed; the decision deck helps leadership decide what to do about it.

For this demo, use the dashboard readout, project files, and example leadership deck included in the demo materials.

Create the first version of the deck:

```
Using the dashboard readout, project files, and example leadership deck, create a matching leadership decision deck. Show what changed, the decision leaders need to make, recommended next steps, and source notes for key metrics or claims.
```

After Codex creates the deck, open it and inspect the story. Check whether it follows the example deck, explains what changed, names the decision leaders need to make, and includes source notes for key metrics or claims.

Before refining the deck, ask Codex to show its reasoning:

```
Before I refine this deck, show me how you arrived at the recommendation. For each key claim, cite the dashboard section or source table behind it, and call out any caveat that should be visible to leadership.
```

This is an important review step for analytical work. You are not just accepting a polished answer. You can ask Codex to explain its reasoning, show its sources, and make the evidence reviewable.

Then refine the deck for leadership:

```
Update the deck so it is tighter for a leadership audience. Keep the visual style aligned to the example deck, make the recommendation explicit, and move any caveats into speaker notes.
```

Review the revised deck before using it. Look for a clearer recommendation, a tighter leadership story, visual alignment with the example deck, and caveats preserved in speaker notes.

Finally, turn the deck workflow into a reusable skill:

```
Turn this into a skill for producing leadership decision decks.
```

The skill captures the structure, evidence standard, and deck format so the next leadership decision deck can start from the way your team already works.

## What to try next

You do not have to start by rebuilding every operating review or connecting every system at once. Pick one business operations workflow that already shows up in your week: a weekly performance readout, a leadership decision deck, or an initiative status update.

The pattern is the same as what we showed in the webinar: give Codex the right files and data context, ask for a specific deliverable, check the reasoning and sources, then refine the workflow so you can reuse it next time.

For more examples, visit [How business operations teams use Codex](https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex/).

1

Table Of Contents

[ChatGPT 101 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

[Codex for everyday work: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/codex-for-everyday-work-webinar-resource-guide-2026-05-05)

By Diana Stegall

[ChatGPT 102 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide)

[How marketing teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-marketing-teams-use-codex-webinar-resource-guide-2026-06-22)

Jun 23rd, 2026 • Views 175

[How data science teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-data-science-teams-use-codex-webinar-resource-guide-2026-05-28)

May 28th, 2026 • Views 805

[How sales teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-sales-teams-use-codex-webinar-resource-guide-2026-06-10)

Jun 11th, 2026 • Views 925

[How finance teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-finance-teams-use-codex-webinar-resource-guide-2026-05-19)

May 20th, 2026 • Views 1.6K

[How marketing teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-marketing-teams-use-codex-webinar-resource-guide-2026-06-22)

Jun 23rd, 2026 • Views 175

[How sales teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-sales-teams-use-codex-webinar-resource-guide-2026-06-10)

Jun 11th, 2026 • Views 925

[How finance teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-finance-teams-use-codex-webinar-resource-guide-2026-05-19)

May 20th, 2026 • Views 1.6K

[How data science teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-data-science-teams-use-codex-webinar-resource-guide-2026-05-28)

May 28th, 2026 • Views 805
