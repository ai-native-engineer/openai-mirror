<!-- source: https://help.openai.com/en/articles/8801890-managing-workspace-lifecycle-and-migration-in-chatgpt-business -->

# Managing workspace lifecycle and migration in ChatGPT Business

Learn how personal-workspace migration, seat-type changes, leaving a workspace, and deactivation work in ChatGPT Business.

Updated: 1 hour ago

***Note:*** *Starting June 24, 2026, Codex seats will no longer be available to new ChatGPT Business plans, or to Business workspaces that never added a Codex seat prior to June 24 2026. Business workspaces that had added a Codex seat prior to June 24, 2026, including pending invites as of June 24 can continue to manage and add usage-based Codex seats.*

# Overview

A workspace is a unique ChatGPT environment with its own settings, members, and resources.  
  
Personal workspaces are tied to existing ChatGPT accounts, and contain chats, memory, context, apps, and other ChatGPT features specific to the user. Similarly, organizations can set up workspaces for their ChatGPT Business accounts, containing information, features, and context applicable to the organization and its members.  
  
This article covers workspace migration aspects, including keeping a personal workspace separate, merging personal data into a Business workspace, handling seat-type changes, leaving a workspace and workspace activation/deactivation.

**Important**: after you leave a workspace, you cannot access data in that workspace unless you are invited back.

## Keep or merge a personal workspace

When you accept an invite to a ChatGPT Business workspace and you also have a ChatGPT Personal workspace, you have two options:  
  
  
**Keep a personal workspace separate**  
  
If you keep your ChatGPT Personal workspace, your personal data stays separate from your Business workspace, and you can switch between the two workspaces.  
  
If you have a Plus subscription, the subscription stays active until you cancel it. You continue to have access to chats in the Personal workspace even after cancellation.  
  
  
**Merge a personal workspace into ChatGPT Business**  
  
If you merge your ChatGPT Personal workspace into your Business workspace, data from the Personal workspace moves into the Business workspace and the Personal workspace is deleted after migration.  
  
If you have an active subscription, OpenAI automatically cancels it and refunds the remaining subscription period, except for mobile subscriptions.  
  
If you have a mobile subscription, cancel it separately on iOS or Android. If you are charged after migrating, contact OpenAI support for refund and cancellation help.  
  
After the merge is complete, the Personal workspace no longer appears in the account. Only the Business workspace remains.  
  
Merging workspaces is permanent and cannot be undone.

## Understand what migrates and what does not

When you merge a personal workspace into a Business workspace:

* Existing chat history moves to the Business workspace
* GPTs from the Personal workspace move to the Business workspace
* Plugins are deleted
* Custom instructions are deleted and do not migrate
* If you previously verified a domain in the GPT Builder Profile, you must verify that domain again in the new Business workspace

If the domain cannot be verified because it is already verified by another organization, remove the domain from the Builder Profile in the Personal workspace before trying again.  
  
In rare cases, long-running or historical chats may not be retrievable after a merge. Save important conversations before migrating.  
  
Data export is not available in a Business workspace.  
  
To merge a personal workspace into ChatGPT Business:

* Switch to the Business workspace by clicking on the profile icon from your account.
* Go to **Settings > Data Controls**.
* Select **Merge data from your personal workspace**.
* Follow the prompts to complete the migration.

## Seat-type changes and workspace access

As of June 24, 2026, Codex seats are no longer available to new ChatGPT Business workspaces. A Business workspace that had a Codex seat before June 24, 2026, can include standard ChatGPT seats, usage-based Codex seats, or a mix of both. If you need a larger deployment or more advanced controls, consider ChatGPT Enterprise.

### Changing a member from a standard ChatGPT seat to a Codex seat

This seat-type change is available only in Business workspaces that had a Codex seat before June 24, 2026.  
  
If an existing Business user is changed from a standard ChatGPT seat to a Codex seat:

* They lose ChatGPT access in the workspace
* They are redirected to Codex or shown a message that chat is not available in that workspace
* If they also have a personal workspace, they can still use that separate personal workspace
* Workspace history may no longer be available from the Codex-only seat. Workspace history has not been deleted and is available if the user is switched back to a ChatGPT seat.

### Changing a member from a Codex seat to a standard ChatGPT seat

If an existing Business user is changed from a Codex seat to a standard ChatGPT seat:

* ChatGPT Business access is restored
* Codex access continues
* The user can switch between workspaces as usual

## Access risks after a merge

Once personal data is migrated, that data becomes part of the Business workspace.  
  
If you later lose access to the Business workspace, leave the workspace, get removed from the workspace, or the workspace is deactivated, you also lose access to the migrated data. When you sign in again, you are redirected to a new Personal workspace without the previous Business data.  
  
If you later change from a standard ChatGPT seat to a Codex seat, review whether the merged chat history will remain accessible before making that change.  
  
Review your organization’s policies before deciding whether to merge a personal workspace into a Business workspace.

## Troubleshoot missing chats or GPTs after a merge

After a successful merge, the Personal workspace disappears and the content moves into the Business workspace. Migration and re-indexing can take time, and chats or GPTs may take up to about 24 hours to appear and become searchable.  
  
Try these checks first:

* Confirm that you are in the correct Business workspace.
* Refresh the browser, or sign out and sign back in.
* Use chat search and check the Archived chats view.
* Check the GPTs list in the Business workspace.

If content is still missing, contact Support and include the account email, the Business workspace name or ID if known, the names or approximate dates of missing chats or GPTs, and screenshots of missing content or errors.

## Leave a workspace

### To leave an active workspace:

* Select the Business workspace from the profile menu.
* Go to **Workspace settings**.
* Select **Members**.
* Next to your own name, select the **more options menu (•••)**.
* Select **Leave workspace**.
* Enter your email address to confirm, then select **Leave workspace** again.

### To leave a deactivated workspace:

If the workspace is deactivated, it appears locked and greyed out in the profile menu. Select the **more options menu (•••)** for that workspace, then select **Leave workspace**.  
  
If you are an Owner, you can also select the workspace to reactivate the subscription instead of leaving.

### Resolve a failed to leave workspace error

You may see a failed-to-leave-workspace error if:

* You are the last Owner in the workspace
* You are an Admin and an Owner must first change your role to Member or remove you from the workspace

## Workspace Deactivation

A Business workspace can be deactivated if an Owner cancels the subscription or fails to make a payment. In most cases, users can still access the workspace until the end of the next billing cycle, after which the workspace is deactivated. A workspace can also be deactivated sooner because of fraud, abuse, or other terms violations.  
  
Disputing a payment can also cause an unexpected deactivation. If you see an unexpected charge, first check whether someone in the workspace invited another user.  
  
If a Business workspace is deactivated:

* Data in the workspace remains intact
* Users cannot access the workspace
* Only workspace Owners can access the workspace settings needed for reactivation
* Users who still have a Personal workspace can continue to use it
* Users without a Personal workspace are prompted to create a new Personal workspace

If a user previously merged a Personal workspace into the Business workspace, the previous Personal workspace cannot be recovered.

### Reactivating a deactivated workspace

Only a workspace owner can reactivate a deactivated workspace.

* Sign in with the same email that was an Owner for the Business workspace and managed the subscription.
* Create a Personal workspace if ChatGPT prompts you to do so.
* Select the profile menu and find the greyed-out deactivated Business workspace.
* Select the **more options menu (•••)**, then select **Reactivate Workspace**.
* Select the subscription details and the desired number of users.
* Pay the outstanding invoice.

When you reactivate a Business subscription, you must have at minimum the same number of ChatGPT seats prior to deactivation, but there is no required number of Codex seats. If the workspace had a Codex seat before June 24, 2026, you can continue to manage and add Codex seats after reactivation. Reactivating a workspace that did not have a Codex seat before this date does not make it eligible to add a first Codex seat.

## Create a new workspace instead of reactivating

You can create a new Business workspace instead of reactivating the deactivated one, but the old data cannot be merged into the new workspace. The new workspace starts as a blank slate.  
  
A new self-serve Business workspace starts with standard ChatGPT seats and does not inherit the deactivated workspace’s eligibility to add Codex seats.

## Migrating Business workspace to other plans

ChatGPT Business does not support merging one Business workspace into another.  
  
Each Business workspace is a separate entity with its own members, billing subscription, settings, and data. A newly created Business workspace does not inherit the settings or subscription of an existing Business workspace.  
  
GPTs created in one Business workspace cannot be transferred to another Business workspace.  
  
  
To upgrade an existing ChatGPT Business workspace to ChatGPT Enterprise while keeping the same workspace and data, contact [OpenAI sales.](https://openai.com/contact-sales)  
  
If you want to move data from a Business workspace into a separate Enterprise workspace, please contact [OpenAI sales](https://openai.com/contact-sales) to discuss your available options.

# FAQ

## Is a personal-to-Business merge reversible?

No. A merge is permanent and cannot be undone.

## What happens if my seat changes from a standard ChatGPT seat to a Codex seat?

This change is available only in Business workspaces that had a Codex seat before June 24, 2026. You lose ChatGPT access in the workspace and may lose access to workspace history while you remain on a Codex seat.

## What happens if my seat changes from Codex to a standard ChatGPT seat?

ChatGPT Business access is restored, and Codex access continues.

## Can I export data before I leave or after I merge?

No. Data export is not available in a ChatGPT Business workspace.

## What happens to my Plus subscription if I merge?

OpenAI automatically cancels the remaining subscription period and refunds it, except for mobile subscriptions. For mobile subscriptions, you must cancel the subscription from the Apple app store or the Google play store.

## What should I do if I am still charged after migrating from a mobile subscription?

Cancel the subscription separately on iOS or Android, and contact Support if charges continue after migration. [Read more](/en/articles/20001043-how-do-i-avoid-being-charged-twice-if-i-subscribe-to-chatgpt-on-ios-android-and-the-web) about avoiding duplicate charges and what to do if you get charged.
