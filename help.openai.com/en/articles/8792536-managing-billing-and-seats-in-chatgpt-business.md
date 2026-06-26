<!-- source: https://help.openai.com/en/articles/8792536-managing-billing-and-seats-in-chatgpt-business -->

# Managing billing and seats in ChatGPT Business

Learn how standard ChatGPT seats, Codex seats, credits, and billing cadence work in ChatGPT Business.

Updated: 1 hour ago

***Note:*** *Starting June 24, 2026, Codex seats will no longer be available to new ChatGPT Business plans, or to Business workspaces that never added a Codex seat prior to June 24 2026. Business workspaces that had added a Codex seat prior to June 24, 2026, including pending invites as of June 24 can continue to manage and add usage-based Codex seats.*

## Overview

This article applies to self-serve ChatGPT Business billing for standard ChatGPT seats and usage-based Codex seats. Read our [overview article](/en/articles/8792828-what-is-chatgpt-business?preview) to learn more about ChatGPT Business.

**Note**: As of April 2, 2026, we’ve changed the pricing structure for ChatGPT Business and have reduced the price of standard ChatGPT seats by **by USD $5 per month** (note that prices will vary depending on your specific region and local currency). If you are on a monthly plan, the new, lower price will be reflected on your next bill. If you’re on an annual plan, it will be reflected at your next renewal. In both cases, you’ll receive a credit applied to your next subscription renewal to account for the price change. [Read more](/en/articles/8792536#refunds-and-cancellations) about the credit refund.

ChatGPT Business is built around 2 types of seats: **standard ChatGPT seats** and **Codex seats.** Each seat type determines what a user can access and how you are billed for that user.

| Seat type | Included access | Billing model | Minimum seats required |
| --- | --- | --- | --- |
| Standard ChatGPT seat | ChatGPT and Codex | Fixed per-user, per-month cost | 2 |
| Codex seat | Codex only | Usage-based | No minimum in eligible workspaces |

### Standard ChatGPT seats (fixed cost)

Standard ChatGPT seats are billed per user and require a minimum purchase of 2 standard ChatGPT seats.

* **Monthly plan:** $25 per user per month
* **Annual plan:** $20 per user per month, billed annually

ChatGPT seats include baseline access to Codex, and you can use [flexible pricing](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) and purchase workspace credits to extend usage beyond the included rate limits for [Codex](https://developers.openai.com/api/docs/pricing) and for ChatGPT [models](/en/articles/12003714-chatgpt-business-models-limits).

### Codex seats (usage-based, no fixed cost)

Codex seats have no fixed monthly seat price.  
  
In a Business workspace that had a Codex seat before June 24, 2026, there is no minimum number of Codex seats, but the workspace requires credits for Codex activity.  
  
After June 24th, Codex seats are no longer available to new Business workspaces.  
  
Read more about how [credits work](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans), and refer to the [Codex rate card](/en/articles/20001106-codex-rate-card) for latest pricing information.

### Managing billing in your ChatGPT workspace

You can review and manage seats, payment methods, and other billing settings from **Workspace settings →** [**Billing**](https://chatgpt.com/admin/billing)**.**  
  
  
A Business workspace that had a Codex seat before June 24, 2026, can include only standard ChatGPT seats, only Codex seats, or a mix of both. New self-serve Business workspaces cannot add a first Codex seat. Standard ChatGPT seats include core ChatGPT Business workspace access, ChatGPT access, and access to Codex.

### Payment methods

ChatGPT Business is a self-serve subscription that currently supports credit and debit card payments only. Invoice billing, bank transfer, wire, ACH, purchase orders, net terms, and split payments are not available for self-serve Business workspaces.  
  
If your organization requires invoicing, contact Sales to discuss a contracted plan such as ChatGPT Enterprise or ChatGPT Education. When reaching out, include your organization name, estimated number of seats, preferred billing cadence, and any compliance or security requirements.  
  
Support cannot convert an existing self-serve ChatGPT Business workspace to invoice billing.

## Billing for standard ChatGPT seats

Billing cadence applies to standard ChatGPT seats. Credits for usage-based products are separate, and are covered later in this article.

### Monthly plan

Under the monthly plan:

* At the start of each billing month, you are charged for your baseline number of standard ChatGPT seats.
* If you add standard ChatGPT seats above the baseline during the month, those seats are charged on a prorated basis.
* At the beginning of the next billing period, you are charged based on the current number of standard ChatGPT seats for the upcoming month.
* If the number of standard ChatGPT seats is reduced below the baseline during the month, the baseline adjusts to the new reduced count at the next monthly invoice date. You are still billed for the baseline number of standard ChatGPT seats during the current billing month.

### Monthly plan example

A user buys 10 standard ChatGPT seats at a monthly price of $25 per seat, for a total of $250. On day 10, the user adds 3 standard ChatGPT seats, bringing the total to 13. On the next invoice, the total charge is $375.

* 13 seats × $25 monthly price = $325
* 3 extra seats × 20 days used ÷ 30 days × $25 monthly price = $50
* Total = $375

### Annual plan

Under the annual plan:

* At the beginning of the billing year, you are charged for your baseline number of standard ChatGPT seats.
* If you add standard ChatGPT seats during the year, those seats are billed on a prorated basis at the end of each monthly true-up cycle.
* At the end of a monthly true-up cycle, you are charged for seats above the baseline at a prorated annual rate, and the new standard-seat count becomes the baseline for the rest of the year.
* True-ups reconcile actual seat usage with what has already been billed.
* If you add 1 times your current baseline or 20 standard ChatGPT seats in a month, you receive an instant invoice for a true-up before the monthly cycle ends, and the baseline resets immediately.

### Annual-plan example

A user buys 5 standard ChatGPT seats at an annual price of $20 per seat per month, for a total of $1,200 for the year. On day 10, the user adds 3 standard ChatGPT seats, bringing the total to 8. On the next invoice, the user is charged $700 total for the additional seats for the days used and the remainder of the year.

* Invoice 1: 5 seats × $20 × 12 months = $1,200
* First monthly true-up cycle: 20 days used ÷ 30 days × 3 seats above baseline × $20 monthly subscription price, plus 3 seats above baseline × $20 monthly subscription price × 11 months remaining in the annual plan
* Total = $700

If the owner removes 2 users on day 20 of month 2, nothing changes in the billing process because the seat count remains below the new baseline.

## Billing for Codex seats and credits

Codex seats are usage-based seats. They do not incur a fixed recurring seat fee, but they do require workspace credits for activity. Learn more about credits by reading our Help Center article: [**Flexible pricing for Business and Enterprise/Edu plans**](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans). Then refer to the [Codex Rate Card](/en/articles/20001106-codex-rate-card) for the latest pricing for ChatGPT Business.  
  
The Codex-seat billing guidance in this section applies to Business workspaces that had a Codex seat before June 24, 2026. New self-serve Business workspaces cannot add Codex seats.  
  
If you see a Codex usage-limit banner in Workspace settings, add credits so members can continue using Codex. You can also enable automatic recharge to help avoid future credit interruptions.  
  
If your Business workspace had a Codex seat before June 24, 2026, and currently has only standard ChatGPT seats, you can add a Codex seat and will be prompted to add credits using the saved payment method.  
  
When you add your first standard ChatGPT seat to a Codex-only workspace, you will be prompted to purchase a minimum of 2 seats using the saved payment method.  
  
Read [**managing credits and spend controls**](/en/articles/20001155) for step-by-step instructions on adding credits, enabling automatic recharge, and setting workspace limits.

## Billing impacts of adding or removing seats

Before adding or removing members, verify the current standard ChatGPT seat count, Codex-seat count, and available credits in the workspace billing area. To understand the mechanics of inviting members and adding seats, refer to our Help Center article: [Managing workspaces, people, and access in ChatGPT Business.](/en/articles/8542216)

### Add standard ChatGPT seats

When you add members with standard ChatGPT seats to a ChatGPT Business workspace, you add standard ChatGPT seats to the subscription.

* **Flexible monthly plan:** standard ChatGPT seats above the baseline are billed on a prorated basis.
* **Annual plan:** standard ChatGPT seats above the baseline are billed at the end of the monthly true-up cycle on a prorated basis.

### Add Codex seats

If your Business workspace had a Codex seat before June 24, 2026, you can add members with Codex seats. The seat itself has no fixed monthly cost, but the workspace needs credits for usage.

### Remove standard ChatGPT seats

Reducing team size by removing standard ChatGPT seats affects future billing **only after the standard ChatGPT seat count drops below the baseline** and the billing cycle resets. For the current period, you are still billed for the current standard ChatGPT seat baseline.

If you want to continue offering standard ChatGPT seat access, **you must purchase at least 2.**

**To reduce or remove standard ChatGPT seats,**

* Sign in as a Workspace Owner.
* Go to **Workspace settings >** [**Billing**](https://chatgpt.com/admin/billing)
* Select **Plan**
* Update the number of standard ChatGPT seats to the desired total.
* Confirm the change.
* Review the next renewal date. The reduced standard ChatGPT seat count applies to a future invoice or renewal, not the current billed period.

### Moving a member with a standard ChatGPT seat to a Codex seat

This seat-type change is available only in Business workspaces that had a Codex seat before June 24, 2026.  
  
Changing a user from a standard ChatGPT seat to a Codex seat affects both product access and future billing. Review the seat-type change in **Workspace settings** > [**Members**](https://chatgpt.com/admin/members) page and any related credit requirements before confirming the change. Note that we do not offer refunds for changing from Standard ChatGPT seats to Codex mid-cycle for both monthly and annual plans.

## Manage billing information

Only Owners can view and manage workspace billing information.

From the billing settings area, Owners can:

* View past invoices
* Change credit card details
* Update billing information
* Cancel the plan through **Manage plan**
* See the next invoice date and amount
* See how many standard ChatGPT seats and Codex users are currently in the workspace
* Access credit-related controls such as adding credits or enabling auto-top-up if those controls are available in the billing area

### Change billing cadence

Owners can change the billing schedule from monthly to annual, or from annual to monthly, for standard ChatGPT seats.

* Go to the billing area for the workspace.
* Select **Manage license**.
* Select **Billing schedule**.
* Select the new billing schedule, then select **Continue**.
* Select **Confirm**.
* Review the next renewal date, because the change takes effect at renewal rather than immediately.

Examples:

* Monthly to annual: if today is July 8, 2024, and the monthly subscription renews on July 17, 2024, changing to annual means the next renewal still happens on July 17, 2024, but the subscription then runs through July 17, 2025.
* Annual to monthly: if today is July 8, 2024, and the annual subscription renews on September 17, 2024, changing to monthly means the next renewal still happens on September 17, 2024, but the subscription then runs through October 17, 2024 instead of September 17, 2025.

### Manage tax and VAT information

If you are in a region that levies VAT, you can self-identify as a business and enter your Tax ID at checkout. This automatically exempts the purchase from VAT, and the same status applies to future invoices.

## Refunds and Cancellations

**Note:** As of April 2, 2026, we’ve changed the pricing structure for ChatGPT Business and have reduced the price of standard ChatGPT **seats by USD $5 per month** (note that prices will vary depending on your specific region and local currency).   
  
If you are on a monthly plan, the new, lower price will be reflected on your next bill. If you’re on an annual plan, it will be reflected at your next renewal. In both cases, you’ll receive a credit applied to your next subscription renewal to account for the price change.  
  
Depending on whether you have a monthly plan or an annual plan, we’re applying a **pro-rated pricing difference refund** to your current billing cycle as a credit to be used for **future ChatGPT seat subscriptions.**   
  
**This is not a cash refund to your original method of payment** - the credit will remain on your account and will automatically be applied to your invoice for your next subscription payment.   
  
Note that this credit is not displayed in settings - you can review it in your list of invoices.If you cancel your subscription, choose not to renew, or delete your account, the credit is forfeit. This credit cannot be transferred between accounts, or applied to a new account. The credit cannot be used for [Codex](/en/articles/20001106-codex-rate-card) or other [flexible pricing account features](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans).

### ChatGPT seats

Unused standard ChatGPT seats are not refundable once you commit to a seat count on either a monthly or annual plan. ChatGPT seat billing is based on the number of seats selected at checkout, not actual usage.  
  
Owners can adjust your plan’s seat count at the end of your billing cycle for future periods.

### Codex seats

Codex seats do not have a fixed monthly charge, and credits are not refundable except in limited circumstances. [Learn more](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans#h_7fbbd9e98d).  
  
Owners/admins can cancel your plan from Workspace settings > [Billing](https://chatgpt.com/admin/billing). Click the **Cancel** button in the bottom of the page to get started.

# FAQ

## Does ChatGPT Business still require 2 seats?

Standard-seat access requires a minimum purchase of 2 standard ChatGPT seats.  
  
In a Business workspace that had a Codex seat before June 24, 2026, a Codex-only configuration does not require a minimum number of Codex seats. New self-serve Business workspaces cannot add a first Codex seat.

## Do Codex seats have a monthly seat cost?

Codex seats have a fixed seat price of $0 per user per month, but Codex activity requires workspace credits.

## When will I see new pricing changes take effect?

New pricing changes take effect from your next billing cycle (monthly or annual).

## Where do I see the credit refund for the new pricing changes?

Depending on whether you have a monthly plan or an annual plan, we’re applying a pro-rated pricing difference refund to your current billing cycle as a credit to be used for **future ChatGPT seat subscriptions.** The refund will be applied when you renew next (either annually or monthly).   
  
This is not a cash refund to your original method of payment - the credit will remain on your account and will automatically be applied to your invoice for your next subscription payment. Owners can review invoices in Workspace settings > [Billing](https://chatgpt.com/admin/billing).

## Can I request a refund for an unused standard ChatGPT seat?

No. Unused standard ChatGPT seats are non-refundable once the workspace has committed to the seat count for that billing period.

## Can I reduce the number of standard ChatGPT seats on my plan?

Yes. Owners can reduce paid standard ChatGPT seats for future invoices through self-serve billing controls. If the workspace will continue to offer standard-seat access, the total cannot stay below 2 standard ChatGPT seats.

## Is there an upper limit to the number of seats I can purchase at one time?

The upper limit is 1,000 seats per purchase, across all seat types. If you need larger numbers of seats, [consider ChatGPT Enterprise](https://help.openai.com/en?q=What%20is%20ChatGPT%20Enterprise).
