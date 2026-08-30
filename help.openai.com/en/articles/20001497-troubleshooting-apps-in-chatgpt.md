<!-- source: https://help.openai.com/en/articles/20001497-troubleshooting-apps-in-chatgpt -->

# Troubleshooting apps in ChatGPT

Resolve problems with app availability, connected accounts, provider permissions, workspace restrictions, and supported actions.

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

# An app shows an availability message

Different messages require different next steps:

* **Not available on your plan**: Check the app's plan requirements.
* **Admin approval required**: Ask your workspace administrator to review the plugin and its included app. This message does not mean a request was already submitted.
* **Requires workspace setup**: Ask a workspace administrator to configure the app.
* **Requires a workspace**: Switch to an eligible managed workspace if you have one.
* **Synced by admin**: The app may be available through an administrator-managed sync connection rather than your own provider account.
* **Desktop only** or **Open in desktop app**: Use the supported desktop experience.

## Administrator-managed sync controls are missing

Ask a workspace owner or administrator to check your plan, supported provider, and configured data residency region. An available live app connection does not necessarily include sync. Individually authorized sync is no longer available.

For supported providers and sync setup regions, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

For instructions to find your workspace’s configured region, see: [Data residency and inference residency for ChatGPT](https://help.openai.com/articles/9903489).

# An app shows Disabled by admin

In a managed workspace, ask an administrator to open **Workspace settings**, select **Apps** or **Plugins** as available, and review the app and its plugin.

In Enterprise or Edu, ask the administrator to check role-based access when applicable. In Business, ask whether the app is enabled for the workspace.

If you use a personal account and do not have a workspace administrator, a **Disabled by admin** message does not by itself establish that an administrator blocked the app. Check your plan, region, provider account, app version, and product surface. If the message continues after those checks, contact OpenAI Support.

## You are the workspace owner or administrator

If you are already the owner or an administrator, review the app, its plugin, and any role-based access settings available to your workspace. If the app or its controls are missing, or the settings do not match the message shown, [contact OpenAI Support](https://help.openai.com/articles/6614161).

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

# An app is connected, but ChatGPT cannot use it

An app can appear as **Connected** without being available in the current chat, model, or ChatGPT surface.

1. Confirm that you are using the intended ChatGPT workspace and connected provider account.
2. Review the app’s availability and requirements for the selected model and surface.
3. Start a new chat. Use the app controls available in your interface and ask for a specific, supported task, such as finding a document by its title.

If app controls are still missing, ChatGPT does not use the app, or the problem continues after the relevant authorization checks, do not keep reconnecting it. Check [OpenAI service status](https://status.openai.com/) and [contact OpenAI Support](https://help.openai.com/articles/6614161) with the steps you tried and the state you observed.

For connection and app-use instructions, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# An app cannot find expected information

* For apps that require individual authorization, confirm that the intended provider account is connected. If the app supports multiple accounts, you may need to specify the account in your request.
* For administrator-managed sync, confirm that your workspace has configured the source.

Check whether the relevant provider account or administrator-managed source grants you access to the missing information. Connecting an app does not create additional source-system permissions.

If the app uses sync, the initial index may still be in progress or the content may fall outside the configured sync scope.

For sync status and source limitations, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

# A file is found, but its contents cannot be used

Finding a filename or other file details does not mean ChatGPT retrieved the file’s contents or can analyze them for your requested task. For example, an app may find a video in a connected service without being able to analyze it.

Check the app’s supported file types and capabilities for the feature you are using. If the task requires a different supported format, use an appropriate export or transcript only when you have permission to share it.

If you choose to upload a file separately, see: [File Uploads FAQ](https://help.openai.com/articles/8555545). Upload requirements are separate from the capabilities and limits of connected apps.

# An app cannot complete an action

A connected app may be able to read information without being able to create, edit, send, or delete it.

Check whether:

* The app supports the action.
* The connected account has permission to perform it.
* The provider approved the required authorization scope.
* A workspace administrator allows the action.
* ChatGPT is waiting for your approval.
* A safety protection blocked the request.

App permissions do not override provider authorization, workspace restrictions, or safety protections.

For action approvals, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

# ChatGPT asks for approval unexpectedly

On an eligible personal account, open **Settings**, select **Apps** or **Plugins**, and review the available **Permissions** settings.

**Allow low-risk actions** applies when no account, workspace, app, or connection policy overrides it. Higher-risk actions may require confirmation or be denied.

An app or individual connected account can have a different permission setting. Managed-workspace members may receive one-time or conversation-specific approval prompts based on workspace policies.

For all current permission options, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

# Lockdown Mode blocks an app

Lockdown Mode can restrict apps that need live access to an external service. Whether an administrator-managed indexed source remains available depends on the workspace, source, permissions, and current security policy.

Review the message shown for the current conversation. Do not turn off a security protection unless you understand the effect and are allowed to change that setting.

# An app reaches a usage limit

App use may count toward your ChatGPT plan limits, feature-specific allowances such as deep research, and limits imposed by the provider.

Review the relevant ChatGPT feature limit and any provider message before retrying.

# You cannot find the disconnect option

1. Open **Settings**.
2. Select **Apps** or **Plugins**, depending on what is available, and open the app.
3. If **Connected accounts** appears, use the relevant account’s more options menu (•••). Otherwise, review **Connection** or the app’s more options menu (•••).

Disconnecting one account does not necessarily remove other accounts or administrator-managed sync. Disconnecting the last account can uninstall some associated plugins, while uninstalling a plugin can disconnect all linked accounts.

For disconnection and data-retention details, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494) and [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

# A previously synced app is unavailable

Individually authorized app sync is no longer available. An old sync connection cannot be reconnected, restored, or upgraded through a personal account.

The former synced integrations for Aha!, Azure Boards, Basecamp, Help Scout, Pipedrive, Teamwork, Zoho CRM, and Zoho Desk are no longer supported.

Other providers may still offer supported live apps even though their former sync option is retired. Review the current app details instead of following an old sync setup guide.

If you previously used a synced app, check which options are still supported:

* Open **Apps** or **Plugins**, depending on the interface shown for your account, and look for the provider.
* If a current app is available, connect your provider account for supported live access.
* If your managed workspace supports administrator-managed sync for that provider, ask a workspace administrator to review the available setup.
* If the provider no longer offers a supported integration, the retired synced connection cannot be reactivated.

For provider account setup, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

For supported workspace indexing, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

# Contact OpenAI Support

If the issue continues, include the following in your support request:

* The app and plugin name.
* The affected account or workspace.
* The exact message.
* The model you selected and the ChatGPT app or interface you used.
* The steps you tried.
* The date, time, and time zone of the attempt.
* A screenshot with sensitive information removed.

For contact instructions, see: [How can I contact support?](https://help.openai.com/articles/6614161)

Do not include passwords, access tokens, or sensitive conversation content in your support request.
