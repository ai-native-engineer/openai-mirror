<!-- source: https://help.openai.com/en/articles/12512241-outlook-email-and-calendar-app-for-chatgpt -->

# Outlook Email and Calendar app for ChatGPT

Learn how to use the Outlook Email and Calendar apps with ChatGPT, including new support for shared/delegated mailboxes and calendars via dedicated actions and scopes.

Updated: 14 days ago

# Outlook Email app

Make ChatGPT more actionable with your own Outlook mailbox, available on demand. The Outlook Email app enables ChatGPT to securely connect to your inbox so you can search messages, pull key details, and reference content in chat.  
  
  
[Learn more about connecting a new app](/en/articles/11487775).

## Example use cases and prompts

**Communication and writing**

* “Summarize the latest update from [sender] about this project.”
* “Draft a reply that covers the three main points in the last email from [sender].”

**Organization and productivity**

* “Show my latest emails from the finance team.”
* “List unread emails from yesterday.”
* “Find emails from:[name] subject:[keyword] after:2025-10-01.”

**Analysis and reporting**

* “Create a table of sender, subject, and date for emails about [topic] in the last 7 days.”
* “Identify action items from the last three emails about [project].”

[Learn more about app use cases and prompts.](/en/articles/12084614)

## Capabilities and Permissions

### What it can do

* Searches and retrieves messages from the signed-in user’s mailbox (read-only), including metadata such as subject, sender, recipients, timestamps, and plain-text body.
* Supports keyword and structured searches such as from:, subject:, and date filters.
* Fetch endpoints provide full message text for results returned by search.

### Permission requested (scopes)

***Note:*** *The app requires the following scopes to be reviewed and approved by your Microsoft Entra admin. If the scopes are not approved by your Entra admin, you may see an error when trying to connect the app within ChatGPT.*   
  
*Approval of scopes does not immediately make all actions available to users. Admins and owners must still review app actions in* ***Workspace settings > Apps*** *for the app. In* ***Action control****, admins can choose how the app's current actions are handled by allowing all actions, allowing only read actions, or selecting a custom set of actions.*  
  
*If admins select* ***Custom****, they can also choose how actions added later are handled by selecting* ***Enable all new actions****,* ***Only enable new read actions****, or* ***Disable new actions****. If admins select* ***Disable new actions****, they must review and enable new actions before users can use them. After admins allow additional actions, users may need to reconnect the app to use them.*

```
offline_access  
User.Read  
Mail.Read  
Mail.ReadWrite  
Mail.Read.Shared   
Mail.ReadWrite.Shared   
Mail.Send  
Mail.Send.Shared   
MailboxSettings.Read   
MailboxSettings.ReadWrite
```

Shared/delegated mailbox actions are supported via dedicated actions and scopes. You must provide the exact mailbox owner email (UPN) when accessing shared mailboxes.

### Known limitations

* Search precision follows Microsoft Graph indexing latency — very recent emails may take a short time to appear.
* Some broad or long-running requests (for example, summarizing all emails over an extended period of time) may exceed service limits enforced by Microsoft. In these cases, ChatGPT may return an error.
* **Workaround:** Narrowing the date range or breaking the request into smaller queries often resolves the issue.
* Your workspace owner or admin may restrict which Outlook accounts you can connect, to an approved set of domains.
* `MailboxSettings.Read` scope is required to provide answer in the user's timezone and reference mailbox categories.
* Outlook write actions are not available when using the app through Company Knowledge.

# Outlook Calendar app

The Outlook Calendar app allows ChatGPT to read and search a user’s calendar events using Microsoft Graph APIs. It powers capabilities like summarizing upcoming events or finding specific meetings, always in a read-only capacity.  
  
  
[Learn more about connecting a new app](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

## Example use cases and prompts

**Communication and writing**

* “Summarize my next three meetings, including attendees and locations.”
* “Draft a message to reschedule my 2 pm sync with [name].”

**Organization and productivity**

* “What is on my schedule this afternoon?”
* “Find my sync with the design team.”
* “Show meetings from yesterday between 1 pm and 5 pm.”

**Analysis and reporting**

* “Create a table of meeting title, organizer, date/time, and attendees for meetings about [topic] in the next 7 days.”

[Learn more about app use cases and prompts.](/en/articles/12084614-connector-use-cases-and-prompts)

## Capabilities and Permissions

### What it can do

* Returns metadata such as event title, start/end time, location, description, and attendees.
* Search queries can filter by date range, keywords, or participant names.

### Permission requested (scope)

```
offline_access  
User.Read  
Calendars.Read  
Calendars.ReadWriteCalendars.ReadWrite.Shared  
MailboxSettings.Read
```

Note: shared/delegated calendar actions are supported via dedicated actions and scopes. Existing personal calendar behavior remains unchanged.

### Known limitations

* Event descriptions are read-only
* Search precision follows Microsoft Graph API, which is limited.
* Your workspace owner or admin may restrict which Outlook accounts you can connect, to an approved set of domains.
* `MailboxSettings.Read` scope is required to provide answers in the user's timezone.
* Outlook write actions are not available when using the app through Company Knowledge.
