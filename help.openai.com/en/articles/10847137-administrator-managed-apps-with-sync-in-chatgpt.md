<!-- source: https://help.openai.com/en/articles/10847137-administrator-managed-apps-with-sync-in-chatgpt -->

# Administrator-managed apps with sync in ChatGPT

Learn how eligible workspaces index approved app content and how administrator-managed sync differs from connecting an individual app account.

Administrator-managed app sync lets an eligible workspace owner or administrator connect a supported source and make approved content available for indexed search in ChatGPT.

ChatGPT uses indexed content to find relevant information from the configured source. Source permissions, administrator-selected scope, workspace restrictions, and the availability of the app still apply.

Connecting an app account for live access is a separate experience. Individually authorized app sync is no longer available.

For help connecting a provider account without sync, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Check availability

Administrator-managed sync depends on your workspace plan, administrator settings, supported provider, configured region, and the ChatGPT interface you use. Not every app or workspace supports indexing.

Supported administrator-managed sources may include Google Drive, SharePoint, and Microsoft Teams when those options are available for your workspace and region. Confirm eligibility in the provider’s current setup article.

A source listed as an app or plugin is not necessarily available for administrator-managed sync. Ordinary app connections, actions, and indexed search may have different availability and permissions.

For workspace controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

## Data residency

The regions below refer to your workspace’s configured data residency region, not your physical location. For eligible workspaces with data residency enabled, new administrator-managed sync connections are supported in the following regions:

| **App** | **Supported workspace data residency regions** |
| --- | --- |
| Google Drive | Australia, Canada, Europe (EEA + Switzerland), India, Japan, Singapore, South Korea, United Arab Emirates, United Kingdom, and United States |
| SharePoint | Europe (EEA + Switzerland), Japan, and United States |
| Microsoft Teams | Europe (EEA + Switzerland), Japan, and United States |

Your plan, administrator settings, and provider permissions must also support the connection. If data residency is not enabled for your workspace, these sync-region restrictions do not apply.

This table describes administrator-managed sync setup availability, not separate live app connections or inference residency. For data residency details and instructions to check your workspace’s configured region, see: [Data residency and inference residency for ChatGPT](https://help.openai.com/articles/9903489).

# Set up an administrator-managed source

A workspace owner or authorized administrator must complete provider setup. The exact steps depend on the app, your administrator interface, and any permissions required by the provider.

* Go to **Admin > Plugins** and open the plugin that includes your app. If your workspace uses **Workspace settings > Apps**, select the app there.
* Review the app’s settings and the roles or groups allowed to use it.
* If **Indexed search** or another administrator-managed setup option appears, select **Set up** and complete the provider-specific connection flow.
* Approve any required Google Workspace or Microsoft administrator permissions and select the content or sources to include.
* Wait for initial indexing to finish, then verify that eligible workspace members can retrieve only content they are allowed to access.

For provider-specific setup and troubleshooting, see: [Google Drive app and setup in ChatGPT](https://help.openai.com/articles/10929079), [SharePoint app and setup in ChatGPT](https://help.openai.com/articles/12143177), and [Microsoft Teams app and setup in ChatGPT](https://help.openai.com/articles/12552368).

# Use indexed content

After setup, ChatGPT can reference relevant indexed information when it helps answer a question. The available content depends on the configured source, the administrator-selected scope, and the member’s permissions in the connected service.

You can ask questions such as “Summarize our team’s project plan” or “Find the latest document about our launch.” Available app-selection controls vary by your account and the ChatGPT interface you use.

The initial index may take time to become available. New content and permission changes can also take time to appear after the source refreshes.

If the source is unavailable, use the live provider connection when supported or ask your workspace administrator to review the administrator-managed setup.

# Access and permissions

Administrator-managed sync does not grant members access to content they cannot view in the underlying provider.

* Workspace administrators control which sources are connected and which roles or groups can use the app.
* Provider permissions determine the files, sites, channels, messages, or other supported content each member can access.
* The administrator-selected source scope can further limit what ChatGPT indexes.
* A separate provider account connection may be required for live app actions, even when administrator-managed indexed search is already available.

For app permissions and approval settings, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

# Data controls and privacy

Workspace administrators manage the supported sync connection and any available indexing or source-scope settings. Removing or changing an administrator-managed connection can affect content available to the workspace.

Data handling depends on the applicable workspace agreement, configured retention settings, provider, and account controls. Do not assume that disconnecting an individual live app account also removes a workspace-managed indexed source.

For provider access, account disconnection, and workspace privacy boundaries, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

# Troubleshoot administrator-managed sync

* Confirm that you are signed in to the intended managed workspace.
* Check whether the specific app and administrator-managed indexing option are available for your workspace and region.
* Ask a workspace owner or administrator to review role access, provider administrator approval, source scope, and current setup status.
* Confirm that affected members already have permission to access the source content in Google Drive, SharePoint, or Microsoft Teams.
* Allow time for initial indexing and later content or permission refreshes.
* For live app actions, verify the separately connected provider account and any required action approvals.

For additional steps, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

# FAQ

## What happened to individually authorized app sync?

Individually authorized app sync is no longer available. Existing personal sync connections cannot be restored or upgraded. Eligible workspaces can continue using supported administrator-managed sync when a workspace administrator configures it.

## Can I still connect an app without sync?

Yes, when the app is available for your account or workspace. A supported live app connection lets ChatGPT access the provider according to the account authorization, available actions, and administrator controls. It does not create an individually managed index.

## Which apps support administrator-managed sync?

Availability depends on the provider and workspace. Google Drive, SharePoint, and Microsoft Teams may offer administrator-managed setup where supported. Check the setup options shown for your workspace rather than assuming every app supports indexing.

## Does GitHub support administrator-managed sync?

Current GitHub access uses the supported non-synced integration. For setup and repository access, see: [Connecting GitHub to ChatGPT](https://help.openai.com/articles/11145903).

## Can a workspace member set up sync without an administrator?

No. Administrator-managed sync must be configured by a workspace owner or another administrator with the required workspace and provider permissions.

## Can I disconnect an administrator-managed source myself?

Members cannot remove a source managed by their workspace administrator. Ask your administrator to review the connection or your access. You can manage a separate individual live app account when the app supports that option.

## How do I know whether indexed content is current?

Initial indexing and later content or permission updates take time. If expected content is missing, ask your administrator to review the configured source scope, indexing status, and your access in the underlying provider.
