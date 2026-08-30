<!-- source: https://help.openai.com/en/articles/10408842-google-app-data-controls-faq -->

# Google app data controls FAQ

Learn how your data is accessed and used when you connect Google services to ChatGPT.

ChatGPT workspace and Google Workspace administrators should review the Google app actions and OAuth scopes approved for their organization. Google Drive includes supported Google Docs, Sheets, and Slides actions; a provider administrator may need to approve any additional requested scopes.

# FAQ

## How does OpenAI use my data that's retrieved from the Google app?

When you connect a Google app such as Gmail, Calendar, or Drive, ChatGPT can access information needed for the supported requests you make, subject to your Google account permissions and workspace settings. An ordinary app connection does not automatically create a personal synced index. Separately, an eligible workspace administrator can configure administrator-managed Google Drive indexing when the workspace and source support it.

If you have Memory enabled, eligible information accessed through connected Google apps may help personalize ChatGPT, subject to your settings and the Google-specific data-use limitations described below.

We do not train our generalized models on data directly from connected Google apps or derivations of that data, except:

* when a conversation is submitted as feedback (for example, by using thumbs up/down);
* manually copied, pasted, or uploaded data from a Google app into ChatGPT conversations; or
* included in ChatGPT's response.

For connected-app data handling, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496). For OpenAI’s broader privacy practices, review the [Privacy Policy](https://openai.com/policies/privacy-policy).

The same policies apply when you browse or use Google Drive files from Library. Viewing or adding a Google Drive file from Library to a chat does not change how OpenAI uses data from connected Google apps.

## What if I have 'Improve the model for everyone' enabled in my ChatGPT settings?

Even if this setting is enabled, we do not train our generalized models on data accessed directly from connected Google apps. We train according to what's described above.

If the '**Improve the model for everyone**' setting is disabled, app data will not be used to improve our models even if it appears as part of your ChatGPT conversations.

## Will ChatGPT "remember" information from my Google account?

If Memory is enabled, ChatGPT may use eligible information from a connected Google app to personalize your experience, subject to your settings and applicable Google-specific data-use restrictions. Some sources or workflows prevent new memories from being saved. To review Memory settings, go to **Settings** > **Personalization**.

## Can Google app data be used for Memory or other personalization?

When Memory is enabled, eligible information from connected Google apps may help personalize ChatGPT. Whether a new memory can be saved depends on the source, workflow, and applicable product restrictions.

ChatGPT is designed to use only information that appears relevant to helping you, and we do not train our generalized models on Google app data except as described above. Google app data may contain information you might consider sensitive, so only enable the Google app if you're comfortable with ChatGPT using this data.

You can turn off Memory, review and delete saved memories, disconnect a Google app, or delete relevant conversations. These controls are separate: disconnecting an app does not automatically delete existing chats or saved memories.

## Why am I seeing suggested prompts based on Google data?

Where available, eligible information from connected Google apps can inform suggested prompts. To turn them off:

1. Go to **Settings > Personalization**.
2. Turn off **Suggested prompts**, if the setting appears.

This does not disconnect your Google apps, stop existing scheduled tasks, or delete existing data.

For the suggestion control and its limits, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

## Does ChatGPT respect existing permissions?

Yes. For an individual Google connection, ChatGPT can access only content available to the account you connect, after you authorize access. A supported administrator-managed Google Drive source uses the workspace’s configured connection; members can retrieve only content they already have permission to access.

For managed workspaces, your organization's Google **Workspace settings** may also limit which OAuth scopes the ChatGPT/OpenAI app can request. ChatGPT workspace admins can enable or disable Google app actions in ChatGPT, and ChatGPT requests the Google scopes needed for the actions that are enabled. Google Workspace then checks whether the ChatGPT/OpenAI app is trusted or approved for those scopes.

If a required Google scope has not been approved, users may see an authorization or permission error when connecting, reconnecting, or using an enabled action. Existing Google app connections are not removed when new scopes are introduced.

You can disconnect a Google app at any time in your ChatGPT settings.

When Google Drive appears in Library, Library only shows files and folders available to the connected Google account. Opening or adding a file from Library does not change its sharing settings or permissions in Google Drive.

## How does Gmail work with event-triggered tasks?

Eligible users can create an event-triggered (webhook-based) task in Work that responds to new messages in a connected Gmail account. The task can use sender or subject conditions and can access only the Google account and permissions authorized for that connection. A recipient who schedules a shared Gmail-triggered task must connect their own Gmail account.

Pause or delete the task to stop that task from processing new email events. Disconnect Gmail to remove the connection and stop related mailbox monitoring. Existing Google Workspace approvals and the Gmail scope listed in this article continue to apply.

For instructions, see: [Scheduled tasks in ChatGPT](https://help.openai.com/articles/10291617).

## What happens if a Google scope is not approved?

If a Google app action is enabled in ChatGPT but the required Google OAuth scope is not approved, users may see an authorization, admin approval, or permission error when they create a new connection, reconnect an existing Google account, or use that action.

Some Google OAuth flows can fail before ChatGPT receives a useful signal about which scope was blocked. If users report connection or reconnect errors, compare the Google actions enabled in ChatGPT with the scopes approved for the ChatGPT/OpenAI app in Google Workspace. A Google Workspace administrator can approve the missing scope, or a ChatGPT workspace administrator can disable the action that requires it.

Browsing and previewing Google Drive files requires read access. Actions that update a source file require the corresponding write access and must be enabled in ChatGPT. If a required scope is not approved, a user may be able to view a file but see an authorization or permission error when trying to update it.

## Will existing Google app connections be removed when new scopes are introduced?

No. Existing Google app connections are not removed because new scopes are introduced. However, users may need to reconnect, or may see errors when using a newly enabled action, if that action requires a Google scope your organization has not approved.

If your organization uses supported administrator-managed Google Drive indexing, a Google scope update does not by itself remove that connection. ChatGPT workspace administrators should review enabled actions and disable any they do not want to authorize. Google Workspace administrators should review and approve the OAuth scopes required by the remaining enabled actions. Individual Google app sync is no longer available.

## What controls do I have about how my data is stored and used?

You can control how your connected app data is used by:

* Disconnecting a Google app at any time.
* Turning Memory on or off in **Settings** > **Personalization**.
* Turning off **Suggested prompts**, where available, in **Settings > Personalization**.
* Deleting individual conversations.
* Turning off model improvement in your ChatGPT settings.
* For workspace admins, reviewing which Google app actions are enabled in ChatGPT workspace settings.
* For Google Workspace admins, trusting the ChatGPT/OpenAI app or explicitly approving the Google OAuth scopes required by enabled actions.

If you delete a conversation, app data retained in that conversation follows ChatGPT’s chat-deletion policy. Chats are scheduled for permanent deletion within 30 days, unless they have already been de-identified and disassociated from you or OpenAI must retain them longer for security or legal obligations.

For conversation deletion, see: [Chat and File Retention Policies in ChatGPT](https://help.openai.com/articles/8983778). For app data controls, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

If you disconnect your Google Drive account, ChatGPT can no longer access files through that individual connection. Disconnecting your account does not automatically remove a separate administrator-managed workspace index, delete existing conversations or saved memories, or change your original files in Google Drive. Workspace administrators should review the applicable retention and deletion terms before removing an administrator-managed source.

## What admin scopes are requested by Google apps in ChatGPT?

Google Docs, Sheets, and Slides actions are available through the Google Drive app. ChatGPT supports Google app actions for Google Drive files, BigQuery, and Google Meet actions surfaced under Google Calendar. These actions require additional Google OAuth scopes.

Workspace admins should review Google app action settings in ChatGPT, and Google Workspace admins should confirm that the ChatGPT/OpenAI OAuth app is trusted or approved for the required scopes.

Existing Google app connections are not removed when new scopes are introduced, but users may see authorization errors when connecting, reconnecting, or using an enabled action that requires an unapproved scope. Administrator-managed Google Drive indexing remains a separate workspace configuration.

### Gmail

* <https://www.googleapis.com/auth/gmail.modify>

### Google Calendar

* <https://www.googleapis.com/auth/calendar.events>
* <https://www.googleapis.com/auth/meetings.space.readonly>
* For Google Meet actions surfaced under Google Calendar, such as Meet space lookup, conference records, recordings, transcripts, transcript entries, and artifacts.

### Google BigQuery

* <https://www.googleapis.com/auth/bigquery>
* <https://www.googleapis.com/auth/bigquery.readonly>
* <https://www.googleapis.com/auth/bigquery.insertdata>

### Google Contacts

* <https://www.googleapis.com/auth/contacts.readonly>
* <https://www.googleapis.com/auth/contacts.other.readonly>

### Google Drive

(including Google Docs, Sheets, and Slides actions)

* <https://www.googleapis.com/auth/drive.readonly>
* <https://www.googleapis.com/auth/drive.metadata.readonly>
* <https://www.googleapis.com/auth/drive.activity.readonly>
* <https://www.googleapis.com/auth/drive>
* For Google Drive actions that create, update, share, move, upload, copy, or delete Drive-family files.

### Google Docs

* <https://www.googleapis.com/auth/documents>
* <https://www.googleapis.com/auth/documents.readonly>

### Google Sheets

* <https://www.googleapis.com/auth/spreadsheets>
* <https://www.googleapis.com/auth/spreadsheets.readonly>

### Google Slides

* <https://www.googleapis.com/auth/presentations>
* <https://www.googleapis.com/auth/presentations.readonly>

For Google Drive setup, see: [Google Drive app and setup in ChatGPT](https://help.openai.com/articles/10929079).

## How can admins allow some Google actions but not others?

Use ChatGPT workspace app settings to disable actions your organization does not want users to run. Google Workspace administrators should approve the OAuth scopes required by the actions you leave enabled. Manage existing Google permissions separately in Google Workspace.

Use this decision rule:

* If you want users to use an action, approve the required Google scope and keep the action enabled in ChatGPT.
* If you do not want to approve a Google scope, disable every ChatGPT action that requires that scope.
* If an action remains enabled while its Google scope is blocked, users may encounter authorization or permission errors.

## What should admins do after approving scopes?

After Google Workspace approvals and ChatGPT action settings are aligned, ask affected users to create a new Google connection or reconnect their existing Google account. If a user previously saw an authorization or admin approval error, ask them to retry only after you confirm the required scopes are approved or the blocked action is disabled.

## Does using Google Drive in Library change how my Google apps data is stored or used?

No. The same data controls for connected Google apps apply to Google Drive files accessed from Library. OpenAI does not train its generalized models on data directly from connected Google apps or derivations of that data, except as described above in this article.

## Which Google account and files appear in Library?

Library uses the Google account you choose when connecting Google Drive. It only shows content available to that account under its existing permissions. For the initial Google Drive in Library experience, this includes My Drive and files and folders shared directly with you; Shared Drives aren’t included yet.

## What happens when I disconnect or reconnect Google Drive?

After you disconnect Google Drive, ChatGPT can no longer access files through that individual connection. A separate administrator-managed Google Drive index is controlled by the workspace administrator and applicable workspace settings. Reconnecting may require you to authorize newly requested scopes. Existing connections are not removed only because new scopes are introduced, but a newly enabled action may require you to reconnect before you can use it.

## Why can I view a Google Drive file in Library but not update it?

The update may not be supported in ChatGPT, the required action may be disabled, or ChatGPT may not have the required Google Drive permission or OAuth scope. You can still open the original file in Google Drive to use the full Google editing and collaboration experience.

## Can workspace admins control Google Drive access in ChatGPT?

ChatGPT workspace admins can control which Google Drive actions are enabled for their workspace. Google Workspace admins can control whether the ChatGPT app is trusted or whether the OAuth scopes required by those actions are approved. If an action is disabled or its required scope is blocked, users won’t be able to use that action.
