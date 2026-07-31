<!-- source: https://help.openai.com/en/articles/11647665-fast-mode-faq -->

# Fast mode FAQ

Frequently asked questions about Fast mode

Updated: 4 hours ago

We offer Fast mode for API customers who want access to faster, more consistent performance on certain models. Below are answers to common questions about how it works, pricing, model availability, rate limits, reliability, policies, and eligibility.

> *Note: Priority processing was renamed Fast mode on July 30, 2026. You can use either service\_tier: priority or service\_tier: fast in your API requests.*

Learn more [here](https://openai.com/api-priority-processing/).

### Is Fast mode available in all regions?

Availability of Fast mode depends on applicable laws and regulations in each jurisdiction. Please contact your Account Director if you have questions about availability in your region.

# **How it works**

Customers can direct traffic to Fast mode on a per request basis using the existing service\_tier parameter, with the option `service_tier = "fast"`.

Tokens served by Fast mode will be billed on a per-token basis, priced at a premium relative to Standard processing rates.

In addition to being configured at the request level, you can also default a project to Fast mode in Project settings > Default Service Tier: Fast. You can still override per request. Selecting Fast in your project settings is equivalent to selecting Priority.

## How does this interact with Scale Tier?

Scale Tier will remain separate from Fast mode. Requests sent to Fast mode will be billed separately and will not count against your purchased Scale Tier TPM bundles.

## Can I automatically send my Scale Tier spillover traffic to Fast mode?

No. Traffic sent to Scale Tier will not automatically spill over to Fast mode.

## How is Fast mode billed?

Tokens served by Fast mode will be billed on a per-token basis, priced at a premium relative to Standard processing rates.

## Is my annual commitment tied to a specific processing mode?

No. All processing modes count against your annual Enterprise spend commitment.

## Do I still get a discount on Cached input tokens?

Yes! Cached Inputs receive the same 50-75% discount as they do in Standard processing.

## How do I view my Fast mode usage and spend?

To view tokens processed by Fast mode (fka Priority processing), go to the Usage dashboard, select Chat Completions or Responses, and Group by Service Tier.

To view Fast mode cost, go to the Usage dashboard, and select Group by Line Item.

On the Usage dashboard, requests using either priority or fast as the service\_tier will continue to appear as priority. This will be updated for future models.

# Models

## Is Fast mode available for long context, fine-tuned models, embeddings, etc.?

Not at this time. We will evaluate in the future whether to offer Fast mode on additional products beyond our latest models.

## How do other modalities work with Fast mode?

Fast mode supports the same multimodal capabilities available on Standard. In particular, images can be used as inputs to Priority processing and are processed with the same fast latency.

## Will future models be supported?

We plan to offer Fast mode on new GPT models, but we don’t guarantee that every model will be supported.

# Rate limits

## What are the rate limits?

Priority processing consumption is treated the same as standard API traffic for rate limits.

## What are the ramp rate limits?

Fast mode has ramp rate limits to ensure consistently high performance for all customers, while still providing flexible, on-demand pricing. If (a) Fast mode performance is degraded AND (b) a customer’s traffic is ramping too quickly, then some requests may be downgraded to Standard processing instead in rare instances.

The current Fast mode ramp rate limit is defined in our primary documentation here.

# Best practices for staying within your ramp rate limit

Gradually increase traffic when changing models. For example, if your application is transitioning from a previous snapshot to a new one, use a feature flag to transition traffic over the course of a few hours rather than all at once.

Avoid running large data processing or asynchronous jobs on Fast mode. These jobs can ramp traffic very quickly, and often do not need the improved performance of Fast mode.

If you routinely encounter ramp rate limits, consider purchasing Scale tier quota instead.

## Are ramp rate limits shared across my projects or organizations?

Yes, all of your traffic contributes to the same ramp rate limit.

# Policies

## What happens if Fast mode is not meeting the latency target?

Please reach out to your AD with any questions or concerns. Fast mode SLAs will be treated the same as Scale Tier SLAs; service credits will be offered should we fail to meet those SLAs for customers on Enterprise agreements during a given time window.

## Is Fast mode compatible with Data Residency?

Yes.

## Is Fast mode compatible with ZDR and the BAA?

Yes.

## Was this article helpful?
