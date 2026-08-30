<!-- source: https://help.openai.com/en/articles/12628342-company-knowledge-in-chatgpt -->

# Company knowledge in ChatGPT

Use the Company Knowledge plugin and the sources available to you to get organization-specific answers in ChatGPT.

Company Knowledge is a plugin that helps ChatGPT answer organization-specific questions using the knowledge sources available to you. It replaces the previous company knowledge option in chat.

* Get organization-specific answers that help you plan, decide, and act.
* Works with supported sources available to you in ChatGPT, including connected apps and custom apps built with MCP.

A supported administrator-managed Google Drive source can be available without an individual connection. This is separate from an admin installing the Company Knowledge plugin: installing the plugin does not connect your app accounts.

* Use supported [custom apps](https://help.openai.com/articles/12584461) built with MCP to access company-specific data when those apps are available to you in ChatGPT.
* Enterprise and Edu administrators and owners can control app access using RBAC.
* Apps can include capabilities such as search, interactive UI, and writes. See the Apps SDK for more info.

To use Company Knowledge, the plugin must be available to you and installed, and you need at least one supported knowledge source. App access and provider authorization still apply; installing the plugin alone does not grant access to source data.

The steps in this article cover ChatGPT on the web.

# Availability and requirements

* Plans: Available on ChatGPT Business, Enterprise, and Edu.
* Prerequisites:
* Your workspace must allow the Company Knowledge plugin and the sources you want to use. An admin may need to enable a plugin or source that is not already available.
* Knowledge sources must be supported by the plugin and available to you in ChatGPT.
* The app must also be enabled for the workspace and connected for the user, unless an admin-managed connection applies.
* Members authenticate a provider account when the selected app requires individual authorization. Some supported sources are available through an administrator-managed workspace connection instead.

# How it works

* Make sure the Company Knowledge plugin is installed, then open a new or existing conversation in ChatGPT.
* Enter **@Company Knowledge** in the message composer, or select **Company Knowledge** from the **+** tools menu.
* Ask your question (for example: “Summarize this account’s latest feedback and risks”).
* If the plugin asks you to connect an app needed for your request, complete the connection if your workspace allows it.
* To connect another source, follow the app’s connection process. For setup, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).
* Review the answer and any source links provided before relying on the information.

# App setup and availability

Company Knowledge uses enabled, eligible apps. For general app discovery and workspace access, see: [Connected apps in ChatGPT](https://help.openai.com/articles/11487775).

* Workspace owners and administrators can manage plugin and source access in **Admin > Plugins**. The **Apps** administration page may also remain available.
* To install Company Knowledge for eligible roles, open the plugin’s details and set **Installation policy** to **Installed**. Plugin installation does not connect individual app accounts or grant access to source data.
* Apps are enabled by default in ChatGPT Business. New Enterprise and Edu workspaces start with a selected set of enabled apps. This change does not alter existing workspace settings and does not apply to Healthcare workspaces. Administrators can change app availability.
* You can discover workflows in the plugins directory, then connect any supported included apps and complete required authentication. A supported administrator-managed source may already be available without an individual connection.
* For workspace-built integrations, see: [Developer mode and custom apps in ChatGPT](https://help.openai.com/articles/12584461).
* Enterprise admins/owners can use RBAC to further control access to apps.

# Security, safety, and data considerations

Company Knowledge respects permissions in the connected source. A member can retrieve only information they are already allowed to access through an individually authorized account or a supported administrator-managed connection.

Enterprise and Edu administrators and owners can manage access to individual apps using RBAC and group-level permissions. They can also require SSO and SCIM for account and user provisioning.

# Compliance

Eligible Enterprise and Edu workspaces can review supported app and conversation events through the Compliance Platform when it is available and configured. For details, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# Limitations and known behaviors

* Select **Company Knowledge** with an **@** mention or from the **+** tools menu when you want to use it. ChatGPT may also use the plugin without an explicit mention.
* When Company Knowledge isn’t selected, ChatGPT may still use apps automatically as part of the default experience.
* The plugin does not override workspace access controls or app permissions. For app-action and approval settings, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

# FAQ

## Who can use Company Knowledge?

Company Knowledge is available to eligible ChatGPT Business, Enterprise, and Edu workspace members when supported sources and administrator settings allow access.

## Do admins need to enable anything before users can start?

Not always. Apps are enabled by default in ChatGPT Business. New Enterprise and Edu workspaces start with a selected set of enabled apps; this does not change existing settings or apply to Healthcare workspaces. An admin may still need to enable the Company Knowledge plugin or a source that your workspace does not allow.

## Is Company Knowledge enabled for everyone?

You can use Company Knowledge when the plugin is available and installed for you and at least one supported source is authorized and available to you.

## Do users need to sign in to each app?

Authenticate an individual provider account when the selected app requires it. An eligible administrator-managed source may be available without an individual connection. For setup, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

## Does Company Knowledge respect our existing permissions?

Yes. ChatGPT can only access what each user is already allowed to view.

## How are permissions enforced?

Company Knowledge respects existing permissions in your connected apps. Users only see what they already have access to.

## Does OpenAI train on our data?

OpenAI does not use ChatGPT Business, Enterprise, or Edu workspace data to train its models by default. For data-use details, see: [Data sharing and privacy for apps in ChatGPT](https://help.openai.com/articles/20001496).

## Will responses show where information came from?

When an answer includes citations or source links, use them to verify the information.

## Which apps are supported?

The plugin discovers the knowledge sources available to you when it runs. App availability can depend on your plan, workspace settings, role, and the app’s own requirements.

## Does it work with custom apps built in developer mode?

The plugin can discover supported [custom apps](https://help.openai.com/articles/12584461) built with MCP when those apps are available to you in ChatGPT. Workspace access, app permissions, and provider authorization still apply.

## Where do answers come from and can I verify them?

The plugin uses the knowledge sources available to you. If an answer includes source links, open them to check the details.

## Is data residency supported?

Company Knowledge uses the apps and administrator-managed sources available to your workspace. Data residency support for sync depends on the provider and your workspace’s configured region. General ChatGPT data residency availability does not mean every app supports sync in that region.

For supported sync setup regions, see: [Administrator-managed apps with sync in ChatGPT](https://help.openai.com/articles/10847137).

GitHub does not offer administrator-managed sync.

## Are there any geo restrictions?

A partner app may have regional restrictions. If an app is unavailable in your region, its connection option may be unavailable in the plugin or app details.
