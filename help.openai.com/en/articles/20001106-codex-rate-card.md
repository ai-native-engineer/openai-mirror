<!-- source: https://help.openai.com/en/articles/20001106-codex-rate-card -->

# Codex rate card

Learn how Codex credit rates work across Plus, Pro, Business, Enterprise, Edu, Health, and Gov plans.

Updated: 3 days ago

## Overview

This article outlines the current credit rates for Codex, under the flexible pricing structure for Plus, Pro, Business, Enterprise, Edu, Health, and Gov plans.  
  
[Learn more about credits in ChatGPT Plus and Pro.](/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora)  
  
[Learn more about credits in ChatGPT Business, Enterprise, and Edu.](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

**Note**: On April 2, 2026, we updated Codex pricing to align with API token usage, instead of per-message pricing. This change was applicable to new and existing Plus, Pro, ChatGPT Business and new ChatGPT Enterprise plans.

On April 23, 2026, we made this update for all existing ChatGPT Enterprise plans as well, inclusive of Edu, Health, Gov, and ChatGPT for Teachers.

Please refer to the [new rate card](/en/articles/20001106-codex-rate-card#codex-rate-card-token-based-pricing) in the section below for details.

## Codex rate card - token-based pricing

**This rate card applies to the following customer plans:**

* **New and existing ChatGPT Plus and Pro customers**
* **New and existing ChatGPT Business customers**
* **New and existing Enterprise/Edu/Gov/Health/ChatGPT for Teachers customers**

  + A small subset of Enterprise customers should continue using the [legacy rate card](/en/articles/20001106-codex-rate-card#legacy-rate-card). For more information [contact OpenAI sales](https://openai.com/contact-sales/).

Codex usage is priced based on **API token usage,** calculated as credits per million input tokens, cached input tokens, and output tokens. Learn more about tokens [here](/en/articles/4936856-what-are-tokens-and-how-to-count-them).  
  
This format replaces average per-message estimates with a direct mapping between token usage and credits. It is most useful when you want a clearer view of how input, cached input, and output affect credit consumption.  
  
Under this model, actual credit usage depends on the mix of input, cached input, and output tokens in each task. The table below displays **credits per 1M tokens for each token type.**

| **Model** | **Input tokens** | **Cached input tokens** | **Output tokens** |
| --- | --- | --- | --- |
| GPT-5.5 | 125 credits | 12.50 credits | 750 credits |
| GPT-5.5 Cyber | 500 credits | 50 credits | 3,000 credits |
| GPT-5.4 | 62.50 credits | 6.250 credits | 375 credits |
| GPT-5.4-Mini | 18.75 credits | 1.875 credits | 113 credits |
| GPT-5.3-Codex | 43.75 credits | 4.375 credits | 350 credits |
| GPT-5.2 | 43.75 credits | 4.375 credits | 350 credits |
| GPT-5.3-Codex-Spark | *research preview* | *research preview* | *research preview* |
| GPT-Image-2.0 (image) | 200 credits | 50 credits | 750 credits |
| GPT-Image-2.0 (text) | 125 credits | 31.25 credits | 250 credits |

**Note:**

* GPT-5.5 Cyber is available as a part of the [OpenAI Daybreak/Trusted Access for Cyber program.](https://help.openai.com/articles/20001258)
* A typical Codex task using GPT-5.5 may consume **between 5-45 credits per task.**
* Fast mode consumes credits at a higher rate for supported models. See [**Speed**](https://developers.openai.com/codex/speed) for rates.
* Code review uses GPT-5.3-Codex.
* GPT-5.3-Codex-Spark may be available in Codex as a research preview - credit rates for this model are not final.
* Read about [**Codex usage rate limits**](https://developers.openai.com/codex/pricing#what-are-the-usage-limits-for-my-plan). Codex usage limits are shared with other agentic features once pricing for those features is effective.
* If you're using ChatGPT Business or Enterprise, see the [ChatGPT Rate Card for Business/Enterprise](/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu) for pricing and effective dates for agentic features in ChatGPT.
* If you're using Plus or Pro, see [ChatGPT for Excel pricing and effective dates](/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro).

On average, Codex costs ~$100-$200/developer per month, though there is a large variance depending on model used, number of instances users are running, automations, and usage of fast mode. [**Read more**](https://developers.openai.com/codex/pricing#what-can-i-do-to-make-my-usage-limits-last-longer) about best practices in maximizing your rate limits and managing token consumption.  
  
You can monitor usage limits in Codex settings > [**Usage**](https://chatgpt.com/codex/settings/usage) panel. Depending on your plan and workspace role, you may also be able to view remaining credit, purchase credits, or manage auto-reload there. If you cannot add credits yourself, ask your workspace owner or admin.

## Legacy rate card

*Most new and existing customers across all plans have been migrated to the new token-based pricing, and should use the new rate card listed in this page.*   
  
*A small subset of Enterprise customers should continue using the legacy rate card until we migrate you to the new* [*token-based pricing*](/en/articles/20001106-codex-rate-card#codex-rate-card-token-based-pricing) *for Codex. For more information* [*contact OpenAI sales*](https://openai.com/contact-sales/)*.*

The legacy rate card expresses Codex usage as approximate average credits per message or pull request. These averages are useful for rough planning, but actual credit usage can vary based on task size, model choice, and reasoning requirements.

|  | **Unit** | **GPT-5.5 Cyber** | **GPT-5.5** | **GPT-5.4** | **GPT-5.3-Codex** | **GPT-5.1-Codex-mini** |
| --- | --- | --- | --- | --- | --- | --- |
| Local Tasks | 1 message | ~56 credits | ~14 credits | ~7 credits | ~5 credits | ~2 credits |
| Cloud Tasks | 1 message | Not available | Not available | ~34 credits | ~25 credits | Not available |
| Code Review | 1 pull request | Not available | Not available | ~34 credits | ~25 credits | Not available |

These averages also apply to legacy GPT-5.2, GPT-5.2-Codex, GPT-5.1, GPT-5.1-Codex-Max, GPT-5, GPT-5-Codex, and GPT-5-Codex-Mini.

GPT-5.5 Cyber is as a part of the [OpenAI Daybreak/Trusted Access for Cyber program.](https://help.openai.com/articles/20001258)

## FAQ

### Why are there two Codex rate cards?

We’ve modified our pricing from credits per message, to credits per token type consumed. OpenAI supports both the legacy rate card and the updated token-based rate card. The applicable version depends on workspace migration status.

### Which rate card should I use?

Most new and existing Plus, Pro, ChatGPT Business, Enterprise, Health, Edu, and Gov customers should use the [**token-based pricing rate card**](/en/articles/20001106-codex-rate-card#codex-rate-card-token-based-pricing). Note that small set of Enterprise customers should continue using the [**legacy rate card**](/en/articles/20001106-codex-rate-card#legacy-rate-card). If you're an Enterprise customer and have questions, [contact OpenAI Sales](https://openai.com/contact-sales/).

### What changed in the updated token-based rate card?

The legacy rate card shows approximate average credits per message or pull request. The updated token-based rate card shows credits by token type.

### Why is the rate card being changed?

Credits remain the core pricing unit that customers purchase and consume. The updated token-based format makes credit usage easier to map to actual model activity, aligns Codex pricing more closely with token-based metering, and gives clearer visibility into how input, cached input, and output contribute to total usage.

### How does this affect my pricing?

The impact depends on your workload mix. Some users may see higher credit consumption, while others may see lower credit consumption, depending on how much input, cached input, and output their tasks use. Output-heavy tasks and fast mode generally consume more credits than lighter tasks.
