<!-- source: https://help.openai.com/en/articles/20001608-managing-google-drive-access-in-chatgpt -->

# Managing Google Drive access in ChatGPT

Configure shared-drive restrictions and My Drive access for the Google Drive app in your ChatGPT workspace.

Updated: 19 days ago

Workspace owners and admins can control which Google Drive locations ChatGPT can use. You can allow selected shared drives, block selected shared drives, and separately allow or turn off My Drive access.

These controls apply to supported searches, file reads, and writes. Files must also be accessible to the connected user's Google account. Changing the ChatGPT policy does not change permissions in Google Drive.

## Availability

These controls are available in Enterprise workspaces where enabled. Confirm that you're in the intended ChatGPT workspace, that you're a workspace owner or admin, and that the app is enabled. If **Safety & Security Controls** is still missing, contact your OpenAI account team or [OpenAI Support](https://help.openai.com/articles/6614161). Include your workspace plan, your role, and the control you can't find.

## Before you begin

* Decide which shared drives your organization wants to allow or block.
* Gather their shared-drive IDs. Use IDs, not drive names or URLs.
* Decide whether members should be able to use files outside shared drives through **Allow My Drive**.
* Choose test files and accounts that can confirm the intended access.

# Find and verify shared-drive IDs

A shared-drive ID is also the ID of that drive's top-level folder.

1. Open the shared drive itself in Google Drive on the web.
2. If its address contains `/folders/`, copy the identifier after that segment, without any query parameters.
3. Confirm that you opened the shared drive's top-level folder, rather than a file or a folder inside it.

If you can't identify the drive, ask your Google Workspace administrator for its ID. Administrators can also use the Google Drive API to [list shared drives](https://developers.google.com/workspace/drive/api/guides/manage-shareddrives) and [verify a drive's ID and name](https://developers.google.com/workspace/drive/api/reference/rest/v3/drives/get).

# Configure shared-drive access

1. Open Google Drive in your workspace's app settings.
2. Open **Safety & Security Controls**.
3. Choose **Allowed drives** or **Blocked drives**.
4. Enter the shared-drive IDs, or upload a CSV.
5. Set **Allow My Drive** separately.
6. Select **Save**.
7. Reopen the settings and confirm the saved mode, list, and My Drive setting.

* **Allowed drives:** ChatGPT can use the listed shared drives, subject to the connected user's Google permissions. An empty list blocks all shared drives.
* **Blocked drives:** ChatGPT excludes the listed shared drives. An empty list excludes none.

Use one shared-drive mode at a time. Allowed and blocked shared-drive lists cannot be combined.

## Manage My Drive access

**Allow My Drive** is enabled by default. It covers files outside shared drives, including files shared from another person's My Drive.

This setting is independent of the shared-drive list. Turning it off does not block content in an otherwise permitted shared drive.

## Upload or download a list

A CSV contains one shared-drive ID per row. You can include an optional `drive_id` header. Shared-drive IDs are case-sensitive.

Uploads add unique IDs to the draft list. Select **Save** to apply them.

Download the current list before making bulk changes. The download includes the current draft, including unsaved edits.

## Resolve drive names

Connecting your Google account can show names for drives you can access. This is optional for entering and saving shared-drive IDs. An unresolved name does not, by itself, mean the policy was lost.

# Test your configuration

Use non-sensitive test content. For write tests, use a test item and a harmless change.

Use the same Google account for your tests that the workspace member will use in ChatGPT.

1. Confirm that the account can open each test file directly in Google Drive.
2. Start a new ChatGPT conversation and request a file from a permitted shared drive.
3. Request a file from an excluded shared drive. ChatGPT should not retrieve its contents.
4. Test a My Drive file against the saved **Allow My Drive** setting.
5. If members use supported write actions, test an approved write in a permitted location and a write targeting an excluded location.

Policy changes can take time to propagate. Verify fresh permitted and blocked requests before relying on a tightened policy.

## If excluded content still appears

Confirm whether the response used a new request through Google Drive. Information already in a conversation or Memory is not evidence that the app retrieved it again. Don't paste excluded content into the test prompt.

Reopen **Safety & Security Controls** and confirm the saved drive mode, IDs, and **Allow My Drive** setting. Verify that the test file is in the intended shared drive or My Drive location.

If a fresh app request still retrieves excluded content, contact your OpenAI account team or [OpenAI Support](https://help.openai.com/articles/6614161). Include the relevant saved restrictions, the affected file's ID or link, the connected account and workspace, the test time and time zone, and what happened. Include a request ID if one is shown; otherwise, say it wasn't shown. Don't include the excluded content itself.

# Understand the limitations

* Shared-drive controls apply to whole shared drives. They do not provide folder, individual-file, user, group, or Google Drive label exclusions.
* Shortcuts do not bypass a blocked location.
* The workspace policy does not grant a user access they lack in Google Drive.
* Changing content controls does not erase content already retrieved into conversations or saved memories. Retention and Memory controls are separate.

For connecting Google Drive and reviewing its permissions, see: [Google Drive app and setup in ChatGPT](https://help.openai.com/articles/10929079).

# FAQ

## Does allowing a shared drive give every workspace member access?

No. The file must satisfy both the workspace policy and the connected user's existing Google permissions.

## Does turning off My Drive also block files shared from another person's My Drive?

Yes. **Allow My Drive** covers files outside shared drives, including files shared from another person's My Drive.

## Does an empty list remove shared-drive restrictions?

It depends on the mode. An empty **Allowed drives** list blocks all shared drives. An empty **Blocked drives** list excludes none.

## Can group managers configure these settings?

A group-manager role alone does not grant access to these workspace-wide settings. Workspace owners and admins configure the policy.

## Do my former sync selections restrict live app access?

Use the current saved **Safety & Security Controls** policy to verify live app access. Don't rely on former sync selections or indexing status alone. Reopen the controls, review the saved restrictions, and update them if needed. Select **Save** after making changes, then test permitted and excluded content with fresh requests.
