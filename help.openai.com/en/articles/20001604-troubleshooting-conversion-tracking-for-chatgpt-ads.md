<!-- source: https://help.openai.com/en/articles/20001604-troubleshooting-conversion-tracking-for-chatgpt-ads -->

# Troubleshooting conversion tracking for ChatGPT Ads

Find the next step when events are missing, requests fail, or conversion reports differ.

Updated: 9 days ago

Use this guide if events are missing, requests fail, or Ads Manager disagrees with your business records. Start with one completed purchase, submitted lead, or other action. Note what happened and when, then choose the question below that fits.

An event records an action, such as a purchase. The Pixel sends events from a visitor's browser; the Conversions API (CAPI) sends them from your server. Ads Manager collects these events in a data source. Attribution determines which ad gets credit. An attribution window sets how long after an ad interaction an action can qualify.

# FAQ

## 1. Where should I start?

Identify the action you want to measure, what sends it, and the ad account and Pixel ID used. Your setup might use the Pixel, CAPI, a partner integration, or a combination. CAPI needs a Pixel ID even if you have not installed the browser Pixel.

For first-time setup, see: [Conversion Measurement](https://help.openai.com/articles/20001409) and [Conversion Tracking](https://developers.openai.com/ads/conversion-tracking). Your developer can use the [Pixel](https://developers.openai.com/ads/measurement-pixel), [CAPI](https://developers.openai.com/ads/conversions-api), and [Supported Events](https://developers.openai.com/ads/supported-events) guides. Keep CAPI requests and keys on your server.

If a partner manages your integration, use the [measurement partner setup guide](https://help.openai.com/articles/20001416) or [mobile measurement partner setup guide](https://help.openai.com/articles/20001372). For a HubSpot connection, see: [Setting up ChatGPT Ads in HubSpot](https://help.openai.com/articles/20001522).

For an existing setup, check each step:

* Did the action send an event request?
* Did the request return an error, or was it accepted?
* Can you confirm that the correct data source received the event?
* Was the event credited to an ad in the campaign report?

## 2. My Pixel is installed. Why don't I see purchases or leads?

The Pixel can load without sending the purchase or lead event you need. Ask your developer to check one completed action:

* Check the event name, Pixel ID, and the page or callback that sends it. A page view is not a completed purchase.
* Confirm the Pixel initializes before sending the event, including when a tag manager loads it.
* Check the browser console and network request. A tag manager's “fired” message alone does not confirm that the event was sent. Pixel debug mode can help.
* Check whether consent choices, browser blocking, or your site's security policy prevented the request.
* Check signed-in pages, checkout, booking sites, redirects, and embedded forms. A working Pixel on the landing page does not confirm tracking elsewhere.

If no request was sent, fix that step first. Waiting for reporting will not help. Use the [Pixel troubleshooting guide](https://developers.openai.com/ads/measurement-pixel#troubleshooting) before adding another integration.

## 3. What should I do if an event is rejected, times out, or returns a server error?

Save the response code, exact error, request time, and event ID. Ask your developer to check the event format, Pixel ID, and key. CAPI event requests use a Conversions API key for the same ad account. Setup, management, and reporting requests use the separate Advertiser API key. Do not send API keys to Support.

With CAPI batches, one invalid event can cause the whole batch to fail.

CAPI requires the original action time in Unix milliseconds. The event must be within the last 7 days and no more than 10 minutes in the future. This submission limit is separate from the attribution window. Do not change an old event's time to make it pass.

A timeout or server error may leave you unsure whether the event arrived. Check the original request and any receipt records. If you retry the same action, keep its original event ID and timestamp. A new ID could make it look like another action.

Investigate a rejection or persistent request failure promptly. The 24–48-hour reporting estimate does not apply to these errors. For request requirements, see: [Conversions API](https://developers.openai.com/ads/conversions-api).

## 4. I see that the event was accepted. Why isn't it in the report?

Acceptance does not mean an event was credited to an ad. Check what the response confirms and whether the request used the correct data source. In CAPI, validate\_only set to true checks the events without saving them.

For a new event, your developer can check [recent events](https://developers.openai.com/ads/conversion-tracking#monitoring-events), where available. This shows a recent sample, not a full history or an attribution result.

If you cannot check receipt, contact Support with the original response and a sample event. Tell us which checks you completed; you do not need to find the cause first.

If receipt is confirmed, continue to question 5. Do not resend the event with new IDs just because the campaign report has not changed.

Attributed conversions can take approximately 24–48 hours to appear, and recent totals may change during processing. This does not guarantee that every accepted event will appear or confirm that it was received. See: [Measure Results](https://help.openai.com/articles/20001214).

## 5. Events are being received. Why does the campaign still show zero conversions?

Before changing the integration, check:

* Is the intended data source connected to the correct account?
* Does the event you send match the campaign's conversion setting? For custom events, check the custom type and exact event name. A matching display label is not enough.
* Was the correct conversion attached to the campaign before the activity you are checking?
* Did the action follow an ad click or view that qualifies under the attribution settings?
* Are you viewing the correct campaign, event column, dates, and reporting time basis?

Matching information helps connect an event to an ad, but does not guarantee credit. Preserve the real OpenAI click reference, oppref, through the visit and include it in server events when available. Never invent a reference or use another visitor's.

Check browser and server events separately. A reference or customer field available to the Pixel may be missing from the server event.

A conversion-optimized campaign's selected goal cannot be changed after creation. To use a different goal, create a new campaign. Custom events cannot be optimization goals. See: [Conversion-optimized Campaigns](https://help.openai.com/articles/20001412).

After fixing a configuration mismatch, check new eligible activity. Do not assume the change repairs earlier reports. For matching rules, see: [Conversion Measurement](https://help.openai.com/articles/20001409).

## 6. Why do Ads Manager, our analytics tool, and our CRM disagree?

Compare the same actions and reporting rules. Your CRM may count every purchase; an ad report counts purchases credited to that platform. Different platforms can credit the same purchase differently.

In Ads Manager, **Conversions** combines click-through and eligible view-through conversions when the view-through reporting window is 1 day. With a 0-day view window, it counts click-through conversions only. Use the same setting when comparing reports.

For example, someone clicks an ad, returns directly later, and buys. One tool may label the visit “Direct,” while another credits the earlier ad. That difference alone does not mean the purchase was counted twice.

If the traffic-source labels differ, check the landing URL and tracking parameters used on that visit. Current campaign settings may differ from those used earlier.

Compare:

* Account, campaign, event type, filters, and reporting level.
* Date range, time zone, and whether dates refer to the ad interaction or the conversion itself.
* Click-through and view-through settings and the exact metric or column selected.
* Recent processing delays, duplicate handling, consent, and available matching information.
* Modeled conversions, where available, which can differ from directly recorded transactions.
* For values, currency, units, and whether the comparison uses the whole order or individual items.

For revenue, compare tax, shipping, discounts, and fees. Check that browser and server copies send the same order value. **Order Created Sales** and **Order Created ROAS** count only attributed order\_created events.

Imported GA4 activity includes events across the selected property's traffic sources. Those totals are not campaign-attributed conversions. See: [Connect Google Analytics 4 to OpenAI Ads Manager](https://help.openai.com/articles/20001562).

For API comparisons, record the endpoint and set the reporting options explicitly. An omitted setting may not match Ads Manager. Reports may also include different events: some cover campaign goals but not other tracked actions. An event missing from one report does not prove it was never received.

Use the same settings for a CSV comparison and keep the unedited exports. See: [Measure Results](https://help.openai.com/articles/20001214) for Ads Manager views and [Reporting](https://developers.openai.com/ads/reporting) for API options.

## 7. Will using the Pixel and CAPI count a purchase twice?

To avoid counting the same action twice, use the same Pixel ID, event name, and event ID in its browser and server copies. The event ID field is id in CAPI and event\_id in the Pixel. Use the same custom event name on both sides too.

Keep the same ID when retrying an action; use a new ID for each different action. Check for duplicate tags, repeated page loads or callbacks, and partner integrations that may already send the event.

Do not resend a duplicate to change the original event's value or matching information. Check the documented behavior before attempting a correction. See: [browser and server deduplication](https://developers.openai.com/ads/conversions-api#deduplicate-browser-and-server-events).

## 8. We use Shopify. Do we need another integration?

Check your Shopify connection before adding another integration. Confirm the connected ad account and Pixel, then check which events the app sends for your store.

If you also use custom tags, checkout code, or a server sender, check whether they send the same events. Shopify setups can use different combinations of browser and server tracking. See: [Set up ChatGPT Ads for Shopify](https://help.openai.com/articles/20001523).

## 9. How should we handle consent and testing?

Only send data you are permitted to share, and respect visitors' consent choices. Your developer should follow the integration's consent and supported matching-data guidance, including any required normalization and hashing. Do not remove consent controls to increase reported conversions or improve a score.

Measurement consent and opt\_out serve different purposes. The opt\_out option concerns personalization; it does not stop all measurement requests. Ask your developer to check consent handling in both browser and server integrations.

Record the time, name, and ID of one test action. Check whether it was sent, validated, and received. A successful implementation test does not show that an ad qualifies for credit.

CAPI's validate\_only option checks events without saving them. Pixel debug mode logs activity but does not keep test events out of reporting. Label tests in your records, and do not invent purchases or change event times to force a result.

## 10. Does a low or unavailable Event Quality Score mean tracking is broken?

Not by itself. Event quality assesses the information received from a data source. It does not tell you how many conversions received ad credit. A low or unavailable score alone cannot establish whether tracking works.

Check that recent real actions are captured correctly, then investigate the warning. Do not send extra events or invented identifiers to raise the score. For checks and refresh timing, see: [Understand and improve event quality](https://help.openai.com/articles/20001513).

## 11. What should I include when contacting Support?

Tell us what you expected, what happened, when it started, and what you checked. Include what you have from this list:

* Ad account ID, Pixel ID or data source, and affected campaign and ad identifiers.
* Integration type and the exact event name, including any custom event name.
* One or two existing sample event IDs and action timestamps, with the time zone.
* For request failures or uncertain receipt: response code, exact error, request time, any returned request ID or CF-Ray, and a redacted payload or log excerpt.
* For reporting differences: date range, reporting time basis, attribution settings, selected columns, CSV export, and a comparison showing the same scope.
* Relevant screenshots and any recent setup changes, including a separate checkout or partner integration.

Tell us whether you confirmed the event was sent, accepted, or received, or whether you only checked the report. You can ask for help even if you cannot complete these checks.

Remove API keys, authorization headers, passwords, cookies, and unnecessary customer information from attachments. Report errors or a previously working integration that suddenly stops promptly. Do not wait for the reporting window to pass.
