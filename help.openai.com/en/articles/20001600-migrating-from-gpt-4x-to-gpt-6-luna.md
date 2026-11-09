<!-- source: https://help.openai.com/en/articles/20001600-migrating-from-gpt-4x-to-gpt-6-luna -->

# Migrating from GPT-4.x to GPT-6 Luna

Evaluate GPT-6 Luna, compare cost and performance, and plan your migration from GPT-4.x.

Updated: 17 days ago

GPT-6 Luna is the recommended starting point for migrating existing GPT-4.x use cases. The right configuration depends on your application, so evaluate the model on representative workloads before moving production traffic.

## Choose your reasoning setting

Start with reasoning effort set to `none`. Most GPT-4.x use cases are expected to migrate with this setting. Test other settings to find the right balance of quality, latency, and cost for your application.

For API changes and technical details, see the [GPT-6 developer guide](https://developers.openai.com/api/docs/guides/latest-model).

## Compare cost and performance

GPT-6 Luna has a lower per-token price than the GPT-4.x models covered by this migration. For most use cases, it offers a more capable model at a lower per-token price.

Compare total cost on your own workloads before migrating. Token usage and reasoning settings can affect the cost of each task.

## Migrate your application

1. **Establish a baseline.** Select representative requests, including important edge cases, and record your current model’s quality, latency, and cost.
2. **Evaluate Luna.** Start with reasoning effort set to `none` and compare results against your baseline. Check the behaviors your application depends on, including output formatting and tool use where relevant.
3. **Tune and retest.** Adjust prompts, reasoning effort, and verbosity based on your evaluation results, then retest.
4. **Roll out gradually.** Begin with a limited share of production traffic. Monitor quality, latency, errors, and cost before completing the migration.

## Get support

**Self-serve customers:** Contact OpenAI Support through the chat bubble at [help.openai.com](https://help.openai.com).

**Sales-managed customers:** Contact your OpenAI account team to arrange support from our engineering team. We can help develop a migration plan tailored to your product and identify how to get the most out of Luna.
