<!-- source: https://help.openai.com/en/articles/20001416-set-up-measurement-partner-integrations -->

# Set up Measurement Partner Integrations

Connect a measurement partner to ChatGPT Ads.

Updated: 8 hours ago

ChatGPT Ads supports integrations with select measurement partners to help advertisers measure campaign performance and understand actions taken after someone engages with an ad. Depending on the partner, integrations may support capabilities such as conversion tracking, attribution, reporting, and optimization across web, app, and offline activity. Available capabilities and setup options vary by partner; refer to the partner’s documentation for current details.

For specific mobile measurement partner integrations we support, [view the setup guides here](/en/articles/20001372-set-up-mobile-measurement-partner-integrations).

## **Before you begin**

You’ll need:

* An active Ads Manager account
* A Pixel ID and Conversions API key from the Conversions section of Ads Manager
* A data source containing the conversion events you want to send
* The appropriate permissions in your data partner
* A list of the standard or custom events you want to send to ChatGPT Ads

See [OpenAI’s measurement documentation](https://developers.openai.com/ads) for information about supported events, the JavaScript Pixel, and the Conversions API.

These are the current measurement partners supported for ChatGPT Ads. We’ll update this article as additional partner integrations become available.

## Set up Hightouch

1. In Hightouch, open Destinations, click Add destination, and select ChatGPT Ads (OpenAI).
2. Authenticate the destination by entering your ChatGPT Ads Pixel ID and API key.
3. Select the model containing the events you want to send to ChatGPT Ads and create a sync to the OpenAI destination.
4. Configure record matching and map the event properties you want to send to ChatGPT Ads. Make sure the event model uses a truly unique primary key so Hightouch sends every event.

For complete instructions, see the [HighTouch setup guide](https://hightouch.com/docs/destinations/open-ai).

## Set up LiveRamp

1. Reach out to your LiveRamp rep to request access to the OpenAI integration.
2. If you haven't already, set up a batch file or streaming event feed to LiveRamp. For more instructions on setting up streaming conversion events to LiveRamp, see [here](https://docs.liveramp.com/privacy-manager/en/implement-liveramp-online-conversions-api-program-with-ats-for-web.html). For batch events, such as in store offline conversions, see [here](https://docs.liveramp.com/connect/en/using-a-universal-file-for-multiple-attribution-programs.html). Both offline and online conversions can be either streamed via API or batched in flat files to LiveRamp.
3. [Create a destination account for OpenAI](https://docs.liveramp.com/connect-2/en/the-openai-conversions-api-program-for-offline-conversions.html) using your pixel ID and Conversions API key
4. Map your events using the “Event Types” section of the document [here](https://docs.liveramp.com/privacy-manager/en/universal-events-and-parameters-for-online-conversions-api.html).
5. Check your OpenAI ads manager to confirm successful receipt of your events.

For complete instructions, see the [LiveRamp setup guide](https://docs.liveramp.com/connect-2/en/the-openai-conversions-api-program-for-offline-conversions.html).

## Set up Triple Whale

1. In ChatGPT Ads Manager, go to **Settings**, select **General**, and create an API key for Triple Whale.
2. In Triple Whale, go to **Data > Integrations**, find **ChatGPT Ads**, and click **Connect**.
3. Enter your ChatGPT Ads API key and click **Save**.
4. Continue applying Triple Whale UTMs to your ChatGPT Ads campaigns to attribute traffic, orders, and customer journeys in Triple Whale.

For complete instructions, see the [Triple Whale setup guide](https://kb.triplewhale.com/en/articles/15590515-how-to-connect-chatgpt-ads-to-triple-whale).

**Note:** Triple Whale also offers data enrichment through [Sonar Optimize](https://kb.triplewhale.com/en/articles/15649724-sonar-optimize-data-enrichment-for-chatgpt-ads).

## Was this article helpful?
