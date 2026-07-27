<!-- source: https://openai.com/api-reserved-tier/ -->

# Reserved Tier for API Customers

*This offering is available to Enterprise customers. Please* [*contact our sales team*](/contact-sales/) *to learn more. To purchase Scale Tier on models released before GPT‑5.6, see* [*Scale Tier*](/api-scale-tier/)*.*

## Overview

Reserved Tier is designed for customers that want to pre-purchase capacity that is incremental to rate limits and available even during periods of peak demand.

Reserved Tier lets you purchase provisioned throughput for a specific model. To make it easy to understand how much you’ll need, it is denominated in dollars per minute. Your reserved amount can be used flexibly across Standard and Priority processing, context lengths, and regions. Reserved Tier is not available for Batch or Flex processing usage. Usage above your reserved amount is billed at normal pay-as-you-go rates.

**By choosing Reserved Tier, you can secure compute capacity for our most demanded models and unlock additional scale.** Reserved Tier purchases are automatically added to your rate limits, enabling you to secure capacity for periods of higher demand.

## How it works

With Reserved Tier, you purchase a reserved dollar-per-minute amount for a specific model. While your usage is within that reserved amount, standard and priority processing requests for that model are covered by your reservation.

If usage exceeds your reserved amount, the additional usage is processed on a pay-as-you-go basis for the selected service tier and billed at normal rates.

For example:

* If you reserve $2 per minute for GPT‑5.6, eligible usage for that model is deducted from your reserved amount at list price.
* For any minute where your eligible usage is $2 or less, your usage is covered by Reserved Tier and no additional usage charges apply.
* If your eligible usage exceeds $2 in a minute, the amount above your reservation is billed at normal pay-as-you-go rates. For example, if you use $2.75 in a minute, $2.00 is covered by Reserved Tier and $0.75 is billed as pay-as-you-go overage.

These usage calculations are done with the pay-as-you-go list prices for the model. See the FAQ below for how discounts apply to Reserved Tier.

#### Pricing + SLAs

#### Token units and rate limits

#### Policies

### How is Reserved Tier ordered and provisioned?

Once you’ve signed an order form to enable Reserved Tier, you can add and remove token units through your [developer console in Organization Settings > Capacity Management⁠(opens in a new window)](https://platform.openai.com/).

### When does billing start?

Billing starts the moment when Reserved Tier token units are first allocated, and is applied to your standard OpenAI bill.

### What happens once I hit my Reserved tier $pm quota?

Requests above your Reserved Tier $pm quota (“overage”) are processed using standard Pay-As-You-Go (PAYG) billing.

### What traffic is eligible for Reserved Tier?

Reserved tier is available for Standard and Priority processing, all request context lengths, and for regional processing. Batch or Flex processing usage is not included in Reserved Tier and will be billed at PAYG rates.

### How are discounts reflected in my Reserved Tier purchases?

Reserved Tier purchases burn down at list prices; discounts are applied at the time of $/min purchase. For example, if you have a 5% discount, when purchasing $1/min in Reserved Tier ($1440/day list price), you’d actually pay $1368/day. Any overage will be billed at your normal discounted PAYG rates.

When sizing your Reserved Tier purchase, convert your current discounted PAYG spend back to its list-price equivalent. For example, if you pay $9.50/min after a 5% discount, you should purchase $10/min of Reserved Tier—not $9.50/min.

### Is my Reserved Tier traffic subject to an SLA?

Yes. SLA for the service tier you use for your requests, such as Priority or Standard, will apply.

One additional benefit of Reserved Tier is in times of peak load where OpenAI can not serve all traffic, we will reject other traffic before rejecting Reserved Tier traffic.

### How can I purchase token units on Reserved Tier?

Once Reserved Tier is enabled for your account, you can manually adjust your token units in the Capacity Management tab of your Organization Settings.

### How can I view my Reserved Tier usage?

You can view your Reserved tier usage aggregated by day in the Capacity Management section of your Organization Admin Settings.

### How do I figure out my total rate limits?

You can see your current rate limits in your [settings page⁠(opens in a new window)](https://platform.openai.com/settings/organization/limits).

When you purchase $pm for Reserved Tier, requests within your purchased quota will not count against your rate limits. Overage will be treated as normal PAYG traffic and fall within your rate limit restrictions.

### How do I enable calls to use Reserved Tier?

This happens automatically. Any traffic you send on Standard or Priority processing will automatically be counted against your $pm Reserved Tier purchase.

### How does Zero Data Retention (ZDR) work for Reserved Tier?

If customers have a use case that qualifies for ZDR, then their Reserved Tier usage will adhere to that same retention policy.
