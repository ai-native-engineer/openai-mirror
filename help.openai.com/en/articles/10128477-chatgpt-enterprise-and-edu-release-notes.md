<!-- source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes -->

# ChatGPT Enterprise and Edu release notes

Review new features, administrative controls, and product updates for ChatGPT Enterprise and Edu.

Updated: 3 hours ago

# September 11, 2026

## Group Managers for ChatGPT Enterprise

In ChatGPT Enterprise, workspace owners and admins can designate a workspace member as a group manager and delegate selected group administration, such as analytics, usage limits and requests, or permitted feature and model permissions on assigned roles. This designation is separate from the member’s built-in workspace role.

For supported actions and setup, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

## Test a member’s model access

Admins can use **Models > Test** in [Admin Console](https://admin.openai.com) to inspect a member’s model access and the settings behind it. Testing does not grant access, change usage limits, or override plan or seat eligibility.

For the steps, see: [ChatGPT Enterprise and Edu - Models & Limits](https://help.openai.com/articles/11165333).

## Audit logs for Codex policies and configurations

Changes made through the Codex **Policies & Configurations** interface are recorded in workspace audit logs. Authorized admins can review the logs in the UI or retrieve them through the Compliance API.

For access and retrieval guidance, see: [OpenAI Compliance Platform for Enterprise and Edu Customers](https://help.openai.com/articles/9261474).

## Create, update, and delete groups with the Admin API

The Groups Admin API supports group creation, updates, and deletion in eligible workspaces, helping admins automate recurring group-management tasks. Workspace access and the required Admin key permissions still apply.

For setup and permissions, see: [Managing Admin keys in Admin Console](https://help.openai.com/articles/20001407).

## Quick chats from the desktop

In the ChatGPT desktop app for macOS and Windows, you can now send typed requests from the floating Pets controls and check task progress without opening the main window.

Choose **Mini** in **Settings > Pets** to use the controls without a companion. Open Quick Chat with Option+Space on macOS or Windows+Alt+P on Windows. Existing workspace restrictions on Pets still apply. [Learn more](https://learn.chatgpt.com/docs/pets?surface=app).

## Appshots on Windows

Appshots are now available on Windows. Press both Alt keys to share the frontmost app’s window with ChatGPT, then describe the help you need. The attachment includes a screenshot and text the app makes available, which can extend beyond the visible area.

You can change the shortcut and destination chat in settings. On Windows, Appshots open in the main app. Your organization’s Appshots settings still apply. [Learn more](https://learn.chatgpt.com/docs/appshots).

# September 10, 2026

## Data plugin in ChatGPT Work and Codex

The Data plugin helps you analyze connected business data in ChatGPT Work and Codex. Ask a business question, investigate changes, or create an interactive dashboard or report. You can refine the analysis with follow-up questions and bring in your team’s metric definitions and other business context.

Administrators can select Data in **Workspace settings** > **Plugins** to review its installation policy and manage access by role or group. Data-source plugins and their apps may need separate setup. Members can start with `@Data`; connected-account permissions and workspace access controls apply. [Learn more](https://help.openai.com/articles/20001518).

# September 9, 2026

## **Updated models and usage limits in ChatGPT Voice**

ChatGPT Voice can now use GPT-5.6 or GPT-6 Astra when it needs to search or reason through harder questions. Choose your model and reasoning effort using the same controls as text chat. Available models and their usage limits depend on your plan and workspace settings.

We’re also updating GPT-Live pricing and daily usage limits:

* Enterprise workspaces with usage-based billing in U.S. dollars: $0.05 per minute.
* Enterprise and Edu workspaces using credits: 1.25 credits per minute, down from 5 credits.
* Legacy Enterprise and Edu plans: Up to 3 hours with GPT-Live-1, replacing the previous Live and mini allowances.

Legacy Enterprise and Edu plans no longer switch to GPT-Live mini after reaching a Voice limit. Search and reasoning usage follows the selected model’s normal limits and pricing, separately from Voice usage.

With these updates, the separate Instant/Medium/High Voice intelligence levels are deprecated.

Learn more: [https://help.openai.com/en/articles/20001274-chatgpt-voice](/en/articles/20001274-chatgpt-voice)

## **Share files and folders from your Library**

Library sharing lets you share files and folders in ChatGPT, choose who can access them, and work with shared content directly in your conversations.

### **What’s new**

* **Share with specific people.** Invite recipients and assign Viewer or Editor access.
* **Share across your workspace.** Make content available to everyone in your workspace.
* **Manage access.** Review who has access, change permissions, or remove access from the sharing dialog.
* **Find and use shared content.** Access items in **Shared with me** and use shared files in conversations with ChatGPT.

### **Shared folders and ownership**

Files uploaded to a shared folder belong to the folder’s owner. The person who uploaded each file is still recorded.

If you upload a file to someone else’s shared folder and they later remove your folder access, the file stays in their folder and you lose access to it.

### **Workspace admin controls**

Admins can control whether members can create Library shares or change sharing permissions, with controls for the workspace and role default groups.

Turning off Library sharing prevents new shares and permission changes. **Existing shared content remains accessible**, and members can still access content shared with them.

## Deep Research in ChatGPT Work and Codex

Deep Research in Work helps members investigate complex questions across the web, files, and supported authorized apps, then produce a cited deliverable they can review and refine. Members with Work/Codex access can type @Deep Research or explicitly ask for deep research on web, desktop, iOS, or Android.

Admins manage the Deep research permission under Workspace settings → Permissions & roles. Web search must also be enabled. Workspace and connected-source permissions continue to apply. Deep research uses the existing Work/Codex allowance or credits - limits in Chat are unchanged. Learn more about [deep research](https://help.openai.com/articles/10500283) and [workspace controls](https://help.openai.com/articles/11509118).

## Codex CLI worktrees and workflow improvements

Codex CLI 0.154.0 adds experimental support for starting or forking tasks in separate Git worktrees. You can browse and resume those worktrees, and answer questions inline while Codex continues working.

The update also preserves formatting when you copy responses and refreshes plugin tools in existing sessions. Update the CLI to use these changes. [Learn more](https://learn.chatgpt.com/docs/codex/cli).

# September 8, 2026

## Codex task and worktree improvements on iOS

ChatGPT for iOS 1.2026.244 lets you reference another task with `@` and answer Codex’s questions while work continues, without replacing your draft. File browsing now keeps your reading position and adds recent files and Back navigation.

When starting a remote worktree, you can choose a branch or include current local changes. On iOS 26, setup can continue in the background with a Live Activity. Remote work requires a connected computer and follows workspace settings. [Learn more](https://learn.chatgpt.com/docs/remote).

# September 3, 2026

## Zendesk & OneNote Plugins in ChatGPT and Codex [Beta]

Today, we added the Zendesk and OneNote plugins in the Plugin directory. The Zendesk plugin helps teams review support tickets and customer history, find relevant knowledge, and prepare replies in ChatGPT and Codex. Members connect their own Zendesk accounts to work with the support information they can access.

The OneNote plugin helps you find and summarize notes, gather decisions and action items, and create or update notes through supported actions in ChatGPT and Codex.

Read more: [Zendesk Plugin](https://help.openai.com/articles/20001512), [OneNote Plugin](https://help.openai.com/articles/20001511).

## Share Sites with people outside your workspace

Eligible ChatGPT Enterprise workspaces can now let Site owners share live Sites with named external viewers. Recipients sign in with the account that was granted access and can view the shared Site without joining the workspace. Additionally, viewer access does not grant editing or publishing rights, or make the Site public.

Workspace owners and admins can allow invitations for selected roles in **Workspace settings** > **Permissions & roles** by enabling **Sites** and **Allow members to invite external visitors to sites**. This permission is separate from public publishing. Learn more about the controls in [Managing ChatGPT Sites for your workspace](/en/articles/20001338).

## More control over browser and computer use

New policy settings give enterprise admins more control over how supported desktop clients use browsers and native apps. Admins can set website defaults and exceptions, restrict uploads, downloads, browser history and developer access, and control automatic review, saved approvals and how long site approvals last. Native-app rules can allow or block specific macOS and Windows apps. Admins can also restrict importing data from another browser.

Where the policy editor is available, open Codex Policies and Configurations and edit the policy’s Requirements. Controls apply on supported clients and platforms; allowing a site or app does not bypass other policies or approval prompts. Learn more about [managed browser and computer-use controls](https://learn.chatgpt.com/docs/enterprise/managed-configuration#control-browser-and-computer-use).

# September 1, 2026

## **Healthcare plugins for ChatGPT and Codex**

Eligible ChatGPT for Healthcare and HIPAA-enabled ChatGPT Enterprise workspaces can now use two healthcare plugins in ChatGPT and Codex:

* **Healthcare Public Data:** Search nine public healthcare sources for medical research, clinical trials, medication information, Medicare data, and provider records. The plugin is read-only and does not access patient charts.
* **Epic:** Review authorized patient information from your organization’s Epic electronic health record. Access is read-only and requires an administrator-configured Epic EHR app, an individual Epic sign-in, and existing patient-chart permissions.

Admins manage plugin availability and app access separately. Do not include protected health information in searches sent to public healthcare sources. Before using Epic with protected health information, confirm your organization has an applicable Business Associate Agreement and an approved workspace configuration.

Learn more: [Using Healthcare Public Data in ChatGPT and Codex](https://help.openai.com/articles/20001489) and [Using the Epic plugin with ChatGPT and Codex](https://help.openai.com/articles/20001490).

# August 28, 2026

## Import and sync plugin marketplaces from GitHub

Workspace admins and owners can centrally distribute plugin marketplaces from public or private GitHub repositories and keep plugins up to date with automatic daily sync. Go to **Workspace settings > Plugins** and select **Add > Import marketplace** to get started, or select **Sync now** on a marketplace to request an update.

Admins and owners control installation policies for eligible roles and required app access in workspace settings. Repository policy values do not override these settings, and app permissions and authentication requirements still apply. [Learn more](https://help.openai.com/articles/20001504) about marketplace setup and review [supported formats and configuration](https://learn.chatgpt.com/docs/enterprise/plugin-management).

# August 27, 2026

## **Centralized identity management in Admin Console**

Eligible ChatGPT Enterprise and Edu customers can now manage more workspace and identity settings in [Admin Console](https://admin.openai.com/):

* Manage workspace members, groups, roles, permissions, and general settings.
* Sync users and groups once through centralized, tenant-wide SCIM, then assign groups to supported ChatGPT workspaces or Ads accounts.
* Manage users and roles for Ads accounts, where available.

Existing workspace-level SCIM configurations remain supported.

Learn more: [Managing your tenant in Admin Console](https://help.openai.com/articles/12289294) and [SCIM provisioning and management](https://help.openai.com/articles/10011769).

## Model access controls, workspace settings, and Windows improvements

We’ve released some improvements affecting Enterprise/Edu workspaces:

* Model access controls let workspace owners manage access to supported models at the workspace and role level.
* Users, Groups, Roles, Permissions, and General settings are now in the admin console - they’re still available in Workspace settings, and clicking on existing tabs will take you to the admin console. Existing permissions still apply. To learn more, see: [role-based access controls](https://help.openai.com/articles/11750701) and [workspace settings](https://help.openai.com/articles/8411955).
* Codex improvements on Windows include `codex doctor` diagnostics, Remote Control from Windows to other devices, and preferred Linux distribution selection when multiple WSL distributions are installed. Managed devices need an administrator-approved build through MDM. Availability depends on your workspace and app build. To learn more, see: [Codex](https://help.openai.com/articles/11369540).

# August 25, 2026

## Shared scheduled tasks and webhook-triggered tasks

Enterprise, Edu, and ChatGPT for Healthcare workspace members can share customizable scheduled tasks within their workspace. Admins can also enable webhook-triggered tasks in Work so approved apps can surface relevant updates without repeated manual checks. In ChatGPT for Healthcare, these tasks are not covered under a Business Associate Agreement (BAA) and must not be used to transmit, store, or process protected health information (PHI).

Supported webhooks include new Gmail messages, Slack channel messages, and GitHub pull request activity.

### Create webhook-triggered tasks

Eligible members can ask Work on web, iOS, and Android to respond to a new Gmail message, Slack channel message, or supported GitHub pull request event. For example, ask ChatGPT to summarize client feedback from Slack or prepare next steps after a GitHub pull request changes. Members need access to Work and the approved app. Add @ChatGPT to each monitored Slack channel. Enterprise, Edu, and ChatGPT for Healthcare admins must first enable Allow event-triggered scheduled tasks in Permissions & roles > Work. This permission is off by default.

### Share scheduled tasks

Eligible members can share scheduled or webhook-triggered tasks with others in the same workspace, who can review and customize the instructions and, when applicable, the schedule. Admins control sharing with **Share chats and scheduled tasks in the workspace**. Scheduling a webhook-triggered copy also requires **Allow event-triggered scheduled tasks**, access to **Work**, and the recipient’s own approved connected app.

For more information, see: [Scheduled tasks in ChatGPT](https://help.openai.com/articles/10291617).

# August 20, 2026

## Enterprise feature updates

* **Workspace owners and admins can use new workspace-scoped Admin APIs to automate invitation and member administration.** Invitation APIs support listing, retrieving, creating, resending, and deleting invitations. User APIs support retrieving accepted members and, for workspace owners, updating built-in roles or seats and removing workspace memberships. SCIM-managed changes continue through the identity provider, and last-owner protections apply. For setup and permissions, see [Managing Admin keys](https://help.openai.com/articles/20001407). For endpoint paths and schemas, see the [Admin API reference](https://chatgpt.com/public/admin/api-reference).
* **The Global Admin Console now makes it clearer which tenant or workspace you are working in and adds workspace-specific URLs for supported pages.** Workspace members can view analytics limited to their own activity, while cross-user views remain available only to authorized roles. ChatGPT Workspace Settings remain in their current location. [Learn more about the Global Admin Console](https://help.openai.com/articles/12289294).
* **Personal Analytics supports Work and Codex for eligible Enterprise and Edu workspaces.** After an admin enables the plugin, members can install it in ChatGPT Desktop and ask about activity associated with their signed-in identity and privacy-protected aggregate workspace trends. It is read-only and cannot show another user’s individual activity or another workspace’s data. [Learn more about Personal Analytics](https://help.openai.com/articles/20001478).
* **Collaborate on ChatGPT Sites (Enterprise only).** In Enterprise workspaces, Site owners can add active members of the same workspace as editors. Editors can update and save a Site and, after the owner publishes it for the first time, publish later versions to the same Site URL. Owners keep control of sharing, Site settings, analytics, ownership, version restoration, and editor access. Co-editing uses the existing Sites workspace controls and does not add a separate RBAC toggle; public publishing remains off by default and admin-controlled. [Learn more about managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338).
* **Use Apple Messages from Codex and ChatGPT Work.** On Apple silicon Macs, the Apple Messages plugin in the ChatGPT desktop app can read and search iMessage, SMS, and RCS conversations and prepare or send messages through Messages. By default, ChatGPT asks the user to approve the message and recipients before sending. Managed-workspace admins can disable Apple Messages through the existing Computer Use control. [Learn more about the Apple Messages plugin](https://developers.openai.com/codex/plugins?surface=app#app-use-apple-messages-from-codex).
* **Use Computer History in more regions (Enterprise only).** Computer History is now available in the EEA, Switzerland, and the United Kingdom for Enterprise users in the ChatGPT desktop app on macOS. It is off by default, requires Memories, and must be enabled by a workspace admin before a member can opt in. [Learn more about Computer History](https://developers.openai.com/codex/customization/computer-history).
* **Share a read-only snapshot of a Codex chat.** Workspace share links are limited to authenticated members of the originating workspace, and admins can turn off workspace share links. A snapshot does not update when the original chat changes. Codex redacts known secret patterns, but users should review the snapshot because sensitive paths, diffs, images, or other content may remain. [Learn more about sharing a Codex chat](https://developers.openai.com/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread).
* **Export the public plugin catalog.** Eligible ChatGPT Enterprise workspace owners and admins can export a CSV from **Admin > Plugins > Public > Export CSV**. The export can be up to 48 hours old, and excludes workspace-created plugins [Learn more about exporting the public catalog](https://developers.openai.com/codex/enterprise/apps-and-connectors#export-the-public-catalog-for-review).

# August 13, 2026

## Chat model defaults

Workspace owners and admins can configure the starting Chat model and reasoning level from **Workspace settings > Models**. Owners and admins can apply an admin default or allow **User’s last choice** for new chats - note that defaults do not grant access to unavailable models or override enforced workspace requirements.

The ChatGPT Desktop app should be upgraded to version 26.812.10818 or later for the new controls to take effect.

## Updated model picker for Enterprise and Edu

Members in the Enterprise/Edu workspaces have updated model-picker and composer experience. The picker makes the available intelligence choices easier to compare while preserving workspace model availability and access controls.

## Audit logs in the Global Admin Console

Workspace owners and admins can now review supported audit events from the [Global Admin Console.](https://admin.openai.com) Access and event coverage depend on the selected workspace and admin role. [Read more](https://help.openai.com/articles/12289294#audit-logs).

## Additive role-based access controls

Workspace owners in Enterprise and Edu workspaces can now configure eligible permissions in ordinary custom roles with **Default**, **On**, or **Off**. **Default** inherits the workspace setting, **On** explicitly grants the permission, and **Off** denies access through that role only. ChatGPT evaluates all applicable ordinary roles additively: if any role grants the permission, either explicitly or by inheriting an enabled workspace setting, the member retains access. An **Off** setting denies access through that role only. If every applicable role is set to **Off**, access is denied. Lockdown Mode is evaluated separately and can further restrict network-enabled capabilities. Learn more about [role-based access controls](https://help.openai.com/articles/11750701).

## Work and Codex usage and cost data

Members of eligible Enterprise workspaces with credit-based billing can review per-chat lifetime credit usage across Work and Codex. Usage figures and estimated costs are planning aids and are not invoices. Members can also review monthly usage and history from the **Usage & billing tab** in ChatGPT Desktop. Regular Chat usage is not included. This feature requires ChatGPT Desktop version 26.812.10818 or later. [Read more](https://help.openai.com/articles/20001478).

## Personal Analytics plugin

The Personal Analytics plugin is available for eligible workspaces. After a workspace owner or admin enables the plugin, members can install it in ChatGPT Desktop and ask questions about their own Work and Codex activity and available aggregated workspace trends. [Read more](https://help.openai.com/articles/20001478).

## Codex service accounts

Eligible workspaces can create non-human service accounts for Codex automation. Workspace owners and admins can assign roles and groups, configure plugins, share account management, and issue scoped access tokens for CI runners and scheduled jobs. [Read more](https://developers.openai.com/codex/enterprise/service-accounts).

## Windows desktop performance improvements

The ChatGPT desktop app for Windows includes performance improvements. These improvements require ChatGPT Desktop version 26.803.41515 or later.

## Computer History for ChatGPT Enterprise

Computer History is an optional feature in the ChatGPT macOS app that lets Enterprise members bring context from selected apps and websites into ChatGPT and Codex. It records interaction events—not screenshots, screen recordings, microphone input, or system audio—and private browsing is not included.

Computer History is off by default, and Enterprise admins can grant access by role before each member chooses whether to opt in. Members can pause Computer History, choose included apps and sites, and inspect or delete timeline items. Note that Computer History is not currently available in the EEA, UK or Switzerland.

# **August 10, 2026**

## **Retiring individual-user sync for connected apps**

Starting August 10, new individually authorized sync connections will no longer be available. On August 14, existing individual-user sync connections will be disabled, and deletion of associated synced data will begin. Administrator-managed sync is unaffected. By August 14, review your workspace’s connector settings and take the following actions where applicable:

| **Connector** | **Required admin action** |
| **Google Drive** | Enable the Google Drive plugin. If synced knowledge is required, configure admin-managed Google Drive sync using domain-wide delegation. |
| **SharePoint** | Enable the SharePoint plugin. If synced knowledge is required, configure admin sync. |
| **GitHub** | Enable the non-synced GitHub plugin. |
| **GitLab Issues** | We will communicate availability of the replacement plugin soon. |
| **Azure Boards (Azure DevOps)** | We will communicate availability of the replacement plugin soon. |
| **Basecamp** | We will communicate availability of the replacement plugin soon. |
| **Help Scout** | Identify affected users and workflows, and notify them that synced access will end. We are actively working with the partner to provide a replacement. |
| **Zoho Desk** | Identify affected users and workflows, and notify them that synced access will end. We are actively working with the partner to provide a replacement. |
| **Teamwork** | Identify affected users and workflows, and notify them that synced access will end. We are actively working with the partner to provide a replacement. |
| **Aha!** | Identify affected users and workflows, and notify them that synced access will end. We are actively working with the partner to provide a replacement. |
| **Zoho CRM** | Identify affected users and workflows, and notify them that synced access will end. We are actively working with the partner to provide a replacement. |
| **Pipedrive** | Identify affected users and workflows, and notify them that synced access will end. We are actively working with the partner to provide a replacement. |

# August 7, 2026

## Files and Projects in ChatGPT Voice

GPT-Live in ChatGPT Voice now supports file uploads and Projects. You can now upload files in a voice conversation and analyze its contents or ask questions. You can also use voice in Projects, referencing recent project chats, sources, and project instructions.

## Live is now the default Voice experience

For Enterprise, Edu, and Healthcare workspaces, Live is now the default Voice experience when a workspace owner enables Voice - the Early Model Access setting enablement is no longer required. Workspace owners can turn off Voice by disabling Voice in workspace settings.

[Learn more about ChatGPT Voice](/en/articles/20001274).

# August 6, 2026

## New controls for desktop app updates

ChatGPT Enterprise, ChatGPT for Healthcare, and ChatGPT Edu admins can now turn off in-app updates for the ChatGPT desktop app on supported macOS and Windows builds. This lets organizations review new releases before users receive them and deploy approved versions through their existing device management process.

The app's built-in updater remains enabled by default. Organizations that turn it off are responsible for promptly deploying new releases and security fixes; OpenAI does not provide version pinning, a separate stable release channel, or extended support for older versions. [Learn more](https://learn.chatgpt.com/docs/enterprise/manage-app-updates).

# **August 4th, 2026**

## **Large pastes are now handled as attachments for all plans**

Starting today for **ChatGPT Enterprise and Education** users, long pastes are handled differently in ChatGPT.

If you paste **more than 10k characters** into the composer, ChatGPT will automatically convert the content into an **attachment** instead of inserting it directly into the text field. This keeps the composer cleaner and helps prevent large pastes from consuming your entire context window.

You can still move the content back into the message at any time by clicking on **Show in text field** to convert the attachment back to a direct paste.

This is already available to users on all other plans.

## **Education plugins for teaching and learning**

ChatGPT Edu workspaces now have access to three guided plugins in ChatGPT Work and Codex: **College Educator**, **K–12 Educator**, and **College Student**. ChatGPT for Teachers workspaces managed through a district domain claim have access to **K–12 Educator**. These plugins can help educators create lessons, assessments, and communications grounded in course materials, and help college students build study plans and practice course concepts.

* **College Educator:** Helps faculty design and update courses and syllabi, create interactive learning materials and multimedia assessments, adapt materials for diverse learners, and package content for their LMS.
* **K–12 Educator:** Helps teachers create lesson materials, assignments, rubrics, and instructional resources, with Learning Commons context for aligning materials to state standards and learning progressions.
* **College Student:** Helps students use course materials and a Study Goal to get source-grounded explanations, guided practice, study plans, quizzes, flashcards, and visual explanations.

The plugins are available in the Plugin Directory but are not installed by default. Note that these plugins are not available to Enterprise accounts. Workspace admins can manage plugin availability and permissions. Learn more in [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

## **Migrate usage limits from weekly to monthly**

Workspace owners can now migrate weekly limits configured in Permissions & roles to monthly limits conveniently. Open Workspace settings → Permissions & roles, select any role, scroll to Weekly limits, choose **Migrate**, and confirm. Starting the migration from any role moves all remaining weekly role-based limits in the workspace and may take several minutes, depending on workspace size.

On August 15, remaining ChatGPT Enterprise workspaces that still use weekly role-based spend limits are scheduled to move automatically to monthly usage limits. [Learn more about managing usage limits and overages.](https://help.openai.com/articles/20001001)

# **July 23, 2026**

## **A more natural ChatGPT Voice experience**

ChatGPT Voice is rolling out to Enterprise and Edu workspaces with two distinct experiences:

* **Voice in Chat**: Have natural, real-time conversations to ask questions, brainstorm, and explore ideas. Powered by GPT-Live, Voice in Chat supports interruptions, follow-up questions, and capabilities such as web search where available. It is available in Desktop Chat and on supported web, iOS, and Android experiences.
* **Voice in Work and Codex**: Starting in the desktop app, ChatGPT Voice can control your computer and coordinate work across multiple agents, active conversations, and projects. Use it to start tasks, check progress, interrupt or redirect work, and receive updates while tasks continue in the background. Available on macOS and Windows, with paired iOS remote access. Standalone Voice in Work and Codex is not available on web or mobile.

For the first two weeks, workspace owners must enable both **Voice** and **Early Model Access** before members can select Live in their Voice settings. Existing Advanced Voice conversations will not automatically switch to Live during this period.

After the early access period, Live becomes the default Voice experience for workspaces with **Voice** enabled. Workspace owners can turn off Voice entirely by disabling **Voice**.

For workspaces on flexible pricing, Voice in Chat uses 5 credits per minute. Voice in Work and Codex uses approximately 6 credits per minute for credit-based Enterprise workspaces. Legacy Enterprise workspaces include one hour of Voice, two hours of Voice Mini, and approximately 45 minutes of Voice in Work and Codex per five-hour window. Tasks delegated through Work or Codex draw from the existing shared usage pool at standard rates.

Learn more about [ChatGPT Voice](/en/articles/20001274) and [Voice pricing for Business, Enterprise, and Edu](/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu).

## ChatGPT Work enablement

For ChatGPT/Edu Enterprise workspaces, Work is enabled by default for members unless a workspace owner or admin turns it off. Workspace settings and role-based access controls continue to determine each member’s access, including for eligible Enterprise workspaces with Enterprise Key Management enabled.

Learn more in [ChatGPT Work and Codex](/en/articles/20001275) and [Managing workspace settings in ChatGPT Enterprise](/en/articles/8411955).

## Model defaults

In Workspace settings → **Models**, workspace owners and admins can set the starting model, reasoning level, speed, and new-chat behavior for Work and Codex. These settings define the starting experience. They do not grant access to unavailable models or replace available-model controls, role-based access, or enforced workspace requirements.

Learn more in [Managing workspace settings in ChatGPT Enterprise](/en/articles/8411955) and [ChatGPT Work and Codex](/en/articles/20001275).

## Usage limits

We’re moving Usage Limits from Workspace settings to the Global Admin Console. Owners and admins can set a workspace default, create group and user overrides, review effective limits, and control requests for more usage. In Usage limits → Workspace, admins can keep the default Monthly period, which resets on the first day of each calendar month in UTC, or choose Aligned to billing cycle when that option is available.

Learn more in [Manage usage limits and overages](/en/articles/20001001) and [Global Admin Console](/en/articles/12289294).

## Usage estimates and group analytics

For eligible workspaces, estimated dollar values may appear next to credits in Analytics, Billing, usage-limit editors, the Cost API, and the Codex analytics API. Estimates use the selected workspace’s overage rate and are for planning. Billing → Invoices remains the source for issued charges. Analytics leaderboards also now include a Groups tab with group-level breakdowns by product, metered item, and model.

Learn more in [Global Admin Console](/en/articles/12289294) and [Workspace analytics](/en/articles/10875114).

# **July 22, 2026**

## **OpenAI Presence and AI phone support updates**

OpenAI Presence is now available in limited general availability as a managed platform for organizations building and operating governed AI agents for high-volume workflows. Presence supports voice or chat deployments with controls for testing, permissions, monitoring, and human escalation. Availability depends on workflow fit, implementation readiness, and delivery capacity. Contact your OpenAI account team to discuss access. Learn more about [OpenAI Presence](/en/articles/20001405).

AI phone support, which uses OpenAI Presence, is no longer experimental. Users in the United States, Canada, and Australia can call without a ChatGPT account for routine product, account, and troubleshooting questions. This automated support channel cannot submit reports or requests, connect users with a live agent, initiate an escalation or account review, or guarantee follow-up. Learn more about [AI phone support](/en/articles/11391933).

# **July 16, 2026**

## **Expanded Admin APIs and analytics**

Admins can now create and manage workspace-scoped Admin keys in the Global Admin Console under Credentials > Admin keys. These keys work with supported ChatGPT and Codex administration APIs for group management, the Spend Controls API, cost reporting, and analytics. Available permissions depend on the admin's workspace role, and Admin keys cannot be used for model inference.

The Global Admin Console now includes up to 120 days of credit and Codex analytics history. Spend Controls and the Usage limits tab remain in ChatGPT and are not part of this Global Admin Console launch. Admins can continue to manage usage limits, including the No limit option where available, from Workspace settings → Usage limits. Learn more in [Manage usage limits and overages in ChatGPT Enterprise and Edu](https://help.openai.com/articles/20001001) and [Global Admin Console](https://help.openai.com/articles/12289294).

## **ChatGPT desktop app experience updates**

We’ve updated the ChatGPT desktop app to make it easier to choose between Chat and Work, find your conversations and Projects, and continue Work across devices. These updates are now live for all plans on macOS and Windows.

### **macOS and Windows**

* **A clearer desktop layout:** A global switcher lets you choose between ChatGPT and Codex. In ChatGPT, choose Chat for quick questions and conversational help, or Work to complete tasks end to end.
* **Unified Recents:** Chat and Work conversations now appear together in Recents, where you can sort, filter, and pin them.
* **Projects in the desktop app:** Your existing ChatGPT Projects now appear in the app. You can start a Chat conversation inside a Project or begin a Work thread using Project context.
* **Continue Work across devices:** Cloud Work conversations now sync across web, mobile, and desktop, so you can start on one surface and continue on another. Local conversations stay on your computer.
* **Codex remains unchanged:** As part of this update, Codex remains a separate view, and its workflows and history are unchanged. Quick Chats remain available for fast conversations.
* **No changes to workspace controls:** Existing workspace access permissions, security settings, governance, and spend controls are unchanged.

# July 15, 2026

## Apps with sync now support EKM workspaces

Apps with sync are now available for ChatGPT Enterprise and Edu workspaces with Enterprise Key Management (EKM) enabled. This update applies to all apps with sync.

To learn more, see [ChatGPT apps with sync](https://help.openai.com/articles/10847137) and [OpenAI Enterprise Key Management (EKM) overview](https://help.openai.com/articles/20000943).

# **July 9, 2026**

## **Introducing ChatGPT Work**

ChatGPT Work is an agent for longer, more involved tasks. It can research and analyze information, work across connected apps and files, and create finished documents, spreadsheets, presentations, reports, and Sites. You can follow its progress, answer questions, change direction, and approve important actions as it works.

Work can also keep projects moving through Scheduled Tasks that run once, repeat on a schedule or trigger, or monitor for changes.

On web and mobile, Work is rolling out to paid plans except Free and Go. Pro, Pro Lite, Enterprise, and Edu users receive access first; Plus and Business users will follow over the coming days. Work is available in all supported regions.

On web and mobile, Enterprise and Edu workspaces have a two-week preview period. Work is off by default during the preview, and admins can opt out before it turns on automatically at the end of the preview.

We’re also replacing the App Directory with the Plugin Directory. Existing app connections are unaffected. Plugins can package skills, apps, and app templates for specific workflows, and are available from ChatGPT on web and desktop, including Work and Codex.

[Learn more about ChatGPT Work and Codex](https://help.openai.com/articles/20001275).

[Learn more about plugins and the new plugin directory.](/en/articles/20001256-plugins-in-chatgpt-and-codex)

## **Skills are now generally available**

Enterprise and Edu users can find skills under Plugins in the sidebar, on the Skills tab in the Plugin Directory.

## **The new ChatGPT desktop app brings Chat, Work, and Codex together**

The new ChatGPT desktop app is available globally for macOS and Windows. It combines Chat for questions and conversation, Work for research and finished deliverables, and Codex for software development in one app.

On desktop, Work can use local files and desktop apps with your permission. The built-in browser lets ChatGPT gather information from websites and work with supported web-based tools and files. Codex also adds inline editing within diffs, pull-request review in the side panel, faster computer use, and support for multiple repositories in one project.

If you already use the Codex app, update it as usual to move to the new ChatGPT desktop app. If you use the previous ChatGPT desktop app, follow the prompt in the app to download the new version. The previous app may remain installed as ChatGPT Classic. ChatGPT Classic continues to receive model updates, bug fixes, security patches, and support for its existing Enterprise capabilities, while new agent features such as Work and Codex are available in the new app.

[Learn more about moving to the new ChatGPT desktop app.](https://help.openai.com/articles/20001276)

## **Introducing ChatGPT Sites in public beta**

ChatGPT Sites lets you turn your work or ideas into an interactive website or lightweight app without leaving ChatGPT. You can create dashboards, project trackers, launch calendars, prototypes, internal portals, and reports, then preview and refine the result with ChatGPT before sharing it.

Business and Enterprise customers already have access to Sites. Starting today, they can also publish Sites publicly and share them with anyone through a URL, expanding Sites beyond people in their workspace.

To create a Site, start in ChatGPT Work on the web or in Work or Codex in the ChatGPT desktop app. Describe what you want to build, add any relevant content, files, data, links, or constraints, and review the private preview before publishing.

In Enterprise workspaces, public publishing is off by default and must be enabled by an admin. Sites is also rolling out in public beta to Pro, Pro Lite, and Edu users, with Plus users following over the coming days. Sites is not available on Free or Go plans. Public publishing and the expanded beta rollout are not available in the EEA, Switzerland, or the United Kingdom at launch.

[Learn more about creating and managing ChatGPT Sites.](https://help.openai.com/articles/20001339)

## **Retiring group chats in ChatGPT**

Beginning July 9, users on web, iOS, and Android will no longer be able to create new group chats, turn existing conversations into group chats, or join a group chat through an invite link.

Existing group chats will remain available and can continue to be used for now. When an existing group chat becomes read-only, users will retain access to the messages, files, and images already shared there. Individual ChatGPT conversations are unaffected.

## **Retiring Atlas**

We’re deprecating Atlas as we bring browser-based agentic capabilities into ChatGPT and Codex. Atlas is scheduled to stop working on August 9, 2026.

We want to make this transition as easy as possible. Before then, move any Atlas data you want to keep. Atlas browser data, including bookmarks, open tabs, and browser history, will not transfer automatically. You can export your cookies and passwords to the ChatGPT desktop app and your bookmarks to Chrome. Be sure to save any important pages or URLs from your open tabs and browser history before August 9.

Your ChatGPT conversation history is separate and will remain available in ChatGPT, subject to your plan, workspace settings, and account access.

We’re building on what we learned from Atlas to bring a more capable browser experience to ChatGPT, including multiple tabs, downloads, improved navigation, and account login support where available. For deeper browser-based agentic work, try the ChatGPT desktop app. For help while browsing in Chrome, try the ChatGPT Chrome extension or sidebar, where available.

You can learn more about moving off Atlas in our [Help Center article](https://help.openai.com/articles/20001371).

## July 6, 2026 ChatGPT for PowerPoint is now generally available

ChatGPT for PowerPoint is now generally available for Enterprise and Edu workspaces. Users can create and revise editable presentations directly in Microsoft PowerPoint, analyze a deck’s narrative and structure, and use approved Skills and apps to work from authorized sources. Advanced edits and template matching may still require review.

Admins can enable the add-in through workspace settings or deploy it through Microsoft 365, including RBAC-based access where applicable. For eligible workspaces, ChatGPT for PowerPoint supports workspace policy enforcement, scoped source access, Compliance API coverage for prompts and responses, EU Inference Residency, and Enterprise Key Management. [Learn more about ChatGPT for PowerPoint](https://help.openai.com/articles/20001242).

## Excel/Sheets and Workspace Agent pricing

ChatGPT for Excel/Sheets tasks now use token-based credit pricing for Enterprise and Edu workspaces. Workspace Agent runs also use token-based credit pricing for Enterprise workspaces. Credit use is based on input tokens, cached input tokens, and output tokens rather than a fixed credit cost.

ChatGPT for PowerPoint remains free for Enterprise customers through August 6, 2026. Charging starts after that date under the same token-based pricing model as ChatGPT for Excel/Sheets. [Learn more in the ChatGPT rate card](https://help.openai.com/articles/11481834).

# **June 26, 2026**

## **Simplified controls in the model picker**

We’re rolling out an updated model picker for ChatGPT Enterprise and Edu on web, iOS, and Android. It makes it easier to choose the balance of speed and reasoning effort that works best for a task without changing the underlying models available to a workspace.

The picker now includes:

* **Instant**
* **Medium**
* **High**
* **Extra High**
* **Pro Standard**
* **Pro Extended**

Medium replaces Thinking Standard, High replaces Thinking Extended, and Extra High replaces Thinking Heavy. Pro Standard and Pro Extended continue to use GPT-5.5 Pro. Thinking Light is no longer available.

All six options are available to Enterprise and Edu workspaces, subject to workspace access settings. **Reasoning Model Access** controls Medium, High, and Extra High. **Pro Model Access** controls Pro Standard and Pro Extended. Options that a member cannot access are hidden from the picker.

The **Redirect Auto Router to Thinking mini** setting is unchanged and continues to apply only to automatic reasoning. On iOS and Android, the picker appears at the top of the conversation. On web, it appears in the message composer.

## **Admin controls for plugins for ChatGPT Enterprise and Edu**

Workspace admins and owners can now manage plugins from **Workspace settings > Plugins**. This page brings plugin discovery and governance into one surface, including search and filters for status, installation policy, roles, category, and catalog. Additionally, workspace owners can enable or disable plugins for their workspace or for select roles from **Workspace settings > Permissions & Roles**.

Admins and owners can set whether plugins are available for members to install or installed by default - for the workspace, or for specific roles. Admins can also view the apps the plugin uses, and manage the plugin from this view. Learn more: [Plugins in Codex](/en/articles/20001256-plugins-in-codex)

# **June 25, 2026**

## **Memory improvements for ChatGPT Enterprise and Edu**

We’re rolling out improved memory for ChatGPT Enterprise and Edu. When memory is enabled, ChatGPT can use relevant context from past chats to keep memory current and make responses more relevant as work changes, rather than relying only on details saved manually.

Users can now:

* Review a memory summary showing information ChatGPT may use to personalize responses.
* View Sources below personalized responses to see relevant context from memories, past chats, and custom instructions.
* Correct memory, delete a referenced chat, mark a source as not relevant, turn memory off, or return to legacy Saved memories.

The memory summary is a high-level view of relevant context and may not include everything ChatGPT can remember or reference.

For ChatGPT Enterprise, the improved experience will begin with an early access period of approximately two weeks. During early access, admins can turn on Use improved memory in Workspace settings. After early access, it will turn on by default for eligible workspaces unless an admin opts out. Admins and users can switch back to legacy Saved memories.

This update does not affect Codex memory. Project-only memory remains contained within each project and does not use memories or conversations from outside that project. These improvements are available at no additional cost.

Learn more about the [research](https://openai.com/index/chatgpt-memory-dreaming/) behind these memory improvements in ChatGPT.

## **Codex Remote GA and DigitalOcean workspaces**

Codex Remote is now generally available to users in ChatGPT Enterprise and Edu workspaces. From the ChatGPT mobile app, users can start or continue work on a connected Mac or Windows host, review progress, and approve actions from their phone. Remote Control now uses authenticated one-to-one QR pairing between each supported mobile device and each host. Connections used since June 8 remain paired; older inactive connections need to pair again. Signing out turns off Remote Control without removing existing pairings.

The new [DigitalOcean Droplet Workspace plugin](https://chatgpt.com/plugins/share/5dc672c7116c44ff92595d48e72df522) is also available to ChatGPT Enterprise and Edu users. It lets Codex provision a DigitalOcean Droplet, configure SSH access, and connect it to the Codex app as a remote workspace. Users should update the ChatGPT mobile app and Codex app to the latest versions before connecting. [Learn more about using Codex with a ChatGPT plan](https://help.openai.com/articles/11369540).

# June 19, 2026

## Slack connector actions and OAuth scope approvals

Enterprise and Edu workspaces can now enable Slack connector actions in ChatGPT. In addition to searching Slack, ChatGPT can take supported actions such as joining a channel, creating a reminder, uploading a file, or updating a user's Slack profile when the connector and relevant actions are enabled.

Admins can review Slack under Apps in ChatGPT and use Action control to manage which actions are available. Some actions may require additional Slack OAuth scopes or approval from a Slack workspace or Enterprise Grid admin. Existing Slack capabilities that do not require the new scopes continue to work if additional scopes are not approved. Learn more in the [ChatGPT Slack app article](https://help.openai.com/articles/12525822).

# June 18, 2026

## Usage limits, Global Admin Console billing and analytics

Enterprise and Edu admins now have new tools for managing credit usage and reviewing billing-related activity. Usage limits in Workspace settings let admins and owners set monthly credit limits by workspace, group, and user, review increase requests, and migrate from existing weekly limits in Permissions & roles.

The Global Admin Console now also includes updated Analytics and Billing areas for eligible workspaces, including credit analytics, Codex and ChatGPT usage views, plan details, credit balances, grant activity, invoices, usage alerts, and overage limit settings. Admins, owners and analytics viewers can view usage data, and export data across different features and dimensions, such as credits used by Codex and ChatGPT, leaderboards for users and agents, and Codex and ChatGPT usage broken down by feature.

Learn more: [Setting usage limits in ChatGPT Enterprise and Edu](/en/articles/20001001-setting-usage-limits-in-chatgpt-enterprise-and-edu), [Global Admin Console](/en/articles/12289294-global-admin-console).

## Record & Replay in Codex

Record & Replay is a new Codex app feature for macOS that lets eligible Enterprise and Edu users demonstrate a workflow once and turn it into a reusable skill. It is designed for stable, repeatable workflows that are easier to show than describe, and the generated skill can later guide Codex through similar tasks with available tools such as Computer Use, browser actions, and installed plugins.

Record & Replay requires Computer Use to be available and enabled, and initial availability excludes the European Union, UK and Switzerland. For managed Codex deployments, disabling Computer Use also disables Record & Replay and related enablement flows. Learn more in the [Record & Replay guide](https://developers.openai.com/codex/record-and-replay).

# June 17, 2026

## Data export for ChatGPT Edu workspaces

Members of ChatGPT Edu workspaces without a data residency configuration can now export their workspace data when a workspace admin enables **Data export**. Members can request an export from **Settings > Data controls**, download the export from the email they receive, and upload the included conversation JSON to a new conversation in a personal ChatGPT account for reference.

Data export is off by default, and the setting applies to all workspace members. [Learn more](https://help.openai.com/articles/20001279).

# **June 11, 2026**

## **Library for Enterprise, Edu, and Healthcare workspaces**

Library is rolling out to Enterprise, Edu, and Healthcare workspaces, giving members a dedicated place to find and reuse files they upload to or create in ChatGPT. Files saved to Library follow workspace retention policies.

Workspace owners can control whether ChatGPT automatically references Library files when responding. Turning off automatic referencing does not remove Library or prevent members from browsing, searching, opening, or attaching files themselves. For Healthcare workspaces, automatic referencing is off by default.

Library-specific Compliance API endpoints are also available for exporting and deleting Library files. Library does not introduce new external sharing or multiplayer collaboration.

[Learn more about File storage and Library in ChatGPT](/en/articles/20001052-library-for-chatgpt).

## **Global admin console updates**

Cloud Console now includes [external app access](/en/articles/12289294-global-admin-console#external-access) controls for Sign in with ChatGPT. Admins can turn external application access on or off for the organization, require applications to be approved before members can use them, and approve or disable individual applications.

## **Codex updates**

We’ve shipped a few Codex updates, including:

* Computer Use for Windows for Enterprise plans. See [Computer Use](https://developers.openai.com/codex/app/computer-use), [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration), and the [configuration reference](https://developers.openai.com/codex/config-reference).
* [Developer mode](https://developers.openai.com/codex/app/browser#developer-mode) for Browser use in Chrome and the Codex in-app browser, where available. Developer mode lets Codex use controlled Chrome DevTools Protocol (CDP) access for performance profiling and deeper debugging of network traffic, console output, runtime errors, DOM state, and applied styles. The feature is turned off by default at the user level, and can be enabled from Codex app settings. Admins and owners can turn off the feature for their workspace from [Codex cloud settings](https://chatgpt.com/codex/cloud/settings/) by accessing the **Policies & Configurations** pane. [Learn more](/en/articles/11369540-using-codex-with-your-chatgpt-plan#in-app-browser-developer-mode).

The release also adds /init in the app composer for generating an AGENTS.md scaffold, support for configuring per-app access controls for Computer Use on Windows, clearer usage-limit errors with workspace guidance and reset timing when available, and a new **Unread chats** section in the command menu. [Learn more](https://developers.openai.com/codex/changelog).

# June 8, 2026

## App permissions for connected apps

Workspace admins can now use App permissions, where available, to choose when ChatGPT asks members before using connected apps. Admins can set a workspace-wide default and choose a different permission for individual apps, with options such as **Always ask**, **Any changes**, and **Important actions**.

Important actions is the default and allows ChatGPT to read from apps automatically while asking before actions that may have a meaningful effect outside ChatGPT, expose sensitive information, or be difficult to undo. App permissions replace the previous Action consent setting where available, while app access, RBAC, and Action control remain separate admin controls.

Learn more: [Apps in ChatGPT](/en/articles/11487775); [Admin Controls, Security, and Compliance in apps](/en/articles/11509118).

# June 5, 2026

## Plugin sharing for Enterprise workspaces

Plugin sharing is now available by default for eligible ChatGPT Enterprise workspaces in Codex. Users can share local plugins with their workspace so teammates can install and use shared plugins from the Codex plugin directory.

Workspace admins can disable plugin sharing in **requirements.toml** using MDM or cloud-managed configuration. Learn more: [Share a local plugin with your workspace](https://developers.openai.com/codex/plugins/build#share-a-local-plugin-with-your-workspace).

# June 2, 2026

## Build and deploy internal workspace apps with Sites

ChatGPT Sites is now available in preview for eligible ChatGPT Enterprise and Edu workspaces. Available as a plugin, users can ask Codex to create, iterate on, and deploy lightweight full-stack JavaScript/TypeScript web apps with hosted site URLs, Sign in with ChatGPT access, and data/file storage, while keeping access workspace-internal.

ChatGPT Sites is default off for Enterprise/Edu workspaces - admins and owners can manage enablement and access through workspace settings and RBAC. ChatGPT Sites can be enabled from **Workspace settings > Permissions & Roles.** Admins and owners can disable published sites from \*\*Workspace settings > Sites.

\*\*For build, deployment, storage, access, and limitation details, see the [Codex Sites developer guide](https://developers.openai.com/codex/sites).

## Role-specific plugins in Codex

Role-specific plugins are rolling out in Codex for supported ChatGPT Enterprise workspaces. This first set includes Sales, Data Analytics, Product Design, Creative Production, Investment Banking, and Public Equity Investing. These plugins package role-specific skills, app integrations, starter prompts, and workflow guidance so teams can use Codex for sales prep, analytics and dashboards, prototypes, creative assets, and financial research.

This launch also adds 66 single-app plugins that expand the integrations available in Codex, including tools such as Databricks, Salesforce, Hex, and Clay. Users can add available plugins from the Codex plugin directory, and Codex can help them complete setup. Workspace admins control the underlying app permissions in workspace settings. For some workflows, such as using Databricks or Snowflake in Data Analytics, admins may need to complete connector setup before users can use the plugin.

Learn more: [Plugins in Codex](https://help.openai.com/articles/20001256).

## Active account session controls

We’re rolling out **Active sessions**, a new security feature in ChatGPT that helps users review sessions associated with their account and sign out of sessions they don’t recognize. **Availability:** This feature is not available for accounts linked to an organization’s SSO sign-in, including SAML or OIDC. This can apply even if the organization does not require SSO for every sign-in, or if the user signed in another way for their current session.

Users with access can now:

* Review first-party OpenAI sessions from **Settings** > **Security** > **Active sessions**, with available details such as device, app, approximate location, sign-in time, trusted-device status, and whether it is the current session.
* Log out of individual sessions or all sessions from **Active sessions**

Active sessions shows sessions known through session management, including ChatGPT, Codex, and API Platform sessions where available. It does not manage third-party app sessions, connected apps, Sign in with ChatGPT sessions used only for third-party services, or Codex CLI sessions.

Learn more: [Managing active sessions in ChatGPT](https://help.openai.com/articles/20001257)

# May 29, 2026

## Codex updates: Computer use and remote control for Windows, GitHub Enterprise app template support

Codex now supports Computer Use on Windows in the Codex app. Users with Codex access can use Computer Use to let Codex see, click, and type in Windows applications. With remote control, users can also continue Windows workflows from ChatGPT on iOS or Android, or from Codex on Mac, to check progress, respond to prompts, and steer while away from the desk while the Windows machine remains the host for project files, shell, app server, and local context.

Windows Computer Use and remote control are disabled for Enterprise users by default. To enable, contact your OpenAI account representative to be enrolled into early access.

For customer-hosted GitHub Enterprise Server repositories, workspace admins can set up and publish a GitHub Enterprise app from the ChatGPT app template so Codex can use the workspace-specific connector for Codex Web, Code Review, and Security Review.

Learn more: [Computer Use](https://developers.openai.com/codex/app/computer-use), [Remote control](https://developers.openai.com/codex/remote-connections), [Set up the GitHub Enterprise app template in ChatGPT](https://help.openai.com/articles/20001248).

# May 28, 2026

## **New controls and capabilities for ChatGPT workspace agents**

We’re rolling out new model, admin, app access, and response capabilities for ChatGPT workspace agents in Enterprise and Edu.

Workspace agents now support:

* **GPT-5.5 and reasoning effort controls:** When building an agent, creators can choose GPT-5.5 and set the reasoning effort the agent uses. We’ve also improved response speed across agents.
* **Role-based publishing permissions:** Workspace admins can control which roles can publish agents to the shared workspace directory.
* **Guided agent setup:** ChatGPT now asks setup questions to help users create useful agents more quickly.
* **Speech output:** Agents can now create audio files as part of their responses.
* **Smarter Slack thread replies:** Agents used in Slack can respond to relevant follow-up messages in a thread after the initial mention. Creators can choose whether an agent responds to relevant thread messages or only when it is mentioned.

## App templates for GitHub Enterprise, Snowflake, and Databricks

Workspace admins and owners on Enterprise and Edu plans can now use ChatGPT app templates to create workspace-specific apps for GitHub Enterprise, Snowflake, and Databricks. App templates provide a guided setup flow for provider-specific configuration such as OAuth credentials, callback URLs, webhook details, managed MCP server URLs, and workspace access controls before admins publish the app to members.

Use the new setup guides to understand the general app-template flow and the provider-specific steps for each template: [ChatGPT app templates](https://help.openai.com/articles/20001247), [GitHub Enterprise app template](https://help.openai.com/articles/20001248), [Snowflake app template](https://help.openai.com/articles/20001249), and [Databricks app template](https://help.openai.com/articles/20001250).

After publishing, admins can manage the resulting app from Workspace settings > Apps > Enabled, including role access, action controls, and action confirmation.

# **May 22, 2026**

## **Workspace agents are now generally available in ChatGPT Business, Enterprise, and Edu.**

Workspace agents help teams get more done together across tools. They can own entire workflows on their own, follow team processes, and be shared across your team so people can build once and use together.

We’ve also added new admin controls and visibility:

* Agent builders can set safeguards on which actions agents can take for each app enabled in their workspace.
* Business, Enterprise, and Edu admins can view workspace agent activity and usage in the

  [admin console](https://admin.openai.com)

  .

We’ve extended the free period for workspace agents until July 6, 2026. Credit-based pricing will begin on that date. (edited)

# May 21, 2026

## Codex updates: goal mode, browser improvements, remote locked use, admin analytics, and plugin sharing status

Codex now gives Enterprise and Edu users more ways to work toward longer-running goals and iterate in the browser, while eligible admins get updated usage analytics:

* [Appshots](https://developers.openai.com/codex/appshots) in the macOS app let users attach an app window to a Codex thread with a hotkey, including a screenshot and available text. Appshots are available for ChatGPT Edu accounts today, support for ChatGPT Enterprise accounts coming soon.
* [Goal mode](https://developers.openai.com/codex/prompting#goal-mode) is generally available across the Codex app, IDE extension, and CLI, so users can define an outcome and success criteria and let Codex keep working toward it.
* [In-app browser annotations](https://developers.openai.com/codex/app/browser#styling-feedback) support more precise styling feedback for browser-based and frontend work.
* [Locked computer use](https://developers.openai.com/codex/app/computer-use#locked-use) lets users keep Codex working remotely and securely after the Mac locks, subject to existing regional constraints. Admins and owners can turn this feature off by setting **remote\_computer\_use = false** in the [Policies & Configurations](https://chatgpt.com/codex/cloud/settings/policies) setting in Codex cloud. Review [configuration reference](https://developers.openai.com/codex/config-reference#requirementstoml) for more details.
* [Browser-use improvements](https://developers.openai.com/codex/app/browser) add advanced annotation mode, faster asset extraction, read-only JavaScript context, tab grouping usability, less Chrome extension tab clutter, and reliability improvements.
* The [global admin console](/en/articles/12289294-global-admin-console) now includes Codex analytics for Enterprise admins, with active users, credits and tokens, threads and turns, user leaderboards, plugin usage, accepted lines of code, model usage, and a console-aligned UI.
* [Plugin sharing](https://developers.openai.com/codex/plugins/build#share-a-local-plugin-with-your-workspace) lets teams share locally built plugins with workspace members from the Codex app. Plugin sharing is **disabled by default for ChatGPT Enterprise** - reach out to your OpenAI account contact for details on how to enable the feature. For ChatGPT Edu accounts, plugin sharing is enabled by default.

Learn more: [Goal mode](https://developers.openai.com/codex/prompting#goal-mode), [locked computer use](https://developers.openai.com/codex/app/computer-use#locked-use), [in-app browser annotations](https://developers.openai.com/codex/app/browser#styling-feedback), and [plugin sharing](https://developers.openai.com/codex/plugins/build#share-a-local-plugin-with-your-workspace).

## **Workspace agents are now generally available in ChatGPT Business, Enterprise, and Edu.**

Workspace agents help teams get more done together across tools. They can own entire workflows on their own, follow team processes, and be shared across your team so people can build once and use together.

We’ve also added new admin controls and visibility:

* Agent builders can set safeguards on which actions agents can take for each app enabled in their workspace.
* Business, Enterprise, and Edu admins can view workspace agent activity and usage in the

[admin console](https://admin.openai.com).

We’ve extended the free period for workspace agents until July 6, 2026. Credit-based pricing will begin on that date.

# May 18, 2026

## Beta label removed from the Apps Directory and app creation flow

We removed the Beta label from the Apps Directory in ChatGPT on web and desktop, and from the new app creation flow.

This is a labeling update only. It does not change the Apps Directory experience, app creation workflows, dev mode capabilities, or the existing elevated-risk guidance for dev mode.

# May 15, 2026

## Microsoft Teams app with admin-managed sync in ChatGPT

The [Microsoft Teams app with admin-managed sync](/en/articles/20001234) is now available for eligible ChatGPT Enterprise and Edu workspaces. Owners and admins can connect Microsoft Teams once for the workspace so ChatGPT can reference supported Teams messages and conversation metadata that members already have permission to access.

Owners and admins can enable sync from Workspace settings → Apps, choose which Teams content to include with the scope picker and an optional Microsoft Purview sensitivity label filter, then deploy it through Deploy to your team. The synced experience is read only, may take time to fully populate after setup, and remains separate from the regular self-service Microsoft Teams app.

# May 14, 2026

## Codex remote access and access tokens for automation

Codex now supports remote access from the ChatGPT mobile app, letting users stay connected to longer-running work, answer questions, redirect execution, approve actions, review outputs, and switch between connected hosts while Codex continues operating in the underlying Mac host or connected remote environment. The mobile experience surfaces live state from that environment, including project context, approvals, screenshots, terminal output, diffs, and test results. Enterprise workspaces can also use Codex access tokens for trusted, non-interactive local workflows that need ChatGPT workspace identity and enterprise controls without a browser sign-in.

To try it, update both the ChatGPT mobile app and the Codex app on macOS. Mobile setup can require workspace-enabled Remote Control access and may involve SSO, multi-factor authentication, or passkey steps.

Additionally, access tokens are available for ChatGPT Enterprise workspaces, with admins able to manage workspace-level availability, members using permitted roles to create their own tokens, and governance surfaces reflecting access token activity where available.

Remote control is turned off by default, and Admins/owners can enable from Workspace settings.

Learn more in [Remote connections](https://developers.openai.com/codex/remote-connections), [Access tokens](https://developers.openai.com/codex/enterprise/access-tokens), [Admin setup](https://developers.openai.com/codex/enterprise/admin-setup), and [Governance](https://developers.openai.com/codex/enterprise/governance).

# May 7, 2026

## ChatGPT Workspace Agents now support Enterprise workspaces with EKM

ChatGPT workspace agents are now available to eligible ChatGPT Enterprise workspaces with Enterprise Key Management (EKM).

Workspace agents let organizations build and use agents for repeatable tasks and business workflows across connected apps, including ChatGPT and Slack. Agents can be created from templates or from scratch, previewed before publishing, shared within a workspace, and run on a schedule.

Eligible EKM workspaces can now create and use workspace agents, connect supported tools and apps, add skills, files, and custom MCP servers, schedule recurring runs, use agents in connected Slack channels, and view version history and analytics.

Workspace agents remain off by default. Admins can enable agent building, publishing, and Slack usage for eligible workspaces through admin controls.

# May 6, 2026

## ChatGPT for Intune for iOS and iPadOS

We’ve added ChatGPT for Intune to the Apple App Store. ChatGPT for Intune is a separate iOS app for ChatGPT Enterprise organizations that manage mobile access management through Microsoft Intune and Microsoft Entra. The app lets IT teams apply Microsoft app protection policies and Conditional Access policies to the ChatGPT mobile experience on iOS and iPadOS.

ChatGPT for Intune is available for Enterprise accounts only and requires organizational onboarding with OpenAI before use. Enterprise owners and admins should reach out to their OpenAI account director to start onboarding, then configure the required Microsoft Entra and Intune settings before rollout.

Once onboarded, users can download the app from the Apple App Store and sign in with enterprise Microsoft authentication. Learn more in [Setting up ChatGPT for Intune](/en/articles/20001232-setting-up-chatgpt-for-intune).

## **Easier model selection in ChatGPT**

We’re making it easier to choose the right model before you send a message. Model selection now appears in the composer, so you can find and switch models from the same place where you write your prompt.

We’re also moving thinking effort controls into the model picker. When you choose a Thinking or Pro model, you can select the level of thinking effort directly from the model picker.

## Analytics and Agents in the global admin console

The global admin console now includes new Analytics and Agents areas. Analytics gives admins a consolidated view of adoption and usage, with trend views for active users and message activity plus drilldowns for GPTs, projects, skills, users, tool interactions, connector interactions, and workspace health.

Agents gives admins a consolidated view of workspace agents across the organization. Admins can open an agent to review details such as Agent ID, recent activity, connected apps, memory files, schedules, and agent analytics such as unique users and runs over time, or move into Builder to edit it. Workspace Owners can access these views from the global admin console. [Learn more](/en/articles/12289294-global-admin-console).

# May 5, 2026

## ChatGPT for Excel and Google Sheets

ChatGPT for Excel and Google Sheets is now available globally for Enterprise, Edu, and K-12 workspaces, bringing a spreadsheet-native ChatGPT sidebar to Excel and Google Sheets for building, updating, explaining, and reviewing multi-tab spreadsheets. It supports Skills and apps where available so spreadsheet work can be grounded in approved files, systems, and data sources.

Enterprise, Edu, and K-12 customers have a free preview through June 2, 2026; after that, usage follows credits and usage terms. The experience supports workspace controls including RBAC, data and inference residency where available, Enterprise Key Management, and Compliance API coverage. Admins can enable ChatGPT for Excel and Sheets from workspace settings. [Learn more](https://help.openai.com/articles/20001063).

# **April 30, 2026**

## **Updates to admin-managed SharePoint sync**

We are migrating the ChatGPT SharePoint app [scope requests](https://help.openai.com/articles/12143177-sharepoint-app-in-chatgpt?#permission-requested-scope) from **delegated scopes to** Microsoft **application scopes,** for the admin-managed "**Deploy to your team**" sync option. The migration helps ChatGPT sync selected SharePoint content and evaluate SharePoint permissions, including legacy SharePoint site group membership, without depending only on the files visible to the admin who completed setup. Additionally, admins and owners can configure **Microsoft Purview sensitivity** labels from app settings.

These new scopes will need to be approved by a Microsoft Entra admin for the new feature set to be active. Admins and owners can conveniently re-authenticate the SharePoint app by navigating to **Workspace Settings > Apps,** and locating the prompt "Reconnect SharePoint for better syncing" at the top of the view, or by searching for the SharePoint app and clicking the 'Re-auth required' button to obtain the new feature set. This prevents the need to disconnect and reconnect, which will cause re-syncing of the index.

Learn more about the [SharePoint app in ChatGPT](/en/articles/12143177-sharepoint-app-in-chatgpt), and review the [FAQ](/en/articles/12143177-sharepoint-app-in-chatgpt#faq-admin-managed-app-with-sync) for the admin-managed sync option for more information.

# April 22, 2026

## **ChatGPT Workspace Agents for Enterprise and Business**

ChatGPT workspace agents are rolling out gradually over the next few weeks to ChatGPT Business and Enterprise workspaces.

Workspace Agents let organizations build and use agents for repeatable tasks and automate business workflows leveraging all your connected apps & can run in ChatGPT and/or Slack. Workspace agents can be created, previewed before publishing, shared within a workspace, and run on a schedule.

Eligible workspaces can now:

* Create agents from templates or build from scratch.
* Connect agents to tools and apps such as Google Drive, Google Calendar, Slack, and SharePoint.
* Add skills, files, and custom MCP servers.
* Share agents privately, by link, or in the workspace directory.
* Schedule recurring runs in ChatGPT.
* Use agents in connected Slack channels.
* View version history and analytics for agents.

Workspace admins can also manage access to agent building, publishing, and Slack usage through admin controls. ChatGPT workspace agents are off by default at launch, and admins can enable them for eligible workspaces.

**Note:** ChatGPT workspace agents are not available for ChatGPT Enterprise workspaces with EKM at launch.

## Data Residency for apps with sync in Japan

All apps with sync now support in-region data residency in Japan for ChatGPT Enterprise/Edu workspaces. Previously, in Japan, data residency for apps with sync was limited to Google Drive and GitHub. This launch extends Japan data residency support to all sync connectors. Learn more about [data residency](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).

# **April 9, 2026**

## **GPT-5.3 Instant mini in ChatGPT**

Today, we’re releasing **GPT-5.3 Instant Mini** in ChatGPT. It replaces GPT-5 Instant Mini as the fallback model users reach after hitting their rate limits for GPT-5.3 Instant. Because it serves as a fallback, it won’t appear in the model picker.

Compared with GPT-5 Instant Mini, GPT-5.3 Instant Mini feels more natural in conversation, with stronger writing and contextual awareness throughout chats. It outperforms GPT-5 Instant Mini across a range of use cases.

## **Control SCIM group discoverability in sharing flows**

Workspace owners can now control whether SCIM-managed groups are discoverable in sharing flows like projects and GPTs. A new setting **Discoverable by workspace users** is available under **Identity & provisioning > Directory Sync (SCIM)** and is enabled by default to preserve existing behavior.

When this setting is **disabled**:

* SCIM-managed groups will **no longer appear** in sharing flows.
* If a project or GPT is already shared with one or more SCIM-managed groups, those groups will be removed from the sharing list the next time the project or GPT is updated.

This setting can help reduce accidental oversharing and ensures group-based sharing remains aligned with centrally managed access policies.

For more information, see: [SCIM Integration FAQ](https://help.openai.com/articles/10011769).

# April 8, 2026

## Outlook shared mailbox and shared calendar actions

The Outlook Email and Calendar apps for ChatGPT now support more delegated Outlook workflows for teams. With the right Microsoft permissions, users can ask ChatGPT to list and read shared mailbox messages, browse shared mailbox folders, mark shared mail read or unread, move shared messages, and send plain-text email from or on behalf of a shared mailbox. ChatGPT can also create, update, respond to, cancel, delete, and attach small files to events on shared Outlook calendars.

Workspace owners and admins should review Microsoft Entra permissions, [RBAC](/en/articles/11750701-rbac) access, and the Outlook app's action controls before enabling newly added actions. Users who previously connected Outlook may need to reconnect after the workspace enables the new actions; Microsoft Entra approval may also be required. [Learn more](/en/articles/12512241).

# April 2, 2026

## New Codex seats in ChatGPT Enterprise

We're introducing a new seat type for ChatGPT Enterprise: a [Codex seat](/en/articles/8265053-what-is-chatgpt-enterprise#overview) based on [flexible pricing](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans). Codex seats provide access to Codex only - they do not include ChatGPT workspace access, and have no fixed cost per user per month. Using Codex requires [workspace credits](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans#how-do-credits-work-in-chatgpt-plans), while standard ChatGPT seats continue to include ChatGPT and Codex with baseline access and optional flexible pricing for usage beyond included [rate limits](https://developers.openai.com/codex/pricing#frequently-asked-questions).

Read more about the Codex seat and seat-type behavior [here](/en/articles/8265053-what-is-chatgpt-enterprise#overview). For member management, SCIM provisioning, and how to change a member's seat type, see [Managing members, seat types, roles and access in ChatGPT Enterprise](/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise#change-member-seat-types).

We've also updated the [Codex Rate Card](/en/articles/20001106-codex-rate-card). New ChatGPT Enterprise workspaces use [token-based rates](/en/articles/20001106-codex-rate-card#codex-rate-card-token-based-pricing), while existing Enterprise and new/existing [ChatGPT Edu](/en/articles/9377311), [ChatGPT for Teachers](/en/articles/12844995), and [ChatGPT for Healthcare](/en/articles/20001046) workspaces continue on the [legacy message-based rates](/en/articles/20001106-codex-rate-card#legacy-rate-card) until migration. If you have questions about the new rates or migration timing, contact your OpenAI representative.

# March 27, 2026

## Updated Box, Notion, Linear, and Dropbox apps

We're rolling out updated [Box](/en/articles/12368225-box-app-with-sync), [Notion](/en/articles/12532955-notion-app-with-sync), [Linear](/en/articles/12526595-linear-app-with-sync), and [Dropbox](/en/articles/12364275-dropbox-app-with-sync) apps in ChatGPT Enterprise and Edu. These updates add new app actions, including new write capabilities where supported, and bring the latest app experience into ChatGPT.

The new apps are disabled by default, and workspace admins/owners can review the app as well as the app's actions in **Workspace settings > Apps** to enable those aligned to their workspace needs. New actions (such as write actions) may involve updated scopes - admins/owners should check the [Box](/en/articles/12368225-box-app-with-sync), [Notion](/en/articles/12532955-notion-app-with-sync), [Linear](/en/articles/12526595-linear-app-with-sync), and [Dropbox](/en/articles/12364275-dropbox-app-with-sync) app pages for details, and authorize any scopes required. New users may not be able to connect these apps until the scope authorizations are met, or actions are enabled/disabled in alignment with authorized scopes.

Members who previously connected these apps may need to reconnect the app after admin review to start using the updated experience.

## Add sources to your projects from anywhere

Projects now make it easier to build a living knowledge base by adding sources from apps, conversations, and quick text inputs. You can paste a link to a Slack channel or a Google Drive file or folder to add it directly as a project source, save useful ChatGPT responses into your project so strong outputs become reusable knowledge, and paste notes, briefs, or reference material directly into a project.

In Enterprise and Edu workspaces, app access follows workspace controls. Admins and owners can manage app availability in Workspace settings > Apps, and can use [RBAC](/en/articles/11750701-rbac) to assign app access to specific roles. Learn more about [projects in ChatGPT](/en/articles/10169521-using-projects-in-chatgpt).

# **March 26, 2026**

## **Plugins in Codex**

Codex now includes a curated plugins directory that lets users discover, install, and use packaged workflows built from apps and skills directly in Codex. Plugins are installable bundles for reusable Codex workflows, making it easier to share the same setup across projects or teams. Plugins can package skills, optional app integrations, and MCP server configurations in a single place. [Learn more.](https://developers.openai.com/codex/plugins)

Plugin access follows workspace app controls. Enterprise and Edu admins can manage enabled apps in Workspace settings → Apps, and can use [RBAC](/en/articles/11750701-rbac) to assign app access to specific roles.

# **March 25, 2026**

## **Google Drive connector unification**

Google’s file connectors in ChatGPT are now unified under Google Drive, providing a single app experience for interacting with your Google Docs, Sheets and Slides on Google Drive.

The new Google Drive actions are off by default for Enterprise/Edu workspaces. Admins/owners can review and manage actions from **Workspace settings > Apps.** Locate the Google Drive entry and click **Manage actions.**

Existing users of Google Drive, Docs, Sheets and Slides apps are unaffected - previously connected apps continue to work. After the new actions are enabled by admins/owners, existing users may reconnect the Google Drive app to start using the new actions within ChatGPT. New users can connect only to the Google Drive app to use Docs, Sheets and Slides actions, without needing to connect the separate apps.

Google Workspace admins may need to re-authorize Google scopes corresponding to app actions - otherwise, users may hit connection errors when trying to connect. [Read more.](/en/articles/10408842-google-app-for-chatgpt-data-controls-faq)

# March 20, 2026

## **Impact survey updates in workspace analytics**

### ChatGPT Edu

Impact surveys are now available for ChatGPT Edu in addition to Enterprise, with an Edu-specific question set.

### Export

Impact survey results can now be exported.

### Admin-created surveys

Workspace owners can now launch an **Admin-created** survey from the **Impact** tab. These surveys let workspace owners trigger an impact survey for their workspace on demand, unlike the regularly scheduled OpenAI-created surveys.

Note that custom question and answer sets are not supported at this time.

### Survey start date change

OpenAI-created impact surveys will now begin on or after **March 31, 2026** instead of the previously communicated March 26, 2026.

To learn more about impact surveys, see: [Managing impact surveys in workspace analytics](https://help.openai.com/articles/20001149).

# March 19, 2026

## Legacy deep research mode deprecation notice

The legacy deep research mode will be removed on Thursday, March 26, 2026. This change only affects the legacy mode; the current deep research experience will remain unchanged.

Historical conversations and results will remain accessible.

To learn more about deep research, see: [Deep research in ChatGPT](https://help.openai.com/articles/10500283).

# **March 18, 2026**

## **GPT-5.4 mini in ChatGPT**

We’re rolling out GPT-5.4 mini in ChatGPT. GPT-5.4 mini is available to Free and Go users via the “Thinking” feature in the + menu. For all other users, GPT-5.4 mini is available as a rate limit fallback for GPT-5.4 Thinking.

For Plus, Pro, and other paid users, GPT-5.4 mini will be used as a fallback for GPT-5.4 Thinking when rate limits are reached, helping with continued access to reasoning capabilities during high usage. Enterprise customers will retain the option to default Auto routing to GPT-5.4 mini, if preferred.

GPT-5.4 mini will not appear as a selectable model in the model picker. Learn more in our [blog post](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/).

# **March 17, 2026**

## **Updates to the model picker in ChatGPT**

We’ve simplified the model picker to make it easier to choose the right level of reasoning.

Users on Plus, Pro, Business, Enterprise, and Edu accounts will see a set of model options depending on their plan, including:

* **Instant** – fast responses for everyday questions
* **Thinking** – deeper reasoning for more complex tasks
* **Pro** – the most advanced reasoning models

The Auto functionality can be accessed by clicking **Configure** in the model picker menu and choosing "Auto-switch to thinking.” This setting will automatically be on if your last chat was set to Auto.

### **Configure more advanced settings**

If you want more control, click **Configure** to:

* Turn **automatic switching** between Instant and Thinking on or off
* Access **legacy models**
* Set **thinking effort** when Thinking or Pro is selected

We’ve also simplified the **retry menu**, making it easier to regenerate responses with Thinking or Pro models by clicking on the three dots underneath the response.

# **March 13, 2026**

## **Write actions for Google and Microsoft Apps in ChatGPT**

We've updated scopes and actions in Google and Microsoft apps in ChatGPT to include support for write actions. You can now use apps like Microsoft Outlook email to draft emails for you, Google Docs and Sheets to create spreadsheets or docs, or set up meetings using the respective calendar apps.

Write actions remain disabled by default until workspace admins enable them in **Settings > Apps > Manage actions** per app. For Microsoft apps, some customers may also need Microsoft Entra admin approval for updated scopes before new users can connect successfully. Learn more in the Help Center: [Apps in ChatGPT](/en/articles/11487775), [Microsoft Outlook app for ChatGPT](/en/articles/12512241-outlook-email-and-calendar-app-for-chatgpt), [Microsoft Calendar app for ChatGPT](/en/articles/12512241-outlook-email-and-calendar-app-for-chatgpt), and [Microsoft Teams app for ChatGPT](/en/articles/12552368-microsoft-teams-app-for-chatgpt).

# March 12, 2026

## Workspace analytics

A refreshed analytics experience, entitled **Workspace analytics**, is now available for ChatGPT Enterprise and Edu. Workspace analytics, replacing **User analytics**, introduces workspace-level analytics to help admins understand adoption, engagement, and how teams use ChatGPT across their organization.

Key highlights:

* **Refreshed analytics experience:** Updated visuals and navigation, including new tabs that surface insights on how teams use ChatGPT and the outcomes it delivers.
* **Benchmark comparisons**: Compare adoption and engagement metrics against an industry median.
* **Impact**: Understand self-reported outcomes such as productivity, time saved, work quality, and work satisfaction through surveys sent to users.

* **Task insights**: View aggregated patterns of work in ChatGPT, including task categories and conversation topics.

Additionally, a new user type, *analytics viewer*, allows designated workspace members to view workspace analytics alongside workspace owners and admins.

***Note:***\* Task Insights and user-distributed impact surveys are \****enabled by default.***\* Workspace admins and owners may opt out of one or both of these features. Workspaces \****will have approximately 2 weeks*** \*from initial release to opt out before surveys may be sent to users.

*For more information and an overview of the Workspace analytics*\* feature, see: [Workspace analytics for ChatGPT Enterprise and Edu](https://help.openai.com/articles/10875114).

For guidance on how to operationalize these insights (playbooks, enablement motions, champion programs), see our Academy guide: [ChatGPT Enterprise workspace analytics guide](https://academy.openai.com/public/clubs/admins-6o6xf/resources/chatgpt-enterprise-user-analytics-guide).

# **March 11, 2026**

## **Updated scopes for Microsoft apps**

We updated the scopes requested by the [Outlook Calendar](/en/articles/12512241), [Outlook Email](/en/articles/12512241), [Microsoft SharePoint](/en/articles/12143177) and [Microsoft Teams](/en/articles/12552368) apps to support additional actions. Microsoft Entra admins will need to review and approve the updated app scopes before new users connect - users may hit connection issues, otherwise.

Note that the new scopes do not automatically make available (or enable) new actions for these apps (including any write actions). Workspace admins and owners will need to review available app actions by locating the app entry in **Workspace settings > Apps**, and then clicking **Manage actions**.

New actions, when made available, are disabled by default - admins/owners can review and then enable actions if appropriate for their workspace.

## Retiring GPT-5.1 models

As of March 11, 2026, GPT-5.1 models are no longer available in ChatGPT.

This applies to GPT-5.1 Instant, GPT-5.1 Thinking, and GPT-5.1 Pro. Existing conversations that used GPT-5.1 will automatically continue on the corresponding current model: GPT-5.3 Instant, GPT-5.4 Thinking, or GPT-5.4 Pro.

# **March 6, 2026**

## **Skills beta for ChatGPT Enterprise and Edu**

We’re introducing **Skills**, a new way for teams to turn proven workflows into reusable instructions that ChatGPT can apply automatically. Skills define when to use a workflow, the steps to follow, and the format of the result—so teams get consistent outputs without repeating the same instructions in every prompt.

Skills can be shared across a workspace and automatically applied in conversation when relevant. For Enterprise and Edu, admins can manage who can create, share, and install skills using role-based controls. Skills are currently in beta and are off by default for Enterprise and Edu workspaces. Admins can enable them at any time.

# **March 4, 2026**

## **Codex app on Windows**

Codex app is now available on Windows for ChatGPT Enterprise and Edu workspaces that include Codex. Members can run multiple Codex agents in parallel from a Windows desktop surface, with isolated worktrees and reviewable diffs that stay interoperable with Codex in the CLI and IDE.

Admins do not need to set up separate app-specific permissions for the app. Codex Local permissions continue to govern local usage, and Codex Cloud permissions govern delegated cloud tasks from the app and other cloud-based Codex surfaces. Learn more: [Using Codex with your ChatGPT plan](/en/articles/11369540-using-codex-with-your-chatgpt-plan).

# **March 3, 2026**

## **GPT-5.3 Instant Update**

GPT‑5.3 Instant delivers more accurate answers, richer and better-contextualized results when searching the web, and reduces unnecessary dead ends, caveats, and overly declarative phrasing that can interrupt the flow of conversation. GPT-5.3 Instant is default off for ChatGPT Enterprise and Edu workspaces - Admins can enable it via the **Early Model Access toggle** in workspace settings in the “Models” section.

This update focuses on the parts of the ChatGPT experience people feel every day: tone, relevance, and conversational flow. These are nuanced problems that don’t always show up in benchmarks, but shape whether ChatGPT feels helpful or frustrating. GPT‑5.3 Instant directly reflects user feedback in these areas.

# **February 27, 2026**

## **ChatGPT Web and Android updates: Edit image prompts, share faster, and smoother conversations**

### **Web**

* **Edit messages with images.** You can now edit messages that include image attachments, so you don’t have to start over to adjust your prompt or regenerate results.
* **Open search results in a new tab.** Cmd+click in the search panel now opens results in a new tab, making it easier to explore without losing your place.
* **Faster sharing.** Sharing chats is now easier and faster, with a quicker-loading share menu.
* **Export visuals from Code Blocks.** Flowcharts, diagrams, and data visualizations created in Code Blocks can now be exported as images for easy reuse.

### **Android**

* **Automatic scroll to latest message.** Existing conversations now automatically scroll to the bottom, so you can jump right back in.
* **Faster sidebar actions.** Sidebar interactions, such as renaming chats, are now faster and more responsive.
* **Improved dictation visuals.** Dictation now has a clearer, more streamlined interface that keeps your text visible and updates as you speak.
* **Keyboard opens automatically when attaching files.** The keyboard now opens automatically after you attach a file, helping you continue your message seamlessly.

### **Bug fixes**

* Fixed increased message streaming errors in GPT-5.2 Thinking
* Fixed a flicker affecting the Voice Mode button when opening a conversation
* Sidebar actions on mobile web no longer stick while scrolling

# **February 23, 2026**

## Projects: Chats and Sources tabs

We’re updating projects with a new tabbed layout so you can easily access sources alongside your chats:

* Projects now have two tabs: Chats and Sources
* Project files have moved from Project settings to the Sources tab.
* Files in Sources can now be sorted by Newest, Oldest, or Alphabetical.

# February 20, 2026

## **Data Residency for Google Drive and GitHub apps with sync**

Google Drive and GitHub apps with sync now support in-region data residency for ChatGPT Enterprise/Edu for all supported data residency regions. Previously, data residency for these apps was only supported in the US. This launch includes both Google Drive user-auth sync and workspace-auth sync. Learn more about [data residency.](/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)

# **February 19, 2026**

## Retiring GPT-5 legacy models

As [previously announced](https://openai.com/index/retiring-gpt-4o-and-older-models/), we are also retiring GPT-5 (Instant and Thinking), [as previously announced](https://openai.com/index/gpt-5-1/). There are no API changes at this time. For details, see our [blog post](https://openai.com/index/retiring-gpt-4o-and-older-models/) and [Help Center](/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models).

## Interactive Code Blocks in ChatGPT

We improved Code Blocks in ChatGPT to make them more interactive.

You can write, edit, and preview your code in ChatGPT, all in one
place:

* Write and edit text in-line
* Preview diagrams and mini apps directly in chat
* Review code in split-screen views

# February 10, 2026

## **Updates to deep research**

We’re introducing improvements to deep research in ChatGPT to help produce more accurate, credible reports with greater control. You can now focus research on specific websites and a larger collection of connected apps as trusted sources.

A redesigned sidebar entry point and fullscreen report view make it easier to start, review, and manage research in one place. Create and edit a research plan before it begins, and track progress with the ability to adjust direction mid-run.

For Enterprise and Edu workspaces, this update does not modify your current role-based access controls (RBAC) or the default deep research configuration.

For more information, please refer to our help center article: [Deep research in ChatGPT](https://help.openai.com/articles/10500283)

# February 2, 2026

## Introducing the Codex App

Today we’re releasing the Codex app for macOS, a command center for managing multiple coding agents in parallel. The app lets you run long‑horizon and background tasks, review clean diffs from isolated worktrees, see agent progress and decisions, and execute reusable skills and automations.

The Codex app follows the same admin controls as Codex local and Codex cloud. Codex local must be enabled for members to use the Codex app. Admins/owners can control Codex access from [Workspace settings](https://chatgpt.com/admin/permissions) -> Permissions & roles, with [RBAC](/en/articles/11750701-rbac), and can use the [compliance API](/en/articles/9261474-compliance-api-for-enterprise-customers) to manage and log Codex usage.

For a limited time, Enterprise/Edu users without flexible pricing receive 2x Codex rate limits. Enterprise/Edu users with flexible pricing qualify for a special promotion, [contact sales](/en/articles/9047878-how-can-i-contact-sales) to learn more.

Get started by [downloading](https://chatgpt.com/codex) the macOS app, and [learn more](/en/articles/11369540-using-codex-with-your-chatgpt-plan) about Codex.

# **January 30, 2026**

## **More models for GPTs with custom actions**

GPTs with custom actions can now use more models in the model picker, including GPT-5.2 Instant and GPT-5.2 Thinking. o-series and Pro models aren’t supported for custom actions. Model availability depends on what your admin has enabled for your workspace.

Previously, GPTs with custom actions could only use GPT-4o, GPT-4.1, and GPT-5 Instant.

# December 18 2025

## Introducing the app directory in ChatGPT

You can now browse and add approved apps in the new [**app directory**](https://chatgpt.com/apps). Apps let you work with your tools and data directly inside a conversation—from interactive in-chat experiences to secure connections that allow ChatGPT to search and reference information from third-party services.

As part of this update, [**connectors now appear in the directory as apps**](/en/articles/11487775-apps-in-chatgpt), making it easier to manage all your tools in one place. References across the Help Center have been updated to reflect this new terminology.

For ChatGPT Enterprise and Edu, apps are disabled by default. Admins and owners can control which apps are available to users using role-based access controls and set which actions each app is allowed to take through [workspace settings](https://chatgpt.com/admin/ca).

Apps are available to all logged-in ChatGPT users, with availability and functionality varying by plan and region. Some apps or capabilities may not be available in certain regions (including the EEA, GB, or Switzerland) or may require specific plan tiers.

Additionally, [developers can submit apps for review and publication](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/) in the app directory, making approved apps available to a broader set of ChatGPT users.

# December 15, 2025

## Apps & connectors admin UI refresh

We’ve refreshed the Apps & connectors section in Workspace settings for admins and owners with a clearer layout: tabs for Enabled, Available, and Draft; a streamlined list view; search and filters; and bulk actions like selecting multiple apps to manage roles or disable. Enabling actions, including sync where supported, now live directly in each connector’s listing.

Available to ChatGPT Enterprise/edu admins in [Workspace settings](https://chatgpt.com/admin/ca). Note that Apps and connectors are disabled by default for Enterprise/Edu plans - enable connectors from the **Available** tab, set up sync, [RBAC](/en/articles/11750701-rbac), and configure MCP actions (depending on app/connector).

Read more about [apps](/en/articles/12503483-apps-in-chatgpt-and-the-apps-sdk) and [connectors](/en/articles/11487775-connectors-in-chatgpt).

# December 11, 2025

### **GPT-5.2 in Early Access for Enterprise**

This week, we’re rolling out GPT-5.2, the most capable model series yet for professional knowledge work with improved work artifact creation like spreadsheets, tool use and longer context retrieval. As with GPT-5.1, we’re continuing to improve our main models for everyone on a regular basis to make them more useful and enjoyable to use.

We’re releasing GPT-5.2 to Enterprise and Edu workspaces in **Early Access**, meaning you can turn it on now for your workspace in [admin settings](https://chatgpt.com/admin/permissions), where you can also manage access to legacy models. We’ll be transitioning custom GPTs to GPT-5.2 on January 12, 2026, and we recommend GPT creators switch as early as possible. [Learn more about custom GPTs.](/en/articles/8555535-gpts-chatgpt-enterprise-version#models-and-custom-actions)

The credits for GPT-5.2 will remain the same as GPT-5. See the current [ChatGPT rate card](/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu) for pricing information.

### **The ChatGPT Compliance API is now part of the OpenAI Compliance Logs Platform**

The OpenAI Compliance Logs Platform is a new, unified way for enterprises to export observability and compliance data via immutable, time-windowed JSONL log files. The Compliance Logs Platform is also now available with Audit, Auth, and Codex logs.

It helps deliver improved reliability, minutes-level latency, and a single ingestion pattern across multiple log categories, including the brand-new ChatGPT Audit & Authentication Logs and Codex Usage Logs. These logs make it possible to audit changes made to workspaces, track authentication activities, and understand Codex usage. [Learn more](/en/articles/9261474-compliance-api-for-enterprise-customers).

# December 3, 2025

## Adding the Atlassian Rovo MCP connector

We’re adding Atlassian Rovo to our list of MCP connectors, which brings in your Jira, Compass, and Confluence information to bring relevant project context into your chats. This connector enables you to take supported write actions in Jira right from ChatGPT — such as creating issues and triggering workflows—based on what you request and on patterns identified in your project data. All actions are initiated, approved and completed directly in chat.

Admins can review actions and other basic information about the connectors in **Workspace settings → Apps**, and set user permissions using [RBAC](https://rbac/). Users can add the Atlassian Rovo from **Settings → Apps & Connectors**.

The Atlassian Rovo connector is available to Enterprise, Edu, Business, Pro and Plus customers with connectors enabled for their workspace.

# November 25, 2025

## Model updates for Enterprise and Edu

GPT-5.1 Instant is now live in the model picker for ChatGPT Enterprise and Edu workspaces, and GPT-5.1 Auto and GPT-5.1 Thinking are no longer available as Early Access options.

GPT-5.1 Pro is now available in Early Access for Enterprise and Edu. Admins and owners can enable access in your [workspace's settings](https://chatgpt.com/admin/permissions). GPT-5.1 Pro is intended for more complex tasks where more reasoning is helpful.

New custom GPTs created in Enterprise and Edu will begin using GPT-5.1 as the default model. Existing custom GPTs are unchanged, and creators can still select a different model (depending on what’s enabled for the workspace and role).

# November 24, 2025

## New MCP connectors available today

We’re rolling out a new set of MCP access connectors built by partners and reviewed by OpenAI, including **Amplitude, Fireflies, Vercel, Monday.com, Stripe, Hex, Egnyte, Alpaca, BioRender, Semrush, and Jam.dev**. This is available to Enterprise, Edu, Business, Pro and Plus customers with connectors enabled for their workspace. These connectors expand the set of tools customers can bring into ChatGPT and will be followed by additional connectors on a rolling basis.

The connectors released today are **access connectors**, which fetch content when a user asks a question, built using MCP. Admins continue to govern access to connectors using RBAC. Connectors remain default off for Enterprise plans, and default on for Business plans.

Admins can review **Actions** and other basic information about these connectors in **Workspace settings → Apps**.

# November 19, 2025

## Custom connectors in company knowledge

Starting today, company knowledge will support custom MCP connectors with search/fetch functionality. Custom connectors fitting these criteria that are enabled for your organization will appear in the company knowledge experience for allowed users, giving your team a more complete, accurate, and company-specific context when using the feature.

Admins/owners can continue to manage access to custom connectors through [RBAC](/en/articles/11750701-rbac) in Workspace settings.

Learn more about [company knowledge](/en/articles/12628342-company-knowledge-in-chatgpt-business-enterprise-and-edu) and [custom MCP connectors](/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta).

# November 12, 2025

## GPT-5.1 in ChatGPT

We’re updating GPT-5 to GPT-5.1 Instant and GPT-5.1 Thinking, making answers both smarter and more conversational. GPT-5.1 Instant now uses light adaptive reasoning for tougher questions while staying fast, and GPT-5.1 Thinking adapts its thinking time more precisely for complex tasks with clearer, less jargony responses.

GPT-5.1 Auto continues to route each query to the best model, and GPT-5 models remain available for three months under the Legacy models dropdown so you can compare and transition at your own pace.

Please note that access to GPT-5.1 is by default disabled for ChatGPT Enterprise workspaces. Admins and owners can enable access in their [**workspace settings**](https://chatgpt.com/admin/permissions).

# November 13, 2025

## Apps & Apps SDK now available to Enterprise/Edu plans

ChatGPT Enterprise/Edu customers will now have access to ChatGPT apps. Apps include interactive interfaces – like presentations, maps, and playlists – that respond to natural language and adapt to your conversation. You can start with a bulleted outline and ask Canva to turn it into a professional presentation, or turn a rough sketch into a FigJam diagram—all without leaving ChatGPT.

Our pilot partners—like Figma, Canva, Booking.com, Coursera, Expedia, Spotify, and Zillow—will be available to Enterprise/Edu customers in markets where their services are offered, starting in English, with more apps coming.

You can also build your own apps with the [Apps SDK](/en/articles/12515353-build-with-the-apps-sdk), then test and deploy it for your team using [developer mode](/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta). Get started in the docs. Learn more: [Apps in ChatGPT and the Apps SDK](/en/articles/12503483-apps-in-chatgpt-and-the-apps-sdk) and [Build with the Apps SDK](/en/articles/12515353-build-with-the-apps-sdk)

## Synced Connector Updates

ChatGPT Enterprise/Edu workspaces can now use ChatGPT connectors for [Azure Boards](/en/articles/12628387-azure-boards-synced-connector), [Basecamp](/en/articles/12628389-basecamp-synced-connector), and [Zoho CRM](/en/articles/12825765-zoho-crm-synced-connector) These connectors deliver faster, higher-quality answers–especially for knowledge-heavy prompts like strategy summaries, policy lookups, and internal research.

For Enterprise/Edu workspaces, connectors are disabled by default— admins and owners can enable specific connectors at any time from their [Workspace connectors settings](https://chatgpt.com/admin/ca), and configure connector access through [RBAC](/en/articles/11750701-rbac). Individual users can connect enabled connectors they want to use from **Settings > Apps & Connectors**. Once enabled, ChatGPT will automatically reference the indexed content when relevant. Learn more about how to use connectors [here](/en/articles/11487775-connectors-in-chatgpt).

# November 6, 2025

## Custom connector action controls

Admins and Owners can now enable or disable individual actions for custom connectors (e.g., to allow *read* but not *write)* and manually refresh actions to pick up developer updates. This brings finer control over what connectors can do in ChatGPT and a simple review path when new connector capabilities are added. Find these controls in **Workspace Settings → Connectors → Manage actions** or during publish.

Available to ChatGPT Enterprise and Edu workspaces using custom connectors. Toggles apply at the workspace level; new actions are disabled by default until approved and modified actions keep their prior state. To use Refresh, an admin/owner must connect to the connector as a user.

[Learn more about these controls in our Help Center article](/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta#h_2496ac9f24).

# October 27, 2025

## Synced Connector Updates

Enterprise and Edu workspaces can now use ChatGPT connectors for [Aha!](/en/articles/12628380-aha-synced-connector), [Asana](/en/articles/12628359-asana-synced-connector), [ClickUp](/en/articles/12628397-clickup-synced-connector), [GitLab Issues](/en/articles/12628403-gitlab-issues-synced-connector), [Help Scout](/en/articles/12628422-help-scout-synced-connector), [Teamwork.com](/en/articles/12628436-teamwork-synced-connector), and [Zoho Desk](/en/articles/12628448-zoho-desk-synced-connector). Synced connectors deliver faster, higher-quality answers – especially for knowledge-heavy prompts like strategy summaries, policy lookups, and internal research.

Admins and Owners can enable connectors from their [Workspace connectors settings](https://chatgpt.com/admin/ca), and can configure user access using [RBAC](/en/articles/11750701-rbac). Connectors remain off by default until an Admin or Owner turns them on. Individual users can connect enabled connectors they want to use from Settings > Apps & Connectors. Once enabled, ChatGPT will automatically reference the indexed content when relevant. Learn more about how to use connectors [here](/en/articles/11487775-connectors-in-chatgpt).

# October 23, 2025

## Company knowledge in ChatGPT

Company knowledge is a new way to bring together context from all your [connected tools](/en/articles/11487775-connectors-in-chatgpt) for answers that know your business, with citations and links back to sources from your apps (for example: Slack, SharePoint, Google Drive, GitHub, Notion, HubSpot, Zendesk, Azure DevOps, Asana, and more).

Company knowledge respects your existing company permissions, so ChatGPT only has access to what each user is already authorized to view. It follows the role-based permissions admins have set for each connector. OpenAI never trains on your data by default. [Learn more](https://openai.com/business-data/) about OpenAI's enterprise-grade security, compliance, and data privacy programs.

Admins enable connectors for the workspace and can manage access with [RBAC](/en/articles/11750701-rbac). At least one connector must be enabled for a user to see company knowledge.

To use it, start a chat, select company knowledge under the message composer, and ask your question to see cited results from approved connectors. Learn more in our [Help Center article](/en/articles/12628342-company-knowledge-in-chatgpt-business-enterprise-and-edu).

# October 17, 2025

## Build, upload, and publish MCP connectors in ChatGPT [Beta]

We’re rolling out full Model Context Protocol (MCP) support with developer mode so your organization can build, test, and publish MCP-powered [connectors](/en/articles/11487775-connectors-in-chatgpt) with read/write capabilities that let ChatGPT take action in your tools. Kick off workflows, create project management tasks, update your CRM, or combine connectors for more complex orchestrations.

Admins can review and publish connectors to the workspace, and use [RBAC](/en/articles/11750701-rbac) to control who can develop, test, and use each connector. Build your own MCP connector, or upload trusted third party connectors.

Learn more in our [Help Center article](/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta).

# October 16, 2025

## Updated Workspace settings

We’ve updated Workspace settings to make administration clearer and faster. A new **General** tab now centralizes workspace customization (name, logo, appearance, and workspace-wide instructions) and adds an **AI policy modal** you can configure to remind users of your organization’s AI policies on a recurring basis.

We’ve also streamlined navigation by combining Identity & provisioning with IP allowlists into a new **Identity & access tab**, and by renaming Settings & permissions to **Permissions & roles.**

See [What workspace settings can I control for my workspace](/en/articles/8411955-what-workspace-settings-can-i-control-for-my-workspace) for details.

## Enterprise Key Management (EKM)

Enterprise Key Management (EKM) is now available for Enterprise and Edu customers. This capability allows organizations to encrypt all customer content using their own external Key Management System (KMS), giving organizations greater control over data security and compliance.

EKM supports integrations with Google Cloud Platform (GCP), Amazon Web Services (AWS), and Microsoft Azure.

Read our [OpenAI Enterprise Key Management (EKM) Overview](https://help.openai.com/articles/20000943) to get started.

Note that EKM will be initially available for ChatGPT Enterprise and Edu workspaces, and will be available for the OpenAI API in the coming weeks.

# October 13, 2025

## Introducing the ChatGPT app & connector for Slack

We’re rolling out two new ways to bring Slack and ChatGPT together: a [connector](/en/articles/11487775-connectors-in-chatgpt) that brings your Slack context into ChatGPT, and a ChatGPT app for Slack – an integration that enables you to chat with ChatGPT from inside Slack.

With the [**ChatGPT app for Slack,**](https://intercom.help/openai/en/articles/12462158-chatgpt-app-for-slack) you can chat one-on-one with ChatGPT in a dedicated Slack sidebar – a space to ask questions, summarize long threads into action items, draft replies, and search messages and files you already have access to. Chats you start in Slack also appear in your ChatGPT sidebar, so it’s easy to pick up later from web or mobile. Semantic search is supported for Slack customers with AI enabled on Business+ or Enterprise+ plans; all other plans use keyword search.

With the [**ChatGPT connector for Slack**](https://intercom.help/openai/en/articles/12525822-chatgpt-connector-for-slack)**,** you can securely bring in context from your Slack channels and DMs, making responses more helpful. Available in chat, Deep Research, and Agent Mode. Admins can enable the connector from their [Workspace connectors settings](https://chatgpt.com/admin/ca), and can configure user access by [RBAC](/en/articles/11750701-rbac). Users can enable the connector from **Settings > Apps & Connectors**.

Both app and connector are available to **Plus, Pro, Business and Enterprise/Edu** customers. Additionally, the ChatGPT app for Slack requires a **paid Slack account;** availability and workspace installation may depend on your Slack workspace settings.

Installing the app requires the connector to be enabled for your account.

Visit the [**ChatGPT app for Slack**](https://intercom.help/openai/en/articles/12462158-chatgpt-app-for-slack) page to get started with installation.

We additionally added the [Intercom synced connector](/en/articles/12562556-intercom-synced-connector), which allows you to access and interact with your Intercom data—including conversations, tickets, and help center content.

# October 9, 2025

## Connector Updates

Enterprise and Edu workspaces can now use an **admin-managed sync connector for SharePoint**. Admins authenticate once and deploy at workspace scale—choosing to sync all sites or specific folders via a file picker—while ChatGPT enforces existing SharePoint permissions. Users are matched by email and only see files they already have access to, with no per-user setup required. Connections can be enabled, updated, or removed at any time. Read more in our [SharePoint Connector Help Center article](/en/articles/12143177-sharepoint-connectors-on-chatgpt).

We’re also adding [**Notion**](/en/articles/12532955-notion-synced-connector) and [**Linear**](/en/articles/12526595-linear-synced-connector) as [synced connectors](/en/articles/10847137-chatgpt-synced-connectors), so teams can securely bring Notion pages and Linear issues/discussions into Chat for fast answers and summaries.

All three connectors are managed in ChatGPT workspace [**Admin connectors settings**](https://chatgpt.com/admin/ca) in the **Synced connectors** section ([RBAC](/en/articles/11750701-rbac) supported). Once enabled, ChatGPT will automatically reference the indexed content when relevant.

# October 6, 2025

## Updates to Codex

We’re rolling out new Codex capabilities to help teams work and build better: [Codex now works in Slack](https://developers.openai.com/codex/integrations/slack), and supports programmatic control through the [Codex SDK](https://developers.openai.com/codex/sdk). We’ve also added new admin controls and analytics so workspace admins can manage Codex Cloud environments, set safe defaults for CLI/IDE usage, and monitor usage with improved dashboards. Additionally, [Codex rates](/en/articles/11481834-chatgpt-rate-card#h_e8c3d8c100) have been updated.

For more information, review our Help Center article on [Codex](/en/articles/11369540-using-codex-with-your-chatgpt-plan), and the [Codex developer documentation](https://developers.openai.com/codex).

# October 3, 2025

## GPT-5 Auto routing control for reasoning

Enterprises on [flexible pricing](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) can now adjust how **GPT-5 Auto** handles reasoning requests. When enabled, these requests will route to **GPT-5 Thinking Mini** instead of **GPT-5 Thinking**.

If your workspace or custom roles have **GPT-5 Thinking** enabled, members can still manually select it from the model picker at any time.

Learn more about how to enable this setting in [ChatGPT Enterprise and Edu - Models & Limits](/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits).

# September 25, 2025

## Introducing project sharing

Today, we’re announcing an update to [projects in ChatGPT](/en/articles/10169521-projects-in-chatgpt). Now you can share projects with teammates in your workspace, adding files and instructions together to guide ChatGPT’s responses toward a shared goal. Members can chat with the project’s context to stay on the same page as new information gets added and create work that stays consistent in tone.

Shared projects are ideal for ongoing work like client management, content creation, reporting, and research.

Invite members in your workspace by individual email, group email, or shared link. Add/remove project members, set project access permissions, create new chats, add/remove files, and allow members to bring existing chats into the project. Memory is project-only, ensuring sensitive data stays safely within the project.

For more information, see our help center article on [project sharing](/en/articles/10169521-projects-in-chatgpt#h_e8f291686b).

*Note: Shared projects include a 4-week early access period until October 23, 2025. They’re off by default during this time. You can enable access for specific roles anytime with role-based access controls (RBAC), or keep the feature off for your entire workspace in Settings. If you take no action, the feature turns on for everyone when early access ends, following any RBAC settings you’ve set. Learn more* [*here*](/en/articles/10169521-projects-in-chatgpt#h_542cf9638f)*.*

# September 15, 2025

## Updates to Codex

We’re adding GPT-5-codex, a GPT-5 variant optimized for agentic coding in Codex. It’s available everywhere you use Codex: default for cloud tasks and code review, and selectable for local workflows via the Codex CLI and IDE extension. Use GPT-5-codex for coding-focused work in Codex, or Codex-like environments; use GPT-5 for general, non-coding tasks. Please review the [announcement](https://openai.com/index/introducing-upgrades-to-codex/) blog for more information.

*Note: GPT-5-Codex is not currently supported in ChatGPT or the API.*

To learn more about Codex, visit the [developers site](http://developers.openai.com/codex) as well as our general help article: [Using Codex with your ChatGPT plan](/en/articles/11369540).

# September 4, 2025

## Website blocking for ChatGPT agent

Enterprise and Edu workspace owners can now request to block specific websites or entire domains (including all subdomains) from ChatGPT agent browsing and actions.

If you would like a blocklist set up for your workspace, contact your OpenAI Account Director or Customer Success Manager.

If you do not have an account team, please [contact OpenAI Support](/en/articles/6614161-how-can-i-contact-support).

Learn more about [website blocking in ChatGPT agent](/en/articles/11752874-chatgpt-agent#h_a916076c08).

# September 3, 2025

## SharePoint sync connector

Enterprise and Edu workspaces can now use the [SharePoint synced connector](/en/articles/10847137-chatgpt-synced-connectors-faq), which enables workspace members to securely ask questions and get answers directly from their OneDrive and SharePoint files. Connections can be created, deleted, or modified at any time. Once enabled, ChatGPT will automatically reference your SharePoint content when relevant.

ChatGPT Enterprise workspace Admins must enable access to the SharePoint connector and the SharePoint *sync connector* in their workspace’s [Admin connectors settings](https://chatgpt.com/admin/ca). Once this is enabled, each user can connect their individual account by signing in to SharePoint through an OAuth flow. [Admins can further configure access settings with RBAC.](/en/articles/11750701-rbac)

[Learn more about setting up the SharePoint synced connector for your workspace.](/en/articles/12143177-sharepoint-synced-connectors-setup)

## IP allowlisting

Enterprise and Edu workspaces can now enable **IP allowlisting** to control which IP addresses can access ChatGPT and the Compliance API. When enabled, only users from the IPs you specify will be allowed access. Any request from an unlisted IP will be blocked, even if the user has valid credentials.

This feature applies to all ChatGPT endpoints, including authenticated file downloads and Compliance API keys. For Compliance API traffic, IP Allowlisting is always enforced and cannot be turned off.

**Note:** IP Allowlisting is specific to **ChatGPT**. It does **not** apply to the API Platform ([platform.openai.com](https://platform.openai.com/?utm_source=chatgpt.com))

Workspace owners and admins can manage allowlists in a new tab in **Workspace Settings** entitled **IP allowlist**.

Learn how to set up and manage IP allowlisting in our article: [IP allowlisting for ChatGPT](/en/articles/12111596-ip-allowlisting-for-chatgpt)

# August 28, 2025

## GitHub connector access for Enterprise and Edu

Enterprise and Edu workspaces globally can now use the GitHub [synced connector](/en/articles/10847137) and [chat connector](/en/articles/11487775-connectors-in-chatgpt#h_584a7d13e3) in ChatGPT, in addition to the GitHub deep research connector.

The synced connector pre‑indexes your organization’s GitHub repositories, enabling faster and higher‑quality contextual responses about code, commits, and pull requests—making it the recommended option for improved quality.

For detailed setup steps, including how to exclude certain repositories, see [Connecting GitHub to ChatGPT](/en/articles/11145903-connecting-github-to-chatgpt). Access to connectors can be managed through ChatGPT’s [RBAC controls for connectors](/en/articles/11509118-admin-controls-security-and-compliance-in-connectors-enterprise-edu-and-team#h_227601b351).

Learn more about [connectors](/en/articles/11487775-connectors-in-chatgpt).

## RBAC for connectors

Role-based access controls (RBAC) now extend to connectors. Enterprise and Edu workspaces can assign connector access directly to custom roles, giving admins greater flexibility when managing permissions across teams.

For a walkthrough on how to configure RBAC for connectors, please refer to our article here: [Admin Controls, Security, and Compliance in Connectors](/en/articles/11509118-admin-controls-security-and-compliance-in-connectors-enterprise-edu-and-team#h_227601b351)

Learn more about [RBAC](/en/articles/11750701-rbac).

## Gmail, Google Calendar, and Google Contacts connectors in ChatGPT

Gmail, Google Calendar, and Google Contacts are now available to connect and use in chat. Once you enable them, ChatGPT will automatically reference them when relevant, making it faster and easier to bring information from these tools into your conversations without having to manually select them each time.

If you already have Gmail or Google Calendar enabled for deep research, you can now also use them in chat. To use them in deep research, you will still need to enable each connector separately and select it every time you start a new deep research request.

Learn more about [**connectors**](/en/articles/11487775-connectors-in-chatgpt).

# August 27, 2025

## Updates to Codex

Starting today, Codex works with you everywhere you build—in your terminal or IDE, on the web, in GitHub, and even from the ChatGPT iOS app. Your ChatGPT account connects it all, so you can work seamlessly between your local environment and Codex’s cloud without losing state.

We’re excited to introduce the latest Codex updates:

* **IDE Extension:** The new extension brings codex into VS Code, Cursor, and other VS Code forks, so that you can seamlessly preview local changes and edit code

* **Sign in with ChatGPT:** Available in both the IDE and CLI, eliminating API key setup and providing access directly through your existing ChatGPT plan

* **Seamless Local ↔ Cloud Handoff:** Developers can pair with Codex locally and then delegate tasks to the cloud to execute asynchronously without losing state

* **Upgraded Codex CLI:** Refreshed UI, new commands, and bug fixes

* **Code reviews in GitHub:** Set up Codex to automatically review new PRs in a repo, or mention @codex in PRs to get reviews and suggested fixes

Additionally, all product information and updates for Codex moving forward will be announced on our new site: [developers.openai.com/codex](http://developers.openai.com/codex). The Codex Enterprise Admin Guide is also now available on this site: [developers.openai.com/codex/chatgpt-enterprise](https://developers.openai.com/codex/chatgpt-enterprise)

We invite you to explore the site for more details on these new features, as well as guides on how to get started.

To learn more about Codex, visit the new [developers site](http://developers.openai.com/codex) as well as our general help article [Using Codex with your ChatGPT plan](/en/articles/11369540).

# August 22, 2025

## Project-only memory

An improvement to [projects](/en/articles/10169521-projects-in-chatgpt) is now available. When creating a project, users have the option to enable **project-only memory.**

With **project-only memory** enabled, ChatGPT can use other conversations in that project for additional context, and won’t use your [saved memories](/en/articles/11146739-how-does-reference-saved-memories-work) from outside the project to shape responses. Additionally, it won’t carry anything from the project into future chats outside of the project.

This creates a focused, self-contained space, which is useful for long-running or sensitive work where you want ChatGPT to stay anchored to that project’s tone, context, and history.

Note:

* **Personal Memory** must be enabled to utilize this feature.

* **Settings** -> **Personalization** -> **Memory**

* **Workspace Memory must be enabled to utilize this feature.**

* Workspace owners can enable this by **Workspace Settings** -> **Memory**

* This feature will initially only be available on the ChatGPT website and Windows app. Support for mobile (iOS and Android) and macOS app will follow in the coming weeks.

Learn more about [memory in projects](/en/articles/10169521-projects-in-chatgpt#h_374a3efb05).

# August 14, 2025

## Study Mode

Study mode is now available to ChatGPT Enterprise users. Study mode works with any model available in ChatGPT on iOS, Android, web, and desktop.

Study mode is a new learning experience in ChatGPT designed to help you build a deeper understanding of any topic. When you turn it on, ChatGPT will ask interactive questions to understand your goals and skill level, then work with you to reach the answer together.

With Study mode enabled, ChatGPT can:

* Guide understanding with Socratic-style questions.

* Break concepts into easy to follow sections starting simple and adding complexity as you progress.

* Personalize responses based on your past chats if memory is on, using examples and tips tailored to you.

* Check your understanding with open-ended prompts and feedback.

* Work with your materials by referencing images or PDFs you upload.

You can enable study mode at any time by selecting **Tools** in the prompt window and choosing **Study and learn** from the drop‑down menu or go to [**chatgpt.com/studymode**](http://chatgpt.com/studymode).

Study mode is powered by custom system instructions and can have some inconsistent behavior and mistakes across conversations. We plan on training this behavior directly into our main models once we’ve learned what works best through iteration and user feedback.

[**Learn more about study mode.**](/en/articles/11780217)

# August 12, 2025

## GPT-5

GPT-5 in ChatGPT is our next flagship model and the new default for all logged-in users. It simplifies ChatGPT to a single auto-switching system that brings together the best of our previous models into a **smart, fast model.**

ChatGPT Enterprise and Edu workspaces have flexibility in how legacy models are made available. Workspace admins can enable additional legacy models (GPT-4.1, GPT-4.5, OpenAI o3, o3-pro, and o4-mini) for the entire workspace in their [**admin settings**](https://chatgpt.com/admin). These models [**consume credits**](/en/articles/11481834-chatgpt-rate-card), so availability is controlled at the admin level.

[Learn more about ChatGPT Enterprise limits.](/en/articles/11165333-chatgpt-enterprise-models-limits)

# August 11, 2025

## Additional connectors

**Now connect even more tools in ChatGPT for useful, relevant responses in chat.**

Microsoft Teams, Outlook email and calendar connectors are now available to search by chat in addition to deep research.

To enable, visit **Settings** → **Connectors**→ **Connect** on the application. Note that connectors are still in beta and defaulted off for Enterprise & Edu plans. Admins can enable them for their workspace in [Settings](https://chatgpt.com/admin/settings).

Learn more about [connectors](/en/articles/11487775-connectors-in-chatgpt).

# August 8, 2025

## ChatGPT agent

ChatGPT agent is now available for Enterprise and Edu plans. This was previously made available to Plus, Pro, and Team users on July 17, 2025.

ChatGPT agent allows ChatGPT to complete complex online tasks on your behalf. It seamlessly switches between reasoning and action—conducting in-depth research across public websites, uploaded files, and [connected](/en/articles/11487775-connectors-in-chatgpt) third-party sources (like email and document repositories), and performing actions such as filling out forms and editing spreadsheets—all while keeping you in control.

Learn more in the [ChatGPT agent FAQ](/en/articles/11752874-chatgpt-agent).

# August 6, 2025

## Study Mode

Study mode is now available to ChatGPT Edu users. Study mode works with any model available in ChatGPT on iOS, Android, web, and desktop.

Study mode is a new learning experience in ChatGPT designed to help you build a deeper understanding of any topic. When you turn it on, ChatGPT will ask interactive questions to understand your goals and skill level, then work with you to reach the answer together.

With Study mode enabled, ChatGPT can:

* Guide understanding with Socratic-style questions.

* Break concepts into easy to follow sections starting simple and adding complexity as you progress.

* Personalize responses based on your past chats if memory is on, using examples and tips tailored to you.

* Check your understanding with open-ended prompts and feedback.

* Work with your materials by referencing images or PDFs you upload.

You can enable study mode at any time by selecting **Tools** in the prompt window and choosing **Study and learn** from the drop‑down menu or go to [**chatgpt.com/studymode**](http://chatgpt.com/studymode).

Study mode is powered by custom system instructions and can have some inconsistent behavior and mistakes across conversations. We plan on training this behavior directly into our main models once we’ve learned what works best through iteration and user feedback.

[Learn more about study mode.](/en/articles/11780217)

# July 24, 2025

## Canva and Notion connectors

Enterprise and Edu users can now connect to Canva and Notion for both chat search and deep research.

Learn more about [connectors](/en/articles/11487775-connectors-in-chatgpt), as well as about [controls, security, and compliance for admins](/en/articles/11509118-admin-controls-security-and-compliance-in-connectors-enterprise-edu-and-team).

## Chat search for HubSpot and custom connectors (MCP)

Enterprise and Edu users can now utilize chat search with HubSpot and custom connectors (MCP) in addition to deep research.

Learn more about [connectors](/en/articles/11487775-connectors-in-chatgpt), as well as [how to create a custom connector using MCP](https://platform.openai.com/docs/mcp).

# July 17, 2025

## New role-based access controls ('RBAC') in Admin Settings

Starting today, new role-based access controls will begin rolling out to Enterprise/Edu workspaces.

Workspace Owners will gain RBAC functionality within [chatgpt.com/admin/settings](http://chatgpt.com/admin/settings) where they can:

* Set a default role for members who do not have one or more Custom Roles assigned

* Create custom roles with granular permissions that override the workspace default role

* Assign one or multiple Custom Roles to Groups

* View and manage Custom Roles in a centralized tab

All of our [supported countries](https://platform.openai.com/docs/supported-countries) should have access to this feature.

For all details see our [RBAC help article](/en/articles/11750701-rbac).

# June 24, 2025

## Priority Processing in the API

We’re launching **Priority processing** for Enterprise API users. Priority processing offers the same premium latency and uptime SLAs as Scale Tier, but with flexible pay-as-you-go pricing and no provisioning requirements. It’s designed for latency-sensitive, user-facing workloads where consistently fast response times are important.

At launch, Priority processing is available for the following models:

* GPT-4o, GPT-4o mini

* GPT-4.1, GPT-4.1 mini, GPT-4.1 nano

* o3

* o4-mini

Enterprise customers can select Priority processing on a per-request basis using the service\_tier="priority" parameter. Usage is billed separately from Scale Tier commitments. Ramp rate limits apply to protect performance during rapid traffic increases.

Learn more about [Priority processing](https://openai.com/api-priority-processing/) and read [our FAQ](/en/articles/11647665-priority-processing-faq).

## Project file limit increased

Projects for Enterprise and Edu users now support up to 40 uploaded files, increased from the previous limit of 20.

# June 18, 2025

## Record mode in ChatGPT macOS desktop app

Capture meetings, brainstorms, or voice notes.

* ChatGPT will transcribe, summarize, and turn them into helpful outputs like follow-ups, plans, or even code.

* Available on the macOS desktop app only

Record mode will be disabled by default for all Enterprise and Edu workspaces, and must be enabled by a workspace owner under **Workspace Settings -> Record.**

Learn more about [ChatGPT Record](/en/articles/11487532).

Note that record mode rolled out to Team users on June 4. Today, it is also enabled for Enterprise and Edu plans.

## OpenAI o3-pro replaces o1-pro in model picker

OpenAI o3-pro will replace o1-pro in the model picker for ChatGPT Enterprise and Edu users. o3-pro is our latest pro model, delivering stronger performance across complex science, programming, business, and education queries.

* Supports browsing, Python, file analysis, and image reasoning

* Does not support image generation, canvas, or temporary chats. Continue to use GPT-4o, o3, or o4-mini for those features

Learn more about [o3-pro](https://platform.openai.com/docs/models/o3-pro).

## Adding More Capabilities to Projects

We’re adding several updates to projects in ChatGPT to help you do more focused work.

* Deep research and voice mode support

* Sharing chats from projects

* Starting a new project directly from a chat

* Upload files and access model selector on mobile

Learn more about [projects in ChatGPT](/en/articles/10169521-using-projects-in-chatgpt).

Note these improvements rolled out to Plus, Pro, and Team users on June 12. Today, they are also enabled for Enterprise and Edu plans.

## Custom GPTs support all models

Custom GPTs without actions will support all available models in ChatGPT. GPT creators can define a recommended model for their GPT, and users will have the option to switch models while using it.

GPTs with custom actions will continue to support GPT-4o and GPT-4.1 only.

Learn more about [GPTs](https://help.openai.com/en/collections/8475420-gpts).

# June 16, 2025

## Expanded Model Support for Custom GPTs

Enterprise and Edu users can now choose from the full set of ChatGPT models (GPT-4o, o3, o4-mini and more) when building Custom GPTs—making it easier to fine-tune performance for different tasks, industries, and workflows. Creators can also set a recommended model to guide users.

Key details:

* GPTs *without Custom Actions* can use the model picker to select from all models available to the user.

* GPTs *with Custom Actions* currently support GPT-4o and 4.1

* Available on web

# June 4, 2025

## Connectors in ChatGPT (Beta)

Customers can now enable connectors to bring internal tools and content into ChatGPT.

* Supported connectors: Google Drive, SharePoint, Dropbox, and Box

* Real-time access with in-line citations

* Admins control connector access in Admin Settings (off by default)

Learn more about [Connectors in ChatGPT](/en/articles/11487775).

## Connectors in deep research (Beta)

Use connectors in Deep Research to generate long-form, cited responses that include your company’s internal tools.

* Supported connectors: Google Drive, SharePoint, Dropbox, Box, Outlook, Gmail, Google Calendar, Linear, GitHub, HubSpot, and Teams

* Combines internal + web sources for synthesis

Learn more about [Connectors in ChatGPT](/en/articles/11487775).

## Google Drive synced connector

The synced connector indexes your organization’s Drive content in advance, enabling fast and high quality contextual responses.

* Semantic search across Docs, Slides, Sheets, and more in ChatGPT

* Supports o4-mini, o3, and GPT-4o

* Admin scoping by user

Learn more about the [Google Drive synced connector](/en/articles/10847137).

## Custom connectors via Model Context Protocol (Beta)

Admins can now build and deploy custom connectors to proprietary systems using Model Context Protocol (MCP).

* Requires a remote MCP server

* Available only in deep research

* Admin-published connectors appear in the connector list for all users

Learn more about [building custom connectors with MCP](http://platform.openai.com/docs/mcp).

## New flexible pricing for ChatGPT Enterprise plans

Flexible pricing for Enterprise plans introduces credit-based access to advanced ChatGPT models and features. Enterprise workspaces purchase a shared credit pool at the contract level. All users in a workspace draw from this pool when using advanced features. There are no individual rate limits. All users retain unlimited access to core ChatGPT models and features.

# May 29, 2025

## Web Composer UI Changes

We’re streamlining the composer. Instead of separate buttons for “Search”, “Deep research”, and more, you’ll now see a single **Tools** dropdown in the lower-left corner.

![ChatGPT composer with Tools menu open for image creation, web search, writing or code, and deep research](https://images.ctfassets.net/j22is2dtoxu1/5lfLurlZBnN0Z5XnQr45eY/40ce9051e53e71e3842f14353cf6ef4f/may292025_web_composer.png?q=80&fm=webp&w=878)

All the same capabilities and tools are still there—just tidier and easier to access in one menu.

# May 22, 2025

## Releasing GPT-4.1 in ChatGPT

Since its launch in the API in April, GPT-4.1 has become a favorite among developers—by popular demand, we’re making it available directly in ChatGPT.

GPT-4.1 is a specialized model that excels at coding tasks. Compared to GPT-4o, it's even stronger at precise instruction following and web development tasks, and offers an alternative to OpenAI o3 and OpenAI o4-mini for simpler, everyday coding needs.

Starting today, Enterprise and Edu users can access GPT-4.1 via the "more models" dropdown in the model picker. GPT-4.1 has the same rate limits as GPT-4o for paid users.

## Introducing GPT-4.1 mini, replacing GPT-4o mini, in ChatGPT

GPT-4.1 mini is a fast, capable, and efficient small model, delivering significant improvements compared to GPT-4o mini—in instruction-following, coding, and overall intelligence. GPT-4.1 mini replaces GPT-4o mini in the model picker under "more models" for paid users, and will serve as the fallback model for free users once they reach their GPT-4o usage limits. Rate limits remain the same.

Evals for GPT-4.1 and GPT-4.1 mini were originally shared in the [blog post](https://openai.com/index/gpt-4-1/) accompanying their API release. They also went through standard safety evaluations. Detailed results are available in the newly launched [Safety Evaluations Hub](https://openai.com/safety/evaluations-hub/).

# May 15, 2025

## Export Deep Research as PDF

You can now export your deep research reports as well-formatted PDFs—complete with tables, images, linked citations, and sources.

To use, click the share icon and select 'Download as PDF.' It works for both new and past reports.

## Mobile UI Composer Consolidation (iOS/Android)

We've removed the row of individual tool icons from the mobile composer and replaced it with the new sliders‑style icon to open the **Skills** menu; tapping that button opens a bottom‑sheet menu where users can choose tools like Create an image or Search the web.

![ChatGPT message composer with Ask anything prompt plus, tools, microphone, and voice mode buttons](https://images.ctfassets.net/j22is2dtoxu1/40QIpEtjPhGLqTMBCejijc/aa6c15ae67b99544531be358a8759417/2025-05-15.png?q=80&fm=webp&w=1344)

No tools are deprecated—access is simply consolidated to clear space and reduce on‑screen clutter.

# May 8, 2025

## User Analytics in ChatGPT - GA

The revamped User Analytics dashboard can be accessed in the **Manage workspace** console in the **Analytics tab**. It provides more comprehensive data on usage, adoption, and engagement than the original analytics tab.

This improved dashboard gives Admins a high-level view of how ChatGPT is being used across your organization—use it to track adoption and engagement, understand usage patterns for top tools and GPTs, and identify use cases and user trends.

See [User Analytics for ChatGPT Enterprise and Edu](/en/articles/10875114-user-analytics-for-chatgpt-enterprise-and-edu) and [Compliance API vs User Analytics in ChatGPT Enterprise/Edu](/en/articles/11327494-compliance-api-vs-user-analytics-in-chatgpt-enterprise-edu).

# May 2, 2025

## 4o Image Generation in GPTs

GPTs can now leverage ChatGPT’s image-generation capabilities to produce images on demand for users.

GPT creators can enable "4o Image Generation" in the Configure section of the GPT editor, under **Capabilities**.

![Capabilities list with Web Search, Canvas, and 4o Image Generation enabled, Code Interpreter unchecked](https://images.ctfassets.net/j22is2dtoxu1/670wNgOwRdKAaHf8VI6aWE/ba31f174568be19ebf78a10af4891615/2025-05-02-4oimage.png?q=80&fm=webp&w=282)

# May 1, 2025

## Deep research

Users that reach their monthly limit (10 tasks/month) with the standard deep research model will now receive 15 additional requests automatically for that month with our lightweight, cost-effective version until the monthly limit resets.

[Learn more about deep research.](/en/articles/10500283-deep-research-faq)

## Tasks in o3 and o4-mini

You can now create scheduled tasks that enable ChatGPT to run automated prompts and proactively reach out to you on a scheduled basis with o3 and o4-mini. The “ChatGPT with Schedules Tasks” option in the model selector has been removed.

[Learn more about scheduled tasks in ChatGPT.](/en/articles/10291617-scheduled-tasks-in-chatgpt)

# April 24, 2025

## o3 and o4-mini

With the introduction of o3 and o4-mini / o4-mini-high, they will supersede o1 and o3-mini / o3-mini-high respectively within ChatGPT.

**OpenAI o3** is our most powerful reasoning model that pushes the frontier across **coding, math, science, visual perception**, and more. It sets a new SOTA on benchmarks including Codeforces, SWE-bench (without building a custom model-specific scaffold), and MMMU. It’s ideal for complex queries requiring multi-faceted analysis and whose answers may not be immediately obvious. It performs especially strongly at visual tasks like analyzing images, charts, and graphics. In evaluations by external experts, o3 makes 20 percent fewer major errors than OpenAI o1 on difficult, real-world tasks—especially excelling in areas like programming, business/consulting, and creative ideation. Early testers highlighted its analytical rigor as a thought partner and emphasized its ability to generate and critically evaluate novel hypotheses—particularly within biology, math, and engineering contexts.

**OpenAI o4-mini** is a smaller model optimized for fast, cost-efficient reasoning—it achieves remarkable performance for its size and cost, particularly in **math, coding, and visual tasks**. It is the best-performing benchmarked model on AIME 2024 and 2025. In expert evaluations, it also outperforms its predecessor, o3‑mini, on non-STEM tasks as well as domains like data science. Thanks to its efficiency, o4-mini supports significantly higher usage limits than o3, making it a strong high-volume, high-throughput option for questions that benefit from reasoning.

# April 10, 2025

## ChatGPT images

Image generation in GPT-4o is now available to all users as the default image generator in ChatGPT. Users who prefer to continue with DALL·E can still access it through the DALL·E GPT.

You can generate images with ChatGPT by simply asking the model to create an image with the details you want, or by selecting the Create image option in the composer. [Learn more](/en/articles/8932459-creating-images-in-chatgpt).

# March 31, 2025

## User Analytics in ChatGPT - public beta

The revamped User Analytics dashboard can be accessed in the Manage workspace console in the Analytics tab. It provides more comprehensive data on usage, adoption, and engagement than the original analytics tab.

This improved dashboard gives Admins a high-level view of how ChatGPT is being used across your organization—use it to track adoption and engagement, understand usage patterns for top tools and GPTs, and identify use cases and user trends.

See User Analytics for [ChatGPT Enterprise and Edu (public beta)](/en/articles/10875114-user-analytics-for-chatgpt-enterprise-and-edu-public-beta) for details.

# March 20, 2025

## Shared Projects Update

We’re holding off on launching shared projects with View and Edit access so that we can work on a more collaborative version that will be valuable to users.

# March 13, 2025

## Coding with Work with Apps on macOS

When working with IDEs, you can ask ChatGPT to edit open files directly—no copy-pasting required. When you ask for an edit, ChatGPT will generate a diff that you can review and apply, and there’s also an option to automatically apply edits. Diffs are easy to revert in the ChatGPT UI, or by using CMD+Z in your editor.

![ChatGPT desktop companion open beside Xcode while editing a Swift SolarSystemDemo file](https://images.ctfassets.net/j22is2dtoxu1/65OOMxu5HjncQxWzWjrRj5/0bdc13b5c7e8a9e43f710aa0da58feb3/2025-03-13.gif)

Enterprise admins can flip the "Work with Apps" toggle off in their Admin Settings to disable this functionality for their workspace members.

## GPT-4.5 in ChatGPT

As of March 13, 2025, users in Enterprise and Edu plans will now be able to use our GPT-4.5 model in ChatGPT!

See GPT-4.5 in ChatGPT for details.

# March 10, 2025

## Deep research in Compliance API ChatGPT

As of March 10th, 2025, for Enterprise customers using the Compliance API your options include:

* Search for the "deep research global prompt".

* Look for the tool name in the response look for **{"tool\_name":"deep\_research"}**.

# February 25, 2025

## Deep research in ChatGPT

In ChatGPT deep research is now available to users on the Enterprise plan.

Deep Research allows ChatGPT to agentically and asynchronously browse the web to complete your professional or personal work.

Enterprise and Edu users will have 10 deep research queries per month.

See our Deep research FAQ for details.

# February 13, 2025

## o1 pro mode and o3-mini in ChatGPT

In ChatGPT o1 pro mode is now available to Enterprise and o3-mini to Enterprise Edu!

* **o3-mini:** OpenAI **o3-mini** has replaced o1-mini in the model picker. It’s more cost effective and offers higher rate limits at lower latency. It’s a reasoning model, making it a great choice for coding, STEM, and logical problem-solving tasks. o3-mini shows its chain of thought, and can browse the web.

* **o1 pro mode**: Also available in the model picker this week is **o1 pro mode**. Designed for accuracy and depth, it excels in research, engineering, business, and law—ideal for professionals tackling highly complex challenges. O1 pro mode will take longer to think through a problem. So responses can take some time. Due to its computational intensity, each user is limited to five queries per month. For most tasks, o1, o3-mini, or GPT-4o will remain optimal choices.

*Re: File Uploads*

* *Images, docs, and PDFs are supported in the* ***o1****,* ***o3-mini****, and* ***o3-mini-high***\* models. No spreadsheets (CSV/Excel).\*
* *Only images are supported in* ***o1 pro mode****. No docs/PDF and no spreadsheets (CSV/Excel).*

## Canvas Sharing

ChatGPT Enterprise and Edu users can now share a Canvas asset such as rendered React/HTML code, document, or code with another user, similar to how you share a conversation. You can do this from the Canvas toolbar when Canvas is open.

![OpenAI canvas preview with dotted text reading "Sharing now available"](https://images.ctfassets.net/j22is2dtoxu1/3grkJx9AQfn7R06zrXXBOJ/c1234a8d43170d22caefd88d0af3a6e9/2025-02-13.gif)

For more details about the canvas feature in ChatGPT, check out the following Help Center article!

# January 23, 2025

## Projects

Projects are now available for all paid plans including Enterprise and Edu.

See Using projects in ChatGPT for details.

# January 16, 2025

## Visual Retrieval (PDFs) for ChatGPT Enterprise

ChatGPT Enterprise now supports reading and understanding visuals (images, graphs, diagrams, etc.) embedded in PDF files. Users can upload a PDF, and ChatGPT can interpret the text and any visual elements within that file.

For details see Visual Retrieval with PDFs FAQ.

# December 12, 2024

## o1

Starting today, all ChatGPT Enterprise customers will be able to access o1 through the model selector, replacing o1-preview.

o1 can now be used to reason about image uploads, opening up new applications by analyzing and explaining visual representations with more detail and accuracy. We have also trained the model to be more concise in its thinking, resulting in faster response times than o1-preview.

# December 11, 2024

## Apple Intelligence with ChatGPT

ChatGPT admins can now enable and disable access to Apple Intelligence from their workspace admin settings, under Connections.

If this setting is toggled off, users cannot select their ChatGPT Enterprise/Edu workspace when logging in with their OpenAI credentials.

# December 10, 2024

## Canvas

Today we made Canvas available in 4o by default for all users, Free and Paid. Additionally, we launched a number of new capabilities for canvas, including:

* **Canvas in GPTs**: Canvas can now be used with GPTs when enabled in the GPT creator. This toggle will be enabled for newly created GPTs by default.
* **Python code execution**: You can now execute Python code in a canvas. ChatGPT will take a pass on fixing bugs in your code and provide comments on errors. Please note that executing Python can make external network requests, and Enterprise workspace admins can disable Python code execution by toggling the **Canvas code execution** setting in their [Admin settings](https://chatgpt.com/admin/settings). This is turned off by default for all Enterprise accounts.
* **Canvas shortcut:** You can now paste content into ChatGPT and instantly open it in canvas via a shortcut in the upper right corner of the composer.
* **Canvas in Toolbox:** Canvas has been added as an option in the toolbox.

Workspace admins can now use the Compliance API to get, list, and delete canvas text documents.

Please note that the Admin Setting to disable canvas has been removed, as this feature is now out of beta. If this was previously disabled, we will continue to honor that setting. Please contact our support team using the chat bubble in the bottom-right corner of this page.

# December 3, 2024

## Work with Apps on macOS

ChatGPT can now read content from your coding apps, bringing you smarter, more accurate answers tailored to your work by using Work with Apps on macOS. Learn more about [Work with Apps on macOS](/en/articles/10119604-work-with-apps-on-macos).

Enterprise admins can flip the "Work with Apps" toggle off in their Admin Settings to disable this functionality for their workspace members.

# November 22, 2024

## Updates to the ChatGPT Web experience

We are rolling out the following updates over the next two weeks to all ChatGPT users.

### **Sidebar redesign**

* New floating mode added with soft dismiss behavior

* Recent conversations are now limited in the sidebar, with an unlimited infinite scroll flyout for all conversations

* Recent GPTs & Pinned GPTs are now displayed below conversations

* Settings are now always in the bottom of the sidebar

* A small settings icon was added in larger viewports when the sidebar is not open

* New transitions were added to create a more immersive feel

### **Other updates for ChatGPT on Web**

* The core underpinnings of the site were revamped, offering much better support for a larger variety of devices and sizes

* Initiating a new conversation now scrolls it into view at the top of the screen

* Initiating a new conversation no longer auto scrolls to the bottom while the message is generating

* The sidebar when pinned can now stay open with an active Canvas if enough space is available

* A new composer bar layout now fades content underneath it as you scroll with an updated look & feel

* The new chat button has been moved to the left of the Model Picker to be easier to access

* The system icon in conversations has been removed to make additional horizontal space

* DALL-E focused view has an updated layout

* GPT Creator has an updated layout

### **Improved Mobile Web Experience**

* The experience with the on-screen keyboard on mobile devices has been greatly improved across iOS & Android devices

* The new sidebar is always in floating mode and auto closes when switching threads

* We no longer focus the composer on mobile web when switching conversations

* An issue causing scroll to get stuck in certain situations should be resolved

# November 20, 2024

## Update to GPT-4o

We’ve updated GPT-4o for ChatGPT users on all paid tiers. This update to GPT-4o includes improved writing capabilities that are now more natural, audience-aware, and tailored to improve relevance and readability. This model is also better at working with uploaded files, providing deeper insights and more thorough responses.

# November 19, 2024

## Advanced Voice for ChatGPT Web

Starting today, we’re beginning to roll out Advanced Voice Mode on web (already available on mobile and desktop apps). Users can now start a voice chat on chatgpt.com on their desktop and have real-time, natural conversations with ChatGPT while doing tasks like planning, writing, and brainstorming.

# November 14, 2024

## Windows App

The improved Windows app is now available through the Microsoft Store for ChatGPT Enterprise and Edu workspaces. ChatGPT users that are familiar with our experience on the web can seamlessly integrate the Windows app into anything they’re doing on their computer.

User access to the ChatGPT Windows app will follow your IT admin’s policies for apps in the Microsoft Store. In the coming weeks, IT admins will also have the option to deploy the app to employee devices via MDM/MAM, rather than allowing direct downloads from the Store.

As with any ChatGPT Enterprise experience, user chat history is secure and will not be used to improve OpenAI's services.

Learn more about the [ChatGPT Windows app](/en/articles/9982051-using-the-chatgpt-windows-app).
