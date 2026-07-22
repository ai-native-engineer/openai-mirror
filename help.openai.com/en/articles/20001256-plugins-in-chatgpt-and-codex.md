<!-- source: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex -->

# Plugins in ChatGPT and Codex

Learn how plugins work in ChatGPT and Codex, how workspace admins manage installation by role, and how app permissions apply.

***As of July 9, 2026, we’ve migrated the app directory to the Plugin directory.*** ***Plugins are the primary way to discover workflow capabilities across ChatGPT and Codex. A plugin can include skills, apps, and app templates - apps remain the integrations that connect ChatGPT or Codex to external data and actions, while plugins make it easier to enable workflows in ChatGPT. Existing app connections remain unaffected, and users can add new plugins from the plugin directory, connecting and authenticating the underlying app as before. Workspace admins manage plugin installation in Workspace settings > Plugins, and can manage each underlying app’s access and permissions from within the plugin configuration, or from Workspace settings > Apps.***

# Overview

Plugins help Codex and ChatGPT complete repeatable work by packaging the capabilities needed for a specific workflow. A plugin can include workflow guidance, such as skills, and can also depend on approved apps that connect to tools, data, or actions.  
  
This article is for workspace admins, owners, and users who need to understand how plugins work, how plugins relate to apps, and what needs to be enabled before a plugin can be used in ChatGPT.

# What is a plugin?

A plugin is a packaged capability for a workflow. Depending on the plugin, it may include:

* [**Skills**](https://help.openai.com/articles/20001066), which provide reusable instructions, prompts, and workflow patterns that help Codex complete a task.

* [**Apps**](https://help.openai.com/articles/11487775), which connect Codex or ChatGPT to systems, data, and actions approved for your workspace.

* [**App templates**](https://help.openai.com/articles/20001247), which help an admin create or configure the app the plugin needs.

Some plugins are broad, while others are built for a specific line of business, such as sales, data analytics, or internal operations. A line-of-business plugin may bring together several capabilities so users can complete a job without manually switching between separate tools.  
  
A single plugin may have multiple skills and apps, allowing users to accomplish a wide variety of tasks. A **Plugins** section in **Workspace settings** lets workspace admins manage plugin availability and choose which roles receive a plugin automatically. Existing app settings continue to control who can use an app, what actions it can take, and related settings. Any plugin that includes the app inherits those permissions.  
  
Since the plugin is a container for apps and skills, all existing app functionalities, such as apps with UI, apps with sync, search functionality, and other features continue to work. Connecting an app continues to involve user authentication and workspace admins continue to have all the app controls, including action controls to align with workspace needs.

# Plugin Directory

The plugin directory is the primary place for people to discover workflow capabilities across ChatGPT and Codex. A plugin listing can include one or more apps, skills, and app templates. The plugin directory replaces the app directory, with all existing apps packaged into plugins. New app submissions will also arrive in the app directory packaged in a plugin. The plugin directory is available both in ChatGPT web and ChatGPT desktop, and is available in ChatGPT Work and ChatGPT Codex.  
  
To get started, open the plugin directory and select a plugin to review its capabilities, including apps, required setup, and connection requirements.  
  
The plugin directory is visible across ChatGPT plans. Whether you can install or invoke a plugin depends on your plan, workspace settings, role, supported surface, region, and the capabilities of its included apps.  
  
Select a plugin listing to review each included app’s capabilities, connection requirements, terms, and privacy policy. If a plugin requires an app, that app must be enabled for your workspace and role before the app-backed capability can be used.  
  
  
**Note**: the **Connect** button for a given app may be greyed out based on geo restrictions, workspace settings, or your plan type. If the button or tooltip says **Disabled by admin**, ask your workspace admin to enable the app before trying again.

# How plugins use apps

Many plugins depend on apps to reach external systems. For example, a plugin may need access to a workspace-approved app that connects to a repository, data warehouse, CRM, document store, or messaging tool.  
  
A plugin listing may be visible even when an included capability cannot be used. Required apps must be enabled for the member’s role; installation and invocation may also depend on plan, workspace, role, and supported surface.  
  
Existing [app permissions](https://help.openai.com/articles/11487775) continue to apply to plugins. Depending on the app, workspace admins and owners may control:

* Which users, groups, or roles can access it (Enterprise and Edu only). For more information, see: [RBAC](https://help.openai.com/articles/11750701).

* Whether it can read data only or also take actions

* Whether users must confirm actions before they run

* Whether sync, domain restrictions, source boundaries, or other app-specific settings apply.

Any plugin that uses the app inherits these settings.  
  
Approving an app in ChatGPT does not override permissions in the source system. If a user cannot access a file, repository, record, workspace, or channel in the connected system, the plugin should not give them access to it through Codex.  
  
Note that not all plugins contain apps. Some plugins may only contain skills.

## Plugins that include app templates

Some plugins may include an [app template](https://help.openai.com/articles/20001247) or depend on an app created from a template. App templates are not the same as a ready-to-use app. A workspace admin or owner may need to enter organization-specific configuration, create a draft app, publish it, and assign access before members can use the plugin.  
  
If a plugin depends on an app template that has not been set up yet, members may need an admin to complete setup first. The plugin cannot use the app template by itself.  
  
For more about template setup, see [ChatGPT app templates](https://help.openai.com/articles/20001247).

# Connecting a plugin

1. Browse plugins from the [ChatGPT plugin directory](https://chatgpt.com/plugins), from **Settings** > **Plugins**, or from the **Plugins** entry in the sidebar in either ChatGPT web or the ChatGPT Desktop app.
2. Select the app you are interested in.
3. Select **Connect** if available.
4. Complete **OAuth** and **enable sync** if required.
5. After the plugin is connected, invoke it in chat by using @ mentions in your prompt or by selecting + and then More to select the app you want to add.

# Setting up a plugin for the workspace

The Plugins Directory is visible across ChatGPT plans. Whether someone can install or use a plugin still depends on their plan, workspace settings, role, supported surface, and the plugin’s included capabilities. Before asking members to use a plugin, review its requirements and configure any required apps.  
  
A plugin that requires a specific app is available only when that app is enabled for the member's role. Plugins that include only skills, or include optional apps, remain available by default.  
  
Admins and owners in Business and Enterprise/Edu workspaces can configure both Plugins and the underlying apps:

* **Workspace settings -> Plugins** allows you to configure whether a plugin is enabled or disabled, and whether it is available workspace wide or to specific roles, and provides a lead-in to configure the app that’s within the plugin.

* **Workspace settings -> Apps** allows you to configure apps, including actions, controls, sync, and availability.

Both settings panes are complementary. Use the Plugins configuration pane to manage a plugin in its entirety. Use the Apps configuration pane to manage apps specifically.  
  
Get started:

* Go to **Workspace settings > Plugins**, and select the plugin.

* Review the plugin's included skills, required apps, optional apps, and app templates.

* In the Installation **policy**, choose **Available** or **Installed** for each eligible role.

* If the plugin requires an app, open the required app from the plugin page or go to **Workspace settings > Apps**, then select the app or app template.

* If the app is not enabled, select **Enable**. If the included app is still a draft, select **Publish** after reviewing the configuration.

* Review **Role access**, **Real-time access**, **Configure actions**, **Configure approvals**, **Indexed search**, and **Sync authorization** where those controls are available for the app. [Read more about configuring apps.](/en/articles/11487775-apps-in-chatgpt#business-and-enterpriseedu-workspace-setup)

* If the app requires provider authentication, ask a test user to connect their account, then run a low-risk test prompt.

The following sections provide a quick guide of setting up an app. Read more about apps [here](/en/articles/11487775-apps-in-chatgpt#business-and-enterpriseedu-workspace-setup).

### Find and review the relevant app or app template

If you know which plugin you want to set up, go to **Workspace settings > Plugins**, select the plugin, and review the included apps and app templates. If an app is required, go to **Workspace settings > Apps** to configure it. Existing role access, action controls, app permissions, and related settings apply to every plugin that uses the app.  
  
You can also go directly to Workspace settings -> Apps when you already know the app or template name. Use **Directory** to enable a new app, **Enabled** to manage an approved app, or **Drafts** to review a custom app awaiting publication. Business apps are enabled by default; Enterprise and Edu apps are disabled by default.  
  
Select the more options menu (...) for the app, then select **View Details** and confirm:

* Which system the app connects to

* What information it can search or fetch

* Whether it can sync data into ChatGPT

* Whether it is required or optional for the plugin

Then review any actions the app can take, especially anything that can create, update, or send information.  
  
If the app connects to sensitive systems or regulated data, pause for the right vendor, legal, security, or [data residency](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) review. For [custom MCP apps](/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt), include the MCP server, authentication model, exposed tools, write-action behavior, and any plugin package that depends on the app in that review before publishing.

### Assign app access and set action and data boundaries

Enterprise and Edu admins and owners can decide which workspace members can use an app by assigning it to [users, groups, or roles](https://help.openai.com/articles/11509118). A plugin that includes the app inherits this access assignment.  
  
You can use [RBAC or app access controls](/en/articles/11750701-rbac) to assign the app only to that group, then expand later once the workflow is validated.  
  
A plugin that uses an app inherits the app's role access, action controls, and related settings. Note that app assignment in your workspace settings controls **who can access the app in ChatGPT**. It does not override the user's existing permissions in the connected source system. Users must still have the appropriate OAuth and other permissions to use the connected system that powers the app.  
  
Admins and owners can also review what the app is allowed to do:

* Keep the first version read-only when possible.

* Allow [write or modify actions](/en/articles/11487775-apps-in-chatgpt#configure-actions) only when the team needs them.

* Require admin review for newly added actions when appropriate.

* Use [domain restrictions](/en/articles/11487775-apps-in-chatgpt#manage-domains) to keep users on approved work accounts.

* [Limit sync to approved folders, drives, repositories, spaces, or channels](/en/articles/10847137-chatgpt-apps-with-sync) when available.

### Publish and validate

When the app settings look right, select Publish.  
  
If the plugin was imported from a marketplace, use Refresh on the workspace plugin when you want to pull the latest version from its original source.  
  
After launch, periodically review access, [action controls](/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business), [sync settings](/en/articles/10847137-chatgpt-apps-with-sync), support questions, [analytics](/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu), and [compliance needs](/en/articles/9261474-compliance-api-for-enterprise-customers).

# Disabling plugins

Plugin status and plugin installation are separate controls. A plugin is essentially a package of instructions (skills) and access to external systems (apps). Disabling a plugin disables the apps and skills within the plugin.

### What “**Disable plugin**” does

In **Workspace settings > Plugins**, open the plugin's more options menu (...) and select **Disable plugin**. The confirmation shows the plugin's enabled apps that will be disabled. This action changes app access; it does not uninstall the plugin package from members who already installed it.  
  
Because app settings are shared, disabling an app can also affect other plugins and ChatGPT experiences that use the same app. Review the affected-app list before continuing.  
  
  
**Available** and **Installed** are installation policies, not app permissions. **Available** lets eligible members install the plugin themselves. **Installed** installs it automatically for the selected role. Neither setting grants access to an app or its underlying data.

## Security and permission considerations

When reviewing a plugin, use the same review process you use for apps in ChatGPT.  
  
Confirm what external system the plugin depends on. Confirm whether the plugin can use read-only actions, write actions, or both. Confirm whether action confirmation is required for sensitive actions. Keep the first rollout limited to a pilot group when possible. Review whether legal, security, privacy, data residency, or vendor approval is needed before expanding access. Periodically review access after rollout.  
  
Apps may have their own terms, privacy policies, and data residency commitments. Review those terms before enabling access for sensitive or regulated workflows.

# FAQ

## Why can't I find the plugin?

The Plugins Directory is visible across ChatGPT plans, but installing and using a plugin can depend on your plan, workspace settings, role, supported surface, and the plugin’s included capabilities. In a managed workspace, ask an admin or owner to confirm the plugin’s Installation policy and any required app access. In Codex, directory changes can take up to six hours to refresh; restart Codex or refresh plugin data before retrying.

## Why does the plugin say an app needs setup?

The plugin may require an app that is not enabled for your role or that still needs configuration. Ask a workspace admin or owner to review the required app. The admin may need to enable it, create it from a template, publish a draft, or assign access before members can use the plugin.

## Why does a plugin say I need to connect required apps?

Some plugins are installed before the required apps are connected. Codex can use the plugin after those required apps are connected and enabled for your role.

## Why can't the plugin access the expected data?

Check both ChatGPT workspace access and the source system. The user must have access to the app in ChatGPT and must also have permission to the underlying content in the connected system.

## Why can't the plugin take an action?

An admin may have limited the app to read-only access, or the action may require confirmation. Ask the admin to review action controls, action confirmation settings, and any source-system permissions required for the action.

## Why is the related plugin still visible in Codex after I disabled an app in ChatGPT?

Disabling an app blocks the plugin from using that app-backed capability, but it does not uninstall an already installed plugin. The plugin may remain visible in Codex, and its skills or other capabilities that do not require the disabled app can remain usable. Ask a workspace admin or owner to review the plugin's required and optional apps, installation policy, and app permissions. See **Disabling plugins** above.

## Why can I see a plugin but only use it in Codex?

Some local or Codex-specific plugins are only usable in Codex. A plugin that was created locally or appears in a personal section may need to be uploaded, imported, or made available by an admin before it can be used by the broader workspace.

## Why don't I have access to skills?

Personal skills in Work are available on paid plans except Free and Go. In a managed workspace, plugin installation and use may also depend on workspace settings, role, and supported surface.
