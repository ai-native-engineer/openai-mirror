<!-- source: https://help.openai.com/en/articles/12525822-chatgpt-slack-app -->

# ChatGPT Slack app

Connect Slack to ChatGPT to search messages, reference permitted workspace content, and use available Slack actions.

## Overview

The ChatGPT Slack app (formerly connector) enables ChatGPT users and workspace members to securely search and ask questions across their Slack messages, threads, and channels. Connections can be created, deleted, or modified at any time. Once enabled, ChatGPT will automatically reference your Slack content when relevant.

Where available and enabled by a workspace admin, the ChatGPT Slack app can also take Slack actions on a user's behalf, such as joining a channel, creating a reminder, uploading a file, or updating the user's Slack profile.

See: [Apps in ChatGPT](https://help.openai.com/articles/11487775) for more information.

**Type:** app with search and actions

**Where you can use it:** Chat, deep research, and agent mode.

**Note:** The ChatGPT Slack app is not currently available to Plus and Pro users in the European Economic Area (EEA), Great Britain (GB) and Switzerland (CH). Business and Enterprise users are not affected.

*Slack is a third-party service. When you enable and use the ChatGPT Slack app, relevant requests and data may be transmitted to Slack and handled under Slack’s terms and privacy, retention, and data-residency policies. Review your organization’s Slack policies before enabling or using the app.*

**Example prompts**

* “Summarize the discussions in the #engineering-team Slack channel from this week. Provide a concise overview of the main topics and decisions.”
* “Catch me up on everything unread in my Slack threads.”
* “Give me the recent updates from the #incident-service-unavailable Slack channel, including a summary of the root cause behind the incident.”
* “Create a one-page meeting brief with key points discussed in the #Marketing channel this week. Include action items.”

*Note: To use ChatGPT inside Slack, install* [*the ChatGPT app for Slack*](/en/articles/12462158)*. The ChatGPT connector for Slack is required to use this functionality.*

# Capabilities and Permissions

## What it can access

* Slack conversations, threads, and channels you have access to.

## What it can do

* Summarize discussions and pull insights from Slack channels and DMs.
* Search channels and DMs by keyword (all Slack plans) or semantic search (for Slack Business+ and Slack Enterprise+ customers with AI plans only).
* Create recaps or briefs based on information scattered across a channel.
* Where enabled by a workspace admin, take Slack actions on a user's behalf, such as joining a channel, creating a reminder, uploading a file, or updating the user's Slack profile.

**Permissions requested:**

* [Methods](https://docs.slack.dev/reference/methods)

* [Scopes](https://docs.slack.dev/reference/scopes/)

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

* Inviting users to conversations: **channels:write.invites**, **groups:write.invites**, and related conversation write scopes.
* Joining or leaving conversations: **channels:write**, **groups:write**, **im:write**, and **mpim:write**.
* Creating reminders: **reminders:write**.
* Uploading files to Slack: **files:write**.
* Listing starred items: **stars:read**.
* Listing user groups: **usergroups:read**.
* Listing conversations visible to the user: **channels:read**, **groups:read**, **im:read**, and **mpim:read**.
* Updating a Slack profile: **users.profile:write**.

**Known limitations**

* Use with deep research, Pro models, or agent mode may exhaust your per-user Slack API limits quota even if workspace-wide limits are not reached.
* Enterprise/Edu owners and admins must enable the ChatGPT Slack app and enable access for users or groups through role-based access controls (RBAC), where available, in their [ChatGPT workspace admin settings](https://chatgpt.com/admin/ca).
* If your organization requires Slack admin approval for app scopes, a Slack admin may need to approve or reinstall the updated ChatGPT Slack app before users can grant additional scopes for newly enabled Slack actions.

## Business / Enterprise / Edu workspace setup

Business, Enterprise, and Edu workspace owners and admins can manage the Slack app from **Workspace settings > Apps**.

For Business workspaces, the Slack app is enabled by default. Admins should review **Action control** for Slack and disable any action whose required Slack scope they do not want to approve.

For Enterprise and Edu workspaces, admins must enable Slack from the app directory before members can connect it. During setup or later management, admins can:

1. Select **App details** to review the Slack app.
2. Select **User access** to configure role-based access controls, where available.
3. Select **Action control** to review which Slack actions are available for the workspace.
4. Disable any action that requires a Slack OAuth scope your organization does not want to approve.
5. Select **Manage domains** if you want to limit which Slack accounts workspace members can connect.

If your organization uses Slack Enterprise Grid or requires admin approval for app scopes, coordinate with a Slack admin before enabling new Slack actions in ChatGPT.

Once Slack is enabled in ChatGPT and approved in Slack where required, each user can connect their individual account by signing in to Slack through an OAuth flow. See instructions below.

## Individual Setup

ChatGPT Plus, Pro, Business and Enterprise/Edu users can enable access to the ChatGPT Slack app in their account's [settings](https://chatgpt.com/#settings/Connectors) - browse the [app directory](/en/articles/11487775-apps-in-chatgpt) select the **Slack** entry, and click **Connect**. Follow through the OAuth flow, selecting the appropriate Slack workspace as required.

Note that the ChatGPT Slack app can only connect to one Slack workspace at a time.

# FAQ

## Why am I being asked to reconnect Slack?

You may be asked to reconnect Slack when ChatGPT needs a Slack OAuth scope that your account has not granted yet. This can happen when your workspace admin enables a new Slack action that requires an additional scope.

If your Slack admin has not approved the required scope, the new action may remain unavailable until approval is complete. Previously available Slack actions should continue working.

## What should admins check if a new Slack action is unavailable?

Check both admin surfaces:

1. In ChatGPT, confirm the Slack app is enabled for the workspace and the action is enabled in **Action control**.
2. In Slack, confirm the ChatGPT Slack app has been approved or reinstalled with the required OAuth scopes, if your Slack workspace requires admin approval.
3. Ask the user to reconnect Slack or retry the new action after approval is complete.

## What if my organization does not want to approve a Slack scope?

Disable every ChatGPT Slack action that requires that scope. Users in your workspace will not be able to use those actions in ChatGPT.

## Can Enterprise admins control who has access to the ChatGPT Slack app?

Enterprise admins [can further configure access to users settings with RBAC.](/en/articles/11750701-rbac)

## Does the ChatGPT Slack app support semantic search?

Yes. Both keyword and semantic search (search by meaning) are supported, depending on Slack plan type. All plans have access to keyword search, while semantic search is only available to customers on Slack Business+ or Slack Enterprise+ plans.

## Do I need to use the exact channel name when I ask about a channel?

No. Channel matching is fuzzy and works similarly to Slack search. You don’t need the exact name as long as it’s close (for example, “marketing-team” vs. “marketing-teams” is fine). Very broad or unrelated names may not match.

**Note:** You don’t need to include the # symbol when referring to a channel in your question.

## Can I connect ChatGPT to more than one Slack workspace at a time?

No. The ChatGPT Slack app is 1:1. To connect a different Slack workspace, first disconnect the current one, then connect the new workspace.

## Do users have to manually invoke the app in each chat?

No. When the ChatGPT Slack app is enabled and relevant, ChatGPT can automatically use it in your conversation.

## Do I need a paid Slack plan to use the app?

You don’t need a paid Slack plan to use the app, but you do need a paid ChatGPT plan. If your Slack workspace isn’t on a Slack Business+ or Enterprise+ plan, search will default to keyword search.

## How do Slack retention policies affect what ChatGPT can show?

ChatGPT only accesses Slack content that’s available to you through Slack’s APIs at the time of the request. If messages or files have been deleted or are no longer available due to your Slack retention settings, they won’t appear in ChatGPT.

**Tip:** If a result seems missing, check your Slack retention policy and channel access.

## How does data residency work with Slack and other apps?

Search and deep research apps are compatible with OpenAI data residency. However, connected applications (like Slack) are third-party services. Data sent to a connected app is subject to that app’s own data residency and retention policies. For example, if your organization has Data Residency in Europe, OpenAI limits storage of Customer Content to Europe up to the point where your query is sent to the connected app. Ensure your connected apps also meet your residency requirements.

## What’s captured in the Compliance API?

User conversations—including those that use apps—are available through the Compliance API. Additionally, all app calls are logged as a part of the [OpenAI Compliance Logs platform](https://chatgpt.com/public/admin/api-reference#tag/Logs:-Apps).
