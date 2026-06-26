<!-- source: https://help.openai.com/en/articles/20001273-setting-up-and-troubleshooting-sso-and-scim-for-ads-manager -->

# Setting up and troubleshooting SSO and SCIM for Ads Manager

Learn how tenant-level SSO and SCIM work with Ads roles, how to create or access additional ad accounts, and how to troubleshoot sign-in issues.

Updated: 10 hours ago

Single sign-on (SSO) and System for Cross-domain Identity Management (SCIM) for Ads Manager are configured at the OpenAI tenant level in the [Global Admin Console](https://admin.openai.com/). Ads access is then controlled through Ads-specific administrative and ad-account roles.

# **Before you begin**

* You must be a Global Admin to configure tenant-level identity settings and manage tenant membership.
* A user must have the Ads Admin role to create ad accounts in the tenant.
* Access to an existing ad account requires an ad-account role: Ad Account Admin, Ad Account Member, or Ad Account Viewer.
* Use the same work email address in your identity provider, the Global Admin Console, and Ads Manager.

# **How Ads roles work**

Global Admin and Ads Admin are separate roles. A Global Admin can manage the tenant, identity settings, and users, but being a Global Admin does not automatically grant permission to create an ad account. Assign the Ads Admin role to users who need to create ad accounts.

After an ad account exists, assign the appropriate ad-account role to each user or group. A single email address can access multiple ad accounts when that user has been assigned a role in each account.

# **Set up SSO for Ads Manager**

1. Open the [Global Admin Console](https://admin.openai.com/) and select the tenant you want to manage.
2. Configure and verify your domain and identity provider by following [Configuring SSO](/en/articles/9534785-configuring-sso).
3. Add the users or groups who need Ads access to the tenant.
4. Assign Ads Admin to anyone who needs to create ad accounts. For an existing ad account, assign Ad Account Admin, Ad Account Member, or Ad Account Viewer as appropriate.
5. Ask the user to open [Ads Manager](https://ads.openai.com/) and sign in with the same work email address configured in the tenant.

If your organization also uses ChatGPT or the API platform, working SSO in those products does not by itself grant Ads access. Confirm the user is in the correct tenant and has the required Ads role.

# **Set up SCIM for Ads Manager**

For Ads-only customers, SCIM provisioning is managed at the tenant level in the Global Admin Console. Tenant-level SCIM for Ads does not replace product-level SCIM configurations used for ChatGPT or the API platform.

1. Configure SCIM by following the [SCIM Integration FAQ](/en/articles/10011769-scim-integration-faq) and your identity provider's instructions.
2. Assign the required users or groups to the OpenAI application in your identity provider and confirm that provisioning succeeds.
3. In the Global Admin Console, confirm that the provisioned user appears in the tenant. If an invitation is pending, the user must accept it.
4. Assign Ads Admin if the user needs to create ad accounts, or assign an ad-account role for each existing account the user should access.
5. Ask the user to sign in to Ads Manager with the provisioned email address.

You can also assign a SCIM-synced group to an Ads role. This lets role access follow group membership managed in your identity provider.

# **Create another ad account**

1. Confirm that the user has the Ads Admin role in the tenant. Global Admin alone is not sufficient.
2. Open [Ads Manager](https://ads.openai.com/) with the email address associated with the tenant.
3. Use the option to create a new ad account. If the option is not shown, confirm the Ads Admin role and that the user is operating in the intended tenant.
4. After creation, assign ad-account roles to the users or groups who need access.

Do not rely on a direct onboarding URL to create an additional account. If the user already has an Ads Manager session, the site may open their existing account instead of starting a new onboarding flow.

# **Troubleshooting sign-in and access**

## **The user is sent to a password login instead of the identity provider**

* Confirm the user entered the same work email address that is configured in the tenant and identity provider.
* Confirm that the email domain is verified and SSO is configured for the intended tenant.
* Ask the user to sign out of other OpenAI accounts or retry in a private browser window to avoid using an existing session for a different email address.
* If the issue continues, contact OpenAI Support with the user's email address, tenant ID, approximate timestamp and time zone, and a screenshot of the page or error.

## **The user can sign in but cannot create an ad account**

Confirm that the user has the Ads Admin role. Global Admin and ad-account roles do not automatically include permission to create a new ad account.

## **A SCIM-provisioned user cannot access Ads Manager**

* Confirm the provisioning event succeeded in the identity provider.
* Confirm the user appears in the correct tenant and has accepted any pending invitation.
* Confirm that the user or their synced group has the required Ads Admin or ad-account role.
* Confirm that the email address used to sign in exactly matches the provisioned identity.

# **Frequently asked questions**

## **Is SSO or SCIM managed at the tenant level?**

Yes. For Ads-only customers, SSO and SCIM are configured in the Global Admin Console at the tenant level. Ads Admin and ad-account roles are then used to control Ads-specific permissions.

## **Is Global Admin the same as Ads Admin?**

No. Global Admin manages the tenant and identity configuration. Ads Admin grants permission to create ad accounts and manage Ads access.

## **Does SCIM automatically grant access to every ad account?**

No. SCIM provisions the user's tenant identity. The user or a synced group must also be assigned the appropriate Ads Admin or ad-account role.

## **Can the same email address access multiple ad accounts?**

Yes. Assign the user an appropriate role in each ad account. The user can then use the same email address to access those accounts.

## **Why does SSO work for another OpenAI product but not Ads Manager?**

Authentication and product access are separate. Confirm that the user is in the intended tenant and has an Ads-specific role, even if SSO already works for ChatGPT or the API platform.

# **Related articles**

* [Configuring SSO](/en/articles/9534785-configuring-sso)
* [Managing Ads users in the Global Admin Console](/en/articles/20001192-managing-ads-users-in-the-global-admin-console)
* [SCIM Integration FAQ](/en/articles/10011769-scim-integration-faq)
