<!-- source: https://learn.chatgpt.com/use-cases/use-your-computer-with-codex -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Use your computer with ChatGPT

Let ChatGPT click, type, and navigate apps on your Mac.

Difficulty **Easy**

Time horizon **5m**

Use Computer Use to hand off multi-step tasks across Mac apps, windows, and files, and monitor progress in picture-in-picture.

## Best for

* Tasks that move across apps, windows, browser sessions, or local files on your Mac
* Work you want to hand off and let ChatGPT continue in the background

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/use-your-computer-with-codex/?export=pdf)

Use Computer Use to hand off multi-step tasks across Mac apps, windows, and files, and monitor progress in picture-in-picture.

Easy

5m

Related links

[Computer Use](/codex/computer-use)  [Plugins](/codex/plugins)  [Customize ChatGPT](/codex/customization/overview)

## Best for

* Tasks that move across apps, windows, browser sessions, or local files on your Mac
* Work you want to hand off and let ChatGPT continue in the background

## Starter prompt

@Computer [do the task you want completed across your Mac]
For example:
- Play some music to help me focus.
- Help me add my interview notes from Notes to Ashby.
- Look through my Messages app for the trip ideas Brooke sent me this week, add the best options to a new note called "Yosemite ideas", and draft a reply back to her.

@Computer [do the task you want completed across your Mac]
For example:
- Play some music to help me focus.
- Help me add my interview notes from Notes to Ashby.
- Look through my Messages app for the trip ideas Brooke sent me this week, add the best options to a new note called "Yosemite ideas", and draft a reply back to her.

## Introduction

You can let ChatGPT operate an app the same way you would: by clicking, seeing, and typing. [Computer Use](/codex/computer-use) is useful when the task lives inside a normal app UI, even if that app does not have a dedicated plugin.

This works especially well for tasks that jump between apps or windows, such as collecting notes, updating a system of record, copying details from one place to another, or drafting a reply after checking context in a few different apps.

## How to use

1. Install the [Computer Use plugin](/codex/computer-use).
2. Start your request with `@Computer`, or mention a specific app such as `@Slack` or `@Messages`.
3. Describe the task and the outcome you want.
4. Approve access when ChatGPT needs it, then let it continue the task in the background.

If you mention a specific app and a plugin exists for that app, ChatGPT may prefer the plugin over Computer Use. That is usually what you want. If no plugin exists, ChatGPT can fall back to Computer Use and operate the app directly.

For example:

* `@Computer Play some music to help me focus.`
* `@Computer Help me add my interview notes from Notes to Ashby.`
* `@Computer Go through my Slack and add reminders for everything I need to do by end of day.`

## Practical tips

### Follow along while ChatGPT works

When Computer Use starts working in an app, ChatGPT automatically opens a picture-in-picture (PiP) preview. Move the PiP around the ChatGPT window or click it to open the app being used. If you use a Pet, you can send the PiP to your Pet to monitor the task outside the ChatGPT window. When a task uses multiple apps or browser windows, their previews appear as a stack you can cycle through. If you dismiss the PiP, you can reopen it from the **Summary** view while Computer Use is running.

### Choose the browser ChatGPT should use

Computer Use takes control of the app it is operating. If you want to keep working in one browser while ChatGPT browses in another, tell it which browser to use. You can also set a default in [customization](/codex/customization/overview), for example: “When using Computer Use for web browsing tasks, default to Chrome instead of Safari.”

### Avoid parallel runs in the same app

Do not run two Computer Use tasks against the same app at the same time. That makes it much harder for ChatGPT to keep stable context about the current window and state.

### Stay signed in

For smoother runs, make sure you are already signed in to the apps and services you want ChatGPT to use. If your Mac locks while Computer Use is running, the activity will stop.

## Good follow-ups

Once the work finishes, keep the same chat open if you want ChatGPT to summarize what it changed, double-check the result, or turn the workflow into a more repeatable pattern through [customization](/codex/customization/overview).

## Suggested prompt

**Hand Off One Computer Task**

@Computer [do the task you want completed across your Mac]
For example:
- Play some music to help me focus.
- Help me add my interview notes from Notes to Ashby.
- Look through my Messages app for the trip ideas Brooke sent me this week, add the best options to a new note called "Yosemite ideas", and draft a reply back to her.

## Related use cases

[![](/codex/use-cases/complete-tasks-from-messages.webp)

### Complete tasks from messages

Use Computer Use to read one Messages thread, complete the task, and draft a reply.

Knowledge Work  Integrations](/codex/use-cases/complete-tasks-from-messages)[![](/codex/use-cases/prepare-committee-packet.webp)

### Prepare a committee packet

Use ChatGPT with prior minutes, policy drafts, stakeholder feedback, program data...

Knowledge Work  Integrations](/codex/use-cases/prepare-committee-packet)[![](/codex/use-cases/build-exam-study-system.webp)

### Build an exam study system

Use ChatGPT with learning objectives, notes, readings, problem sets, prior quizzes, exam...

Knowledge Work  Analysis](/codex/use-cases/build-exam-study-system)
