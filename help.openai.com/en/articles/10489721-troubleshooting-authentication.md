<!-- source: https://help.openai.com/en/articles/10489721-troubleshooting-authentication -->

# Troubleshooting authentication

Resolve common issues with domain verification, SSO, SCIM, workspace access, and sign-in errors.

Updated: 2 days ago

# Overview

Use this guide to resolve common authentication issues for ChatGPT and the API Platform. It covers domain verification, System for Cross-domain Identity Management (SCIM), single sign-on (SSO), identity provider (IdP) configuration, and sign-in errors.  
  
If authentication worked previously and the issue began recently, check [OpenAI Status](https://status.openai.com/) for an active incident before changing your configuration.  
  
Start with the issue or error message that matches what you see. Keep the exact error message available if you need to contact OpenAI Support.

# Domain verification

Domain verification confirms that your organization controls a domain. For setup instructions, see [Domain Verification](https://help.openai.com/articles/8871611).

## Use the same domain across multiple OpenAI organizations

A domain can be verified in only one OpenAI Admin Portal. If you need to use the same domain with an organization or workspace that is not in that Admin Portal, contact OpenAI Support.

## Verify a parent domain and its subdomains

Verifying a parent domain does not verify its subdomains. Verify each subdomain separately.

## Verify a domain when TXT records are not permitted

OpenAI must be able to read the required TXT record through a public DNS lookup. If your organization's security policy prevents you from adding the record, contact your OpenAI account team to discuss whether manual verification is available for your situation.

## Resolve an expired domain verification attempt

A completed domain verification does not expire. The **Expired** status means the 7-day setup period ended before verification was completed. Start domain verification again, add the required TXT record, and complete the verification check within 7 days.

# SCIM resources

Use the article that matches the product you manage:

* For ChatGPT setup and provisioning guidance, see [OpenAI ChatGPT SCIM Integration FAQ](https://help.openai.com/articles/9627404).
* For cross-product SCIM questions and troubleshooting, see [SCIM Integration FAQ](https://help.openai.com/articles/10011769).

# SSO and identity provider configuration

For an explanation of how authentication settings are shared between ChatGPT and the API Platform, see [SSO Overview](https://help.openai.com/articles/10468051). For complete setup instructions, see [Configuring SSO](https://help.openai.com/articles/9534785).

## Access SSO settings for ChatGPT and API Platform

Use [OpenAI Identity](https://admin.openai.com/identity) in the Global Admin Console to manage SSO for ChatGPT workspaces and API Platform organizations. If an expected workspace or organization is not listed, contact OpenAI Support to confirm that it is connected to the Admin Portal and that you have the required admin access.

## Access the Identity page in API Platform

The **Identity** page is available to API Platform admins for Enterprise Platform organizations with a **Custom** or **Unlimited** billing plan. Confirm your organization's billing plan. If the page is still unavailable, contact your OpenAI account team.

## Configure identity providers

A single organization ID supports one IdP configuration. A ChatGPT workspace and its corresponding API Platform organization share the same organization ID and IdP configuration.

## Understand Enforce SSO for ChatGPT

**Enforce SSO** applies when all of the following are true:

* The user is accessing the ChatGPT workspace where SSO is enforced.
* The user's sign-in email matches a verified domain.
* The workspace requires SSO for that domain.

Users whose email domains are not verified can continue to use non-SSO sign-in methods, such as a password or social sign-in. This allows guest access without requiring the guest's domain to use your SSO configuration.  
  
API Platform SSO is domain-based. For more information about product-specific behavior, see [SSO Overview](https://help.openai.com/articles/10468051).

# Sign-in and workspace issues

## A password reset email does not arrive

If the account was created with SSO or a social sign-in method such as Google, Microsoft, or Apple, it does not have an OpenAI password to reset. Sign in using the original method. If necessary, reset your credentials through your identity provider.  
  
If the account was created with an email address and password:

1. Confirm that you entered the email address associated with the account.
2. Check the spam or junk folder.
3. Request another password reset email.

For more information, see [Can I Change How I Log Into My Account (Authentication Method)?](https://help.openai.com/articles/4936824).

## A workspace is missing from the workspace switcher

Sign out of ChatGPT, then sign in again. If the missing workspace requires SSO, use its SSO sign-in option. If it does not require SSO, use the same non-SSO method that you normally use for the account.

## A user's name is missing or incorrect

If new users are prompted to enter their name and birthday, or their email address appears as their display name, OpenAI may not be receiving valid name attributes in the SAML response.  
  
Review the IdP attribute mapping and confirm that:

* The response includes valid first-name and last-name attributes.
* The SAML response and assertion are not encrypted.

# Resolve specific error messages

## The signed-in email is not in the ChatGPT workspace

**Your Identity Provider signed you in as {email}, but that email has not been added to your ChatGPT workspace.**  
  
The SSO configuration returned an account that is not a member of the ChatGPT workspace.

* If the email address is correct, ask a workspace admin to invite it to the workspace.
* If the email address is incorrect, ask your IT admin to correct the email mapping in the IdP.
* If the correct email must be associated with an existing OpenAI account, contact OpenAI Support for account-specific guidance.

## Error: identity\_provider\_mismatch

**You tried signing in as user@example.com using a password, which is not the authentication method you used during sign up. Try again using the authentication method you used during sign up. (error=identity\_provider\_mismatch)**  
  
The sign-in method does not match the method originally used for the account. Try again with the original method, such as a password, a temporary code, Google, Microsoft, Apple, or your organization's SSO.  
  
If you no longer have access to the original sign-in method, or you need to use a password to access another workspace, contact OpenAI Support.

## Error: require\_sso\_login

The workspace requires SSO, but the sign-in attempt used a social sign-in method or password.

1. Sign out of ChatGPT.
2. On the sign-in page, enter your email address.
3. Select the SSO option, then authenticate with your organization's IdP.

## Error: Something went wrong while getting your SSO info

This message can appear while OpenAI checks whether an account belongs to an Enterprise workspace. It may indicate that a VPN, proxy, browser extension, firewall, or other network control is blocking an authentication request.  
  
Ask your IT team to check the network path and confirm that required OpenAI domains are allowed. For current allowlist guidance, see [Network recommendations for ChatGPT errors on web and apps](https://help.openai.com/articles/9247338).  
  
If your organization uses an IdP **Tile URL**, try that URL to determine whether the standard sign-in path is the source of the issue.

## Error: No accessible workspaces

This message can appear when the email address returned by the IdP has changed but the OpenAI account is still associated with the previous SAML profile.  
  
Ask your IT admin to confirm the email address returned by the IdP. If the email is correct and the error continues, contact OpenAI Support for help resolving the account mapping.

## Error: Invalid thumbprint

This message usually indicates that the X.509 certificate configured in OpenAI does not match the certificate in the SAML response.

1. Confirm which certificate the IdP uses to sign the SAML response.
2. Compare it with the certificate uploaded on the **Identity** page.
3. Upload the current certificate if needed.

## Error: Oops! Please use your organization's SSO to access your account.

This message appears when SSO is enforced but the sign-in attempt used another method, such as Google, Microsoft, Apple, or a password.

1. Return to the sign-in page.
2. Enter your email address, then select the SSO option.
3. If the message appears again after IdP authentication, ask your IT team to confirm that you are in the IdP access group for OpenAI.

## Error: the connection is not enabled

This message usually means that the IdP **Tile URL** is not active for the connection. ChatGPT and API Platform share the same underlying organization ID, and only one of their two Tile URLs is active at a time. The ChatGPT Tile URL is active by default. Contact OpenAI Support if you need to switch to the API Platform Tile URL.  
  
If this error appears only in the ChatGPT mobile app, update the app to the latest version and try again.

## The sts.windows.net page cannot be found

This message may indicate an incorrect schema mapping or SSO sign-in URL in the IdP configuration. Verify both settings and replace any outdated or incorrect URL with the current value shown in your IdP's SSO configuration.

# Still not working?

## Before escalating

Confirm that [OpenAI Status](https://status.openai.com/) does not show an active incident, then collect the following details:

* The exact error message and, when possible, a screenshot.
* The affected account email address and sign-in method.
* Whether the issue affects one user or multiple users.
* The date and time of the issue, including the time zone.
* The browser, app version, operating system, and device.
* The IdP and any relevant workspace or organization ID.
* Whether the issue occurs through direct sign-in, the Tile URL, or both.
* The troubleshooting steps already completed.

Do not share passwords, one-time codes, private keys, or other authentication secrets.

## Contact OpenAI Support

Open the chat bubble at the bottom of [help.openai.com](https://help.openai.com/) to contact OpenAI Support. For guidance on submitting a request, see [How can I contact support?](https://help.openai.com/articles/6614161).
