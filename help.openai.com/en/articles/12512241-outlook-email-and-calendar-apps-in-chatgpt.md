<!-- source: https://help.openai.com/en/articles/12512241-outlook-email-and-calendar-apps-in-chatgpt -->

# Outlook Email and Calendar apps in ChatGPT

Learn how to use the Outlook Email and Calendar apps with ChatGPT, including shared and delegated mailboxes and calendars, people lookup, and contact management actions.

The Outlook Email and Outlook Calendar apps connect ChatGPT to supported Microsoft account information. Available actions depend on your account permissions, Microsoft Entra consent, workspace settings, and the app you select.

## Choose the right Microsoft connection

Use your own ChatGPT account. Before connecting Outlook, confirm which ChatGPT account and workspace you are using.

Adding another Microsoft account, where supported, creates another app connection. It does not switch your ChatGPT account or workspace. For setup, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

For a shared or delegated mailbox or calendar, connect the Microsoft account that already has access to that resource. ChatGPT does not grant Microsoft sharing or delegation permissions. If you need access, ask the resource owner or your Microsoft administrator.

# Outlook Email app

The Outlook Email app lets ChatGPT search and reference messages, look up people, and use supported contact-management actions when they are enabled for your account and workspace.

For account setup and authorization, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

## Example use cases and prompts

Communication and writing

* “Summarize the latest update from [sender] about this project.”
* “Draft a reply that covers the three main points in the last email from [sender].”

Organization and productivity

* “Show my latest emails from the finance team.”
* “List unread emails from yesterday.”
* “Find emails from:[name] subject:[keyword] after:2025-10-01.”

Analysis and reporting

* “Create a table of sender, subject, and date for emails about [topic] in the last 7 days.”
* “Identify action items from the last three emails about [project].”

For more examples, see: [Plugin use cases and prompts](https://help.openai.com/articles/12084614).

## Capabilities and permissions

### What it can do

* Search and retrieve messages from the signed-in user’s mailbox, including metadata such as subject, sender, recipients, timestamps, and plain-text body.
* Support keyword and structured message searches such as from:, subject:, and date filters.
* Return full message text for search results.
* Search relevant people, work or school directory users, and saved mailbox contacts.
* List and retrieve Outlook contacts and contact folders.
* Create, update, and delete Outlook contacts and contact folders when actions are enabled.

### Requested permissions

Some actions require Microsoft permissions that a Microsoft Entra administrator must approve for your organization. If a required permission is missing, you may see an error when connecting the app or using the action.

Granting a Microsoft permission does not automatically enable every Outlook action. A workspace administrator must review each Outlook app’s action settings and enable only the actions the organization permits. If **Configure Microsoft permissions** appears in **Admin > Plugins**, select it to review the combined permission request for enabled Microsoft apps.

Under **Actions**, administrators can enable the supported read or write actions their organization permits. Under **New actions**, select:

* **Enable all new actions**
* **Only enable new read actions**
* **Disable new actions**

If new actions require additional Microsoft permissions, members may need to reconnect after those permissions are approved.

### Required Microsoft app permissions

Some actions in the Outlook Email, Outlook Calendar, Microsoft Teams, and SharePoint apps require Microsoft Graph permissions that a Microsoft Entra administrator must grant for the organization. A ChatGPT workspace owner or admin and a Microsoft Entra administrator may be different people, so coordinate with the person who can grant organization-wide consent.

### Review permissions in ChatGPT

If your workspace still uses the **Apps** settings page, follow these steps for the Microsoft app you want to review:

1. Sign in to ChatGPT as a workspace owner or admin.
2. Open **Apps** in your workspace settings and select the Microsoft app you want to review.
3. Open the app’s more options menu (•••) and select **Manage app**.
4. Select **Microsoft permissions**.
5. Review each Microsoft Graph permission and the ChatGPT actions listed beneath it. **Upcoming** means an action is included for advance permission review but is not currently available. **Approved** means the permission was included in the last successful approval flow completed through ChatGPT for that app and workspace.
6. Select only the permissions your organization wants to include in the request. The available permissions and actions can differ by app. If your organization does not want to grant a permission, leave it out of the request and keep every action that depends on it disabled.

### Complete the request in Microsoft Entra

1. Select **Review permissions in Microsoft Entra**. If Microsoft Entra does not open, allow pop-ups for ChatGPT and try again.
2. Sign in with a Microsoft Entra administrator account that can grant organization-wide consent.
3. Confirm that the correct organization and the verified **ChatGPT / OpenAI, L.L.C.** application are shown.
4. Review the selected permission request. The Microsoft Entra confirmation screen does not provide per-permission checkboxes: select **Accept** to grant the complete selected request, or select **Cancel** to make no change.
5. Return to ChatGPT and confirm that the approval flow completed.

Review the action settings for every enabled Microsoft app. Microsoft permissions are granted to the Entra tenant and OpenAI application, and a single permission request in ChatGPT may cover multiple apps.

### After permissions are approved

Microsoft permission approval does not enable ChatGPT actions or connect an individual user’s Microsoft account. Workspace owners and admins must separately enable the actions they want to make available. Users may also need to connect or reconnect their Microsoft account after permissions change.

If an action still does not work, confirm that:

1. The action is enabled in the ChatGPT workspace’s app settings.
2. The permission grant still exists in Microsoft Entra.
3. The user’s Microsoft connection has been created or refreshed with the required permissions.

If an Entra administrator later changes or revokes the grant directly in Microsoft, review the grant in Entra and rerun the ChatGPT approval flow.

offline\_access

User.Read

Mail.Read

Mail.ReadWrite

Mail.Read.Shared

Mail.ReadWrite.Shared

Mail.Send

Mail.Send.Shared

MailboxSettings.Read

MailboxSettings.ReadWrite

People.Read

User.ReadBasic.All

Contacts.Read

Contacts.ReadWrite

For supported shared or delegated mailboxes, ChatGPT can read messages, browse folders, mark messages as read or unread, move messages, and send plain-text email from or on behalf of the mailbox. These actions depend on your Microsoft permissions and workspace app settings. Give ChatGPT the exact mailbox address when making your request.

### Known limitations

* If an email is missing from the results, try a narrower date range and a distinctive sender, subject, or keyword.
* A broad search or summary may return incomplete results or an error. Coverage depends on the query and the results retrieved.
* For a large request, split the date range into smaller periods and ask ChatGPT to search each one.
* Your workspace owner or admin may restrict connections to Outlook accounts from an approved set of domains.
* The MailboxSettings.Read scope is required to provide answers in the user's time zone and reference mailbox categories.
* Attachments from messages in shared or delegated mailboxes can’t currently be retrieved. The list\_attachments and fetch\_attachment actions work only with messages in the signed-in user’s mailbox.

# Outlook Calendar app

The Outlook Calendar app lets ChatGPT read and search calendar events and availability. It also supports actions on shared calendars, subject to your Microsoft permissions and workspace app settings. When enabled, the app can look up people and create or manage Outlook contacts and contact folders.

For account setup and authorization, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

## Example use cases and prompts

Communication and writing

* “Summarize my next three meetings, including attendees and locations.”
* “Draft a message to reschedule my 2 pm sync with [name].”

Organization and productivity

* “What is on my schedule this afternoon?”
* “Find my sync with the design team.”
* “Show meetings from yesterday between 1 pm and 5 pm.”

Analysis and reporting

* “Create a table of meeting title, organizer, date/time, and attendees for meetings about [topic] in the next 7 days.”

For more examples, see: [Plugin use cases and prompts](https://help.openai.com/articles/12084614).

## Capabilities and permissions

### What it can do

* Return event metadata such as title, start and end time, location, description, and attendees.
* Filter calendar searches by date range, keywords, or participant names.
* Read basic availability and scheduling information.
* Read delegated or shared calendars, events, calendar views, permissions, and meeting-time suggestions.
* Create, update, RSVP to, cancel, or delete events on supported shared calendars, and add small attachments to those events, when the required permissions and actions are enabled.
* Search relevant people, work or school directory users, and saved mailbox contacts.
* List, retrieve, create, update, and delete Outlook contacts and contact folders when actions are enabled.

### Requested permissions

offline\_access

User.Read

Calendars.Read

Calendars.ReadWrite

Calendars.ReadWrite.Shared

MailboxSettings.Read

Calendars.Read.Shared

People.Read

User.ReadBasic.All

Contacts.Read

Contacts.ReadWrite

Specify the target calendar in your request. Access to a shared calendar does not guarantee that every calendar action is available; Microsoft permissions and workspace app settings still apply.

### Known limitations

* Supported actions can differ between personal, shared, and delegated calendars. Shared-calendar write support does not mean that the same actions are available for every calendar.
* For more targeted results, specify a date range and distinctive meeting details, such as the title, organizer, or attendees. Search results may not include every matching event.
* Your workspace owner or admin may restrict connections to Outlook accounts from an approved set of domains.
* The MailboxSettings.Read scope is required to provide answers in the user's time zone.
