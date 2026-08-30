<!-- source: https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt -->

# Managing app permissions in ChatGPT

Learn how app permissions, action approvals, provider access, and workspace settings affect connected apps in ChatGPT.

App permissions determine when ChatGPT can read information from a connected account or take an action on your behalf.

These settings control how an app is used once access is available. They do not connect accounts, grant provider permissions, change source-system access, or override workspace policies. Account-wide or workspace-wide defaults can be configured before an individual app account is connected.

For account setup and disconnection, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

## Availability

Available settings depend on your account, the app, the connected account, and your workspace.

Personal accounts may see **Permissions** after installing a plugin that includes an app. Connection-specific controls can require an eligible connected account. Managed-workspace members may instead see approval prompts governed by workspace policy.

# Understand permission options

Depending on your account and the app, you may see:

* **Always ask**: ChatGPT asks before reading app information or making changes.
* **Allow read actions**: ChatGPT can read without asking but asks before making changes.
* **Allow low-risk actions**: ChatGPT automatically approves low-risk actions. Higher-risk actions may require confirmation or be denied. This setting applies when no account, workspace, app, or connection policy overrides it.
* **Allow all actions**: ChatGPT can perform supported actions without additional approval prompts. This option carries elevated risk.

For more information about security warnings on sensitive capabilities, see: [Elevated Risk labels](https://help.openai.com/articles/20001062).

The standard account-wide and workspace-wide permission selectors do not offer **Allow all actions**. It may be available for an individual app or connected account, and existing workspace policies can differ.

Some menus shorten these labels to **Allow read**, **Allow low-risk**, or **Allow all**.

# Understand action risk

An action may require additional review when it can affect another service, expose sensitive information, or be difficult to undo.

Examples can include:

* Sending an email, message, comment, or invitation.
* Creating, editing, or deleting a file or record.
* Changing account, access, sharing, or security settings.
* Making a purchase or other financial transaction.
* Sharing sensitive personal, financial, health, or identity information.

Actions are evaluated against the available app capabilities, provider permissions, workspace policies, and safety protections. Some requests may be denied instead of showing an approval prompt.

# Set your default permission

For an eligible personal account, use the steps below if **Settings** shows **Plugins**.

If **Settings** shows **Apps** instead, open **Apps** to review the permission controls available to your account. The same account-wide selector may not be available.

1. Open your profile menu and select **Settings**.
2. Select **Plugins**.
3. Open **Permissions**.
4. Choose the default permission you want to use.

The overall setting can appear after you install a plugin that includes an app. Controls for a specific app or account can require an eligible connection, and not every app supports the same settings.

# Set a permission for one connected account

1. Open **Settings**, then select **Apps** or **Plugins**, depending on which option is available.
2. Select the relevant plugin or app.
3. If **Connected accounts** appears, open the relevant account’s more options menu (•••) and select **Settings**.
4. Review **Permissions** for that account. For an app with one account, open the available **Permissions** setting instead.
5. Select an available permission, then select **Save** if shown.

An account-specific setting applies only to that connection. Another account connected to the same app can have a different setting.

To restore a connected account’s inherited setting, select the option marked **Default**, then select **Save**. A single-account page may show **Reset**; older **Apps** settings may show **Reset to default**.

# Respond to an approval prompt

Before a supported action runs, ChatGPT may show an approval card describing the app and the proposed action.

Depending on the action and your account, the available controls may include:

* **Deny** or **Decline**: Do not perform the requested action.
* **Allow** or **Allow once**: Approve the current action.
* **Allow low-risk actions**: Approve the current action and allow future low-risk actions using the same connected account. Higher-risk actions may require confirmation or be denied.
* **Always allow**: When offered for an eligible, explicitly connected personal account, allow supported future actions without repeated prompts.

For the app action approvals described here, **Always allow** is not offered as a persistent permission to managed-workspace members, for automatically available connections, or for actions that require additional safety review.

Review the app, account, and proposed action before approving a request. A saved approval does not override workspace restrictions, provider permissions, or safety protections. Depending on the product surface, a sensitive action may be denied instead of showing an approval prompt.

# Understand workspace restrictions

In a managed workspace, different settings control different parts of app access:

* Plugin installation settings determine whether the plugin is available.
* Workspace app settings determine whether the underlying app can be used.
* Enterprise and Edu role controls can limit which members can access an app.
* Provider authorization determines which external account and permissions are connected.
* Action controls determine which app actions are available.
* App permissions determine when ChatGPT asks before using an available action.

Business administrators can control whether an app is enabled for the workspace. Enterprise and Edu administrators can also configure role-based access where supported.

Controls that restrict direct app actions do not necessarily restrict information retrieved from synced data. Sync content-selection settings do not necessarily restrict separate live app actions.

Workspace Agents use separate agent-level action-safety settings that remain subject to workspace policies.

For administrator guidance, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# Remove an app's access

Changing an app permission does not disconnect the app or revoke access already granted to a provider account.

To stop future access through an individual account, open **Settings**, select **Apps** or **Plugins**, choose the app, and disconnect the account. The provider may also offer separate account-unlinking controls.

Disabling an app for a workspace can affect other members, dependent plugins, or an administrator-managed index. Review the warning shown before changing workspace-wide access.

App permissions are separate from Memory, personalization, data retention, and model-training controls.

For data handling, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).
