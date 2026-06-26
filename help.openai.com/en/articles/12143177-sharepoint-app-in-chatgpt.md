<!-- source: https://help.openai.com/en/articles/12143177-sharepoint-app-in-chatgpt -->

# SharePoint app in ChatGPT

Updated: 9 days ago

# Overview

Make ChatGPT more actionable and personalized with your own Sharepoint data source, now available on demand. The Sharepoint app enables ChatGPT to securely connect to SharePoint so you can search files, pull live data, and reference content right in the chat.  
  
To get started, find the SharePoint app in the ChatGPT app directory. Depending on your plan type, you can connect to SharePoint in two ways:

## User-authenticated SharePoint access

Each user signs in with their own SharePoint account using OAuth, allowing ChatGPT to use SharePoint content that user already has permission to access. This connection option is available to all plan types, and is best for individual access, flexible rollout and user-led exploration.

## SharePoint app with sync

Depending on the plan, you can enable sync for the SharePoint app. Enabling sync allows SharePoint content to be indexed in advance for faster, higher-quality retrieval in ChatGPT. This connection option is available to Pro, Business and Enterprise/Edu plans. Admins/owners can further configure the sync option by:

* deploying SharePoint sync for all users in your workspace (Enterprise/Edu only), or
* enabling sync, then allowing individual users to connect their own SharePoint account using OAuth.

In both types of connections, admins/owners can manage access from Workspace settings → Apps, including using [RBAC](/en/articles/11750701-rbac) to control user access (Enterprise/Edu only).

***Note****: As of April 30, 2026 we are migrating the ChatGPT SharePoint app* [*scope requests*](/en/articles/12143177-sharepoint-app-in-chatgpt?preview=#permission-requested-scope) *from* ***delegated scopes to*** *Microsoft* ***application scopes,*** *for the admin-managed "****Deploy to your team****" sync option. The migration helps ChatGPT sync selected SharePoint content and evaluate SharePoint permissions, including legacy SharePoint site group membership, without depending only on the files visible to the admin who completed setup. Additionally, admins and owners can configure Microsoft Purview sensitivity labels from app settings.*  
  
  
*These new scopes will need to be approved by a Microsoft Entra admin. Admins and owners can conveniently re-authenticate the SharePoint app by navigating to* ***Workspace Settings > Apps,*** *and locating the prompt "Reconnect SharePoint for better syncing" at the top of the view, or by searching for the SharePoint app and clicking the 'Re-auth required' button to obtain the new feature set. This prevents the need to disconnect and reconnect, which will cause re-syncing of the index.*

### Deploy to you team when you need centralized control

(Enterprise/Edu only) This is the best fit if your organization wants an admin to choose what SharePoint content is synced, apply workspace-level access controls, and roll out a predictable configuration across the workspace.

### Use user-authenticated setup for pilots or user-led adoption

This is the best fit when you want individual users to connect their own SharePoint account and explore the experience without a centrally managed sync scope.

### If both connection types are enabled, choose and communicate a primary model

Both can technically be enabled at the same time. If your organization requires centrally selected scope and a more controlled deployment pattern, use admin-managed sync as the primary rollout model and communicate that clearly to users.

### Pilot before broad rollout if your environment depends heavily on group-based access resolution or complex SharePoint structures

If your deployment relies on directory-based permission resolution, Teams-connected SharePoint sites, or complex inherited access patterns, validate behavior with a pilot before broad rollout.

[Learn more about connecting a new app](/en/articles/11487775-connectors-in-chatgpt#h_615184a466).

# Example use cases and prompts

## Communication and writing

Draft updates, synthesize documents, or follow company guidelines using connected tools.

* “Draft an executive update using the latest info on project [x].”
* “Consolidate all the documents on [x] into a guide for new hires.”

## Organization and productivity

Organize your knowledge, surface important documents, and boost your personal productivity.

* “Find the latest pitch decks on [x].”
* “Find me the top three most relevant documents on [topic].”

## Analysis and reporting

Analyze internal and external data for competitive and market research.

* “Create a side-by-side comparison of my product offering with competitor [x] using our internal docs and public web sources.”
* “Identify opportunities in [x] industry based on our internal docs and public web information."

[Learn more about app use cases and prompts.](/en/articles/12084614-connector-use-cases-and-prompts)

# Capabilities and permissions

## What it can access

* **Supported file types:** .txt, .pdf, .docx, .pptx, .xlsx, .csv

## What it can do

* Read content and metadata for files and folders you can access in SharePoint
* Respect SharePoint permissions, including items shared with you

## Permission requested (scope)

***Note:*** *The app requires the following scopes to be reviewed and approved by your Microsoft Entra admin. If the scopes are not approved by your Entra admin, you may see an error when trying to connect the app within ChatGPT.*   
  
*Approval of scopes does not immediately make all actions available to users. Admins and owners must still review app actions in* ***Workspace settings > Apps*** *for the app. In* ***Action control****, admins can choose how the app's current actions are handled by allowing all actions, allowing only read actions, or selecting a custom set of actions.*  
  
*If admins select* ***Custom****, they can also choose how actions added later are handled by selecting* ***Enable all new actions****,* ***Only enable new read actions****, or* ***Disable new actions****. If admins select* ***Disable new actions****, they must review and enable new actions before users can use them. After admins allow additional actions, users may need to reconnect the app to use them.*

All setup types:

|  |  |
| --- | --- |
| **Scope** | **Explanation** |
| `offline_access` | Allows the app to maintain access after setup so synced content can stay up to date without requiring the user to reconnect each time. |
| `User.Read` | Allows the app to read the signed-in user's basic profile information during setup and authentication. |
| `Files.Read.All` | Allows the app to read files the user has access to. This is also used to populate files in the file picker and support core sync functionality. |
| `Files.ReadWrite.All` | Allows the app to access and update files the user has access to when write access is required for the connected file experience. |
| `Sites.Read.All` | Allows the app to read items in SharePoint sites the user has access to for standard setup flows. |

The following scopes are additionally required for admin-managed setups:

|  |  |
| --- | --- |
| **Scope** | **Explanation** |
| `Group.Read.All` | Allows the app to read Microsoft 365 groups used in file permissions. Without this scope, group-based access controls cannot be processed correctly. |
| `GroupMember.Read.All` | Allows the app to read membership in Microsoft 365 groups used for permissions. Without this scope, user access inherited through groups cannot be processed correctly. |
| `Sites.FullControl.All` | Allows the app to read items across site collections the user can access. This is required for admin-managed sync so file picker selection and sync-all-content flows work correctly. [Read FAQ for details on why this scope is required.](/en/articles/12143177-sharepoint-app-in-chatgpt?preview=#why-is-the-app-requesting-sharepoint-scopes) |
| `Sites.Selected` | Allows the app to read items from site collections explicitly configured by users. This scope is included for compatibility, but `Sites.FullControl.All` is the primary scope used for admin-managed sync. |
| `User.Read.All` | Allows the app to read user information needed to attribute access controls correctly. Without this scope, user-based permissions cannot be processed correctly. |
| `SensitivityLabels.Read.All` | Allows the app to read sensitivity labels applied to files so labels can be respected during sync. |

## Known limitations

* Maximum supported file size is **100 MB per file**
* Content directly from **SharePoint site pages** is not supported. To be indexed and available in ChatGPT, content must be in a supported file type.
* Initial sync can take time. In smaller environments, content may begin appearing within hours; in larger environments, full sync can take longer.
* During partial sync, some recent content may already be available while older or less frequently accessed content is still syncing. Some results may be missing until full sync completes.
* Apps with sync are designed to work best for Q&A and search-style queries. Performance may be more limited for very large-scale aggregation tasks or especially complex analysis.
* For admin-managed sync, OneDrive access is supported only when the workspace admin selects **sync all** and has the required SharePoint admin permissions. If the admin manually selects sites and folders during setup, OneDrive is not supported in that selection flow.
* Only a single admin-managed SharePoint sync instance is supported per workspace.
* Existing admin-managed SharePoint connections may need reauthentication before sensitivity label filtering and improved legacy SharePoint group permission support are available.
* Files protected by Microsoft Purview sensitivity labels that enforce encryption or access control are not synced by ChatGPT.

[Learn more about Admin Controls, Security, and Compliance in](/en/articles/11509118-admin-controls-security-and-compliance-in-connectors-enterprise-edu-and-business) apps.

# User-authenticated SharePoint access setup

You can connect to the SharePoint app by locating it in the ChatGPT app directory. Follow the steps listed in this article on [connecting new apps](/en/articles/11487775-apps-in-chatgpt#how-to-connect-to-a-new-app).

# SharePoint app with sync setup

Depending on your plan type, there are two ways to deploy the SharePoint app with sync for your team:

## Deploy to your team

Enterprise/Edu plans only: Admins can connect once for all users in their workspace - individuals don’t need to configure anything themselves. During setup, admins can select the scope of sites or folders to sync with a scope picker, ensuring only the right content is made available.  
  
Once enabled, ChatGPT will automatically match users whose SharePoint and ChatGPT accounts share the same email domains, applying any pre-existing SharePoint role-based access control (RBAC) settings to ensure security. Each member will only see and access the SharePoint files in ChatGPT that they already have permission to access.

## Self-service

Each user links their own SharePoint account via OAuth and can enable or disable sync during app setup, or in **Settings → Apps**. Business and Enterprise/Edu admins can control overall app and sync availability from the admin settings page, including RBAC (Enterprise/Edu only).

Pro users that want to enable sync for their accounts must follow the **Self-service** setup option. You can enable setup when connecting the app, or from **Settings → Apps** post connection.

# Enterprise/Edu workspace setup

## Option 1: Deploy to your team

ChatGPT Enterprise workspace Admins must enable access to the SharePoint app in their workspace’s [Admin apps settings](https://chatgpt.com/admin/ca), or by clicking on their profile icon and selecting Workspace settings.

* Click **Enable Sync**. You will see a choice between **Deploy to your team** and **Self-service set up**.
* Use **Configure access** [for RBAC.](/en/articles/11750701-rbac)
* Optionally, Select **Manage domains** to limit connected SharePoint accounts to an approved set of domains.
* Click **Enable Sync**.
* Select **Deploy to your team**, and complete any OAuth steps needed.

You can now pick the sites/folder scope for your team. Click through to complete the setup.

Once setup is complete, ChatGPT starts syncing with SharePoint. The initial sync can take up to a few hours or longer, depending on the volume of data to sync.

Once finished, users can ask ChatGPT questions about their OneDrive and SharePoint files.

## Option 2: User-authenticated setup

Enterprise Admins must first enable the SharePoint app from [Admin app settings](https://chatgpt.com/admin/ca) (see Option 1 above), and then Enable sync.

Users can then enable SharePoint sync from their accounts. To enable, users must:

1. Go to **Settings > Apps**.
2. Find SharePoint in your list of connected apps. If you haven’t connected yet, click on the SharePoint tile, and click **Connect**.
3. Select Sync as the connection type and click **Continue**.
4. Complete OAuth setup.

If you have formerly connected to SharePoint, click Enable Sync for the SharePoint entry.

The initial sync can take up to a few hours, depending on the volume of data to sync. Once it’s finished, users can ask ChatGPT questions about their OneDrive and SharePoint files.

# Business workspace setup

ChatGPT Business workspace Admins must enable access to the Sharepoint app in their workspace’s [Admin apps settings](https://chatgpt.com/admin/ca). Once this is enabled, each user can connect their individual account by signing in to SharePoint through an OAuth flow.

## Step 1: Enable Sharepoint app access in Admin settings

ChatGPT admins can access [Admin apps settings](https://chatgpt.com/admin/ca) by clicking their profile icon and selecting Workspace settings.  
  
Under **Apps -> Enabled**, ensure that Sharepoint is enabled. This toggle will grant individual users access to both the Sharepoint app and the Sharepoint app with sync. You can configure the app by clicking on the ellipsis (...) menu. Select **Manage domains** to limit connected SharePoint accounts to an approved set of domains.  
  
Once this is done, members of your workspace will be able to enable sync on their individual accounts.

## Step 2: Workspace user connects to SharePoint (OAuth)

If you have already connected Sharepoint to your individual account, please skip to [Step 3](#h_ae1f228d5a).

On ChatGPT, click on **+** and **More**. Then, choose SharePoint and follow the sign-in (OAuth) steps.  
  
Alternatively, you can go to Settings and select Apps. Then, select Sync and choose SharePoint, and complete the sign-in flow.  
  
After completing the Sharepoint sign-in flow, the sync will be enabled automatically.

## Step 3: User enables sync for Sharepoint

To enable SharePoint sync:

1. Go to **Settings** > **Apps**.
2. Find **SharePoint** in your list of connected apps.
3. Click **Enable sync**.

The initial sync can take anywhere from a few minutes to a few hours. Once it’s finished, users can ask ChatGPT questions about their OneDrive and SharePoint files.

# ChatGPT Pro setup

ChatGPT Pro users can enable access to the Sharepoint app with sync from **Settings > Apps**.

To enable SharePoint sync:

1. Go to **Settings** > **Apps**
2. If you haven’t previously connected to SharePoint, find the SharePoint tile, and click **Connect**.
3. If you have previously connected to SharePoint, click **Enable sync**.

The initial sync can take anywhere from a few minutes to a few hours. Once it’s finished, users can ask ChatGPT questions about their OneDrive and SharePoint files.

# FAQ - General

## Do you sync both OneDrive and SharePoint?

Yes. The sync app with sync works with both personal files in **OneDrive** and shared drives in **SharePoint**.

## What happens if I don’t enable sync?

If you don’t enable sync (either as a workspace admin, or in user settings), the app will still work for file search. You can still query your SharePoint sites, but data won’t be continually indexed for up-to-date information. Read more about

## Can admins control who has access to the app with sync?

Yes, [you can further configure access to users settings with RBAC.](/en/articles/11750701-rbac)

## When will new or updated files be reflected?

New and updated files are typically reflected within a few minutes to about an hour.

## Are file permissions respected by ChatGPT?

File permissions are always respected. Users only have access to their own files and to files that others have shared with them.

## Can an individual user connect a SharePoint account from any domain in user-authenticated mode?

Yes. For the user-authenticated app with sync, there are no domain restrictions; users can connect to any SharePoint account they have access to.

## I formerly had the user authenticated app enabled for my Enterprise workspace. How do I switch to the admin-managed app?

Admins can transition smoothly by going to **Admin settings → Apps → SharePoint → Deploy to team**. This will add the admin-managed sync without immediately disabling the user-authenticated app, avoiding downtime.

# FAQ - Admin-managed app with sync

## How is this different from the SharePoint user-authenticated app with sync?

The user authenticated app with sync requires each user to individually authenticate (OAuth) and sync their own files. Admins could enable SharePoint for the org, but they couldn’t deploy it directly to everyone.  
  
The admin-managed app with sync lets an administrator authenticate and deploy across the organization, so users don’t need to complete individual setup. After admin setup and activation are complete, users can start using it without personal OAuth configuration.

## What if we already set up the user-authenticated app with sync?

Admins can transition smoothly by going to **Admin settings → Apps → SharePoint → Deploy to team**. This will add the admin-managed sync without immediately disabling the user-authenticated app with sync, avoiding downtime.

## After I turn on the admin-managed app with sync, do users need to manually enable the app in their chat?

No. After setting up admin sync, users don’t need to authenticate individually. Users can simply ask questions such as “Show me X in SharePoint.”

## Does the admin-managed app with sync also support access to OneDrive files?

Yes, but only if the ChatGPT workspace admin selects **sync all** in the setup flow and is a [SharePoint admin](https://learn.microsoft.com/en-us/sharepoint/sharepoint-admin-role) with full permissions to manage settings, content, and permissions across all sites and sub-sites within a SharePoint site collection.  
  
If the workspace admin opts to manually select sites and folders in the sync setup process, OneDrive is not supported (the admin folder picker does not support selecting OneDrive in the selection flow.)  
  
As a reminder, users will only have access to the content they have permission to view in, SharePoint.

## How does ChatGPT know which users to enable?

Access is based on strict email domain matching between SharePoint and ChatGPT. A user’s SharePoint account must match their ChatGPT account email.

## What about role-based access control (RBAC)?

Admins can control which groups have access to SharePoint through RBAC. The app respects existing SharePoint RBAC configurations. If an admin has already set RBAC, those settings apply. If not, admins can configure RBAC at any time

## Will users still only see files they have permission for?

Yes. SharePoint’s existing file permissions are fully honored. Users only access the files they already have permission to view in SharePoint.

## What can admins control when setting up the app?

Admins must be both a SharePoint admin and a ChatGPT admin. They can choose to sync all files or specific sites and folders. Files managed this way will appear in ChatGPT as “admin-managed” under the connection type.

## Can admins change what’s synced later?

Yes. Admins can update the sync scope from the SharePoint app settings. Select **Limit content** to change which content is synced or to configure sensitivity label filtering, when available.

## Can we use both the user-authenticated and admin-managed apps?

Yes. Both apps can technically be enabled at the same time.

## When will new or updated files be reflected?

New and updated files are typically reflected within **a few minutes to about an hour**.

## Can I choose the scope of sync, such as specific folders or files?

Yes, you can select the sync scope during the setup, or edit the sync scope.

## Can we enable multiple admin-managed SharePoint app with sync in the same workspace (e.g., one per tenant/brand)?

Only a single admin-managed SharePoint instance is supported per workspace.

## Why does the Microsoft consent screen show both delegated and application permissions?

During the migration to application permissions for admin-managed SharePoint sync, Microsoft may show both delegated permissions and application permissions. This temporary overlap helps preserve existing SharePoint connector behavior while enabling improved coverage and sensitivity label filtering. In future, we may remove delegated scope requests entirely.

## Why is the app requesting Sites.FullControl.All?

The app requests [Sites.FullControl.All](https://learn.microsoft.com/en-us/graph/permissions-reference#sitesfullcontrolall) so it can fetch document permissions fully and accurately. Microsoft’s guidance for [scanning permission hierarchies with Microsoft Graph delta queries](https://learn.microsoft.com/en-us/graph/api/driveitem-delta?view=graph-rest-1.0&tabs=http#scanning-permissions-hierarchies) states that apps need Sites.FullControl.All to process permissions correctly. In our testing, Sites.Read.All could delay access-control updates, which meant document permissions were not always reflected right away.

## Why is the app requesting Sharepoint scopes?

This change allows the app to fetch access control and group information for a (legacy) Sharepoint Site.

## Why is the app requesting scope Sites.Selected?

Scope Sites.Selected is a strict subset of Sites.FullControl.All. The app needs at least one of the two to operate correctly. Sites.Selected allows organizations and IT admins to further restrict access for the App. We recommend leaving the Scope present.

Note: if the admin is considering revoking Sites.FullControl.All, please ensure that selected sites are made accessible by [following this microsoft guide](https://learn.microsoft.com/en-us/graph/api/site-post-permissions?view=graph-rest-1.0&tabs=http) to ensure the connector works correctly.

OpenAI enabled this scope for early pilot and recommends reaching out before this scope is relied on.

## How are Microsoft Purview sensitivity labels handled?

Admin-managed SharePoint sync can use Microsoft Purview sensitivity label metadata to exclude selected labeled files from sync. This requires the SensitivityLabels.Read.All permission.  
  
Microsoft Sensitivity Labels are handled based on whether the label is configured to encrypt content. A label can be classification-only: Microsoft describes sensitivity labels as [clear-text metadata](https://learn.microsoft.com/en-us/azure/information-protection/aip-classification-and-protection#what-a-sensitivity-label-is) used to classify content, and these labels do not by themselves encrypt the file or change who can open it.   
  
Files with classification-only sensitivity labels can be synced if they are otherwise in scope and the user has SharePoint permission to access them. Admins can exclude files with selected classification-only labels from sync by using the sensitivity label filter.  
  
If a sensitivity label is [configured with access control](https://learn.microsoft.com/en-us/purview/encryption-sensitivity-labels#how-to-configure-a-label-for-encryption), Microsoft applies encryption to the content. Microsoft states that encrypted content can be [decrypted only by users authorized by the label's encryption settings](https://learn.microsoft.com/en-us/purview/encryption-sensitivity-labels) and remains encrypted wherever it resides. These protected files are not synced by ChatGPT and are automatically excluded; admins do not need to select these labels in the sensitivity label filter.

## I previously set up the admin-managed SharePoint app. How do I get the new features?

If you already set up admin-managed SharePoint sync, do not disconnect and reconnect the app. Disconnecting and reconnecting can cause SharePoint content to be resynced and reindexed, which can delay availability in ChatGPT.  
  
Instead, go to the SharePoint app settings (from Workspace Settings > Apps) and use the reauthentication prompt. The reauthentication preserves existing sync and any previous Content Selection. To update selection, select **Limit content** to make changes such as adding newly discovered Sites, or excluding content labeled with un-protected sensitivity labels (Note: protected sensitivity labels are always excluded).

## What happens if I do not reauthenticate with the additional Microsoft scopes?

Your existing SharePoint app connection remains active, and pre-existing functionality continues unchanged. However, you will not be able to use features that require the additional Microsoft scopes, including sensitivity label filtering and improved support for legacy SharePoint group permissions.
