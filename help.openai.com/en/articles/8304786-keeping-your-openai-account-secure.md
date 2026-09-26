<!-- source: https://help.openai.com/en/articles/8304786-keeping-your-openai-account-secure -->

# Keeping your OpenAI account secure

Protect your account, review security activity, and respond to suspected unauthorized access.

Updated: 4 hours ago

# Overview

Use this guide to protect your OpenAI account, review security activity, and manage active sessions. If you use the OpenAI API, follow the API key guidance to protect your keys and monitor usage.

If you think your account or API key has been compromised, go to [Respond to a suspected compromise](#respond-to-a-suspected-compromise) and contact OpenAI Support right away.

# Keep your account secure

Start with your sign-in credentials and security settings. These steps can help reduce the risk of unauthorized account access.

## Use strong, unique sign-in credentials

If you use a password, use a unique password that you do not reuse on other sites. We recommend using a password manager to generate and store passwords.

Change your password right away if you think it was exposed, reused, or shared.

## Enable multi-factor authentication (MFA)

Enable multi-factor authentication (MFA) to add another verification step during sign-in. For more information, see: [Enabling or disabling multi-factor authentication (MFA)](https://help.openai.com/articles/7967234).

Even if someone gets your password, they would still need the second factor to access your account.

Enabling MFA does not cancel existing logins. If you suspect unauthorized access, change your password if you use one and log out of all sessions before enabling MFA.

If you want hardware-backed account protection and do not already have a security key, eligible OpenAI users can learn about the OpenAI + Yubico YubiKey bundle. To learn more, see: [OpenAI + Yubico YubiKey bundle](https://help.openai.com/articles/20001269).

## Use Advanced Account Security

For eligible consumer ChatGPT accounts, Advanced Account Security adds stronger sign-in requirements and stricter account safeguards. For more information, see: [Advanced Account Security](https://help.openai.com/articles/20001221). It is not available for ChatGPT Enterprise users, enterprise-managed accounts, or accounts associated with an enterprise-managed domain.

## Be cautious with emails and links

Be cautious with emails that ask for credentials or direct users to web pages that require account details.

Always double-check the email address and URL to make sure they are from a trusted source.

# Review account activity and manage sessions

Security history shows past security events. Use **Active sessions** to review and manage current sessions.

## Review your security history

Security history shows recent security events for your OpenAI account. Examples include sign-ins, sign-outs, password changes, and changes to multi-factor authentication (MFA), passkeys, and other security settings.

To open your security history on the web:

1. In ChatGPT, go to **Settings**.
2. Select **Security and login**.
3. Select **Security history**.

Review the event type and time alongside the location and device details. Some details may be approximate or unavailable.

If you see activity you didn’t perform or authorize, follow the steps in [Respond to a suspected compromise](#respond-to-a-suspected-compromise).

## Log out of all sessions

You can log out of all active sessions across devices. To review and manage individual sessions, see: [Managing active sessions in ChatGPT](https://help.openai.com/articles/20001257).

In ChatGPT on the web:

1. Go to **Settings**.
2. Select **Security and login**.
3. Select **Active sessions**.
4. Find **Log out of all sessions**.
5. Select **Log out all**.
6. In the confirmation modal, select **Log out of all devices**.

This logs you out of all active sessions across devices, including your current session. It may take up to 30 minutes for other ChatGPT sessions to be logged out.

On Platform, go to **Your Profile > Security** and select **Log out of all devices**.

# Protect your API keys

If you use the OpenAI API, protect your API keys as well as your sign-in credentials. An exposed API key can allow unauthorized API usage through your account, which can result in charges or activity that violates our terms of service.

## Use environment variables

Store your API key in environment variables within your development environment. This helps keep the key out of application code and reduces the risk of exposure.

If you use GitHub Actions, use [GitHub secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to store your API key.

## Do not ship your API key

Do not embed your API key directly in an application, such as a mobile app. This makes the key vulnerable to exposure and misuse.

## Be cautious with third-party products

Use caution with third-party libraries, frameworks, and tools that request access to your API key. Even if a product seems reputable, there is still a risk of key exposure or misuse.

Before using a third-party product that requires your API key, review the company and the product carefully. Check reviews, read the privacy policy, and look for any security concerns raised by the community.

## Review code before publishing

Before pushing code to public repositories, review it to make sure no sensitive information, such as API keys, is exposed.

Use automated scanning tools that can flag potential leaks. You can also review [GitHub's secret scanning tutorial](https://docs.github.com/en/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories) for more guidance.

When OpenAI detects an API key on the public internet, or leaked inside an app in an app store, the API key is disabled immediately.

## Rotate your API keys

Periodically change your API keys by deleting old keys and creating new ones through the [API key dashboard](https://platform.openai.com/account/api-keys).

## Monitor API spending and usage

Set multiple spend thresholds, such as 90% and 95%, against a monthly budget at the organization or project level to monitor monthly spend.

Configure custom email recipients to integrate with mailing lists, incident management platforms, and messaging platforms. This can be configured in Platform settings.

You can also enforce an organization or project hard limit to stop affected API requests when tracked spend reaches that amount. Enforcement is not instantaneous, so recorded spend may slightly exceed the limit. For more information, see: [Spend limits](https://developers.openai.com/api/docs/guides/spend-limits).

Use separate API keys for each feature, team, product, or project to make usage easier to track. For more information, see: [tracking usage by API key](https://platform.openai.com/api-keys).

# Respond to a suspected compromise

Act quickly if you suspect unauthorized account access or an exposed API key. Follow the steps that match your situation.

## Secure your account after suspected unauthorized access

1. If you use a password and think it was exposed, reused, or shared, change it right away.
2. [Log out of all sessions](#log-out-of-all-sessions) using the instructions above.
3. If you use the OpenAI API, delete your API keys and review your API usage for unexpected activity.
4. [Review your security history](#review-your-security-history) for unfamiliar activity. Keep details that may help with account recovery.
5. [Contact OpenAI Support](#contact-openai-support).

## Revoke an exposed API key

If you think an API key has been compromised:

1. Delete the affected key through the [API key dashboard](https://platform.openai.com/account/api-keys).
2. Review your API usage for unexpected activity and keep the details.
3. [Contact OpenAI Support](#contact-openai-support).

## Contact OpenAI Support

Contact OpenAI Support by opening a new chat on any Help Center page. Include details of activity you didn’t perform or authorize. These details can help with account recovery.

## Was this article helpful?
