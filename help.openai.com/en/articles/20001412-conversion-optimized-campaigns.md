<!-- source: https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns -->

# Conversion-optimized Campaigns

Learn how to create conversion-optimized cost-per-click campaigns in Ads Manager Beta.

Updated: 19 hours ago

Use Conversion-optimized  (oCPC) campaigns when you want ChatGPT Ads to optimize toward a specific conversion event after someone clicks your ad. For a general overview of campaign objectives, see [Create Campaigns for ChatGPT](/en/articles/20001210-create-campaigns-for-chatgpt).

## Before you start

Before creating an oCPC campaign, make sure:

* Conversion tracking is set up for your ad account. You can set it up via [Conversions API](https://developers.openai.com/ads/conversions-api) and/or [Javascript Pixel](https://developers.openai.com/ads/measurement-pixel)
* At least one supported standard conversion event is available. Custom conversion events are not currently supported for oCPC.
* You know which conversion event you want the campaign to optimize toward.
* You are ready to create a new campaign. Existing CPM or CPC campaigns cannot be converted to oCPC at this time.

## 1. Create a new campaign

In Ads Manager, create a new campaign and set the Objective to Conversions. This selects oCPC for the campaign type.

The campaign objective cannot be changed after campaign creation. If you need a different objective later, create a new campaign.

## 2. Choose a conversion event

Choose the Conversion event you want to optimize for. This is the downstream action, such as a purchase, sign-up, lead submission, or other supported standard conversion event, that ChatGPT Ads will use to guide delivery.

Each oCPC campaign uses one selected conversion event. The conversion event cannot be changed after campaign creation. To optimize toward a different event, create a new campaign.

## 3. Set campaign budget, dates, and locations

Set your campaign budget, start and end dates, and location targeting as you would for other campaign objectives. Choose settings that give the campaign enough time and budget to gather meaningful performance data.

## 4. Create ad groups and set a Bid Cap

Create ad groups and ads as you normally would. For each ad group, set a Bid Cap.

Bid Cap is the maximum amount you can pay for a click in an auction. oCPC uses this cap while optimizing toward clicks that are more likely to lead to your selected conversion event. Your actual CPC is determined by the auction and may be lower than your Bid Cap.

## 5. Launch and monitor performance

For oCPC campaigns, Ads Manager shows standard delivery and spend metrics alongside conversion reporting. You can review performance across the reporting views available in Ads Manager.

Because oCPC is click-billed, **Average CPC** is still the main cost metric for what you pay per click. Given oCPC optimizes toward your selected conversion event, **Conversions** is the key outcome metric to monitor.

When evaluating performance, look at conversion volume together with spend and clicks. You may also calculate cost per conversion by dividing spend by conversions.

## Optimization tips

* Choose the conversion event that best represents your campaign goal
* Use a conversion event with enough signal. Events that happen too rarely can make performance harder to evaluate
* Keep conversion tracking healthy. Incomplete or misconfigured tracking can make reporting and optimization less effective
* Monitor performance and adjust your Bid Cap based on campaign delivery and results. There is no recommended bid amount at this time
* Review performance over enough volume before making large changes to bids, budgets, or creative

## FAQ

### Which conversion event types are supported for oCPC?

oCPC currently supports one standard conversion event per campaign. Custom conversion events are not currently supported for oCPC.

### Can I convert an existing CPM or CPC campaign to oCPC?

You cannot modify existing CPM or CPC campaigns to use oCPC at this time. Create a new campaign with the Conversions objective in Ads Manager.

### Can I change the conversion event after creating an oCPC campaign?

No. The campaign objective and conversion event cannot be changed after creation. To optimize toward a different event, create a new campaign.

### Does oCPC mean I pay per conversion?

No. oCPC optimizes delivery toward your selected conversion event, but billing is still based on valid clicks.

### Will I always pay my Bid Cap?

No. Your Bid Cap is the maximum you can pay for a click. Your actual CPC is determined by the auction and may be lower than your Bid Cap.

## Next steps

After creating your oCPC campaign, you can:

* [Create ad groups and ads](/en/articles/20001211-create-ad-groups-for-chatgpt)
* [Launch your campaign](/en/articles/20001209-launch-campaigns)
* [Measure results](/en/articles/20001214-measure-results)

## Was this article helpful?
