<!-- source: https://help.openai.com/en/articles/12368225-box-app-and-setup-in-chatgpt -->

# Box app and setup in ChatGPT

Connect Box to ChatGPT to find authorized files, manage account permissions, and troubleshoot access.

The Box app lets ChatGPT search and use files your connected Box account can access. You can ask questions about documents, summarize information, compare files, or work with available Box actions without setting up individual sync.

Box availability depends on your ChatGPT plan, workspace configuration, and Box account permissions. If you use a managed workspace, an administrator may need to make Box available before you can connect.

For an overview of connected apps, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

# Connect Box to ChatGPT

1. Open **Apps** or **Plugins**, depending on which option appears for your account.
2. Find and select **Box**.
3. Select **Connect**. If Box is listed as a plugin instead, select **Install plugin** and complete the connection prompt when it appears.
4. Sign in to the Box account that has access to the files and folders you need.
5. Review the permissions shown by Box, approve the connection, and return to ChatGPT.

For general connection instructions, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Use Box in a conversation

After connecting Box, ask ChatGPT about files and folders that your Box account can access. Include a project name, document title, folder, or subject when you can.

For example:

* “Find our quarterly planning documents in Box and summarize the major priorities.”
* “Compare the two onboarding documents in my Box folder and list the differences.”
* “Summarize the documents shared with me about the product launch.”
* “Find the latest project brief in Box and identify the open questions.”

ChatGPT can work only with content that is available through your authorized Box connection. If a file is not accessible to your Box account, connecting Box does not give ChatGPT additional access.

Box actions can vary by account, workspace, and enabled capabilities. An action that changes Box content is available only when the app offers it, the relevant permissions allow it, and any required approval is granted.

# Understand Box permissions

Box continues to control which files and folders your account can access, including content shared with you. ChatGPT also respects app availability, role access, and action settings configured for your ChatGPT workspace.

Review the permissions on Box’s authorization screen when you connect. Requested permissions can depend on the connection and available actions. If Box permissions change or new authorization is required, you may need to reconnect.

For an explanation of provider permissions, app approvals, and connected accounts, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

For information about data shared with connected apps, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

For workspace administration, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# Disconnect or change your Box account

To stop using a connected Box account, open **Apps** or **Plugins**, select **Box**, and use the available disconnect option.

If you use Box through a plugin, open its settings and use the available uninstall or connection-management option. To remove Box account authorization too, review your connected apps separately.

To use a different Box account, disconnect the existing account and complete the connection process again with the correct Box credentials.

# Troubleshoot Box access

## Box is not available

Confirm that Box is available for your account. In a managed workspace, also check that an administrator has enabled it for your role. If Box appears as a plugin, check the **Plugin directory**.

## A file or folder is missing

Confirm that the connected Box account can open the file directly in Box. Check the account, file-sharing settings, folder permissions, and any restrictions applied by your organization.

Try a more specific prompt that includes the document title or project name. ChatGPT cannot retrieve content that the Box account cannot access.

## Box asks you to reconnect

Review the authorization request and reconnect when additional permission or a refreshed connection is needed. If your organization manages Box access, contact the appropriate Box or ChatGPT workspace administrator.

For additional help, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

# FAQ

## Does Box use individual sync?

No. Use the available Box app or plugin to access authorized content. Do not follow older instructions that ask you to set up individual sync or wait for a Box sync status.

## Can ChatGPT access files shared with me?

ChatGPT can use shared Box files only when the connected Box account already has permission to access them and the app can retrieve them.

## Can my workspace administrator control Box access?

Yes. Workspace settings can control whether Box is available and which roles or actions are allowed. These settings do not override the permissions of your Box account.

## Can I use Box in an Enterprise Key Management workspace?

Availability in an Enterprise Key Management workspace depends on whether the specific Box app or plugin is supported for that workspace and has been enabled by an administrator. Ask your workspace administrator to check the available app, key-management settings, and provider permissions.
