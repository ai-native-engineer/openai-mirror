<!-- source: https://academy.openai.com/public/clubs/government/blogs/before-the-first-meeting-a-morning-brief-for-government-chiefs-of-staff -->

Article

September 9, 2026

# Before the first meeting: A morning brief for government chiefs of staff

![Before the first meeting: A morning brief for government chiefs of staff](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/academy-cover-v2-37c6d41f-ee1f-4fe3-8956-35c74c2f0ff7-1788874933039.jpeg?fit=scale-down&width=1200)

# Productivity

## How to use scheduled tasks in ChatGPT to build a repeatable briefing routine—with staff review built in.

![Laura  Keenan](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Headshot-53798635-8187-41c2-bd0a-15cee49c1e98-1784555485528.jpeg?fit=scale-down&width=60)

![Before the first meeting: A morning brief for government chiefs of staff](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/academy-cover-v2-37c6d41f-ee1f-4fe3-8956-35c74c2f0ff7-1788874933039.jpeg?fit=scale-down&width=1200)

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-e76c5596-0f1c-479b-b3e9-7f71f1e2cf7b-1788873910168.png)

A chief of staff’s morning can begin with three versions of the agenda, an overnight email that changes the conversation, and a decision the leader needs to make before the first meeting.

The preparation is familiar: gather the context, reconcile the updates, and identify what deserves the leader’s attention. Repeating that work every morning makes it a useful place to try scheduled tasks in ChatGPT.

OpenAI’s  [scheduled-tasks walkthrough](https://learn.chatgpt.com/training/walkthroughs/scheduled-tasks) demonstrates preparing meeting briefs from connected calendar events and emails, refining the result, and scheduling it to run again. For a government chief of staff, the application is straightforward: a first draft of the morning packet, ready for staff review.

## Start with one leader and one useful brief

Choose a bounded pilot: one calendar, a defined set of related correspondence, and a brief your leader can scan quickly. Decide what a useful result must contain before scheduling anything.

A practical structure is:

**Today’s priorities:** The issues most likely to need the leader’s attention.

**Meeting preparation:** Purpose, relevant context, and any documented decision requested.

**Open commitments:** Follow-ups, owners, and deadlines supported by the records.

**Gaps to resolve:** Missing information or conflicting updates that staff should check.

Use an agency-approved environment and only information permitted there. Confirm that scheduled tasks and the required connections are available in your workspace; this example does not establish availability in any particular government deployment. You can practice the drafting step with fictional materials if live connections are unavailable.

## Prompt 1: Build the first morning brief

Replace the bracketed text with your approved sources and local time zone.

> Prepare a draft morning brief for the chief of staff supporting [office or leader]. Use [approved calendar] for today’s meetings in [time zone] and [approved email source] for relevant correspondence from the past seven days.
>
> Begin with up to three priorities, explaining why each needs attention today. Then summarize each meeting: time, purpose, relevant background, documented decisions requested, and open commitments with their recorded owners and deadlines.
>
> Link factual statements to the supporting events or messages. Distinguish documented facts from your inferences. Do not infer attendance from an invitation or invent a position, owner, deadline, or decision. Flag conflicting records and missing information. Identify any source you could not access and include the preparation timestamp.
>
> Keep the main brief under 600 words. Return it for my review without sending messages or changing records.

Read the first result against the original sources. Does it capture the decision behind the meeting? Does it distinguish a proposed deadline from an agreed one? A polished summary still needs those checks.

## Prompt 2: Make the brief useful for decisions

> Revise this brief for a leader with five minutes to prepare. Put documented decisions needed today first, followed by unresolved dependencies and significant changes. Move routine background below the main brief.
>
> For each decision, state what is being asked, the documented deadline, and what information is still missing. If the sources do not establish that a decision is needed, say so. Preserve source links and uncertainty. List up to three questions I should resolve with staff before sharing the packet.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-0bd2405c-db99-4848-aaf6-945add8346c8-1788873933795.png)

*The review step: verify the sources, resolve gaps, and add the judgment only your office can provide.*

## Prompt 3: Schedule the version you have reviewed

Once the format is useful, add the schedule in the same conversation. The walkthrough explains how to inspect results, edit instructions, or pause a task in the Scheduled tab.  [See the setup steps](https://learn.chatgpt.com/training/walkthroughs/scheduled-tasks).

> Run this morning-brief task every weekday at 7:00 a.m. America/New\_York. Use that day’s calendar and the latest relevant correspondence from the approved sources specified above. Keep the structure, word limit, source links, and review boundaries we established.
>
> Include the preparation timestamp and clearly identify any unavailable sources or incomplete coverage. If there are no meetings, say so. Return each draft for my review without sending messages or changing records.

Check the next scheduled run. For tasks that depend on local files or locally saved skills, OpenAI’s walkthrough instructs users to keep the computer on and the desktop app running.

## When the agenda changes, ask what changed

A morning brief is a snapshot. Before a consequential meeting, request a fresh check:

> Compare the morning brief above with the latest accessible records for [meeting]. Show only changes to the time, agenda, documented decisions, and open commitments. Link each change to its source and distinguish confirmed changes from proposals. Flag unresolved conflicts. Do not update the calendar or contact participants.

## Keep the chief of staff in the review loop

The value of this routine is having more preparation in hand when the day begins. Staff still need to judge what matters, check sensitive context, and decide what reaches the leader.

Try it for one week. Track preparation time, corrections required, and whether the brief surfaces the right decisions. Refine the instructions based on those results before expanding to another recurring product.

Start with tomorrow’s first meeting. Build a brief worth reading. Then make that preparation repeatable.

**Watch and try:**  [Scheduled Tasks video](https://www.youtube.com/watch?v=urXc4xxixVU) ·  [Step-by-step walkthrough](https://learn.chatgpt.com/training/walkthroughs/scheduled-tasks)﻿

<!-- yt-inline:urXc4xxixVU -->
[![Scheduled Tasks](https://img.youtube.com/vi/urXc4xxixVU/hqdefault.jpg)](https://www.youtube.com/watch?v=urXc4xxixVU)

<details>
<summary>자막: Scheduled Tasks (2:10)</summary>

[00:00]
If you find yourself asking ChatGPT
to do the same thing every day,
turn it into a scheduled task.
With ChatGPT Work, I can create a scheduled task
to handle it automatically whenever I choose:
hourly, daily, weekly, you name it.
Let me show you how I use one
to get ready for my meetings
before the day even starts.
I'm using the desktop app, but you can also do this
in ChatGPT Work on the web or mobile at chatgpt.com.
For this, ChatGPT needs to use my calendar and email.
I'll open Plugins and make sure
Google Calendar and Gmail are connected.
If either one isn't, I'll select Install
and connect my account.
Before I schedule anything,
I want to make sure the result is actually useful.
I'll ask ChatGPT to look at today's meetings,
find relevant emails,
and make me a short brief for each one.

[00:01]
Great. That's exactly what I need.
Now I'll ask ChatGPT to do the same thing
every weekday at nine.
Now if I open Scheduled in the sidebar
I can see the task, the schedule,
and when it's running next.
I can change the time, pause it,
or remove it whenever I want.
You can also use scheduled tasks with skills.
A skill remembers how I like the work done.
The scheduled task decides when it happens.
I'm updating the scheduled task
to use my meeting prep skill,
so the document is formatted exactly how I like.
You can use the same idea for a twice a day
an urgent inbox check
Finding cool events in the city
Or hunting for sold out tickets
to a show you've been wanting to see
Just say what you want and when you want it.

[00:02]
Same routine, way less effort.
That's ChatGPT Work.

</details>


*Images are AI-generated editorial illustrations, not product screenshots or depictions of an actual government office.*

[From a Full Calendar to Executive Readiness: Five ChatGPT Work Prompts for Government Executive Assistants](/public/clubs/government/resources/from-a-full-calendar-to-executive-readiness-five-chatgpt-work-prompts-for-government-executive-assistants-2026-08-11)

By Laura Keenan

[A face behind the service: 5 image prompts for welcoming veterans](/public/clubs/government/blogs/a-face-behind-the-service-5-image-prompts-for-welcoming-veterans)

By Laura Keenan

By David Sperry • Jul 19th, 2025 • Views 210

[11:26](/public/clubs/government/videos/getting-started-chatgpt-government)

[Getting Started with ChatGPT Enterprise for Government Employees](/public/clubs/government/videos/getting-started-chatgpt-government)

By David Sperry • Jul 19th, 2025 • Views 114

By David Sperry • Jul 19th, 2025 • Views 211

[Show the story: 8 image prompts for government work](/public/clubs/government/blogs/show-the-story-8-image-prompts-for-government-work)

By Laura Keenan • Sep 9th, 2026 • Views 42

By David Sperry • Jul 19th, 2025 • Views 210

By David Sperry • Jul 19th, 2025 • Views 211

[Show the story: 8 image prompts for government work](/public/clubs/government/blogs/show-the-story-8-image-prompts-for-government-work)

By Laura Keenan • Sep 9th, 2026 • Views 42

[11:26](/public/clubs/government/videos/getting-started-chatgpt-government)

[Getting Started with ChatGPT Enterprise for Government Employees](/public/clubs/government/videos/getting-started-chatgpt-government)

By David Sperry • Jul 19th, 2025 • Views 114
