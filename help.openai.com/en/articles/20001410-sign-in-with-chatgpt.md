<!-- source: https://help.openai.com/en/articles/20001410-sign-in-with-chatgpt -->

# Sign in with ChatGPT

Learn how Sign in with ChatGPT lets you use your ChatGPT identity to access supported external applications.

Updated: 2 hours ago

# Overview

Sign in with ChatGPT is an identity-provider sign-in option that lets you use identity information from your ChatGPT account to create or connect an account with a supported external application. When an application offers this option, select **Sign in with ChatGPT** or **Continue with ChatGPT**.  
  
You choose whether to use ChatGPT to sign in. Signing in does not independently give the external application access to your ChatGPT conversations, memory, files, tokens, billing information, or other ChatGPT account data.

# Availability

Sign in with ChatGPT is available globally to authenticated ChatGPT users, including users in Enterprise organizations. It is launching first with OpenAI Academy and Codex Sites. Other supported external applications may offer Sign in with ChatGPT in the future.  
  
Availability for members of an organization also depends on the organization’s admin settings.

# Use Sign in with ChatGPT

1. On a supported application’s sign-in page, select **Sign in with ChatGPT** or **Continue with ChatGPT**.
2. Review the identity information shown in the sign-in flow.
3. Continue only if you want to use your ChatGPT identity to create or connect your account with the external application.

# Information shared with an external application

When you use Sign in with ChatGPT, ChatGPT shares the identity information shown during sign-in, such as your name, email address, and profile picture.  
  
Sign in with ChatGPT does not independently share:

* Your ChatGPT conversations or memory
* Your files or tokens
* Your billing information or other ChatGPT account data

If an external application requests additional access, that request is separate from signing in. Any additional access is limited to the permissions that you or your organization admin approve. Review the permission request before continuing.

# Privacy and data OpenAI collects

When you use Sign in with ChatGPT, OpenAI collects and processes information needed to authenticate you, apply organization settings, complete the authorization, and protect the sign-in flow. Depending on your sign-in method, device, and organization settings, this may include:

* Your OpenAI account information, such as account identifiers, email address, authentication provider, and selected workspace or organization, when applicable
* Details about the external application and authorization, such as the application identifier, requested and approved permissions, authorization decision, and sign-in outcome
* Technical and security information, such as request and session identifiers, IP address, location information inferred from the request, browser or app version, user agent, device identifiers, and security signals

This description of OpenAI’s processing is separate from the information released to the external application. Review the previous section for what the application receives. Any additional application access requires a separate permission flow.

# Manage access for your organization

By default, Sign in with ChatGPT is enabled for organizations that have not set an explicit policy. Existing allow or deny policies, including approved-application lists, remain in effect and are not overwritten.  
  
Global admins can manage Sign in with ChatGPT in the [global admin console](https://help.openai.com/articles/12289294#external-access):

1. Go to **Access**, then select **External Access**.
2. Turn off **Enable Sign in with ChatGPT for your organization** to prevent members from using Sign in with ChatGPT.
3. Turn on **Approved applications** to allow members to use Sign in with ChatGPT only with applications that your organization approves.
4. Use the **Approved** control to manage each application.

These controls manage Sign in with ChatGPT as an identity-provider sign-in option. They do not grant an external application access to ChatGPT account data beyond the identity information and any separate permissions shown to the user.  
  
Learn more about the [global admin console](https://help.openai.com/articles/12289294#external-access).

# If you cannot use Sign in with ChatGPT

If you do not see Sign in with ChatGPT, the external application might not support it, it might not be available to your account yet, or your organization’s admin policy might restrict it. Use another sign-in method offered by the application or contact your organization admin.

## Was this article helpful?
