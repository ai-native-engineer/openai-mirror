<!-- source: https://openai.com/api-scale-tier/ -->

# Scale Tier for API Customers

*This offering is available to Enterprise customers. Please* [*contact our sales team⁠*](/contact-sales/) *to learn more.* ***To access the same premium latency and reliability benefits on a flexible, pay-as-you-go basis, see*** [***Priority processing***⁠](https://openai.com/api-priority-processing)***.***

Scale Tier lets you purchase a set number of API input and output tokens per minute (known as “token units”) upfront for access to one specific model snapshot. Each token unit is purchased for a minimum of 30 days. Additional models may be added based on customer interest.

By choosing Scale Tier, you can unlock:

* **Predictable latency:** Scale Tier is designed to generate tokens faster and at a more consistent speed than the pay-as-you-go (PAYG) service, even during peak demand.
* **Uncapped scale:** Any quota purchases with Scale Tier is automatically added to your rate limits, so you can confidently scale further.
* **Higher reliability:** Scale Tier traffic offers a 99.9% uptime SLA and prioritized compute.

|  | Input bundle | Output bundle | Uptime SLA | Latency SLA |
| --- | --- | --- | --- | --- |
| GPT-5.5 | 50,000 TPM $750.00 per unit/day | N/A3 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.4 mini | 50,000 TPM $100.00 per unit/day | N/A3 | 99.9% | 99% > 100 tokens per second2 |
| GPT-5.4 excludes long-context4 | 50,000 TPM $300.00 per unit/day | N/A3 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.2 | 25,000 TPM $105.00 per unit/day | 2,500 TPM $84.00 per unit/day | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.1 | 25,000 TPM $75.00 per unit/day | 2,500 TPM $60.00 per unit/day | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 | 25,000 TPM $75.00 per unit/day | 2,500 TPM $60.00 per unit/day | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 mini | 500,000 TPM $275.00 per unit/day | 50,000 TPM $220.00 per unit/day | 99.9% | 99% > 80 tokens per second2 |
| GPT-4.1 excludes long-context1 | 30,000 TPM $110.00 per unit/day | 2,500 TPM $36.00 per unit/day | 99.9% | 99% > 80 tokens per second2 |
| GPT-4.1 mini excludes long-context1 | 500,000 TPM $450.00 per unit/day | 50,000 TPM $175.00 per unit/day | 99.9% | 99% > 90 tokens per second2 |
| GPT-4.1 nano excludes long-context1 | 500,000 TPM $110.00 per unit/day | 50,000 TPM $40.00 per unit/day | 99.9% | 99% > 100 tokens per second2 |
| GPT-4.1 fine tuning | 30,000 TPM $165.00 per unit/day | 2,500 TPM $36.00 per unit/day | 99.9% | 99% > 80 tokens per second2 |
| GPT-4.1 mini fine tuning | 500,000 TPM $900.00 per unit/day | 50,000 TPM $175.00 per unit/day | 99.9% | 99% > 90 tokens per second2 |
| o3 | 25,000 TPM $75.00 per unit/day | 5,000 TPM $60.00 per unit/day | 99.9% | 99% > 80 tokens per second2 |
| o4-mini | 30,000 TPM $50.00 per unit/day | 5,000 TPM $32.50 per unit/day | 99.9% | 99% > 90 tokens per second2 |
| GPT-4o | 30,000 TPM $124.59 per unit/day | 2,500 TPM $39.34 per unit/day | 99.9% | 99% > 80 tokens per second2 |
| GPT-4o mini | 500,000 TPM $114.75 per unit/day | 50,000 TPM $49.18 per unit/day | 99.9% | 99% > 90 tokens per second2 |
| GPT-4o mini fine tuning | 500,000 TPM $229.50 per unit/day | 50,000 TPM $98.36 per unit/day | 99.9% | 99% > 90 tokens per second2 |
| o1 | 5,000 TPM $163.93 per unit/day | 1,000 TPM $131.15 per unit/day | 99.9% | 99% > 80 tokens per second2 |
| o3-mini | 30,000 TPM $78.69 per unit/day | 5,000 TPM $52.46 per unit/day | 99.9% | 99% > 90 tokens per second2 |

1Requests estimated at >128K prompt tokens

2Calculated as p50 request latency on a per 5 minute basis. For customers with existing enterprise agreements that have latency SLAs calculated as p50 request latency on a per minute basis, the prior SLAs are also still applicable.

3With GPT-5.4, Scale tier is purchased as a bundle of combined input and output tokens per minute. Usage of input tokens, cached input tokens, and output tokens counts against this combined bundle at different rates. See the How it Works section below.

4Long context is >272K

## How it works

With Scale Tier, you can purchase input and output token units. For example, with GPT‑4.1 each input unit costs $110/day and entitles you to 30k input tokens/min. Each output unit costs $36/day and entitles you to 2.5k output tokens/min. Each token unit is purchased for a minimum of 30 days.

More information about how Scale Tier interacts with Prompt Caching can be found in the FAQ section below.

With GPT‑5.4 you buy a Combined Input and Output tokens/min. This gives you greater flexibility and removes the need to predict your input and output token ratio. As you use scale tier, we count tokens against your Combined Tokens as follows:

* Input tokens count as 1
* Cached input tokens follow the per-model caching as below in the FAQ section
* Output tokens count based on the PayG price ratio of Output to Input tokens for the model. For example, with GPT‑5.4 one output token counts as 6.

#### Pricing

#### Token units and rate limits

#### Models

#### Reliability

#### Policies
