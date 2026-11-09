<!-- source: https://help.openai.com/en/articles/20001634-bidding-strategies-and-how-pricing-works-in-chatgpt-ads -->

# Bidding strategies and how pricing works in ChatGPT Ads

Choose how ChatGPT Ads works toward your business goals, and understand how bidding relates to what you pay.

Updated: 10 hours ago

ChatGPT Ads is evolving to be more intelligent by default, taking on more of the work of managing campaigns so you can focus on the results that matter to your business. You tell us the outcomes you care about and the budget or target cost that works for your business, and our system adjusts bids and ad delivery to work toward those goals.

## **Choose a bidding strategy**

Your strategy guides how bids are set. Intelligent bidding focuses on your desired business outcome within your budget. Target CPA and Target CPC let you specify an average cost per conversion or click, while the system manages individual bids and adjusts delivery toward that target.

### **Intelligent bidding**

Intelligent bidding, formerly Maximize Results (Autobid), automatically adjusts bids and ad delivery to help drive your desired business outcome within your budget. You do not need to manage individual bids.

Use this option when you want the system to pursue results within your budget without specifying a target average CPA or CPC.

### **Target CPA for conversion campaigns**

Target CPA, or target cost per action, is the average amount you’d like to pay for a conversion, such as a purchase or lead. While Max Bid limits individual bids, Target CPA gives our system a conversion-cost goal to work toward. The system uses your target and available conversion signals to dynamically adjust bids and delivery, aiming to get as many conversions as possible from your budget while working toward your desired average CPA. This gives you a more direct way to guide campaign delivery around your acquisition goals without managing individual bids.

Starting Monday, November 9, Target CPA replaces Max Bid as the bidding option for advertisers creating **new** conversion campaigns who want to work toward a specific cost per conversion.

For example, a $50 Target CPA tells the system to work toward an average conversion cost of $50. Some conversions may cost more and others less; actual average CPA may be higher or lower than your target.

### **Target CPC for click campaigns**

Target CPC, or target cost per click, is the average amount you’d like to pay for a click. Starting Monday, November 9, Target CPC is available for **new** click campaigns.

While Max CPC caps individual bids, Target CPC lets our system bid above or below your target in individual auctions, aiming to deliver as many clicks as possible from your budget while working toward your desired average CPC. Individual clicks may cost more or less than your target, and actual average CPC may be higher or lower.

### **Existing Max Bid and Max CPC campaigns**

Max Bid and Max CPC are legacy bid controls rather than average outcome-cost targets. Max Bid sets an auction-bid ceiling; Max CPC sets a maximum click bid.

Max Bid and Max CPC will retire on January 1, 2027 for existing campaigns. Target CPA replaces Max Bid for conversion campaigns and Target CPC replaces Max CPC for click campaigns. Begin moving campaigns to the new options in Ads Manager from November 9, 2026.

## **How bids and pricing work**

Your campaign objective, bidding strategy and budget guide how ChatGPT Ads pursues results for your business. With Intelligent bidding, Target CPA or Target CPC, our system considers the likelihood of a click or conversion alongside the price it would pay, then chooses auction bids on your behalf. Your budget and any target cost guide those decisions, helping the system evaluate opportunities against the outcomes and costs that matter to your business.

Auctions determine which eligible ads are shown. The final winning auction bid sets the price you pay. This pricing rule applies across all bidding strategies, including existing Max Bid and Max CPC campaigns.

Your Target CPA or Target CPC is an average-cost goal that guides the system's auction bids. It is not a fixed price per conversion or click, and actual average costs may be higher or lower than your target. The system makes individual bidding decisions to work toward your outcome and cost goal. This approach applies across all campaigns and bidding strategies.

## **Set a realistic target**

* **Review recent actual CPA for the same conversion event, or actual CPC for a click campaign.** Use a consistent reporting period and allow for conversion-reporting delay.
* **Compare recent performance with what the outcome is worth to your business.** A target below recent performance may restrict delivery.
* **Set or adjust the target as your campaign moves to the new strategy.** Review spend, results and actual average cost together as the campaign learns.

For example, $400 in spend and 10 attributed purchases gives an actual CPA of $40 for that reporting scope. Use that result and your acquisition goals as a starting point. Setting a $20 target does not mean the system can deliver purchases at half the observed cost.

Follow the supported transition steps shown for your campaign.

## **Conversion data and event quality**

For conversion campaigns, set up the [OpenAI Pixel](https://developers.openai.com/ads/measurement-pixel), [Conversions API](https://developers.openai.com/ads/conversions-api), or both, and select a supported conversion event. Verify that real events are arriving at the data source linked to the campaign. Setup alone does not establish that usable conversion signals are being received.

Event Quality Score (EQS) describes the usefulness of received event information for measurement. Conversion volume describes how often the selected action occurs. A high score does not establish that there are enough signals to support scale.

Check event-quality warnings for missing matching information, delays or repeated events, and resolve signal gaps. Weak or missing conversion signals can reduce delivery and leave budget unspent.

Use the [OpenAI Pixel](https://developers.openai.com/ads/measurement-pixel) guide or [Conversions API](https://developers.openai.com/ads/conversions-api) guide for setup, [Conversion-optimized Campaigns](/en/articles/20001412-conversion-optimized-campaigns) for supported events and billing choices, and [Understanding and improving event quality](/en/articles/20001513-understanding-and-improving-event-quality) for diagnostics.

## **Audience bid multipliers**

Where an audience bid multiplier is available, review it alongside the base target. A $50 Target CPA with a 1.2× new-customer multiplier gives that segment a $60 target. This remains an average-cost goal, not a guaranteed price per conversion.

### **FAQs**

### **How do the changes apply to API campaigns?**

We’re adding dedicated Target CPA and Target CPC fields so API partners can create campaigns with target bidding or switch existing campaigns to it.

* Before November 18, 2026: The Max Bid and Max CPC fields retain their existing behavior. Partners can begin adopting the new target fields once they are available.
* From November 18: We recommend using the new Target CPA and Target CPC fields. The legacy fields will remain supported through December 31, but using them to create a campaign or change an existing ad group’s bid type will select Target CPA or Target CPC, respectively. For these operations, submitted values will represent average-cost targets rather than maximum bids.
* Starting January 1, 2027: The Max Bid and Max CPC fields will be deprecated. Partners should update their integrations to use the new target fields before this date.

### **Will my campaign spend its full budget?**

Your campaign may not spend its full budget if targets are too restrictive, eligible opportunities are limited, or conversion signals are weak or missing.

To help your campaign deliver effectively, review your targets against recent performance. For conversion campaigns, set up the OpenAI Pixel or Conversions API and confirm that your selected conversion events are being received. Then review your Event Quality Score (EQS) and Diagnostics in Ads Manager to identify and resolve data-quality issues. Reliable conversion data helps our system learn which opportunities are likely to lead to conversions and optimize delivery toward your campaign goals.

### **Does Target CPA mean I’m billed for conversions?**

Your bidding goal and billing event are separate settings. A campaign can optimize for conversions while charges are based on clicks or impressions, depending on its billing setting. See [Conversion-optimized Campaigns](/en/articles/20001412-conversion-optimized-campaigns) for details.

### **Is a cost target a guaranteed maximum?**

No. Target CPA and Target CPC are average-cost goals. Actual average costs can be higher or lower, and individual results can cost different amounts.

### **What if conversion events are missing?**

Confirm the selected event, campaign-source links and real event receipts, then review quality warnings. See [Troubleshooting conversion tracking](/en/articles/20001604-troubleshooting-conversion-tracking-for-chatgpt-ads) and [Conversion Measurement](/en/articles/20001409-conversion-measurement) for help investigating missing events or reporting differences.
