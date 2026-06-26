<!-- source: https://help.openai.com/en/articles/10408842-google-app-for-chatgpt-data-controls-faq -->

# Google App for ChatGPT – Data Controls FAQ

Learn how your data is accessed and used when you connect Google services to ChatGPT

Updated: 3 days ago

***Note:*** *Starting June 15, 2026, ChatGPT is adding new Google app actions for Google Drive files, BigQuery, and Google Meet actions surfaced under Google Calendar. These actions require additional Google OAuth scopes in Google Workspace.*  
  
*Before June 15, 2026, workspace admins should coordinate across the people who manage ChatGPT workspace settings and Google Workspace app access. In ChatGPT, review which Google app actions are enabled for your workspace. In Google Workspace, either mark the ChatGPT/OpenAI OAuth app as* ***Trusted****, if that fits your organization's security policy, or explicitly approve every Google scope required by the actions you keep enabled.*  
  
*If your workspace is configured to enable new app actions by default, new Google actions may be available to users starting June 15, 2026 unless an admin disables them. If you do not want to approve a scope, disable every ChatGPT app action that requires that scope. Users in your workspace will not be able to use disabled actions, but this avoids authorization errors caused by enabling actions whose Google scopes are blocked in your Google Workspace tenant.*  
  
*You can review Google app actions in* [*ChatGPT workspace app settings*](https://chatgpt.com/admin/apps?tab=workspace&q=drive)*. Google Workspace admins can review app access in* [*Google Admin console API controls*](https://admin.google.com/ac/owl)*. In Google Admin console, search for the ChatGPT/OpenAI app. For Google's guidance on trusted and limited app access, see* [*Control which apps access Google Workspace data*](https://knowledge.workspace.google.com/admin/apps/control-which-apps-access-google-workspace-data#trustorlimit)*.*

## How does OpenAI use my data that's retrieved from the Google app?

When you connect a Google app (like Gmail, Calendar, or Drive), ChatGPT may create an indexed copy and [sync](/en/articles/10847137-chatgpt-apps-with-sync) the content from that app to help provide more relevant and useful information.  
  
If you have [Memory](/en/articles/8590148-memory-faq) enabled, this synced content may be used to personalize your ChatGPT by proactively providing helpful information or suggestions (for example, summarizing upcoming events or surfacing relevant documents). When you disconnect the app, the indexed copy will be deleted within 30 days.  
  
We do not train our generalized models on data directly from connected Google apps or derivations of that data, except:

* when a conversation is submitted as feedback (for example, by using thumbs up/down);
* manually copy, pasted, or uploaded data from a Google app into ChatGPT conversations; or
* included in ChatGPT's response.

For more information, please see [this article](/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) and our [Privacy Policy](https://openai.com/policies/privacy-policy).

## What if I have 'Improve the model for everyone' enabled in my ChatGPT settings?

Even if this setting is enabled, we do not train our generalized models on data synced directly from connected Google apps. We train according to what's described above.  
  
If the 'Improve the model for everyone' setting is disabled, synced app data will not be used to improve our models even if it appears as part of your ChatGPT conversations.

## Will ChatGPT "remember" information from my Google account?

If you have Memory enabled, ChatGPT may save and use relevant information it has accessed, including from connected apps, to provide more helpful information to you. You can turn Memory off or manage saved memories in your settings, which can be accessed by going to **Settings > Personalization**.

## Can Google app data be used for Memory or other personalization?

If you connect Google apps and have [Memory](/en/articles/8590148-memory-faq) enabled, ChatGPT may use relevant information from Google apps to personalize your experience, including by creating memories or other personalized context that can help ChatGPT respond more usefully later.  
  
ChatGPT is designed to use only information that appears relevant to helping you, and we do not train our generalized models on Google app data except as described above. Google app data may contain information you might consider sensitive, so only enable the Google app if you're comfortable with ChatGPT using this data.  
  
You can control this by turning [Memory](/en/articles/8590148-memory-faq) off, disconnecting a Google app, or deleting relevant conversations.

## Does ChatGPT respect existing permissions?

Yes. ChatGPT can only access content from the Google account you choose to connect, and only after you grant permission during setup.  
  
For managed workspaces, your organization's Google Workspace settings may also limit which OAuth scopes the ChatGPT/OpenAI app can request. ChatGPT workspace admins can enable or disable Google app actions in ChatGPT, and ChatGPT requests the Google scopes needed for the actions that are enabled. Google Workspace then checks whether the ChatGPT/OpenAI app is trusted or approved for those scopes.  
  
If a required Google scope has not been approved, users may see an authorization or permission error when connecting, reconnecting, or using an enabled action. Existing Google app connections are not removed when new scopes are introduced.  
  
You can disconnect a Google app at any time in your ChatGPT settings.

## What happens if a Google scope is not approved?

If a Google app action is enabled in ChatGPT but the required Google OAuth scope is not approved, users may see an authorization, admin approval, or permission error when they create a new connection, reconnect an existing Google account, or use that action.  
  
Some Google OAuth flows can fail before ChatGPT receives a useful signal about which scope was blocked. If users report connection or reconnect errors, compare the Google actions enabled in ChatGPT with the scopes approved for the ChatGPT/OpenAI app in Google Workspace. Then either approve the missing scope or disable the action that requires it.

## Will existing Google app connections be removed when new scopes are introduced?

No. Existing Google app connections are not removed because new scopes are introduced. However, users may need to reconnect, or may see errors when using a newly enabled action, if that action requires a Google scope your organization has not approved.  
  
If your organization already uses Google app sync, the sync feature is not removed by this scope update. Admins should still review any newly enabled actions and approve or disable the scopes they require before asking users to retry.

## What controls do I have about how my data is stored and used?

You can control how your connected app data is used by:

* Disconnecting a Google app at any time
* Turning [Memory](/en/articles/8590148-memory-faq) on or off in **Settings > Personalization**
* Deleting individual conversations
* Turning off model improvement in your ChatGPT settings
* For workspace admins, reviewing which Google app actions are enabled in ChatGPT workspace settings
* For Google Workspace admins, trusting the ChatGPT/OpenAI app or explicitly approving the Google OAuth scopes required by enabled actions

If you delete a conversation, any connected app data retained within that conversation is also deleted within 30 days.  
  
Learn more about how conversations are deleted in [this article](/en/articles/8809935-how-to-delete-and-archive-chats-in-chatgpt), and our general retention practices in [this article](/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt). Learn more about how to control your settings in [this article](/en/articles/7730893-data-controls-faq).

## What admin scopes are requested by Google apps in ChatGPT?

***Note:*** *Google Docs, Sheets, and Slides actions are available through the Google Drive app. Starting June 15, 2026, ChatGPT is adding Google app actions for Google Drive files, BigQuery, and Google Meet actions surfaced under Google Calendar. These actions require additional Google OAuth scopes.*  
  
*Before June 15, 2026, workspace admins should review Google app action settings in ChatGPT and Google Workspace admins should confirm that the ChatGPT/OpenAI OAuth app is trusted or approved for the required scopes.*   
  
*Existing Google app connections are not removed when new scopes are introduced, but users may see authorization errors when connecting, reconnecting, or using an enabled action that requires an unapproved scope. Google app sync is not removed by this scope update.*

### Gmail

* https://www.googleapis.com/auth/gmail.modify

### Google Calendar

* https://www.googleapis.com/auth/calendar.events
* https://www.googleapis.com/auth/meetings.space.readonly

* For Google Meet actions surfaced under Google Calendar, such as Meet space lookup, conference records, recordings, transcripts, transcript entries, and artifacts.

### Google BigQuery

* https://www.googleapis.com/auth/bigquery
* https://www.googleapis.com/auth/bigquery.readonly
* https://www.googleapis.com/auth/bigquery.insertdata

### Google Contacts

* https://www.googleapis.com/auth/contacts.readonly
* https://www.googleapis.com/auth/contacts.other.readonly

### Google Drive

**(including Google Docs, Sheets, and Slides actions)**

* https://www.googleapis.com/auth/drive.readonly
* https://www.googleapis.com/auth/drive.metadata.readonly
* https://www.googleapis.com/auth/drive.activity.readonly
* https://www.googleapis.com/auth/drive

* For Google Drive actions that create, update, share, move, upload, copy, or delete Drive-family files.

### Google Docs

* https://www.googleapis.com/auth/documents
* https://www.googleapis.com/auth/documents.readonly

### Google Sheets

* https://www.googleapis.com/auth/spreadsheets
* https://www.googleapis.com/auth/spreadsheets.readonly

### Google Slides

* https://www.googleapis.com/auth/presentations
* https://www.googleapis.com/auth/presentations.readonly

Read our article on [Google Drive](/en/articles/10948259) for more info.

## How can admins allow some Google actions but not others?

Use ChatGPT workspace app settings to disable any action whose Google scope your organization does not want to approve. If an action is disabled, users in that workspace cannot use it, and ChatGPT does not need that action's scope for the workspace.  
  
Use this decision rule:

* If you want users to use an action, approve the required Google scope and keep the action enabled in ChatGPT.
* If you do not want to approve a Google scope, disable every ChatGPT action that requires that scope.
* If an action remains enabled while its Google scope is blocked, users may encounter authorization or permission errors.

## What should admins do after approving scopes?

After Google Workspace approvals and ChatGPT action settings are aligned, ask affected users to create a new Google connection or reconnect their existing Google account. If a user previously saw an authorization or admin approval error, ask them to retry only after you confirm the required scopes are approved or the blocked action is disabled.
