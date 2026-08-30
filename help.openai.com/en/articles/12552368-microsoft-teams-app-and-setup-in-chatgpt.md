<!-- source: https://help.openai.com/en/articles/12552368-microsoft-teams-app-and-setup-in-chatgpt -->

# Microsoft Teams app and setup in ChatGPT

Connect Microsoft Teams to ChatGPT, review Microsoft permissions, and configure administrator-managed Teams sync for an eligible workspace.

The Microsoft Teams app can search and reference Teams content available to your connected Microsoft work or school account. Supported live actions depend on your app permissions and workspace settings. Eligible Enterprise and Edu administrators can separately configure administrator-managed indexing for approved Teams content.

Live access can support approved actions, such as sending a message or managing a Planner task. Administrator-managed sync is read-only and does not require each workspace member to connect a personal synced account.

For an overview of connected apps, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

## Availability

Microsoft Teams availability depends on your ChatGPT plan, location, workspace settings, Microsoft account, and your organization's Microsoft Entra policies.

Administrator-managed Microsoft Teams sync is available only in eligible Enterprise and Edu workspaces and supported regions. There is no individual or self-service Teams sync option.

For the workspace data residency regions that support administrator-managed Microsoft Teams sync, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

# Connect Microsoft Teams

1. Open **Plugins** or **Apps**, depending on the options available in your version of ChatGPT.
2. Find **Microsoft Teams** and select the option to connect your account.
3. Sign in with the Microsoft account you use for Teams.
4. Review the requested permissions and complete the Microsoft authorization flow.
5. Return to ChatGPT.

If your organization requires administrator consent, your Microsoft Entra administrator may need to approve the requested permissions before you can connect or use certain actions.

For general connection instructions, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Use Microsoft Teams in a conversation

After connecting Teams, you can ask ChatGPT to find information in conversations you already have permission to access.

Examples include:

* “Summarize the Teams conversations about the launch from the past week.”
* “Find the decisions and open questions from the project planning channel.”
* “Draft a status update using the latest messages from the incident response chat.”
* “Find my Planner tasks for this project and group them by owner.”

Depending on the permissions approved by your organization and the actions enabled in ChatGPT, the live Teams app may also:

* Search or retrieve messages from chats and channels.
* List teams, channels, chats, and other supported conversation details.
* Send or reply to Teams messages.
* Create supported chats or channels.
* Read, create, update, or delete supported Microsoft Planner tasks.
* Retrieve information from eligible scheduled Teams meetings.

Meeting transcript and recording features depend on your plan and Microsoft permissions. When available, transcript text can be retrieved only if a transcript exists and your Microsoft account can access it. Recording actions provide recording metadata, not the recording file contents.

ChatGPT may ask you to confirm an action before it sends a message, changes a task, or performs another action in Teams.

# Manage Microsoft Teams permissions

Microsoft Teams permissions determine which conversations and actions are available. ChatGPT does not grant access to teams, chats, channels, or meetings that your Microsoft account cannot access.

A ChatGPT workspace owner or administrator manages app availability and allowed actions. A Microsoft Entra administrator grants the Microsoft Graph permissions required by those actions. These roles may be held by different people.

For more information about workspace controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

## Review permissions for live Teams access

Depending on the enabled actions, the Microsoft Teams app may request permissions such as:

* User.Read, User.Read.All, or User.ReadBasic.All: Identify users and retrieve account information needed by supported actions.
* offline\_access: Maintain the authorized connection without requiring a new sign-in for every request.
* Chat.Read: Read chats available to the signed-in user.
* ChatMessage.Send: Send or reply to chat messages when those actions are enabled.
* ChannelMessage.Read.All: Read messages in channels the signed-in user is authorized to access.
* ChannelMessage.Send: Send or reply to channel messages when allowed.
* Team.ReadBasic.All and Channel.ReadBasic.All: Read basic team and channel information.
* Chat.Create and Channel.Create: Create supported chats or channels when those actions are enabled.
* Tasks.Read and Tasks.ReadWrite: Read or manage supported Microsoft Planner tasks.
* Calendars.Read and OnlineMeetings.ReadWrite: Resolve supported scheduled Teams meetings.
* OnlineMeetingTranscript.Read.All: Retrieve eligible meeting transcripts and transcript content.
* OnlineMeetingRecording.Read.All: Retrieve metadata for eligible meeting recordings.

Some advanced Teams actions may require additional Microsoft permissions. The exact permissions requested depend on the actions available and enabled in your workspace.

## Approve Microsoft permissions

These steps describe the **Plugins** administrator interface. If your workspace uses **Apps** administration, go to **Workspace settings > Apps**, select **Microsoft Teams**, and then select **Microsoft permissions**. Continue with the permission review and Microsoft approval below.

1. Sign in to ChatGPT as a workspace owner or administrator.
2. Go to **Admin > Plugins**.
3. Select **Configure Microsoft permissions** to review the combined request for your workspace’s Microsoft apps.
4. Review the permissions and the actions associated with each one.
5. Select only the permissions your organization wants to include in the request.

### Complete Microsoft administrator approval

1. Continue to Microsoft Entra and sign in with an administrator account that can grant organization-wide consent.
2. Verify the organization and the ChatGPT/OpenAI application.
3. Review the selected request, complete the Microsoft consent flow, and return to ChatGPT.

Approving a Microsoft permission does not automatically enable its related action. Workspace administrators must also review **Actions**, **Role access**, and related workspace settings. Members may need to reconnect their Microsoft account after new permissions are approved.

# Set up administrator-managed Microsoft Teams sync

Administrator-managed sync indexes approved Teams message content and conversation metadata for an eligible Enterprise or Edu workspace. A workspace administrator connects once for the organization; members do not configure individual synced connections.

The administrator-managed Teams index is read-only. It does not send messages, create chats or channels, manage Planner tasks, or perform other live Teams actions.

## Prepare the workspace and Microsoft tenant

Before starting:

* Confirm that administrator-managed Teams sync is available for your ChatGPT workspace and region.
* Sign in as a ChatGPT workspace owner or administrator.
* Use a Microsoft Teams administrator account that can grant the required Microsoft Entra consent.
* Decide which teams, channels, or chats should be included.
* Review any Microsoft Purview sensitivity-label requirements.
* Decide whether members should also retain access to the separate live Microsoft Teams app.

## Review permissions for administrator-managed sync

Administrator-managed Teams sync requests Microsoft Graph permissions so ChatGPT can process approved conversation content, user identities, and group membership. Most of these permissions are application permissions, which let the approved connection operate without requiring every member to sign in individually.

The requested permissions can include:

* Channel.ReadBasic.All: Read channel names and descriptions.
* ChannelMember.Read.All: Read channel membership.
* ChannelMessage.Read.All: Read supported channel messages.
* Chat.Read.All: Read supported chat messages.
* Directory.Read.All: Read directory data needed to map users and permissions.
* Group.Read.All: Read Microsoft 365 groups.
* GroupMember.Read.All: Read group memberships.
* SensitivityLabels.Read.All: Read Microsoft Purview sensitivity labels when label-aware configuration is used.
* Team.ReadBasic.All: Read basic information about teams.
* TeamMember.Read.All: Read team membership.
* User.Read.All: Read user profiles needed to match workspace members.

SensitivityLabels.Read.All uses delegated access. The other administrator-managed permissions are granted according to the Microsoft consent flow presented for your organization's configuration.

A Microsoft Entra administrator must approve the requested permissions. Granting the connection access to read approved Teams content does not allow workspace members to retrieve conversations they cannot already access in Microsoft Teams.

## Configure the administrator-managed connection

1. Sign in to ChatGPT as a workspace owner or administrator.
2. Go to **Admin > Plugins** and open the plugin that includes **Microsoft Teams**. If your workspace uses **Workspace settings > Apps**, select **Microsoft Teams** there.
3. Confirm that Microsoft Teams is enabled for the workspace.
4. Review **Role access** if your workspace supports role-based access controls.
5. If you see **Indexed search**, select **Set up**.

### Approve the source and finish setup

1. Sign in with the Microsoft Teams administrator account requested during setup.
2. Review and approve the Microsoft permissions in Microsoft Entra.
3. Choose the teams, channels, or chats your organization wants to include.
4. Apply a Microsoft Purview sensitivity-label filter when available and appropriate.
5. Complete setup and allow time for the initial index to be created.

If the Microsoft administrator account does not match the account requested by the setup flow, use an authorized account before continuing.

## Choose Teams content and sensitivity-label filters

The administrator's content selection and any Microsoft Purview filter define the scope of the administrator-managed Teams index. Content outside that selected scope is not indexed.

Microsoft Teams membership and Microsoft 365 permissions still determine which indexed conversations each member can retrieve.

The time needed for initial indexing depends on the amount of Teams content and the size of your organization. Large tenants may take longer, and the source might not be available until the initial index is ready.

After setup, messages and permission information refresh periodically. Recent messages, membership changes, or permission updates may take time to appear.

## Keep live actions and indexed content separate

The live Microsoft Teams app and administrator-managed Teams sync can both be enabled, but their controls are different:

* Live actions use the member's connected Microsoft account and the permissions approved for those actions.
* Administrator-managed sync uses the approved workspace connection and the administrator's selected indexing scope.
* Microsoft Purview filters applied to the indexed connection do not automatically limit a separate live Teams connection.
* Action parameter constraints do not apply to administrator-managed indexed data.
* Disabling a live action does not, by itself, disable an existing administrator-managed sync connection.

If your organization needs the administrator-managed content scope to control how Teams information is retrieved, review the live Teams app's read actions and disable any that conflict with your policy.

# Supported content and limitations

Administrator-managed Teams sync can index supported message text and conversation metadata, including timestamps, source links, author information when available, and the membership information required to enforce permissions.

It does not separately index Teams attachments, files, videos, or meeting recordings unless relevant text appears in supported message content.

Administrator-managed sync does not support:

* Sending or replying to Teams messages.
* Creating chats, channels, or teams.
* Creating or changing Planner tasks.
* Retrieving the contents of recording files.
* Setting up an individual or self-service synced connection.

Some of these actions may still be available through the separate live Teams app if your workspace allows them and your Microsoft account has the required permissions.

# Troubleshoot Microsoft Teams

For help with connection or permission errors, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

## Microsoft Teams does not appear

Confirm that the app is available to your account and that your workspace administrator has enabled it. In a managed workspace, check whether **Role access** or an approved-domain policy limits who can connect.

## Microsoft administrator approval is required

Ask a Microsoft Entra administrator to review the permissions associated with the Teams actions your organization wants to use. A ChatGPT workspace administrator can disable actions that depend on permissions your organization does not want to grant.

## A Teams action still does not work

Confirm that:

* The relevant action is enabled in the app's **Actions** settings.
* The corresponding Microsoft permission is still granted in Microsoft Entra.
* The intended Microsoft account is connected.
* The member can access the relevant Teams chat, channel, meeting, or Planner resource.
* The account has been reconnected if new Microsoft permissions were introduced.

## Synced Teams messages are missing

Check that the conversation is included in the administrator-managed scope, that it is not excluded by a sensitivity-label filter, and that the member belongs to the relevant chat, channel, or team. Allow time for initial indexing and later permission refreshes.

## Meeting transcripts or recordings are unavailable

Confirm that:

* The meeting is eligible.
* Your ChatGPT plan supports the requested feature.
* The signed-in Microsoft account can access the meeting.
* The required Microsoft permissions are approved.

Transcripts must exist before they can be retrieved. Recording actions provide metadata rather than recording file contents.

## Administrator-managed sync is unavailable

Verify that your workspace is eligible, that Teams sync is supported in your configured region, and that an authorized Microsoft administrator can approve the requested application permissions. There is no personal or self-service Teams sync option.

# FAQ

## Can I use Microsoft Teams without enabling sync?

Yes. When the Microsoft Teams app is available to your account, you can connect your Microsoft account for live access and approved actions. Administrator-managed sync is a separate workspace feature.

## Can I enable Teams sync for my own account?

No. Teams sync is available only through administrator-managed deployment in eligible workspaces.

## Can administrator-managed sync send Teams messages?

No. Administrator-managed Teams sync is read-only. Sending or replying to a message requires a separately enabled live Teams action and the appropriate Microsoft permissions.

## Can members see conversations they cannot access in Microsoft Teams?

No. Teams membership and Microsoft 365 permissions continue to determine what each member can retrieve.

## Can administrators choose which teams, channels, or chats are indexed?

Yes. Administrators can select the content included in the administrator-managed connection and apply supported sensitivity-label filters. Those restrictions apply to the index, not automatically to a separate live Teams connection.

## Do members need to connect their own Teams accounts for administrator-managed sync?

No. The administrator configures the workspace connection. A member may still connect their own Microsoft work account separately when live Teams actions are available.

## Are meeting recordings included in the administrator-managed Teams index?

No. The index covers supported messages and conversation metadata. Recording actions in the separate live Teams app can return recording metadata when the user is eligible and authorized, but they do not return the recording file contents.
