<!-- source: https://help.openai.com/en/articles/12289294-managing-your-tenant-in-admin-console -->

# Managing your tenant in Admin Console

Find your tenant, switch between products, and manage the users, roles, and settings available in Admin Console.

Admin Console is where authorized admins manage their OpenAI tenant and the product resources their role allows them to access. Use **Global settings** for tenant-wide identity, or select a ChatGPT workspace or Ads account for product-specific settings.

What you can see depends on your products, plan, and administrator roles. For ChatGPT, the updated Admin Console experience is available to eligible Enterprise and Edu workspaces. Standalone ChatGPT Business customers continue using their existing ChatGPT workspace settings.

# Open Admin Console and select a resource

![Screenshot of the OpenAI Admin Console showing a “Choose what to manage” page. It lists available resources under a tenant, including Global settings, a ChatGPT workspace, and an Ads account, with an option to use another account.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_I_yf3jFRb8zUBqTgQBLew459f4fjUVSrBAmIkjtisZg/0506c81d84f1248c676366cd68969bcc/lbas_img_I_yf3jFRb8zUBqTgQBLew459f4fjUVSrBAmIkjtisZg.png?q=80&fm=webp&w=1344)

![Screenshot of the OpenAI Admin Console with the left navigation resource selector expanded. It shows options for a tenant global settings entry, a ChatGPT workspace, and an Ads account, while the main panel on the right displays an Overview page with a Daily active users section.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_EeGcd8SSEZQ-q6YgMKcNTtIuZYxJ_OAsBhUBP8l_XC0/94d7bc172b433859b1fc19ca2c49209a/lbas_img_EeGcd8SSEZQ-q6YgMKcNTtIuZYxJ_OAsBhUBP8l_XC0.png?q=80&fm=webp&w=864)

1. Sign in to [Admin Console](https://admin.openai.com) with the OpenAI account associated with your tenant.
2. If you have access to more than one tenant, select the tenant you want to manage.
3. Choose **Global settings** for tenant-wide administration, or select the ChatGPT workspace or Ads account you want to manage.
4. Open the available section for your task, such as **Access**, **Users & groups**, **Analytics**, or **Billing**.

A resource appears only when it belongs to the selected tenant and your role allows you to access it. If a section is unavailable, confirm the selected account, tenant, and administrator role.

![Screenshot of the OpenAI Admin Console showing a resource selector menu. The selected resource is “Acme Enterprise” labeled “ChatGPT workspace,” and the dropdown lists “Acme Corp.” as Global settings, “Acme Enterprise” as a ChatGPT workspace with a checkmark, and “Acme Advertising” as an Ads account.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_sjrhRRlybd9GWu5aB1GwBIb9qEkSpH-3kzXu2AimcoM/de1f4ceb8fce492414dece161065beeb/lbas_img_sjrhRRlybd9GWu5aB1GwBIb9qEkSpH-3kzXu2AimcoM.jpg?q=80&fm=webp&w=522)

If you are invited as a global admin before you have an OpenAI account, open Admin Console and create an account with the invited email address. Under **Pending invitations**, select **Accept**. Joining the tenant does not give you access to a ChatGPT workspace, API organization, or Ads account.

The tenant’s **Users** list is not the same as a ChatGPT workspace’s **Members** list. If counts, a workspace, or analytics are missing, confirm the selected tenant and open the workspace itself. Ask OpenAI Support or your account team to check an unexpected tenant association; do not create a replacement tenant or workspace.

# Understand administrator roles and boundaries

| **Role or access** | **What it can manage** | **What it does not grant** |
| --- | --- | --- |
| Global admin | Supported tenant-wide identity settings, verified domains, identity-provider connections, tenant administration, and eligible advertising-account creation. | Automatic owner or admin access to every ChatGPT workspace, API organization, or Ads account. |
| User manager (where available) | Assigned tenant users and groups, where this role is available. | The ability to assign or remove global admins, change tenant-wide settings, or administer another product. |
| Member | Read-only access to supported tenant users, groups, roles, and resources. | The ability to change tenant settings, manage users or groups, or grant administrator roles. |
| Ads admin | Permission to create eligible advertising accounts. | Automatic access to every existing advertising account. |

One person can hold several roles, but each role must be assigned in its own scope. For details about ChatGPT workspace roles, see: [Role Based Access Controls for ChatGPT Enterprise](https://help.openai.com/articles/11750701). A tenant **Member** role is separate from membership in a ChatGPT workspace.

# Manage tenant-wide identity

![Screenshot of an Admin Console Access page with the Domains tab selected. A search box appears at the top right, and a table lists the domain “example.com” with products shown as “All workspaces, All API orgs.”](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_OoozZ3Ev1b-fTGHWQcII5M9x1lkIHof6y5zaieZSw6c/116d8079bba2b4fa653b645ada561cdd/lbas_img_OoozZ3Ev1b-fTGHWQcII5M9x1lkIHof6y5zaieZSw6c.png?q=80&fm=webp&w=1344)

## Review domains and sign-in settings

In **Global settings**, open **Access** > **Domains** to review domain verification status and product eligibility. A newly verified domain can initially apply to all eligible ChatGPT workspaces and API organizations. Review the resulting mappings and confirm an administrator recovery path before changing sign-in requirements.

For domain verification and product eligibility, see: [Verifying your domain for OpenAI identity](https://help.openai.com/articles/8871611).

A standalone ChatGPT Business workspace owner manages SSO and domains from the workspace’s existing identity settings. If those settings are read-only or show **Cloud Console ↗**, ask a global admin to manage the shared tenant connection. For Business setup and plan limits, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188).

## Choose how people join

Automatic account creation and external-domain invitations are configured for an individual ChatGPT workspace. Automatic account creation does not require SSO. Review seat usage, existing personal accounts, and any Enterprise or Edu migration prompt before enabling it.

For employees with personal, Plus, or Pro accounts, see: [Onboarding employees with existing ChatGPT accounts](https://help.openai.com/articles/10479654).

## Check directory sync and existing connections

In **Global settings**, open **Access**, then select **Directory** to review available tenant-wide SCIM and synchronization status. Tenant-wide SCIM cannot be enabled while a linked ChatGPT workspace or API organization has an active product-level connection. Coordinate an approved migration before changing an existing connection.

For directory setup, product assignments, and synchronization, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

## Manage external application access

Where available, **External Access** controls whether members can use Sign in with ChatGPT for supported external applications. Use **Enable Sign in with ChatGPT for your organization** and **Approved applications** to apply your tenant’s external application rules.

# Review users, groups, and product access

![Screenshot of the OpenAI Admin Console showing the Users & groups page. A left sidebar lists navigation items such as Overview, Access, Users & groups, and External Access, while the main panel displays a user list with columns for users and groups.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_C1KQM4ZUDXc8umvRtsj4rvNrUKLUt1Xj6MRkTbyxayc/5dcedd2378425b8946ce6a63ce7668d1/lbas_img_C1KQM4ZUDXc8umvRtsj4rvNrUKLUt1Xj6MRkTbyxayc.jpg?q=80&fm=webp&w=1344)

Go to **Users & groups** and select **Users** to find a person in the selected tenant. Open the person’s profile and select **Access & roles** to review product access. Depending on the available view, direct assignments may appear under **Direct roles**. Select **Groups** to review the person’s group memberships, and select **SCIM Groups** to inspect synchronized groups.

![Users & groups page in Admin Console with Users and SCIM Groups tabs, a search field, and user names, email addresses, and group counts.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_PSQ7BOJ6EbIUzc_YapNnSmu81RskklJm4PPKKUHARXM/8c02b74f6c4f6cc7988136e90378d2bf/lbas_img_PSQ7BOJ6EbIUzc_YapNnSmu81RskklJm4PPKKUHARXM.png?q=80&fm=webp&w=1344)

For tenant-synchronized SCIM groups, **Product access** can assign supported ChatGPT workspaces and Ads accounts. API organizations are not available in this editor. Review advertising-account roles in the selected Ads account.

![Screenshot of an Admin Console user profile for Avery Chen on the Access & roles tab. A left navigation sidebar shows sections such as Overview, Access, Users & groups, External Access, Usage, Credits, Environments, and Audit logs. The main panel lists product access for ChatGPT, including Acme Enterprise, and role assignments for Admin Console and an Ads account.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_3ZDPqVmE9oy7RyuIqx65-b7beRCfz_wLTi47gc3RexU/c29664885cc0a59b30863db73e16a545/lbas_img_3ZDPqVmE9oy7RyuIqx65-b7beRCfz_wLTi47gc3RexU.jpg?q=80&fm=webp&w=1344)

Before granting access, review a group’s existing product and role assignments and use the least-privileged role required. Tenant-wide **Product access** does not assign custom ChatGPT workspace roles.

A synchronized group is managed by your identity provider. Do not add or remove its members directly in a product. Manage Enterprise and Edu workspace members and groups in Admin Console, Business workspace members and groups in ChatGPT, API organization members in the API Platform, and Ads users in the appropriate advertising account.

The presence of a user in **Users** does not replace a product invitation or grant membership across every resource. Manual invitations remain specific to the supported ChatGPT workspace, API organization, or Ads account.

# Manage a selected Ads account

Select the intended Ads account before reviewing **Users & groups** or account-specific roles. A global admin or Ads admin can create advertising accounts; an ad account admin, member, or viewer receives permissions for a particular account.

For Ads sign-in, account roles, and directory-access rules, see: [Managing identity and access for Ads Manager](https://help.openai.com/articles/20001273).

# Review analytics, audit logs, credentials, and billing

## Analytics

Depending on your role and plan, **Analytics** can include ChatGPT or Codex usage, active users, leaderboards, credits, and exportable activity. Available data windows and refresh times vary by report. Estimated costs, when shown, are planning estimates rather than settled charges or invoices. Where available, a workspace member can review only their own activity unless a separate workspace role grants broader access.

| **Analytics area** | **Historical window** | **Typical refresh** |
| --- | --- | --- |
| ChatGPT and Codex credit analytics | Up to 120 days. | Approximately every 1 to 6 hours. |
| Codex usage analytics | Up to 120 days. | Approximately every 1 to 6 hours. |
| ChatGPT usage analytics | Up to the previous 12 months. | Up to 48 hours. |

Codex product access does not automatically include analytics. Where available, a workspace owner can grant **Allow members to administer Codex** through a custom role. This gives the user access to supported Codex usage analytics for that workspace without making them a workspace admin or global admin.

Where available, workspace analytics can be filtered by synchronized groups, such as a department or pilot team. Group visibility and analytics access depend on the selected workspace and your role. Follow your company’s or school’s privacy policies.

Where available, estimated costs use the selected workspace’s pricing and are planning estimates, not settled charges. The issued invoice is the authoritative billing record. For deeper ChatGPT reporting, including eligible GPT, project, or skill activity, use the selected workspace’s analytics settings.

## Audit logs

Where available, a global admin can open **Global settings**, then select **Audit logs** under **Security** to review tenant-wide administrative activity. Workspace audit logs are separate and available only to eligible workspace owners or admins. If **Audit logs** is missing, check the selected tenant or workspace, your role, and feature availability.

## Credentials

Workspace owners and admins can use **Credentials > Admin keys** in an eligible ChatGPT workspace to manage workspace-scoped Admin keys for supported administration APIs. A global admin role alone does not grant access. Admin keys do not grant access to models or model inference. For setup, permissions, and key management, see: [Managing Admin keys in Admin Console](https://help.openai.com/articles/20001407). Where available, separate Codex service-account credentials support automation. For setup guidance, see: [Create and manage Codex service accounts](https://developers.openai.com/codex/enterprise/service-accounts).

## Billing and agents

Available **Billing** and agent-management sections depend on the selected resource, plan, and permissions. Billing access for one workspace or product does not grant access to another.

For eligible Enterprise or Edu workspaces, **Billing** can include **Plan**, **Grant activity**, and **Invoices**. Billing is scoped to the selected workspace, and invoice access can require the workspace owner role.

## Review workspace usage limits

The separate **Usage limits** page can show **Workspace**, **Groups**, **Users**, and, when available, **Pending requests**. The workspace default applies unless an eligible group or user override provides a different limit. Where available, **Allow users to see usage in credits and dollars** changes what members can see without changing usage limits or overage settings.

* **Monthly (default)** resets on the first day of each calendar month in UTC.
* **Aligned to billing cycle** resets on the monthly period anchored to the workspace billing cycle.
* An eligible user or group override can use **Unlimited usage** when that option is available.
* Removing an override returns the user or group to the next applicable inherited limit.
* When a person reaches an applicable limit, additional eligible usage can pause until the limit increases or the next usage period begins.

## Review workspace agents

Where available, the agent area lets authorized administrators review workspace agents, associated activity, connected apps, memory files, schedules, and supported agent analytics. Agent access depends on the selected resource and administrator role.

# Resolve access or missing-resource problems

* Confirm that you signed in with the correct OpenAI account and selected the intended tenant.
* Check whether you need a global admin or user manager role for a tenant-wide task.
* Check whether you need an owner, admin, Ads admin, or account-specific role for the selected resource.
* Complete any required SSO sign-in before opening a protected resource.
* Continue managing API organization members, projects, and settings in the API Platform.
* Contact your global admin or account team if an expected resource or feature remains unavailable.
