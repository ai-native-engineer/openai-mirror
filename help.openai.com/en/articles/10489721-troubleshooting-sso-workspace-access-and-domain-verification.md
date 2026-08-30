<!-- source: https://help.openai.com/en/articles/10489721-troubleshooting-sso-workspace-access-and-domain-verification -->

# Troubleshooting SSO, workspace access, and domain verification

Fix missing workspaces, SSO sign-in failures, identity-provider mismatches, and domain-verification errors.

If you can sign in but cannot find your company’s workspace, first confirm the email address on your invitation and ask a workspace admin to check your membership. If sign-in fails, find the section that matches the message you see.

If the problem began after a previously working sign-in, check [OpenAI Status](https://status.openai.com/) before changing your identity-provider or network configuration.

# Check your account and find a missing workspace

1. Confirm that you are using the intended OpenAI account and email address.
2. Select the correct OpenAI tenant, ChatGPT workspace, or API Platform organization.
3. Check that you have the product-specific invitation, membership, or administrator role required for that resource.
4. Use the sign-in method required by the resource: password, supported social sign-in, or your tenant’s SSO connection.
5. If more than one API identity-provider option appears, select the connection specified by your API organization administrator.

If a workspace is missing, ask its owner or admin to confirm your invitation and membership before changing DNS, SSO, or identity-provider settings. Admin Console and an individual workspace can require different sign-in methods.

# Resolve domain verification problems

## The domain is already verified elsewhere

A domain may already be verified for another tenant. Ask your company’s or institution’s IT administrator to confirm which tenant has the domain. Contact OpenAI Support or your account team before attempting to move or reuse it.

Do not remove a domain from a working tenant, create a second tenant, or reverify it just to resolve a conflict. If your DNS record is correct but setup directs you to contact Support, or if two tenants need the same domain, ask OpenAI Support or your account team before changing existing access.

## A subdomain is not recognized

Verifying a parent domain does not automatically verify every subdomain. Verify the exact domain or subdomain used by the affected account when your configuration requires it.

## Your company or school cannot add a DNS TXT record

OpenAI must be able to read the required TXT record through a public DNS lookup. If security policy prevents you from adding that record, ask your OpenAI account team whether another verification path is available for your specific situation.

## The DNS TXT record is visible, but verification fails

DNS changes can take up to 24 hours to appear publicly. Confirm the exact domain, record name, and complete TXT value. If verification still fails, contact your OpenAI account team or OpenAI Support before changing the domain or creating another tenant.

## The verification attempt shows Expired

A completed domain verification does not expire. An **Expired** setup status means the 7-day verification window ended before the TXT record was confirmed. Start the verification again, add the required record, and complete the check within the new setup window.

For the full process, see: [Verifying your domain for OpenAI identity](https://help.openai.com/articles/8871611).

# Find or confirm the relevant identity settings

## An expected workspace or tenant is missing

* Confirm that you selected the intended OpenAI tenant.
* Check whether the task requires a global admin, a ChatGPT Business workspace owner, or an API organization owner. For Business workspace identity settings, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188).
* Confirm that the workspace or API organization is associated with the expected tenant.
* Retry using the sign-in method required by the missing resource.

If the resource is still missing, ask your account team or OpenAI Support to verify its association. Do not delete or recreate the user account, workspace, or tenant.

The tenant-level **Users** list can differ from a workspace’s **Members** list. If counts do not match, select the correct tenant, open the expected workspace, and check the role associated with your account. If Admin Console may be using an old session, sign out and try again in a private browser window.

## The API Platform Identity page is unavailable

The API Platform Identity page is available only for eligible API organizations and authorized administrators. Confirm that the API organization has a supported Custom or Unlimited billing plan, or another specifically supported configuration, and that you have the required API organization role.

API organization administration remains in the API Platform. Access to Admin Console or to a ChatGPT workspace does not automatically grant access to an API organization’s settings.

## The wrong identity provider is selected

Eligible API Platform configurations can support multiple provider connections. ChatGPT workspaces do not generally support multiple identity providers. Confirm that the user selected the connection assigned to the intended product and verified domain.

# Check SSO policies and identity-provider mapping

## A workspace requires SSO

**Required** workspace SSO applies to members whose email address matches a verified domain covered by its sign-in policy. Invited users from other domains may still use another permitted sign-in method. If every member must use SSO, ask your account team which controls are available. Turning off **Allow External Domain Invites** blocks new external invitations but does not affect existing members or invitations already sent.

If the workspace requires SSO, sign out and start again using the tenant’s identity-provider connection. Do not assume that an existing Admin Console session satisfies the workspace’s SSO policy.

## The email or domain does not match

A mismatch can appear as “SSO mismatch user creation” or **sso\_mismatch\_user\_creation**. It means the invited account, identity-provider response, verified domain, or assigned SSO connection does not line up.

1. Ask the workspace or tenant administrator which email address received the invitation.
2. Ask the identity-provider administrator which email address is returned in the SAML or OpenID Connect (OIDC) response.
3. Compare the full addresses, including aliases, subsidiary domains, and subdomains.
4. Confirm that the returned domain is verified and available to the intended tenant or workspace.
5. Check that the user is assigned to the correct identity-provider application, connection, and product resource.
6. Correct the identity-provider mapping or use the approved invitation process for the intended address.

For example, an invitation sent to user@company.com does not match an identity-provider response for user@subsidiary.com. A verified domain still fails if the user signs in through a different SSO connection or does not have the required product membership.

If a work email address recently changed, first confirm whether the account is managed through tenant-wide SCIM or an eligible ChatGPT workspace-level SCIM connection. Tenant-wide SCIM cannot update the account email; changing the identity-provider claim alone does not resolve the mismatch.

**Do not delete the existing account, create an unapproved replacement account, or bypass required SSO. Use another sign-in method only when the applicable product policy explicitly permits it.**

## Microsoft Entra ID sends the wrong account email

In Microsoft Entra ID, the email address, user principal name (UPN), and preferred\_username may not match. Ask the identity-provider admin which value is sent to OpenAI and confirm that SAML and SCIM identify the intended existing account.

Before changing a managed email, check whether the new address already belongs to another OpenAI account. If it does, stop and contact OpenAI Support. Do not delete either account, clear authentication profiles, or create a replacement user.

## A tenant-managed email address changed

Verifying a company or school domain can restrict self-service account-email changes. Tenant-wide SCIM cannot change the email address on an existing OpenAI account, and OpenAI Support cannot make that change manually. If your company or school uses an eligible ChatGPT workspace-level SCIM connection, ask your administrator whether the existing user’s email can be updated through that connection.

**Changing the SAML or OIDC email claim without coordinating the existing OpenAI account can create a separate account and leave existing projects, agents, and conversation history attached to the original account. Do not delete the original account, clear authentication profiles, or create a replacement account. Contact OpenAI Support before making changes.**

## A user’s name is missing or incorrect

If a new user is asked to enter a name and birthday, or their email address appears as their display name, review the provider’s attribute mapping.

* Confirm that the SAML response includes the expected first-name and last-name attributes.
* Confirm that the email claim identifies the correct existing account.
* Check that the SAML response and assertion are not encrypted.

# Resolve common sign-in and workspace issues

## A password reset email does not arrive

If the account was created through an identity provider or social sign-in method such as Google, Microsoft, or Apple, there may be no OpenAI password to reset. Sign in using the original method or reset the credentials with the appropriate provider.

If the account uses an email address and password:

1. Confirm that you entered the correct account email address.
2. Check the spam or junk folder.
3. Request another password reset email.

For more detail, see: [Changing your OpenAI account sign-in method](https://help.openai.com/articles/4936824).

## A workspace is missing from the workspace switcher

Sign out, sign in again with the correct account, and use the SSO method required by the missing workspace. Confirm that the user has an active invitation or membership and that the workspace belongs to the expected tenant.

## You see Workspace not found

Check the selected workspace, your assigned role, and the workspace’s required authentication method. If the resource is still unavailable, ask the account team or OpenAI Support to verify the workspace association.

# Match the error message to the next action

## Your identity provider signed you in with an email that is not in the workspace

The SSO connection returned an account that does not have membership in the intended ChatGPT workspace.

* If the email is correct, ask a workspace administrator to invite it.
* If the email is wrong, ask IT to correct the identity-provider email mapping.
* If an existing OpenAI account needs account-specific remediation, contact OpenAI Support.

## sso\_mismatch\_user\_creation

Compare the invitation address with the identity-provider email claim, verified domain, assigned SSO connection, and product membership. Use the mismatch steps in the previous section.

## identity\_provider\_mismatch

This error means the sign-in method does not match the method associated with the account. Retry using the original method, such as Google, Microsoft, Apple, a password, a temporary code, or the tenant’s SSO connection.

If you no longer have access to the original method, contact OpenAI Support for the verified account-recovery path.

## No eligible ChatGPT account found (chatgpt\_account\_missing)

Automatic account creation does not reactivate a removed or deactivated membership. A workspace owner or admin must confirm the person is authorized and invite them again.

SSO can succeed even when the expected ChatGPT workspace invitation, membership, or SCIM assignment is missing. Ask an administrator to confirm the exact email, identity-provider application assignment, pending invitation or active membership, and latest SCIM sync. If those records disagree or the account email recently changed, contact OpenAI Support. Do not delete or recreate the account.

## enterprise\_sso\_login\_unavailable

This error can appear when your OpenAI account can sign in only through one tenant’s SSO, but the API organization or product you selected cannot use that connection. This can affect a personal API organization, an API organization outside the same tenant, or a product where SSO is unavailable.

Confirm the tenant and product you are trying to open. Use a sign-in method already linked to your account and permitted for that product. If no permitted method is available, contact OpenAI Support. Your ChatGPT workspace admin may not manage the API organization. Do not delete authentication profiles, create a replacement account, or bypass an SSO policy.

## require\_sso\_login

The selected workspace requires SSO, but the sign-in attempt used another method.

1. Sign out of ChatGPT.
2. Enter your account email address on the sign-in page.
3. Select the tenant’s SSO option and authenticate with the configured identity provider.

## invalid\_state

If this error appears after identity-provider sign-in or multi-factor authentication (MFA), open a new private browser session and try the approved sign-in flow again. If it continues, ask your administrator to check your identity-provider application assignment, workspace invitation or membership, and SCIM group assignment or sync status. Retry SSO once those records are correct. If the problem continues, contact OpenAI Support with the approximate time and any request ID. Do not remove existing sign-in methods or authentication profiles.

## Something went wrong while getting your SSO info

A VPN, proxy, browser extension, firewall, or other network control may be blocking an authentication request. Ask your IT team to verify the network path and allow the required OpenAI domains.

If the tenant provides an identity-provider sign-in tile, try it to determine whether the issue affects only the standard sign-in path. For network guidance, see: [Troubleshooting ChatGPT network, firewall, and managed-device access](https://help.openai.com/articles/9247338).

## No accessible workspaces

This can happen when the email returned by the identity provider changed while an older authentication profile or workspace membership still refers to the previous address. Ask IT to confirm the email claim, tenant, and workspace assignments.

If those values are correct and the error continues, contact OpenAI Support for account-mapping assistance.

## Invalid thumbprint

The identity provider’s current X.509 signing certificate may not match the certificate configured in OpenAI.

1. Identify the certificate the identity provider uses to sign the SAML response.
2. Compare it with the certificate configured on the OpenAI **Identity** page.
3. Update the configured certificate if the provider has rotated or replaced it.

## Oops! Please use your organization’s SSO to access your account

The workspace requires SSO, but the user attempted to sign in with a password or social sign-in provider.

1. Return to the sign-in page and enter the account email address.
2. Select the tenant’s SSO option.
3. If the error appears again after identity-provider authentication, ask IT to confirm that the user belongs to the provider’s OpenAI access group.

## The connection is not enabled

The selected identity-provider tile or connection may not be active for the intended product. Confirm that the tenant’s active ChatGPT or API Platform connection matches the tile URL, then ask OpenAI Support for help if the expected connection cannot be enabled.

If the error appears only in the ChatGPT mobile app, update the app and try again.

## The sts.windows.net page cannot be found

Review the Microsoft Entra ID or related identity-provider schema mapping and SSO sign-in URL. Replace outdated or incorrect values with the current values shown in the provider and OpenAI setup flows.

# Get help with SCIM provisioning

If users can authenticate but are not provisioned or assigned correctly, review the product-specific directory configuration, identity-provider group assignments, and workspace or API organization membership.

For directory-sync setup and troubleshooting, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

# Collect safe troubleshooting details

* The exact error message and, when appropriate, a screenshot.
* The affected account email address and sign-in method.
* The product, workspace, API organization, and relevant administrator role.
* Whether one person or multiple users are affected.
* The date and time of the issue, including time zone.
* The browser, application version, operating system, and device.
* The identity provider and whether the issue occurs through standard sign-in, an identity-provider tile, or both.
* The troubleshooting steps already completed.

**Do not share passwords, one-time verification codes, private keys, raw SAML assertions, or other authentication secrets.**

Use the verified Support contact flow described in [How to contact OpenAI Support](https://help.openai.com/articles/6614161).
