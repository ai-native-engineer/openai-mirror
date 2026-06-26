<!-- source: https://help.openai.com/en/articles/11647665-priority-processing-faq -->

# Priority Processing FAQ

Frequently asked questions about Priority processing

Updated: 2 days ago

We now offer Priority processing for Enterprise API customers who want access to faster, more consistent performance on certain models. Below are answers to common questions about how it works, pricing, model availability, rate limits, reliability, policies, and eligibility.  
  
Learn more [here](https://openai.com/api-priority-processing/).

# Access

## Who can access Priority processing?

Priority processing is currently available to Enterprise customers.

## Is Priority processing available in all regions?

Availability of Priority processing depends on applicable laws and regulations in each jurisdiction. Please contact your Account Director if you have questions about availability in your region.

# Pricing

## How do I begin using Priority processing?

Customers can direct traffic to Priority processing on a per request basis using the existing `service_tier` parameter, with the option `service_tier="priority"`.

## How does this interact with Scale Tier?

Scale Tier will remain separate from Priority processing. Requests sent to Priority processing will be billed separately and will not count against your purchased Scale Tier TPM bundles.

## Can I automatically send my Scale Tier spillover traffic to Priority processing?

No. Traffic sent to Scale Tier will not automatically spill over to Priority processing.

## How is Priority processing billed?

Tokens served by Priority processing will be billed on a per-token basis, priced at a premium relative to Standard processing rates.

## Is my annual commitment tied to a specific processing mode?

No. All processing modes count against your annual Enterprise spend commitment.

## Do I still get a discount on Cached input tokens?

Yes! Cached Inputs receive the same 50-75% discount as they do in Standard processing.

## How do I view my Priority processing usage and spend?

To view tokens processed by Priority processing, go to the Usage dashboard, select Chat Completions or Responses, and Group by Service Tier. To view Priority processing cost, go to the Usage dashboard, and select Group by Line Item.

# Models

## Is Priority processing available for long context, fine-tuned models, embeddings, etc.?

Not at this time. We will evaluate in the future whether to offer Priority processing on additional products beyond our latest models.

## How do other modalities work with Priority processing?

Priority processing supports the same multimodal capabilities available on Standard. In particular, images can be used as inputs to Priority processing and are processed with the same fast latency.

## Will future models be supported?

We plan to offer Priority processing on new GPT models, but we don’t guarantee that every model will be supported.

# Rate limits

## What are the rate limits?

Priority processing consumption is treated the same as standard API traffic for rate limits.

## What are the ramp rate limits?

Priority processing has ramp rate limits to ensure consistently high performance for all customers, while still providing flexible, on-demand pricing. If (a) Priority processing performance is degraded AND (b) a customer’s traffic is ramping too quickly, then some Priority requests may be downgraded to Standard processing instead in rare instances.  
  
The current Priority processing ramp rate limit is defined in our primary documentation [here](https://platform.openai.com/docs/guides/priority-processing#rate-limits-and-ramp-rate).

## Best practices for staying within your ramp rate limit

* Gradually increase traffic when changing models. For example, if your application is transitioning from a previous snapshot to a new one, use a feature flag to transition traffic over the course of a few hours rather than all at once.

* Avoid running large data processing or asynchronous jobs on Priority processing. These jobs can ramp traffic very quickly, and often do not need the improved performance of Priority processing.
* If you routinely encounter ramp rate limits, consider purchasing Scale tier quota instead.

## Are ramp rate limits shared across my projects or organizations?

Yes, all of your traffic contributes to the same ramp rate limit.

# Policies

## What happens if Priority processing is not meeting the latency target?

Please reach out to your AD with any questions or concerns. Priority processing SLAs will be treated the same as Scale Tier SLAs; service credits will be offered should we fail to meet those SLAs for customers on Enterprise agreements during a given time window.

## Is Priority processing compatible with Data Residency?

Yes.

## Is Priority processing compatible with ZDR and the BAA?

Yes.
