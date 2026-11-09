<!-- source: https://help.openai.com/en/articles/20001558-use-the-chatgpt-ads-manager-plugin -->

# Use the ChatGPT Ads Manager plugin

Create and manage ChatGPT ads, analyze performance, and get recommendation-only reviews from ChatGPT or Codex.

Updated: 16 days ago

The ChatGPT Ads Manager plugin connects to the Ads Manager accounts you can access. Use natural language to explore account structure, draft and preview ads, make confirmed changes, understand performance, troubleshoot delivery, and get prioritized recommendations.

# What you can do

## Create ads from a website or brief

Share a public website or product page, or describe what you want to promote. The plugin can:

* Draft an ad title and description from your website or brief
* Find a suitable image on your website, use an image you provide, reuse eligible creative, or generate a new image after you choose that option
* Create one ad or a coordinated set of standard ad variants that use the same approved image, crop, and destination
* Show you a preview before uploading or saving anything
* Add the ad to an existing campaign and ad group, or create the missing campaign structure
* Upload the approved creative and create the ad with the status you confirm

Before creating anything, the plugin shows the landing page, image, copy, campaign settings, budget, targeting, and other relevant details for your approval.

For creative guidance, see [Create Ads for ChatGPT Ads](/en/articles/20001212).

## Create ads from an existing product feed

If your account has an eligible product feed, the plugin can create a product-feed campaign, ad group, and ad template. Product imagery comes from the feed, and each product-feed ad group supports one non-archived ad template.

See [Create campaigns from product feeds](/en/articles/20001268-create-campaigns-from-product-feeds).

## Manage campaigns, ad groups, and ads

You can ask the plugin to find an account, campaign, ad group, or ad by name. It can:

* Review current settings and statuses
* Create a campaign or ad group directly
* Preview an existing ad
* Update supported campaign, ad-group, and ad settings
* Pause, activate, or archive supported resources
* Replace an existing ad image

Each change is scoped to a specific resource. The plugin shows the account, current state, proposed state, and exact values that will change before asking for approval. After a successful update, it reads the resource back to verify the result.

See [Create Campaigns for ChatGPT Ads](/en/articles/20001210) and [Edit Campaigns](/en/articles/20001215-edit-campaigns).

## Analyze performance and conversions

The plugin can analyze results across an entire account or within a campaign, ad group, or ad. You can use it to:

* Compare and rank campaigns, ad groups, or ads
* Review impressions, clicks, spend, CTR, average CPC, and average CPM
* Analyze attributed conversions when conversion measurement is configured
* Examine trends over a selected date range
* Break down supported results by time, device, country, or child resource
* Review conversion sources and settings, or inspect recent raw conversion events for diagnostics

If you do not provide a date range, the plugin defaults to the trailing seven completed days in the account's local time zone. Results reflect the data currently available in Ads Manager, including normal reporting and attribution delays.

See [Measure Results](/en/articles/20001214-launch-your-campaign-and-monitor-performance) and [Conversion Measurement](/en/articles/20001409-conversion-measurement).

## Get one-time or recurring recommendations

Ask the plugin for a one-time review of your active campaigns, or schedule daily or weekly reviews to monitor performance over time. It checks readiness, delivery, and measurement, then prioritizes opportunities across budget, bidding, targeting, copy, and creative. Reviews include supporting evidence and clear next steps, but never change your account. You can preview a recurring review before confirming its schedule.

## Troubleshoot delivery

If a campaign is not delivering or scaling, the plugin can trace the path from account to campaign to ad group to ad to measurement. It identifies the earliest supported constraint, separates observed account evidence from interpretation, and provides a prioritized recovery plan. The diagnosis is read-only.

See [Troubleshooting Common Issues](/en/articles/20001217).

## Set up and administer a business ad account

Where self-serve setup is available, the plugin can guide a business advertiser through creating one ad account for its own business. It can help you:

* Enter business, website, account, industry, country, currency, and time-zone details
* Attach a logo, use an exact image link, generate a logo after you choose that option, or defer the logo
* Select the business that should own the account
* Review the final details and explicitly accept the applicable terms

For an existing account, the plugin can also list users and pending invitations, invite users, change roles, remove active users, and replace the account logo. A replacement logo enters brand review, and the current public logo stays active until the replacement is approved.

Identity verification, billing, payment, tax, and other readiness steps remain in Ads Manager. See [Ads Manager Beta Account Setup](/en/articles/20001213-ads-manager-beta-account-setup).

# How confirmations work

The plugin distinguishes between reviewing information and making a change:

* Reading account data, analyzing performance, troubleshooting, and recommendation reviews do not change your account.
* Drafting or previewing an ad does not upload or publish it.
* Uploading creative or creating or updating an account, campaign, ad group, ad, logo, or user access requires confirmation of the exact action.
* Account creation also requires explicit acceptance of the [Advertising Terms](https://openai.com/policies/advertising-terms/) and [Privacy Policy](https://openai.com/policies/privacy-policy/).

If any proposed detail changes after approval, the plugin shows the updated proposal and asks again before proceeding.

# Example requests

* “Create six ad variants from this product page.”
* “Create a product-feed campaign using my active feed.”
* “Compare my campaigns over the trailing seven completed days.”
* “Why isn't my Spring Launch campaign delivering?”
* “Give me a CMO-style review of my active campaigns.”
* “Set up a weekly recommendation-only review.”
* “Pause my Brand Awareness campaign.”
* “Invite my teammate to this ad account as a member.”
* “Help me create an ad account for my business.”

Including the account or campaign name and a date range will usually produce a more precise result. You do not need to provide internal resource IDs.

# Current limitations

* The plugin can only access accounts and resources available to your connected Ads Manager user. Available actions depend on your role and the features enabled for the account.
* A coordinated multi-ad request supports standard ads only, with no more than 50 new ads per request. The variants share one approved image, crop, and destination.
* A product-feed ad group supports one non-archived ad template. Business-agent ad creation is not supported.
* Billing, payment methods, tax details, legal identity information, and appeals must be completed directly in Ads Manager.
* Recurring reviews are recommendation-only and do not make automatic campaign changes.
* Recent raw conversion-event diagnostics are limited to the latest 50 events from the previous 15 minutes and are not historical reporting. The plugin does not receive conversion value, so it does not report revenue or ROAS.
* The plugin cannot override verification, policy review, account eligibility, or delivery decisions.

# FAQs

## Do I need an Ads Manager account to draft an ad?

No. You can draft and preview creative before selecting an account. An eligible Ads Manager account with write access is required to upload creative or save the ad.

## Can the plugin create multiple ads at once?

Yes. It can create a coordinated set of standard ad variants that share the same approved image, crop, and destination, up to 50 new ads per request. Product-feed ad groups support one non-archived ad template.

## Will the plugin make a change without asking me?

No. It shows the complete proposal and asks for confirmation before uploading creative or creating or updating Ads Manager resources.

## Can recurring reviews automatically optimize my campaigns?

No. One-time and scheduled reviews are read-only. They provide recommendations, and any supported follow-up change is presented separately for your approval.

## Can the plugin guarantee that a campaign will deliver?

No. It can identify supported blockers, analyze performance, and recommend next steps, but delivery still depends on account readiness, review, targeting, budget, available opportunities, and other Ads Manager factors.

## Can the plugin manage billing or identity verification for me?

No. It can check limited setup status and direct you to the appropriate next step, but billing, payment, tax, and legal identity workflows remain in Ads Manager.
