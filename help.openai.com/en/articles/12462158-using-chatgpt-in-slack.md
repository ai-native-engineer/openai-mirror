<!-- source: https://help.openai.com/en/articles/12462158-using-chatgpt-in-slack -->

# Using ChatGPT in Slack

Install and use ChatGPT inside Slack, connect the appropriate account, and review workspace permissions and data controls.

Updated: 12 hours ago

The ChatGPT app in Slack lets you use ChatGPT from within an eligible Slack workspace. Conversations started there can also appear in your ChatGPT account, subject to the connected account, workspace settings, and applicable privacy controls.

The app only needs to be installed once per Slack workspace, by an admin or authorized user.

# What you can do

* Draft posts, updates, and replies without leaving Slack.

* Search channels, messages, and files you already have access to. Keyword search is available on all Slack plans. Semantic search (search by meaning) requires Slack AI Search to be enabled for your workspace on a supported Slack Business+ or Enterprise+ plan.

* Connect Slack in ChatGPT: You can not only use ChatGPT within Slack, but also search Slack messages from inside your ChatGPT account. Your chats will appear within your ChatGPT sidebar, so it’s easy to pick up where you left off.
* Summarize long conversations in other channels into notes with owners, action items, and next steps.

You can also connect Slack as a source inside ChatGPT without installing the ChatGPT app in Slack. For that separate experience, see: [Using Slack in ChatGPT](https://help.openai.com/articles/12525822).

Slack is a third-party service. When you enable and use the [ChatGPT Slack app](https://help.openai.com/articles/12525822), relevant requests and data may be transmitted to Slack and handled under Slack’s terms and privacy, retention, and data-residency policies. Review your organization’s Slack policies before enabling or using the app.

# Get started

Installing ChatGPT in Slack can connect Slack with other enabled ChatGPT capabilities. Use multi-factor authentication for Slack accounts that authorize or administer the app. Workspace administrators should review installation permissions, requested scopes, and their organization’s security policies.

## Prerequisites

* Your [Slack workspace must allow](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace) installation of the ChatGPT app for Slack.
* Your Slack plan supports the features required by your organization.
* You have a Plus, Pro, Business, Enterprise, or Edu ChatGPT account.
* In Enterprise and Edu workspaces, Slack must be enabled and your account must have access. To review availability and role-based access controls (RBAC), admins can go to **Admin > Plugins** and select the plugin that includes Slack. Slack is enabled by default for Business workspaces.

Availability depends on your ChatGPT plan, region, Slack workspace, and the ChatGPT app settings enabled for that workspace.

## Install the ChatGPT app in Slack

Go to [**Apps**](https://slack.com/help/articles/360001537467-Guide-to-apps-in-Slack) [in Slack](https://slack.com/help/articles/360001537467-Guide-to-apps-in-Slack) to check whether ChatGPT is already installed in your workspace.

1. Open the [Slack Marketplace](https://slack.com/marketplace), search for ChatGPT, and start the installation.
2. Sign in to your ChatGPT account if prompted.
3. Review the **Add ChatGPT to Slack** screen and select **Continue to Slack**.

You will then be directed to the Slack authentication flow, where you can review and grant the app the required permissions. Depending on your workspace settings, this may require an approval [from a Slack admin](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace).

Before using the app, connect it to your ChatGPT account.

1. Select **Connect ChatGPT**.
2. In ChatGPT, go to **Apps** or **Plugins**, depending on what is available, and select **Slack** or the plugin that includes it.
3. Select **Connect**.

In an Enterprise or Edu workspace, you can connect only if the [Slack app](https://help.openai.com/articles/12525822) is enabled and your account has access. If **Connect** is grayed out, ask your workspace admin to review app availability and access settings.

## Use the ChatGPT app in Slack

After Slack is connected in ChatGPT, you can start using ChatGPT within Slack in a dedicated sidebar. You can find the ChatGPT app in Slack in the list of apps for your Slack workspace, or [add it to the navigation bar](https://slack.com/help/articles/212596808-Adjust-your-sidebar-preferences#customize-the-navigation-bar).

You can ask ChatGPT to summarize thread information, draft and polish your replies, and search for messages and files. You can search across all channels you have access to, or direct ChatGPT to search specific channels by including channel names in your prompt.

Example prompts

* “Summarize the discussions in the engineering-team Slack channel from this week. Provide a concise overview of the main topics and decisions.”
* “Catch me up on everything unread in my Slack threads.”
* “Give me the recent updates from the incident-service-unavailable Slack channel, including a summary of the root cause behind the incident.”
* “Create a one-page meeting brief with key points discussed in the Marketing channel this week. Include action items.”

Chats you start in the ChatGPT app for Slack will also appear in your ChatGPT sidebar on web or mobile, so you can pick up where you left off. If you continue the conversation in ChatGPT, those chat updates are not synced to Slack and do not appear in the ChatGPT app for Slack.

You can also search apps enabled for your ChatGPT account. For an overview, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

## Deletion and data controls

You can view all conversations you started from the ChatGPT app for Slack in both your Slack account and ChatGPT account, and can [delete them](https://help.openai.com/articles/8809935) from your ChatGPT account.

Deleting a chat removes it from your ChatGPT sidebar, but the chat may be retained in Slack for a period specified by your Slack workspace settings. Contact your Slack admin to learn about [retention policies](https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack). A chat you deleted from ChatGPT may continue to be visible in the ChatGPT app for Slack for the duration of the retention period, but can no longer be continued.

You can disconnect your ChatGPT account from Slack at any time. Go to **Settings**, select **Apps** or **Plugins**, select Slack, and select **Disconnect**. You will no longer be able to initiate chats from the ChatGPT app in Slack.

Disconnecting your ChatGPT account from Slack will not automatically delete the copy of your Slack conversations in your ChatGPT conversation history. You can choose to [delete them](https://help.openai.com/articles/8809935) from within your ChatGPT account after disconnection. Additionally, your chat history is maintained in the ChatGPT app for Slack, and may be cleared after a period of time, based on your [Slack retention policy](https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack).

To reconnect Slack, go to **Settings**, select **Apps** or **Plugins**, select Slack, and follow the connection prompts.

## Privacy and security

ChatGPT respects Slack’s existing permissions — only the messages and files you already have access to in Slack are searchable.

Chats from the ChatGPT app for Slack do not write memories if you have memories enabled in your ChatGPT settings. Data sent from your ChatGPT account to Slack includes model responses to your prompts, which may incorporate previously saved memories (if enabled).

Chats you start in the ChatGPT app for Slack cannot be viewed, modified, or deleted by other users on Slack.

Eligible Enterprise and Edu administrators may access supported conversation records through the Compliance Platform when it is available and configured. For details, see the Compliance API section below.

ChatGPT can make mistakes.

## Limitations

* Heavy usage may exhaust your per-user Slack API quota even if workspace-wide limits are not reached.

In Enterprise and Edu workspaces, Slack must be enabled for your workspace and available to your account. If Slack is unavailable, ask an admin to check the plugin that includes it in **Admin > Plugins** and review any role or group access restrictions. For an overview, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

## Compliance API

Eligible Enterprise and Edu administrators can review supported conversations and app activity through the Compliance Platform when available. For workspace controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# FAQ

## How do I find the ChatGPT app for Slack?

You can find it by searching for ChatGPT in the [Slack Marketplace](https://slack.com/marketplace). Note that your Slack admin must support installation of the app, and may have access control restrictions.

## Do I need to be signed into ChatGPT while using the ChatGPT app for Slack?

After setting up the ChatGPT app for Slack and enabling the connection in ChatGPT, you do not need to be signed into ChatGPT to use it in Slack.

## Can I connect my ChatGPT account to multiple Slack workspaces?

You can connect to one Slack workspace at a time. To switch workspaces, go to **Settings**, select **Apps** or **Plugins**, disconnect the current Slack workspace, and connect the other workspace.

## How do I search for messages or files?

Both the ChatGPT app in Slack and the Slack app in ChatGPT support keyword search on all Slack plans. Semantic search (search by meaning) requires Slack AI Search to be enabled for your workspace on a supported Slack Business+ or Enterprise+ plan. Your Slack admin can restrict access to AI features.

## Do I need to use the exact channel name when I ask about a channel?

No. Channel matching is fuzzy and works similarly to Slack search. You don’t need the exact name as long as it’s close (for example, “marketing-team” vs. “marketing-teams” is fine). Very broad or unrelated names may not match.

Note: You don’t need to include the # symbol when referring to a channel in your question.

## How do I disconnect my ChatGPT account from Slack, and what happens to the ChatGPT app for Slack after I disconnect?

To disconnect your ChatGPT account from Slack, go to **Settings**, select **Apps** or **Plugins**, select Slack, and select **Disconnect**. After disconnection, you cannot use the ChatGPT app in Slack or retrieve Slack information through that connection until you reconnect. You can still review previous chats in your ChatGPT account or in the Slack app, subject to your Slack workspace’s message-retention policy.

You can also [remove the ChatGPT app from Slack](https://slack.com/help/articles/360003125231-Remove-apps-and-custom-integrations-from-your-workspace) if authorized.

## How do chats started from the ChatGPT app for Slack appear in my ChatGPT account? How do I delete them?

Chats started in the ChatGPT app for Slack appear as regular conversations in your ChatGPT sidebar. To delete a chat, use the more options menu (•••) that appears when you hover over it.

## Do regular ChatGPT capabilities (web search, connected apps) work in the ChatGPT app for Slack?

You can use ChatGPT web search and other apps (if enabled in your ChatGPT account) within the ChatGPT app for Slack. Deep research, agent mode, and model switching are not available.

## Why doesn’t the chat in the ChatGPT app for Slack update after I continue the conversation in ChatGPT?

Chat updates from your ChatGPT account are not synced to Slack and will not appear in the ChatGPT app for Slack.

## How do memories work with the ChatGPT app for Slack?

Your ChatGPT memories may be incorporated in model responses that are shared with the ChatGPT app for Slack if you have memories turned on in your ChatGPT settings. New memories are not saved based on chats from the ChatGPT app for Slack, even if you continue them within your ChatGPT account.

## How does data residency work?

Applicable ChatGPT data residency commitments cover eligible in-scope ChatGPT content. Information sent to Slack is also subject to Slack’s own data residency and retention policies.

# Troubleshoot the ChatGPT app in Slack

## Resolve an app configuration error

To fix this message, follow these steps:

1. In Slack, open the ChatGPT app’s **About** tab and identify the Slack workspace authorized to use the app. If you cannot identify the correct workspace, ask your Slack administrator.
2. Select **Connect ChatGPT** in Slack, then follow the current authorization flow shown for your ChatGPT account and Slack workspace.
3. If Slack is connected to the wrong workspace, select **Disconnect**, then select **Connect** and follow the current authorization flow. Review any warning before disconnecting an existing account.
4. On the Slack authorization screen, select the workspace where ChatGPT is installed and approved. If you are unsure which workspace to select, ask your Slack administrator. Review the requested permissions and select **Allow**.
5. Return to ChatGPT after authorization, then send a message to the ChatGPT app in Slack to confirm the connection works.

If the issue continues, confirm that Slack and ChatGPT are connected to the same authorized workspace, then contact your Slack administrator or OpenAI Support.
