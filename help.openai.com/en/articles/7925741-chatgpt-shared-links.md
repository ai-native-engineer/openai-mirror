<!-- source: https://help.openai.com/en/articles/7925741-chatgpt-shared-links -->

# ChatGPT shared links

Generate a unique URL to be able share a link to one of your ChatGPT conversations

## Overview

Shared links let people view a ChatGPT conversation or an eligible scheduled task. Scheduled task sharing is available to eligible users across ChatGPT plans, including Free and Go. The information included, who can open the link, and how shared content changes depend on the account, workspace, and type of content.

Review the content and audience before sharing. A link does not provide access to the creator’s account, but anyone permitted to open it can view its shared content.

## Understand shared link types

### Share conversations and responses

A shared conversation can include conversation history, an individual assistant response, supported images, or uploaded files. Available content depends on the sharing experience, account features, and recipient permissions.

A response that is still generating may not appear until it is complete. Review the entire shared preview before sending the link.

### Share scheduled tasks

A shared task link includes the task title, full instructions, schedule, and original time zone. It may preserve a ChatGPT mode or model when that option is available to the recipient.

Eligible active or paused scheduled tasks can be shared, including event-triggered (webhook-based) tasks. Completed tasks cannot be newly shared. Tasks that run only on a computer cannot be scheduled from a shared link.

A recipient must sign in before scheduling a shared task and needs access to scheduled tasks, available task capacity, and any required workspace or connected-app permissions. To schedule an event-triggered task, the recipient also needs access to **Work** and their own connected app.

For task instructions, see: [Scheduled tasks in ChatGPT](https://help.openai.com/articles/10291617).

## Understand access and privacy

### Review personal-account access

Anyone who has a link created from a personal account can view the shared conversation or scheduled task.

A personal-account conversation link includes the content available when the link is created or updated. Messages added later are not included automatically.

### Review managed-workspace access

A link created in a ChatGPT Business, Enterprise, or Edu workspace, or in a ChatGPT for Healthcare workspace, can be opened only by eligible members of the same workspace. People outside that workspace cannot view the shared content.

Unlike a personal-account conversation snapshot, a workspace conversation link can include messages added after sharing. Review the sharing notice before adding new information to a shared workspace conversation.

A Business or Enterprise workspace member can view a public scheduled task shared from a personal account, but cannot schedule that task in their workspace. Access to personal-account conversation links depends on workspace settings. A workspace-created link remains restricted to its originating workspace.

### Review names and sensitive information

Shared conversation links are anonymous by default. Some existing or older sharing experiences may display the creator’s name, so review the preview before sending a link.

A shared scheduled task does not include the creator’s profile name, chat history, previous task results, saved memories, custom instructions, uploaded or local files, connected-app data, or connected-app credentials. Recipients use their own account and app permissions.

Supported images and uploaded files can appear in a shared conversation. Names or personal information entered in a conversation, task title, or task instructions can also be visible. A task title may appear in a link preview.

Do not include health information, financial details, passwords, account numbers, or other sensitive personal information in shared content.

## Create and update shared links

### Share a conversation

1. Open the conversation.
2. Select **Share**.
3. Review the conversation and any available sharing options.
4. Select **Create link** or **Copy link**, depending on the option shown.
5. Send the link to the intended recipient.

### Share a scheduled task

1. Go to **Scheduled**.
2. Select the task’s more options menu (•••).
3. Select **Share**.
4. Review the task details in **Share task**.
5. Select **Copy link**.
6. Send the copied link to the intended recipient.

### Update shared content

To update a personal-account conversation snapshot, open the conversation, select **Share**, and select **Update link**. A workspace conversation can automatically include later messages, so review its sharing notice before continuing the conversation.

To update a shared scheduled task, open the task in **Scheduled**, select **Share**, and select **Copy link** again. This refreshes the shared snapshot at the same URL. It does not change a task another person already scheduled.

## Manage and delete shared links

### Find shared links

1. Go to **Settings**.
2. Select **Data controls**.
3. For **Shared links**, select **Manage**.

The list includes shared conversation links and shared scheduled task links.

### Delete a shared link

From the shared-link list, select **Delete shared link** for an individual item. To remove every link, open **More actions** and select **Delete all shared links**.

Task creators can also open the original task’s **Share task** dialog, select the trash can icon next to the shared link, and select **Delete share** to confirm.

### Understand recipient-owned copies

Continuing a shared conversation creates a separate, private conversation in the recipient’s account. Scheduling a shared task creates a separate task that uses the recipient’s account, app connections, and workspace permissions.

Deleting a shared link stops future access to that link but does not delete the original conversation or task. It also does not remove a conversation or task another person already saved.

### Understand source-content deletion

Deleting a conversation removes its shared conversation link. If the conversation has an associated scheduled task, the task pauses, but its shared task link remains available. Delete the task link separately to stop access.

Deleting the original scheduled task removes its shared task link. Copies already saved by another person remain in that person’s account.

### Prepare to delete an account

Shared conversation links are deleted when their creator deletes the account.

Before deleting an account, delete any shared scheduled task links from the original tasks or from **Shared links** in **Data controls**. Copies already saved by other people remain in their accounts.

## Review workspace admin controls

Enterprise and Edu workspace admins can manage **Share chats and scheduled tasks in the workspace** from **Workspace settings > Permissions & roles** when that permission is available. Turning the permission off prevents workspace members from sharing conversations or scheduled tasks and from scheduling tasks from shared links in that workspace.

ChatGPT Business links are restricted to their originating workspace, but Business does not provide the same workspace-wide control for disabling shared links.

**Allow event-triggered scheduled tasks** is a separate **Work** permission that is turned off by default in Enterprise, Edu, and ChatGPT for Healthcare workspaces. In ChatGPT for Healthcare, event-triggered tasks are not covered under a Business Associate Agreement (BAA) and must not be used to transmit, store, or process protected health information (PHI). To schedule a shared event-triggered task, a recipient needs this permission, access to **Work**, their own connected app, and permission to share scheduled tasks in the workspace.

For admin guidance, see: [Managing workspace settings in ChatGPT Enterprise](https://help.openai.com/articles/8411955).

For Business-specific information, see: [Managing data and sharing in ChatGPT Business](https://help.openai.com/articles/8798634).

## Understand data exports and compliance

A personal-account data export includes shared conversation metadata in shared\_conversations.json. Each record includes the shared-link ID, conversation ID, title, and anonymity setting. Scheduled tasks, shared scheduled task links, and their saved snapshots are not currently included in personal account data exports.

The Enterprise Compliance API includes underlying scheduled tasks, but it does not currently include shared task links or their saved snapshots. Data export is not available from a ChatGPT Business workspace.

## Recognize and report unsafe links

Shared conversation links begin with https://chatgpt.com/share/. Shared scheduled task links begin with https://chatgpt.com/s/.

Confirm that a link uses the chatgpt.com domain and comes from a trusted sender before opening it.

For a shared conversation, select **Report conversation** if that option appears. For a shared scheduled task, select **Report** if that option is available.

If an in-product reporting option is unavailable, use the [OpenAI content reporting form](https://openai.com/form/report-content/).

For instructions, see: [Reporting content in ChatGPT and OpenAI platforms](https://help.openai.com/articles/10245791).

## FAQ

### Can I restrict a shared link to specific people?

Shared links do not offer recipient-by-recipient access controls. Personal-account links are available to anyone who has the link. Managed-workspace links are limited to members of the originating workspace.

### Can I set an expiration date for a shared link?

Shared links do not have configurable expiration dates. Delete a link when access is no longer needed.

### Do shared links appear in search results?

Shared link pages are not intended for search-engine indexing, but this does not make a link private. Anyone who can access a link can also forward it.

### Does changing model-training settings delete existing shared links?

For a personal account, changing **Improve the model for everyone** does not delete existing shared links or change who can open them. Manage or delete shared links separately.

For details, see: [Data controls FAQ](https://help.openai.com/articles/7730893).
