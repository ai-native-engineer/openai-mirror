<!-- source: https://help.openai.com/en/articles/11489188-sso-for-chatgpt-business-faq -->

# SSO for ChatGPT Business - FAQ

Frequently asked questions about SSO on the ChatGPT Business plan.

Updated: 3 days ago

For a walkthrough on setting up SSO for your ChatGPT Business workspace, please refer to our article: [Configuring SSO for ChatGPT](/en/articles/9534785-configuring-sso-for-chatgpt).

***Note:*** *As of August 29th, 2025, we've renamed ChatGPT Team to ChatGPT Business. For more information and questions related to the name change, please refer to our article:* [*ChatGPT Business Rename FAQ*](/en/articles/12111915)

# General

## What are all of the functional differences between SSO in an Enterprise/Edu plan vs on a Business plan?

Other than Business SSO being self-serve, the functional differences are:

* **No SCIM / AD group sync on the Business plan**, so all user provisioning and de-provisioning is manual.
* **Scope:** Business SSO touches **only ChatGPT**; it does **not** carry over to platform.openai.com. This is different from SSO on Enterprise/Edu, where SSO can optionally span both ChatGPT **and** Platform.
* **Account migration:** Enterprise/Edu forces users on a verified domain to **migrate or delete** matching consumer accounts; Users on the ChatGPT Business plan will have the ability to do account migration at the individual user level, but Business plan workspace admins cannot enforce it.

## Which SSO protocols does ChatGPT Business support?

SAML and OIDC.

## What does IdP / SSO / SP mean?

* **Identity Provider (IdP)**: Refers to the service you use to manage digital identity.
* **Single Sign-On (SSO):** One centralized managed IdP login lets a user access all linked apps without re-entering credentials.
* **Service Provider (SP) – ChatGPT:** The app (i.e. ChatGPT) that trusts the IDPs token and grants the user access.

For details [see our SSO Overview](/en/articles/10468051-sso-overview).

## Where do I set up SSO for my Business workspace?

In your ChatGPT Business workspace settings located at <https://chatgpt.com/admin/identity> be on the Identify & Provisioning tab where you can set up the following for your workspace:

1. [Verified Domains](/en/articles/8871611-domain-verification)
2. [Identity Management](/en/articles/9534785-configuring-sso-for-chatgpt-enterprise)

## How do I set up Directory Sync for SCIM provisioning / de-provisioning for my Business plan workspace?

[Upgrade to ChatGPT Enterprise](https://openai.com/contact-sales/?utm_source=chatgpt-scim-upgrade&utm_medium=identity-page&utm_campaign=scim-upgrade) if you need Directory Sync (SCIM).

## Do I need to verify a domain before I can turn on SSO?

Yes. Domain verification proves you own the email namespace you plan to federate with your identity provider (IdP). SSO setup is disabled until at least one domain is verified.

## Does verifying a domain cost extra?

No, it does not cost extra. Domain Verification is included in every ChatGPT Business subscription.

## Why do I get “Domain already verified by another workspace” when I try to enable SSO?

Business wizard errors when the domain is already owned by an Enterprise (or other Business or other API Platform SSO instance) workspace.  
  
Your company’s IT team can reach out to the OpenAI Sales team via our Contact Sales form to discuss a workspace consolidation. See [How to contact the OpenAI Sales team](/en/articles/9047878-how-can-i-contact-sales).

## Can I invite contractors or external collaborators who don’t exist in my IdP?

Yes, you can allow external domain invites to invite those users and external collaborators to your ChatGPT Business workspace.

## What happens to my SSO settings if I later upgrade this Business workspace to ChatGPT Enterprise?

To upgrade to Enterprise reach out to our OpenAI Sales team via our Contact Sales form. See [How to contact the OpenAI Sales team](/en/articles/9047878-how-can-i-contact-sales).

## What happens if everyone authenticates through SSO and the connection fails—how do we regain access?

In this case there are two options:

1. Business workspace Admin reaches out to our Support team for assistance in disabling SSO. The Admin should have a Password/Social method to login.
2. If you allow external domains, you could implement a *backdoor* admin account with an external domain, so SSO enforcement does not apply to that account. Then use this user (which should auth with Password/Social) to login if you get locked out.

## Can I mix SSO and password logins?

Yes. If your Business workspace uses SSO for ChatGPT only, users who also need to access Platform or Intercom can simply click **Forgot password** to set a regular password and continue signing in with email/password there.

## Which identity providers (IdPs) are supported?

ADP OpenID Connect, Auth0 SAML, CAS SAML, ClassLink SAML, Cloudflare SAML, CyberArk SAML, Duo SAML, Entra ID (Azure AD), Google SAML, JumpCloud SAML, Keycloak SAML, LastPass SAML, Login.gov OpenID Connect, Microsoft AD FS, miniOrange SAML, NetIQ SAML, Okta, OneLogin, Oracle, PingFederate, PingOne, Rippling, Salesforce, Shibboleth Generic SAML, Shibboleth, SimpleSAMLphp SAML, VMware Workspace One.  
  
“Custom SAML” or “Custom OIDC” are both also available for selection in the wizard.

## Does the ChatGPT Business plan allow more than one verified email domain per workspace?

Yes.

## Can a ChatGPT Business plan workspace still in the free trial enable SSO, or is activation blocked until payment is captured?

There is not a free-trial flow for the ChatGPT Business plan today. New workspaces must complete the $1 launch-promo purchase with a payment captured before they can enable SSO.

## Is SSO fully included in the $30 /user/mo ChatGPT Business plan price, or are there any hidden fees (e.g., per-connection charge) we need to disclose?

Yes, there is no separate fee for Business-SSO beyond the base seat price of the Business plan itself. SSO is available at no additional cost.

## How are expiring certs handled?

Currently, the onus for renewing certificates lies with the Business workspace admins and their corresponding IT teams. The OpenAI Support team is available to assist should any action be needed, but the renewal/rotation of the certificate is expected to be performed in the customer's IdP.

## What is the recommended flow if the only workspace owner who configured SSO leaves the company before handing off access?

The current flow blocks the departure: the sole workspace owner must transfer ownership to another member before they can leave.

## If users first log in with password and later via SSO (same email), do their conversations merge automatically or create duplicate accounts?

If the SSO assertion returns the **same** email address, ChatGPT links the sign-in to the existing profile—conversation history stays intact and no duplicate account is created. A new (empty) account is spun up only if the SSO response supplies a **different** email; once that mapping is corrected, the user’s original account (with all history) is still there.

# SSO scenarios and expected behavior

## Org owns both Enterprise & Business workspaces on the same verified domain

When the Business-plan setup wizard checks the domain it will simply say the domain is “already verified.” It doesn’t reveal which workspace (Enterprise or otherwise) owns it—just that someone else has already completed verification.

## Two separate Business workspaces share one domain

Only one Business workspace can own domain verification.  
  
Your company’s IT team can reach out to the OpenAI Sales team via our Contact Sales form to discuss a workspace consolidation. See [How to contact the OpenAI Sales team](/en/articles/9047878-how-can-i-contact-sales).

## ChatGPT SSO enabled while Platform SSO is still off

SSO in ChatGPT and SSO in the API Platform need to be configured in their respective admin portals (ChatGPT and API).

## Business workspace downgrades or cancels while SSO is on

The solution here is that each user would need to forget password to get back in as the only option.

## SCIM-managed users on Enterprise join a Business workspace

This scenario is both possible and supported. SCIM provisions the original invitation to the configured org/workspace. Once the user exists in the OpenAI system, there is nothing preventing the user from being invited to other Business/Enterprise workspaces. This expected behavior will not change with the release of self-serve SSO for Team plans.

## Multi-domain companies (e.g., acme.com and acme-intl.com)

Business workspaces can verify more than one email domain. Add each domain in the same portal and complete verification for each domain you plan to use with SSO.

## Domain already verified on Platform but not on ChatGPT

Your company’s IT team can reach out to the OpenAI Sales team via our Contact Sales form to discuss a workspace consolidation. See [How to contact the OpenAI Sales team](/en/articles/9047878-how-can-i-contact-sales).

## Admin leaves before completing domain verification

Ensure there is another admin/owner of the workspace who can complete domain verification.
