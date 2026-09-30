<!-- source: https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing -->

# ChatGPT Rate Card (Business, Enterprise/Edu credit-based pricing)

Learn how credit rates work for ChatGPT Chat, Work, and Codex for Business & Enterprise/Edu plans.

Updated: 7 hours ago

This article outlines the current credit rates for ChatGPT Business and Enterprise/Edu plans under flexible, credit–based pricing. It covers ChatGPT models and features, ChatGPT for Excel, ChatGPT for PowerPoint, Workspace Agents, ChatGPT Work, and Codex.

For more information about how credits and flexible pricing work, see [Flexible pricing for the Enterprise, Edu and Business plans](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans).

For Enterprise agreements billed in USD, see: [ChatGPT Rate Card (Enterprise token-based pricing)](https://help.openai.com/articles/20001415). To compare billing models, see: [Token-based billing for ChatGPT Enterprise](https://help.openai.com/articles/20001520). Your agreement determines the applicable rates. Contact your OpenAI account team if you are unsure which applies. For Plus or Pro credit rates, see [Using Credits for Flexible Usage in ChatGPT (Free/Go/Plus/Pro)](/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora).

# How credit-based pricing works

Depending on the feature, usage is measured as one of the following:

* A fixed number of credits per message, task, generation, or connected minute.
* Credits per 1M input tokens, cached input tokens, and output tokens.

Tokens are small units of information that OpenAI models process and generate. For token-based credit rates, total credit usage is calculated as follows:

**Total credits = (input tokens / 1,000,000 × input rate) + (cached input tokens / 1,000,000 × cached input rate) + (output tokens / 1,000,000 × output rate)**

Actual credit usage varies based on the model, task complexity, input size, cached input, output length, automations, and fast mode. To learn more, see [What are tokens and how to count them?](https://help.openai.com/articles/4936856)

# Chat models

The credit rate for a ChatGPT message is based on the model used by the selected option.

|  |  |  |
| --- | --- | --- |
| **Model** | **Unit** | **Credits (approximately)** |
| Instant | 1 message | N/A — Unlimited |
| GPT-5.6 Sol | 1 message | 10 credits |
| GPT-5.6 Sol Pro | 1 message | 50 credits |
| GPT-6 Pro | 1 message | 50 credits |
| GPT-Rosalind-Research | 1 message | 20 credits |

Instant chat is unlimited. Medium, High, and Extra High use different reasoning efforts, but they all use GPT‑5.6 Sol and have the same rate of 10 credits per message. Selecting a higher reasoning effort does not increase the per-message credit rate.

Instant may automatically switch to Medium when a request requires more reasoning. When this happens, the message uses GPT‑5.6 Sol and is charged at 10 credits.

Unlimited or virtually unlimited access is subject to abuse guardrails and any model-specific usage allowances. Temporary restrictions may apply to prevent misuse.

GPT-6 Pro is powered by GPT-6 Astra. When billed using credits, GPT-6 Pro costs 50 credits per Chat message, the same rate as GPT-5.6 Sol Pro. Chat usage is metered separately from Astra usage in Work and Codex.

GPT-Rosalind-Research is only available to select Enterprise plans. [Read more.](/en/articles/20001193-gpt-rosalind-for-life-sciences-research)

# ChatGPT features

|  |  |  |
| --- | --- | --- |
| **Feature** | **Unit** | **Credits (approximately)** |
| Agent mode | 1 message | 30 credits |
| Deep research | 1 task | 50 credits |
| Images | 1 generation | 5 credits |
| Voice in ChatGPT | 1 minute | 1.25 credits |

For ChatGPT Edu customers, the following usage is included at no additional cost and does not consume credits:

* Images: 3 generations per rolling 24-hour period.
* Deep research: 5 queries per rolling 24-hour period.

The 24-hour period begins at the time of first use. For example, if a user generates an image at 10:00 AM, they can generate two additional images until 10:00 AM the following day. Usage beyond these limits consumes credits at the rates listed above.

# ChatGPT Work and Codex

GPT-6.1 Sol, GPT-6 Sol, and GPT-6 Luna are models for ChatGPT Work and Codex. They are not available in Chat.

ChatGPT Work and Codex usage is priced based on token usage, calculated as credits per 1M input tokens, cached input tokens, and output tokens. The rates below are for Standard mode.

This rate card applies to:

* ChatGPT Business users on standard ChatGPT seats, and users on Codex-only seats in eligible Business workspaces.
* New and existing Enterprise, Edu, Health, Gov, and ChatGPT for Teachers customers whose workspaces use credit-based pricing.
* A small subset of Enterprise customers that should continue using the legacy Codex rate card until their workspace is migrated. If you are unsure which rate card applies, contact [OpenAI Sales](https://openai.com/contact-sales/).

For ChatGPT Business, standard ChatGPT seats use [included plan limits first](https://learn.chatgpt.com/docs/pricing#what-are-the-usage-limits-for-my-plan). If the workspace has purchased credits, eligible usage can continue from the shared credit pool after an included limit is reached. Usage-based [Codex-only seats](https://help.openai.com/articles/8792828) include Codex usage only and require workspace credits from first use.

Enterprise and Edu workspaces on [credit-based flexible pricing](https://help.openai.com/articles/11487671) scale usage with credits and do not have fixed rate limits; workspaces without flexible pricing remain subject to their plan limits.

Reasoning choices such as Ultra are not separate model rows in this rate card: Ultra uses maximum reasoning and may run additional agents for eligible users, so credit usage still depends on the model used and the tokens produced by the task and any agents it runs.

GPT-5.4 and GPT-5.4 mini are no longer available in Codex when you sign in with ChatGPT. Use GPT-5.6 Terra instead of GPT-5.4 and GPT-5.6 Luna instead of GPT-5.4 mini. OpenAI API access and Codex use with your own API key are not affected.

***Note****: GPT-5.6 Sol’s promotional pricing is available at least through Nov 21, 2026. The promotion applies to eligible usage paid for with purchased credits. Included plan usage, 5-hour and weekly limits are unchanged.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Model** | **Input tokens (credits per 1M)** | **Cached input tokens (credits per 1M)** | **Output tokens (credits per 1M)** |
| GPT-6 Astra | 250 credits | 25 credits | 1,250 credits |
| GPT-6.1 Sol | 50 credits | 2.5 credits | 250 credits |
| GPT-6 Sol | 50 credits | 5 credits | 250 credits |
| GPT-6 Luna | 2.5 credits | 0.25 credits | 12.5 credits |
| GPT-5.6 Sol | 100 credits | 10 credits | 500 credits |
| GPT-5.6 Terra | 50 credits | 5 credits | 300 credits |
| GPT-5.6 Luna | 5 credits | 0.5 credits | 30 credits |
| GPT-Rosalind-Research | 125 credits | 12.50 credits | 625 credits |
| GPT-5.5 | 125 credits | 12.50 credits | 750 credits |
| Daybreak Blue (GPT-5.6 Sol) | 100 credits | 10 credits | 500 credits |
| Daybreak Red | 312.5 credits | 31.25 credits | 1,875 credits |
| GPT-5.3-Codex | 43.75 credits | 4.375 credits | 350 credits |
| GPT-5.2 | 43.75 credits | 4.375 credits | 350 credits |
| GPT-Image-2 (image) | 200 credits | 50 credits | 750 credits |
| GPT-Image-2 (text) | 125 credits | 31.25 credits | 250 credits |
| GPT-6 Astra Law \* | 312.50 credits | 31.25 credits | 1,562.5 credits |

These rates apply to supported ChatGPT Work and Codex activity, including local tasks, cloud tasks, automations, code review, auto review, and delegated workers. Charges are based on the model used and the actual input, cached input, and output tokens consumed.

\* Access to Astra for Law is limited to selected law firms in the United States through [Trusted Access](https://openai.com/solutions/industries/law/).

## Notes

* Codex does not charge for cache writes.
* Daybreak access requires approval through the [OpenAI Daybreak/Trusted Access for Cyber program](https://help.openai.com/articles/20001258). Daybreak Blue usage with GPT-5.6 Sol uses the GPT-5.6 Sol rates. Daybreak Red requires separate approval and provisioning.
* A typical Codex task using GPT-6.1 Sol may consume between 2 and 15 credits per task.
* **Fast mode:** When using credits, Fast mode is charged at 2× the Standard rate for the same model. Supported models include GPT-6.1 Sol, GPT-6 Astra, GPT-6 Sol, and GPT-6 Luna, where available.
* **Ultrafast:** When using credits, GPT-6 Astra Ultrafast is charged at 6× the Standard GPT-6 Astra rate. Ultrafast is available in ChatGPT Work and Codex on Pro $500 and eligible Enterprise and Edu plans.
* Compared with Standard mode for the same model, Fast mode uses your included subscription allowance at 2.5× the rate, and GPT-6 Astra Ultrafast at 8× the rate. These rates describe allowance usage, not speed increases.  See [Speed](https://developers.openai.com/codex/agent-configuration/speed) for availability and billing details.
* Code review uses GPT-5.3-Codex.
* Auto review uses GPT-5.6 Luna.
* Codex, ChatGPT Work, Excel, PowerPoint, Word, and Workspace Agents share agentic usage and credits when available on your plan. See [Codex pricing and usage limits](https://developers.openai.com/codex/pricing).
* GPT-Rosalind-Research is only available to select Enterprise plans. [Read more.](/en/articles/20001193-gpt-rosalind-for-life-sciences-research)

On average, Codex costs approximately $100–$200 per developer per month, though actual costs vary significantly depending on the model used, the number of concurrent instances, automations, and fast mode. See [best practices for maximizing rate limits and managing token consumption](https://developers.openai.com/codex/pricing#what-can-i-do-to-make-my-usage-limits-last-longer).

# ChatGPT for Word, Excel, PowerPoint, and Workspace Agents

Note: Excel/Sheets, PowerPoint, Word, and Workspace Agents use token-based pricing. The rates shown for those features apply to Business and Enterprise plans.

## ChatGPT for Word, Excel/Sheets, and PowerPoint

These features use token-based pricing at API model rates. Usage depends on the model and the input, cached input, and output tokens used for your task. Rates apply to models supported by each feature.

From Sep 17, 2026 through Sep 30, 2026, ChatGPT Business and Enterprise customers can use GPT-5.6 Sol in ChatGPT for Word during a free preview. This preview applies only to Word.

Standard rates, in credits per 1 million tokens:

|  |  |  |  |
| --- | --- | --- | --- |
| **Model** | **Input** | **Cached input** | **Output** |
| GPT-5.6 Luna | 5 credits | 0.5 credits | 30 credits |
| GPT-5.6 Terra | 50 credits | 5 credits | 300 credits |
| GPT-5.6 Sol | 100 credits | 10 credits | 500 credits |
| GPT-6 Astra | 250 credits | 25 credits | 1,250 credits |

GPT-5.6 Sol is the default model where available. Model availability depends on your region and workspace settings. Workspace admins can enable or disable access to each model.

Usage examples:

* A typical ChatGPT for Excel/Sheets task may use 5–20 credits per message.
* A typical ChatGPT for PowerPoint task may use 10–50 credits per message.

Actual usage varies by model and task.

## ChatGPT Workspace Agents

|  |  |  |  |
| --- | --- | --- | --- |
| **Model** | **Input tokens (credits per 1M)** | **Cached input tokens (credits per 1M)** | **Output tokens (credits per 1M)** |
| GPT-5.6 | 100 credits | 10 credits | 500 credits |

A typical end-to-end Workspace Agent run using GPT-5.6 may consume between 5 and 25 credits.

## Included rate limits for ChatGPT Business

A standard ChatGPT Business seat includes ChatGPT and Codex. ChatGPT Work, Workspace Agents, Excel, PowerPoint, Word, and Codex use a shared allowance and credit pool. Once a feature’s pricing is in effect, flexible pricing lets you continue beyond included limits. A usage-based Codex-only seat provides access to Codex only. See [What is ChatGPT Business?](/en/articles/8792828-what-is-chatgpt-business) for more about seat types.

ChatGPT Work follows the same usage structure as Codex. Because Codex examples are based on coding tasks, ChatGPT Work usage varies by task.

# ChatGPT Sites

ChatGPT Sites is available to Business and Enterprise customers, with public publishing available where supported. Sites is also rolling out in public beta to additional paid plans. Pricing information will be available soon.

# Monitoring usage and managing credits

You can monitor Codex & Work usage limits in Codex settings under [Usage](https://chatgpt.com/codex/settings/usage). Depending on your plan and workspace role, you may also be able to view remaining credits, purchase credits, or manage auto-reload there. If you cannot add credits yourself, ask your workspace owner or admin.

Actual credit usage varies based on the model used, task size, input and output mix, automations, fast mode, and the number of concurrent Codex instances.

# Legacy rates

## Legacy ChatGPT models

The following rates apply to legacy ChatGPT models and are billed in credits per message.

|  |  |  |
| --- | --- | --- |
| **Model** | **Unit** | **Credits (approximately)** |
| o3 | 1 message | 10 credits |
| o3-pro | 1 message | 50 credits |
| GPT-5.3 | 1 message | N/A — Unlimited |
| GPT-5.4 Thinking mini | 1 message | N/A — Unlimited |
| GPT-5.3 Pro | 1 message | 50 credits |
| GPT-5.3 Thinking | 1 message | 10 credits |
| GPT-5.4 Thinking | 1 message | 10 credits |
| GPT-5.4 Pro | 1 message | 50 credits |
| GPT-5.5 Instant | 1 message | N/A — Unlimited |
| GPT-5.5 Thinking | 1 message | 10 credits |

One prompt and response form a single message. Unlimited or virtually unlimited access is subject to abuse guardrails and any model-specific usage allowances. Temporary restrictions may apply to prevent misuse.

## Legacy Codex rate card

Most new and existing customers using credit-based pricing have been migrated to token-based credit pricing and should use the ChatGPT Work and Codex rate card above. A small subset of Enterprise customers should continue using this legacy rate card until their workspace is migrated. For more information, contact [OpenAI Sales](https://openai.com/contact-sales/).

The legacy rate card expresses Codex usage as approximate average credits per message or pull request. Actual credit usage can vary based on task size, model choice, and reasoning requirements. For GPT-6 Sol and GPT-6 Luna, average legacy usage is approximately 5 credits and 1 credit per message, respectively.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Activity** | **Unit** | **GPT-6 Astra** | **GPT-6.1 Sol** | **GPT-6 Sol** | **GPT-6 Luna** | **GPT-5.6 Sol** | **GPT-5.6 Terra** | **GPT-5.6 Luna** | **GPT-5.5 Cyber** | **GPT-5.5** |
| Local tasks | 1 message | ~16 credits | ~4 credits | ~5 credits | ~1 credit | ~11 credits | ~6 credits | ~1 credits | ~56 credits | ~14 credits |
| Cloud tasks | 1 message | Not Available | Not available | Not available | Not available | Not available | Not available | Not available | Not available | Not available |
| Code review | 1 pull request | Not Available | Not available | Not available | Not available | Not available | Not available | Not available | Not available | Not available |

These averages also apply to legacy GPT-5.2, GPT-5.2-Codex, GPT-5.1, GPT-5.1-Codex-Max, GPT-5, GPT-5-Codex, and GPT-5-Codex-Mini.

# FAQ

## Which rate card should I use?

Use the rates in this article if your workspace uses credit-based flexible pricing. If your Enterprise agreement specifies usage-based billing in U.S. dollars, see: [ChatGPT Rate Card (Enterprise token-based pricing)](https://help.openai.com/articles/20001415). Your agreement determines your applicable rates. A small subset of Enterprise customers should continue using the legacy Codex rate card until their workspace is migrated. If you are unsure, contact your OpenAI representative or [OpenAI Sales](https://openai.com/contact-sales/).

## Why are some rates fixed while others are token-based?

Some ChatGPT experiences are billed as a fixed number of credits per message, task, generation, or minute. Agentic products and Codex are billed by the input, cached input, and output tokens used, which provides a direct mapping between model activity and credit consumption.

## Does selecting a higher ChatGPT reasoning effort increase the message rate?

No. Medium, High, and Extra High use different reasoning efforts, but they use GPT-5.6 Sol and have the same 10-credit message rate.

## How does token-based pricing affect my credit usage?

The impact depends on your workload mix. Some users may see higher credit consumption and others may see lower consumption depending on input, cached input, and output usage. Output-heavy tasks and fast mode generally consume more credits than lighter tasks.
