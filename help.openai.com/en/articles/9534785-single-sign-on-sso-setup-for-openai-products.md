<!-- source: https://help.openai.com/en/articles/9534785-single-sign-on-sso-setup-for-openai-products -->

# Single sign-on (SSO) setup for OpenAI products

Connect an identity provider, verify a domain, and configure single sign-on for eligible OpenAI products.

Single sign-on (SSO) lets your team sign in using an existing work account. Your setup depends on whether identity is managed by a ChatGPT Business workspace, a shared OpenAI tenant, or an eligible standalone API Platform organization.

Before you begin, identify the product you are configuring and the admin who can manage its identity settings. For an introduction to tenants and product access, see: [Getting started with OpenAI identity and access for managed workspaces](https://help.openai.com/articles/9047883).

# Choose the right SSO setup for your plan

| **What you need to manage** | **Who can make changes** | **Where to start** | **What to know** |
| --- | --- | --- | --- |
| ChatGPT Enterprise or Edu | global admin | Open [Admin Console](https://admin.openai.com/identity) and select your tenant’s **Access** settings. | The shared identity-provider connection can apply to supported ChatGPT workspaces and other eligible products. Review each product’s sign-in policy separately. |
| Standalone ChatGPT Business | workspace owner | Open your Business workspace’s **Identity & access** settings. | Use the existing workspace identity settings for SSO and domain verification. If they are read-only, ask a global admin to manage the shared tenant connection. For setup, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188). |
| API organization linked to a tenant | global admin | Start in [API Platform identity settings](https://platform.openai.com/settings/organization/identity). If SSO or domain controls are read-only, follow the link to Admin Console. | Manage the shared connection and applicable API product policy in Admin Console. API members, projects, billing, and API organization settings stay in the API Platform. |
| Ads Manager | global admin | Open [Admin Console](https://admin.openai.com/identity) and select the relevant tenant and Ads product. | Turning on the shared connection does not automatically turn on Ads SSO or grant an advertising-account role. For the Ads-specific flow, see: [Managing identity and access for Ads Manager](https://help.openai.com/articles/20001273). |

If your identity settings are read-only, you are usually looking at a product that now uses the tenant’s shared connection. Follow the link to Admin Console instead of setting up a second identity provider.

If a ChatGPT workspace shows **Cloud Console ↗** beside read-only identity settings, use it to open Admin Console. Ask an authorized global admin to manage the shared connection.

SSO controls how people sign in. Invitations, product membership, and administrator roles remain separate.

# Check your access before you begin

* Confirm which OpenAI tenant, ChatGPT workspace, API organization, or Ads account you need to manage.
* Confirm that you are a global admin for a tenant-managed connection or the workspace owner for a standalone ChatGPT Business connection.
* Check that your subscription or API billing plan includes the relevant SSO capability.
* Confirm that you can update DNS records for a domain controlled by your company or school.
* Confirm that you can create or update the application in your identity provider.
* Identify the users who need access and any existing product memberships, invitations, or SCIM connections.

SSO availability and identity-provider options depend on the product, plan, tenant, and current setup. A ChatGPT subscription does not automatically include API organization access or API SSO.

## Apply identity-provider security policies

Configure multi-factor authentication (MFA), device restrictions, and conditional-access rules in your identity provider. Those controls apply when someone authenticates through that provider. Users who can sign in another permitted way may not be covered by the same identity-provider rules.

# Protect administrator access

1. Keep one authenticated administrator session open in your regular browser.
2. Use a private or incognito window to test the identity-provider sign-in flow.
3. Leave SSO **Optional** while you verify the connection and affected accounts, when that setting is available.
4. Confirm that another authorized administrator or approved recovery method is available before selecting **Required** or **Off**, changing a connection, or rotating a certificate.

Do not use **Off** as a substitute for “not enforced”: it disables SSO for the selected product and can sign out affected users.

# Set up SSO for ChatGPT Business

ChatGPT Business includes SSO and domain verification for an active, paid workspace. A workspace owner configures an independently managed connection in the existing ChatGPT workspace settings. If the settings are read-only or show **Cloud Console ↗**, ask a global admin to manage the shared tenant connection. For Business-specific steps and plan limits, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188).

The remaining setup steps apply to tenant-managed SSO connections and must be completed by a global admin.

# Open your tenant’s identity settings

1. Sign in to [Admin Console](https://admin.openai.com/identity) as a global admin.
2. Select the OpenAI tenant you need to manage.
3. Open **Access** and review **Domains**, **Single Sign-On (SSO)**, and any available product sign-in policies.

If a ChatGPT workspace or API Platform organization is linked to the same tenant, its own identity page may be read-only and direct you here. Existing API organization membership, projects, and billing remain in the API Platform.

# Verify a company or school domain

![Admin Console Access page with the Domains tab selected and a verified example.com domain listed for all workspaces and API organizations.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_9GCACNkPJt46Uao1quaRRqaQjv2FWl0v2a4FVnoe9F8/eba04d031bfa28e347747d1674ce47e7/lbas_img_9GCACNkPJt46Uao1quaRRqaQjv2FWl0v2a4FVnoe9F8.png?q=80&fm=webp&w=1344)

![A modal dialog titled “Add a Domain” asks the user to enter an email domain to verify, shows a single text field with the placeholder “yourcompany.com,” and includes Cancel and Add buttons plus a close icon.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_eSpu7lv95tMCkTa37SQj2I19Mqxtbl7zJUFKLkXO0o8/53f4ba24b2d35ea133a76c634056c58b/lbas_img_eSpu7lv95tMCkTa37SQj2I19Mqxtbl7zJUFKLkXO0o8.png?q=80&fm=webp&w=910)

**Domain verification can affect sign-in, existing personal or API accounts, account migration, and email changes. Review the people and products that use the domain before continuing.**

1. Under **Domains**, select the add (+) button.
2. Enter an email domain your company or school controls.
3. Copy the DNS TXT record shown in the setup flow.
4. Add that TXT record to the domain’s public DNS configuration.
5. Return to Admin Console and select **Check Domain**.
6. Confirm that the domain status is **Verified**.

DNS changes can take up to 24 hours to become publicly visible. After the TXT record appears, return to Admin Console and select **Check Domain**. The setup flow allows up to 7 days to complete verification and supports up to 99 verified domains where that limit applies. If another tenant has already verified the domain, contact your OpenAI account team or Support before changing the existing setup.

For domain verification and product eligibility, see: [Verifying your domain for OpenAI identity](https://help.openai.com/articles/8871611).

# Connect your identity provider

![Admin Console Access page with the Single Sign-On (SSO) tab selected, no identity provider connected, and a Set up SSO button.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_TX_9hxX8QD60IF6M39_qweSaoqu303lRZzEjE11NWfI/b47c674f1b3fa17ef1e5411b43d89ae2/lbas_img_TX_9hxX8QD60IF6M39_qweSaoqu303lRZzEjE11NWfI.png?q=80&fm=webp&w=1344)

1. Under **Single Sign-On (SSO)**, select **Set up SSO**.
2. Choose one of the providers shown, such as **Okta**, **Entra**, or **Custom SAML** when available.
3. If your provider is not listed, select **Custom SAML** when offered; an existing configuration may also offer **Custom OIDC**.
4. Follow the setup flow to create or connect the application in your identity provider.
5. Copy the SSO URL, audience or entity identifier, and other requested values into the identity-provider application.

Provider-specific screens differ. Use the values shown for your actual tenant and connection; do not reuse setup values from another workspace or API organization.

The number of identity-provider connections you can add depends on your tenant’s enabled features and administrator permissions.

**An identity-provider app tile or bookmark must use the connection-specific sign-in URL for its product. ChatGPT and API Platform can use different URLs; update the tile or bookmark if its connection changes.**

**Resetting or replacing an existing connection can change SSO URLs, audience values, certificates, and saved sign-in bookmarks. Update the identity-provider application and user instructions before replacing a working connection.**

# Configure identity-provider metadata

![SSO setup step 5 with Manual configuration selected for entering identity provider metadata](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2bbe3eb8463d99fc1534f9f4/5f8227f5f6f2fa4998d0cb4414e814aa/Screenshot-2B2025-04-07-2Bat-2B9_45_28-E2-80-AFAM.png?q=80&fm=webp&w=1344)

## Use dynamic configuration

When your identity provider offers a metadata URL, enter that URL in the setup flow. The provider’s metadata supplies the supported issuer, sign-in endpoint, and signing-certificate details.

## Use manual configuration

If a metadata URL is not available, enter the identity-provider SSO URL, issuer, and X.509 signing certificate shown in your provider’s configuration. Confirm that the certificate matches the one used to sign the SAML response.

# Map user identity attributes

Configure your identity provider to return one stable primary email address for each person. First and last name are optional but recommended when your provider supports them.

* **Email address:** Required. It must identify the same OpenAI account the person uses for product access.
* **First name:** Optional but recommended.
* **Last name:** Optional but recommended.

**OpenAI does not decrypt encrypted SAML responses or assertions. Send an unencrypted SAML response and assertion signed with the expected X.509 certificate.**

## Use the correct account email

If your identity provider returns an alias, a different email, or more than one email claim, OpenAI may match the wrong account. That can make an existing account, chat history, or workspace appear missing.

For Microsoft Entra ID, check whether the sign-in claim uses the person’s email address, user principal name (UPN), or preferred\_username. Configure the SSO and SCIM mappings to identify the intended existing OpenAI account. If the destination email already belongs to another account, stop and contact OpenAI Support before making changes.

## Coordinate managed email changes

Changing an identity-provider email claim does not automatically update an existing OpenAI account. Tenant-wide SCIM cannot change the email address on an existing OpenAI account. If your company or school uses an eligible ChatGPT workspace-level SCIM connection, ask your administrator whether that connection supports updating the existing account before changing the sign-in claim.

# Assign users and confirm product access

1. Assign the intended people or groups to the OpenAI application in your identity provider.
2. Confirm that each person also has the right ChatGPT workspace invitation, API organization membership, or Ads account role.
3. If your tenant uses SCIM, verify the synchronized group and its supported product assignment.
4. Test a user who belongs to the product or workspace you are configuring.

An identity-provider assignment may be required for authentication, but it does not invite that person to every workspace, assign an API role, or grant access to an advertising account.

# Choose a sign-in policy for each product

![Screenshot of an OpenAI configuration page showing SSO settings for ChatGPT, API, Ads, and the Admin portal. A policy dropdown is open with options Required, Optional, and Off, with Optional selected.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_P8MqzU1gSBKLbL73dR8pQr7wujZGzmiuYEX_CfVyjWY/908ac46eced6d84e37c23d93f87c9045/lbas_img_P8MqzU1gSBKLbL73dR8pQr7wujZGzmiuYEX_CfVyjWY.png?q=80&fm=webp&w=1344)

After the shared identity-provider connection is active, review the policy for each product that appears in Admin Console. An available product may offer **Required**, **Optional**, or **Off**.

| **Product** | **How the policy applies** | **What to check** |
| --- | --- | --- |
| ChatGPT | A product-wide policy can apply to ChatGPT workspaces. Where supported, individual workspaces can have their own policy. | Verify the intended workspace, member invitation, and workspace-specific setting. |
| API Platform | The API Platform sign-in policy applies to linked API organizations. If **Customize by API Org** is available, an authorized global admin can set API-organization-specific policies. | Verify API organization membership and the API organization selected in the API Platform. |
| Ads Manager | Ads has its own product sign-in policy. | Verify that Ads SSO is enabled as intended and that the person also has the correct advertising-account role. |
| Admin Console | Admin Console has its own sign-in policy. | Protect access for at least one authorized global admin before requiring SSO. |

**Turning on the shared connection does not automatically enable SSO for every product. If a product’s policy is Off, users cannot use SSO for that product. Users also need the correct identity-provider assignment and product membership.**

For ChatGPT configurations, **Required** SSO applies to members whose email address uses a verified domain covered by the workspace policy. Invited members from other domains may still use another permitted sign-in method. If every member must use company SSO, ask your account team which controls are available. Turning off **Allow External Domain Invites** limits new invitations; it does not remove existing guests or invitations already sent.

Changing a ChatGPT policy to **Required** or **Off** can sign out affected users. Review workspace overrides and communicate the change before applying a broad policy.

# Test the connection and apply the correct policy

![OpenAI Single Sign-On test succeeded confirmation page](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-950428c8f7f006e93886fe21/c3abde951cff2f07dc51c77193d17c72/test_connection.png?q=80&fm=webp&w=1344)

1. Select **Test Single Sign-On** or the equivalent test step shown in the setup flow.
2. Authenticate with the intended identity provider in a private browser window.
3. Confirm that the user reaches the correct ChatGPT workspace, API organization, or Ads account.
4. Verify the required invitation, membership, or account role.
5. Review the applicable product or workspace sign-in policy.
6. Change the policy to **Required** only after successful testing and an approved administrator recovery plan.

# Resolve sign-in or access problems

If someone cannot sign in, check the verified domain, identity-provider assignment, email claim, X.509 certificate, product membership, and applicable product sign-in policy. A successful tenant sign-in does not guarantee access to a specific workspace, API organization, or Ads account.

For product-specific errors and recovery steps, see: [Troubleshooting SSO, workspace access, and domain verification](https://help.openai.com/articles/10489721). If you cannot restore administrator access, contact [OpenAI Support](https://help.openai.com/articles/6614161).
