<!-- source: https://help.openai.com/en/articles/20001339-creating-and-managing-chatgpt-sites -->

# Creating and managing ChatGPT Sites

Create, edit, publish, share, and manage Sites in ChatGPT.

Updated: 2 days ago

ChatGPT Work is gradually rolling out to eligible accounts over the coming days. If you don't see ChatGPT Work in your account yet, your account may not have access yet. Availability will continue to expand as the rollout progresses.

# Overview

ChatGPT Sites lets you create, preview, publish, and share interactive websites and lightweight apps. You can create Sites in Work on ChatGPT web, and in Work or Codex in the ChatGPT desktop app.  
  
To use Sites, simply ask ChatGPT to build you a website with a description of what you want the website to do. You can also use **@Sites** in your prompt to specifically trigger building a website.

# ChatGPT Sites availability

ChatGPT Sites is available in public beta on paid plans except Free and Go. It is not available in the EEA, Switzerland, or the United Kingdom at launch. Pro, Pro Lite, Enterprise, and Edu receive Sites first; Plus and Business follow over the coming days. If you do not see Sites, it may still be rolling out to your account. Workspace admins may control who can create and publish Sites. In Enterprise workspaces, public publishing is off by default and must be enabled by an admin before eligible members can publish publicly.  
  
If you’re a ChatGPT workspace owner or admin, you can review [Managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338).

## Public Beta Limits

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

## Use a custom domain

Where custom domains are available, Sites does not register a domain for you. You must already own the domain and be able to change its DNS records. Custom domains are not available in Enterprise workspaces at launch.  
  
To connect a custom domain:

1. Open the Site's settings and select **Add domain**.
2. Enter the apex domain or subdomain you want to use.
3. Copy the DNS records and values Sites provides, and add them through your domain provider.
4. Wait a few minutes, then refresh the domain status in Sites.

You can also ask ChatGPT to help point the domain at your Site. If browsing or computer use is enabled, ChatGPT can help you navigate the domain provider after you sign in.

# Edit a Site

## On web or on the desktop app

1. Open the chat where the Site was created, or select Sites in the sidebar, locate the Site, and select the edit icon.
2. The composer will load with the Site already referenced within the chat.
3. Describe the change you want, such as changing copy, layout, data, styles, links, forms, or interactive behavior.
4. Review the updated preview.
5. Ask ChatGPT for any follow-up changes.
6. Publish the updated version only after you have reviewed it.

# Review, share and publish a Site

After creating a Site, open its preview and use the sharing controls available to your account. A new Site is limited to its owner and workspace admins until access is changed. Available access options depend on your plan and workspace settings.

## On web or on the ChatGPT Desktop App

1. Review the Site preview and check that it does not include information or content you do not want to share. You can also open Sites from the sidebar and locate the Site you want to share.
2. Select **Share**.
3. Under **Who has access**, choose one of the available options:

   * Owner and workspace admins
   * Selected active users or groups, where supported
   * Anyone in the workspace, where supported
   * Anyone on the internet, only when public publishing is enabled
4. Available sharing options and sign-in requirements depend on your account and workspace. Review the selected audience before publishing.
5. If you choose Anyone on the Internet, the Site will be publicly accessible. Carefully review your Site before proceeding.
6. Select Publish.
7. After the site is live, use **Visit** to open it or **Copy link** to share the URL.

# Take down a Site

## On web or on the ChatGPT desktop app

1. Open Sites from the sidebar.
2. If you want to change access to the site, you can use Share settings to restrict access to only a select set of people, or yourself.
3. If you want to permanently delete the site, click Delete site, and follow the instructions in the prompt.
4. Confirm that the Site is no longer available to the previous audience.

Note: Deleting a site permanently removes it, and you cannot restore deleted sites. To confirm deletion, type the Site slug in the dialog, then select Permanently delete.

# How sign-in work on Sites

Sign-in behavior depends on the Site’s access settings and any authentication feature built into the Site. Before publishing, test the Site from the intended visitor experience and confirm that access matches your intended audience.  
  
For limited sharing, invite supported users or groups through the Site’s access controls. Invited visitors must sign in with the account that received access.  
  
A public Site is available without ChatGPT workspace access. A Site may also include its own sign-in feature when that feature is supported and intentionally added. A Site’s audience setting and an authentication feature inside the Site are separate controls.  
  
Before you share or publish a Site, review its content, access setting, forms, sign-in behavior, files, links, and interactive features. Remove or change anything that should not be available to the intended audience.  
  
If your Site uses Sign in with ChatGPT, explain what visitor information the Site receives and how it uses that information. You are responsible for complying with applicable privacy and data-protection laws.

# What to check before you share or publish

Before you share or publish a ChatGPT Site, check that it does not include confidential or sensitive data, or third-party content unless you have the right to share it.  
  
Make sure the Site behaves the way you expect when opened by another user, the access setting matches your intended audience, your workspace admin allows public publishing if you are in a workspace, and you have reviewed any content, generated text or images, links, uploaded files, forms, and interactive behavior the Site includes. For example, you should review features that allow site visitors to provide personal information or other content, such as open-text fields, message boards, or sign-in functionality, and consider whether you want those features to be part of your Site and whether you want to collect, share, or publish that information. For more information about your obligations when collecting and processing personal data from others through a public Site, see [this article](https://help.openai.com/articles/20001340).

# Limits and unsupported uses

Sites is designed for web experiences that can be hosted through the supported Sites runtime. Some capabilities may not be supported at launch or may require a different product surface.  
  
Supported capabilities depend on the Sites runtime and the features available to your account. Some frameworks, private networks, databases, background services, and hosting patterns may not be supported.  
  
ChatGPT Sites does not support data residency or inference residency at launch. This includes deployed Sites, Site code, D1/R2 data and file storage, artifacts, and logs. Learn more in [Data residency and inference residency](/en/articles/9903489-data-residency-and-inference-residency).  
  
Sites must not process Protected Health Information or payment-card data; target children under 13 or the applicable age of digital consent; enable financial transactions; distribute malware; enable phishing; impersonate people or organizations; or otherwise violate the OpenAI Usage Policies or ChatGPT Sites Terms.

# FAQ

## Why can’t I use ChatGPT Sites?

Confirm that Sites is available for your plan and region, that rollout has reached your account, and that you are signed in to the correct workspace. Sites is not available on Free or Go, or in the EEA, Switzerland, or the United Kingdom at launch. In Enterprise, ask an admin whether Sites is enabled for your role.

## I’m in an Enterprise workspace. Why can’t I publish a ChatGPT Site I created to the public?

In Enterprise workspaces, public publishing is off by default. An admin must enable public publishing and grant the appropriate role access before members can publish publicly.

## Why can’t I access a ChatGPT Site?

A Site must be shared with you, available to your workspace, or published publicly before you can access it. You may need to sign in to the account or workspace that has access, when prompted.

## Why was my site taken down?

OpenAI may remove or restrict a Site if there is a risk that it violates OpenAI policies or platform safety requirements. If you believe your Site was removed in error, please submit an appeal using the link in the email notification you received. This helps us route your request correctly and review it more efficiently.  
  
If you can’t access that email, you can submit an appeal through our intake [form](https://openai.com/form/appeal/).  
  
If you are part of a Business or Enterprise workspace, your workspace owner or admin may also disable Sites created in that workspace. Contact your workspace owner or admin for details.

## How do I report or request takedown of a ChatGPT Site?

If you believe a Site violates OpenAI policies, report it using the [content reporting form](/en/articles/10245791). Include the full Site URL and enough detail to identify the issue.

## What information does a Site use?

Depending on how you create and publish a Site, Sites can include information from ChatGPT prompts, instructions, conversation context, uploaded or referenced files, site code, generated artifacts, hosted URLs, access settings, storage, metadata, logs, and operational data needed to host, secure, debug, or enforce policy on the Site.

## Does OpenAI use information from ChatGPT Sites to train its models?

Your conversations with ChatGPT follow your existing data controls, including conversations where you create, design, or edit a Site or ask ChatGPT to retrieve information from one.  
  
For ChatGPT Business and Enterprise/Edu customers: OpenAI does not use your conversations with ChatGPT or information accessed from Sites to train its models by default.  
  
For ChatGPT Free, Go, Plus, and Pro users: OpenAI may use your conversations with ChatGPT to train our models if your “Improve the model for everyone” setting is on, which includes conversations where you use ChatGPT to create, design, edit, or manage a Site. For example, if you ask ChatGPT to edit a published Site or retrieve information from it, ChatGPT may bring relevant information from the Site into your conversation to help complete your request. You should only ask ChatGPT to use information that you have permission to provide. You can read more about how your data is stored and used in [this article](https://help.openai.com/articles/7730893) in our help center.
