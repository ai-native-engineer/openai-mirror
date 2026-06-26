<!-- source: https://help.openai.com/en/articles/12552368-microsoft-teams-app-for-chatgpt -->

# Microsoft Teams app for ChatGPT

Updated: 13 days ago

Make ChatGPT more actionable with your Microsoft Teams chats, available on demand. The Teams app enables ChatGPT to securely search your 1:1 and group chats so you can surface relevant conversations and reference them in chat.  
  
  
[Learn more about connecting apps](/en/articles/11487775)

## Example use cases and prompts

**Communication and writing**

* “Summarize my recent chat with the sales team.”
* “Draft a reply that covers the three main points in the last email from [sender].”

**Organization and productivity**

* “Show my latest emails from the finance team.”
* “List unread emails from yesterday.”
* “Find emails with [keyword] from last week.”

**Analysis and reporting**

* “Create a table of sender, subject, and date for emails about [topic] in the last 7 days.”
* “List links that were shared in the chat with [team] over the past 7 days.”

[Learn more about app use cases and prompts.](/en/articles/12084614)

## Capabilities and Permissions

### What it can do

* Returns metadata including subject, sender, recipients, timestamps, and plain-text body.
* Supports keyword and structured searches such as from:, subject:, and date filters.
* Fetch endpoints provide full message text for results returned by search.

### Permission requested (scope):

***Note:*** *The app requires the following scopes to be reviewed and approved by your Microsoft Entra admin. If the scopes are not approved by your Entra admin, you may see an error when trying to connect the app within ChatGPT.*   
  
*Approval of scopes does not immediately make all actions available to users. Admins and owners must still review app actions in* ***Workspace settings > Apps*** *for the app. In* ***Action control****, admins can choose how the app's current actions are handled by allowing all actions, allowing only read actions, or selecting a custom set of actions.*  
  
*If admins select* ***Custom****, they can also choose how actions added later are handled by selecting* ***Enable all new actions****,* ***Only enable new read actions****, or* ***Disable new actions****. If admins select* ***Disable new actions****, they must review and enable new actions before users can use them. After admins allow additional actions, users may need to reconnect the app to use them.*

```
offline_access  
User.Read  
User.Read.All  
Chat.Read  
ChatMessage.Send  
ChannelMessage.Read.All  
ChannelMessage.Send  
Team.ReadBasic.All  
Channel.ReadBasic.All  
Chat.Create  
Channel.Create  
Tasks.Read  
Tasks.ReadWrite
```

### Workspace domain restriction

Business and Enterprise/Edu owners and admins can restrict which email domains members can use to connect the Teams app to ChatGPT by limiting connected accounts to an approved set of domains.  
  
Configure this option by selecting **Manage domains** for the Microsoft Teams app from Workspace settings → Apps.

### Known limitations

* Results limited to messages where the authenticated user is a participant.
