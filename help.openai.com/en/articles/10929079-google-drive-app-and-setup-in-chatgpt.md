<!-- source: https://help.openai.com/en/articles/10929079-google-drive-app-and-setup-in-chatgpt -->

# Google Drive app and setup in ChatGPT

Connect Google Drive to ChatGPT, manage access to Google Docs, Sheets, and Slides, and configure administrator-managed sync for an eligible workspace.

The Google Drive app connects ChatGPT to files and folders your Google account can already access. Depending on the permissions you grant and the actions your workspace allows, you can search files, reference Google Docs, Sheets, and Slides, and use supported actions in your conversations.

Eligible workspace administrators can also configure administrator-managed sync to create an indexed Google Drive knowledge source. A personal or individual connection provides live access only; it does not create a personal synced index.

For an overview of connected apps, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

## Availability

Google Drive availability depends on your ChatGPT plan, location, workspace settings, and Google Workspace policies. If you belong to a managed workspace, your administrator may need to enable the app or approve the actions you want to use.

Administrator-managed sync is available only to eligible managed workspaces. Personal and individual ChatGPT accounts cannot configure Google Drive sync.

For the workspace data residency regions that support administrator-managed Google Drive sync, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

# Connect Google Drive

1. Open **Plugins** or **Apps**, depending on the options available in your version of ChatGPT.
2. Find **Google Drive** and select the option to connect your account.
3. Sign in to the Google account you want to use.
4. Review the Google permissions requested for the available actions.
5. Complete Google's authorization flow and return to ChatGPT.

If you have more than one Google account, connect the one that has access to the files you need. A managed workspace may also limit the email domains that members can connect.

For help with switching or disconnecting accounts, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Use Google Drive in a conversation

After connecting Google Drive, you can ask ChatGPT to find or work with files you have permission to access. Google Docs, Sheets, and Slides actions are available through the Google Drive app rather than separate apps.

Depending on your plan, permissions, and workspace settings, try prompts such as:

* “Find the latest project plan in my Google Drive and summarize the next steps.”
* “Compare the two budget spreadsheets I shared last week.”
* “Use the launch notes in my Google Drive to draft a short customer update.”
* “Update this document with the action items from our meeting.”

Actions that change a file, such as creating, updating, moving, sharing, or deleting it, require the corresponding Google permissions and must be available in your workspace. ChatGPT may ask you to confirm an action before carrying it out.

# Manage Google Drive permissions

Google permissions determine what the connected account can access. ChatGPT cannot use files that the connected Google account cannot open.

In a managed workspace, a ChatGPT administrator controls which Google Drive actions are available. A Google Workspace administrator separately controls whether the ChatGPT/OpenAI app is trusted or approved for the Google OAuth scopes those actions require. These roles may be held by different people.

For information about workspace action controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

If an action is enabled in ChatGPT but the corresponding Google scope is blocked, you may encounter an authorization error when connecting, reconnecting, or using the action. Your Google Workspace administrator can approve the required scope, or your ChatGPT workspace administrator can disable the action that depends on it.

The Google Drive app can request different permissions for reading files, viewing file metadata, or creating and updating files. Google Docs, Sheets, and Slides actions may require additional permissions for their respective file types.

For Google-specific privacy, permissions, and data-use details, including Memory and provider controls, see: [Google app data controls FAQ](https://help.openai.com/articles/10408842).

For general privacy guidance, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

# Set up administrator-managed Google Drive sync

Administrator-managed sync lets an eligible workspace index selected Google Drive content without requiring every member to set up a personal synced connection. A Google Workspace service account accesses approved content on behalf of an administrator, while Google Drive file and group permissions still determine which results each workspace member can see.

Before starting, confirm that:

* Your ChatGPT workspace is eligible for administrator-managed Google Drive sync.
* You are a ChatGPT workspace owner or administrator.
* A Google Workspace administrator can configure domain-wide delegation and approve the required scopes.
* Your organization permits the creation and secure handling of a Google Cloud service account key.
* The Google accounts used by workspace members can be matched to their ChatGPT workspace accounts.

Use the same Google Workspace domain for Google Drive and your ChatGPT workspace whenever possible. If those email addresses do not match, follow the account-matching guidance later in this article.

## Create a Google Cloud project and enable the required APIs

1. Sign in to Google Cloud with an account that can create a project in your organization's Google Workspace.
2. Create or select the project your organization will use for the ChatGPT connection.
3. Go to **APIs & Services** > **Library**.
4. Enable each of the following APIs:

* **Google Drive API**
* **Google Drive Activity API**
* **Admin SDK API**

## Create a service account and download its key

1. In Google Cloud, open **APIs & Services** and then **Credentials**.
2. Select **Create Credentials**, then **Service account**.
3. Enter a name and description for the service account, and complete setup.
4. Open the new service account and select **Keys**.
5. Select **Add Key**, then **Create new key**, and select **JSON** as the key type.
6. Download the JSON key and store it according to your organization's security policy.
7. Open the service account's details and record its unique ID. You will need this value when configuring domain-wide delegation.

ChatGPT does not require you to assign an additional Google Cloud IAM role to the service account solely to complete this connection. The service account receives the approved access through domain-wide delegation.

If Google Cloud says that service account key creation is disabled, contact your organization's Google Cloud administrator. Do not weaken an organization-wide security policy without the required internal approval. If approved, an administrator can configure an appropriate scoped exception for the project and then retry key creation.

## Configure domain-wide delegation

1. Sign in to the Google Admin console with an account that can manage **API controls**.
2. Open **Security**, then **Access and data control**, and then **API controls**.
3. Open **Manage Domain Wide Delegation** and select **Add new**.
4. Enter the service account's unique ID as the client ID.
5. Add the following comma-separated OAuth scopes: `https://www.googleapis.com/auth/admin.directory.group.readonly, https://www.googleapis.com/auth/admin.directory.group.member.readonly, https://www.googleapis.com/auth/admin.directory.user.readonly, https://www.googleapis.com/auth/admin.directory.user.alias.readonly, https://www.googleapis.com/auth/drive.activity.readonly, https://www.googleapis.com/auth/drive.metadata.readonly, https://www.googleapis.com/auth/drive.readonly, https://www.googleapis.com/auth/userinfo.profile, https://www.googleapis.com/auth/userinfo.email`
6. Select **Authorize**.

The directory scopes let ChatGPT evaluate user, alias, and group membership. The Drive scopes allow approved files, metadata, and activity to be indexed. The profile and email scopes help match the correct Google Workspace users and validate the administrator account.

## Configure a Google Workspace administrator account

1. In the Google Admin console, open **Directory**, and then select **Users**.
2. Create or identify the Google Workspace administrator account that the service account will act on behalf of.
3. Open the account's role assignments.
4. Assign the required **Groups Reader**, **User Management Admin**, and **Storage Admin** roles.
5. Save the changes.

You will provide this administrator account's email address to ChatGPT. Do not enter or share the administrator account's password with ChatGPT.

## Complete setup in ChatGPT

1. Sign in to ChatGPT as a workspace owner or administrator.
2. Go to **Admin > Plugins** and open the plugin that includes **Google Drive**. If your workspace uses **Workspace settings > Apps**, select **Google Drive** there.
3. Open the **Google Drive** settings. If you see **Indexed search**, select **Set up**.
4. Enter a display name for the administrator-managed connection if prompted.
5. Select **Upload key** and upload the Google Cloud service account's JSON key.
6. Enter the Google Workspace admin email address for the administrator account you configured.

### Choose the content and finish setup

1. Choose whether to include users' My Drives.
2. Choose which shared drives to include or exclude.
3. Select which workspace members can use the administrator-managed connection.
4. Complete setup and start the initial sync.

Google Drive sync is managed at the workspace level. Members do not create or enable their own individual synced Google Drive connections.

## Choose which shared drives to include

You can configure the shared-drive scope in one of three ways:

* Include all shared drives.
* Include most shared drives and exclude specific shared-drive IDs.
* Exclude shared drives by default and include only the shared-drive IDs you specify.

If the setup flow uses **Include by default** or **Exclude by default**, choose the option that matches your organization's intended scope. A shared drive's ID appears in its Google Drive URL.

Review whether users' My Drives should be included before starting sync. Some connection settings cannot be changed after indexing begins without recreating the connection.

## Match Google Workspace and ChatGPT accounts

Administrator-managed sync works best when each member uses the same primary work email address for Google Workspace and ChatGPT.

If your organization uses different domains, a Google Workspace administrator can add an alternate email address to the appropriate Google Workspace user:

1. In the Google Admin console, open **Directory**, and then select **Users**.
2. Open the user who needs access.
3. Add an alternate email address that matches the user's ChatGPT sign-in email.
4. Save the change and retry the connection.

The alternate address must be explicitly configured in Google Workspace. Gmail addresses created with a plus sign, such as alex+work@example.com, do not provide a supported workaround for account matching.

A personal Gmail address cannot serve as the administrator identity for an administrator-managed Google Workspace connection. Whether a personal Google account can use a separate live Google Drive app depends on the app’s current availability and account requirements.

# Understand sync timing and access

The initial index can take hours or longer depending on how many files and shared drives are in scope. Some content may become available before the entire index finishes.

After indexing, ChatGPT refreshes approved content and permissions periodically. Updates to files, sharing permissions, or group membership may take time to appear.

Administrator-managed sync does not give a member access to files they cannot already access in Google Drive. Shared-drive inclusion also does not override Google Drive file permissions.

If both live Google Drive access and administrator-managed sync are enabled, the two experiences have different permissions and controls. Live actions use the member's connected Google account. Administrator-managed sync uses the workspace-managed service account and the administrator's selected indexing scope.

# Troubleshoot Google Drive

For general connection issues, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

## Google Drive does not appear

Check that Google Drive is available for your plan and location, and confirm that your workspace administrator has enabled the app. If your organization restricts account domains, use an approved Google account.

## Google authorization is blocked

Ask your Google Workspace administrator to review whether the ChatGPT/OpenAI app is trusted or approved for the Google scopes required by your enabled actions. Ask your ChatGPT administrator to disable actions that require scopes your organization does not approve.

## Administrator-managed setup cannot verify the administrator

Confirm that:

* The service account's client ID is authorized for domain-wide delegation.
* Every required OAuth scope is included, including userinfo.email and userinfo.profile.
* The administrator email belongs to the same Google Workspace.
* The Google Workspace administrator account has the required directory and storage roles.
* The uploaded JSON key belongs to the intended service account.

## Files are missing from results

For administrator-managed sync, check that:

* The file is within an included My Drive or shared drive.
* The member has permission to open it in Google Drive.
* The initial sync has had time to process it.

For live access, confirm that the correct Google account is connected.

## A file appears, but ChatGPT cannot use its contents

Finding a Google Drive filename or file details does not confirm that ChatGPT retrieved the contents or can analyze them for the task you requested.

For supported-format checks and next steps, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

## A member cannot access the administrator-managed connection

Verify that the member is included in the connection's workspace access settings and that their ChatGPT email can be matched to an eligible Google Workspace account or configured alias.

# FAQ

## Can I enable Google Drive sync for my personal ChatGPT account?

No. Individual Google Drive sync is no longer available. You can still use a supported live Google Drive connection when it is available to your account. Administrator-managed sync requires an eligible workspace.

## Do members need to connect Google Drive individually for administrator-managed sync?

No. An administrator configures the workspace connection and selects who can use it. A member may still connect their own Google account separately when live Google Drive actions are available.

## Can ChatGPT access Google Docs, Sheets, and Slides?

Yes. Supported Google Docs, Sheets, and Slides capabilities are available through the Google Drive app. Access depends on the connected account, enabled actions, and approved Google permissions.

## Can an administrator limit which shared drives are indexed?

Yes. The administrator can include all shared drives, exclude selected shared drives, or include only selected shared drives. Google Drive file and group permissions still apply.

## Does disconnecting my Google account remove my workspace's administrator-managed index?

No. Disconnecting your own live Google Drive connection removes access through that connection, but it does not delete a separate administrator-managed workspace index. Only a workspace administrator can manage the workspace-level sync connection.
