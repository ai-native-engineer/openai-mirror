<!-- source: https://help.openai.com/en/articles/20001214-measure-results -->

# Measure Results

Understand the reporting tools available in Ads Manager Beta.

Updated: 4 days ago

In Ads Manager Beta, you can measure campaign performance with reporting tools that help you track delivery and monitor results. As the platform evolves, we’ll introduce additional metrics, reporting views, and insights over time.

## Metrics

You can currently track the following metrics across all levels (campaign, ad group, and ad):

* **Impressions**: Number of times your ads were shown
* **Clicks**: Number of times users clicked on your ads
* **Spend**: Total amount spent delivering your ads
* **CTR:** Percentage of impressions that resulted in clicks
* **Avg CPC:** Average cost per click
* **Avg CPM:** Average cost per thousand impressions
* **Conversions:** Number of conversion events attributed to your campaigns, if conversion measurement is set up. To get started with conversions, visit our [measurement documentation](https://developers.openai.com/ads)

These metrics are available in table view, chart view, and CSV export downloads and can be used to evaluate delivery, engagement, and pacing across your campaigns.

### How conversions appear in reporting

Ads Manager displays a single **Conversions** metric for the selected reporting scope and date range.  
  
Standard and custom conversion events can be configured for attribution. However, attributed conversion events are currently combined into the total **Conversions** value shown in the reporting table and CSV export.

## Table view

Table view is the default reporting view for monitoring performance in Ads Manager Beta.

* Navigate to the Campaigns, Ad Groups, or Ads page
* Review performance metrics directly in the table on each page, including impressions, clicks, spend, CTR, Avg CPC, Avg CPM, and conversions when available

## CSV download

CSV downloads allow you to export reporting data from Ads Manager Beta for offline analysis.  
  
  
**Cumulative values:**

* Set the date range in the top right corner to the period you want to analyze
* Click the three-dot menu in the top right corner
* Select ‘Download Cumulative Values’

**Daily values:**

* Click the three-dot menu in the top right corner
* Select the dates you want to download reporting for
* Select ‘Download Daily Values’

## Insights charts

Ads Manager Beta includes chart views that allow you to analyze performance trends over time.

* Select the chart icon next to the three-dot menu
* Click View insights
* Select the metric(s) you want to view: impressions, clicks, spend, or any combination of all three
* Set the date range you want to analyze

## Measurement and reporting FAQ

### How do I validate that the JavaScript Pixel is installed correctly?

Install the JavaScript Pixel on pages where you want to measure ad activity, confirm it initializes with the correct pixel ID, and use debug mode while testing. See the [JavaScript Pixel documentation](https://developers.openai.com/ads/measurement-pixel) for installation, event, and troubleshooting guidance.

### Can I deploy the Pixel through Google Tag Manager?

Yes, as long as your tag manager loads the Pixel snippet on the correct pages and does not block or reorder the initialization and event calls. If the tag manager prevents the Pixel from loading reliably, install the snippet directly or use server-side measurement where appropriate.

### How should I measure Shopify, headless storefront, or server-side purchase events?

Use the browser Pixel for browser-side events and the [Conversions API](https://developers.openai.com/ads/conversions-api) for server-side events. If you pass server-side conversions, preserve and send the available click reference values, such as oppref, so events can be attributed correctly.

### Why do Ads clicks differ from Google Analytics sessions or landing-page visits?

Ads clicks measure ad interactions. Analytics sessions depend on page load, redirects, consent settings, browser blocking, UTM handling, attribution windows, and time zone settings. Compare the same date range and time zone, then use CSV exports to check campaign and ad-level activity.

### Do dynamic UTM macros work?

Static UTM parameters are supported when you add them to destination URLs. Dynamic macro syntax is not supported at this time.

### Why do conversions appear as one metric in reporting?

Ads Manager reporting may roll attributed standard and custom conversion events into the Conversions metric. Use your event names, Pixel or API implementation, campaign IDs, and CSV exports to compare against your internal reporting.

### Why do my conversion events show 0 in Ads Manager?

A conversion event can be firing or accepted and still show 0 in Ads Manager if it does not match the conversion event configured for the campaign.  
For standard events, the configured event type must match the event you send. For custom events, Ads Manager must use Event type: `Custom` and the custom event name must exactly match the event name you send. A matching display name alone is not enough.  
Also make sure the correct conversion is attached to the campaign before traffic starts. If you correct the configuration, test again with new eligible traffic. Historical events from the mismatched setup will not backfill.

### What should I include before contacting support about reporting?

Include the following:

* Ad account ID
* Campaign & Ad Names
* Date range and Time zone
* Ads Manager CSV export
* Analytics comparison
* Pixel ID
* Event names
* Sample conversion timestamps
* Screenshots of the discrepancy.

This helps support isolate implementation issues from reporting or attribution differences.
