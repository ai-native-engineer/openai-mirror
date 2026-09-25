<!-- source: https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt -->

# Connected apps in ChatGPT

Learn what connected apps can do, how to manage your accounts, and where to find help with permissions, privacy, and troubleshooting.

Updated: 7 hours ago

Apps connect ChatGPT to services you already use, such as Google Drive or Slack, so you can work with their information in a conversation. Depending on the app, you can ask ChatGPT to find a file, summarize a document, or look up a message.

Some apps also provide interactive experiences, such as maps or cards, or let ChatGPT take supported actions in the connected service.

To get started, choose an available app, connect an account if prompted, and tell ChatGPT what you want to do.

## Availability

App availability depends on the app, your ChatGPT plan, region, workspace, role, model, and the ChatGPT interface you use.

# Connect and manage an app account

1. Open **Apps** or **Plugins**, depending on the options shown for your account, and select the app or the plugin that includes it.
2. Select **Install plugin** if shown. This may also start the app's connection or setup flow.
3. If prompted, select **Connect** or continue the app's setup flow.
4. If the app requires individual authorization, sign in to the account that already has access to the information you want to use.
5. Review the requested services and permissions, then complete any required provider authorization.

Some apps require no individual sign-in or use an administrator-managed connection. Installing a plugin does not replace any account authorization or workspace approval required to use its apps.

For plugin setup, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

To review a connection later, open **Settings**, select **Apps** or **Plugins** as available, and select the app or connected account you want to manage. Some apps support multiple connected accounts.

For complete setup, account-selection, reconnection, and disconnection steps, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

# Use an app in a conversation

After setup, open a supported ChatGPT conversation and describe what you want to do. You can mention an available app or plugin with **@**, or select **+** and choose it from the available menu. Some interfaces place additional options under **More**.

For example, after connecting a Google Drive account that has access to your project files, try:

Find my project brief in Google Drive and summarize the next steps.

ChatGPT may ask for approval before reading information or completing an action. Review the request before approving it.

# Understand app capabilities

Depending on the app, you can:

* Search and reference information from connected services.
* Use supported apps as sources in deep research.
* Some apps support syncing to index content in advance for faster responses and improved quality. For details, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).
* Interact with maps, cards, documents, or other in-chat app experiences.
* Take supported actions, such as creating or updating information.

Live supports connected apps through the plugins available to your account. App availability, account connections, workspace controls, and existing permissions still apply. If an action needs your approval, review it using the on-screen controls in your Voice conversation.

## Use apps with event-triggered tasks

Eligible users can create a task in **Work** that runs when a supported connected app receives a matching event. Supported events include new Gmail messages, new Slack channel messages, and GitHub pull request activity in authorized github.com repositories.

The task can access only the connected account and information allowed by its existing app permissions. Workspace app settings, role permissions, and approval requirements continue to apply. If an action requires approval, the task pauses until you review it. In ChatGPT for Healthcare, event-triggered tasks are turned off by default and are not covered under a Business Associate Agreement (BAA). Do not use them to transmit, store, or process protected health information (PHI).

Event-triggered (webhook-based) tasks can be shared. Eligible recipients use their own connected apps, account permissions, and workspace access to schedule an independent copy.

For more information, see: [Scheduled tasks in ChatGPT](https://help.openai.com/articles/10291617).

# Use apps in a workspace

In ChatGPT Business, many apps are enabled by default, but administrators can change workspace access. New Enterprise and Edu workspaces start with a selected set of enabled apps; these defaults do not change existing workspace settings and do not apply to Healthcare workspaces. Plugin availability, app access, role permissions, and provider-account authorization are separate controls.

If a managed-workspace app shows **Disabled by admin**, ask an administrator to review the app or its plugin in the available workspace settings. If you use a personal account without a workspace administrator, check the app requirements and contact OpenAI Support if the message continues.

For workspace configuration, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

## Compliance

* User conversations, including conversations using any app, are already available in the Compliance API.
* All app calls are logged as part of the [OpenAI Compliance Logs platform](https://chatgpt.com/public/admin/api-reference#tag/Logs:-Apps).
* Read more: [Compliance API for Enterprise Customers](https://help.openai.com/articles/9261474-compliance-api-for-enterprise-customers).

# App permissions

App permission settings determine when ChatGPT asks before reading information or taking an action.

## Permission options

Available options may include:

* **Always ask**
* **Allow read actions**
* **Allow low-risk actions**
* **Allow all actions**, for an eligible app or account

**Allow low-risk actions** applies when no account, workspace, app, or connection setting overrides it. Sensitive actions may require approval or be denied.

**Allow all actions** carries elevated risk because supported actions may run without another confirmation. The standard account-wide and workspace-wide permission selectors do not offer this option.

For account-specific settings, approval prompts, and workspace restrictions, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

## What app permissions do not change

App permissions do not grant an app new access. The data and actions available to an app are determined by the app, the access granted when it was connected, and any workspace controls.

To remove an app's access, disconnect it or ask your workspace administrator to disable it. Changing an app permission only changes when ChatGPT asks before using the access the app already has.

App permissions are separate from settings that apply generally to all conversations in ChatGPT, such as Memory, personalization, data retention, and your choices about whether content may be used to improve models. Manage those features in their respective ChatGPT settings.

# Get help with an app

If an app is missing, will not connect, cannot find expected information, or cannot complete an action, check the selected account, app requirements, provider authorization, and any workspace restrictions.

App use may count toward your ChatGPT plan limits, feature-specific allowances, and limits imposed by the app provider.

For issue-specific steps, see: [Troubleshooting apps in ChatGPT](https://help.openai.com/articles/20001497).

## Provider-specific setup

For setup instructions, account permissions, and provider-specific troubleshooting, see:

* [Google Drive app and setup in ChatGPT](https://help.openai.com/articles/10929079)
* [SharePoint app and setup in ChatGPT](https://help.openai.com/articles/12143177)
* [Microsoft Teams app and setup in ChatGPT](https://help.openai.com/articles/12552368)
* [Outlook Email and Calendar apps in ChatGPT](https://help.openai.com/articles/12512241)
* [Using Slack in ChatGPT](https://help.openai.com/articles/12525822)
* [Connecting GitHub to ChatGPT](https://help.openai.com/articles/11145903)
* [Connecting GitLab to ChatGPT and Codex](https://help.openai.com/articles/20001486)
* [Box app and setup in ChatGPT](https://help.openai.com/articles/12368225)
* [Notion app and setup in ChatGPT](https://help.openai.com/articles/12532955)

# FAQ

## What is the difference between an app and a plugin?

An app connects ChatGPT to an external service, such as Google Drive or Slack, so it can access information or perform supported actions. A plugin packages capabilities into a workflow and can include one or more apps, skills, or both. Some plugins include only skills and do not connect to an external service. Installing a plugin does not bypass an app’s authorization requirements or workspace permissions. For details, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

## Can I remove an app from my workspace or account?

Admins and owners can disable an app from [Workspace settings](https://chatgpt.com/admin/ca). Users can disconnect apps from **Settings > Apps**.

Your connected third-party application may also have its own options for unlinking.

## What does ChatGPT share with apps?

After you enable an app, the app may be able to access information from ChatGPT in order to help provide context for your requests. For example, if the Canva app is enabled and you ask, “Canva, can you turn these ideas into a presentation?”, then the app may access and use relevant context from your ChatGPT conversations (such as names or taglines you have been brainstorming) in order to help generate a design based on what you have discussed.

If you have Memory turned on, when an app is responding to your requests, it may also leverage relevant information from memories to provide more customized and useful interactions for you. For example, if you have Memory turned on and you ask, “Canva, can you design a flyer for my business?”, then the app may access and use relevant context from your memories (such as the fact that you have a dog-walking business) to better customize the requested flyer. You can learn more about[Memory](https://help.openai.com/articles/8590148), including how to disable it or control individual memories.

Apps you enable may also see basic information typically shared when you visit a website, such as your IP address, device or browser type, language and region settings, and approximate location, and can use that information to improve the accuracy of your results. Approximate location is based on your IP address and reflects a general area like your city or region, not your exact street address or GPS coordinates. For example, if you have enabled the Zillow app and ask to find houses nearby, the app can use your approximate location to show listings in your area without you needing to type in a city or ZIP code.

Data shared with apps is handled according to each app’s terms of service and privacy policies, which you will see before enabling the app.

## How does ChatGPT use information from apps?

After you enable an app, ChatGPT can use information in the app as context to help provide responses. If you have. [Memory](https://help.openai.com/articles/8590148) enabled in your settings, ChatGPT may remember relevant information accessed from the app, unless that app or connected source restricts Memory from saving that information. ChatGPT can also use relevant information accessed from apps to inform web search queries when ChatGPT [searches the web](https://help.openai.com/articles/9237897) to provide you with information.

## Does OpenAI use information from apps to train its models?

* For ChatGPT Business, Enterprise, and Edu customers: OpenAI does not use information accessed from connectors to train models by default.

For ChatGPT Free, Plus, Go, and Pro users: OpenAI may use information accessed from apps to train our models if your “Improve the model for everyone” setting is on. You can read more about how your data is stored and used in[this article](https://help.openai.com/articles/7730893) in our help center.
