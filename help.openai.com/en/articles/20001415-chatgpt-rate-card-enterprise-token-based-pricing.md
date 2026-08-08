<!-- source: https://help.openai.com/en/articles/20001415-chatgpt-rate-card-enterprise-token-based-pricing -->

# ChatGPT Rate Card (Enterprise token-based pricing)

Learn how token rates work for ChatGPT models and features across Chat, ChatGPT Work and Codex

Updated: 3 hours ago

***Note****:* *This rate card applies only to new Enterprise customers whose agreement specifies usage-based billing in USD.* *Rates are shown in U.S. dollars (USD) and, unless another billing unit is listed, are charged per 1 million input, cached input, and output tokens. Refer to your agreement for applicable rates, discounts, and other commercial terms.*

*If you are on an existing Enterprise/Edu plan, new Edu plan, or on a ChatGPT Business plan, refer to the* [*ChatGPT Rate Card*](https://help.openai.com/articles/11481834) *and* [*Codex Rate card*](https://help.openai.com/articles/20001106) *for credit based pricing.*

*If you are unsure which rate card applies to your workspace, contact your OpenAI representative.*

# Overview

This article outlines the current rates for ChatGPT features based on the token-based, [flexible](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) pricing structure for new Enterprise plans. It covers pricing for all features associated with Chat, Work and Codex usage.

Customers on credit-based pricing plans should refer to [ChatGPT Rate Card (Credit based Pricing)](/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu). For questions about your plan, please reach out to your OpenAI representative.

### What are tokens?

Tokens are small units of information that OpenAI models process and generate. Token-based pricing measures usage across input tokens, cached input tokens, and output tokens. Your total charge is calculated by applying the applicable rate for the model and feature used to each token category, then adding those amounts together. You can learn more about how tokens are calculated [here](/en/articles/4936856-what-are-tokens-and-how-to-count-them).

# Chat models

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| GPT-5.6 Sol*Medium, High, Extra High* | $5.00 | $0.50 | $30.00 |
| GPT-5.6 Sol Pro | $5.00 | $0.50 | $30.00 |
| GPT-5.5 *Instant, Medium, High, Extra High* | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | N/A | $180.00 |
| GPT-5.5-Rosalind | $12.50 | $1.25 | $75.00 |
| o3 | $2.00 | $0.50 | $8.00 |
| o3-pro | $20.00 | N/A | $80.00 |
| GPT-5.3 | $1.75 | $0.175 | $14.00 |

* Prices are expressed per million input, cached input, and output tokens. These rates replace ChatGPT message rates which were previously based on [model and message count](/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu). Messages sent in chat will be based on token usage and model, so that usage pricing is standardized across all product surfaces.
* The total cost of a request is calculated as follows: cost = (input tokens × input rate) + (cached-input tokens × cached-input rate) + (output tokens × output rate)
* Instant uses GPT-5.5 Instant. Medium, High, and Extra High use different reasoning efforts, but selecting a higher reasoning effort does not increase the token price.

# ChatGPT Work and Codex models

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| GPT-5.6 Sol | $5.00 | $0.50 | $30.00 |
| GPT-5.6 Terra | $2.00 | $0.20 | $12.00 |
| GPT-5.6 Luna | $0.20 | $0.02 | $1.20 |
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Cyber | $12.50 | $1.25 | $75.00 |
| GPT-5.5-Rosalind | $12.50 | $1.25 | $75.00 |
| GPT-5.4 | $2.50 | $0.25 | $15.00 |
| GPT-5.4-Mini | $0.75 | $0.075 | $4.50 |
| GPT-5.3-Codex | $1.75 | $0.175 | $14.00 |
| GPT-5.2 | $1.75 | $0.175 | $14.00 |
| GPT-5.3-Codex-Spark | Research preview | Research preview | Research preview |

These rates apply to supported ChatGPT Work and Codex activity, including local tasks, cloud tasks, automations, code review, auto review, and delegated workers. Charges are based on the model used and the actual input, cached input, and output tokens consumed.

Image generation, Voice, web search, long context, fast mode, and regional processing may create separate or additional charges as described below.

## Note:

* Prices apply for all reasoning levels available for a given model (light, medium, high, extra high, ultra) unless otherwise noted.
* The total cost of a request is calculated as follows: cost = (input tokens × input rate) + (cached-input tokens × cached-input rate) + (output tokens × output rate)
* GPT-5.5 Cyber is available as a part of the [OpenAI Daybreak/Trusted Access for Cyber program.](https://help.openai.com/articles/20001258)
* Code review uses GPT-5.3-Codex.
* Auto review uses GPT-5.4.
* GPT-5.3-Codex-Spark may be available in Codex as a research preview. Pricing for this model is not final.

## Feature availability and applicability

The feature rates below apply wherever the listed feature is available across Chat, Work, and Codex, unless a section states otherwise. A single request may include both model-token charges and separate feature charges.

# Core ChatGPT features

## Deep research

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| o3-deep-research | $10.00 | $2.50 | $40.00 |
| o4-mini-deep-research | $2.00 | $0.50 | $8.00 |

## Images

These image-generation rates apply wherever GPT-Image-2.0 is available across ChatGPT, Work, and Codex.

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| GPT-Image-2.0 (image) | $8.00 | $2.00 | $30.00 |
| GPT-Image-2.0 (text) | $5.00 | $1.25 | - |

Image generation usage is measured in tokens, with total cost based on input text tokens, input image tokens when editing an image, and image output tokens. Image output-token usage varies with the requested dimensions and quality, while edits that include reference images may require additional input tokens. Larger or higher-quality images generally use more tokens, although token usage can vary by resolution. For image generation cost estimates, use the [calculator](https://developers.openai.com/api/docs/guides/image-generation#calculating-costs) in the image generation guide.

## Voice

| **Feature** | **Rate** |
| --- | --- |
| Voice in Chat | $0.12 / minute+ Back end model (BEM) billed at token rates. BEM is GPT-5.5. |
| Voice in Work and Codex | $0.12 / minute+ Back end model (BEM) and delegated workers billed at token rates. BEM is GPT-5.6 Terra. |

Connected minutes and model activity are metered separately. A Voice session may therefore incur both the connected-minute charge and token charges for the backend model and any delegated workers.

When Voice starts a Codex task, the task is charged using the applicable ChatGPT Work and Codex model rates above. See [ChatGPT Voice in Desktop pricing and limits](https://developers.openai.com/codex/pricing#chatgpt-voice-in-desktop) for current availability, plan allowances, and usage limits.

Prices in USD per 1M tokens.

| **Model** |  | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- | --- |
| gpt-4o-realtime-preview | Audio | $40.00 | $2.50 | $80.00 |
|  | Text | $5.00 | $2.50 | $20.00 |
| gpt-4o-mini-realtime-preview | Audio | $10.00 | $0.30 | $20.00 |
|  | Text | $0.60 | $0.30 | $2.40 |

Realtime and audio model usage is generally priced per 1 million tokens, with separate rates for text and audio inputs, cached inputs, and outputs. Total cost is calculated by applying the relevant rate to each token category used during the interaction and adding the charges together. Some specialized models are priced using another unit, such as minutes of audio or characters generated, where noted.

## Web search

| **Feature** | **Rate** |
| --- | --- |
| Web Search (all models) | $10.00 / 1K web runs+ Search content tokens billed at model rates. |
| Image Web Search (all models) | $10.00 / 1K web runs+ Search content tokens billed at model rates. |

# ChatGPT for Excel, PowerPoint, and Workspace Agents

Note: For customers on the token-based Enterprise plan, pricing is changing from a fixed number of credits per task to usage-based pricing calculated from tokens. ChatGPT for PowerPoint usage remains free for Business and Enterprise customers through August 6, 2026—after that date, charging starts under the same token-based pricing model as ChatGPT for Excel/Sheets.

## ChatGPT for Excel / Sheets

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| GPT-5.6 Sol | $5.00 | $0.50 | $30.00 |

## ChatGPT for PowerPoint

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| GPT-5.6 Sol | $5.00 | $0.50 | $30.00 |

## ChatGPT Workspace Agents

Prices in USD per 1M tokens.

| **Model** | **Input** | **Cached input** | **Output** |
| --- | --- | --- | --- |
| GPT-5.6 Sol | $5.00 | $0.50 | $30.00 |

Usage across Codex, ChatGPT Work, ChatGPT for Excel, ChatGPT for PowerPoint, and Workspace Agents is charged using the applicable model and feature rates in this article.

Note that these products share the same agentic usage when they are available on your plan.

# Additional fees and multipliers

The following fees and multipliers may apply in addition to the standard model rate.

| **Feature** | **Rate** |
| --- | --- |
| Long context*>272K input tokens* | Input: 2x Standard rateCached input: 2x Standard rateOutput: 1.5x Standard rate |
| Fast mode*Codex and Work modes only; see* [*Speed*](https://developers.openai.com/codex/speed) *for more details.* | GPT-5.6: 2x Standard rateGPT-5.5: 2.5x Standard rateGPT-5.4: 2x Standard rate |
| Regional processing (data residency)*See* [*Your data*](https://developers.openai.com/api/docs/guides/your-data) *guide for supported regions and processing details.* | 1.1x Standard rate |

## Note:

* Long context is only supported in GPT-5.6, GPT-5.5, and GPT-5.4 (Work and Codex tabs). Long context is not available in the Chat tab.

# Monitoring usage and managing costs

You can monitor your Codex usage in the [global admin console](https://admin.openai.com). For information about rate limits and reducing token consumption, see [Codex pricing and usage limits](https://developers.openai.com/codex/pricing#what-are-the-usage-limits-for-my-plan) and [best practices for managing token consumption](https://developers.openai.com/codex/pricing#what-can-i-do-to-make-my-usage-limits-last-longer).

Actual costs vary based on the model used, task size, input and output mix, automations, fast mode, and the number of concurrent Codex instances.

## Was this article helpful?
