<!-- source: https://help.openai.com/en/articles/12525822-using-slack-in-chatgpt -->

# Using Slack in ChatGPT

Connect Slack to ChatGPT to search messages, reference permitted workspace content, and use available Slack actions.

The ChatGPT Slack app connects Slack to ChatGPT so you can search messages, threads, and channels you already have permission to access. Available actions depend on your Slack authorization, workspace settings, and app permissions.

Where available and enabled by a workspace admin, the ChatGPT Slack app can also take Slack actions on a user's behalf, such as joining a channel, creating a reminder, uploading a file, or updating the user's Slack profile.

For an overview of connected services, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

Type: app with search and actions

Where you can use it: Chat, deep research, and agent mode.

Availability depends on your ChatGPT plan, region, Slack workspace, and administrator settings. Check the options available in your account.

Slack is a third-party service. When you enable and use the ChatGPT Slack app, relevant requests and data may be transmitted to Slack and handled under Slack’s terms and privacy, retention, and data-residency policies. Review your organization’s Slack policies before enabling or using the app.

Example prompts

* “Summarize the discussions in the #engineering-team Slack channel from this week. Provide a concise overview of the main topics and decisions.”
* “Catch me up on everything unread in my Slack threads.”
* “Give me the recent updates from the #incident-service-unavailable Slack channel, including a summary of the root cause behind the incident.”
* “Create a one-page meeting brief with key points discussed in the #Marketing channel this week. Include action items.”

Using ChatGPT inside Slack is separate from using Slack as a connected source in ChatGPT. For setup instructions, see: [Using ChatGPT in Slack](https://help.openai.com/articles/12462158).

# Capabilities and permissions

## What it can access

* Slack conversations, threads, and channels you have access to.

## What it can do

* Summarize discussions and pull insights from Slack channels and DMs.
* Search channels and DMs by keyword on all Slack plans, or by meaning with semantic search on supported Slack Business+ or Enterprise+ workspaces where Slack AI Search is enabled.
* Create recaps or briefs based on information scattered across a channel.
* Where enabled by a workspace admin, take Slack actions on a user's behalf, such as joining a channel, creating a reminder, uploading a file, or updating the user's Slack profile.

Permissions requested:

* Methods
* [assistant.search.context](https://docs.slack.dev/reference/methods/assistant.search.context/)
* [chat.getPermalink](https://docs.slack.dev/reference/methods/chat.getPermalink/)
* [conversations.replies](https://docs.slack.dev/reference/methods/conversations.replies/)
* Scopes
* [search:read.public](https://docs.slack.dev/reference/scopes/search.read.public)
* [search:read.private](https://docs.slack.dev/reference/scopes/search.read.private)
* [search:read.mpim](https://docs.slack.dev/reference/scopes/search.read.mpim)
* [search:read.im](https://docs.slack.dev/reference/scopes/search.read.im)
* [search:read.files](https://docs.slack.dev/reference/scopes/search.read.files)
* [search:read.users](https://docs.slack.dev/reference/scopes/search.read.users)
* [chat:write](https://docs.slack.dev/reference/scopes/chat.write)
* [channels:history](https://docs.slack.dev/reference/scopes/channels.history)
* [groups:history](https://docs.slack.dev/reference/scopes/groups.history)
* [mpim:history](https://docs.slack.dev/reference/scopes/mpim.history)
* [im:history](https://docs.slack.dev/reference/scopes/im.history)
* [canvases:read](https://docs.slack.dev/reference/scopes/canvases.read)
* [canvases:write](https://docs.slack.dev/reference/scopes/canvases.write)
* [users:read](https://docs.slack.dev/reference/scopes/users.read)
* [users:read.email](https://docs.slack.dev/reference/scopes/users.read.email)

### Additional scopes for Slack actions

Some Slack actions require additional Slack OAuth scopes. The exact scopes requested can depend on which Slack actions are enabled and which scopes your workspace has already approved.

New or updated Slack actions may request scopes for:

* Inviting users to conversations: channels:write.invites, groups:write.invites, and related conversation write scopes.
* Joining or leaving conversations: channels:write, groups:write, im:write, and mpim:write.
* Creating reminders: reminders:write.
* Uploading files to Slack: files:write.
* Listing starred items: stars:read.
* Listing user groups: usergroups:read.
* Listing conversations visible to the user: channels:read, groups:read, im:read, and mpim:read.
* Updating a Slack profile: users.profile:write.

Known limitations

* Use with deep research, Pro models, or agent mode may exhaust your per-user Slack API quota even if workspace-wide limits are not reached.
* In Enterprise and Edu workspaces, the Slack app must be enabled for your workspace and available to your account. Workspace owners and admins can manage role-based access controls (RBAC), where supported, in the plugin’s settings.
* If your organization requires Slack admin approval for app scopes, a Slack admin may need to approve or reinstall the updated ChatGPT Slack app before users can grant additional scopes for newly enabled Slack actions.

## Set up Slack for a managed workspace

Business, Enterprise, and Edu admins can manage Slack in **Admin > Plugins**. Select the plugin that includes Slack to review availability, actions, access settings, and any Slack approval requirements. If your workspace still uses **Apps** settings, review Slack there.

For Business workspaces, the Slack app is enabled by default. Admins should review **Actions** for Slack and disable any action whose required Slack scope they do not want to approve.

For Enterprise and Edu workspaces, confirm that Slack is enabled and that the intended members have access. If Slack is disabled, enable it before members connect. During setup or later management, admins can:

* Review Slack’s details in the plugin that includes it, or in the **Apps** administration page if your workspace still uses it.
* Select **Role access** to configure role-based access controls, where available.
* Select **Actions** to review which Slack actions are available for the workspace.
* Disable any action that requires a Slack OAuth scope your organization does not want to approve.
* Select **Manage domains** if you want to limit which Slack accounts workspace members can connect.

If your organization uses Slack Enterprise Grid or requires admin approval for app scopes, coordinate with a Slack admin before enabling new Slack actions in ChatGPT.

Once Slack is enabled in ChatGPT and approved in Slack where required, each user can connect their individual account by signing in to Slack through an OAuth flow. See instructions below.

## Individual setup

Eligible Plus, Pro, Business, Enterprise, and Edu users can connect Slack:

1. Find **Slack** in **Apps** or **Plugins**, depending on the options shown for your account.
2. Select **Connect**.
3. Complete the authorization flow for the intended Slack workspace.

Availability depends on your plan, region, and workspace settings.

You can connect the ChatGPT Slack app to only one Slack workspace at a time.

## Create a task from Slack channel activity

Eligible users can create an event-triggered (webhook-based) task in Work that responds to new messages in a connected Slack channel. The Slack account must be connected to ChatGPT, and the user must have access to the channel.

1. Go to **Settings**, select **Apps** or **Plugins**, and connect Slack.
2. Add @ChatGPT to each public or private channel you want the task to monitor.
3. Open **Work** and describe the Slack activity and the action ChatGPT should take.
4. Review **Trigger**, **Condition**, and **Prompt** in the task details.

Slack triggers apply to messages in channels the app has joined, and can be narrowed by channel, sender, or thread. Direct messages, reactions, message edits, and deletions do not trigger tasks. Existing regional availability, workspace permissions, and admin approval requirements continue to apply.

Enterprise, Edu, and ChatGPT for Healthcare admins must enable **Allow event-triggered scheduled tasks** for Work before members can create Slack-triggered tasks.

## Share a scheduled task that uses Slack

When scheduled task sharing is available for your account, you can share an eligible scheduled task whose instructions refer to Slack. Eligible recipients can create a separate task using their own Slack account. Their account must have access to the Slack workspace or channels their copy requires.

A shared task link does not transfer your Slack connection, credentials, channel access, or message history. The task instructions are visible in the shared link, so remove sensitive Slack content before sharing. Existing Slack app availability, workspace permissions, and regional restrictions still apply.

Event-triggered Slack tasks can be shared. Eligible recipients must connect their own Slack account, have access to each monitored channel, and add @ChatGPT to each channel their task monitors.

For more information, see: [Scheduled tasks in ChatGPT](https://help.openai.com/articles/10291617).

# FAQ

## Why am I being asked to reconnect Slack?

You may be asked to reconnect Slack when ChatGPT needs a Slack OAuth scope that your account has not granted yet. This can happen when your workspace admin enables a new Slack action that requires an additional scope.

If your Slack admin has not approved the required scope, the new action may remain unavailable until approval is complete. Previously available Slack actions should continue working.

## What should admins check if a new Slack action is unavailable?

Check both admin surfaces:

1. In ChatGPT, confirm the Slack app is enabled for the workspace and the action is enabled in **Actions**.
2. In Slack, confirm the ChatGPT Slack app has been approved or reinstalled with the required OAuth scopes, if your Slack workspace requires admin approval.
3. Ask the user to reconnect Slack or retry the new action after approval is complete.

## What if my organization does not want to approve a Slack scope?

Disable every ChatGPT Slack action that requires that scope. Users in your workspace will not be able to use those actions in ChatGPT.

## Can Enterprise admins control who has access to the ChatGPT Slack app?

Enterprise and Edu administrators can use supported role-based access controls to manage which members or groups can use the Slack app.

## Does the ChatGPT Slack app support semantic search?

Yes, when Slack AI Search is enabled for your workspace on a supported Slack Business+ or Enterprise+ plan. Semantic search finds matches by meaning; keyword search is available on all Slack plans. Slack admins can restrict access to AI features.

## Do I need to use the exact channel name when I ask about a channel?

No. Channel matching is fuzzy and works similarly to Slack search. You don’t need the exact name as long as it’s close (for example, “marketing-team” vs. “marketing-teams” is fine). Very broad or unrelated names may not match.

Note: You don’t need to include the # symbol when referring to a channel in your question.

## Can I connect ChatGPT to more than one Slack workspace at a time?

No. The ChatGPT Slack app can connect to only one Slack workspace at a time. To switch workspaces, disconnect the current one, then connect the new workspace.

## Do users have to manually invoke the app in each chat?

No. When the ChatGPT Slack app is enabled and relevant, ChatGPT can automatically use it in your conversation.

## Do I need a paid Slack plan to use the app?

You don’t need a paid Slack plan to use the app, but you do need a paid ChatGPT plan. Without Slack AI Search enabled on a supported Slack Business+ or Enterprise+ workspace, search uses keywords.

## How do Slack retention policies affect what ChatGPT can show?

ChatGPT only accesses Slack content that’s available to you through Slack’s APIs at the time of the request. If messages or files have been deleted or are no longer available due to your Slack retention settings, they won’t appear in ChatGPT.

Tip: If a result seems missing, check your Slack retention policy and channel access.

## How does data residency work with Slack and other apps?

ChatGPT data-residency controls apply to supported, in-scope customer content. Slack is a separate provider, and information sent to Slack is subject to Slack’s own storage, retention, privacy, and data-residency terms. Review both your ChatGPT workspace configuration and your organization’s Slack policies.

## What’s captured in the Compliance API?

Eligible Enterprise and Edu administrators may review supported conversation and app-activity records through the Compliance Platform when available and configured. Available data depends on administrator permissions and the applicable product.
