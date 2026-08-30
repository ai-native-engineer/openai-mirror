<!-- source: https://developers.openai.com/training/walkthroughs/scheduled-tasks/ -->

](/images/codex/work-101/scheduled-tasks.webp)](https://cdn.openai.com/devhub/videos-learn/work-101/scheduled-tasks.mp4)

# Set up scheduled tasks

Ask ChatGPT to run useful work later or repeat it on a schedule, then review every run in the Scheduled tab.

## Do it once, then schedule it

Ask ChatGPT in plain language what to do and when.

First, run the task in a regular chat and refine the result. When it
looks right, stay in the same chat and tell ChatGPT when to run it
again. ChatGPT turns that request into a scheduled task.

For this example, connect Gmail and Google Calendar in Plugins ([see more about plugins](/training/walkthroughs/plugins-and-skills)). ChatGPT can then use the calendar events and related emails to
prepare source-linked meeting briefs.

## Manage it from Scheduled

The Scheduled tab acts like an inbox for upcoming tasks and completed
runs. Open it to see what is active, what is paused, and when each task
will run next.

Open a task to review its latest result and run history. You can also
edit the instructions or schedule, pause the task, or delete it.

### Scheduled

Ask ChatGPT to schedule tasks, set reminders, or monitor for updates

Search scheduled tasks

AllActivePaused

Mark all as read

* Daily inbox summaryEvery weekday at 8:00 AM·Next run in 16 hours
* Weekly project updateFridays at 4:00 PM·Next run in 2 days
* Meeting follow-up remindersDaily at 5:00 PM·Next run in 4 hours

**Use plugins and skills with scheduled tasks.** Plugins such as Google Calendar and Gmail can provide current information for
each run. A skill preserves the method, and the scheduled task decides when the
work happens.

If the task only needs connected tools, run it on the web or choose Cloud in
the desktop app when available. Keep your computer on and the desktop app
running when a task needs local files or a skill saved only on that
computer.

In Plugins, connect Gmail and Google Calendar. Check that you selected the right accounts, then complete both steps in the same Work chat. If today is empty, change the first prompt to a date
with meetings.

1. ### First, run it once

   Using @Google Calendar, review today’s meetings and find the relevant emails in @Gmail. Prepare a short brief for each meeting with these sections: objective, client priorities, decisions, risks, and next steps. Link to the original emails and calendar events. Flag missing details. Show me the briefs before taking any other action.

   [Open this prompt in ChatGPT Work (opens in a new tab)](https://chatgpt.com/?surface=work&prompt=Using+%40Google+Calendar%2C+review+today%E2%80%99s+meetings+and+find+the+relevant+emails+in+%40Gmail.+Prepare+a+short+brief+for+each+meeting+with+these+sections%3A+objective%2C+client+priorities%2C+decisions%2C+risks%2C+and+next+steps.+Link+to+the+original+emails+and+calendar+events.+Flag+missing+details.+Show+me+the+briefs+before+taking+any+other+action.)
2. ### Then, add the schedule

   Copy this prompt into the same chat.

   Schedule this task to run every weekday at 9:00 AM. On each run, use that day’s meetings and the latest relevant emails. Return the same source-linked briefs without sending messages or changing events.

Open Scheduled, check the next run, and pause the task if you were only
practicing.

## [Creating slides and docs](/training/walkthroughs/creating-slides-and-docs)

Turn messy source material into a clear document, shape the refined content into a slide deck, and save both formats as templates to reuse.

![Video thumbnail for Creating slides and docs](/images/codex/work-101/creating-slides-and-docs.webp)
