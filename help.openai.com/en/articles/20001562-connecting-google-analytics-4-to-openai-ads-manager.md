<!-- source: https://help.openai.com/en/articles/20001562-connecting-google-analytics-4-to-openai-ads-manager -->

# Connecting Google Analytics 4 to OpenAI Ads Manager

Connecting Google Analytics 4 (GA4) lets advertisers share GA4 data with OpenAI to support campaign optimization, where eligible, and compare attribution results between OpenAI Ads Manager and Google Analytics.

Updated: yesterday

**Availability**: This feature is in beta. Reach out to your account manager to get early access.

Connect Google Analytics 4 (GA4) to share analytics data with OpenAI for attribution comparisons and, where eligible, campaign optimization.

# Before you begin

You’ll need:

* Access to the advertiser account you want to connect.
* A Google account with at least Viewer access to the relevant GA4 property.
* Your organization’s authorization to connect the property and allow OpenAI to retrieve and use its GA4 data.

An advertiser account can have one GA4 connection with one selected property. Make sure you use a Google account that can access that property. Your GA4 administrator can help verify your access.

If your organization restricts third-party Google apps, ask your Google Workspace administrator to review the connection request. Don’t bypass Google security warnings.

# Data access and terms

Connecting GA4 gives OpenAI read-only access to data from the property you select.

OpenAI imports aggregate reports from your selected GA4 property, including dates, event names and counts, source/medium, campaign names, key-event counts and purchase revenue. The initial import covers the previous 30 completed days across traffic sources, using your property’s time zone.

Data is updated daily.

We use this data for attribution comparisons and, where eligible, campaign optimization. You can disconnect the property in Ads Manager’s GA4 connection settings.

Connecting GA4 authorizes OpenAI to retrieve and use the selected property’s data on your organization’s behalf under the [Advertising Terms](https://openai.com/policies/advertising-terms/). You must have authority to bind your organization. You also confirm that your organization has provided the required notices, has and will maintain the necessary rights, consents and lawful bases, and will comply with applicable law and those terms.

OpenAI’s collection and use of personal data through this integration is covered by the [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy/).

# Connect your property

1. In Ads Manager, open the advertiser account you want to connect.
2. Go to Conversions → Data Sources, select Create, then choose Google Analytics 4.
3. Review the connection information and terms, then select Agree.
4. Choose the Google account that has access to your property. Review the request for read-only Google Analytics access, then select Allow.
5. Back in Ads Manager, choose your GA4 property. Check its name and property ID, then select Select property and import.

# Map your events

In **Preview data mapping**, review the mappings between GA4 events and Ads Manager events. Use **Search GA4 event** to find an event, then choose the corresponding Ads Manager event from its dropdown. For example, `generate_lead` can map to **Lead Created**, and `page_view` to **Page Viewed**. Choose mappings that reflect what each event represents in your implementation. Select **Save** to save your changes.

# Review your imported data

Open your GA4 connection from Data Sources to check its status, latest successful sync and imported activity.

Today’s activity is excluded from the initial import. The seven-day trend compares the most recent seven complete days with the seven days immediately before them.

The mapping screen lists distinct event names. The Events value on the data-source row counts imported activity, rather than distinct event names.

These totals cover the property’s traffic across sources, not just purchases, key events or activity attributed to OpenAI ads. They aren’t campaign conversion counts or ROAS. When comparing with GA4, use the same property, reporting dates, time zone and filters.

# Show the GA4 campaign column

In **Campaigns**, open **Customize columns**. Under **Conversion Events**, select **GA4 Conversions**, then select **Save changes**.

# Manage your connection

**Reconnect**: If Ads Manager requests authorization again, open the connection from Data Sources, open the property’s menu, and click edit. When you see Reconnect required, select Reconnect, then Agree. Use a Google account that still has access to the selected property.

**Disconnect.** To stop new imports, open the property’s menu and select Disconnect. Your previously imported reports are kept. To connect the property again, choose Reconnect from the same menu and follow the Google sign-in steps above.

For persistent connection or import errors, contact your OpenAI Ads support contact with the error message.

# Troubleshooting

## Missing GA4 property

Check that you’re signed in to the correct Google account and have access to the specific property. If needed, ask your GA4 administrator to verify your access.

## Blocked Google authorization

Your organization may restrict third-party Google apps. Ask your Google Workspace administrator to review the request. Do not bypass a Google security warning.

## Missing events or differing totals

Confirm that the selected property has data for the completed dates shown. In GA4, compare event counts for the same property, dates, and time zone. Reports filtered to one event or traffic source may differ from the property-wide total.

## Out-of-date data

Check the last successful sync and reconnect if you’re asked to authorize the connection again. If an error persists, contact your OpenAI Ads support contact with the GA4 property ID and the error message.
