<!-- source: https://developers.openai.com/training/walkthroughs/plugins-and-skills/ -->

](/images/codex/work-101/plugins-and-skills.webp)](https://cdn.openai.com/devhub/videos-learn/work-101/plugins-and-skills.mp4)

# Plugins and skills

Plugins give ChatGPT new things it can do. Skills save how you want those things done.

## Plugins add capabilities

Plugins connect ChatGPT Work to apps and services you already use. They
can bring in current information and help ChatGPT take action in tools
like Slack, Gmail, Google Calendar, Notion, GitHub, and Figma.

![](/images/codex/apps/gmail.svg)

Gmail

Find emails, pull out useful details, and draft replies.

![](/images/codex/apps/google-calendar.svg)

Google Calendar

Check availability and create calendar events.

![](/images/codex/apps/slack.svg)

Slack

Find conversations, summarize context, and draft messages.

![](/images/codex/apps/notion.svg)

Notion

Find knowledge and create or update pages.

More plugins for the work you do

* [![](/images/codex/work-plugins/google-drive.png)   Google Drive](https://chatgpt.com/plugins/plugin_connector_1p_ab21a553bfbc81919ea8fd1858e3ffa7)
* [![](/images/codex/work-plugins/outlook-email.png)   Outlook Email](https://chatgpt.com/plugins/plugin_connector_1p_6bcb5879c73c819196abc70016166099)
* [![](/images/codex/work-plugins/teams.png)   Teams](https://chatgpt.com/plugins/plugin_connector_1p_eba8b52fe53881918408d4b46b957644)
* [![](/images/codex/work-plugins/sharepoint.png)   SharePoint](https://chatgpt.com/plugins/plugin_connector_1p_dca009ae2c848191ae14df3a47c5e7fd)
* [![](/images/codex/work-plugins/github.svg)   GitHub](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699)
* [![](/images/codex/work-plugins/canva.png)   Canva](https://chatgpt.com/plugins/plugin_connector_68df33b1a2d081918778431a9cfca8ba)
* [![](/images/codex/work-plugins/figma.png)   Figma](https://chatgpt.com/plugins/plugin_connector_68df038e0ba48191908c8434991bbac2)
* [![](/images/codex/work-plugins/linear.svg)   Linear](https://chatgpt.com/plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c)
* [![](/images/codex/work-plugins/atlassian-rovo.png)   Atlassian Rovo](https://chatgpt.com/plugins/plugin_connector_692de805e3ec8191834719067174a384)
* [![](/images/codex/work-plugins/hubspot.png)   HubSpot](https://chatgpt.com/plugins/plugin_asdk_app_697acb8e53d88191bf7a79e62012ae14)
* [![](/images/codex/work-plugins/zoom.jpg)   Zoom](https://chatgpt.com/plugins/plugin_asdk_app_69373a13116c819189d046aea1278836)
* [![](/images/codex/work-plugins/dropbox.png)   Dropbox](https://chatgpt.com/plugins/plugin_asdk_app_69b31dc2110c8191b8b47dc98fe5a052)
* [![](/images/codex/work-plugins/adobe-acrobat.jpg)   Adobe Acrobat](https://chatgpt.com/plugins/plugin_asdk_app_6938a7d323f48191aeabaf579802bf45)
* [![](/images/codex/work-plugins/outlook-calendar.png)   Outlook Calendar](https://chatgpt.com/plugins/plugin_connector_1p_fd0f4f41caa88191a9456514bbffa06d)

Select a plugin to open it in ChatGPT. Available plugins and actions depend
on your plan and workspace.

### Browse plugins

Open [Plugins](https://chatgpt.com/plugins)
to explore what is available. Choose one for the job, connect your account,
and use it directly in your conversation.

 [![The ChatGPT Work plugin directory](/images/codex/get-started-with-work/plugins.webp)](https://chatgpt.com/plugins)

### Use plugins in a task

01

#### Connect your apps

Open Plugins and connect Gmail and Google Calendar, or choose the
plugins your own task requires. Check the account and requested
access before connecting.

[![](/images/codex/apps/gmail.svg)Gmail

Find and draft email

Add](https://chatgpt.com/plugins/plugin_connector_1p_95d39881713c8191931482a62d6edff9?q=gmail)[![](/images/codex/apps/google-calendar.svg)Google Calendar

Review events and availability

Add](https://chatgpt.com/plugins/plugin_connector_1p_f8509de903288191b14a160c6c5d20b0?q=calendar)

02

#### Describe the outcome

Ask ChatGPT to find the relevant email, check your calendar, and
prepare a meeting at a time that works. Type **@**
in the message box and select a plugin or skill from the menu. Here,
use **@Gmail** and **@Google Calendar**.

Find the latest email about [project] in @Gmail. Check @Google Calendar and suggest a 30-minute kickoff before Friday. Draft the title, attendees, time, and agenda. Show me everything before creating the event.

[Open this prompt in ChatGPT Work (opens in a new tab)](https://chatgpt.com/?surface=work&prompt=Find+the+latest+email+about+%5Bproject%5D+in+%40Gmail.+Check+%40Google+Calendar+and+suggest+a+30-minute+kickoff+before+Friday.+Draft+the+title%2C+attendees%2C+time%2C+and+agenda.+Show+me+everything+before+creating+the+event.)

03

#### Review the result

Open the source email and check the time, attendees, and agenda.
Ask for changes or approve the event when it looks right.

![](/images/codex/apps/google-calendar.svg)

Google Calendar

**Ready for review**

* Time **Thursday · 2:00 PM**
* People **Attendees from the email**
* Agenda **Project context and next steps**

Example action Create meeting

## Save and reuse a skill

A skill saves the instructions, references, and examples that tell ChatGPT
how you want a task done. Use one when you repeat a task or want every
result to follow the same structure.

In the example above, you used Gmail and Google Calendar to plan a project
kickoff: the first meeting for a new project.

Next, ask ChatGPT to turn that email and calendar event into a
source-linked brief with these sections: objective, client priorities, decisions, risks, and next steps.
Review the brief, refine it, and save the process as Meeting Prep. Then
run it for another meeting.

For example, a skill can prepare meeting briefs, format project updates,
plan weekly meals, build trip packing lists, turn notes into study guides,
or review monthly spending in a consistent format.

1. **Do it once:** Finish a task with the result you want.
2. **Save the method:** Keep the instructions and examples.
3. **Use it again:** Run the skill with new information.
4. **Refine it:** Update the method as your needs change.

In the ChatGPT desktop app, connect Gmail and Google Calendar in Plugins
before you begin. Replace [project] with your own project. Start the first
prompt in Work, then copy and paste each follow-up into that same chat.

1. ### Schedule a meeting

   Find the latest email about [project] in @Gmail. Check @Google Calendar and suggest a 30-minute kickoff before Friday. Draft the title, attendees, time, and agenda. Show me everything before creating the event.

   [Open this prompt in ChatGPT Work (opens in a new tab)](https://chatgpt.com/?surface=work&prompt=Find+the+latest+email+about+%5Bproject%5D+in+%40Gmail.+Check+%40Google+Calendar+and+suggest+a+30-minute+kickoff+before+Friday.+Draft+the+title%2C+attendees%2C+time%2C+and+agenda.+Show+me+everything+before+creating+the+event.)
2. ### Prepare a brief

   Review the source email, time, attendees, and agenda before approving the event.

   Prepare a brief for this meeting using the relevant email in @Gmail and the event in @Google Calendar. Include these sections: objective, client priorities, decisions, risks, and next steps. Link to the original email and calendar event. Flag missing details instead of guessing.
3. ### Save a skill

   Review the brief and ask for changes until it has the format you want.

   Save this workflow as a skill called meeting-prep. Check @Google Calendar, find the relevant email in @Gmail, and organize each brief into these sections: objective, client priorities, decisions, risks, and next steps. Link to the original email and calendar event, and flag missing details. Ask me before creating or changing any events.
4. ### Run it again

   Use @meeting-prep for another meeting about [project] on my calendar.

## [Set up scheduled tasks](/training/walkthroughs/scheduled-tasks)

Ask ChatGPT to run useful work later or repeat it on a schedule, then review every run in the Scheduled tab.

![Video thumbnail for Set up scheduled tasks](/images/codex/work-101/scheduled-tasks.webp)
