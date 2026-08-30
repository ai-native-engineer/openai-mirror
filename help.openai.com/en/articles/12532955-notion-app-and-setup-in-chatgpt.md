<!-- source: https://help.openai.com/en/articles/12532955-notion-app-and-setup-in-chatgpt -->

# Notion app and setup in ChatGPT

Connect Notion to ChatGPT to search authorized pages, manage access, and troubleshoot workspace permissions.

The Notion app lets ChatGPT search and read content from Notion pages that your connected account is allowed to access. You can ask questions about project notes, planning documents, team guides, and other authorized Notion content.

Notion does not support individual sync. Older instructions for keeping an existing Notion sync connection active no longer apply.

Availability depends on your ChatGPT plan, workspace configuration, and Notion account permissions.

For an overview of connected apps, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

# Connect Notion to ChatGPT

1. Open **Apps** or **Plugins**, depending on which option appears for your account.
2. Find and select **Notion**.
3. Select **Connect**. If Notion is listed as a plugin instead, select **Install plugin** and complete the connection prompt when it appears.
4. Sign in to the Notion account you want to use.
5. Review the Notion workspace and content included in the authorization request, then approve the connection.

If you use multiple Notion workspaces, check that you authorize the account and workspace that contain the pages you need.

For general connection instructions, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Search Notion pages in a conversation

After connecting Notion, ask ChatGPT to find, summarize, or compare information in your authorized Notion content.

For example:

* “Summarize the decisions in our Q3 planning pages.”
* “Find the onboarding guide in Notion and list the steps for a new team member.”
* “Compare the project notes from this month and identify unresolved questions.”
* “Find references to our launch timeline across the Notion pages I can access.”

Include a page title, project name, workspace, or specific subject when you can. If ChatGPT cannot find a page, first confirm that the connected Notion account has access to it.

You do not need to set up individual sync or wait for an initial sync to finish.

# Understand Notion permissions

Connecting Notion does not give ChatGPT access to every page in your organization. Access depends on the Notion account you connect, the workspace and content authorized for the app, and the permissions already granted in Notion.

A page can be missing when:

* You connected a different Notion account.
* The page belongs to another Notion workspace.
* The page has not been shared with the connected account.
* The app was not authorized to access the relevant content.
* Your ChatGPT workspace administrator has restricted the app or your role.

If access changes, review the relevant permissions in Notion and reconnect the app when needed. A ChatGPT workspace administrator can make the app available, but cannot grant access to a Notion page that your Notion account is not allowed to view.

For details about account authorization, app approvals, and workspace restrictions, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

For information about data shared with connected apps, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

# Disconnect or change your Notion connection

To stop using the connected account, open **Apps** or **Plugins**, select **Notion**, and use the available disconnect option.

If you use Notion through a plugin, open its settings and use the available uninstall or connection-management option. To remove Notion account authorization too, review your connected apps separately.

To connect another Notion account or workspace, disconnect the existing account and complete the authorization process again.

# Troubleshoot Notion access

## Notion is missing or unavailable

Confirm that Notion is available for your plan. In a managed workspace, also check that an administrator has enabled it for your role. If you use plugins, look for Notion in the **Plugin directory**.

## A Notion page is not appearing

Open the page in Notion using the same account you connected to ChatGPT. Check that the page is in the authorized workspace and that the account has permission to view it.

If the page is private, restricted, or in a different workspace, ask the page owner or Notion administrator to review access. Reconnect if your authorization needs to be updated.

## Notion asks for authorization again

Reconnect the app and review the current request. If a workplace policy or administrator setting prevents access, contact the relevant Notion or ChatGPT workspace administrator.

For additional help, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

# FAQ

## Does Notion support individual sync?

No. The current Notion app uses authorized access to available Notion content. Individual sync and previously configured individual sync connections are no longer available.

## Can ChatGPT read every page in my Notion workspace?

No. ChatGPT can use only content available to the connected Notion account and authorized for the app. Private pages and pages outside that account’s access remain unavailable.

## Can a workspace administrator give ChatGPT access to private Notion pages?

No. A ChatGPT workspace administrator can manage app availability and role access, but Notion page permissions still determine which content the connected account can access.

## Can ChatGPT create or edit Notion pages?

ChatGPT may be able to create or update Notion pages, depending on the app or plugin, your connected account’s permissions, workspace settings, and required approvals. Available actions can differ across experiences.

Support for page or database actions does not mean every Notion feature is available in ChatGPT. For example, applying an existing template to a page is different from configuring a repeating template, native automation, or button.

Check whether the action is offered by your current connection before changing permissions or reconnecting. If it is not supported, configure that feature directly in Notion. For Notion MCP’s current capabilities, see: [Notion’s supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools).
