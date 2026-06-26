<!-- source: https://help.openai.com/en/articles/20001256-plugins-in-codex -->

# Plugins in Codex

Learn how plugins work in Codex, how workspace admins manage plugin availability by role, and how app permissions apply to plugins.

Updated: 15 hours ago

# Overview

Plugins help Codex complete repeatable work by packaging the capabilities it needs for a specific workflow. A plugin can include workflow guidance, such as skills, and can also depend on approved apps that connect Codex to tools, data, or actions.  
  
For Business, Enterprise, and Edu workspaces, plugin availability can depend on workspace settings, feature access, and the apps an admin has enabled. A plugin does not grant new access to data by itself. Users can only use app-backed capabilities when the connected app is available to them and they already have access to the underlying source system.  
  
This article is for workspace admins, owners, and users who need to understand how plugins work and what needs to be enabled before a plugin can be used. Workspace owners and admins can configure plugins from **Workspace settings > Plugins.**

## What is a plugin?

A plugin is a packaged capability for a workflow. Depending on the plugin, it may include:

* [**Skills**](https://help.openai.com/articles/20001066), which provide reusable instructions, prompts, and workflow patterns that help Codex complete a task.
* [**Apps**](https://help.openai.com/articles/11487775), which connect Codex to systems, data, and actions approved for your workspace.
* [**App templates**](https://help.openai.com/articles/20001247), which help an admin create or configure the app the plugin needs.

Some plugins are broad, while others are built for a specific line of business, such as sales, data analytics, or internal operations. A line-of-business plugin may bring together several capabilities so users can complete a job without manually switching between separate tools.

A single plugin may have multiple skills and apps, allowing users to accomplish a wide variety of tasks. The **Plugins** section in **Workspace settings** lets workspace admins manage plugin availability and choose which roles receive a plugin automatically, or disabling the plugin itself. Existing app settings continue to control who can use an app, what actions it can take, and related settings. Any plugin that includes the app inherits those permissions.  
  
Separately, admins and owners can enable some or all apps within a plugin, depending on organizational policy. For example, a sales-focused plugin might include multiple app-backed capabilities that support a sales workflow. You may want to enable the plugin, but disable apps within the plugin that are not relevant to your workspace use. These layered set of controls gives you additional flexibility in plugin usage.

# How plugins use apps

Many plugins depend on apps to reach external systems. For example, a plugin may need access to a workspace-approved app that connects to a repository, data warehouse, CRM, document store, or messaging tool.  
  
Admins and owners control who can use those [apps in ChatGPT](https://help.openai.com/articles/11487775) or Codex. Depending on the app, admins and owners may also control:

* Which users, groups, or roles can access it (Enterprise/Edu only)

  + [Learn more about RBAC](https://help.openai.com/articles/11750701)
* Whether it can read data only or also take actions
* Whether users must confirm actions before they run
* Whether sync, domain restrictions, source boundaries, or other app-specific settings apply.

Approving an app in ChatGPT does not override permissions in the source system. If a user cannot access a file, repository, record, workspace, or channel in the connected system, the plugin should not give them access to it through Codex.

## Plugins that include [app templates](https://help.openai.com/articles/20001247)

Some plugins may include an [app template](https://help.openai.com/articles/20001247) or depend on an app created from a template. App templates are not the same as a ready-to-use app. A workspace admin or owner may need to enter organization-specific configuration, create a draft app, publish it, and assign access before members can use the plugin.  
  
If a plugin depends on an app template that has not been set up yet, members may need an admin to complete setup first. The plugin cannot use the app template by itself.  
  
For more about template setup, see [ChatGPT app templates](https://help.openai.com/articles/20001247).

# Setting up a plugin

Plugins are enabled by default in workspaces, but workspace admins can choose which available plugins are installed automatically for each role. Before asking members to use a plugin, review its requirements and configure any required apps.

A plugin that requires a specific app is available only when that app is enabled for the member's role. Plugins that include only skills, or include optional apps, remain available by default.

1. Go to **Workspace settings > Plugins**, and select the plugin.
2. Click on the ellipsis menu (...) and click **Manage plugin** to review the plugin's included skills, required apps, optional apps, and app templates.
3. Click **Installation policy**, to choose **Available** or **Installed** for each eligible role. **Available** lets members install the plugin. **Installed** installs the plugin for that role by default.
4. If the plugin requires an app, open the required app from the plugin page or go to **Workspace settings > Apps**, then select the app or app template.
5. If the app is not enabled, select **Enable**. If the included app is still a draft, select **Publish** after reviewing the configuration.
6. If the app requires provider authentication, ask a test user to connect their account, then run a low-risk test prompt.

You can also disable a plugin by clicking on the ellipsis menu (...) and clicking **Disable plugin.** This setting is available for plugins which have a single app. You can use this selection to disable the underlying app a plugin relies on.

Note that the plugin will still be available to users for @ mentions in Codex, if installed formerly - but the plugin will no longer be able to use the app.

## Find and review the relevant app or app template

If you know which plugin you want to set up, go to **Workspace settings > Plugins**, select the plugin, and review the included apps and app templates. If an app is required, go to **Workspace settings > Apps** to configure it. Existing role access, action controls, app permissions, and related settings apply to every plugin that uses the app.  
  
You can also go directly to [Workspace settings > Apps](/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) when you already know the app or template name. Start in **Directory** if you are enabling a new app, or check **Enabled** if the app has already been approved. For Business plans, most apps are enabled by default. Use **Drafts** when you are reviewing a custom app that is waiting to be published.  
  
Select the more options menu (...) for the app, then select **View Details** and confirm:

* Which system the app connects to
* What information it can search or fetch
* Whether it can sync data into ChatGPT
* Whether it is required or optional for the plugin

Then review any actions the app can take, especially anything that can create, update, or send information.

If the app connects to sensitive systems or regulated data, pause for the right vendor, legal, security, or [data residency](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) review. For [custom MCP apps](/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt), include the MCP server, authentication model, exposed tools, write-action behavior, and any plugin package that depends on the app in that review before publishing.

## Assign app access and set action and data boundaries

Enterprise and Edu admins and owners can decide which workspace members can use an app by assigning it to [users, groups, or roles](https://help.openai.com/articles/11509118). A plugin that includes the app inherits this access assignment.  
  
You can use [RBAC or app access controls](/en/articles/11750701-rbac) to assign the app only to that group, then expand later once the workflow is validated.

Note that app assignment in your workspace settings controls **who can access the app in ChatGPT**. It does not override the user's existing permissions in the connected source system. Users must still have the appropriate OAuth and other permissions to use the connected system that powers the app.

Admins and owners can also review what the app is allowed to do:

* Keep the first version read-only when possible.
* Allow [write or modify actions](/en/articles/11487775-apps-in-chatgpt#configure-actions) only when the team needs them.
* Require admin review for newly added actions when appropriate.
* Use [domain restrictions](/en/articles/11487775-apps-in-chatgpt#manage-domains) to keep users on approved work accounts.
* [Limit sync to approved folders, drives, repositories, spaces, or channels](/en/articles/10847137-chatgpt-apps-with-sync) when available.

## Publish and validate

When the app settings look right, select Publish.

If the plugin was imported from a marketplace, use Refresh on the workspace plugin when you want to pull the latest version from its original source.

After launch, periodically review access, [action controls](/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business), [sync settings](/en/articles/10847137-chatgpt-apps-with-sync), support questions, [analytics](/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu), and [compliance needs](/en/articles/9261474-compliance-api-for-enterprise-customers).

# Security and permission considerations

When reviewing a plugin, use the same review process you use for apps in ChatGPT.  
  
Confirm what external system the plugin depends on. Confirm whether the plugin can use read-only actions, write actions, or both. Confirm whether action confirmation is required for sensitive actions. Keep the first rollout limited to a pilot group when possible. Review whether legal, security, privacy, data residency, or vendor approval is needed before expanding access. Periodically review access after rollout.  
  
  
[Apps may have their own terms](https://help.openai.com/articles/11509118), privacy policies, and data residency commitments. Review those terms before enabling access for sensitive or regulated workflows.

# FAQ

## Why can't I find the plugin?

Plugin availability can depend on your plan, workspace settings, rollout status, and feature access. If you expected to see a plugin and do not, ask your workspace admin or owner to confirm whether the plugin is enabled for your workspace.

## Why does the plugin say an app needs setup?

Ask a workspace admin or owner to review the required app. The admin may need to enable it, create it from a template, publish a draft, or assign access before members can use the plugin.

## Why can't the plugin access the expected data?

Check both ChatGPT workspace access and the source system. The user must have access to the app in ChatGPT and must also have permission to the underlying content in the connected system.

## Why can't the plugin take an action?

An admin may have limited the app to read-only access, or the action may require confirmation. Ask the admin to review action controls, action confirmation settings, and any source-system permissions required for the action.

## Why is the related plugin still visible in Codex after I disabled an app in ChatGPT?

Plugins can include both app-backed capabilities and skills. Turning off an app or action prevents the plugin from using that app-backed capability, but the plugin may still appear in Codex when other parts of the plugin, such as skills or workflow guidance, are still available. If a visible plugin does not work after an app is disabled or says setup is required, ask a workspace admin or owner to review the underlying app, skill, and plugin availability settings.

## Why don't I have access to skills?

Some plugin behavior may depend on workspace or feature availability. If a plugin is visible but does not work as expected, ask your admin or workspace owner to confirm whether the required plugin, skill, and app capabilities are available for your workspace.
