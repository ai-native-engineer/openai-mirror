<!-- source: https://help.openai.com/en/articles/20001636-auto-join-for-chatgpt-business-workspaces -->

# Auto-join for ChatGPT Business workspaces

Learn how to turn auto-join on or off, who can join your ChatGPT Business workspace, and how seats are billed.

Updated: 16 hours ago

Auto-join lets eligible coworkers join your ChatGPT Business workspace without waiting for a workspace owner to approve each request. In Workspace settings, this option is called **Auto-approve join requests**.

# Who can use auto-join?

Workspace owners can manage auto-join in eligible ChatGPT Business workspaces. There is one auto-join setting for the workspace, not a separate setting for each email domain. Workspace discovery must be enabled for join requests to be approved automatically.

For workspaces that manage domains directly, coworkers can qualify through the primary workspace owner’s current email domain or a verified domain associated with the workspace. A domain matching the primary owner’s current email domain does not need separate domain verification.

For workspaces whose domains are managed centrally by their organization, a coworker’s email domain must be both verified and assigned to that workspace.

Before turning it on, review the eligible domains and your workspace’s default seat type. Auto-join applies to eligible coworkers across those domains, rather than only to people you approve individually.

# How does auto-join affect seats and billing?

What happens when a coworker joins depends on seat availability and whether your workspace supports automatic seat purchases:

* **An eligible seat is available:** Your coworker uses an available seat of your workspace’s default type. Assigning that existing seat does not add a seat charge.
* **A new seat is needed and automatic purchases are supported:** Turning on auto-join is free. If a coworker needs a new seat and auto-join can purchase it automatically, we’ll add a seat of your workspace’s default type and charge you right away for the rest of the current billing period. On monthly billing, if buying the seat requires you to confirm a change to your billing date, the request goes to a workspace owner for approval. Auto-join doesn’t charge for the seat in that case.
* **Your workspace can only use available seats:** Auto-join does not purchase a new seat. A seat must be made available before your coworker can join.

For help managing purchased seats and billing, see [Managing billing and seats in ChatGPT Business](/en/articles/8792536-managing-billing-and-seats-in-chatgpt-business).

# Turn on auto-join

1. Open the Business workspace you want to manage. You must be a workspace owner.
2. Go to **Workspace settings → Billing → Seat preferences**.
3. Review the **Default seat type**, then turn on **Auto-approve join requests**.
4. If a confirmation appears, review the eligibility and billing information, then select **Confirm**. Select **Cancel** if you don’t want to enable it.

For workspaces where auto-join only uses available seats, the setting saves without a paid-seat confirmation.

If you see a message on the ChatGPT home page asking you to turn on auto-join, review the seat and billing details before selecting **Turn on auto-join**. Selecting it enables auto-join immediately for all eligible domains in your workspace, even if the prompt shows only one. Select **Not now** to dismiss the prompt without enabling auto-join.

# Turn off auto-join

Return to **Workspace settings → Billing → Seat preferences** and turn off **Auto-approve join requests**.

Turning off auto-join keeps any seats you’ve already bought on your subscription. To stop paying for an unused seat, open Manage seats and schedule a reduction for your next billing cycle. See [Managing members, seat types, and roles in ChatGPT Business](/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business).

# Frequently asked questions

## Does auto-join add everyone at my company at once?

No. Auto-join approves eligible coworkers when they take action to join. Turning on the setting does not automatically enroll everyone at your company.

## Why does a coworker still need approval?

Check that they’re using an email address on an eligible domain and that both auto-join and workspace discovery are enabled for the correct workspace. For centrally managed domains, also check that the domain is verified and assigned to that workspace. They may also need an available seat if your workspace cannot purchase one automatically, or if an attempted purchase cannot be completed.

Workspace owners can review outstanding requests under **Workspace settings → Members → Pending requests**.

## Why don’t I see the auto-join setting?

Check that you’re a workspace owner and have selected the correct Business workspace. Availability also depends on your workspace’s domain configuration and seat-purchase eligibility.

## Can I remove someone who auto-joined?

Yes. You can remove someone who auto-joined the same way you remove any other member. Go to **Workspace settings > Members** and remove the person from the workspace. Their access ends immediately, but removing them does not cancel the paid seat.

If you no longer need the seat, a workspace owner can use **Manage seats** to schedule a seat reduction. Removing a member or scheduling a reduction does not automatically refund charges for the current billing period. The paid seat remains available until that period ends. On an annual plan, this means the end of the current annual term.

If you reuse the seat before then, you’ll be informed that you’re canceling its scheduled removal. The seat stays on your subscription and continues to renew. If you don’t reuse it and leave the reduction scheduled, your paid seat count decreases at the start of the next billing cycle.

For member-removal steps, see: [Managing members, seat types, and roles in ChatGPT Business](https://help.openai.com/articles/8542216). For seat reductions and refund terms, see: [Managing billing and seats in ChatGPT Business](https://help.openai.com/articles/8792536).

## Does joining move my personal chats into the workspace?

Joining a Business workspace and migrating personal content are separate actions. You can keep your personal workspace separate. See [Migrating your personal workspace](/en/articles/8801890-migrating-your-personal-workspace-to-chatgpt-business-or-enterprise) before choosing to move content.
