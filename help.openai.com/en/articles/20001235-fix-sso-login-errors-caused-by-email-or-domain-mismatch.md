<!-- source: https://help.openai.com/en/articles/20001235-fix-sso-login-errors-caused-by-email-or-domain-mismatch -->

# Fix SSO login errors caused by email or domain mismatch

This article proposes troubleshooting for errors "SSO mismatch user creation" / "sso\_mismatch\_user\_creation" when a User is trying to accept an invite to a ChatGPT workspace / API Org

Updated: 2 days ago

### Overview

If a user cannot sign in with SSO after being invited to a ChatGPT workspace, the issue may be caused by a mismatch between the email address invited to the workspace and the email address returned by your identity provider.  
  
This issue may appear with an error such as:  
  
"SSO mismatch user creation"  
  
or:  
  
"sso\_mismatch\_user\_creation"  
  
For SSO sign-in to work both of the following conditions should be met:

1. The user’s identity provider must return an email address that matches the user’s intended ChatGPT workspace identity.
2. The email domain must also be verified and available for the workspace in your Global Admin Console.

### Steps To Resolve

The steps below will help you check whether you have a misalignment between the invite, SSO email claim, and verified domain.

1. **Confirm the email address used for the workspace invite:** Make sure the user was invited with the email address they are expected to use for ChatGPT.
2. **Confirm the email address returned by your identity provider:** Check your SAML/OIDC configuration and confirm which email address field is sent to ChatGPT during SSO. For SAML, review the email-related attributes as email is the key which ChatGPT uses to map the signing in User to the invite or account on ChatGPT. These values should consistently identify the same user email.

\*For example, if the user was invited as user@company.com, but your identity provider returns user@subsidiary.com, we will treat this as a sign in for user@subsidiary.com and will throw the error.  
  
\*You have 2 options here:

1. **Confirm the Users Domain is verified in Global Admin Console and is mapped to the workspace the User is invited to:** If your identity provider returns an email address from a different domain, that domain must be verified in your Global Admin Console and available to the workspace the user is trying to access.

*For example, if the user was invited as user@company.com, but your identity provider returns user@subsidiary.com, then subsidiary.com must also be verified and mapped appropriately before the user can sign in with SSO using that identity.*

> Fastest workaround: *If SSO is optional for your workspace,* have the user accept the invite using username and password instead of SSO, so they are quickly unblocked. This will afford you some time to troubleshoot the SSO login and the User can already use their ChatGPT account.
