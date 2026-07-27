<!-- source: https://learn.chatgpt.com/docs/pricing -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionOverview

**ChatGPT Work and Codex share usage.** ChatGPT Work usage inside
ChatGPT uses the same pricing, credits, and usage limits as Codex.

## Pricing options

IndividualBusiness / Enterprise

### Free

Explore Codex capabilities on quick coding tasks.

$0/month

[Get Free](https://chatgpt.com/plans/free/)

### Go

Use Codex for lightweight coding tasks.

$8/month

[Get Go](https://chatgpt.com/plans/go)

### Plus

Power a few focused coding sessions each week.

$20/month

[Get Plus](https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex)

* Codex on the web, in the CLI, in the IDE extension, and on iOS
* Cloud-based integrations like automatic code review and Slack
  integration
* The GPT-5.6 model family, including Sol, Terra, and Luna
* GPT-5.6 Luna for higher usage limits on lighter-weight or high-volume
  workloads
* Flexibly extend usage with [ChatGPT credits](#credits-overview)
* Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
  Plus plan

### Pro

Choose 5x or 20x higher rate limits than Plus.

From

$100/month

[Get Pro](https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex)

Everything in Plus and:

* Access to GPT-5.3-Codex-Spark (research preview), a fast Codex model
  for day-to-day coding tasks
* 5x or 20x more Codex usage than Plus\*
* Unlimited ChatGPT Voice on the $200/month tier; tasks still draw from
  your Codex usage budget
* Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
  Pro plan

[\*Learn more about limits on both tiers.](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-plans)

### API Key

Great for automation in shared environments like CI.

[Learn more](/codex/auth)

* Codex in the CLI, SDK, or IDE extension
* No cloud-based features (GitHub code review, Slack, etc.)
* Model availability follows the API models available to your key
* Pay only for the tokens Codex uses, based on [API
  pricing](https://platform.openai.com/docs/pricing)

### Business

Bring Codex into your startup or growing business.

$20/ user / month\*

[Get Business](https://chatgpt.com/team-sign-up)

* Access ChatGPT and Codex across desktop and mobile apps
* Larger virtual machines to run cloud chats faster
* Flexibly extend usage with [ChatGPT credits](#credits-overview)
* A secure, dedicated workspace with essential admin controls, SAML SSO,
  and MFA
* No training on your business data by default. [Learn
  more](https://openai.com/business-data/)
* Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
  Business plan

\*2+ users, billed annually. $25 per user per month when billed monthly.

### Enterprise & Edu

Unlock Codex for your entire organization with enterprise-grade functionality.

[Contact sales](https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex)

Everything in Business and:

* Priority request processing
* Enterprise-level security and controls, including SCIM, EKM, user
  analytics, domain verification, and role-based access control
  ([RBAC](https://help.openai.com/en/articles/11750701-rbac))
* Audit logs and usage monitoring via the [Compliance
  API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)
* Data retention and data residency controls
* Other [ChatGPT features](https://chatgpt.com/pricing) as part of the
  Enterprise plan

### API Key

Great for automation in shared environments like CI.

[Learn more](/codex/auth)

* Codex in the CLI, SDK, or IDE extension
* No cloud-based features (GitHub code review, Slack, etc.)
* Model availability follows the API models available to your key
* Pay only for the tokens Codex uses, based on [API
  pricing](https://platform.openai.com/docs/pricing)

## Invite friends and coworkers

Eligible users can send Codex invitations from the profile menu in the
lower-left corner of the app. Choose **Invite a friend** on an eligible personal
plan or **Invite a coworker** in an eligible Business workspace, enter the
recipient’s email address, and send the invitation.

The invitation dialog shows the current reward, recipient requirements, invite
limits, and when rewards expire for your plan or promotion. Personal and
Business referral programs have separate rewards and eligibility rules.
Referrals aren’t currently available for ChatGPT Enterprise.

From June 11 through June 24, 2026, eligible Plus and Pro users can invite up to
three friends. When an eligible recipient sends their first Codex message, both
people receive a banked rate-limit reset. Banked rate-limit resets are usable for
30 days after they’re granted. Business referrals use separate shared-workspace
credit rewards; review the
[current terms](https://help.openai.com/en/articles/20001271) before you send an
invitation.

## Frequently asked questions

### How much does Sites cost?

[Sites](/codex/sites) is included with eligible ChatGPT plans during public
beta. Availability depends on your plan, region, and workspace settings.

### What are the usage limits for my plan?

The number of messages you can send depends on the model used, size and
complexity of your tasks, and whether you run them locally or in the cloud.
Small scripts or routine functions may consume only a fraction of your
allowance, while larger projects, long-running tasks, or extended sessions that
require the agent to hold more context will use significantly more per message.

Tasks that look similar can consume different amounts of your allowance. Model
choice, context, reasoning, tool use, retrieval, and caching all affect usage,
so prompt length alone isn’t a reliable estimate.

Choose the GPT-5.6 model that best fits your work:

* **Sol** is the best choice when quality and reasoning depth matter most. Use
  it for complex analysis, coding, research, and advanced workflows.
* **Terra** is the everyday default: strong capability with a better balance of
  performance and price.
* **Luna** is optimized for speed and affordability, making it a good fit for
  lighter-weight or high-volume workloads.

PlusPro 5xPro 20xBusinessAPI Key

Plus

|  | Local Messages[\*](#shared-limits-plus) / 5h | Cloud chats[\*](#shared-limits-plus) / 5h | Code Reviews / 5h |
| --- | --- | --- | --- |
| GPT-5.6 Sol | 15-90 | Not available | Not available |
| GPT-5.6 Terra | 20-110 | Not available | Not available |
| GPT-5.6 Luna | 50-280 | Not available | Not available |
| GPT-5.5 | 15-80 | Not available | Not available |
| GPT-5.4 | 20-100 | Not available | Not available |
| GPT-5.4 mini | 60-350 | Not available | Not available |
|  |  |  |  |
| --- | --- | --- | --- |
| \*The usage limits for local messages and cloud chats share a **five-hour window**. Additional weekly limits may apply. | | | |
| For Enterprise/Edu users with flexible pricing, there are no fixed rate limits - usage scales with [credits](#credits-overview) | | | |
| Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features | | | |

Pro 5x

|  | Local Messages[\*](#shared-limits-pro) / 5h | Cloud chats[\*](#shared-limits-pro) / 5h | Code Reviews / 5h |
| --- | --- | --- | --- |
| GPT-5.6 Sol | 75-450 | Not available | Not available |
| GPT-5.6 Terra | 100-550 | Not available | Not available |
| GPT-5.6 Luna | 250-1400 | Not available | Not available |
| GPT-5.5 | 75-400 | Not available | Not available |
| GPT-5.4 | 100-500 | Not available | Not available |
| GPT-5.4 mini | 300-1750 | Not available | Not available |
|  |  |  |  |
| --- | --- | --- | --- |
| \*The usage limits for local messages and cloud chats share a **five-hour window**. Additional weekly limits may apply. | | | |
| For Enterprise/Edu users with flexible pricing, there are no fixed rate limits - usage scales with [credits](#credits-overview) | | | |
| Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features | | | |

Pro 20x

|  | Local Messages[\*](#shared-limits-pro-20x) / 5h | Cloud chats[\*](#shared-limits-pro-20x) / 5h | Code Reviews / 5h |
| --- | --- | --- | --- |
| GPT-5.6 Sol | 300-1800 | Not available | Not available |
| GPT-5.6 Terra | 400-2200 | Not available | Not available |
| GPT-5.6 Luna | 1000-5600 | Not available | Not available |
| GPT-5.5 | 300-1600 | Not available | Not available |
| GPT-5.4 | 400-2000 | Not available | Not available |
| GPT-5.4 mini | 1200-7000 | Not available | Not available |
|  |  |  |  |
| --- | --- | --- | --- |
| \*The usage limits for local messages and cloud chats share a **five-hour window**. Additional weekly limits may apply. | | | |
| For Enterprise/Edu users with flexible pricing, there are no fixed rate limits - usage scales with [credits](#credits-overview) | | | |
| Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features | | | |

Business

|  | Local Messages[\*](#shared-limits-business) / 5h | Cloud chats[\*](#shared-limits-business) / 5h | Code Reviews / 5h |
| --- | --- | --- | --- |
| GPT-5.6 Sol | 15-90 | Not available | Not available |
| GPT-5.6 Terra | 20-110 | Not available | Not available |
| GPT-5.6 Luna | 50-280 | Not available | Not available |
| GPT-5.5 | 15-80 | Not available | Not available |
| GPT-5.4 | 20-100 | Not available | Not available |
| GPT-5.4 mini | 60-350 | Not available | Not available |
|  |  |  |  |
| --- | --- | --- | --- |
| \*The usage limits for local messages and cloud chats share a **five-hour window**. Additional weekly limits may apply. | | | |
| For Enterprise/Edu users with flexible pricing, there are no fixed rate limits - usage scales with [credits](#credits-overview) | | | |
| Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features | | | |

API Key

|  | Local Messages[\*](#shared-limits-api-key) / 5h | Cloud chats[\*](#shared-limits-api-key) / 5h | Code Reviews / 5h |
| --- | --- | --- | --- |
| GPT-5.6 Sol | [Usage-based](https://platform.openai.com/docs/pricing) | Not available | Not available |
| GPT-5.6 Terra | [Usage-based](https://platform.openai.com/docs/pricing) | Not available | Not available |
| GPT-5.6 Luna | [Usage-based](https://platform.openai.com/docs/pricing) | Not available | Not available |
| GPT-5.5 | [Usage-based](https://platform.openai.com/docs/pricing) | Not available | Not available |
| GPT-5.4 | [Usage-based](https://platform.openai.com/docs/pricing) | Not available | Not available |
| GPT-5.4 mini | [Usage-based](https://platform.openai.com/docs/pricing) | Not available | Not available |
|  |  |  |  |
| --- | --- | --- | --- |
| \*The usage limits for local messages and cloud chats share a **five-hour window**. Additional weekly limits may apply. | | | |
| For Enterprise/Edu users with flexible pricing, there are no fixed rate limits - usage scales with [credits](#credits-overview) | | | |
| Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features | | | |

Usage limits are shared with other agentic features once pricing for those
features is effective. This currently includes [ChatGPT for
Excel](https://help.openai.com/articles/20001063) on Plus and Pro.

Speed configurations increase credit consumption for all applicable models, so
they also use included limits faster. Fast mode consumes credits at a higher
rate for supported models. See [Speed](/codex/agent-configuration/speed) for supported models and
rates. Image generations also use included limits ~3-5x faster on average,
depending on image quality and size. GPT-5.3-Codex-Spark is in research preview
for ChatGPT Pro users only, and isn’t available in the API at launch. Because it
runs on specialized low-latency hardware, usage is governed by a separate usage
limit that may adjust based on demand.

### ChatGPT Voice in Desktop

ChatGPT Voice on desktop uses a separate, plan-dependent allowance measured in
rolling five-hour windows. Tasks started through Voice use your existing Codex
usage budget. ChatGPT notifies you when you reach either limit.

ChatGPT Voice in Desktop uses a duplex model: GPT-Live manages the live
conversation, while GPT-5.6 Terra starts and coordinates tasks in the app.

* **Plus:** Approximately 15–30 minutes
* **Pro 5x ($100/month):** Approximately 1–2.5 hours
* **Pro 20x ($200/month):** Unlimited voice access
* **Business:** Approximately 45 minutes
* **Enterprise / Edu (legacy):** Approximately 45 minutes

Unlimited voice access doesn’t make Codex tasks unlimited. Tasks started through
ChatGPT Voice continue to use your existing Codex usage budget.

For Business, Edu, and Enterprise workspaces with credit-based or pay-as-you-go
billing, Desktop voice costs approximately 6 credits per minute. ChatGPT Voice
in Desktop is not available via API Key currently.

### What happens when you hit usage limits?

We want you to be able to complete work already in progress. If you reach your
usage limits during an active turn, the agent will be able to continue working
on that turn, subject to fair use limits.

ChatGPT Plus and Pro users who reach their usage limit can purchase additional
credits to continue working without needing to upgrade their existing plan.

Business, Edu, and Enterprise plans with [flexible
pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)
can purchase additional workspace credits to continue working.

If you are approaching usage limits, you can also switch to a smaller model to
make your usage limits last longer.

All users may also run extra local chats using an API key, with usage charged at
[standard API rates](https://platform.openai.com/docs/pricing).

### How does image generation count toward usage limits?

Image generation counts toward the same general usage limits as local
messages and cloud chats. Image generations use included limits 3-5x faster on
average than similar turns without image generation, depending on
image quality and size. After you reach your included limits, image generation
also draws from [credits](#credits-overview).

Image generation isn’t available on the Free plan. When you use Codex with an
API key, API pricing applies to image generation instead of included ChatGPT
usage limits.

### Where can I see my current usage limits?

You can find your current limits in the [usage
dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your
remaining limits during an active Codex CLI session, you can use `/status`.

Check the dashboard every week or two to understand your pace and remaining
capacity. If usage is higher than expected, consider whether a smaller model or
tighter task scope would still produce a useful result.

### What are tokens and credits?

Tokens are small units of information that ChatGPT reads and writes. Your
prompt, files, chat history, tool results, and ChatGPT’s response all
use tokens.

Credits translate token usage into a simpler unit for tracking and managing
consumption. The credit cost varies by model, context, reasoning, and tools.
After you reach your included limits, available credits let you continue
working.

Usage is calculated in credits per million input tokens, cached input tokens,
and output tokens. [Learn more about
tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).

The rate card below shows the credit cost per million tokens for models and
features.

A small subset of Enterprise customers should continue using the legacy rate
card until we migrate you to the new token-based pricing. For more information,
[contact OpenAI
sales](https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex).

| Credits per 1M tokens | Input Tokens | Cached input tokens | Output Tokens |
| --- | --- | --- | --- |
| GPT-5.6 Sol | 125 credits | 12.5 credits | 750 credits |
| GPT-5.6 Terra | 62.5 credits | 6.25 credits | 375 credits |
| GPT-5.6 Luna | 25 credits | 2.5 credits | 150 credits |
| GPT-5.5 | 125 credits | 12.50 credits | 750 credits |
| GPT-5.4 | 62.50 credits | 6.250 credits | 375 credits |
| GPT-5.4 mini | 18.75 credits | 1.875 credits | 113 credits |
| GPT-5.3-Codex-Spark | research preview | | |
| GPT-Image-2 (image) | 200 credits | 50 credits | 750 credits |
| GPT-Image-2 (text) | 125 credits | 31.25 credits | 250 credits |
|  |  |  |  |
| --- | --- | --- | --- |
| GPT-5.6 usage averages 5-40 credits per message. | | | |
| Fast mode consumes credits at a higher rate for supported models. See [Speed](/codex/agent-configuration/speed) for rates. | | | |

Speed configurations will increase credit consumption for all models that apply.
Fast mode consumes credits at a higher rate for supported models. See
[Speed](/codex/agent-configuration/speed) for supported models and rates.

[Learn more about credits in ChatGPT Plus and
Pro.](https://help.openai.com/en/articles/12642688)

[Learn more about credits in ChatGPT Business, Enterprise, and
Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

### What counts as Code Review usage?

Code Review usage applies only when Codex runs reviews through GitHub—for
example, when you tag `@Codex` for review in a pull request or enable automatic
reviews on your repository. Reviews run locally or outside of GitHub count
toward your general usage limits.

### What can I do to make my usage limits last longer?

The usage limits and credits above are average rates. You can try the following
tips to maximize your limits:

* **Control the size of your prompts.** Be precise with the instructions you
  give the agent, but remove unnecessary context.
* **Limit source material.** Provide only relevant files and, when possible,
  narrow the sources or date range.
* **Match the output to the need.** Define the audience, format, and length, and
  separate required work from optional improvements.
* **Reduce the size of your AGENTS.md.** If you work on a larger project, you
  can control how much context you inject through AGENTS.md files by [nesting
  them within your repository](/codex/agent-configuration/agents-md#layer-project-instructions).
* **Limit the number of MCP servers you use.** Every
  [MCP](/codex/extend/mcp) server adds more context to your messages and uses
  more of your limit. Disable MCP servers when you don’t need them.
* **Switch to a smaller model for routine tasks.** Using GPT-5.4 or
  GPT-5.4 mini can extend your local-message usage limits, depending on the
  model you switch from.

For guidance on choosing and scoping tasks, see [Use Work
efficiently](/codex/prompting#use-work-efficiently).

## Feature availability

| Feature | ChatGPT Plus | ChatGPT Pro | ChatGPT Business | Enterprise / Education | API Key |
| --- | --- | --- | --- | --- | --- |
| Access and surfaces | | | | | |
| --- | --- | --- | --- | --- | --- |
| [Codex cloud](/codex/cloud) |  |  |  |  | — |
| [ChatGPT Work on the web](/codex/get-started-with-work) |  |  |  |  | — |
| [ChatGPT desktop app for local chats](/codex/app) |  |  |  |  |  |
| [Codex CLI](/codex/cli) |  |  |  |  |  |
| [IDE extension](/codex/ide) |  |  |  |  |  |
| [Codex SDK, `codex exec`, and scriptable workflows](/codex/codex-sdk) |  |  |  |  |  |
| [Codex access tokens for trusted automation](/codex/enterprise/access-tokens) | — | — |  |  | — |
| [ChatGPT for Excel](https://help.openai.com/articles/20001063) |  |  |  |  | — |
| Models and multimodal | | | | | |
| [GPT-5.6](/codex/models) |  |  |  |  |  |
| [Fast mode](/codex/agent-configuration/speed) |  |  |  |  |  |
| [Codex-Spark research preview](/codex/models) | — |  | — | — | — |
| [Image generation and editing](/codex/image-generation?surface=app) |  |  |  |  |  |
| [Voice dictation](/codex/prompting#use-voice-dictation) |  |  |  |  | — |
| [ChatGPT Voice](/codex/features/voice) |  |  |  |  | — |
| [Web search](/codex/web-search?surface=app) |  |  |  |  |  |
| Local features | | | | | |
| [Local code review with `/review`](/codex/prompting#do-a-local-code-review) |  |  |  |  |  |
| [Auto-review for approval requests](/codex/sandboxing/auto-review) |  |  |  |  |  |
| [Sandboxing and permission controls](/codex/permissions) |  |  |  |  |  |
| [Project and standalone scheduled tasks](/codex/automations) |  |  |  |  |  |
| [Scheduled tasks](/codex/automations) |  |  |  |  |  |
| [Worktrees and built-in Git tools](/codex/environments/git-worktrees) |  |  |  |  |  |
| [Local environments and repeatable actions](/codex/environments/local-environment) |  |  |  |  |  |
| [Appshots](/codex/appshots) |  |  |  | — |  |
| Browser and remote control | | | | | |
| [Built-in browser previews and comments](/codex/browser?surface=app) |  |  |  |  |  |
| [Computer Use in the browser](/codex/browser?surface=app#app-computer-use-in-the-browser) | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") |
| [Use ChatGPT with Chrome](/codex/chrome-extension) | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") |
| [Computer Use](/codex/computer-use) | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") |
| [Record & Replay (macOS)](/codex/extend/record-and-replay) | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") |
| [SSH remote connections](/codex/remote-connections#connect-to-an-ssh-host) |  |  |  |  |  |
| [Mobile remote control](/codex/remote-connections) |  |  |  |  | — |
| [Browser in ChatGPT Web](/codex/browser?surface=web) |  |  |  |  | — |
| Customization and extensions | | | | | |
| [Custom instructions with `AGENTS.md`](/codex/agent-configuration/agents-md) |  |  |  |  |  |
| [Skills](/codex/build-skills) |  |  |  |  |  |
| [Plugins](/codex/plugins) |  |  |  |  | [Limited†](#codex-plan-plugin-limits "Available with plugin limits") |
| [Plugin sharing](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace) |  |  |  |  | — |
| [Connectors](/codex/plugins) |  |  |  |  | — |
| [MCP](/codex/extend/mcp) |  |  |  |  |  |
| [Subagents and custom agents](/codex/agent-configuration/subagents) |  |  |  |  |  |
| [Memories](/codex/customization/memories) | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") | [Limited\*](#codex-plan-region-limits "Available with regional limits") |
| [Chronicle](/codex/customization/chronicle) | — | [Limited\*](#codex-plan-region-limits "Available with regional limits") | — | — | — |
| Cloud and integrations | | | | | |
| [Codex cloud chats](/codex/cloud) |  |  |  |  | — |
| [Cloud environments and setup scripts](/codex/environments/cloud-environment) |  |  |  |  | — |
| [Cloud agent internet access controls](/codex/cloud/internet-access) |  |  |  |  | — |
| [Sites](/codex/sites) | — | — |  |  | — |
| [GitHub issue and PR delegation with `@codex`](/codex/third-party/github#give-codex-other-tasks) |  |  |  |  | — |
| [GitHub code review and automatic PR reviews](/codex/third-party/github) |  |  |  |  | — |
| [Slack cloud integration](/codex/third-party/slack) |  |  |  |  | — |
| [Linear cloud integration](/codex/third-party/linear) |  |  |  |  | — |
| Admin, security, and analytics | | | | | |
| [SAML SSO, MFA, and workspace user management](/codex/enterprise/admin-setup) | — | — |  |  | — |
| [`requirements.toml` managed config](/codex/enterprise/managed-configuration) |  |  |  |  |  |
| [Cloud-managed config policies](/codex/enterprise/managed-configuration#cloud-managed-requirements) | — | — |  |  | — |
| [ChatGPT workspace RBAC and custom roles](/codex/enterprise/roles-and-workspace-permissions) | — | — | — |  | — |
| [SCIM, EKM, and domain verification](/codex/enterprise/admin-setup#enterprise-grade-security-and-privacy) | — | — | — |  | — |
| [Enterprise retention and residency controls](/codex/enterprise/admin-setup#enterprise-grade-security-and-privacy) | — | — | — |  | — |
| [No training on API or business data by default](https://openai.com/business-data/) | — | — |  |  |  |
| [Analytics dashboard](/codex/enterprise/workspace-analytics) | — | — | — |  | — |
| [Analytics API](/codex/enterprise/analytics-api) | — | — | — |  | — |
| [Compliance API and audit logs](/codex/enterprise/compliance-api) | — | — | — |  | — |
| [Codex Security for connected GitHub repositories](/codex/security) | — | — | — |  | — |

PlusProBusinessEnterpriseAPI Key

#### Access and surfaces

[Codex cloud](/codex/cloud)

[ChatGPT Work on the web](/codex/get-started-with-work)

[ChatGPT desktop app for local chats](/codex/app)

[Codex CLI](/codex/cli)

[IDE extension](/codex/ide)

[Codex SDK and scripting](/codex/codex-sdk)

[Automation access tokens](/codex/enterprise/access-tokens)

—

[ChatGPT for Excel](https://help.openai.com/articles/20001063)

#### Models and multimodal

[GPT-5.6](/codex/models)

[Fast mode](/codex/agent-configuration/speed)

[Codex-Spark research preview](/codex/models)

—

[Image generation and editing](/codex/image-generation?surface=app)

[Voice dictation](/codex/prompting#use-voice-dictation)

[ChatGPT Voice](/codex/features/voice)

[Web search](/codex/web-search?surface=app)

#### Local features

[Local code review](/codex/prompting#do-a-local-code-review)

[Auto-review for approval requests](/codex/sandboxing/auto-review)

[Sandboxing and permission controls](/codex/permissions)

[Scheduled tasks](/codex/automations)

[Scheduled tasks](/codex/automations)

[Built-in Git tools](/codex/environments/git-worktrees)

[Repeatable actions](/codex/environments/local-environment)

[Appshots](/codex/appshots)

#### Browser and remote control

[Built-in browser](/codex/browser?surface=app)

[Computer Use in the browser](/codex/browser?surface=app#app-computer-use-in-the-browser)

[Limited\*](#codex-plan-region-limits "Available with regional limits")

[Chrome browser control](/codex/chrome-extension)

[Limited\*](#codex-plan-region-limits "Available with regional limits")

[Computer Use](/codex/computer-use)

[Limited\*](#codex-plan-region-limits "Available with regional limits")

[Record & Replay](/codex/extend/record-and-replay)

[Limited\*](#codex-plan-region-limits "Available with regional limits")

[SSH remote](/codex/remote-connections#connect-to-an-ssh-host)

[Mobile remote control](/codex/remote-connections)

[Browser in ChatGPT Web](/codex/browser?surface=web)

#### Customization and extensions

[Custom instructions](/codex/agent-configuration/agents-md)

[Skills](/codex/build-skills)

[Plugins](/codex/plugins)

[Plugin sharing](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace)

[Connectors](/codex/plugins)

[MCP](/codex/extend/mcp)

[Subagents](/codex/agent-configuration/subagents)

[Memories](/codex/customization/memories)

[Limited\*](#codex-plan-region-limits "Available with regional limits")

[Chronicle](/codex/customization/chronicle)

—

#### Cloud and integrations

[Cloud chats](/codex/cloud)

[Cloud environments](/codex/environments/cloud-environment)

[Internet controls](/codex/cloud/internet-access)

[Sites](/codex/sites)

—

[GitHub delegation](/codex/third-party/github#give-codex-other-tasks)

[GitHub PR reviews](/codex/third-party/github)

[Slack integration](/codex/third-party/slack)

[Linear integration](/codex/third-party/linear)

#### Admin, security, and analytics

[Workspace management](/codex/enterprise/admin-setup)

—

[`requirements.toml` config](/codex/enterprise/managed-configuration)

[Cloud-managed policies](/codex/enterprise/managed-configuration#cloud-managed-requirements)

—

[RBAC and roles](/codex/enterprise/roles-and-workspace-permissions)

—

[SCIM, EKM, and domains](/codex/enterprise/admin-setup#enterprise-grade-security-and-privacy)

—

[Retention and residency](/codex/enterprise/admin-setup#enterprise-grade-security-and-privacy)

—

[No default training](https://openai.com/business-data/)

—

[Analytics dashboard](/codex/enterprise/workspace-analytics)

—

[Analytics API](/codex/enterprise/analytics-api)

—

[Compliance and audit logs](/codex/enterprise/compliance-api)

—

[Codex Security](/codex/security)

—

\* Feature is currently limited to only specific regions. Check the
individual feature documentation to learn more about geo restrictions.

† Some first party plugins are not available.
