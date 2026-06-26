<!-- source: https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business -->

# Admin Controls, Security, and Compliance in apps (Enterprise, Edu, and Business)

Learn how your organization can manage app usage with admin settings, help ensure secure data flows, and meet compliance needs.

Updated: 2 days ago

***Note:*** *As of August 29th, 2025, we've renamed ChatGPT Team to ChatGPT Business. For more information and questions related to the name change, please refer to our article:* [*ChatGPT Business Rename FAQ*](/en/articles/12111915)

*As of December 17, 2025, we are renaming connectors to apps to present a more unified experience. The term now includes both apps that feature interactive UI and connectors that help you search and reference your information in ChatGPT. We are not removing any existing functionality; previously enabled connectors and company knowledge will continue to work as before.*

# Admin controls

## Default behavior by plan

### ChatGPT Enterprise & Edu

All apps are *disabled* by default. Workspace owners can control which apps are enabled in **Workspace settings → Apps**, as well as assign app specific roles through RBAC (see below).

### ChatGPT Business

In ChatGPT Business, workspace admins can control which apps are enabled for the workspace and can manage role-scoped app permissions.

## RBAC (Role-based access control)

Enterprise and Edu workspaces can assign apps to one or more custom roles. By default, users can access apps that are enabled and available to their role, but admins can control which roles have access. If a user sees an app marked **Disabled by admin**, the app is not available to them because of workspace or role settings; a workspace admin must enable access before the user can connect it.

## Manage app access

App access controls who can use a connected app in the workspace. App permissions control when ChatGPT asks before using an app.  
  
To manage who can use a specific app, go to **Workspace settings > Apps**, open the app's menu, and select **User access**. From there, choose which roles can access the app, then save your changes. If you cancel or close without saving, the app's current access settings remain unchanged.  
  
To manage which apps a role can use:

1. Go to **Workspace settings > Permissions & roles**.
2. Select **Custom roles**.
3. Select the role you want to edit.
4. Scroll to the **Connected data** section.
5. Turn on **Allow members to use apps** to allow app use for that role.
6. Use **Select** to choose specific apps for that role.

## Adding new apps

When enabling a new app at the workspace level, admins are prompted to assign which roles can access it. If the app supports action controls, admins can also review the app's actions before making the app available.  
  
App templates follow the same admin governance model after publishing. Workspace admins and owners review the template-generated draft app, publish it when ready, then manage access, role-scoped permissions, action controls, and app permissions from **Workspace settings > Apps**.  
  
Where available, app permissions replace the previous action confirmation control. If the workspace-wide **App permissions** menu does not show **Never ask**, choose another workspace default or set **Never ask** for a specific app from that app's **App permissions** settings. For setup details, see [ChatGPT app templates](https://help.openai.com/articles/20001247).

## App action controls

RBAC controls who can use an app. For apps that support **Action control**, Action control determines what the app can do. **App permissions** determine when ChatGPT asks members before using an app.

These app permissions apply to ChatGPT conversations. Workspace Agents use per-agent controls set by the agent's builder to determine which app actions are available and when end users are asked to approve them. For agent behavior, see: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).

In **Action control**, admins can choose how the app's current actions are handled by allowing all actions, allowing only read actions, or selecting a custom set of actions. If admins select **Custom**, they can also choose how actions added later are handled by selecting **Enable all new actions**, **Only enable new read actions**, or **Disable new actions**.

Some apps do not support Action control. For those apps, admins can manage app access, but they cannot choose individual actions or how newly added actions are handled.

For apps that support Action control, provider scope approval does not automatically make new actions available in ChatGPT.

To change the workspace default app permission:

1. Open **Workspace settings**.
2. Go to **Permissions & roles > Connected data**.
3. Find **App permissions** and select the workspace default.

To set a different permission for an app:

1. Open the workspace's **Apps** admin page.
2. Open the menu for a published app and select **App permissions**.
3. Choose **Use workspace default** or select a different permission.
4. Select **Save**.

The options may include **Always ask**, **Any changes**, **Important actions**, and **Never ask**, depending on the workspace, app, and rollout status. **Important actions** asks before app actions that could have a meaningful effect outside ChatGPT, expose sensitive information, or be difficult to undo. Some especially risky actions may be blocked instead of being presented for approval.

## Custom apps using MCP

Admins can also allow roles to access developer mode, which allows the creation and testing of custom apps using MCP. Role access to developer mode does not automatically make new MCP actions available. After a custom MCP app is published, the app must be connected in the workspace before its actions can be refreshed. An admin who owns or manages the app can review its actions in **Action control**, and select **Refresh** to review added or changed actions from the MCP server.

## Granular Google Drive (synced) controls

***Note:*** *Google Docs, Sheets, and Slides actions are now available as* ***Google Drive actions****. This unifies all actions into the Google drive app - simplifying Google app usage. Standalone Google Docs, Sheets, and Slides apps rare no longer available on the ChatGPT app directory, and users should connect to the Google Drive app for Docs, Sheets and Slides access.*   
  
*For ChatGPT Enterprise/Edu, these new unified Google Drive actions are* ***off by default*** *until a workspace admin enables them. For ChatGPT Business,* ***they are on by default****. After enablement, Google Workspace admins may need to re-authorize updated Google Drive scopes before users can use these actions, or new users can connect. If you receive complaints from your users that they are unable to connect to Google Drive, please check your Google workspace scope authorizations for Google Drive, Docs, Sheets and Slides, and confirm that all actions in the app have scopes that have been authorized, or turn off actions that you do not want to authorize.*   
  
*Note that the sync feature remains unaffected with this change.*

### File restriction and setup

Enterprise, Edu, and Business workspaces can:

* Limit the app with sync to specific Shared Drives or folders.
* Exclude specific file types from indexing.
* Choose between a **Quick setup** (each user authenticates their account) or **Admin-controlled access** (centralized setup for granular controls)

For additional information regarding enabling the Google Drive app with sync, please refer to our help article: [Google Drive app with sync - self-service setup](/en/articles/10948259)

### RBAC for Google Drive (synced) for Enterprise and Edu

Once you enable the Google Drive app with sync, all users who had access to the non-synced version will also gain access to the synced version. It is not currently possible to set different permissions between synced and non-synced versions.

If you previously set up an allow-list for the Google Drive app with sync before [RBAC for apps was introduced](/en/articles/10128477-chatgpt-enterprise-edu-release-notes#h_343d7ce8ac), your allow-list has been mapped to new RBAC groups and roles called **Google Drive Connector Users** and **Google Drive Connector Role**.

* If your workspace had the Google Drive app enabled at the workspace level, only users on the app with sync allow-list now retain access.
* Users who were not on the allow-list **no longer have access** to the non-synced Google Drive app and **must be re-added.**
* Users with access to the Google Drive app with sync now also have access to the standard Google Drive app.

All other workspace roles and permissions remain unchanged.

## Microsoft Outlook (Calendar & Email), Teams, and Sharepoint permissions required

To enable integration between ChatGPT and Microsoft Outlook, Teams, and Sharepoint, permissions must be granted within Microsoft Entra ID (formerly Azure AD) for each service. Review our Help Center pages for permissions required:

* [Outlook Email](/en/articles/12512241-outlook-email-and-calendar-connectors-for-chatgpt#h_b51322c915)
* [Outlook Calendar](/en/articles/12512241)
* [Microsoft Teams](/en/articles/12552368)
* [Microsoft SharePoint](/en/articles/12143177)
* [Microsoft Azure Boards](/en/articles/12628387)

Each app page describes scope required by that app. For a full list of scopes per app, refer to the ChatGPT [app directory](https://chatgpt.com/apps).

## Custom apps

In Business, Enterprise, and Edu workspaces, only workspace owners, and users with the [respective setting enabled](#h_b441561f7c) (for Enterprise/Edu) can enable developer mode to publish and test custom apps. Users with the **member** role do **not** have the ability to add custom apps themselves.  
  
As with other apps, end users must authenticate with each app themselves before first use.  
  
For a general overview of developer mode and custom apps and MCP connectors in ChatGPT, please refer to our article: [Developer mode and custom apps in ChatGPT](https://help.openai.com/articles/12584461)  
  
For a technical walkthrough of creating a custom MCP connector, please refer to our documentation: [Creating custom MCP](https://platform.openai.com/docs/mcp) apps

***Note:*** *Please note that custom apps are not verified by OpenAI and are intended for developer use only. You should only add custom apps to your workspace if you know and trust the underlying application.* [*Learn more*](https://platform.openai.com/docs/mcp#risks-and-safety)*.*

*Apps may allow end users to share data, which could include protected health information (PHI), with third parties. You should ensure that your use of apps complies with your obligations under HIPAA.*

---

# Security & compliance

## Security

We protect your data with **industry-standard encryption** in transit and at rest. OAuth tokens are stored using strong, audited key-management practices. After an app is enabled, each user authorizes their own account, and ChatGPT only accesses content within that user’s existing permissions, such as read-only scopes.  
  
OpenAI applies ongoing testing, monitoring, and layered mitigation techniques to reduce prompt-injection risk. For added protection, conversations that use apps have locked-down network access to keep data between OpenAI and the specific tools you connect. Strict access controls ensure ChatGPT only sees what each user is permitted to access, and all data remains encrypted in transit and at rest.

## Does OpenAI use information from apps to train its models?

For ChatGPT Business, Enterprise, and Edu customers, we do not use information accessed from apps to train our models. Please see our [Enterprise Privacy page](https://openai.com/enterprise-privacy/) for information on how we use business data.  
  
Chat and deep research data are processed transiently and **not indexed**. App with sync data *is* indexed to speed up answers, while respecting your training settings.

## Data storage & residency

All apps with sync are supported for workspaces with data residency in the United States, Europe (EEA + Switzerland), and Japan. Google Drive and GitHub apps with sync are also supported in all currently supported [data residency regions](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).  
  
For apps with sync that are not supported for data residency in your region, the synced search index is stored in OpenAI’s U.S. Azure data centers.  
  
  
**Non-synced apps:** Apps are compatible with data residency, but it's important to note that connected applications are third-party services, and data sent to a connected application is subject to that application's own data residency policies.  
  
In other words, if you're an organization with Data Residency in Europe, OpenAI will limit storage of Customer Content to take place in Europe up until the point that queries and prompts are sent to a connected application. Please make sure that your connected applications also adhere to any data residency requirements you may have.

## Compliance

User conversations, including conversations using any app, are already available in the Compliance API.  
  
Additionally, all app calls are logged as a part of the [OpenAI Compliance Logs platform](https://chatgpt.com/admin/api-reference#tag/Logs:-Apps).  
  
Read more: [Compliance API for Enterprise Customers.](/en/articles/9261474-compliance-api-for-enterprise-customers)

## Granular Google Drive (synced) security

In addition to OAuth authentication, owners for Business, Enterprise, and Edu workspaces are able to utilize domain-wide delegation (DWD).
