<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/how-data-science-teams-use-codex-webinar-resource-guide-2026-05-28 -->

[Work Users](/en/public/clubs/work-users-ynjqu/overview)

[navigation.content](/en/public/clubs/work-users-ynjqu/content)

Webinar

May 28, 2026 · Last updated on June 11, 2026

# How data science teams use Codex: Webinar resource guide

![How data science teams use Codex: Webinar resource guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-9--42ff09c7-b43a-4f48-9ba8-799ed3039a67-1781141346777.jpeg?fit=scale-down&width=1200)

# Codex

# Codex for Work

## Follow along with our webinar: How data science teams use Codex

![How data science teams use Codex: Webinar resource guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-Academy-Event-Card-Templates-Work-Users-9--42ff09c7-b43a-4f48-9ba8-799ed3039a67-1781141346777.jpeg?fit=scale-down&width=1200)

## Follow along with the webinar: How data science teams use Codex

If you work in data science, analytics, BI, or data engineering, you probably know this moment: the data exists, but the decision-ready output still has to be built. You may have a dashboard with KPI movements, a notebook with the analysis, metric definitions, spreadsheet exports, stakeholder notes, and business context. Now someone still has to reconcile the inputs, validate the numbers, preserve the caveats, and turn the work into something the business can use.

That is the work this webinar focuses on. You will see how Codex can help build the asset around the analysis: pulling context together, creating a reviewable artifact, refining it with team-specific guidance, saving repeatable standards as a skill, and turning a dashboard signal into a recurring update.

## Resources to bookmark

* ﻿[Download Codex for Mac or Windows](https://openai.com/codex/)﻿

* ﻿[Learn the basics about Codex for work](https://openai.com/academy/codex-for-work/)﻿

* ﻿[Explore how data science teams use Codex](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex/)﻿

* ﻿[Explore the top 10 use cases for Codex at work](https://openai.com/academy/how-to-use-codex-for-everyday-work/)﻿

## Mini-demo: Create and revise a dashboard launch checklist

The first demo starts small on purpose. Codex uses one source file, *Enterprise\_Onboarding\_Dashboard\_Context.docx*, to create a real Microsoft Word document called Dashboard Launch Checklist. Then Codex revises that same file instead of starting over.

Before you try this, download the mini-demo file:

﻿[Download](https://docsend.com/view/s/rrff9nap5cs2xmzc)﻿

Use this prompt in Codex:

```
Use the docx file in this folder to create a short Microsoft Word document called Dashboard Launch Checklist.

It should help a data science team review a new executive dashboard before sharing it.

Keep the first version simple, with a title and a short list of checks for metric definitions, data quality, and stakeholder review.
```

After Codex creates the file, open it and review the first draft. Then ask Codex to revise the same document:

```
Revise the Dashboard Launch Checklist to make it more polished and easier to use.

Turn the checks into a table with columns for check, owner, and status, and add a short "Before sharing" section at the end.
```

The thing to notice: Codex is not just answering in the conversation. It is creating and updating an actual file you can open, review, and keep working on.

## Main demo: Build an insights analysis slide

The first main demo shows a realistic data science handoff: multiple workbooks, imperfect labels, launch and campaign context, and a business question that sounds simple but requires careful analysis. The output is a single executive-ready PowerPoint slide that explains what changed, why it likely changed, what the team knows, what is still a hypothesis, and what actions to take next.

Before you try this, download the dummy demo files:

[INSERT DOCSEND LINK HERE]

The first prompt creates the draft slide:

```
Use the files in this folder to explain why Self-Serve Net Revenue changed for the self-serve subscription business in April 2026

Clean the data, quantify the movement, find the main drivers by segment, cohort, channel, geography, and product surface, and use the launch and campaign notes to explain likely causes.

Create a first-pass executive PowerPoint slide called "Subscription Revenue Insights Slide" with the key takeaway, supporting charts, business impact, caveats, recommended actions, and file references.
```

Once Codex creates the slide, open it and inspect the first draft. Check whether it has the core pieces from the demo: the main takeaway, the revenue movement, the driver analysis, caveats, recommended actions, and file references.

Then revise the slide with team-specific review guidance:

```
Revise "Subscription Revenue Insights Slide" using these leadership revenue review standards:

- Lead with the business takeaway, not the analysis process.

- Make the slide action-oriented and easy for an executive audience to scan.

- Do not overstate April as a full-month decline if the data does not support that.

- Separate confirmed findings from hypotheses.

- Preserve caveats and source references.

- Use the launch and campaign notes to explain likely causes without implying certainty where the evidence is incomplete.

- Make the recommended actions specific enough for an owner to take forward.
```

In the webinar, that guidance includes executive review standards, interpretation rules, business context, and review expectations. This is the part that turns a first pass into something much closer to how a real team would use it.

## Turn the slide workflow into something reusable

After the slide is revised, the demo turns the workflow into a reusable Skill so the same analysis structure, interpretation rules, caveat standards, and slide expectations can carry forward.

Use this prompt:

```
Turn this workflow into a reusable skill called "Executive Analysis slides"
```

Then, the next time you want to use that playbook, reference the skill directly:

```
Use $Executive Analysis slides to transform these findings into a slide.
```

The skill is the reusable playbook. It helps the next version start from the standards you already taught Codex, instead of making you rewrite the same guidance each time.

## Main demo: Build and refine an operations analytics dashboard

The second main demo moves from a single slide to a working dashboard. The pattern is similar, but the output is more ambitious: Codex creates the dashboard files, logic, interface, and a workflow for pushing the dashboard signal back to Slack.

Before you try this, download the dummy demo files:

[INSERT DOCSEND LINK HERE]

The first prompt creates the dashboard:

```
Use the files in this folder to build a lightweight operations analytics dashboard.

The dashboard should help the team understand fulfillment performance across sites, channels, and time periods.

Include KPI cards, filters, trend views, site comparisons, return drivers, operational notes, and a methodology section. Make sure the dashboard can be opened locally, inspected, and refined.
```

Once Codex creates the dashboard files, open the dashboard and inspect the first version. Check whether it includes the main metrics, filters, charts, comparison views, notes, and methodology.

Then revise the dashboard with stakeholder-facing standards:

```
Revise the operations dashboard to make it more polished and more useful for a stakeholder audience.

Apply the following guidance:

- Improve the executive readout so the key signal is clear at the top.

- Use a cleaner visual hierarchy for KPI cards, filters, charts, and notes.

- Preserve the underlying analysis and methodology.

- Make site, channel, and time-period comparisons easier to scan.

- Add QA checks or caveats where the data could be misread.

- Keep the dashboard practical for someone who needs to decide what needs attention.
```

This follows the same pattern as the slide demo: the first pass creates the asset, and the second pass gives Codex the standards that make it useful for a real team.

## Send the dashboard signal to Slack

The dashboard is still the source of truth, but Codex can help turn it into an update that shows up where work is already happening. If you have connected Slack in Codex, try this prompt:

```
Send me a Slack DM with a summary of the current operations dashboard.
```

For a one-time update, that is useful. If this is something you want every week, turn it into an automation:

```
Create a weekly automation that sends me a Slack DM every Monday morning with a summary of the current operations dashboard.
```

The automation is not just a reminder. It creates the update and sends it where you already work.

## What to try next

You do not have to start by rebuilding your whole analytics stack or automating every dashboard. Pick one data science artifact that already shows up in your work: an analysis readout, a dashboard QA checklist, a KPI memo, an experiment summary, or a recurring stakeholder update.

The pattern is the same as what we showed in the webinar: give Codex the right files and context, ask for a specific reviewable output, validate the numbers and caveats, then refine the workflow and reuse it next time.

For more examples, visit [How data science teams use Codex](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex/).

Table Of Contents

[27:03](/en/public/clubs/work-users-ynjqu/videos/how-data-science-teams-use-codex-recording-2026-05-28)

Video

[How data science teams use Codex [Recording]](/en/public/clubs/work-users-ynjqu/videos/how-data-science-teams-use-codex-recording-2026-05-28)

[ChatGPT 101 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

[Codex for everyday work: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/codex-for-everyday-work-webinar-resource-guide-2026-05-05)

By Diana Stegall

[How marketing teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-marketing-teams-use-codex-webinar-resource-guide-2026-06-22)

Jun 23rd, 2026 • Views 175

[How business operations teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-business-operations-teams-use-codex-webinar-resource-guide-2026-06-17)

Jun 18th, 2026 • Views 230

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

[How business operations teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-business-operations-teams-use-codex-webinar-resource-guide-2026-06-17)

Jun 18th, 2026 • Views 230
