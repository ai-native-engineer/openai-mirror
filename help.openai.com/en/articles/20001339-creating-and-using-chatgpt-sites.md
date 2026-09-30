<!-- source: https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites -->

# Creating and using ChatGPT Sites

Create, edit, publish, share, and manage Sites in ChatGPT.

Updated: 8 hours ago

ChatGPT Sites lets you create, preview, publish, and share interactive websites and lightweight apps. You can create Sites in Work on ChatGPT web, and in Work or Codex in the ChatGPT desktop app.

In ChatGPT Business and Enterprise workspaces with connected-app access enabled, you can also build Sites that read information from supported connected apps, such as issue dashboards and document finders. Each visitor uses their own connected accounts and existing permissions.

To use Sites, ask ChatGPT to build a website and describe what you want it to do. You can also use **@Sites** in your prompt.

ChatGPT Sites is available in public beta for ChatGPT workspaces, Plus, and Pro accounts. If you do not see Sites, it may still be rolling out to your account. Workspace admins may control who can create and publish Sites. In Enterprise workspaces, public publishing is off by default and must be enabled by an admin before eligible members can publish publicly.

If you’re a ChatGPT workspace owner or admin, you can review [Managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338).

## Public beta limits

During the public beta, Sites usage is included up to plan-specific limits. ChatGPT will notify you as you approach a limit.

If you reach a beta limit, you may be unable to create a new Site, add storage, or keep a high-usage Site publicly available until usage is reduced. You can still edit and manage existing Sites.

Limits apply across all Sites on the account and may change during the public beta. Check the Sites experience for the limits currently shown for your plan or workspace.

Enterprise and Edu limits may vary by workspace.

# Create a Site

Start in Work on ChatGPT web, or in Work or Codex in the ChatGPT desktop app. Describe what you want to build and include the content, files, data, links, or constraints ChatGPT should use.

For example, you can ask ChatGPT to build dashboards, project trackers, launch calendars, prototypes, internal portals, and reports.

ChatGPT can help generate the website, provide a private preview of it for your review, and refine it based on your feedback.

For a detailed description of creating a site, including prompts, version controls, access and secrets, see the [ChatGPT Sites developer guide](https://developers.openai.com/codex/sites).

In Business workspaces, Sites is enabled by default. In Enterprise workspaces, an admin must enable Sites through role-based access controls. If you do not see Sites, ask your workspace admin whether it is enabled for your workspace or role.

**Note**: Sites is not available in the ChatGPT Classic app. Download the latest version of the ChatGPT app [here](https://chatgpt.com/download/).

## On web or the ChatGPT desktop app

1. On web, select Work. In the desktop app, select ChatGPT and then Work, or select Codex.
2. In the chat window, describe the website you want ChatGPT to build. Include the word “website” in your prompt, or mention @Sites.
3. Add the content, files, data, links, and constraints ChatGPT should use.
4. Review the preview ChatGPT generates.
5. Ask ChatGPT for changes until the Site is ready to share or publish.

When you deploy, ChatGPT generates a Site URL. Every deployment URL is a production URL. To review changes without updating the live Site, save a version first and deploy only after you have reviewed it.

## Build a Site with connected apps

Use connected apps to build a tool for a recurring task, such as tracking assigned issues or finding project documents.

Before you begin, confirm that connected-app access is enabled for your Business or Enterprise workspace and that you’ve connected the apps you want to use. Your workspace admin must turn on **Allow use in Sites** for each supported plugin.

1. Describe the tool you want to build, the connected apps it should use, and the information it should show. If you’re unsure which apps to use, ask ChatGPT which available apps could help.
2. Review the preview with your data. ChatGPT uses your available connections while building and previewing the Site. Ask for changes until the Site is ready to share.
3. Publish the Site privately for your workspace, then share the link with a teammate.
4. Ask your teammate to sign in, review the requested access, and choose their own connected account. Test that the Site shows the information they expect before sharing it more widely within the workspace.

For example, you can ask: “Build a Site using my connected issue tracker that shows issues assigned to me, grouped by priority. Add project filters and links to the original issues.”

Each visitor uses their own connected accounts and existing permissions. For the visitor authorization steps, see: [Use your connected apps in a Site](/en/articles/20001339-creating-and-managing-chatgpt-sites#use-your-connected-apps-in-a-site).

## Use a custom domain

Where custom domains are available, Sites does not register a domain for you. You must already own the domain and be able to change its DNS records. Custom domains are not available in Enterprise workspaces at launch.

To connect a custom domain:

1. Open the Site's settings and select **Add domain**.
2. Enter the apex domain or subdomain you want to use.
3. Copy the DNS records and values Sites provides, and add them through your domain provider.
4. Wait a few minutes, then refresh the domain status in Sites.

You can also ask ChatGPT to help point the domain at your Site. If browsing or computer use is enabled, ChatGPT can help you navigate the domain provider after you sign in.

## Use a Site to host a plugin

You can use ChatGPT Sites to host an MCP server that ChatGPT uses through a plugin. This lets you make a Site-backed workflow available from a conversation, subject to the Site, plugin and connected-service permissions that apply. Ask ChatGPT or Codex to add an **MCP server** to a new or existing Site, and describe the information the tools should read and any changes they should be able to make.

Read more: [Hosting a plugin with ChatGPT Sites.](https://help.openai.com/articles/20001547)

For plugin creation and installation, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

# Edit a Site

## On web or on the desktop app

1. Open the chat where the Site was created, or select Sites in the sidebar, locate the Site, and select the edit icon.
2. The composer will load with the Site already referenced within the chat.
3. Describe the change you want, such as changing copy, layout, data, styles, links, forms, or interactive behavior.
4. Review the updated preview.
5. Ask ChatGPT for any follow-up changes.
6. Publish the updated version only after you have reviewed it.

## Edit from your published Site

When the editing controls are available, you can start an edit from your published Site in a desktop browser. You must be signed in as the Site owner or an editor.

1. Open the published Site.
2. Select **Edit site**.
3. Describe the changes you want in **Describe your edits**.
4. Select **Send edits** to continue in ChatGPT with the Site and your instructions.
5. Review the updated preview, then publish the changes when they’re ready.

Sending instructions from the Site starts the editing workflow. It does not immediately change the published Site.

# Edit a Site with collaborators

A Site owner can give an active member of the same ChatGPT workspace **Can edit** access. An editor can update and save the shared Site. After the owner publishes the Site for the first time, an editor can publish later versions to the same Site URL.

## Give someone edit access

1. Open the Site and select **Share**.
2. Under **Who has access**, add or select an active member of the same workspace.
3. Change their access to **Can edit**.

The editor can open **Sites** and select **Shared with you** to find the Site. They can then open the Site, make changes, review the updated preview, and save a version. After the owner completes the first publish, the editor can publish later versions.

Only the owner can manage who has access, change the Site name or URL, transfer ownership, or configure owner-only settings such as secrets and custom domains. Before giving someone edit access, coordinate how changes will be reviewed. An editor can publish later versions without a separate owner-approval step.

## Change or remove edit access

1. Open the Site and select **Share**.
2. Under **Who has access**, find the editor.
3. Change their access to **Can view**, or remove them.

Changing or removing edit access stops the person from editing the Site. Whether they can still view it depends on the Site’s remaining audience settings.

If **Can edit** or **Shared with you** is not available, co-editing may not yet be available for your account. Contact your workspace owner or administrator to ensure that the Sites permission toggles are enabled for your user account.

# Review, share, and publish a Site

After creating a Site, open its preview and use the sharing controls available to your account. A new Site is limited to its owner and workspace admins until access is changed. Available access options depend on your plan and workspace settings.

## On web or the ChatGPT desktop app

1. Review the Site preview and check that it does not include information or content you do not want to share. You can also open Sites from the sidebar and locate the Site you want to share.
2. Select **Share**.
3. Under **Who has access**, choose one of the available options:

* Owner and workspace admins
* Selected active users or groups, and named external viewers (see section below).
* Anyone in the workspace, where supported
* Anyone on the internet, only when public publishing is enabled

1. Available sharing options and sign-in requirements depend on your account and workspace. Review the selected audience before publishing.
2. If you choose Anyone on the Internet, the Site will be publicly accessible. Carefully review your Site before proceeding.
3. Select Publish.
4. After the site is live, use **Visit** to open it or **Copy link** to share the URL.

## Share with someone outside your workspace

A Site owner can add a named person outside the workspace as a viewer. This does not give that person edit access or make the Site public.

1. Open the Site and select **Share**.
2. Use the available people or email control to enter the email address for the person you want to invite.
3. Review the recipient and their view-only access, then save the sharing change.
4. Confirm that the person appears in the Site's access list. Ask them to open the Site while signed in with the account that received access.

In Enterprise workspaces, permission to invite external viewers is required. If the external email option is missing or the invitation is rejected, check with your workspace owner or admin. Availability can also depend on the rollout and the surface you are using. Read more: [Managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338)

To remove an external viewer, remove that person from the Site's sharing controls and check the remaining audience settings. Other access, such as public or workspace-wide access, may still let someone view the Site. Review access from the intended visitor experience after changing it.

External viewers cannot edit or publish the Site. Sharing a Site also does not grant access to other workspace content or independently authorize services used by the Site.

# Schedule updates to a Site

When Site automations are available, you can create a cloud schedule for recurring work on a published Site. To link a schedule, you must own both the Site and the schedule.

1. Open your Site’s **Automations**.
2. Select **Create schedule**.
3. Review the task instructions and timing.
4. Confirm the schedule.

You can add more than one schedule to a Site. Site schedules run in the cloud, including schedules created on desktop.

ChatGPT may also suggest **Set up scheduled task** while you’re working on a Site. Review the instructions and timing before confirming. A suggestion does not create a schedule on its own.

## Manage a Site’s schedules

Open the Site’s **Automations** to find its linked schedules. Open a schedule in **Scheduled** to edit it, pause it, or resume it.

Scheduled tasks can’t use a visitor’s connected-app access from the Site. For recurring data updates, the cloud run needs access to the data source used by the task. Check that the required database or supported connection is available to the scheduled task.

# Take down a Site

## On web or on the ChatGPT desktop app

1. Open Sites from the sidebar.
2. If you want to change access to the site, you can use Share settings to restrict access to only a select set of people, or yourself.
3. If you want to permanently delete the site, select Delete site, and follow the instructions in the prompt.
4. Confirm that the Site is no longer available to the previous audience.

Note: Deleting a site permanently removes it, and you cannot restore deleted sites. To confirm deletion, type the Site slug in the dialog, then select Permanently delete.

# Understand sign-in on Sites

Sign-in behavior depends on the Site’s access settings and any authentication feature built into the Site. Before publishing, test the Site from the intended visitor experience and confirm that access matches your intended audience.

For limited sharing, invite supported users or groups through the Site’s access controls. Invited visitors must sign in with the account that received access.

A public Site is available without ChatGPT workspace access. A Site may also include its own sign-in feature when that feature is supported and intentionally added. A Site’s audience setting and an authentication feature inside the Site are separate controls.

Before you share or publish a Site, review its content, access setting, forms, sign-in behavior, files, links, and interactive features. Remove or change anything that should not be available to the intended audience.

If your Site uses Sign in with ChatGPT, explain what visitor information the Site receives and how it uses that information. You are responsible for complying with applicable privacy and data-protection laws.

## Use your connected apps in a Site

For ChatGPT Business and Enterprise customers, Sites can request read-only access to each visitor’s own connected apps with the required administrator approval and visitor authorization. A shared dashboard, for example, can retrieve live information using each visitor’s account and existing permissions.

When a Site requests connected-app access:

1. Sign in with the ChatGPT account you want to use.
2. Review the requested app access.
3. Choose the connected account and access you want to allow, then return to the Site.

Each visitor uses their own connected accounts and existing app permissions. Sharing a Site does not give other visitors access to your connected accounts. The Site can read information from your connected apps while you’re using it. It can’t use this access to change information in those apps or run scheduled tasks in the background.

Connected features require a Site that is private to a workspace and a visitor who belongs to that workspace. Permission to view a Site, including an invitation as an external viewer, does not independently authorize connected-app access.

You can continue without granting app access, but features that need it won’t work. Review the requested access before approving it: the Site will receive data from the apps you allow.

If the Site cannot use an app, confirm that you are using the correct account and have connected the app. Ask your workspace admin to confirm that **Allow use in Sites** is turned on for the app’s plugin and that the app is available in your workspace. Ask a global admin to check the organization’s approval for ChatGPT Sites.

For administrator checks, see: [Managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338).

# What to check before you share or publish

Before you share or publish a ChatGPT Site, check that it does not include confidential or sensitive data, or third-party content unless you have the right to share it.

Make sure the Site behaves the way you expect when opened by another user, the access setting matches your intended audience, your workspace admin allows public publishing if you are in a workspace, and you have reviewed any content, generated text or images, links, uploaded files, forms, and interactive behavior the Site includes. For example, you should review features that allow site visitors to provide personal information or other content, such as open-text fields, message boards, or sign-in functionality, and consider whether you want those features to be part of your Site and whether you want to collect, share, or publish that information. For more information about your obligations when collecting and processing personal data from others through a public Site, see [this article](https://help.openai.com/articles/20001340).

# Limits and unsupported uses

Sites is designed for web experiences that can be hosted through the supported Sites runtime. Some capabilities may not be supported at launch or may require a different product surface.

Supported capabilities depend on the Sites runtime and the features available to your account. Some frameworks, private networks, databases, background services, and hosting patterns may not be supported.

ChatGPT Sites does not support data residency or inference residency at launch. This includes deployed Sites, Site code, D1/R2 data and file storage, artifacts, and logs. Learn more in [Data residency and inference residency](https://help.openai.com/articles/9903489).

Sites must not process sensitive data such as Protected Health Information or payment-card data (unless solely through a third-party payment processor); target children under 13 or the applicable age of digital consent; distribute malware; enable phishing; impersonate people or organizations; or otherwise violate the OpenAI Usage Policies or ChatGPT Sites Terms.

If you want to sell goods or services or collect payments through your ChatGPT Site, you can do so by using a third-party payment processor. Please note that you are responsible for connecting, configuring, and maintaining any third-party payment processors you choose to use on your ChatGPT Site, and we are not responsible for payments processed through those providers. You are also responsible for any e-commerce activities and transactions with your users, including fulfillment, delivery, refunds, customer support, and any claims or warranties relating to what you sell, as well as for calculating, collecting, and remitting any related taxes and fees.

# FAQ

## Why can’t I use ChatGPT Sites?

Confirm that Sites is available for your plan, that rollout has reached your account, and that you are signed in to the correct workspace. Sites is not available on Free or Go. In Enterprise, ask an admin whether Sites is enabled for your role.

## I’m in an Enterprise workspace. Why can’t I publish a ChatGPT Site I created to the public?

In Enterprise workspaces, public publishing is off by default. An admin must enable public publishing and grant the appropriate role access before members can publish publicly.

## Why can’t I access a ChatGPT Site?

A Site must be shared with you, available to your workspace, or published publicly before you can access it. You may need to sign in to the account or workspace that has access, when prompted.

## Why was my site taken down?

OpenAI may remove or restrict a Site if there is a risk that it violates OpenAI policies or platform safety requirements. If you believe your Site was removed in error, please submit an appeal using the link in the email notification you received. This helps us route your request correctly and review it more efficiently.

If you can’t access that email, you can submit an appeal through our intake [form](https://openai.com/form/appeal/).

If you are part of a Business or Enterprise workspace, your workspace owner or admin may also disable Sites created in that workspace. Contact your workspace owner or admin for details.

## How do I report or request takedown of a ChatGPT Site?

If you believe a Site violates OpenAI policies, report it using the [content reporting form](https://help.openai.com/articles/10245791). Include the full Site URL and enough detail to identify the issue.

## What information does a Site use?

Depending on how you create and publish a Site, Sites can include information from ChatGPT prompts, instructions, conversation context, uploaded or referenced files, site code, generated artifacts, hosted URLs, access settings, storage, metadata, logs, and operational data needed to host, secure, debug, or enforce policy on the Site.

## Does OpenAI use information from ChatGPT Sites to train its models?

The following information applies to your conversations with ChatGPT, including conversations where you create, design, or edit a Site or ask ChatGPT to retrieve information from one.

For ChatGPT Business and Enterprise/Edu customers: OpenAI does not use these conversations or the Site information included in them to train its models by default.

For ChatGPT Free, Go, Plus, and Pro users: OpenAI may use your conversations with ChatGPT to train our models if your “Improve the model for everyone” setting is on, which includes conversations where you use ChatGPT to create, design, edit, or manage a Site. For example, if you ask ChatGPT to edit a published Site or retrieve information from it, ChatGPT may bring relevant information from the Site into your conversation to help complete your request. You should only ask ChatGPT to use information that you have permission to provide. You can read more about how your data is stored and used in [Data Controls FAQ](https://help.openai.com/articles/7730893) in our help center.
