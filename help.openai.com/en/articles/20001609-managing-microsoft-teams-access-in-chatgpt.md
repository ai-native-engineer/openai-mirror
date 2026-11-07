<!-- source: https://help.openai.com/en/articles/20001609-managing-microsoft-teams-access-in-chatgpt -->

# Managing Microsoft Teams access in ChatGPT

Configure team access and sensitivity-label exclusions for the Microsoft Teams app in your ChatGPT workspace.

Updated: 19 days ago

Workspace owners and admins can allow selected Microsoft Teams teams, block selected teams, and exclude channels based on Microsoft Purview sensitivity labels.

These controls apply alongside each user's Microsoft permissions. They do not change Microsoft 365 permissions, team membership, or sensitivity labels.

In these settings, "group" means the Microsoft 365 group behind a team. It does not mean a Teams group chat.

## Availability

These controls are available in Enterprise workspaces where enabled. Confirm that you're in the intended ChatGPT workspace, that you're a workspace owner or admin, and that the app is enabled. If **Safety & Security Controls** is still missing, contact your OpenAI account team or [OpenAI Support](https://help.openai.com/articles/6614161). Include your workspace plan, your role, and the control you can't find.

## Before you begin

* Decide which teams your organization wants to allow or block.
* Gather their Microsoft 365 group IDs.
* For label exclusions, obtain each intended Microsoft Purview label's GUID, including any sublabels you want to exclude.
* If you plan to exclude teams by sensitivity label, confirm that your Microsoft administrator has approved Group.Read.All and that your ChatGPT administrator has enabled the corresponding action needed to read team sensitivity labels.
* Choose test accounts and channels that can confirm the intended access.

# Find and verify Microsoft 365 group IDs

Each team has the same ID as its backing Microsoft 365 group. Use that group's **Object ID**, rather than a tenant ID, channel ID, group-chat ID, or display name.

1. Sign in to the Microsoft Entra admin center for the organization that owns the team.
2. Go to **Entra ID > Groups**.
3. Select **All groups**, then select the Microsoft 365 group associated with the team.
4. Open **Properties** and copy **Object ID**.
5. Confirm the organization and the team's backing group before saving the ID in ChatGPT. If names are ambiguous or you can't access the group, ask your Microsoft administrator to verify it.

For Microsoft's instructions, see: [Managing Microsoft Entra groups](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups).

# Configure team access

1. Open Microsoft Teams in your workspace's app settings.
2. Open **Safety & Security Controls**.
3. Under **Microsoft Teams group access**, choose **Allowed groups** or **Blocked groups**.
4. Add the team group IDs. You can upload a CSV for a larger list.
5. Select **Save**.
6. Reopen the settings and confirm the saved mode and list.

Allowed teams include their existing and future owned channels. Blocked teams exclude their owned channels. Shared channels are evaluated using their owning team.

Allowed and blocked team lists cannot both contain entries. Clearing the last group entries removes the restrictions imposed by those group lists; other configured controls and user permissions still apply.

## Exclude teams by sensitivity label

1. Open **Safety & Security Controls** for Microsoft Teams.
2. Under **Excluded Microsoft Teams sensitivity labels**, add each label GUID you want to exclude.
3. Select **Save**.

The control checks labels assigned to the team's backing Microsoft 365 group. A matching exclusion blocks the team's channels even when the team is otherwise allowed.

Add each label explicitly, including sublabels. An empty exclusion list adds no label restrictions.

## Maintain a large team list

Use native Microsoft 365 group IDs. A CSV contains one group ID per row and can include an optional `group_id` header.

Uploads add unique entries to the draft. Select **Save** to apply them. Download the current list before making bulk changes.

Connecting an account can show available team names. The group IDs remain the policy identifiers.

# Test your configuration

Use non-sensitive test content. For write tests, use a test item and a harmless change.

1. Confirm that the test account can access each test channel directly in Microsoft Teams.
2. Start a new ChatGPT conversation and request content from a permitted team.
3. Request content from a blocked or unlisted team, according to your selected mode.
4. Test a channel whose backing team carries an excluded sensitivity label.
5. If members use supported writes to existing channels, test permitted and blocked write targets.
6. Include a direct message in your checks if your organization's policy needs to account for chat access.

Saved settings and Microsoft metadata can take time to refresh. Verify fresh permitted and blocked requests before relying on a tightened policy.

## If excluded content still appears

Confirm whether the response used a new request through Microsoft Teams. Information already in a conversation or Memory is not evidence that the app retrieved it again. Don't paste excluded content into the test prompt.

Reopen **Safety & Security Controls** and confirm the saved group mode, group IDs, and excluded label GUIDs. Check the channel's owning team, including for shared channels. Team controls don't exclude ordinary one-to-one, group, or meeting chats.

If a fresh app request still retrieves excluded content, contact your OpenAI account team or [OpenAI Support](https://help.openai.com/articles/6614161). Include the relevant saved restrictions, the affected team's group ID and channel identifier, the connected account and workspace, the test time and time zone, and what happened. Include a request ID if one is shown; otherwise, say it wasn't shown. Don't include the excluded content itself.

# Understand the limitations

* Team restrictions apply to channels owned by teams. They do not provide a separate on/off setting for direct messages or group chats.
* Team-label exclusions do not independently scan labels on individual messages or attached files.
* Separate meeting transcript and recording actions are not covered by these team controls. Manage those actions separately in the app's settings.
* When required team ownership or label information cannot be verified, the affected access is blocked.
* Changing these controls does not delete content already retrieved into conversations or remove saved memories. Manage conversations and Memory separately. For removal options, see: [Memory in ChatGPT](https://help.openai.com/articles/8590148) and [Deleting and archiving chats](https://help.openai.com/articles/8809935).

For connecting Microsoft Teams and reviewing available actions, see: [Microsoft Teams app and setup in ChatGPT](https://help.openai.com/articles/12552368).

# FAQ

## Does allowing a team give every workspace member access?

No. Content must satisfy the workspace policy and the connected user's Microsoft permissions.

## Do team restrictions block direct messages or group chats?

They do not exclude ordinary one-to-one, group, or meeting chats. **Microsoft Teams group access** refers to the Microsoft 365 group behind a team, not a group chat.

## Do label exclusions apply to unlabeled teams?

An unlabeled team remains eligible under the other configured controls and the user's Microsoft permissions.

## Can a label exclusion block an otherwise allowed team?

Yes. A matching label exclusion blocks the team's channels even if the team is on the allowed list.

## Do my former sync selections restrict live app access?

Use the current saved **Safety & Security Controls** policy to verify live app access. Don't rely on former sync selections or indexing status alone. Reopen the controls, review the saved restrictions, and update them if needed. Select **Save** after making changes, then test permitted and excluded content with fresh requests.
