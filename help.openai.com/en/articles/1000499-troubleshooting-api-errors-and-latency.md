<!-- source: https://help.openai.com/en/articles/1000499-troubleshooting-api-errors-and-latency -->

# Troubleshooting API Errors and Latency

This article explains how to use the Service Health and Usage dashboards to troubleshoot common errors and latency issues when using the OpenAI API.

Updated: 9 days ago

## Important Links

* [Service Health Dashboard](https://platform.openai.com/settings/organization/service-health) (currently only available to Enterprise API customers)
* [Usage Dashboard](https://platform.openai.com/settings/organization/usage)

## Start with the Right Defaults

When you open the Service Health dashboard, it defaults to:

* All projects
* Last 30 days
* Hourly resolution

This view is useful for orientation only. Meaningful troubleshooting always requires filtering.

## Filter Before Investigating

Correct filtering is the most important step. Most misinterpretations come from mixing models, tiers, or projects.

### Filter by Model (One at a Time)

Always filter to a single model.  
  
Why:

* Issues on low-traffic models can be hidden by higher-volume traffic
* High-volume models can make localized issues look global
* Different models have different performance goals

Note: selecting multiple models aggregates them—it does not switch between them.

### Filter by Service Tier

If you use more than one tier (standard, priority, scale), always filter to the tier you are investigating.  
  
Why:

* Tiers have different performance characteristics
* Priority and scale tiers have defined SLAs
* Mixing tiers obscures paid-tier performance

This is especially important for latency analysis.

### Filter by Project

By default, Service Health shows all projects.  
  
For troubleshooting, filter to the project(s) where the issue was observed.  
  
Why:

* A single high-volume project can dominate metrics.
* Smaller affected projects can be masked by unrelated traffic.

Only leave "All projects" selected if you believe the issue is truly organization-wide.

## Troubleshooting Errors

### Use the HTTP Requests View

To investigate errors:

1. Filter by model and service tier.
2. Open the **HTTP Requests** tab instead of the **Uptime** tab.

This view shows total requests and error counts by HTTP status code. Zoom to minute-level resolution to identify granular spikes or changes.

### Interpret Error Rates, Not Counts

Some errors are expected in any production system. Focus on error **percentage**, not raw totals.  
  
The larger your total volume, the larger the potential number of errors even with an extremely low error rate.

### When Errors Are Missing from Service Health

If you see client-side errors but no corresponding data in Service Health:

* Requests likely did not reach OpenAI.
* The issue is usually upstream (timeouts, proxies, networking).

This is common with aggressive client-side timeouts.

## Troubleshooting Latency

Latency analysis is most meaningful on **priority** and **scale** tiers, which have defined SLAs. Standard tier can show wider latency variation, and does not have guaranteed latency.

### Key Metrics

To view each metric, click the relevant tab:

* **Token Velocity:** Tokens generated per second; independent of prompt size.
* **Request Time:** Total request duration; strongly affected by output size and reasoning.
* **Time to First Token (TTFT):** Time until the first token is generated; strongly affected by uncached input prompt size and reasoning.

Always review P50 / P75 / P95 percentiles. Averages can hide real-user impact.

## 6. Correlating Latency with Token Usage

Service Health shows *when* behavior changed. Usage data helps explain *why*.  
  
In the Usage dashboard, do the following to ensure you're looking at the data relevant to your view in the Service Health Dashboard:

* **Filter** to the same project and model.
* **Group by** service tier, if applicable.
* Focus on output tokens, which most strongly affect latency.

For deeper analysis, export Activity Data and examine tokens per request over time.

## 7. What to Share with Support (If Needed)

If you contact support, include:

* Impacted Org IDs **(important)**
* Impacted endpoints, such as Chat Completions or Responses **(important)**
* Impacted models **(important)**
* Whether this is on Scale or Priority tier **(important)**
* Time ranges with timezone for latency or errors **(important)**
* Relevant x-request-id or X-Client-Request-Id, if available
* Timestamps with timezone, or at least the date, for the requests you provide

If available, also include:

* Project ID related to the requests
* Whether data residency requests are impacted, and which ones
* Descriptions of the trends you’re seeing

For the issue type, include:

* **Errors:** Approximate percentage of failing or erroring requests, response codes, error messages, and how long it took to receive the error response.
* **Latency:** Which percentiles are affected (P50 / P90 / P95 / P99), how high they are compared to the customer’s baseline, and examples of slow requests with send and receive timestamps.
* **Both:** Screenshots or a table of error or latency data, plus how you determined error rates or latency were higher than expected.

## Common Troubleshooting Scenarios

### Timeouts Occur but Service Health Looks Normal

**Possible cause:** requests are timing out before reaching OpenAI.  
  
Check:

* Client or proxy timeout settings
* Local network or load balancer changes
* Presence of 499 errors in Service Health dashboard (these may show up as 5xx errors in your own systems).

### Latency Increased Without a Deployment

**Possible cause:** output token size or reasoning usage increased and/or traffic shifted between service tiers.  
  
Check:

* Average output tokens per request in the Usage dashboard (requires downloading data and dividing output tokens by total requests).
* Request Time and TTFT percentiles in Service Health dashboard.

### Priority or Scale Tier Appears Slow

**Possible cause:** metrics are mixed across tiers, meaning standard-tier traffic is masking paid-tier performance.  
  
Check:

* Filters are restricted to a single tier and model.
* Token velocity comparison between tiers.

### Spike in 5XX Errors

**Likely cause:** transient failures affecting a small percentage of traffic.  
  
Check:

* Error rate percentage
* Whether traffic volume changed at the same time

### Issue Affects Only One Project

**Likely cause:** project-specific configuration or usage pattern.  
  
Check:

* Project-level filtering
* Comparison with unaffected projects

## Final Takeaways

* Filter by model, tier, and project where relevant before interpreting metrics.
* Use **percentiles**, not averages, for latency analysis.
* Small error rates are expected.
* Missing data usually indicates upstream issues.
* Usage data can help explain *why* latency changed; Service Health shows *when* behavior changed.
