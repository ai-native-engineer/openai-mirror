<!-- source: https://help.openai.com/en/articles/12143177-sharepoint-app-and-setup-in-chatgpt -->

# SharePoint app and setup in ChatGPT

Connect SharePoint to ChatGPT, review Microsoft permissions, and configure administrator-managed SharePoint sync for an eligible workspace.

The SharePoint app lets ChatGPT search and reference SharePoint and supported OneDrive for work or school content that your Microsoft account can already access. Personal OneDrive accounts are not supported by the SharePoint app. Available actions depend on your organization’s settings.

Eligible Enterprise and Edu workspace administrators can configure administrator-managed SharePoint sync to index selected content for their workspace. Connecting your own Microsoft account provides live access, but it does not create a personal synced index.

For an overview of connected apps, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

## Availability

SharePoint availability depends on your ChatGPT plan, location, workspace settings, Microsoft account, and your organization's Microsoft Entra policies.

Administrator-managed SharePoint sync is available only in eligible Enterprise and Edu workspaces and supported regions. Individual and personal accounts cannot configure SharePoint sync.

For the workspace data residency regions that support administrator-managed SharePoint sync, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

# Connect SharePoint

1. Open **Plugins** or **Apps**, depending on the options available in your version of ChatGPT.
2. Find **SharePoint** and select the option to connect your account.
3. Sign in with the Microsoft work or school account that can access the SharePoint sites or supported OneDrive for work or school files you want to use.
4. Review the requested Microsoft permissions and complete the authorization flow.
5. Return to ChatGPT.

If your organization requires administrator consent, your Microsoft Entra administrator must approve the permissions before the connection can be used.

For general account-management instructions, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Use SharePoint in a conversation

After connecting SharePoint, ask ChatGPT to find, summarize, or compare files that your connected Microsoft account can access.

Examples include:

* “Find the latest project plan in SharePoint and summarize the open decisions.”
* “Compare the two proposal documents in our sales team's SharePoint site.”
* “Draft an executive update using the launch documents I can access.”
* “Create a folder for this project in the approved SharePoint library.”

Depending on the permissions approved by your organization and the actions enabled in ChatGPT, the live SharePoint app may also support actions such as:

* Creating folders.
* Uploading or updating files.
* Managing sharing links.
* Working with supported SharePoint lists and pages.

An approved Microsoft permission does not automatically enable every corresponding action. Your ChatGPT workspace administrator must separately enable the actions your organization wants to allow. ChatGPT may ask you to confirm actions that change SharePoint content.

# Understand SharePoint permissions

ChatGPT only retrieves content the relevant Microsoft account or authorized workspace member is already allowed to access. SharePoint, OneDrive, Microsoft 365 group membership, and workspace access settings continue to apply.

A ChatGPT workspace owner or administrator manages app availability and actions. A Microsoft Entra administrator grants the Microsoft permissions needed by those actions. These roles may be held by different people.

For more information about workspace controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

## Review permissions for live SharePoint access

Depending on the enabled actions, the SharePoint app may request permissions such as:

* User.Read: Read the signed-in user's basic profile.
* offline\_access: Maintain the authorized connection without requiring the user to sign in for every request.
* Files.Read.All: Read files the signed-in user can access.
* Files.ReadWrite.All: Update or manage files the signed-in user can access when write actions are enabled.
* Sites.Read.All: Read content from SharePoint sites the signed-in user can access.
* Sites.ReadWrite.All: Manage supported SharePoint lists, items, pages, metadata, or other resources when those actions are enabled.
* Sites.Selected: Support site-scoped access after a SharePoint administrator grants access to the selected sites.

The exact permissions requested depend on your organization's configuration and the available actions. A permission should be granted only when your organization intends to allow an action that requires it.

## Approve Microsoft permissions

These steps describe the **Plugins** administrator interface. If your workspace uses **Apps** administration, go to **Workspace settings > Apps**, select **SharePoint**, and then select **Microsoft permissions**. Continue with the permission review and Microsoft approval below.

1. Sign in to ChatGPT as a workspace owner or administrator.
2. Go to **Admin > Plugins**.
3. Select **Configure Microsoft permissions** to review the combined request for your workspace’s Microsoft apps.
4. Review the listed Microsoft permissions and the ChatGPT actions associated with each one.
5. Select only the permissions your organization intends to grant.

### Complete Microsoft administrator approval

1. Continue to Microsoft Entra and sign in with an administrator account that can grant organization-wide consent.
2. Confirm the organization and the verified ChatGPT/OpenAI application.
3. Review the full selected request and complete the Microsoft consent flow.
4. Return to ChatGPT and confirm that the permission review completed.

If Microsoft Entra does not open, allow pop-ups for ChatGPT and try again. The Microsoft consent screen approves or rejects the selected permission request as a whole; it does not provide separate checkboxes for each permission on that screen.

Approving Microsoft permissions does not connect a member's Microsoft account or automatically enable actions in ChatGPT. Workspace administrators must separately review **Actions**, **Role access**, and related workspace settings where available.

# Set up administrator-managed SharePoint sync

Administrator-managed SharePoint sync lets an eligible Enterprise or Edu workspace owner or administrator select SharePoint content to index for the workspace. Members do not create individual synced SharePoint connections.

The administrator-managed index uses organization-approved Microsoft application permissions to evaluate files, sites, Microsoft 365 groups, and access controls. Each member can retrieve only content they are already permitted to access.

## Prepare the workspace and Microsoft tenant

Before starting:

* Confirm that administrator-managed SharePoint sync is available for your workspace and region.
* Sign in as a ChatGPT workspace owner or administrator.
* Coordinate with a Microsoft Entra administrator and, when needed, a SharePoint administrator.
* Decide which SharePoint sites and folders should be indexed.
* Review your organization's Microsoft Purview sensitivity labels and source restrictions.
* Confirm that the Microsoft account used for setup has the permissions required to configure the selected SharePoint sources.

## Review additional administrator-managed permissions

Administrator-managed SharePoint sync can require additional Microsoft permissions:

* Group.Read.All: Read Microsoft 365 groups used in file permissions.
* GroupMember.Read.All: Read group memberships used to determine effective access.
* User.Read.All: Read user information needed to attribute and enforce access controls.
* Sites.FullControl.All: Read SharePoint permission hierarchies and support accurate permission evaluation and administrator-managed indexing.
* Sites.Selected: Support selected-site configuration where applicable.
* SensitivityLabels.Read.All: Read sensitivity-label information when label-aware configuration is used.

Sites.FullControl.All is a broad Microsoft permission, so your Microsoft Entra administrator should review it against your organization's security requirements. Administrator-managed SharePoint sync uses this permission to process SharePoint access controls accurately; granting it does not mean workspace members can view files outside their existing SharePoint permissions.

Sites.Selected may appear for compatibility or selected-site workflows, but it does not replace the other permissions required for administrator-managed sync.

## Configure the administrator-managed connection

1. Go to **Admin > Plugins** and open the plugin that includes **SharePoint**.
2. If your workspace uses **Workspace settings > Apps**, select **SharePoint** there.
3. Open the **SharePoint** settings and confirm that the app is enabled for the workspace.
4. Review **Role access** if your workspace supports role-based access controls.
5. If you see **Indexed search**, select **Set up**.

### Approve the connection and choose content

1. Sign in with the appropriate Microsoft administrator account when prompted.
2. Review and approve the Microsoft permissions requested for administrator-managed access.
3. Select the SharePoint sites or folders your organization wants to include, or select all supported content if that matches your approved rollout.
4. Apply Microsoft Purview sensitivity-label filtering when available and required by your organization's policy.
5. Complete setup and allow time for the initial index to be created.

If an existing SharePoint connection requires updated Microsoft permissions, use the reauthorization prompt in the app settings when available. Disconnecting and recreating an administrator-managed connection can require the index to be rebuilt.

## Choose SharePoint and OneDrive content

The administrator's selected sites and folders determine the indexing scope. Existing SharePoint and Microsoft 365 permissions determine which indexed results each workspace member can retrieve.

Administrator-managed SharePoint sync can include supported OneDrive for work or school content when the administrator selects all supported content and the required SharePoint permissions are granted. Personal OneDrive is not supported. OneDrive is not included in site-and-folder selection flows that do not support selecting OneDrive sources.

Only one administrator-managed SharePoint sync connection is supported per workspace.

# Supported content and limitations

SharePoint supports common file types such as .txt, .pdf, .docx, .pptx, .xlsx, and .csv.

Additional limitations include:

* The maximum supported file size is 100 MB per file.
* Administrator-managed indexing is based on supported file content. SharePoint site pages are not indexed by administrator-managed sync. The live app may create or manage supported site pages when actions are enabled.
* Initial indexing can take hours or longer, depending on the size and complexity of the selected SharePoint environment.
* Some results may be missing while indexing is still in progress.
* Updates to files, group memberships, or permissions may take time to appear after a change.
* Files protected by Microsoft Purview labels that enforce encryption or access restrictions are not indexed.
* Site restrictions, sensitivity-label filters, and other administrator-managed indexing controls apply to the indexed connection. They do not automatically restrict a separately enabled live SharePoint connection.

When live SharePoint access and administrator-managed indexing are both enabled, review each connection separately. A live action can access other content already available to the signed-in work or school account.

# Troubleshoot SharePoint

For general connection issues, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

## SharePoint does not appear

Confirm that SharePoint is available for your account and that your workspace administrator has enabled the app. In a managed workspace, check whether **Role access** or an approved-domain policy limits who can use it.

## Microsoft administrator approval is required

Ask a Microsoft Entra administrator to review the permission request. A ChatGPT workspace administrator can see which SharePoint actions depend on each Microsoft permission and disable actions your organization does not want to approve.

## An action still does not work after approval

Confirm that:

* The action is enabled in the SharePoint app's **Actions** settings.
* The corresponding permission grant still exists in Microsoft Entra.
* The member connected the intended Microsoft account.
* The member reconnected their Microsoft account if new permissions were introduced.
* The Microsoft account has access to the relevant site, file, or folder.

## A SharePoint file is missing

Check that:

* The file is a supported type and does not exceed the size limit.
* If you are using indexed results, the file is within the administrator-managed indexing scope.
* The member can open the file in SharePoint.
* Any recent permission changes have had time to refresh.

## Administrator-managed sync is unavailable

Verify that your workspace is eligible, that SharePoint sync is supported in your configured region, and that an authorized Microsoft administrator has approved the required application permissions. Personal and individual ChatGPT accounts cannot enable SharePoint sync.

# FAQ

## Can I connect SharePoint without enabling sync?

Yes. When the SharePoint app is available to your account, you can connect your Microsoft account for live access to content you are allowed to use. Administrator-managed sync is a separate workspace feature.

## Can I enable SharePoint sync for my personal ChatGPT account?

No. Individual SharePoint sync is no longer available. Only eligible workspace administrators can configure administrator-managed SharePoint sync.

## Can members see files they cannot open in SharePoint?

No. SharePoint and Microsoft 365 permissions continue to determine what each member can retrieve.

## Does SharePoint sync include OneDrive?

It can include supported OneDrive for work or school content when the administrator selects all supported content and the required SharePoint permissions are granted. Personal OneDrive is not supported, and site-and-folder selection flows do not include OneDrive unless that option is explicitly available.

## Why does administrator-managed sync request Sites.FullControl.All?

Microsoft requires access to SharePoint permission hierarchies so the connection can evaluate effective file permissions accurately. Your Microsoft Entra administrator should review this broad permission before approving it. Workspace members still cannot retrieve files they are not authorized to access.

## Can live SharePoint actions and administrator-managed sync be enabled together?

Yes. They use different authorization paths and controls. Administrator-managed site restrictions and sensitivity-label filters do not automatically limit the separate live SharePoint connection.
