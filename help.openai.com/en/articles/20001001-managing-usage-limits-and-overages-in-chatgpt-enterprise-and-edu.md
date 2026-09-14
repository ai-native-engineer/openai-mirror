<!-- source: https://help.openai.com/en/articles/20001001-managing-usage-limits-and-overages-in-chatgpt-enterprise-and-edu -->

# Managing usage limits and overages in ChatGPT Enterprise and Edu

Learn how Enterprise and Edu workspace owners and admins can set monthly limits for users, control workspace overage usage, and monitor shared credits.

To configure monthly usage limits, open [Admin Console](https://help.openai.com/articles/12289294), select your ChatGPT workspace, and open **Usage limits**. You can set limits for the workspace, groups, and individual users.

If your workspace still has weekly role-based limits, they can continue to apply until you configure monthly limits or complete migration. When a migration banner appears in Admin Console, open **Usage limits > Workspace** and select **Migrate now**.

Migration converts eligible weekly role-based limits into monthly usage limits and cannot be undone.

# **Overview**

Enterprise and Edu workspaces have two independent controls that admins and owners can configure for credit-based usage:

* [Usage limits](https://admin.openai.com/usage-limits) set a monthly limit for each user. You can apply a workspace default, group defaults, and user overrides. Additionally, you can configure usage alerts to inform you of spend-control thresholds.
* The **workspace overage limit** determines how much eligible credit-based feature usage can continue after the committed credit pool is exhausted.

Workspace owners and admins can review usage analytics. Only workspace owners can view invoices unless the workspace is configured otherwise.

Note that credit-based usage draws from the workspace’s shared credit pool - A user’s usage limit can stop that user before the pool is exhausted. If the pool is exhausted first, the workspace overage limit determines whether eligible usage can continue. User usage limits continue to apply during overage usage.

These controls represent different points in the same billing journey: usage limits govern individual usage during the selected usage period, the workspace overage limit governs what can happen after the shared pool is exhausted, analytics and usage reports help you review what happened, and invoices show eligible overage usage for the workspace’s billing period.

|  |  |  |  |
| --- | --- | --- | --- |
| **Control** | **Scope and purpose** | **Where managed** | **Notes** |
| Usage limits | Monthly limits for individual users, applied through workspace, group, and user levels | Admin Console → Usage limits | Additional eligible usage for the user is prevented; a task may finish slightly over the limit |
| Workspace overage limit | Workspace-wide cap after the shared credit pool is exhausted | [Admin Console → Billing](https://admin.openai.com/billing) | The workspace cannot continue into additional overage after the cap is reached |
| Usage alerts | Notifications at configured workspace credit thresholds | [Admin Console → Billing](https://admin.openai.com/billing) | Recipients are notified; alerts do not stop usage |
| Analytics and usage reports | Visibility into credit usage and activity for review and reconciliation | [Admin Console →](https://admin.openai.com/billing)Analytics / Admin Console → Billing (download/export) | Shows usage with a possible freshness delay; it does not by itself determine the invoice period or stop usage |
| Invoices | The issued billing document for eligible overage usage in a workspace billing period | Admin Console → [Billing → Invoices](https://admin.openai.com/billing) | Appears after an invoice is issued; invoice access depends on workspace role and billing setup |

Workspace owners and admins can manage usage limits, usage alerts, and workspace overage limits in Admin Console after selecting their ChatGPT workspace. Only workspace owners can view invoices unless the workspace is configured otherwise.

Note: Both Usage limits and the Workspace overage limit have a 'No limit' setting option. 'No limit' has different meanings depending on the configuration surface.

For a group override set in Usage limits, No limit means the group inherits the workspace default; it does not mean unlimited usage.

For the workspace overage limit, configured in the [Admin Console](https://admin.openai.com/), No limit means no cap is configured on eligible overage usage. No limit does not make credits free or unlimited; eligible overage usage can continue and may be billed according to your agreement.

# **Manage monthly usage limits for users**

Usage limits help Enterprise/Edu workspaces set usage-period guardrails for individual users while preserving flexibility for groups and individual exceptions. The workspace can use **Monthly (default)**, which resets usage on the first day of each month in UTC, or **Aligned to billing cycle**, which resets usage at the start of each monthly usage period aligned to the workspace’s billing-cycle start date. The selected period does not change invoice or renewal dates. Workspace admins and owners can configure usage limits. The Member and Analytics viewer roles do not grant permission to change usage limits by themselves.

In ChatGPT Enterprise, [group managers](https://help.openai.com/articles/9083985) with **Manage spend controls** enabled can manage group usage limits and approve or deny requests to increase limits for groups they manage.

This permission does not allow changes to workspace defaults, the usage period, member usage visibility, the request process, or workspace billing and overage settings. For delegation setup, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

## **Use the Usage limits page in the Admin Console**

Workspace admins and owners can open [Admin Console](https://admin.openai.com), select the workspace, and select **Usage limits**. The page includes:

* **Workspace**: Set or remove the Default usage limit, choose the Usage period, open group and user overrides, and configure how members request a limit increase. If you have analytics permission, you can also select View analytics.
* **Groups**: Search groups, review member counts and inherited workspace limits, and add or edit a group override.
* **Users**: Search users or filter by group, compare Used this period, Inherited usage limit, and User override limit, and add or edit a user override.
* **Pending requests**: When the default request process is enabled, review a requester’s current usage and limit, edit the recommended limit if needed, read the justification, and select Approve or Deny.

Under the workspace’s request process, choose Default to collect requests from ChatGPT and Codex in Pending requests, Custom to send members to an HTTPS URL with optional instructions, or Disabled to turn off requests.

### **Switch the usage period**

1. In Usage limits, select Workspace.
2. Next to Usage period, select Edit.
3. Choose Monthly (default) or Aligned to billing cycle.

**Note:** If Aligned to billing cycle is unavailable, review the date shown for when the next billing cycle begins - the option will be available on that date.

1. Select Change usage period. The change takes effect immediately. Existing limit amounts stay the same, but usage counted toward those limits may change.

## **Choose the level of control**

Usage limits support multiple levels:

* **Workspace limits** set the monthly default for each user in the workspace.
* **Group limits** set the monthly default for each user in a group.
* **User limits**, also called user overrides, set a monthly limit for a specific user.

Configure limits and manage increase requests in the [Admin Console](https://admin.openai.com/usage-limits) → **Usage limits**.

## **How limit precedence works**

Usage limits are checked in this order: user override, highest applicable group default, then workspace default.

For example, an engineering group may need a higher default than a contractor group. A specific user can have an individual override if their expected usage differs from the rest of the group. If a user belongs to multiple groups, the highest applicable group default applies unless the user has an individual override.

## **How usage limits and the overage limit interact**

Suppose a user has a monthly limit of 6,000 credits. If the user reaches that limit, additional eligible usage is blocked for that user even if the workspace still has shared credits. If the workspace’s shared credit pool is exhausted first, the workspace overage setting determines whether eligible usage can continue. The user’s 6,000-credit limit still applies during overage usage.

## **Manage requests to increase limits**

In **Usage limits**, workspace admins and owners can allow users to request increases to their monthly limits.

This feature is enabled by default. With the default request process, members can request more usage in ChatGPT and Codex; requests appear in **Usage limits → Pending Requests**, workspace admins receive an email notification, and admins and owners can approve or deny requests.

In ChatGPT Enterprise, [group managers](https://help.openai.com/articles/9083985) with **Manage spend controls** enabled can also approve or deny requests to increase limits for groups they manage.

Admins and owners can also disable requests or send members to a custom URL, such as an internal access request page. Custom request destinations are handled outside **Pending Requests**, so review and approval happen in the destination you choose.

When approving a request in **Pending requests**, admins and owners can choose whether the increased user limit is temporary or permanent. A temporary increase applies through the end of the user’s current usage period. A permanent increase remains in place until an admin or owner changes or removes it.

For **Monthly (default)**, a temporary increase expires at the end of the current calendar month in UTC. For **Aligned to billing cycle**, it expires at the end of the current monthly usage period aligned to the workspace’s billing-cycle start date. After it expires, the user’s effective limit falls back to the next applicable limit: the highest group default that applies, then the workspace default.

The temporary option applies only to user overrides, not workspace or group defaults. Admins and owners can update an active user override from **Users** in **Usage limits**.

Temporary overrides can also be set from the **Users tab**. When setting a user override, you can specify if the override is temporary or permanent. You can set this independent of any requests from users to increase limits.

## **Migrate legacy weekly limits**

If your workspace displays a migration banner, open Admin Console, select the ChatGPT workspace, and go to **Usage limits > Workspace**. Select **Migrate now**, then follow the on-screen instructions.

Review the confirmation message before proceeding. Migration can take several minutes, depending on the size of your workspace, and applies to the eligible weekly role-based limits in that workspace.

Note that migration is irreversible - your weekly limit settings are removed after completion of migration.

When eligible weekly role-based limits are migrated to monthly usage limits, these conversion rules apply:

* A weekly workspace default that is not superseded by a monthly setting converts to a monthly workspace limit at four times the weekly amount.
* A weekly role-based limit that is not superseded by a monthly group or user setting converts to a monthly group override at four times the weekly amount.
* The workspace’s selected usage period—Monthly (default) or Aligned to billing cycle—continues to determine when monthly usage resets.
* Roles, permissions, and feature access do not change. The legacy weekly spend-control configuration is removed after migration, and migration cannot be undone.
* Some users may receive a higher effective limit because the highest applicable group default applies. A user who was previously unlimited through one role may receive a finite migrated limit when another finite role-based limit converts.

Usage limits are checked in this order: user override, highest applicable group default, then workspace default. Until migration is complete, an existing weekly limit in Permissions & roles can still apply when no corresponding monthly layer is configured.

Roles, permissions, and feature access remain managed in Permissions & roles.

## **Automate usage limits with the Spend Controls API**

Eligible Enterprise and Edu workspace admins can use the Spend Controls API to automate the same monthly limit management available in **Usage limits**. The API supports reading and updating usage limits at the workspace, group, and user levels. The API does not currently change the workspace’s usage period; choose **Monthly (default)** or **Aligned to billing cycle** in the Admin Console.

The API uses a ChatGPT Admin API key with the appropriate scope:

* Use `chatgpt.enterprise.usage_limit.read` to read usage-limit settings.
* Use `chatgpt.enterprise.usage_limit.write` to change usage-limit settings.

Workspace owners and admins can create a workspace-scoped Admin key with the required **Usage limits** permissions in Admin Console. This key does not authenticate model-inference requests or API Platform organization endpoints.

For setup and permissions, see: [Managing Admin keys in Admin Console](https://help.openai.com/articles/20001407).

For endpoint details, see: [Spend Controls API reference](https://chatgpt.com/public/admin/api-reference#tag/Spend%20Controls).

# **Control member usage visibility**

For eligible Enterprise workspaces with credit-based billing:

1. Open **Usage limits** in the **Admin Console**.
2. Select **Workspace**.
3. In **Usage visibility and requests**, turn on **Allow users to see usage in credits and dollars**.

Members can then see exact Work and Codex credit usage and estimated dollar values alongside percentages in **Usage & billing**. Regular Chat usage is not included. This setting changes visibility only; it does not change a member’s usage limit or the workspace overage limit. Estimated dollar values are planning aids; issued invoices remain authoritative.

See [**Reviewing Work and Codex usage and using Personal Analytics**](https://help.openai.com/articles/20001478) for the member experience.

# **Manage the workspace overage limit**

Some ChatGPT Enterprise/Edu workspaces use flexible pricing with a shared credit pool. Each workspace’s credit allocation, rates, eligible usage, and billing terms are defined in its agreement with OpenAI.

Overages occur when an eligible workspace continues using credit-based features after its committed credit pool has been used. The additional usage is billed according to your agreement with OpenAI and any configured overage limit.

If you are unsure which terms or types of usage apply to your workspace, contact your OpenAI account team.

## **Review credit usage and overage settings**

When a contracted overage rate is available, estimated dollar amounts may appear alongside credits in the Cost API, Codex analytics API, Admin Console Analytics, and Admin Console spend controls. These values are planning estimates based on the workspace’s overage rate; they are not settled charges, invoices, or a replacement for Billing → Invoices.

If a dollar estimate is missing or differs from another surface, confirm the selected workspace, billing-cycle window, contracted rate and currency, and last-updated timestamp. Use the issued invoice as authoritative. Contact your OpenAI account team or OpenAI Support if the mismatch remains after those checks.

Workspace owners and admins can review credit usage and overage settings from the [Admin Console](https://admin.openai.com/):

1. Open the Admin Console.
2. Select the relevant Enterprise/Edu workspace.
3. Select Billing.
4. Review Unbilled overage for eligible usage that has not yet been billed.
5. Download usage reports from the upper-right corner when you need additional detail.

Use the Billing tabs for different parts of the review:

* Plan shows the credit balance, overage limit, alerts, and a path to view credit usage.
* Grant activity shows credit grants and activity when available for your workspace.
* Invoices shows issued invoices when your role and workspace billing setup allow access. Open an invoice to review the invoice date, due date, payment status, and invoice document when available.

Usage data may have a freshness delay. If you compare a downloaded report with a recent invoice, review the invoice period and report timestamp before escalating a mismatch.

## **Follow the path from usage to invoice**

1. Eligible credit-based usage draws from the workspace’s committed shared credit pool.
2. If the shared pool is exhausted, eligible usage can continue only within the configured workspace overage limit. User usage limits continue to apply.
3. Billing shows current credit information and Unbilled overage for eligible usage that has not yet been billed. Usage reports and analytics can help you inspect activity, but they may have a freshness delay.
4. Overage billing is evaluated after the workspace’s billing period ends, according to the agreement with OpenAI. When comparing limits, usage reports, and invoices, confirm whether the workspace uses Monthly (default) or Aligned to billing cycle, then compare the date ranges shown in the Admin Console.
5. An overage invoice is generally generated after that billing period and sent after a five-business-day review window. When it is issued, it appears in [Billing → Invoices](https://admin.openai.com/billing) for roles with invoice access, such as workspace owners. Use the invoice period, usage-report timestamp, contracted rate, and applicable exception or adjustment to reconcile it.

## **Set the workspace overage limit**

OpenAI does not set a workspace overage limit by default. The setting appears as No limit until a workspace owner defines one. If no overage limit is set, certain feature usage can continue being utilized uninterrupted, but could incur unwanted overage charges. To avoid this, please be sure to set limits by going to the Billing tab.

To configure the workspace overage limit, open Billing, select Manage under Overage limit, and enter a credit value.

* Setting a limit restricts how far the workspace can continue into overages after its committed credit pool is exhausted.
* Setting the limit to 0 prevents the workspace from continuing into overages. Some advanced features may pause until additional credits are available or the limit changes.
* Changing the overage limit affects future eligible usage. It does not retroactively remove usage that already occurred or change an invoice that has already been issued.

## **Configure usage alerts**

Usage alerts notify selected recipients when the workspace reaches a chosen credit threshold, uses all committed credits, or reaches the overage limit. Alerts do not block usage. Use the workspace overage limit when you need a cap.

## **Understand invoice timing, presentment, and review**

If your workspace has eligible overage usage during a billing period, OpenAI may issue an overage invoice according to your agreement with OpenAI. Overage invoices are generally issued monthly and follow the workspace’s contract billing period, which may be anchored to the workspace’s subscription start date rather than the calendar month. After the billing period ends, the invoice is generally generated and sent after a five-business-day review window. Overage invoices are separate from ChatGPT Go, Plus, Pro, Business web subscription billing and separate from API Platform billing.

Your first overage invoice may cover only part of a billing period if overage billing begins after the period starts. Review the invoice period before comparing the invoice with analytics or a downloaded usage report.

An overage invoice includes a summary line item for eligible overage usage. It does not consolidate unrelated charges, such as seat fees. Additional detail, such as usage reports or CSV exports, may be available in billing settings or from your OpenAI account team, depending on your workspace configuration.

To find an issued invoice, open [Admin Console](https://admin.openai.com), select the workspace, open **Billing**, and select **Invoices**. The invoice list can show the invoice date, due date, payment status, and a link to the invoice document when available. Only workspace owners can view invoices unless your workspace is configured otherwise.

If your organization requires a purchase order number, different billing contact, additional invoice recipients, or other invoice metadata, contact your OpenAI account team. These details may be governed by your Order Form or billing setup and may not be editable directly in ChatGPT.

## **Before contacting Support or your account team**

If an overage invoice or usage report does not look correct:

* Confirm that the invoice period matches the usage report period.
* Review the report timestamp because usage data may have a freshness delay.
* Confirm the credit allocation, expiration, rates, and invoicing terms in your Order Form or agreement.
* Confirm whether a workspace overage limit was configured.
* Confirm the workspace’s selected usage period and compare the exact date ranges shown for the user limit, report, and invoice.

## **When to contact Support or your account team**

Contact your OpenAI account team or OpenAI Support if you need help with:

* A charge you do not recognize.
* An invoice that appears to use the wrong rate or invoice period.
* A missing purchase order, billing contact, tax profile, payment detail, or invoice recipient.
* A workspace that should be excluded from overage billing.
* An agreement, promotion, waiver, or adjustment that should apply to the invoice.

Include the workspace name, workspace ID if available, invoice number, invoice period, downloaded usage report if available, and a brief description of the issue. Do not share passwords or one-time codes.

# **FAQ**

**Usage limits**

**On what timeframe are usage limits measured?**
The workspace can use **Monthly (default)**, which resets usage on the first day of each month in UTC, or **Aligned to billing cycle**, which resets usage at the start of each monthly usage period aligned to the workspace’s billing-cycle start date. The Admin Console shows the current UTC date range.

**What does 'no limit' indicate for Group overrides?**
No limit in this context does not mean unlimited; it means that the group will fall back to the specified workspace default. Specifying a limit will result in a group-specific override being applied.

**What if limits are defined at multiple levels (user, workspace, groups)?**
Usage limits are applied in this order: user override, highest applicable group default, then workspace default. If a user belongs to multiple groups, the highest group limit applies unless the user has an individual override.

**How do I check a user’s usage limit?**
Open the [Admin Console](https://admin.openai.com/usage-limits), then review the relevant user or group in **Usage limits**.

**Can a user exceed their usage limit?**
The credit value for some usage cannot be determined exactly until a task completes. A task that starts under the limit may finish and push usage slightly over the limit. Once the limit is reached, usage controls prevent additional eligible usage.

**What if a user is part of multiple groups?**
The user is assigned to the group limit that is the greatest limit of the groups the user is part of. For example, if the workspace has a limit of 5,000 credits and a user is part of two groups, Group A with a limit of 7,000 credits and Group B with a limit of 8,000 credits, assuming the user does not also have a user override, that user will have a monthly limit of 8,000 credits.

**Can members change their limits?**
The Member role by itself does not grant permission to change limits. In ChatGPT Enterprise, [group managers](https://help.openai.com/articles/9083985) can manage limits for their groups when **Manage spend controls** is enabled. As members approach their limits, they may be notified and given an option to request an increase.

**What happens to legacy weekly limits?**
When a workspace with weekly role-based limits is migrated, existing monthly workspace, group, and user settings remain in place and take precedence. Any weekly limit not superseded by a monthly setting is multiplied by four: workspace defaults become monthly workspace limits, while role-based limits become monthly group overrides.

The migration does not change roles, permissions, or feature access. After the migration is complete, the legacy weekly spend-control configuration will be removed and the change cannot be reversed.

**Which limit applies if limits are set both in the Usage limits tab and in the Permissions & roles tab?**
The settings in the Usage limits tab take precedence over the settings in Permissions & roles when both are configured. Usage limits are first checked for user overrides, then the highest applicable group default, then the workspace default. If none of those layers apply, the existing Permissions & roles limit can still apply.

**How do I migrate weekly limits if the option is available?**
If your workspace displays a migration banner, open Admin Console, select the ChatGPT workspace, and go to **Usage limits > Workspace**. Select **Migrate now** and confirm that you want to migrate weekly role-based limits to monthly group-based limits. Migration can take several minutes. If the banner does not appear, your workspace may already be migrated or may not be eligible for manual migration.

**What changes when legacy weekly limits migrate?**
Monthly settings already configured in Usage limits take precedence. Unsuperseded weekly workspace defaults and role-based limits convert to monthly amounts at four times the weekly amount, with role-based limits becoming group overrides. The workspace’s selected monthly reset cadence continues to apply. Roles, permissions, and feature access do not change.

**Can weekly-limit migration be undone?**
No. The migration is irreversible and removes the legacy weekly spend-control configuration.

**Why is the Usage limits pane showing credits used for a user that differs from credit usage shown in other analytics views?**
Credits used data in Usage limits is close to real time while other analytics data is delayed. Additionally, due to the way we process data, the credits used in Usage limits may infrequently have temporary inaccuracies that are typically resolved shortly after they occur.

**Overage limits**

**Who can view overage charges on invoices?**
Workspace owners can view workspace billing information and invoices, including overage charges. Other roles may not have invoice access unless otherwise configured.

**Are ChatGPT workspace overages the same as API Platform billing?**
No. ChatGPT workspace billing and API Platform billing are managed separately. Make sure you are reviewing the billing surface for the product you used.

**When should I expect an overage invoice?**
Overage invoices are generally issued monthly according to your workspace’s contract billing period. The billing period may be anchored to your subscription start date rather than to a calendar month. After the billing period ends, an invoice is generally generated and sent after a five-business-day review window. Your first overage invoice may cover only part of a billing period if overage billing begins after that period starts.

**Where can I find an overage invoice?**
Open the [Admin Console](https://admin.openai.com/), select the relevant workspace, open **Billing**, and select Invoices. For [roles with invoice access](/en/articles/8266401), the table can show the invoice date, due date, payment status, and a link to the invoice document when available.

**Why might analytics, Unbilled overage, a usage report, and an invoice show different numbers?**
First make sure you are comparing the same workspace and the same date range. Usage limits reset according to the workspace’s selected usage period, while invoices follow the workspace’s contract billing period. Analytics and downloaded reports can also have a freshness delay. Compare the invoice period, report timestamp, credit allocation, contracted rate, and any applicable exception or adjustment before escalating a mismatch.

**Does changing the workspace overage limit change past usage or an existing invoice?**
No. Changing the workspace overage limit affects future eligible usage. It does not retroactively remove usage that already occurred or change an invoice that has already been issued.

**Do usage limits or workspace overage limits reset when an overage balance is cleared?**
No. Clearing an overage balance does not change the configured monthly user usage limits or the workspace overage limit. Credits already counted toward a user’s limit continue to count until the selected usage period resets. If the workspace was blocked because it had reached the overage cap, clearing the overage balance can allow eligible usage to continue again under the unchanged overage limit.

**Why might my first overage invoice cover only part of a billing cycle?**
Your first overage invoice may cover only part of a billing cycle, depending on when overage billing begins for your workspace and your organization’s billing date. If you have questions about the period shown on an invoice, contact your OpenAI account team or OpenAI Support.

**Can I update purchase order details or invoice recipients in ChatGPT?**
This depends on your workspace billing setup and agreement with OpenAI. To update purchase order details, invoice metadata, or additional invoice recipients, contact your OpenAI account team.

**How are overage amounts calculated?**
At a high level, overage amounts are based on credits used above your purchased or granted credits, multiplied by your contracted overage rate. Your exact rate and terms can vary by your agreement with OpenAI – contact your OpenAI account representative for more details.

**What is the default overage limit set to a workspace?**
By default, there are no overage limits set for credit-based workspaces – this means it will be set as “No limit.” Any eligible credit-based feature usage can continue after the committed credit pool is used, and the additional usage may be billed according to your agreement with OpenAI. To avoid any unexpected overage charges, Admins should set overage limits to the workspace. Workspace owners can review and update the overage limit in the Admin Console in the billing tab.

**What happens if an overage limit is set to 0?**
If an overage limit is set to 0, the workspace will not be allowed to continue into overages after the committed credit pool is exhausted. Advanced features may pause until additional credits are available or the limit is changed.
