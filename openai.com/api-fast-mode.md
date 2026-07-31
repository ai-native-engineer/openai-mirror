<!-- source: https://openai.com/api-fast-mode/ -->

# Fast mode for API Customers

Fast mode offers reliable, high-speed performance with the flexibility to pay-as-you-go. For our latest frontier model, gpt-5.6-sol, you can access up to 2.5x faster speeds with Fast mode.

**By choosing Fast mode, you can unlock:**

* Predictably low latency: Fast mode generates tokens faster and at a more consistent speed than the Standard processing service, even during peak demand.
* Easy-to-use flexibility: Like Standard processing, Fast mode can be accessed on a flexible, pay-as-you-go basis instead of requiring advance provisioning.

*Note: Priority processing was renamed Fast mode on July 30, 2026. You can use either service\_tier: priority or service\_tier: fast in your API requests.*

|  | Price per 1M input tokens | Price per 1M input tokens (cached) | Price per 1M output tokens | Uptime SLA3 | Latency SLA3 |
| --- | --- | --- | --- | --- | --- |
| GPT-5.6 Sol excludes long context1 | $10.00 | $1.00 | $60.00 | 99.9% | 99% > 80 tokens per second2 |
| GPT-5.6 Terra excludes long context1 | $4.00 | $0.40 | $24.00 | 99.9% | 99% > 70 tokens per second2 |
| GPT-5.6 Luna excludes long context1 | $0.40 | $0.04 | $2.40 | 99.9% | 99% > 100 tokens per second2 |
| GPT-5.5 excludes long context1 | $12.50 | $1.250 | $75.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.4 mini excludes long context1 | $1.50 | $0.150 | $9.00 | 99.9% | 99% > 100 tokens per second2 |
| GPT-5.4 excludes long context1 | $5.00 | $0.500 | $30.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.2 | $3.50 | $0.350 | $28.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5.1 | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 mini | $0.45 | $0.045 | $3.60 | 99.9% | 99% > 80 tokens per second2 |
| GPT-5.1 codex | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-5 codex | $2.50 | $0.250 | $20.00 | 99.9% | 99% > 50 tokens per second2 |
| GPT-4.1 | $3.50 | $0.875 | $14.00 | 99.9% | 99% > 80 tokens per second2 |
| GPT-4.1 mini | $0.70 | $0.175 | $2.80 | 99.9% | 99% > 90 tokens per second2 |
| GPT-4.1 nano | $0.20 | $0.050 | $0.80 | 99.9% | 99% > 100 tokens per second2 |
| GPT-4o gpt-4o-2024-11-20  gpt-4o-2024-08-06 | $4.25 | $2.125 | $17.00 | 99.9% | 99% > 80 tokens per second2 |
| gpt-4o-2024-05-13 | $8.75 | — | $26.25 | 99.9% | 99% > 80 tokens per second2 |
| GPT-4o mini | $0.25 | $0.125 | $1.00 | 99.9% | 99% > 90 tokens per second2 |
| o3 | $3.50 | $0.875 | $14.00 | 99.9% | 99% > 80 tokens per second2 |
| o4-mini | $2.00 | $0.500 | $8.00 | 99.9% | 99% > 90 tokens per second2 |

1Requests estimated at >272K prompt tokens

2Calculated as p50 request latency on a per 5 minute basis. For customers with existing enterprise agreements that have latency SLAs calculated as p50 request latency on a per minute basis, the prior SLAs are also still applicable.

3This is applicable to Enterprise customers only

## How it works

Customers can direct traffic to Fast mode on a per request basis using the existing service\_tier parameter, with the option service\_tier = "fast".

Tokens served by Fast mode will be billed on a per-token basis, priced at a premium relative to Standard processing rates.

In addition to being configured at the request level, you can also default a project to Fast mode in Project settings > Default Service Tier: Fast. You can still override per request. Selecting Fast in your project settings is equivalent to selecting Priority.

## Limitations

* Fast mode rate limits are shared with other service tiers.
* In rare cases, rapid increases to your Fast mode Tokens per Minute can lead to hitting ramp rate limits. If you exceed the ramp rate limit, then additional traffic may be sent to Standard processing instead.

## Frequently asked questions

#### Pricing

#### Models

#### Rate limits

#### Reliability

#### Policies

### What does the change from Priority processing to Fast mode mean for customers?

On July 30, 2026, Priority processing was renamed to Fast mode, and we increased the speeds at which we run gpt-5.6-sol to make it 2.5x faster than standard speeds. The name Fast mode more clearly communicate its primary benefit: faster responses for latency-sensitive workloads. The new name reflects the same flexible, pay-as-you-go processing customers already use. This is not a breaking change as both `service_tier=priority` and `service_tier=fast` continue to be accepted by our API to access this functionality.

For existing models, you can set `service_tier` to either `priority` or `fast` in requests to /v1/responses, /v1/chat/completions, and /v1/usage. Both options will continue to return priority in API responses and appear as priority in the Usage dashboard and invoices.

For models released after gpt-5.6, API responses, usage reporting, and invoices will reflect the fast mode name.

### (For Enterprise customers) How does this interact with Scale Tier?

Scale Tier will remain separate from Fast mode.

Requests sent to Fast mode will be billed separately and will not count against your purchased Scale Tier TPM bundles.

### (For Enterprise customers) Can I automatically send my Scale Tier spill-over traffic to Fast mode?

No. Traffic sent to Scale Tier will not automatically spill over to Fast mode.

### (For Enterprise customers) Is my annual commitment tied to a specific processing mode?

No. All processing modes count against your annual enterprise spend commitment.

### Do I still get a discount on Cached input tokens?

Yes! For a given model, Cached Inputs receive the same 50%, 75%, or 90% discount as they do in Standard processing.

### How do I view my Fast mode usage and spend?

**To view tokens processed by Fast mode (fka Priority processing), go to the Usage dashboard, select Chat Completions or Responses, and Group by Service Tier.**

**To view Fast mode cost, go to the Usage dashboard, and select Group by Line Item.**

**On the Usage dashboard, requests using either priority or fast as the service\_tier will continue to appear as priority. This will be updated for future models.**

### Is Fast mode available for long context, fine-tuned models, embeddings, etc.?

Not at this time. We will evaluate in the future whether to offer Fast mode on additional products beyond our latest models.

### How do other modalities work with Fast mode?

Fast mode supports the same multimodal capabilities available on Standard. In particular, images can be used as inputs to Priority processing and are processed with the same fast latency.

### Will future models be supported?

We don't guarantee that every model will be supported.

### What are the rate limits?

Fast mode consumption is treated the same as standard API traffic for rate limits.

### What are the ramp rate limits?

Fast mode has ramp rate limits to ensure consistently high performance for all customers, while still providing flexible, on-demand pricing. If (a) Fast mode performance is degraded AND (b) a customer's traffic is ramping too quickly, then some Fast mode may be downgraded to Standard processing instead.

The current Fast mode ramp rate limit is defined as processing at least 1M TPM, and increasing traffic by >50% Tokens Per Minute in less than 15 minutes.

Requests processed by Standard service tier will be billed at standard rates, and are not eligible for Priority processing Service Level Objectives.

Requests processed by Standard service tier will include `service_tier="Default"` in the response.

**Best practices for staying within your ramp rate limit**

1. Gradually increase traffic when changing models. For example, if your application is transitioning from a previous snapshot to a new one, use a feature flag to transition traffic over the course of a few hours rather than all at once.
2. Avoid running large data processing or asynchronous jobs on Fast mode. These jobs can ramp traffic very quickly, and often do not need the improved performance of Fast mode.
3. If you routinely encounter ramp rate limits, consider purchasing Scale Tier capacity instead or in addition.

### Are ramp rate limits shared across my projects or organizations?

Yes. All of your traffic contributes to the same ramp rate limit.

### (For Enterprise customers) What happens if it’s not meeting the latency target?

For Enterprise customers, please reach out to your AD with any questions or concerns.

Priority processing SLAs will be treated the same as Scale Tier SLAs; service credits will be offered should we fail to meet those SLAs for customers on enterprise agreements during a given time window.

### Is Fast mode compatible with Data Residency?

Yes

### Is Fast mode compatible with ZDR and the BAA?

Yes
