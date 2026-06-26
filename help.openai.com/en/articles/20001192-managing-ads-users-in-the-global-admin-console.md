<!-- source: https://help.openai.com/en/articles/20001192-managing-ads-users-in-the-global-admin-console -->

# Managing Ads users in the Global Admin Console

Learn what Ads-only customers can manage in the Global Admin Console, including tenant-level user management, roles, groups, SSO, and SCIM provisioning.

Updated: 2 days ago

Ads-only customers can now manage Ads users at the tenant level in the Global Admin Console. Admins can invite users, assign roles, manage groups, and set up SCIM provisioning from the same place they already use for SSO and domain verification.  
  
The available tenant-level roles for Ads are:

* **Ads Admin**: can create ad accounts in the tenant.
* **Ad Account Admin**: full access to ad account data
* **Ad Account Member**: can read and write ad entities without ad account administration controls
* **Ad Account Viewer**: can view ad account data without write or administration controls

**This update is for Ads-only customers.** If your organization also uses ChatGPT, API, Codex, or other OpenAI products, do not treat this as full cross-product user and role management. Broader support across OpenAI products is planned for a later update.

# Current limitations

The Global Admin Console does not yet provide full cross-product user and role management.  
  
At this time:

* ChatGPT, API, Codex, and other product roles are not shown or managed in the Global Admin Console.
* SCIM in the Global Admin Console supports Ads users only.
* Custom tenant-level roles are not supported.

You may see users across OpenAI products in the Global Admin Console. However, broader cross-product user and role management is not yet available.

# Configuring SCIM

Global Admins can configure SCIM by navigating to the [Directory tab of the Access page](https://admin.openai.com/identity?tab=directory) and clicking the “Enable Directory Sync (SCIM)” button:

![Cloud Console M2 - Enable Directory Sync](https://images.ctfassets.net/j22is2dtoxu1/4jTqzHQCV4QajnqpYTqAbd/522d51794201dce6972045f7a9d3c848/Screenshot_2026-04-14_at_12.02.13â__PM.png)

This will redirect you to the setup wizard, which provides a step-by-step guide to configuring a SCIM app in your IdP. For more information, please see our documentation page on [Common SCIM Questions](/en/articles/10011769-scim-integration-faq).  
  
It can take up to 5 minutes for the SCIM connection to activate, and up to 5 minutes to show the latest events issued by your IdP. Following a successful connection, you can begin observing your events back on the Directory tab:

![Cloud Console M2 - Access page](https://images.ctfassets.net/j22is2dtoxu1/6mCV5YnAwUVe0PxgVvNjGW/386422c797557e10b5efd199f00accd1/Screenshot_2026-04-14_at_12.20.08â__PM.png)

## Adding Users to an Ads Account with SCIM

Once SCIM has been configured, there are two main options for how to provision users access to your Ads Account.  
  
The first option is direct provisioning. From [the Users page,](https://admin.openai.com/people) you can click on a given user’s row to be directed to their management panel. From here, you can assign them directly to a group that has the “Ad Account Admin” role or else you can assign this role directly to the user as shown below:

![Cloud Console M2 - Assign role to user](https://images.ctfassets.net/j22is2dtoxu1/2be3AOP3Ayc52kw1IhNhu8/9ec00318019043d41e90a485eef56e80/Screenshot_2026-04-14_at_1.51.09â__PM.png)

The second option is via a SCIM group. If you synced SCIM groups from your IdP into the Admin Console, you can subsequently assign them to specific roles. In this case, you will want to assign your group the “Ad Account Admin” role as shown below:

![Cloud Console M2 - Assign role to group](https://images.ctfassets.net/j22is2dtoxu1/QdfmdcNaQ5IVfQjYmUN9t/a857f4ce8f060b42a520f7eb1a5aa277/Screenshot_2026-04-14_at_1.49.19â__PM.png)

Following this, any users in your SCIM group will now be able to log into your Ads Account.

## Assigning the Ads Admin Role

Similarly, once you have users in your Tenant, you can provision them to the Ads Admin Role. From [the Users page,](https://admin.openai.com/people) you can click on a given user’s row to be directed to their management panel. From here, select the **Direct roles** tab, then click the **+** button in the top-right corner.

![direct roles tab](https://images.ctfassets.net/j22is2dtoxu1/4ECnJWfCmb7oodXbUJ8ch4/7d499cf5cf809171ef7dc5173035ad35/direct_roles.png)

This will open a modal shown below where you can assign the **Ads Admin** role. It is important to note that the following roles do not appear if there are no Ad Accounts in the Tenant:

* Ad Account Admin
* Ad Account Member
* Ad Account Viewer

Instead, you will only see the "Ads Admin" role shown below:

![Ads Admin](https://images.ctfassets.net/j22is2dtoxu1/2xcqpNxDh0Ef38yXPLSUc2/7dd124bd12483f0b69fef5e9f0766d59/Screenshot_2026-04-30_at_3.56.14%C3%A2__PM.png)

Once this role has been granted, its users can create Ad Accounts in the Tenant and thus enable the remaining Ads roles for use.

# FAQ

## Will this rollout cause any breaking changes?

No. This rollout does not introduce breaking changes.

## Why is this only available for Ads-only customers?

At launch, the Global Admin Console does not yet support viewing or managing ChatGPT or API roles. Broader support across OpenAI products is planned for a later update.

## Does SCIM support all products?

No. At launch, tenant-level SCIM in the Global Admin Console supports Ads users only. ChatGPT and API users still need to set up SCIM at the product level.

## What if I need to remove a user from the Ad Account Admin role?

It's recommended to ensure at least one Ad Account Admin remains on an ad account; if you need to remove the only Ad Account Admin, add another Admin before doing so.

## Can I create custom tenant-level roles?

No. The available tenant-level roles are **Global Admin** and **Member**.

## Ads access and SSO FAQ

### What is the difference between an Ads Admin and an ad account role?

An Ads Admin manages Ads users, groups, SSO, and SCIM settings in the Global Admin Console. Ad account roles control what someone can do inside a specific Ads Manager account, such as viewing or managing campaigns. A user may need both the right tenant-level access and the right ad account role before they can work in Ads Manager.

### Why can’t I create an ad account?

If your company already has an OpenAI tenant, you may need an Ads Admin to grant you Ads access in the Global Admin Console before you can create or manage an ad account. If you were invited to an existing ad account, confirm that you accepted the invitation with the same email address and that the account owner assigned the correct ad account role.

### How do SSO Required, Optional, and Off affect Ads users?

When SSO is Required, users must authenticate through your identity provider and also be assigned to the correct IdP application. When SSO is Optional, eligible users can use SSO or another supported sign-in method. When SSO is Off, Ads users sign in without SSO. If a user cannot sign in after SSO is enabled, check the domain, IdP assignment, user email, and Ads role assignment.

### Does ChatGPT workspace membership automatically grant Ads access?

No. ChatGPT workspace membership and Ads access are managed separately. Ads-only customers should manage Ads users in the Global Admin Console, and ad account access still needs to be assigned inside Ads Manager.

### Does SCIM provisioning apply to all OpenAI products?

For Ads-only tenants, SCIM provisioning in the Global Admin Console manages Ads users for that tenant. SCIM configuration for other OpenAI products may be managed separately, so confirm you are configuring the correct OpenAI application and tenant.
