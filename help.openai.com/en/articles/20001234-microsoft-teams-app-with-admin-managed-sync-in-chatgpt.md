<!-- source: https://help.openai.com/en/articles/20001234-microsoft-teams-app-with-admin-managed-sync-in-chatgpt -->

# Microsoft Teams app with admin-managed sync in ChatGPT

Use Microsoft Teams in ChatGPT with admin-managed sync for your workspace.

Updated: 2 days ago

Use Microsoft Teams in ChatGPT with admin-managed sync for your workspace.

# Overview

The Microsoft Teams app with sync lets ChatGPT Enterprise workspace owners and admins connect the Microsoft Teams app once for their workspace and enable sync, **without the user having to do any self service setup**. After owner or admin enablement, ChatGPT indexes supported Microsoft Teams messages and conversation metadata so members can ask questions and get answers from Teams content they already have permission to access. Once enabled, ChatGPT can automatically reference Microsoft Teams when relevant.

***Note:*** *The sync option for the Microsoft Teams app is available only for Enterprise and Edu workspaces and supports only admin-managed deployment through “Deploy to your team.” For a self-service option without sync, see* [*Microsoft Teams app for ChatGPT.*](/en/articles/12552368-microsoft-teams-app-for-chatgpt) *Workspace owners and admins can allow members to use the self-service Microsoft Teams app, the admin-deployed synced option described in this article, or both.*

* **Type:** App with sync
* **Where you can use it:** Chat
* **Setup type:** Admin-managed deployment for eligible Enterprise and Edu workspaces

# Example use cases and prompts

## Communication and writing

Use Microsoft Teams conversations as source material for drafting, summarizing, and finding follow-ups.

* “Summarize Teams conversations about [project] from the past week. Include key decisions, open questions, and people or teams mentioned in the retrieved messages.”
* “Draft an executive update using Teams conversations about [launch], with citations to the most relevant conversations.”

## Organization and productivity

Find relevant conversations and organize them by time, topic, or next action.

* “Catch me up on Teams conversations from last week about [project]. What changed, what follow-ups are suggested by the retrieved messages, and what are the next steps?”
* “Find Teams messages where [customer, initiative, or incident] was discussed and organize them into a timeline with dates and source links.”

## Analysis and reporting

Use Teams conversations as context for retrospectives, planning, and cross-functional reporting.

* “Identify blockers mentioned in Teams about [project] this month and group them by theme.”
* “Create a table of decisions and open questions from Teams conversations about [program], including dates and source links when available.”

## What it can access

* Supported Microsoft Teams messages and conversation metadata exposed through the connected Microsoft tenant
* Message text and metadata, such as sender or author information where available, timestamps, and source links
* Conversation membership and group membership information needed to enforce Microsoft Teams permissions

## What it can do

* Sync supported Microsoft Teams content into ChatGPT so ChatGPT can retrieve relevant Teams context when answering questions
* Let owners and admins choose which Teams content to sync and apply a Microsoft Purview sensitivity label filter
* Respect Microsoft Teams and Microsoft 365 permissions so members only receive content they already have permission to access
* Respect ChatGPT workspace access controls, including role-based access control where available
* Keep synced message content and permission information updated after the initial sync

## Limitations

* The Microsoft Teams app with sync is read only. It does not let ChatGPT send messages, create chats or channels, create tasks, list every team or channel, list every member of a conversation, or perform other live Microsoft Teams actions.
* It does not separately search Teams attachments, files, videos, or meeting recordings unless their text appears in supported message content.

# Microsoft permissions requested

The Microsoft Teams app with sync requests Microsoft Graph permissions so ChatGPT can sync the approved Teams and directory data in the background after a Microsoft Entra admin grants consent. Most requested permissions are application permissions, so ChatGPT can keep approved Teams and directory data synced without each user signing in individually. SensitivityLabels.Read.All is delegated and is used to read sensitivity labels. All requested permissions require Microsoft Entra admin consent.  
  
| Permission | What it allows | | Channel.ReadBasic.All | Read the names and descriptions of all channels | | ChannelMember.Read.All | Read the members of all channels | | ChannelMessage.Read.All | Read all channel messages | | Chat.Read.All | Read all chat messages | | Directory.Read.All | Read directory data | | Group.Read.All | Read all groups | | GroupMember.Read.All | Read all group memberships | | SensitivityLabels.Read.All | Read sensitivity labels | | Team.ReadBasic.All | Get a list of all teams | | TeamMember.Read.All | Read the members of all teams | | User.Read.All | Read all users’ full profiles |

# Deploying Microsoft Teams app with sync to your team

The Microsoft Teams app with sync is deployed by a ChatGPT workspace owner or admin. Members do not need to connect Microsoft Teams individually for admin-managed sync.

## Before you begin

* Make sure Microsoft Teams is enabled for the workspace.
* Use a Microsoft Teams admin account that can grant Microsoft Entra admin consent.
* Decide which Teams, channels, or chats should be included in the sync scope.

## Starting deployment

1. Go to **Workspace settings** > **Apps**.
2. Find Microsoft Teams and make sure the app is enabled for the workspace.
3. Select **Configure access** to control which workspace roles can use Microsoft Teams in ChatGPT, if role-based access control is available for your workspace.
4. Select **Enable Sync** for Microsoft Teams.
5. Select **Deploy to your team**. Microsoft Teams app with sync does not offer a self-service sync option.
6. Continue to the Microsoft sign-in flow and sign in with a Microsoft Teams admin account using the same email shown in ChatGPT during setup.
7. Review and approve the requested Microsoft permissions.

## Choosing what to sync

1. Use the Teams scope picker to choose which Teams content to include in sync.
2. If your Microsoft tenant uses Microsoft Purview sensitivity labels, apply a Microsoft Purview sensitivity label filter.

Complete setup.

## Sync scope

During setup, owners and admins can choose the Teams content ChatGPT should sync. The Teams scope picker and Microsoft Purview filter define the admin-managed sync scope, while Microsoft Teams permissions still apply when members ask questions in ChatGPT. Use the Teams scope picker to select which Teams, channels, or chats are included in sync. If your Microsoft tenant uses Microsoft Purview sensitivity labels, use the Microsoft Purview filter to limit sync by sensitivity label and keep Teams sync aligned with your organization’s information protection policy.  
  
After setup completes, ChatGPT starts syncing Microsoft Teams content and permission information for the selected scope. Initial sync can take time, and some results may be missing until sync is complete. After sync is available, members can ask questions about Microsoft Teams content they already have permission to access without authenticating individually or manually enabling sync.

# Managing sync scope and access

* Owners and admins can update the Teams scope picker selection and Microsoft Purview sensitivity label filter later from **Workspace settings > Apps**.
* Selecting a narrower sync scope reduces what ChatGPT can retrieve. Content outside the selected Teams scope or excluded by the Purview filter is not synced.
* If both the regular Microsoft Teams app and Microsoft Teams app with sync are enabled, reads may come from either app. Microsoft Purview filters apply only to the synced deployment, not to the regular Microsoft Teams app. To make sure the synced scope is honored, owners and admins can disable read actions for the regular Microsoft Teams app in **Workspace settings > Apps**.
* Permission changes apply after sync refreshes, so updates may take time to appear in ChatGPT.
* Initial sync can take time. In smaller environments, content may begin appearing within hours; in larger environments, full sync can take longer.
* During partial sync, some recent content may already be available while older or less frequently accessed content is still syncing. Some results may be missing until full sync completes.
* The Teams chat sync path indexes message text, message previews, timestamps, conversation metadata, author information where available, and source links. It does not separately index attachments, files, videos, or meeting recordings shared in Teams unless their text appears in supported message content.

# Frequently asked questions

## What happens if Microsoft Teams sync is not enabled?

If Microsoft Teams sync is not enabled, ChatGPT will not index Microsoft Teams content in advance for the workspace. Users may still be able to use the standard Microsoft Teams app experience if it is enabled for the workspace and available to them, but the admin-managed sync experience will not be active.

## Can owners and admins control who has access to the Microsoft Teams app with sync?

Yes. Workspace owners and admins can manage app availability from Workspace settings > Apps. In Enterprise and Edu workspaces, they can also use role-based access control to control which roles can access Microsoft Teams in ChatGPT.

## Will users see Microsoft Teams content they do not have permission to access?

No. Microsoft Teams permissions are respected. ChatGPT uses synced conversation and membership information so each member can only retrieve Teams content they are already allowed to access in Microsoft Teams.

## When will new or updated Teams content be reflected?

After the initial sync, Microsoft Teams content and permission information are refreshed periodically. New messages, updates, and permission changes may take some time to appear in ChatGPT.

## Can users disconnect the admin-managed Microsoft Teams sync?

No. The Microsoft Teams sync connection is managed by the workspace owner or admin. Members do not need to connect or disconnect it individually.

## Can ChatGPT send messages or create items in Microsoft Teams through sync?

No. Microsoft Teams app with sync is used to retrieve synced Teams message content and metadata in ChatGPT. It does not let ChatGPT send Teams messages, create chats or channels, create tasks, or perform other live Microsoft Teams actions.

## How is Microsoft Teams app with sync different from the regular Microsoft Teams app?

The regular Microsoft Teams app lets a user connect their own Microsoft Teams account for on-demand access, depending on workspace settings. Microsoft Teams app with sync lets an eligible workspace owner or admin connect once and deploy sync for the workspace. Users do not need to complete personal OAuth setup to benefit from synced Teams content they can already access.

## Is there a Microsoft Teams self-service sync setup?

No. Microsoft Teams app with sync only supports admin-managed deployment through **Deploy to your team**.

## Can owners and admins choose which Teams, channels, or chats are synced?

Yes. During setup, owners and admins can choose which Teams, channels, or chats are included in the sync scope. If the Microsoft tenant uses Microsoft Purview sensitivity labels, owners and admins can also apply a Purview filter. ChatGPT only indexes supported Teams messages and conversation metadata that are in scope, and users still only retrieve content they have permission to access in Microsoft Teams.

## Do users need to manually enable Microsoft Teams in each chat?

No. After admin-managed sync is set up, users do not need to authenticate individually or manually enable sync. They can ask questions about Microsoft Teams content, and ChatGPT can reference synced Teams content when relevant.

## How does ChatGPT know which users should have access?

ChatGPT syncs Microsoft Teams user, conversation, and membership information and maps synced Teams users to ChatGPT workspace users so permissions can be enforced. Users only receive content they are allowed to access in Microsoft Teams.

## Can owners and admins change what is synced later?

Yes. Owners and admins can manage the Microsoft Teams app and sync connection from Workspace settings > Apps, including disabling the app or sync connection. They can also update the Teams scope picker selection and Microsoft Purview filter. Changes apply after sync refreshes.

## Can we enable both the regular Microsoft Teams app and Microsoft Teams app with sync?

Yes. The regular Microsoft Teams app and the admin-managed sync experience are separate setup paths and can both be enabled. If both are enabled, reads may come from either app. Microsoft Purview filters apply only to the synced deployment, not to the regular Microsoft Teams app. If owners and admins need the synced scope to be enforced for reads, they can disable read actions for the regular Microsoft Teams app in Workspace settings > Apps.

## How does Microsoft Teams app with sync appear in Workspace settings > Apps?

After the admin-managed sync deployment is connected, owners and admins see a secondary Microsoft Teams row for the synced deployment. Action controls remain on the regular Microsoft Teams app; the synced deployment does not have separate action controls.
