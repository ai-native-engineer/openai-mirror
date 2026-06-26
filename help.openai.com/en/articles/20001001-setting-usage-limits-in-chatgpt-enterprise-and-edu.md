<!-- source: https://help.openai.com/en/articles/20001001-setting-usage-limits-in-chatgpt-enterprise-and-edu -->

# Setting usage limits in ChatGPT Enterprise and Edu

Usage limits help Enterprise and Edu admins manage workspace credit usage with workspace, group, and user-level limits.

Updated: 5 hours ago

*Starting June 18, 2026, OpenAI is adding* [***Usage limits***](https://chatgpt.com/admin/usage-limits/workspace) *in Workspace settings as a new, streamlined method to set* ***monthly credit limits*** *by workspace, group, and user. Existing usage limits set in* ***Workspace settings -> Permissions & roles -> weekly limits*** *remain available for now, but will be overridden by settings in the Usage limits section. Review the article below carefully to understand how to migrate your current settings.*

*Currently, Usage limits are not automatically set, and the weekly limits in Permissions & roles still apply until you configure limits for your workspace, groups, or users in Usage limits. In early August, we will automatically migrate weekly limits set in Permissions & roles to monthly workspace and group defaults. After that time, the weekly limits setting will no longer take effect.*

## Overview

Usage limits help Enterprise and Edu workspaces manage credit spend without blocking normal adoption. Admins and owners can use the Usage limits pane in Workspace settings to configure for monthly usage limits for workspace users. Usage limits are intended to help admins and owners:

* Set monthly guardrails for credit usage
* Limit unexpected overage from high-usage users, groups, or workflows
* Give power users enough room to keep working within approved budgets

Limits are configured for a calendar month and use UTC time for the monthly window. Note that only admins and owners can configure usage limits; members and analytics viewers cannot.  
  
Read more about roles in ChatGPT Enterprise workspaces.

## Types of limits

Usage limits supports hard spend limits for multiple levels of control:

* **Workspace limits** sets monthly usage caps for each user in the workspace
* **Group limits** sets monthly usage caps for each user in the group
* **User limits (or user override limits)** sets a monthly cap to a specific user.

Use the level that matches the control you need. Workspace limits and group limits are useful for wholesale configurations of limits, and user limits are useful for individual exceptions or high-usage users. You can these limits and manage requests from users to increase limits in **Workspace settings** -> [**Usage limits**](https://chatgpt.com/admin/usage-limits/workspace)

### Example: using workspace, group, and user limits together

An organization may use a workspace limit to set a general control on individual use but use group limits and user limits for more custom configurations or exceptions.  
  
For example, an engineering group that uses ChatGPT and Codex heavily may need a higher limit than a contractor group with occasional usage. A specific power user can also have an individual override if their expected usage differs from the rest of their group.  
  
This approach lets the workspace set an overall spend guardrail while still giving high-value users enough room to work.

## Requests to Increase Limits

In **Usage limits,** workspace admins and owners can allow users to request increases to their monthly usage limits.

This feature is enabled by default, and can be disabled, or customized to route requests to a custom destination, such as an internal access request web page.

If enabled, users will have in-product paths to request usage limit increases when they exceed their monthly limit. Workspace admins and owners can review requests in **Usage limits -> Pending Requests** and approve or deny requests.

Approved requests result in a user override limit that persists until changed or removed (they are not temporary limit increases). Admins and owners can later update the user's configured limit in the **Users** tab in the **Usage limits** pane.

### Migrating from Usage limits configured in Permissions & Settings

If you have previously set limits in **Workspace settings -> Permissions & roles -> Set weekly limits**, you can migrate them to the new Usage limits configuration manually. By early August, we will migrate any remaining settings automatically to workspace and group defaults, and convert to monthly limits - the weekly limit setting will no longer be applicable.  
  
Settings in Usage limits take precedence over a corresponding setting in Permissions & roles when both are configured. Usage limits are first checked for user overrides, then the highest applicable group default, then the workspace default. If Usage limits are not configured, the existing limits configured in Permissions & roles are used as a fallback.

## FAQ

### On what timeframe are usage limits measured?

Usage limits are configured for a **calendar month and use UTC time.** Any usage counted towards a limit resets at the start of the next calendar month UTC time.

### Why is the Usage limit pane showing 0 credits for a given user, even though they have usage displayed in other analytics?

Upon launch, the pane may show zero credits used for a given user for a period of time. This information will populate automatically after the rollout.

### What does 'no limit' indicate for Group overrides?

No limit in this context does not mean unlimited; it means that the group will fall back to the specified workspace default. Specifying a limit will result in a group-specific override being applied.

### What is the logic on how limits are applied when defined at multiple levels (workspace, group, user)?

Usage limits are first applied on the user override setting, then the highest applicable group default, then the workspace default. For example, if a user has an override of 6,000 credits and is part of a group with a limit of 7,000 credits and the workspace has a limit of 5,000 credits, the user will be given a monthly credit limit of 6,000 credits.

### What if a user is part of multiple groups?

The user is assigned to the group limit that is the greatest limit of the groups the user is part of. For example, if the workspace has a limit of 5,000 credits and a user is part of two groups, Group A with a limit of 7,000 credits and Group B with a limit of 8,000 credits, assuming the user does not also have an user override, that user will have a monthly limit of 8,000 credits.

### How do I check a user's usage limits?

Open [Usage limits](https://chatgpt.com/admin/usage-limits/workspace) in workspace settings, then review the relevant user or group. If **Usage limits** is not visible, your workspace may not be eligible or enabled yet.

### Are users able to exceed their limits?

The credit value for some usage cannot be determined exactly until a task completes, so a task that starts under the limit may complete and push usage slightly over the limit. Once the limit is reached, spend controls prevent additional usage.

### What happens to existing weekly limits set in Permissions & roles limits?

At launch, **Usage limits** are unset, and the weekly limits specified in **Permissions & roles** still apply. If you don't configure Usage limits, the limits specified in Permissions & roles continue to apply to groups and individuals until workspace defaults, group defaults, or user overrides are set.  
  
Note that if a specific user or group is not covered by a setting in Usage limits, or a workspace default is not assigned, any limits configured for them in Permissions & Roles will continue to apply.   
  
Note that in early August, we will automatically migrate weekly limits set in Permissions & roles to monthly workspace and group defaults. After that time, the weekly limits setting will no longer take effect.

### Which limit applies if limits are set both in the **Usage limits** tab and in the **Permissions & Roles** tab?

The settings in the **Usage limits** tab take precedence over the settings in **Permissions & Roles** when both are configured. Usage limits are first checked for user overrides, then the highest applicable group default, then the workspace default. If none of those layers apply, the existing **Permissions & Roles** limit can still apply.

### Can members see or change their limits?

Members cannot change limits. As members approach their limits, they may be notified and with an option to request an increase to their limits.
