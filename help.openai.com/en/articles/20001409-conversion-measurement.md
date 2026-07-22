<!-- source: https://help.openai.com/en/articles/20001409-conversion-measurement -->

# Conversion Measurement

Understand how conversion measurement works and how to improve measurement quality.

Updated: yesterday

Conversion measurement helps you understand the actions people take after clicking an ad in ChatGPT, such as making a purchase, submitting a lead, or completing a registration.

To measure conversions, create a data source in Ads Manager and send conversion events using the OpenAI Pixel, the Conversions API, or both. OpenAI evaluates those events against the conversion events configured for your campaign and the applicable attribution window.

To learn where the Conversions metric appears in Ads Manager and how to export reporting data, see [Measure Results](https://docs.google.com/document/d/1QSDGbNrx75mX1PFmmlgan-4fC6M_ZFX0WQnZ30jZZr4/edit?tab=t.y2w710yvuezp).

## How conversions are measured

A conversion can be reported when:

* OpenAI receives an event from a data source connected to your ad account
* The standard or custom event matches a conversion event configured for the campaign
* The event occurs within the applicable attribution window
* OpenAI can connect the event to an eligible ad click using available measurement signals

These signals may include the OpenAI click reference, eligible advanced matching information, and modeled measurement where available.

The OpenAI click reference, called **oppref**, is appended to the end of the landing page URL in the following format: [www.openai.com?oppref=gAAAAAb123](http://www.openai.com?oppref=gAAAAAb123). The OpenAI Pixel captures **oppref** and stores it in a first-party cookie so it can be associated with later conversion events. When available, advertisers can include **oppref** in Conversions API calls.

For more resilient measurement, you can use the [OpenAI Pixel](https://developers.openai.com/ads/measurement-pixel) and [Conversions API](https://developers.openai.com/ads/conversions-api) together. When the same conversion is sent through both methods, use the same event ID so OpenAI can deduplicate it. See the OpenAI Pixel, Conversions API, and [supported events](https://developers.openai.com/ads/supported-events) documentation for setup instructions.

## Advanced matching and measurement quality

### Advanced matching

Advanced matching can help improve measurement quality when direct click information is incomplete. For example, an advertiser may send eligible first-party information, such as normalized and hashed contact information, with a conversion event. This can help provide a clearer view of campaign performance and support better optimization.

### Modeled measurement

Where modeled measurement is available, OpenAI may also use aggregated patterns from observed conversions to estimate attribution for otherwise unattributed advertiser-reported conversion events. This can help make conversion measurement more complete, which gives campaigns better context for optimization. Reported conversion totals may include modeled conversions where available.

Conversion data should be shared only when permitted and in compliance with applicable laws and OpenAI terms. Only send conversion data after providing clear and comprehensive information to users about the data you collect on your site or app and obtaining all necessary consents where required by law. OpenAI uses privacy and security safeguards for conversion data, and Ads Manager reporting is designed to show campaign performance rather than individual-level user activity. The developer documentation includes the latest formatting and hashing guidance.

## How to improve measurement quality

Higher-quality conversion signals can make reporting more useful and give campaigns better context for optimization.

* Install the OpenAI Pixel across relevant pages, and send conversion events when the intended action occurs
* Preserve the OpenAI click reference (**oppref**) through redirects and landing-page navigation
* Include the click reference (**oppref**) with server-side events when it is available
* Provide eligible advanced matching data when permitted and supported
* Use the Pixel and Conversions API together, with the same [event ID](https://developers.openai.com/ads/conversions-api#deduplicate-browser-and-server-events) for the same conversion

## Why OpenAI and third-party analytics may differ

OpenAI Ads Manager, your analytics provider, and other ad platforms may report different conversion totals. Common reasons include:

* Different attribution methods or attribution windows
* Event timestamps, reporting time zones, or date boundaries
* Browser, consent, and storage conditions that affect available measurement information
* Different deduplication behavior
* Campaign or conversion-event configuration
* Modeled conversion reporting, where available

A difference does not necessarily indicate an error.
