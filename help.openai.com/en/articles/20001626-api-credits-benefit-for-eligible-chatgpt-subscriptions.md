<!-- source: https://help.openai.com/en/articles/20001626-api-credits-benefit-for-eligible-chatgpt-subscriptions -->

# API credits benefit for eligible ChatGPT subscriptions

Learn eligibility, activation, monthly grants, API usage, billing, and subscription changes for the ChatGPT-linked API credits benefit.

Updated: 8 days ago

Learn how to claim and use API credits included with eligible ChatGPT Pro and Business subscriptions.

Eligible paid ChatGPT Pro and ChatGPT Business subscribers can claim free API credits as a subscription benefit to build apps and agents with the OpenAI API. The grant funds one linked API organization. It does not increase your ChatGPT or signed-in Codex usage allowance, personal usage-credit balance, or Business workspace credit balance.

The benefit is subject to [API terms](https://openai.com/policies/services-agreement/) and [policies](https://openai.com/policies/usage-policies/), including [API rate limits](https://developers.openai.com/api/docs/guides/rate-limits). Check the limits for your organization and models in [organization limits](https://platform.openai.com/settings/organization/limits).

ChatGPT and API billing remain separate. For settings and charges, see [Managing billing for ChatGPT and the API platform](/en/articles/9039756).

# Eligibility and availability

The included plans are Pro 100, Pro 200, Pro 500, and eligible Business workspaces with paid Standard or Premium seats. Plus, free trials subscriptions do not qualify for this offer. Enterprise, Edu and legacy Codex seats are not established eligible plans or seats for this offer.

Your paid eligible subscription must have been active for at least 7 days before claiming.

An eligible subscription does not itself confirm that a grant has been issued. Complete activation and check the receiving API organization.

# Credit amounts

| **Eligible monthly subscription** | **Full-period API allowance** |
| --- | --- |
| Pro ($100 tier) | $100 per monthly billing period |
| Pro ($200 tier) | $200 per monthly billing period |
| Pro ($500 tier) | $500 per monthly billing period |
| Business Standard seats | $20 per paid Standard seat, pooled for the workspace |
| Business Premium seats | $100 per paid Premium seat, pooled for the workspace |
| Business workspace cap | $500 total per monthly billing period across Standard and Premium contributions |

For a monthly Business workspace, calculate the full-period allowance as the smaller of ($20 × paid Standard seats + $100 × paid Premium seats) and $500. For example, 5 Standard seats and 3 Premium seats contribute $100 + $300 = $400. Ten Standard seats and 4 Premium seats contribute $600 before the cap, so the workspace allowance is $500.

Your first grant is prorated for the time remaining in the paid billing period. A full-period allowance is not necessarily the amount shown when you claim partway through a period. Review the amount displayed in ChatGPT billing before confirming.

Business workspaces billed annually upfront receive the full year’s grant at once, capped at $6,000 per annual billing cycle. The first grant is prorated for the time remaining in the current billing cycle and expires when that cycle ends.

# Before you activate

* Use the same email address for the ChatGPT account and the API account used to link.
* For Pro, activate as the subscription owner and an owner of the receiving API organization.
* For Business, the person activating must own both the ChatGPT workspace and the receiving API organization. Workspace membership or an admin role alone is not enough.
* Have permission to manage billing in the API organization. A custom billing role alone does not replace API organization ownership.
* Choose the intended API organization carefully. One eligible ChatGPT subscription or workspace can link to one API organization, and an API organization can have only one such active link.
* If you are new to the API, you can link your subscription to your Personal API Organization using the email address associated with your eligible ChatGPT subscription. You do not need to finish API onboarding before claiming in ChatGPT. A ChatGPT seat does not grant other workspace members API organization or project access.

# Activate your credits

## Claim in ChatGPT

1. Sign in to the ChatGPT account that owns the eligible Pro subscription, or select the eligible Business workspace as an owner.
2. For Pro, open [Settings → Billing](https://chatgpt.com/settings/billing) in ChatGPT. For Business, open your workspace’s billing settings in ChatGPT or the [Admin Console](https://admin.openai.com/).
3. Find the API credits benefit and start the claim flow.
4. Review the API organization that will receive the credits. If you own multiple eligible organizations, select the one you want to link.
5. Confirm to activate the benefit.
6. Open [API Platform billing settings](https://platform.openai.com/settings/organization/billing/overview) to see the credits in the linked organization.

## Claim in API Platform

1. Sign in to [API Platform](https://platform.openai.com/) with the email associated with your eligible ChatGPT subscription.
2. Select the API organization you own and want to link.
3. Open [Billing](https://platform.openai.com/settings/organization/billing/) and find the API credits benefit.
4. Select the eligible subscription or Business workspace you own.
5. Review the offer and confirm to activate the benefit.
6. Open API Platform billing settings to see the credits in the linked organization.

See [API credits for ChatGPT subscribers](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) for both claim paths and the [API quickstart](https://developers.openai.com/api/docs/quickstart) for your first request.

# Renewal and expiration

After activation, credits are granted automatically when the eligible subscription renews, while the benefit remains available. You do not need to claim again at each renewal.

Monthly grants expire at the end of the subscription billing cycle. Unused credits do not roll over.

Annually prepaid Business workspaces receive the full-year grant upfront, with expiration at the end of the annual billing cycle. A first grant is prorated for the remaining paid term; unused credits do not roll over.

The benefit may change or be removed in the future. Automatic renewal grants depend on the benefit remaining available and your subscription remaining eligible. See [Service Credit Terms](https://openai.com/policies/service-credit-terms/).

# Use the credits and check your balance

Credits apply only to the linked API organization. Promotional credits are used before purchased API credits. API calls and Playground activity draw on the organization's applicable API balance.

An API organization owner can open the [API billing overview](https://platform.openai.com/account/billing/overview). Select the organization you linked and open [Credit grants](https://platform.openai.com/settings/organization/billing/credit-grants) to review its credit-grant details.

For activity and cost reporting, see [Reviewing API usage and costs](/en/articles/10478918). Usage reports and credit-grant records answer different questions; a reported API cost is not necessarily the cash charged after credits are applied.

Business teammates need API organization and project access separately. Their ChatGPT seat does not grant that access. API usage and API limits do not transfer into ChatGPT Business.

The free credits cover paid API Platform usage billed to the linked organization, including Responses and Chat Completions, Agents, Decisions, GPT-Live and Realtime, Images, and built-in tools with their applicable usage and storage charges. See the [developer guide](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) for API coverage and setup.

This benefit does not cover Codex usage through API keys. These API credits also do not increase your ChatGPT or signed-in Codex usage limits.

# Payment methods, limits and running out of credits

You do not need to add an API payment method to use an active promotional grant. Adding an API payment method or purchasing API credits is separate from paying for your ChatGPT subscription.

Your [usage tier](https://developers.openai.com/api/docs/guides/rate-limits#usage-tiers) will update automatically as you qualify for higher tiers.

A credit balance does not remove request-rate, token-rate, model, organization or project limits. See [Troubleshooting API usage and spend limits](/en/articles/6614457).

Your organization uses the free API credits before purchased API credits. If purchased credits remain after the free balance runs out, API requests continue using them. If no credits remain, requests fail with HTTP 429 and error code credit\_balance\_exhausted. To continue, add paid API credits in [billing settings](https://platform.openai.com/settings/organization/billing/overview) or set up Auto Recharge; see [Setting up and managing prepaid API billing](/en/articles/8264644). Review the recharge threshold, target balance and monthly purchase limit before enabling it.

# Subscription changes and linked organizations

Scheduling cancellation does not automatically refund a subscription. Future grants stop when the subscription ends or becomes ineligible. Cancellation alone does not revoke credits already issued; they remain usable until the end of the current billing cycle. Downgrading to an ineligible plan, such as Plus, Go or Free, removes the API organization link at billing-cycle end.

Upgrading a Pro plan, adding paid Business seats or upgrading Business seat types can provide extra prorated credits for the rest of the billing cycle, subject to the applicable cap. Business credits are pooled and capped at $500 per monthly cycle or $6,000 per annual cycle. Adding paid Business seats creates a new invoice and an associated grant. Seat reductions affect the next billing cycle; reassigning an existing seat does not create extra credits.

Joining a Business workspace, merging personal content and changing a subscription are different actions. If your personal Pro subscription continues separately, joining alone does not replace it. Moving from Pro to Business ends the Pro link; after the Business workspace’s paid subscription has been active for seven days, an owner can create a new Business link. Moving a Business subscription to Enterprise removes the API organization link at billing-cycle end. Enterprise is not eligible for this benefit. Any associated refund follows the refund policy separately.

If the owner who linked a Business workspace leaves that workspace, its link is removed. Neither the subscription nor the API organization can be relinked until the current billing cycle ends. [Contact Support](/en/articles/6614161-how-can-i-contact-support) if you need to change the linked API organization. A change request does not guarantee a credit transfer or an additional grant.

For refunds, follow [How do I request a refund for my ChatGPT subscription?](/en/articles/7232895). Applicable legal rights and approved corrections remain in place. An approved full refund removes the unused promotional API credits tied to the refunded charge. A subscription refund is not a cash refund of a free promotional balance.

Deletion, bans and unbans have separate account and credit consequences.

# Troubleshooting

## I don't see the API credits benefit

Check the eligible plan, paid subscription age, selected workspace and account email. For Business, ask an owner to check the workspace's billing page. Availability also depends on the enabled cohort and country. If the offer should be available, contact Support with those details.

## Linking fails or the wrong organization appears

Confirm ownership on both sides, billing-management permission and the matching email. Check whether either side is already linked. Record the exact error and time. Do not create repeated claims to work around an existing link.

## My accounts are linked but I don't see a grant

Select the linked API organization and inspect its billing page. Linking and credit issuance are separate results. If the grant is still missing, contact Support with the subscription/workspace, organization ID, attempted activation time and error message. Remove sensitive information from screenshots; do not send passwords or API keys.

## The amount or expiry is different from what I expected

Compare the full-period allowance with your paid seat mix, billing cadence, remaining paid time and the displayed claim amount. Record the grant amount and expiry you actually see.

## API requests fail even though I have credits

Check the exact error, selected organization/project, remaining balance and expiration. Credit, spend and rate limits are different. Use the [API error-code guide](https://developers.openai.com/api/docs/guides/error-codes) before purchasing more credits.

## Are these ChatGPT Business plugin credits?

No. [ChatGPT Business plugin credit promotions](/en/articles/20001514) add workspace credits under a separate offer. The API grant is held in an API organization and follows its own terms.
