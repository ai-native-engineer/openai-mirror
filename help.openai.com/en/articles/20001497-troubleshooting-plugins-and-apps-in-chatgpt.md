<!-- source: https://help.openai.com/en/articles/20001497-troubleshooting-plugins-and-apps-in-chatgpt -->

# Troubleshooting plugins and apps in ChatGPT

Resolve problems with app availability, connected accounts, provider permissions, workspace restrictions, and supported actions.

Updated: 10 days ago

Start with the section that matches the problem: finding an app, connecting an account, starting an app request, finding a result, reading its contents, or completing an action. A successful connection does not mean every later step will work.

## Availability

Apps can vary by plan, region, workspace, role, selected model, product surface, and provider requirements.

Support in voice conversations varies by app and available features. If an app is unavailable in voice, try a supported text conversation.

# An app or connection setting is missing

If you cannot find an app or its connection controls:

1. Open **Apps** or **Plugins**, depending on the options shown for your account, and look for the app you need.
2. Confirm the plugin is installed if installation is required.
3. Review the app's plan, region, account, and surface requirements.
4. Check that you are using the intended ChatGPT account or workspace.
5. Open **Settings**, select **Apps** or **Plugins**, and select the relevant app or plugin.
6. If the app is not visible, check the other supported **Apps** or **Plugins** entry point when it appears for your account.

A listed plugin might not be installed, and an installed plugin may include an app that is disabled, disconnected, or missing provider authorization. Open the plugin details and refresh before treating a directory status as definitive. For help with installation, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

# A plugin view or event-triggered task is unavailable

Finding or installing a plugin does not mean that every included feature works on your current surface. Review the plugin’s description and the requirements for the specific app, view, or task you want to use.

On Free and Go accounts, you can discover plugins through the directory and recommendations, but plugin extensions are not available to these plans.

For an event-triggered task, check that the app and event are supported, the intended account is connected and authorized, and your plan and workspace allow the task. In **Scheduled**, check whether the task is paused or waiting for approval. See: [Scheduled tasks in ChatGPT](https://help.openai.com/articles/10291617).

Scheduled tasks can use supported connected apps to read information or take actions according to the applicable permissions. An action that sends a message or changes external data may require approval. If approval is required, the task pauses until you review it.

Workspace Agents use separate agent-level action-safety settings. For an agent run, review its configured app connections, authentication type, write approvals, any action constraints, and the applicable workspace policies. See: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).

A missing event option does not by itself mean installation failed. Avoid repeatedly reinstalling or reconnecting a plugin when the feature is unavailable on your account or surface.

If ChatGPT cannot use tools provided by a webpage, check the browser, current page, and signed-in website session. These site tools are separate from installed plugins. For availability and browser checks, see: [Using site tools in the ChatGPT desktop app](https://help.openai.com/articles/20001423).

# An app shows an availability message

Different messages require different next steps:

* **Not available on your plan**: Check the app's plan requirements.
* **Admin approval required**: Ask your workspace administrator to review the plugin and its included app. This message does not mean a request was already submitted.
* **Requires workspace setup**: Ask a workspace administrator to configure the app.
* **Requires a workspace**: Switch to an eligible managed workspace if you have one.
* **Desktop only** or **Open in desktop app**: Use the supported desktop experience.

# A plugin shows Disabled by admin

A plugin can remain listed in the directory even when its access is restricted. Seeing the plugin does not mean its included apps are available to you.

Ask a workspace owner or administrator to review the plugin in [Admin console](https://admin.openai.com). In Enterprise and Edu, review the workspace default and your assigned custom roles. In Business, review workspace-wide availability.

The administrator should check each required app separately. Changing plugin access does not automatically grant app access, change allowed actions, or complete provider authorization.

For administration steps, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# Bulk plugin changes did not apply as expected

If you manage several plugins together, review each plugin's result before repeating the change.

1. Confirm that you selected the intended workspace and plugins in [Admin console](https://admin.openai.com).
2. Check whether you changed **Workspace default** or a custom role. Role-specific controls require a workspace with role-based access control enabled.
3. Review each affected plugin's saved availability. A result for one plugin does not establish that all selected plugins changed.
4. If a result is unclear, verify its saved setting before retrying. Avoid repeating changes that already succeeded.
5. If access still does not match the saved settings, check the affected user's role and any required app's access and provider authorization.

If the issue continues, [contact OpenAI Support](https://help.openai.com/articles/6614161). Include the workspace, affected plugin names, intended setting, selected role or workspace default, time of the change, and any error or result shown. Do not include passwords, tokens, or other secrets.

For the bulk-management steps, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# An app shows Disabled by admin

In a managed workspace, ask an administrator to open Workspace settings > Apps and review the app. To review its plugin, go to [Admin console](https://admin.openai.com), select the intended ChatGPT workspace, open **Plugins**, and review the app and its plugin. For workspace navigation and app access, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

In Enterprise or Edu, ask the administrator to check role-based access when applicable. In Business, ask whether the app is enabled for the workspace.

If you use a personal account and do not have a workspace administrator, a **Disabled by admin** message does not by itself establish that an administrator blocked the app. Check your plan, region, provider account, app version, and product surface. If the message continues after those checks, contact OpenAI Support.

## You are the workspace owner or administrator

If you are already the owner or an administrator, review the app, its plugin, and any role-based access settings available to your workspace. Go to [Admin console](https://admin.openai.com), select the intended ChatGPT workspace, and open **Plugins**. Select **Manage Legacy Apps** to open the **Apps** page.

If you have the required Sites and plugin permissions but creating a plugin for a Site you own fails on the web, first check whether publishing already created the plugin. If it did not, try the same workflow in the latest ChatGPT desktop app, using the same Site, account, and workspace.

Include your workspace, your role, the exact message, and a screenshot showing the missing or inconsistent control. If the app is unavailable before you start a conversation, describe that state; file or conversation details may not apply.

For administrator guidance, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# An app will not connect or authorize

Check that you:

* Selected the intended provider account.
* Can access the relevant information directly in the provider's service.
* Granted all permissions required for the services you selected.
* Meet any workspace-approved account-domain requirements.
* Received any separate approval required from the provider's administrator.

If you see **All permissions are required**, select **Reconnect** and approve every permission required for the apps you selected.

If you see **ChatGPT needs all requested permissions** when connecting Google apps, select **Try again**. On Google’s authorization screen, select **Select all** to approve the requested permissions.

To connect fewer Google apps, select **Select fewer apps** in ChatGPT and choose the apps you want. You must still approve every requested permission for the selected apps.

Your ChatGPT workspace administrator and the provider's administrator may be different people.

For connection and account-selection steps, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

For Google-specific authorization rules, see: [Google app data controls FAQ](https://help.openai.com/articles/10408842).

## An iCloud connection fails

For iCloud Mail or Calendar, enter an Apple app-specific password in the connection form. Mail requires your iCloud Mail address ending in @icloud.com, @me.com, or @mac.com. Calendar requires your primary Apple Account email address, which may differ. If Mail rejects your email address, check that you entered your iCloud Mail address. Do not enter your regular Apple password or share either password in a chat or support request.

Password rejected: Check the intended Apple account and whether its app-specific password was revoked. If needed, generate a replacement using Apple's instructions, then reconnect the affected Mail or Calendar connection.

Temporarily unavailable: A service error does not by itself show that your password is invalid. Note the error and try later; contact support if it continues.

A search is incomplete or an item is forbidden: Check the connected account, source access, and search terms before replacing a credential. Try a narrower calendar date range or a more specific contact name or email address.

If an iCloud send or calendar edit has an unclear result, follow An action stops or its result is unclear below before retrying. Inspect the affected message, event, or recurring series in the intended Apple account.

# An app is connected, but ChatGPT cannot use it

An app can appear as **Connected** without being available in the current chat, model, or ChatGPT surface.

1. Confirm that you are using the intended ChatGPT workspace and connected provider account.
2. Review the app’s availability and requirements for the selected model and surface.
3. Start a new chat. Use the app controls available in your interface and ask for a specific, supported task, such as finding a document by its title.

If app controls are still missing, ChatGPT does not use the app, or the problem continues after the relevant authorization checks, do not keep reconnecting it. Check [OpenAI service status](https://status.openai.com/) and [contact OpenAI Support](https://help.openai.com/articles/6614161) with the steps you tried and the state you observed.

For connection and app-use instructions, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# An app cannot find expected information

For apps that require individual authorization, confirm that the intended provider account is connected. If the app supports multiple accounts, you may need to specify the account in your request.

Check the source permissions for the missing information. Connecting an app does not create additional source-system permissions. Your workspace administrator may also restrict which content an app can access.

For provider-specific setup and access requirements, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

# A file is found, but its contents cannot be used

Finding a filename or other file details does not mean ChatGPT retrieved the file’s contents or can analyze them for your requested task. For example, an app may find a video in a connected service without being able to analyze it.

Check the app’s supported file types and capabilities for the feature you are using. If the task requires a different supported format, use an appropriate export or transcript only when you have permission to share it.

If you choose to upload a file separately, see: [File Uploads FAQ](https://help.openai.com/articles/8555545). Upload requirements are separate from the capabilities and limits of connected apps.

# An app cannot complete an action

A connected app may be able to read information without being able to create, edit, send, or delete it. Use the exact message to choose the next step:

* **Authorization or access error:** Check the intended connected account, provider permissions, and any required provider-admin consent. For connection checks, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).
* **Action unavailable:** Check whether the app supports the requested action and whether your workspace allows it. Permission to read information does not establish permission to change it.
* **Approval required or pending:** Review the current approval prompt, including the app, account, and proposed action. For a scheduled task, check **Scheduled** for a pending approval.
* **Explicit safety block:** Some requests are denied without showing an approval prompt. Changing app permissions, reconnecting an account, or having a saved approval does not override safety protections.

App permissions do not override provider authorization or workspace restrictions. A missing approval prompt alone does not identify the cause of a failed request.

For action approvals, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

If a custom MCP app is missing new tools or starts returning errors after a tool’s definition changes, your workspace may still be using the previously approved tool list. Business, Enterprise, and Edu admins can refresh the existing app’s tool list from workspace app settings without recreating it. The admin must have permission to manage the app and a valid connection to it. For refresh and review instructions, see: [Connecting custom MCP servers in ChatGPT](https://help.openai.com/articles/12584461).

If OpenAI Developers can't finish API key setup for a Site you own, you can add an API Platform key directly in the Site's environment settings. Your workspace must allow the connection, and you must be authorized to use the key. Save it as a secret using the variable name your Site expects. Keep the key out of chats, source code, and site content. Follow the instructions shown in the Site's settings to apply the change, including publishing when required. For details, see: [Creating and using ChatGPT Sites](https://help.openai.com/articles/20001339).

# An action stops or its result is unclear

Check the destination in the intended provider account before trying again. Confirm which changes completed, which partly completed, and which you cannot confirm.

* Before resending an email or message, check the intended account’s sent messages and the destination.
* Before repeating a file or record change, inspect the affected item’s current contents or status.
* For a request involving several items, identify which items changed before repeating the remaining work.

Retry only work you have confirmed is still needed. If you cannot determine the outcome, stop and contact OpenAI Support with the changes you observed and the results you could not confirm.

If the message says that an approval expired or a request was cancelled, check the destination before making a fresh request for any confirmed remaining work. Review any new approval prompt. If you did not cancel the request, include that detail in your support request.

# ChatGPT asks for approval unexpectedly

First identify what the prompt is asking you to approve:

* **Account authorization** connects a provider account and grants the requested provider permissions. App permission settings do not replace this authorization.
* **Action approval** asks whether ChatGPT may perform the proposed operation. Review the app, connected account, and action before approving it.
* **Cloud-browser website permission** controls access to a website. It is separate from confirmation for a consequential action. Allowing a website does not remove that confirmation.

Use the exact message to distinguish an account-authorization problem from an action-approval problem. For browser permissions, see: [Using cloud browser in ChatGPT](https://help.openai.com/articles/20001280).

On an eligible personal account, open **Settings**, select **Apps** or **Plugins**, and review the available **Permissions** settings.

**Allow low-risk actions** applies when no account, workspace, app, or connection policy overrides it. Higher-risk actions may require confirmation or be denied.

An app or individual connected account can have a different permission setting. Managed-workspace members may receive one-time or conversation-specific approval prompts based on workspace policies.

For all current permission options, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

# Lockdown Mode blocks an app

Lockdown Mode can restrict apps that need live access to an external service.

Review the message shown for the current conversation. Do not turn off a security protection unless you understand the effect and are allowed to change that setting.

# An app reaches a usage limit

App use may count toward your ChatGPT plan limits, feature-specific allowances such as deep research, and limits imposed by the provider.

Review the relevant ChatGPT feature limit and any provider message before retrying.

# You cannot find the disconnect option

1. Open **Settings**.
2. Select **Apps** or **Plugins**, depending on what is available, and open the app.
3. If **Connected accounts** appears, use the relevant account’s more options menu (•••). Otherwise, review **Connection** or the app’s more options menu (•••).

Disconnecting one account does not necessarily remove other connected accounts. Disconnecting the last account can uninstall some associated plugins, while uninstalling a plugin can disconnect all linked accounts.

For disconnection and data-retention details, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494) and [Chat and file retention in ChatGPT](https://help.openai.com/articles/8983778).

# A previously synced app is unavailable

App sync, including administrator-managed sync, is no longer available. An old sync connection cannot be reconnected, restored, or upgraded.

The former synced integrations for Aha!, Azure Boards, Basecamp, Help Scout, Pipedrive, Teamwork, Zoho CRM, and Zoho Desk are no longer supported.

Other providers may still offer supported live apps even though their former sync option is retired. Review the current app details instead of following an old sync setup guide.

If you previously used a synced app, check which options are still supported:

* Open **Apps** or **Plugins**, depending on the interface shown for your account, and look for the provider.
* If a current app is available, connect your provider account for supported live access.
* If the provider no longer offers a supported integration, the retired synced connection cannot be reactivated.

For provider account setup, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Contact OpenAI Support

If the relevant checks above do not resolve the issue, stop repeating the same connection, permission, or approval changes. Include the following in your support request:

* The app and plugin name.
* The affected account or workspace and the intended connected provider account.
* The exact message shown.
* Whether the request ran in a chat, a scheduled task, or a Workspace Agent.
* The selected model and ChatGPT app or interface.
* The steps you tried and what happened after each step.
* Any changes you confirmed in the destination, including partially completed work, and any results you could not confirm.
* The date, time, and time zone of the attempt.
* Any request, run, or diagnostic ID shown. If no ID is shown, write “not shown.”
* A screenshot with sensitive information removed.

For contact instructions, see: [How can I contact support?](https://help.openai.com/articles/6614161) Do not include passwords, access tokens, or sensitive conversation content in your support request.
