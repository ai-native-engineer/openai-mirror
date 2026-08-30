<!-- source: https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt -->

# Connecting and managing app accounts in ChatGPT

Learn how to connect the right provider account, review requested access, manage multiple accounts, and disconnect an app.

Some apps ask you to connect an account before ChatGPT can use them. Others do not require individual sign-in or can use a connection set up by your workspace administrator.

When an app requires individual authorization, choose the account that already has access to the information you need and review the requested permissions before approving the connection.

You can return later to review connected accounts, add another supported account, change account-specific settings, or disconnect an app you no longer want to use.

## Availability

An app must be available for your plan, region, account, supported surface, and workspace. In managed workspaces, an administrator may also need to enable the app or approve the account domain.

For help with unavailable apps or **Disabled by admin** messages, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

# Connect an app account

1. Open **Apps** or **Plugins**, depending on which option appears for your account. Select the app or the plugin that includes it.
2. Select **Install plugin** if shown; this may also start the app’s connection or setup flow.
3. If prompted, select **Connect** or continue the app’s setup flow.
4. Sign in to the intended provider account when the app requires individual authorization.
5. Review the requested services and permissions.
6. Complete any required provider authorization.

Select the account that already has access to the information you need. Connecting a personal account does not provide access to files, channels, or records available only to your work account.

Some providers let you include related services in the same authorization flow. Review each selected service before approving access.

A plugin may be listed or installed before its app is ready to use. You still need access to the app, the correct connected account, and any required provider approval. For help with installation, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

# Review provider permissions

The provider’s authorization screen lists the services and provider permissions requested for the selected account. Actions available in ChatGPT also depend on the app’s capabilities and applicable workspace action controls.

If you see **All permissions are required**, select **Reconnect** and approve every permission required for the apps you selected.

If you see **ChatGPT needs all requested permissions** when connecting Google apps, select **Try again**. On Google’s authorization screen, select **Select all** to approve the requested permissions.

To connect fewer Google apps, select **Select fewer apps** in ChatGPT and choose the apps you want. You must still approve every requested permission for the selected apps.

A provider administrator may also need to approve access. The administrator for Google, Microsoft, or another service may be different from your ChatGPT workspace administrator.

Provider authorization does not override workspace restrictions, app action controls, or the existing permissions of the connected account.

For ChatGPT approval settings, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

# Review or connect another account

Some apps support more than one connected account. Availability depends on the app and your account.

1. Open **Settings**, then select **Apps** or **Plugins**, depending on which option is available.
2. Select the relevant plugin or app.
3. If **Connected accounts** appears, review an account or select **Connect another account** when available. Otherwise, use the **Connection** section shown for the app.
4. Sign in and complete any requested authorization.

If an app uses the wrong account, review the accounts connected to it. When supported, specify the account you want to use in your request.

# Use a connected app

After connecting an app, describe what you want to do in a supported ChatGPT conversation.

You can mention an available plugin or app with @, or open + and select it from the available menu. Some interfaces place additional options under **More**.

ChatGPT may request approval before reading information or completing an action. The available actions depend on the app, provider account, and workspace controls.

Support in voice conversations varies by app and available features. If an app is unavailable in voice, use a supported text conversation.

Some apps can be used with deep research. For supported research workflows, see: [Deep research in ChatGPT](https://help.openai.com/articles/10500283).

Administrator-managed sync is a separate workspace capability with its own eligibility and setup requirements. For indexed workspace sources, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

# Reconnect an app

Select **Reconnect** when available. If the app instead asks you to disconnect and connect again, review any warnings before following those instructions.

Choose the intended account again and review any newly requested access. Reconnecting one account does not automatically update every other account connected to the same app.

For Google-specific authorization and data controls, see: [Google app data controls FAQ](https://help.openai.com/articles/10408842).

# Disconnect an app account

1. Open **Settings**, then select **Apps** or **Plugins**, depending on which option is available.
2. Select the relevant plugin or app.
3. If **Connected accounts** appears, open the account’s more options menu (•••). Otherwise, use **Connection** or the plugin’s more options menu (•••).
4. Select **Disconnect**.

Disconnecting stops future access through that account. Other connected accounts or administrator-managed workspace connections can remain active. Disconnecting the last account can also remove some associated plugins from your installed list.

Uninstalling a plugin can disconnect all accounts connected through that plugin. Review the warning before confirming.

Disconnecting an app does not automatically delete existing or archived conversations, saved files, your Memory summary, or other saved memories. Review those items and the provider’s account controls separately.

For retention, synced data, and provider-specific rules, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).
