<!-- source: https://help.openai.com/en/articles/20001257-managing-active-sessions-in-chatgpt -->

# Managing active sessions in ChatGPT

Learn how to review active sessions, log out of individual sessions, and log out of all sessions from ChatGPT security settings.

Updated: 9 days ago

***Note:*** *This feature is not available for accounts linked to an organization’s SSO sign-in, including SAML or OIDC.*

# Overview

Active sessions helps you review recent sessions and trusted devices associated with your OpenAI account from ChatGPT security settings.  
  
A session can represent a signed-in browser session or a first-party OpenAI app session. When available, a session row may show:

* Device or browser information.
* First-party app context, such as ChatGPT, Codex, or API Platform.
* Approximate location.
* Sign-in date and time.
* Whether the device is a trusted device.
* Whether it is your current session.

Session details may be approximate or incomplete. A single browser row can represent sessions across multiple first-party OpenAI products.  
  
Active sessions does not show or manage:

* Third-party app sessions.
* Connected apps.
* Sign in with ChatGPT sessions used only for third-party services.
* Codex CLI sessions.

Active sessions only shows active sessions known through session management. It does not show recently signed-out sessions.

## Availability

The **Active sessions** feature is available across all ChatGPT accounts and workspace types, including personal and managed workspaces.  
  
It is not available for accounts linked to an organization’s SSO sign-in, including SAML or OIDC. This can apply even if your organization does not require SSO for every sign-in, or if you used another sign-in method for your current session.

# Open active sessions

1. In ChatGPT, go to **Settings**.
2. Select **Security**.
3. Select **Active sessions**.

# Review a session

Use the session details to look for devices, locations, or app sessions that you do not recognize.  
  
A row labeled **CURRENT SESSION** is the session you are using now. You cannot log out of the current session from that row. To end your current session, sign out from ChatGPT or use **Log out of all sessions**.

# Log out of a session

1. In **Active sessions**, find the session you want to end.
2. Select **Log out**.
3. In the confirmation modal, select **Log out**.

If the session is a trusted device, the confirmation action may be **Log out and remove**. This logs out the device and removes it from trusted devices.

# Log out of all sessions

1. In **Active sessions**, find **Log out of all sessions**.
2. Select **Log out all**.
3. In the confirmation modal, select **Log out of all devices**.

This logs you out of all active sessions across devices, including your current session. It may take up to 30 minutes.

# When a session has no log out option

A row may not have **Log out** when it is your current session or when session status is unavailable.  
  
If you see **Session status unavailable**, use **Log out of all sessions** if you want to sign out across devices.

# Troubleshoot active sessions

If active sessions cannot load, try again later.  
  
If **Active sessions** does not appear in **Settings** > **Security**, it may not be available for your account. This can happen for accounts linked to an organization’s SSO sign-in.  
  
If a row remains visible after you log it out, wait for normal propagation, refresh **Active sessions**, or use **Log out of all sessions**.  
  
If you suspect unauthorized account activity, change your password if you use one, review your sign-in methods, and contact OpenAI Support.
