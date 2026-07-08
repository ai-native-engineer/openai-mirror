<!-- source: https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu -->

# Manage usage limits and overages in ChatGPT Enterprise and Edu

Learn how Enterprise and Edu workspace owners and admins can set monthly limits for users, control workspace overage usage, and monitor shared credits.

Updated: 6 hours ago

***Note:*** *Any existing weekly limits in Workspace settings → Permissions & roles → Weekly limits continue to apply until you configure monthly limits in Workspace settings → Usage limits. Remaining weekly limits will be migrated automatically in early August. After migration, weekly limits will no longer take effect.*

Enterprise and Edu workspaces have two independent controls for credit-based usage:

* **Usage limits** set a monthly limit for each user. You can apply a workspace default, group defaults, and user overrides.
* The **workspace overage limit** determines how much eligible credit-based feature usage can continue after the committed credit pool is exhausted.

Credit-based usage draws from the workspace’s shared credit pool. A user’s usage limit can stop that user before the pool is exhausted. If the pool is exhausted first, the workspace overage limit determines whether eligible usage can continue. User usage limits continue to apply during overage usage.

| **Control** | **Scope and purpose** | **Where managed** | **When reached** |
| Usage limits | Monthly limits for individual users, applied through workspace, group, and user levels | [Workspace settings → Usage limits](https://chatgpt.com/admin/usage-limits/workspace) | Additional eligible usage for the user is prevented; a task may finish slightly over the limit |
| Workspace overage limit | Workspace-wide cap after the shared credit pool is exhausted | [Global Admin Console → Billing](https://admin.openai.com/billing) | The workspace cannot continue into additional overage after the cap is reached |
| Usage alerts | Notifications at configured workspace credit thresholds | [Global Admin Console → Billing](https://admin.openai.com/billing) | Recipients are notified; alerts do not stop usage |

Workspace admins and owners can manage usage limits in Workspace settings. In the Global Admin Console, admins and owners can configure usage alerts and workspace overage limits. Only workspace owners can view invoices.

**Note: Both Usage limits and the Workspace overage limit have a 'No limit' setting option. 'No limit' has different meanings depending on the configuration surface.**

For a group override set in Usage limits, **No limit** means the group inherits the workspace default; it does not mean unlimited usage.

For the workspace overage limit, configured in the global admin console, **No limit** means no cap is configured on eligible overage usage.

# Manage monthly usage limits for users

Usage limits help Enterprise/Edu workspaces set monthly guardrails for individual users while preserving flexibility for groups and individual exceptions. Limits use a calendar-month window in UTC. Only workspace admins and owners can configure usage limits; members and analytics viewers cannot.

## Choose the level of control

Usage limits support multiple levels:

* **Workspace limits** set the monthly default for each user in the workspace.
* **Group limits** set the monthly default for each user in a group.
* **User limits**, also called user overrides, set a monthly limit for a specific user.

Configure limits and manage increase requests in **Workspace settings** → [**Usage limits**](https://chatgpt.com/admin/usage-limits/workspace).

## How limit precedence works

Usage limits are checked in this order: user override, highest applicable group default, then workspace default.

For example, an engineering group may need a higher default than a contractor group. A specific user can have an individual override if their expected usage differs from the rest of the group. If a user belongs to multiple groups, the highest applicable group default applies unless the user has an individual override.

## How usage limits and the overage limit interact

Suppose a user has a monthly limit of 6,000 credits. If the user reaches that limit, additional eligible usage is blocked for that user even if the workspace still has shared credits. If the workspace’s shared credit pool is exhausted first, the workspace overage setting determines whether eligible usage can continue. The user’s 6,000-credit limit still applies during overage usage.

## Manage requests to increase limits

In **Usage limits**, workspace admins and owners can allow users to request increases to their monthly limits.

This feature is enabled by default. With the default request process, members can request more usage in ChatGPT and Codex; requests appear in **Usage limits → Pending Requests**, workspace admins receive an email notification, and admins and owners can approve or deny requests.

Admins and owners can also disable requests or send members to a custom URL, such as an internal access request page. Custom request destinations are handled outside **Pending Requests**, so review and approval happen in the destination you choose.

Approved requests from **Pending Requests** create a user override that remains in place until it is changed or removed. Admins and owners can later update it from the **Users** tab in **Usage limits**.

## Migrate weekly limits

If you previously set limits in **Workspace settings → Permissions & roles → Set weekly limits**, you can migrate them to Usage limits manually. In early August, remaining weekly limits will be migrated automatically to monthly workspace and group defaults. After migration, the weekly limit setting will no longer apply.

Settings in **Usage limits** take precedence over a corresponding setting in **Permissions & roles → Weekly limits**. Usage limits are checked in this order: user override, highest applicable group default, then workspace default. If none of those layers apply, an existing limit in **Permissions & roles → weekly limits** can still apply until migration is complete.

Note that feature access and [RBAC](/en/articles/11750701-rbac) is still handled in **Permissions &** **r****oles**.

# Manage the workspace overage limit

Some ChatGPT Enterprise/Edu workspaces use flexible pricing with a shared credit pool. Each workspace’s credit allocation, rates, eligible usage, and billing terms are defined in its agreement with OpenAI.

Overages occur when an eligible workspace continues using credit-based features after its committed credit pool has been used. The additional usage is billed according to your agreement with OpenAI and any configured overage limit.

If you are unsure which terms or types of usage apply to your workspace, contact your OpenAI account team.

## Review credit usage and overage settings

Workspace owners and admins can review credit usage and overage settings from the global admin console:

1. Open the [global admin console](https://admin.openai.com/).
2. Select the relevant Enterprise/Edu workspace.
3. Select **Billing**.
4. Review **Unbilled overage** for eligible usage that has not yet been billed.
5. Download usage reports from the upper-right corner when you need additional detail.

Usage data may have a freshness delay. If you compare a downloaded report with a recent invoice, review the invoice period and report timestamp before escalating a mismatch.

## Set the workspace overage limit

OpenAI does not set a workspace overage limit by default. The setting appears as **No limit** until a workspace owner defines one. If no overage limit is set, certain feature usage can continue being utilized uninterrupted, but could incur unwanted overage charges. To avoid this, please be sure to set limits by going to the Billing tab.

To configure the workspace overage limit, open **Billing**, select **Manage** under **Overage limit**, and enter a credit value.

* Setting a limit restricts how far the workspace can continue into overages after its committed credit pool is exhausted.
* Setting the limit to 0 prevents the workspace from continuing into overages. Some advanced features may pause until additional credits are available or the limit changes.

## Configure usage alerts

Usage alerts notify selected recipients when the workspace reaches a chosen credit threshold, uses all committed credits, or reaches the overage limit. Alerts do not block usage. Use the workspace overage limit when you need a cap.

## **Understand and review overage invoices**

If overages have been set and are consumed in a given billing period, the additional usage will be billed at the end of the month, depending on your agreement with OpenAI. Overage invoices are separate from ChatGPT Go, Plus, Pro, Business web subscription billing and separate from API Platform billing.

An overage invoice includes a summary line item for eligible overage usage. Additional detail, such as usage reports or CSV exports, may be available in billing settings or from your OpenAI account team, depending on your workspace configuration.

If your organization requires a purchase order number, different billing contact, additional invoice recipients, or other invoice metadata, contact your OpenAI account team. These details may be governed by your Order Form or billing setup and may not be editable directly in ChatGPT.

## Before contacting Support or your account team

If an overage invoice or usage report does not look correct:

* Confirm that the invoice period matches the usage report period.
* Review the report timestamp because usage data may have a freshness delay.
* Confirm the credit allocation, expiration, rates, and invoicing terms in your Order Form or agreement.
* Confirm whether a workspace overage limit was configured.

## When to contact Support or your account team

Contact your OpenAI account team or OpenAI Support if you need help with:

* A charge you do not recognize.
* An invoice that appears to use the wrong rate or invoice period.
* A missing purchase order, billing contact, tax profile, payment detail, or invoice recipient.
* A workspace that should be excluded from overage billing.
* An agreement, promotion, waiver, or adjustment that should apply to the invoice.

Include the workspace name, workspace ID if available, invoice number, invoice period, downloaded usage report if available, and a brief description of the issue. Do not share passwords or one-time codes.

## Usage limits

### On what timeframe are usage limits measured?

Usage limits are configured for a calendar month and use UTC time. Usage counted toward a limit resets at the start of the next calendar month in UTC.

### What does 'no limit' indicate for Group overrides?

No limit in this context does not mean unlimited; it means that the group will fall back to the specified workspace default. Specifying a limit will result in a group-specific override being applied.

### What if limits are defined at multiple levels (user, workspace, groups)?

Usage limits are applied in this order: user override, highest applicable group default, then workspace default. If a user belongs to multiple groups, the highest group limit applies unless the user has an individual override.

### How do I check a user’s usage limit?

Open [**Usage limits**](https://chatgpt.com/admin/usage-limits/workspace) in Workspace settings, then review the relevant user or group.

### Can a user exceed their usage limit?

The credit value for some usage cannot be determined exactly until a task completes. A task that starts under the limit may finish and push usage slightly over the limit. Once the limit is reached, usage controls prevent additional eligible usage.

### What if a user is part of multiple groups?

The user is assigned to the group limit that is the greatest limit of the groups the user is part of. For example, if the workspace has a limit of 5,000 credits and a user is part of two groups, Group A with a limit of 7,000 credits and Group B with a limit of 8,000 credits, assuming the user does not also have an user override, that user will have a monthly limit of 8,000 credits.

### Can members change their limits?

Members cannot change limits. As members approach their limits, they may be notified and given an option to request an increase.

### What happens to existing weekly limits set in Permissions & roles limits?

By default, Usage limits are unset, and the weekly limits specified in Permissions & roles still apply. If you don't configure Usage limits, the limits specified in Permissions & roles continue to apply to groups and individuals until workspace defaults, group defaults, or user overrides are set.  
  
Note that if a specific user or group is not covered by a setting in Usage limits, or a workspace default is not assigned, any limits configured for them in Permissions & roles will continue to apply.  
  
Note that in early August, we will automatically migrate weekly limits set in Permissions & roles to monthly workspace and group defaults. After that time, the weekly limits setting will no longer take effect.

### Which limit applies if limits are set both in the Usage limits tab and in the Permissions & roles tab?

The settings in the Usage limits tab take precedence over the settings in Permissions & roles when both are configured. Usage limits are first checked for user overrides, then the highest applicable group default, then the workspace default. If none of those layers apply, the existing Permissions & roles limit can still apply.

### Why is the Usage limits pane showing credits used for a user that differs from credit usage shown in other analytics views?

Credits used data in Usage limits is close to real time while other analytics data is delayed. Additionally, due to the way we process data, the credits used in Usage limits may infrequently have temporary inaccuracies that are typically resolved shortly after they occur.

## Overage limits

### Who can view overage charges on invoices?

Workspace owners can view workspace billing information and invoices, including overage charges. Other roles may not have invoice access unless otherwise configured.

### Are ChatGPT workspace overages the same as API Platform billing?

No. ChatGPT workspace billing and API Platform billing are managed separately. Make sure you are reviewing the billing surface for the product you used.

### Why might my first overage invoice cover only part of a billing cycle?

Your first overage invoice may cover only part of a billing cycle, depending on when overage billing begins for your workspace and your organization’s billing date. If you have questions about the period shown on an invoice, contact your OpenAI account team or OpenAI Support.

### Can I update purchase order details or invoice recipients in ChatGPT?

This depends on your workspace billing setup and agreement with OpenAI. To update purchase order details, invoice metadata, or additional invoice recipients, contact your OpenAI account team.

### How are overage amounts calculated?

At a high level, overage amounts are based on credits used above your purchased or granted credits, multiplied by your contracted overage rate. Your exact rate and terms can vary by your agreement with OpenAI – contact your OpenAI account representative for more details.

### What is the default overage limit set to a workspace?

By default, there are no overage limits set for credit-based workspaces – this means it will be set as “No limit.” Any eligible credit-based feature usage can continue after the committed credit pool is used, and the additional usage may be billed according to your agreement with OpenAI. To avoid any unexpected overage charges, Admins should set overage limits to the workspace. Workspace owners can review and update the overage limit in the Global Admin Console in the billing tab.

### What happens if an overage limit is set to 0?

If an overage limit is set to 0, the workspace will not be allowed to continue into overages after the committed credit pool is exhausted. Advanced features may pause until additional credits are available or the limit is changed.
