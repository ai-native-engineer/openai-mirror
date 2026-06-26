<!-- source: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan -->

# Using Codex with your ChatGPT plan

How to access and get started with Codex

Updated: 2 days ago

***Note:*** This article provides an overview of Codex, our coding agent. For additional technical details, please view our [Codex page](https://developers.openai.com/codex/).  
  
  
*For information on ChatGPT features such as Sora, ChatGPT Images, or Voice mode, please refer to other articles in our Help Center.*  
  
*Codex is included across Free, Go, Plus, Pro, Business, Edu, and Enterprise plans. Usage limits and credit options vary by plan.*

# What is Codex?

Codex is an AI agent that helps you write, review, and ship code.

# Getting started

## How to connect Codex with your ChatGPT account

To start using Codex with your ChatGPT plan:  
  
Sign in with your ChatGPT account.  
  
Codex is included in eligible ChatGPT plans, including Free. Usage limits vary by plan.  
  
For more information, including higher-usage options for individuals and Codex credit plans for business users, visit [**chatgpt.com/pricing**](https://chatgpt.com/pricing).  
  
Launch your preferred Codex client and follow the instructions to sign in with ChatGPT:

* [Codex app](http://developers.openai.com/codex/app)
* [Codex CLI](https://developers.openai.com/codex/cli)
* [Codex IDE extension](http://developers.openai.com/codex/ide)
* [Codex web](https://chatgpt.com/codex)

* Requires connecting ChatGPT to your GitHub account

## What terms govern your use of Codex?

When you sign in to Codex using an existing ChatGPT account, the ChatGPT [Terms of Use](https://openai.com/policies/row-terms-of-use/) and [Privacy Policy](https://openai.com/policies/privacy-policy/)—or the corresponding [online services agreement](https://openai.com/policies/services-agreement/) for OpenAI API and ChatGPT Enterprise, Education or Business Users—apply to data shared between Codex and ChatGPT.

## Enterprise setup and controls

### Setup

For an in-depth guide to get your workspace up and running with Codex, please refer to our  
  
guide here: [Enterprise Admin Guide](https://developers.openai.com/codex/enterprise)

### Plugins

For Business and Enterprise/Edu workspaces, access to plugins follows workspace app controls. To disable a plugin, admins/owners can disable the corresponding app from Workspace settings > Apps, or use the Manage actions menu to determine which actions the plugin is allowed to have. Additionally, Enterprise/Edu admins/owners can use [RBAC](/en/articles/11750701-rbac) control which users get access to the app or plugin. Note that controls apply to all surfaces (ChatGPT web, Atlas, ChatGPT mobile and Codex) - it is not currently possible to enable the app and corresponding plugin in one surface, but not others.

### Sites in Codex

ChatGPT Sites is available in preview for eligible Business and Enterprise workspaces, as a plugin within Codex. Business workspaces have Sites enabled by default - for Enterprise workspaces, the feature is available as a toggle in the Early Access section.  
  
Use Sites from Codex to create and deploy workspace-internal web apps with Sign in with ChatGPT access. After creating a site, you can invite users within the workspace to access your site. For the full build, deployment, storage, and access-mode workflow, see the [Codex Sites developer guide](https://developers.openai.com/codex/sites).  
  
Admins and owners can control sites from:

* Go to **Workspace settings > Permissions & Roles**, and enable or disable the Sites toggle. This will allow users to use the sites plugin in Codex to create custom sites, and share it to other users within their workspace.

* Go to **Workspace settings > Sites** to disable an existing site. Use this if you want to take down a previously created site.

### Developer mode for Browser use and in-app browser

Developer mode works with Browser use in Chrome and the Codex in-app browser. It gives Codex controlled access to Chrome DevTools Protocol (CDP) for deeper browser debugging, such as inspecting console output, network traffic, page state, and JavaScript performance.  
  
User can enable the feature locally within the Codex app, by selecting **Settings > Browser** and turn on **Enable full CDP access** under **Developer mode**. Full CDP access lets Codex inspect and control sensitive browser internals that may put your data at risk, and Codex asks for explicit approval before it uses full CDP access to inspect a website.

Admins/owners can turn off the feature for their workspace by accessing the **Policies & Configurations**  in [Codex cloud settings](https://chatgpt.com/codex/cloud/settings/), and by setting `browser_use_full_cdp_access` to false. Disabling Browser use overall will disable CDP, as well.   
  
For setup and approval details, see [Developer mode](https://developers.openai.com/codex/app/browser#developer-mode). Note admins/owners will first need to enable the [in-app browser](https://developers.openai.com/codex/app/browser) before enabling developer mode.

### RBAC (Role-based access control)

Access to Codex is able to be granted to specific user roles. For more information on setting up RBAC, please refer to our guide here: [RBAC](/en/articles/11750701-rbac)

### Compliance API

Codex usage, including local clients such as the CLI and IDE extension as well as web or cloud-delegated usage, is available in the [**Compliance API**](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks). This log surface covers supported Codex clients, separate from cloud-task-specific endpoints.

# Usage limits by plan

Codex usage limits depend on your plan and count toward your agentic usage limit. Usage from Codex, ChatGPT for Excel, and Workspace Agents counts toward agentic usage. The number of Codex messages you can send within these limits varies based on the size and complexity of your coding tasks, and where you execute tasks. Small scripts or simple functions may only consume a fraction of your allowance, while larger codebases, long running tasks, or extended sessions that require Codex to hold more context will use significantly more per message.  
  
If you are nearing or have reached your Codex limit, check the Codex usage page or the limit banner for the options available on your plan. Some Plus and Pro users can add credits to continue using Codex; other users may need to upgrade or wait for the limit to reset.  
  
For a full list of Codex limits, rates, and credit options, refer to the [**pricing page**](https://developers.openai.com/codex/pricing) on the OpenAI developer website.

# Context and Data Controls

Some Codex features can make Codex more helpful by letting it remember context, continue work over time, and connect with tools you choose to use. These include [Memories](https://developers.openai.com/codex/memories), [Automations](https://developers.openai.com/codex/app/automations), Codex’s [in-app browser](https://developers.openai.com/codex/app/browser), and [Computer Use](https://developers.openai.com/codex/app/computer-use). For more information on these and other features, including how to manage the data that these features store and interact with, see our [developer center](https://developers.openai.com/codex).

## Record & Replay

Record & Replay is available in the Codex app on macOS for eligible users. It lets you demonstrate a workflow once and turn it into a reusable skill. It is useful for stable, repeatable workflows that are easier to show than describe.

Record & Replay requires Computer Use to be available and enabled, and initial availability excludes the European Union, Switzerland and the UK. During recording, Codex observes the actions and window content needed to learn the workflow. Keep recordings focused on the task, and avoid entering secrets or sensitive data during the recording.

To learn more, see the [Record & Replay guide](https://developers.openai.com/codex/record-and-replay).

## Data controls

Your ChatGPT training data controls apply to whether content processed through Codex may be used to improve OpenAI’s models. This includes screenshots taken by Computer Use. [Learn more](/en/articles/7730893-data-controls-faq).  Your ChatGPT and Codex conversations remain separate, but some settings and connected services may carry over between them. For example, if you connect Google Drive in ChatGPT, it will also be available in Codex. You can disconnect connected services at any time.

# FAQ

## Which model does the Codex CLI or IDE extension use?

The model Codex uses by default will depend on your version of the CLI or IDE extension and configuration. Check out the [Codex documentation](https://developers.openai.com/codex/models) for available models and how to configure different models.

## Does OpenAI train on my Codex usage?

### Business, Enterprise, and Edu

By default, OpenAI does not use any inputs or outputs from our products for business users, including ChatGPT Business, ChatGPT Enterprise, and the API, to improve our models. However, API organization owners can choose to opt-in to share API data with OpenAI. This setting is not available to certain organizations, including Enterprise and customers with Zero Data Retention enabled.  
  
Learn more about [Sharing feedback, evaluation and fine-tuning data, and API inputs and outputs with OpenAI](/en/articles/10306912-sharing-feedback-evaluation-and-fine-tuning-data-and-api-inputs-and-outputs-with-openai).

### Pro and Plus

Conversations may be used to improve models unless you turn off training in [ChatGPT data controls](https://chatgpt.com/#settings/DataControls). For more information, see [how your data is used to improve model performance](/en/articles/5722486-how-your-data-is-used-to-improve-model-performance).

## Can I run Codex in my IDE?

Yes, the Codex VS Code extension is compatible with most VS Code forks. For other IDEs, you can also run the Codex CLI in the IDE’s terminal.

## Are there separate workspace permissions needed for Codex app?

No. The Codex app follows the same workspace controls as other Codex surfaces. Codex Local controls local use (CLI, IDE extension, and app local workflows), while Codex Cloud controls whether members can run delegated cloud tasks across supported cloud surfaces. To connect to and control a Codex app environment from another Codex client, admins or owners may need to enable Remote Control for the workspace or grant the Remote Control permission through RBAC. The device you want to control must also allow remote control in Codex app settings by turning on Allow this device to be discovered and controlled.

For an in-depth guide to get your workspace up and running with Codex, please refer to our guide here: [**Enterprise Admin Guide**](https://developers.openai.com/codex/enterprise)

## Where can I find more info for troubleshooting Codex app issues?

Refer to our [platform guide](https://developers.openai.com/codex/app/troubleshooting) if you run into issues with using the Codex app. If you need additional help, [contact us](/en/articles/6614161-how-can-i-contact-support).

## How can I get access to Codex Enterprise Analytics?

Access to Codex Enterprise Analytics is available to Enterprise workspaces with Codex enabled. To use the Codex Enterprise Analytics API, use an organization API key that has Codex Enterprise Analytics access. If your API request is rejected because the key is missing access, ask your workspace or organization administrator to provide a key with Codex Enterprise Analytics access.  
  
For setup details and API access, refer to our [**API documentation**](https://chatgpt.com/codex/settings/apireference).

## Do ChatGPT related rate limits for file upload limits, image limits and voice caps apply to Codex?

ChatGPT file uploads, image generation, or voice have separate usage limits, reset periods, and banners. For example, if you see banners like “50 images in the last day”, “resets in 720 hours”, reach voice caps, or see upload-limit banners while uploading files in ChatGPT, those limits do not apply to Codex.  
  
For details on image and video limits and voice limits, see [image & video generation limits](/en/articles/8852938-image-and-video-generation-limits) and [voice usage limits](/en/articles/8918662-voice-mode-limits). For information about ChatGPT file upload limits and troubleshooting, see [File Uploads FAQ](/en/articles/8555545-file-uploads-faq). For information on the status of various ChatGPT services, including file uploads, refer to the [OpenAI status page](https://status.openai.com/).

## How do Codex referral invitations and banked resets work?

Eligible users may see Codex referral invitations in the profile menu. Personal plan users may see **Invite a friend**, and eligible Business workspace members may see **Invite a coworker**. The invitation dialog shows the current reward, recipient requirements, invite limits, and expiration for that offer.  
  
For some Plus and Pro promotions, a successful referral can add a banked Codex rate-limit reset. To use a banked reset, open the profile menu and select the usage summary showing the available reset count, such as **1 reset available**.  
  
Referral rewards vary by offer and plan. For current reward, limit, and eligibility details, see [Invite friends and coworkers](https://developers.openai.com/codex/pricing#invite-friends-and-coworkers) and [Codex Referral Promotions](https://help.openai.com/articles/20001271).

## How can I create project instructions in the Codex app?

Use `/init` in the Codex app composer to generate an `AGENTS.md` scaffold for the current project. This uses the same initialization workflow as the Codex CLI. For other app commands, see [App commands](https://developers.openai.com/codex/app/commands).

## What happens if I reach a usage limit while Codex is working?

If you reach a usage limit during an active turn, Codex can continue working on that turn, subject to fair-use limits. After that turn, check the Codex usage page or the limit banner for the options available on your plan, such as adding credits, applying an available reset, upgrading, or waiting for the limit to reset.  
  
For more details, see [Codex usage limits](https://developers.openai.com/codex/pricing#what-happens-when-you-hit-usage-limits).
