<!-- source: https://help.openai.com/en/articles/11487775-apps-in-chatgpt -->

# Apps in ChatGPT

Bring your tools and data into ChatGPT so you can search, reference, and work faster without leaving the conversation.

Updated: 2 days ago

*As of December 17, 2025, we are renaming connectors to apps to present a more unified experience. The term now includes both apps that feature interactive UI and connectors that help you search and reference your information in ChatGPT. We are not removing any existing functionality; previously enabled connectors and company knowledge will continue to work as before.*

# Overview

Apps let you work with external tools and information to help you get more done in a ChatGPT conversation. Some apps provide in-chat interactive experiences, while others securely connect to your services and data so ChatGPT can pull relevant context into your responses.  
  
You can use select apps to take actions on your behalf, search and reference information from your data sources, run deep research across multiple sources with citations, or sync content in advance so you have up-to-date information on demand in your workspace’s knowledge base. Available apps are listed in the [ChatGPT app directory](https://chatgpt.com/apps). Browse, discover, and install a wide variety of apps to address your use cases.  
  
Apps are available to all logged-in ChatGPT users, with some exceptions. See the note below.

*Note: some apps may not be available in EEA, GB or Switzerland depending on whether the app partner offers service in the region. Some apps and app functionalities may be only available to Plus/Pro/Business and Enterprise/Edu plans.*

# Connectors are now apps

*To present a single unified experience of connected applications in ChatGPT, we have renamed connectors to apps. See the table below for the new terminology. Functionality has not been affected, and you do not need to reconnect any previously enabled connections.*

| **Previous terminology** | **Current terminology** |
| --- | --- |
| Chat connectors | Apps with file search |
| Deep research connectors | Apps with deep research |
| Synced connectors | Apps with sync |

# App capabilities

Certain app capabilities might be limited to certain ChatGPT plans. For example, an app may have File Search (Chat) capabilities for ChatGPT Enterprise, but only have deep research capability for Plus and Pro.

Apps may have several features to help you accomplish your tasks within ChatGPT.

### Interactive apps

Some apps [include rich, in-chat experiences](https://openai.com/index/introducing-apps-in-chatgpt/) (for example, interactive cards, maps, or playlists).

### Search

Apps can help you search and reference information from connected third-party services, pulling relevant context into your conversation.

### Deep research

Some apps can be used with deep research for complex, multi-source analysis, with citations back to the originals.

### Sync

Some apps support syncing to index content in advance for faster responses and improved quality.

### Write actions

Some apps may be able to take actions, such as creating or updating information in a connected service. Availability depends on the app and how it is configured.  
  
App permissions control when ChatGPT asks before using connected apps. By default, ChatGPT uses **Important actions**, which allows reading from apps automatically but asks before actions that may have a meaningful effect outside ChatGPT, expose sensitive information, or be difficult to undo.  
  
Workspace admins can configure which actions an app is allowed to take and, where available, when members must approve app actions.

# App permissions

Apps let ChatGPT read information and take actions in connected services. App permissions control when ChatGPT must ask before using an app.  
  
These app permissions apply to ChatGPT conversations. Workspace Agents use per-agent controls set by the agent's builder to determine which app actions are available and when end users are asked to approve them. For agent behavior, see: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).  
  
These settings apply after an app is connected. They do not connect an app, expand the access you granted when connecting it, or change the app's own permissions.

## Permission options

Available options may include:

* **Always ask:** ChatGPT asks before taking any app action, including reading information.
* **Any changes:** ChatGPT can read automatically, but asks before changing anything.
* **Important actions:** ChatGPT can read automatically, but asks before important actions. This is the default.
* **Never ask:** ChatGPT can read and take actions automatically. This option has elevated risk because actions can happen without a confirmation prompt.

**Never ask** may not be available as an overall default for every account or workspace. It may still be available as a setting for an individual app.

## Important actions

An important action is an app action that could have a meaningful effect outside ChatGPT, expose sensitive information, or be difficult to undo. ChatGPT evaluates the specific action, information being shared, and action context before it runs.  
  
Examples include:

* Sending or editing an email, message, comment, post, invitation, appointment, or other communication on your behalf.
* Deleting content, canceling an appointment, or removing a reservation.
* Making a purchase, issuing a refund, or managing a financial transaction or subscription.
* Uploading a file, or moving or renaming a file in cloud storage.
* Changing sharing permissions, account access, security settings, or creating access credentials.
* Sharing sensitive personal, financial, health, identity, or authentication information with an app.

ChatGPT considers the full context. For example, saving a private draft is generally lower risk than sending that content to another person. Updating a shopping cart without completing a purchase is generally lower risk than placing the order. Changing a normal preference is generally lower risk than changing a security setting.  
  
If one request includes several actions, ChatGPT considers the highest applicable level of risk. Suspicious or hidden instructions in app content can also cause ChatGPT to ask for approval or block the request.  
  
Not every change is considered important. Lower-risk actions, such as saving a private draft, changing a non-security preference, or updating a shopping cart without completing a purchase, may proceed without asking under **Important actions**. To require approval before any change, select **Any changes**.  
  
Some especially risky actions may be blocked instead of being presented for approval. Selecting a less restrictive app permission does not override safety or workspace protections.

## Change app permissions

For a personal account, you can change your default app permission:

1. Open your profile menu and select **Settings**.
2. Select **Apps**.
3. Under **App Preferences**, find **Ask permission**.
4. Choose your preferred option.

Your default applies to connected apps unless you choose a different permission for a specific app.  
  
To choose a different permission for one app:

1. Go to **Settings > Apps**.
2. Select the connected app.
3. In the app's **Preferences**, choose an option under **Ask permission**.

An app-specific selection overrides your default. Select **Reset to default** to remove the override and use your overall setting again.

## When ChatGPT asks for permission

Before an action runs, ChatGPT shows an approval card with information about the app and the proposed action. Review the details before deciding.  
  
Depending on the action and account, you may see:

* **Deny:** Do not perform the action.
* **Allow** or **Allow once:** Perform this action without changing your saved app permission.
* **Always allow:** Perform the action and allow future actions for that connected app without asking again.

The exact buttons may vary. **Always allow** only appears when a persistent choice is available.  
  
For personal accounts, selecting **Always allow** changes that app's permission to **Never ask** and approves the current action. You can change the app's permission later in **Settings > Apps**.  
  
In managed workspaces, persistent permissions are controlled by workspace administrators, so members may not see **Always allow**. Workspace administrators can set workspace-wide and app-specific app permissions where available.

## What app permissions do not change

App permissions do not grant an app new access. The data and actions available to an app are determined by the app, the access granted when it was connected, and any workspace controls.  
  
To remove an app's access, disconnect it or ask your workspace administrator to disable it. Changing an app permission only changes when ChatGPT asks before using the access the app already has.  
  
App permissions are separate from Memory, personalization, data retention, and your choices about whether content may be used to improve models. Manage those features in their respective ChatGPT settings.

# Apps quickstart

1. Browse apps from the [ChatGPT app directory](https://chatgpt.com/apps), from **Settings > Apps**, or from the **Apps** entry in the sidebar.
2. Select the app you are interested in.
3. Select **Connect** if available.
4. Complete OAuth and enable sync if required.
5. After the app is connected, invoke it in chat by using @ mentions in your prompt or by selecting **+** and then **More** to select the app you want to add.

Read on for more details on setup, including workspace setup options for Business and Enterprise/Edu admins.

# Building your own app

In addition to apps available from the [app directory](https://chatgpt.com/apps), you can build your own custom app (formerly “custom connectors”), including to connect ChatGPT to your own tools and internal data.

* Build apps using the Model Context Protocol (MCP) to let ChatGPT call approved tools and retrieve information from services.
* If you are on a workspace plan, admins can control whether [custom apps are allowed](https://help.openai.com/articles/12584461) and how they are rolled out.
* If you are a developer building an app, the Apps SDK is the recommended way to package and publish app experiences, including apps that use MCP-backed tools. You can get started with building apps by referring to the [Apps SDK documentation](https://developers.openai.com/apps-sdk?utm_source=chatgpt.com).

You can also submit apps for publication to the ChatGPT app directory. If your app is approved, inclusion in the app directory may make your app experience available to eligible ChatGPT users. See [submitting apps to the ChatGPT app directory](https://help.openai.com/articles/20001040) for more information.

# App directory

The [app directory](https://chatgpt.com/apps) helps you browse and discover apps in one place. Browse the app directory from **Settings > Apps**.

Your app directory view depends on your plan type. If you are on a Business or Enterprise/Edu plan, you can see the apps available for your workspace by selecting the workspace-specific tab. You can use other tabs to browse through app categories such as Lifestyle and Productivity.

Select each app entry to bring up the app page, which includes information about the app, such as the app’s capabilities. Select **Connect** to enable the app for use on your account.

Note: the **Connect** button for a given app may be greyed out based on geo restrictions, workspace settings, or your plan type. If the button or tooltip says **Disabled by admin**, ask your workspace admin to enable the app before trying again.

### Connect a new app

You can add apps from **Settings > Apps**.

1. Go to **Settings > Apps**.
2. Browse the app directory, find the app you are interested in, and select **Connect**.
3. Complete the app’s login and authorization flow, if applicable.
4. The app is now available for use in ChatGPT conversations.

### Business and Enterprise/Edu workspace setup

Admins and owners can control app availability from **Workspace settings > Apps**.

* Apps are enabled by default for Business plans.
* Apps are disabled by default for Enterprise/Edu plans.

You can view all available apps from the **Directory** tab. The **Enabled** tab shows apps currently enabled for your workspace, and the **Drafts** tab includes [custom apps being developed](https://help.openai.com/articles/12584461) for your organization.  
  
The **Enabled** tab allows you to search and filter for apps and apply actions to a group of apps by selecting them. For example, you can filter for all apps with write actions and disable them as a group.  
  
Workspace users can browse all available apps in the app directory, but they can only connect to apps that have been enabled by their workspace admin.

### Business workspace setup for admins and owners

Apps are enabled by default for Business plans, including apps with sync. You can manage apps from the **Enabled** tab.

* Select the more options menu (•••) for the app you want to manage.
* Select **App details** to review the app.
* Select **Action control** to review which actions are available for the app.
* Select **Disable** to make the app unavailable for your workspace.
* Select **Manage domains** if you want to limit which accounts workspace members can use to connect the app.

You can also use the search and filtering functionality to select and configure multiple apps, so long as the configuration is common to all selected apps.

### Enterprise/Edu workspace setup for admins and owners

Apps are disabled by default for Enterprise/Edu workspaces. You can enable desired apps for your workspace by accessing the **Directory** tab and selecting **Enable** in the app listing. Depending on the app, you can configure several app features during the enablement process and select **Publish** for the changes to take effect.

### Configure access

Choose this option to configure [RBAC](https://help.openai.com/articles/11750701). By default, the app is available to all users in the workspace, but you can restrict access to specific groups.

### Configure actions

Choose this option to configure the actions an app can perform. Select **Action control** to review which actions the app can use in your workspace. Admins can choose how the app's current actions are handled by allowing all actions, allowing only read actions, or selecting a custom set of actions. If admins select **Custom**, they can also choose how actions added later are handled by selecting **Enable all new actions**, **Only enable new read actions**, or **Disable new actions**.  
  
For non-sync apps, you can also add parameter constraints to actions. Parameter constraints help control what arguments the model is allowed to send to an app when the action is called. You can apply constraints to all non-object fields in an action, such as strings, numbers, booleans, arrays, and objects with nested properties. When a constraint blocks an action, end users will see a message explaining that the action was blocked due to a workspace configuration and which constraint prevented it.  
  
To add a constraint:

1. Select **Parameter Constraints** for the action you want to constrain.
2. Locate the parameter you want to constrain and set the required constraint or filter.
3. Select the save button, such as **Save regex** for string constraints or **Save range** for numeric constraints.

If you want to remove the constraint, select **Parameter Constraints** for the action you want to revert, find the parameter, and then either delete the constraints you imposed or select **Reset to default**.

### Manage domains

If available, choose this option to limit which accounts workspace members can connect to ChatGPT by restricting connected accounts to an approved set of domains. The list of approved domains is configurable per app.

### Enable sync

Some apps may allow [sync](https://help.openai.com/articles/10847137). By default, users have to opt into sync from user settings when they connect the app. Some apps may allow you to enable sync for your entire team.  
  
To enable sync for the app, select the checkbox, then select **Publish**. If the app supports it, you may see additional options to deploy team-wide or enable self-service.

* Select **Deploy to your team** if available to enable sync for your entire team. Your team members will not need to do any additional setup.
* Select **Self-service setup** to allow each team member to set up the app or connector individually from **Settings > Apps**.

After choosing options and publishing the app, it appears in the **Enabled** tab. You can further configure it by using the more options menu (•••) next to the app listing.

* Select **App details** for more information about the app.
* Select **User access** to control RBAC.
* Select **Action control** if available to configure app actions.
* Select **Disable** to make the app unavailable for your workspace.

You can also use the search and filtering functionality to select and configure multiple apps, so long as the configuration is common to all selected apps.

# App templates

Some workspace apps start from an app template. A template is an OpenAI-provided setup flow that lets workspace admins and owners create a workspace-specific draft app using their organization's own provider configuration, such as OAuth credentials, callback URLs, webhook details, or a managed MCP server URL.  
  
After an admin creates and publishes the draft, members use the published workspace app. They do not use the template directly. Admins can manage the published app from **Workspace settings > Apps > Enabled**, including access, action controls, and app permissions where available.  
  
For general setup guidance, see [ChatGPT app templates](https://help.openai.com/articles/20001247).

### Manage apps

After app setup, you can manage app settings from **Workspace settings > Apps**. Select the **Enabled** tab, locate the app you want to manage, and then select the more options menu (•••) for the app you want to manage. Review the section above for various configuration options.

# Apps capabilities by plan

| Plan | Interactive | Search | Deep research | Sync | Write | Custom (MCP) |
| --- | --- | --- | --- | --- | --- | --- |
| Free | ✔︎ | Limited | Limited |  | ✔︎ |  |
| Go | ✔︎ | Limited | Limited |  | ✔︎ |  |
| Plus | ✔︎ | ✔︎ | ✔︎ |  | ✔︎ | ✔︎ |
| Pro | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ |
| Business | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ |
| Enterprise/Edu | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ |

Note: Some apps with search and deep research capabilities may not be available to Free/Go users; the **Connect** button on the listing for these apps will be greyed out.

# Supported apps and capabilities

Note: information about apps is now available in the app directory, which is the source of information for any new apps added. Refer to the [app directory listing](https://chatgpt.com/apps) for the most current information on supported apps.

# Admin controls, security, and compliance

* Workspace owners and admins manage app availability from settings. Enterprise/Edu workspaces can configure [RBAC](https://help.openai.com/articles/11750701) for apps.
* User conversations, including conversations using any app, are already available in the Compliance API.
* All app calls are logged as part of the [OpenAI Compliance Logs platform](https://chatgpt.com/admin/api-reference#tag/Logs:-Apps).
* Read more: [Compliance API for Enterprise Customers](https://help.openai.com/articles/9261474-compliance-api-for-enterprise-customers).

# FAQ

### Which models can I use with apps?

Apps are available with all models with the exception of the Pro models.

### In Enterprise, Edu, and Business workspaces, who can enable or disable apps?

Workspace owners and admins manage availability in settings. For Enterprise and Edu, owners can configure role-based access controls (RBAC).

### Are there special rate limits for apps?

No. Apps follow normal ChatGPT rate limits for your plan (external apps may impose their own caps).

### Can I remove an app from my workspace or account?

Admins and owners can disable an app from [Workspace settings](https://chatgpt.com/admin/ca). Users can disconnect apps from **Settings > Apps**.  
  
Your connected third-party application may also have its own options for unlinking.

### What does ChatGPT share with apps?

After you enable an app, the app may be able to access information from ChatGPT in order to help provide context for your requests. For example, if the Canva app is enabled and you ask, “Canva, can you turn these ideas into a presentation?”, then the app may access and use relevant context from your ChatGPT conversations (such as names or taglines you have been brainstorming) in order to help generate a design based on what you have discussed.  
  
If you have Memory turned on, when an app is responding to your requests, it may also leverage relevant information from memories to provide more customized and useful interactions for you. For example, if you have Memory turned on and you ask, “Canva, can you design a flyer for my business?”, then the app may access and use relevant context from your memories (such as the fact that you have a dog-walking business) to better customize the requested flyer. You can learn more about [Memory](https://help.openai.com/articles/8590148), including how to disable it or control individual memories.  
  
Apps you enable may also see basic information typically shared when you visit a website, such as your IP address, device or browser type, language and region settings, and approximate location, and can use that information to improve the accuracy of your results. Approximate location is based on your IP address and reflects a general area like your city or region, not your exact street address or GPS coordinates. For example, if you have enabled the Zillow app and ask to find houses nearby, the app can use your approximate location to show listings in your area without you needing to type in a city or ZIP code.  
  
Data shared with apps is handled according to each app’s terms of service and privacy policies, which you will see before enabling the app.

### How does ChatGPT use information from apps?

After you enable an app, ChatGPT can use information in the app as context to help provide responses. If you have [Memory](https://help.openai.com/articles/8590148) enabled in your settings, ChatGPT may remember relevant information accessed from the app, unless that app or connected source restricts Memory from saving that information. ChatGPT can also use relevant information accessed from apps to inform web search queries when ChatGPT [searches the web](https://help.openai.com/articles/9237897) to provide you with information.

### Does Voice mode support apps?

Voice mode currently does not support apps.

### Does OpenAI use information from apps to train its models?

* For ChatGPT Business, Enterprise, and Edu customers: OpenAI does not use information accessed from connectors to train models by default.

For ChatGPT Free, Plus, Go, and Pro users: OpenAI may use information accessed from apps to train our models if your “Improve the model for everyone” setting is on. You can read more about how your data is stored and used in [this article](https://help.openai.com/articles/7730893) in our help center.
