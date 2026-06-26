<!-- source: https://openai.com/api-priority-processing/ -->

# Priority Processing for API Customers

Priority processing offers reliable, high-speed performance with the flexibility to pay-as-you-go.

By choosing Priority processing, you can unlock:

* **Predictably low latency:** Priority processing generates tokens faster and at a more consistent speed than the Standard processing service, even during peak demand.
* **Easy-to-use flexibility:** Like Standard processing, Priority processing can be accessed on a flexible, pay-as-you-go basis instead of requiring advance provisioning.

|  | Price per 1M input tokens | Price per 1M input tokens (cached) | Price per 1M output tokens | Uptime SLA3 | Latency SLA3 |
| --- | --- | --- | --- | --- | --- |
| GPT-5.5 excludes long context1 | $12.50 | $1.250 | $75.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.4 mini excludes long context1 | $1.50 | $0.150 | $9.00 | 99.9% | 99% > 100 tokens per second2 |
| GPT-5.4 excludes long context1 | $5.00 | $0.500 | $30.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.2 excludes long context1 | $3.50 | $0.350 | $28.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.1 excludes long context1 | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 excludes long context1 | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 mini excludes long context1 | $0.45 | $0.045 | $3.60 | 99.9% | 99% > 80 tokens per second2 |
| GPT-5.1 codex excludes long context1 | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 codex excludes long context1 | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-4.1 excludes long context1 | $3.50 | $0.875 | $14.00 | 99.9% | 99% > 80 tokens per second2 |
| GPT-4.1 mini excludes long context1 | $0.70 | $0.175 | $2.80 | 99.9% | 99% > 90 tokens per second2 |
| GPT-4.1 nano excludes long context1 | $0.20 | $0.050 | $0.80 | 99.9% | 99% > 100 tokens per second2 |
| GPT-4o gpt-4o-2024-11-20  gpt-4o-2024-08-06 | $4.25 | $2.125 | $17.00 | 99.9% | 99% > 80 tokens per second2 |
| gpt-4o-2024-05-13 | $8.75 | — | $26.25 | 99.9% | 99% > 80 tokens per second2 |
| GPT-4o mini | $0.25 | $0.125 | $1.00 | 99.9% | 99% > 90 tokens per second2 |
| o3 | $3.50 | $0.875 | $14.00 | 99.9% | 99% > 80 tokens per second2 |
| o4-mini | $2.00 | $0.500 | $8.00 | 99.9% | 99% > 90 tokens per second2 |

1Requests estimated at >128K prompt tokens

2Calculated as p50 request latency on a per 5 minute basis. For customers with existing enterprise agreements that have latency SLAs calculated as p50 request latency on a per minute basis, the prior SLAs are also still applicable.

3This is applicable to Enterprise customers only

## How it works

Customers can direct traffic to Priority processing on a per request basis using the existing service\_tier parameter, with the option **service\_tier = “priority”.**

Tokens served by Priority processing will be billed on a per-token basis, priced at a premium relative to Standard processing rates. 

In addition to being configured at the request level, you can also default a project to Priority in Project settings → Default Service Tier: Priority. You can still override per request.

## Limitations

* Priority processing rate limits are shared with other service tiers.
* In rare cases, rapid increases to your Priority processing Tokens per Minute can lead to hitting ramp rate limits. If you exceed the ramp rate limit, then additional traffic may be sent to Standard processing instead.

#### Pricing

#### Models

#### Rate limits

#### Reliability

#### Policies
