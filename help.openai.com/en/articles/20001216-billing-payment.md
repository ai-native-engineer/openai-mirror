<!-- source: https://help.openai.com/en/articles/20001216-billing-payment -->

# Billing & Payment

Learn how billing works for ChatGPT Ads.

Updated: 9 days ago

This article explains how billing works for ChatGPT Ads, including what must be configured before campaigns can deliver, how charges are applied, how spend is controlled, and what to do if you need help with a billing issue.

## Set up billing before delivery starts

Before campaigns can begin delivering, billing must be fully set up in Ads Manager Beta. This involves two steps:

* Create a billing profile: enter your business name, business address, and invoice delivery email. The invoice delivery email is used for invoices and other billing-related communication.
* Add a payment method: enter your credit card details and billing address information. When you add a card, OpenAI may place a temporary $100 authorization hold to verify the payment method. The hold is released automatically and may remain on your card for up to 3 days.

## How billing works

ChatGPT Ads currently uses a postpay billing model that charges advertisers after ads have been delivered. As your campaigns run, spend accrues on your account and charges are applied to the payment method saved in Ads Manager Beta.

Currently, ChatGPT Ads can be purchased on a cost per thousand impressions (CPM) basis or a cost per click (CPC) basis based on the campaign objective you select.

* Select a Views objective to buy on a cost per thousand impressions basis (CPM) and optimize for reach. With this objective, you are billed for impressions served.
* Select a Clicks objective to buy on a cost per click basis (CPC) and optimize for traffic. With this objective, you are billed for each click.

Your campaign budget controls the maximum amount you are willing to spend for a campaign. When you create a campaign, choose either a daily budget or a campaign budget. A daily budget sets the maximum you are willing to spend per day, while a campaign budget sets the maximum you are willing to spend across the campaign. You can change the budget amount after creation, but you cannot change the budget type. Actual spend may vary based on delivery, user engagement, and the pricing model selected.

In Ads Manager Beta, you can monitor spend and performance using metrics such as impressions, clicks, spend, CTR, Average CPC, Average CPM, and conversions if [conversion measurement](https://developers.openai.com/ads/measurement-pixel) is set up.

## When charges happen

Your saved payment method is charged when your account reaches its assigned payment threshold.

When you sign up for an Ads Manager Beta account, your account is assigned a payment threshold that determines how much unpaid spend can accrue before your saved payment method is charged. This is not the same as a campaign budget and is not an account spend cap.

Approved advertisers typically start with a lower payment threshold and we may increase your payment threshold automatically over time based on successful payment history and other factors.

For example, if your account has a $25 payment threshold, your card will be charged once your account accrues $25 in unpaid spend. After a successful payment, your outstanding balance will be reduced by the payment amount. If delivery continues, your account can accrue spend again until it reaches the threshold or the end of the month.

If your account still has an outstanding balance at the end of the month, that balance will also be charged at the end of the month even if you have not yet reached your payment threshold. You will receive an emailed receipt for each successful payment.

You cannot manually change your payment threshold, and our support team will not change thresholds on behalf of advertisers.

## If a payment fails

If a payment fails after your account reaches its payment threshold, your ads may stop delivering until the billing issue is resolved. You will receive an email notification if an invoice payment fails. If this happens, your campaigns, ad groups, and ads may show as Not serving. You can open the status tooltip for more detail and update your payment method in Ads Manager Beta.

Eligible advertisers can move to higher payment thresholds over time based on successful payment history. Failed charges, disputes, and chargebacks can pause progression to higher limits.

## Billing FAQ

### Is my payment threshold the same as my campaign budget?

No. Your payment threshold controls when your saved payment method is charged for accrued spend. Your campaign budget controls how much the campaign can spend. Reaching a payment threshold does not mean a campaign has reached its budget, and a campaign budget is not the same as an account spend cap.

### Can support increase or lower my payment threshold?

No. Payment thresholds are assigned and may increase automatically over time based on successful payment history and other factors. Support does not manually change thresholds for advertisers.

### Can I remove a payment method?

If self-serve removal is not available, make sure any outstanding balance is resolved and pause or end campaigns you do not want to continue. For help with account deactivation or payment method questions, contact [ads-support@openai.com](mailto:ads-support@openai.com) with your ad account ID and billing details.

### Can I change my billing country, currency, or legal entity after setup?

Billing country, currency, and legal entity details are tied to account setup and billing records. They may not be self-serve editable after account creation. If the wrong details were entered, contact support with the ad account ID, current details, requested details, and reason for the change.

### Can I use a credit card issued in a different country?

Your billing information and payment method should match the business entity and country or region used when your Ads Manager account was created.

For example, if your advertiser account was created for a U.S.-based business, you should use a U.S.-based billing address and payment method. A card or payment method associated with a different country may not be accepted.

If you need to bill under a different country, region, or legal entity, you may need to create a separate advertiser account using the correct business and billing information.

### Why are my ads not serving after a failed payment?

Ads may stop delivering while a payment issue is unresolved. Update the payment method in Ads Manager Beta, confirm the saved card can be charged, and check the campaign, ad group, and ad status tooltips for more detail.

## If you think a billing number is incorrect

Start by gathering the full context before reaching out to support at [ads-support@openai.com](mailto:ads-support@openai.com).

A strong billing support request should include:

* Invoice ID or charge ID
* Date range in question
* Amount in question
* Affected campaign IDs
* Relevant reporting screenshots or exports
