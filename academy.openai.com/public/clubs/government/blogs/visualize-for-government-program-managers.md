<!-- source: https://academy.openai.com/public/clubs/government/blogs/visualize-for-government-program-managers -->

Article

September 8, 2026

# From status updates to decisions: Visualize for government program managers

![From status updates to decisions: Visualize for government program managers](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/gradual-cover-03ec82e3-b091-49ff-8794-1b9045707c6d-1788873972782.jpeg?fit=scale-down&width=1200)

# ChatGPT

## Four ways to make milestones, dependencies, and next steps easier to see with ChatGPT.

![Laura  Keenan](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Headshot-53798635-8187-41c2-bd0a-15cee49c1e98-1784555485528.jpeg?fit=scale-down&width=60)

![From status updates to decisions: Visualize for government program managers](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/gradual-cover-03ec82e3-b091-49ff-8794-1b9045707c6d-1788873972782.jpeg?fit=scale-down&width=1200)

*Four ways to make milestones, dependencies, and next steps easier to see with ChatGPT.*

You finish the weekly program review with a page of notes, an updated tracker, and a familiar challenge: turning everyone’s individual updates into a clear picture of the program.

Which milestone is at risk? What is waiting on another office? Where does leadership need to make a decision?

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-8312806d-739e-46a6-9d89-e371cf95a042-1788873927745.png)

For government program managers, these questions connect the daily work of coordination to delivery. An interactive visual offers another way to work through them with your team.

OpenAI’s video,  [Make information visual with ChatGPT](https://www.youtube.com/watch?v=jzmNh8lbSp8), introduces a workflow for turning meeting notes into an interactive interface, refining it with calendar views and actions, and exporting an image or publishing a site. That approach is a useful starting point for program reviews: bring the relevant information together, make the relationships visible, and focus the discussion on what happens next.

<!-- yt-inline:jzmNh8lbSp8 -->
[![Make information visual with ChatGPT](https://img.youtube.com/vi/jzmNh8lbSp8/hqdefault.jpg)](https://www.youtube.com/watch?v=jzmNh8lbSp8)

<details>
<summary>자막: Make information visual with ChatGPT (1:26)</summary>

[00:00]
You know how sometimes when
you're talking to ChatGPT or
Codex, you don't want the result to just
be text or output,
you want to visualize it. Well,
there's a skill for that. It's the
Visualize skill and
it lets you turn anything into a
visualization, which is super convenient
when you want to process dense
information. So let's take an example.
Imagine you have a really long doc,
like meeting notes. You could read
through those meeting notes or
you could just ask ChatGPT to generate a
nice interface for them. For example,
here I had these meeting notes about
an event that we're planning and
at a glance, I can see what was
decided, the delivery timeline,
what still needs a decision,
and you can also iterate. For example,
I can ask a calendar view and
that's exactly what I get.
You can go even further than that.
You can have interactive visualization.
So if you need to see things in
different tabs, you can even add buttons
that will send prompts for you in the

[00:01]
chat directly. And when
you're ready to share this with your
team, you can export it as
an image or
you can even publish it as
a site and share a link.
This really is one of my favorite
features. Since I discovered it,
I use it all the time for my
morning brief, to get up to speed on
any topic or
for any projects I'm working on really.
So if you haven't used it,
try it and you'll see.

</details>


## What Visualize brings to a program review

Visualize can create interactive charts, diagrams, calculators, simulations, and other visual explanations inside ChatGPT. Readers can explore relationships or adjust inputs to understand what changes. Availability depends on the plan, platform, account, and workspace. See the  [official Visualizations guide](https://learn.chatgpt.com/docs/visualizations).

For a program manager, a useful first request is specific: “Show me which workstreams depend on this review,” or “Let me filter the action list by responsible office.” Start with a question your next meeting needs to answer.

The following prompts are suggested applications. Use public or fictional information to practice, and use program materials only in an environment approved for that data. These examples do not establish availability in a particular government deployment.

## 1. Leave the coordination meeting with clear ownership

A program can have plenty of activity and still have an unresolved handoff. The communications team is waiting for final requirements. The training lead needs a confirmed launch date. An action appears in the notes without an owner.

An interactive action board could help you surface those gaps and follow up with the right office.

**Try this prompt:**

> Use Visualize to turn these meeting notes into an interactive action board for me as a government program manager. Show each action, responsible office, named owner if provided, due date, status, and dependency. Add filters by workstream and office, plus a calendar for confirmed deadlines. Let me open each action to see its supporting excerpt. Keep agreed commitments separate from proposals. Mark missing owners, dates, and statuses “Not specified.” Notes: [paste approved or fictional notes].

**Then refine it:**

> Add a “Follow up before the next review” view showing unresolved handoffs, missing owners, and questions I need to take back to the team. Do not assign anyone new work.

Use the view to confirm ownership with your colleagues, then record agreed changes in your program’s official tracker.

## 2. See what a slipping milestone affects

A delayed review can affect several workstreams. Seeing those connections helps you explain the implications and discuss options before changing the plan.

**Try this prompt:**

> Use Visualize to create an interactive timeline from the program milestones below. Show baseline dates, responsible offices, and explicitly documented dependencies. Flag missing durations or dependency rules before calculating schedule changes. Add a scenario control that moves a selected milestone by a number of working days and shows the effect on dependent milestones using rules I confirm. Keep the baseline visible and label scenario dates “Proposed.” Show the working-calendar assumptions. Milestones: [paste approved or fictional milestone data].

**Then refine it:**

> Show the effect of a five-working-day delay to the review milestone. Summarize which deliverables move, which remain unchanged, and what needs validation with the workstream owners.

This gives you a concrete basis for a schedule discussion. A scenario remains a planning option until the responsible people agree to a change.

## 3. Make workload assumptions visible

When a program includes processing requests, reviewing submissions, or completing a queue of deliverables, you may need to explain whether the planned throughput can keep pace with demand.

A simple interactive calculator can help colleagues examine the assumptions together.

**Try this prompt:**

> Use Visualize to build a workload scenario calculator for a fictional government program. Begin with 240 pending requests, 100 new requests per week, and capacity to complete 120 per week. Let me adjust incoming volume and weekly completion capacity. Plot the backlog over 12 weeks using: next backlog = max(0, current backlog + arrivals − capacity). Show the formula, assumptions, and a data table. Label the result a simplified planning scenario. Check that the baseline reaches zero at week 12.

**Then refine it:**

> Compare the baseline with 130 new requests per week. Explain what changes and list the additional information I would need before making a resource recommendation.

Real planning would also need to account for request complexity, rework, and available staff time. The calculator gives those discussions a visible starting point.

## 4. Build a leadership view around the decisions needed

A leadership briefing needs to make the next decision clear. A useful view connects an issue to the affected milestone, available options, and the date by which an answer is needed.

**Try this prompt:**

> Use Visualize to create an interactive leadership briefing from the program updates below. Start with three sections: milestones, dependencies, and decisions needed. For each decision, show the question, documented options and tradeoffs, decision owner, requested decision date, and affected deliverables. Let the reader expand an item to inspect its source excerpt. Mark missing information explicitly. Do not invent recommendations, approvals, or status ratings. Updates: [paste approved or fictional updates].

**Then refine it:**

> Create a concise briefing view for a five-minute discussion. Lead with decisions that have documented deadlines before the next program review. Include a text summary and preserve links back to the supporting details.

Before the briefing, confirm that each ask is current, the decision owner is correct, and the options accurately reflect the team’s analysis.

## Try it at your next program review

In a supported ChatGPT chat, type **@**, enter **Visualize**, and select the matching plugin. If it does not appear, check availability for your account and workspace in the  [official guide](https://learn.chatgpt.com/docs/visualizations).

Choose one input: your approved meeting notes, milestone list, or program update. Name the audience and the question you need answered. Then describe the interaction that would help: filter by office, inspect a dependency, or compare a proposed schedule with the baseline.

Check the result against the source, including dates, owners, calculations, and omissions. Ask for readable labels, keyboard-friendly controls, and a text or table alternative. Keep official records current through your established process, and review any export or publication for its intended audience.

At the next meeting, test the view with three questions: **Can we see what is due? Can we see what is blocked? Can we see who needs to decide?**

That is a practical measure of whether the visual is helping you manage the program.

﻿ [Watch the inspiration: Make information visual with ChatGPT](https://www.youtube.com/watch?v=jzmNh8lbSp8).

[Better Powerpoint slides. Clearer decisions for government presentations.](/public/clubs/government/resources/better-powerpoint-slides-clearer-decisions-for-government-presentations-2026-07-24)

By Laura Keenan • Jul 27th, 2026 • Views 22

By Amanda Bullock • Sep 10th, 2026 • Views 20

By David Sperry • Jul 19th, 2025 • Views 211

[From a Full Calendar to Executive Readiness: Five ChatGPT Work Prompts for Government Executive Assistants](/public/clubs/government/resources/from-a-full-calendar-to-executive-readiness-five-chatgpt-work-prompts-for-government-executive-assistants-2026-08-11)

By Laura Keenan • Aug 11th, 2026 • Views 14

[Better Powerpoint slides. Clearer decisions for government presentations.](/public/clubs/government/resources/better-powerpoint-slides-clearer-decisions-for-government-presentations-2026-07-24)

By Laura Keenan • Jul 27th, 2026 • Views 22

By David Sperry • Jul 19th, 2025 • Views 211

[From a Full Calendar to Executive Readiness: Five ChatGPT Work Prompts for Government Executive Assistants](/public/clubs/government/resources/from-a-full-calendar-to-executive-readiness-five-chatgpt-work-prompts-for-government-executive-assistants-2026-08-11)

By Laura Keenan • Aug 11th, 2026 • Views 14

By Amanda Bullock • Sep 10th, 2026 • Views 20
