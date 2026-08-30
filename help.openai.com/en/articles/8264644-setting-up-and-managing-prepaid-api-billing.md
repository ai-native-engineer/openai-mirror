<!-- source: https://help.openai.com/en/articles/8264644-setting-up-and-managing-prepaid-api-billing -->

# Setting up and managing prepaid API billing

Purchase API credits, manage automatic recharges, and understand credit expiration, payment failures, and balance limits.

Updated: 3 days ago

Prepaid billing lets you purchase credits before using the API. Your credit balance decreases as you use the API. If your account has free credits, those are used before purchased credits.

New API accounts use prepaid billing. If you already use monthly billing, you can also purchase credits in advance. Those credits offset your monthly invoice.

Purchased credits expire after 1 year and are non-refundable. OpenAI cannot extend the expiration date of purchased credits or credit grants.

# Set up prepaid billing

Before you begin, make sure you have permission to manage billing for the API organization you want to fund.

1. Go to that organization’s [API billing overview](https://platform.openai.com/account/billing).
2. Select **Add payment details** and complete the payment-information step.
3. Choose your initial credit purchase amount. The minimum purchase is $5, and the default amount is $10.
4. Review **Use auto-reload** before confirming your purchase. It is turned on by default during setup. Turn it off if you do not want automatic credit purchases.
5. If you keep **Use auto-reload** on, set the balance threshold, the balance you want to restore to, and an optional monthly reload limit.
6. Confirm your credit purchase.

Your trust tier, which is based on your usage and payment history, determines the maximum credit balance your account can hold.

After a successful purchase, it may take a few minutes for your balance to update.

# Manage automatic recharges

**Auto recharge** adds credits when your balance falls below the threshold you set. The minimum recharge amount is $5. Your trust tier determines the maximum recharge amount.

The optional monthly recharge limit controls how much can be purchased through automatic recharges:

* Manual credit purchases do not count toward this limit.
* If an automatic recharge would exceed the remaining monthly limit, only the remaining amount may be added, provided it meets the minimum purchase requirement.
* If the monthly limit has already been reached, automatic recharges will not add more credits until the next month.

A recharge limit is not an API usage limit. It controls automatic credit purchases, not the amount of existing credits you can use.

# Add credits when your balance runs out

When a prepaid account runs out of credits, API requests begin returning a billing error. An error with the code credit\_balance\_exhausted means the organization has no prepaid credits remaining.

To purchase more credits:

1. Go to your [API billing overview](https://platform.openai.com/account/billing).
2. Select **Buy credits** or **Add to credit balance**, whichever appears.
3. Complete the credit purchase.

Allow a few minutes for the updated balance to appear before trying again.

## Understand a negative balance

API access may not stop immediately after your credits run out. Usage processed during this delay can appear as a negative credit balance. That amount is deducted from your next credit purchase.

Do not rely on the prepaid balance as an instantaneous spending cutoff.

# Resolve payment and credit issues

## Initial payment fails

If your initial payment fails, you receive an error, and no credits are added to your account.

## Automatic recharge fails

If a recharge payment fails, you receive an email. On prepaid billing, API usage stops when the available balance is exhausted, subject to the processing delay described above.

## Payment is disputed or refunded

If a payment is disputed or refunded, credits equivalent to that amount are removed from your account.

# Check other API limits

A positive credit balance does not mean a request is below every API limit. Request and token rate limits, your organization’s approved monthly usage limit, and any enforced spend limits are separate from your prepaid balance.

For rate-limit errors, see: [Troubleshooting API rate limits and 429 errors](https://help.openai.com/articles/5955604).

For other billing-related errors, check the [API error-code guide](https://developers.openai.com/api/docs/guides/error-codes) before purchasing additional credits.
