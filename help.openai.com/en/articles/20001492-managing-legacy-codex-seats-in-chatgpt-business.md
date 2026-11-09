<!-- source: https://help.openai.com/en/articles/20001492-managing-legacy-codex-seats-in-chatgpt-business -->

# Managing legacy Codex seats in ChatGPT Business

Learn which ChatGPT Business workspaces can use legacy Codex seats, how those seats are billed, and how to manage access, credits, and seat assignments.

Updated: 10 days ago

A legacy Codex seat provides access to Codex without a fixed monthly seat fee. Codex activity is paid for with credits from your workspace’s shared balance.

[Standard](https://help.openai.com/articles/8792828) and [Premium](https://help.openai.com/articles/8792828) seats both include access to ChatGPT and Codex. Legacy Codex seats provide usage-based access to Codex and do not include ChatGPT chat in that workspace.

## Availability

**Starting June 24, 2026**, Codex seats are no longer available to new ChatGPT Business workspaces or to existing workspaces that had never added a Codex seat.

Your workspace can continue to use, add, and manage legacy Codex seats if it had:

* At least one Codex seat before June 24, 2026; or
* A pending invitation for a Codex seat as of June 24, 2026.

An eligible workspace can add Codex seats even if its current members all use Standard or Premium seats. Creating a workspace before June 24, 2026, does not make it eligible on its own.

# What legacy Codex seats include

Legacy Codex seats provide usage-based access to Codex with no fixed monthly or annual seat charge. Codex usage is paid for with credits from the workspace’s shared balance.

A member with a legacy Codex seat cannot use ChatGPT chat in that Business workspace. Assign a Standard or Premium seat if the member needs access to both ChatGPT chat and Codex.

# How legacy Codex seats are billed

Codex seats do not have a recurring seat fee. Your workspace uses its shared credit balance when a member with a Codex seat uses Codex. If the workspace has no available credits, Codex activity is blocked until a workspace owner adds credits.

There is no minimum number of Codex seats in an eligible workspace. Codex seats do not count toward the two-seat minimum or the maximum number of paid Standard and Premium seats.

Codex usage rates depend on the model and activity. For current pricing, see: [ChatGPT rate card (credit-based pricing)](https://help.openai.com/articles/11481834).

# Invite a member with a legacy Codex seat

A workspace owner can select the role and seat type when inviting someone to an eligible workspace. Admins and members can invite members using the workspace’s default seat type. To invite a member as a workspace owner:

1. Go to **Workspace settings > Members**.
2. Select **Invite member**.
3. Enter the person’s email address and select a role.
4. Select **Codex** as the seat type.
5. Review and send the invitation.

The member receives access to Codex after joining the workspace. A workspace owner may be prompted to purchase credits if the workspace does not already have an available credit balance.

## Invite members in bulk

You can invite members in bulk using a CSV file and defining roles and seat types. For the CSV format, see: [Managing members, seat types, and roles in ChatGPT Business](https://help.openai.com/articles/8542216). Use ‘Codex’ as seat type for legacy Codex seats.

# Change a member’s seat type

Only a workspace [owner](https://help.openai.com/articles/8542216) can change a member’s seat type.

1. Go to **Workspace settings > Members**.
2. Find the member you want to update.
3. Select the member’s current seat type.
4. Select the new seat type.
5. Review any access, credit, or billing changes, then confirm.

Purchasing a Standard or Premium seat adds paid capacity to your subscription; assigning an available seat gives a member access without purchasing another seat. Legacy Codex seats do not need to be purchased in advance—their usage draws from workspace credits. For more information, see: [Managing billing and seats in ChatGPT Business](https://help.openai.com/articles/8792536).

## Move from Standard or Premium to a legacy Codex seat

The member keeps Codex access but loses access to ChatGPT chat in the Business workspace. This also applies when using Codex in the desktop app: Codex activity draws from that workspace’s shared credits and is subject to its spending limits.

The vacated Standard or Premium seat remains part of the paid subscription and can be assigned to another member. To stop renewing the paid seat, a workspace owner must schedule its removal in **Manage seats**. The reduction takes effect at the next renewal.

## Move from a legacy Codex seat to Standard or Premium

If an unused paid seat of the selected type is available, the workspace owner can assign it without purchasing another seat. If no paid seat is available, the owner must purchase one before completing the change. New paid seats are charged on a prorated basis for the current billing period.

If the workspace has only legacy Codex seats and no paid subscription, it must first purchase at least 2 Standard seats. Once the subscription is active, the workspace owner can add Premium seats or upgrade an existing Standard seat. The 2-seat minimum can then be met with Standard seats, Premium seats, or a combination of both.

## Seat swaps and reassignment

Seat swaps are available only between Standard and Premium seats. Legacy Codex seats cannot be included in a seat swap.

To move a member to or from a legacy Codex seat, change their seat type instead. Assigning a Standard or Premium seat requires an available paid seat of that type or an additional seat purchase. For seat changes and billing details, see: [Managing billing and seats in ChatGPT Business](https://help.openai.com/articles/8792536).

# Set the default seat type

A workspace owner can manage the default seat type from **Workspace settings > Billing**. **Codex** can be selected only in workspaces eligible for legacy Codex seats.

The default applies when an invitation does not specify a seat type. Changing the default does not change existing members’ seat assignments.

# Remove a member with a legacy Codex seat

Workspace owners and admins can remove members.

1. Go to **Workspace settings > Members**.
2. Find the member you want to remove.
3. Select the member’s **more options menu (•••)**.
4. Select **Remove member**.

Removing the member ends their workspace access immediately. Because legacy Codex seats have no recurring seat fee, there is no recurring charge to cancel. Previously used credits are not restored.

# Manage credits and spending

Credits are shared across the workspace. Legacy Codex seats require credits for all Codex activity, while Standard and Premium seats can use credits for eligible usage beyond their included limits. For privacy and visibility details, see: [Managing data, sharing, and privacy in ChatGPT Business](https://help.openai.com/articles/8798634).

Only workspace owners can purchase credits or configure automatic reload. Workspace owners and admins can change spending limits. For details, see: [Managing credits and spend controls in ChatGPT Business](https://help.openai.com/articles/20001155) and [Flexible pricing for the Enterprise, Edu, and Business plans](https://help.openai.com/articles/11487671).

## Add credits

1. Go to **Workspace settings > Billing**.
2. Select **Add credits**.
3. Select the amount and review your payment method.
4. Confirm the purchase.

Purchased credits are valid for 12 months. Credits are generally nonrefundable, except where required by law or otherwise stated in the applicable [service credit terms](https://openai.com/policies/service-credit-terms/).

## Turn on automatic reload

Automatic reload adds credits when the workspace balance falls below a selected amount.

1. Go to **Workspace settings > Billing**.
2. Select **Automatic reload**.
3. Set a **Minimum balance** and **Target balance**.
4. Set a **Monthly recharge limit** if you want to cap automatic purchases.
5. Review the payment method and turn on automatic reload.

If the balance is already below the minimum, a credit purchase may occur immediately. When the monthly recharge limit is reached, automatic reload pauses until the next month.

## Set Codex spending limits

Workspace owners and admins can set monthly spending limits for legacy Codex seats or individual members. An individual member’s limit overrides the seat-type limit and stays with that member if their seat type changes.

If a member reaches a spending limit, Codex usage pauses until a workspace owner or admin changes the limit or the limit resets. Previously used credits do not reset when a member changes seat type.

# Frequently asked questions

## Why can’t I select Codex as a seat type?

Your workspace must have had a legacy Codex seat before June 24, 2026, or a pending invitation for a legacy Codex seat as of that date. Otherwise, legacy Codex seats are unavailable. Standard and Premium seats both include Codex access.

## Why can’t a member with a legacy Codex seat use ChatGPT chat?

Legacy Codex seats do not include ChatGPT chat. Assign a Standard or Premium seat to give the member access to ChatGPT chat in the Business workspace.

## Why did Codex stop working?

Ask a workspace owner to check the shared credit balance, automatic reload settings, and any applicable spending limits in **Workspace settings > Billing**.

## Why am I being asked to buy 2 seats?

A workspace with only legacy Codex seats has no minimum seat requirement. Adding a paid subscription requires at least 2 Standard seats. Once the subscription is active, Standard and Premium seats both count toward the minimum.

## Can I create a new Business workspace with only legacy Codex seats?

No. New ChatGPT Business workspaces cannot add a first legacy Codex seat. Workspaces with only legacy Codex seats are available only to previously eligible customers.
