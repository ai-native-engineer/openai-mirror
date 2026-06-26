<!-- source: https://help.openai.com/en/articles/8304786-how-can-i-keep-my-openai-accounts-secure -->

# How can I keep my OpenAI accounts secure?

Protect your account from fraud with these best practices.

Updated: 3 days ago

Contact OpenAI Support right away if you are concerned that your account or API key has been compromised. You can reach out to OpenAI Support by opening a new chat in the bottom-right corner of any Help Center page.

# Overview

When using OpenAI services, it is important to keep both your API key and your account secure. Protect against API key leaks and account takeovers with these best practices.

# Keep your account secure

Security is a shared responsibility. OpenAI works to protect account access, and these steps can help reduce the risk of unauthorized use. If account credentials are used without permission, report the issue as soon as possible.

# Prevent API key leaks

An API key is the access code used to call the OpenAI API. If it is leaked, unauthorized users could access the API through your account. This can result in unauthorized charges or activity that violates our terms of service.

### Use environment variables

Store your API key in environment variables within your development environment. This helps keep the key out of application code and reduces the risk of exposure.  
  
If you use GitHub Actions, use [GitHub secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to store your API key.

## Be cautious with third-party products

Use caution with third-party libraries, frameworks, and tools that request access to your API key. Even if a product seems reputable, there is still a risk of key exposure or misuse.  
  
Before using a third-party product that requires your API key, review the company and the product carefully. Check reviews, read the privacy policy, and look for any security concerns raised by the community.

## Set reasonable spend limits

Set multiple spend thresholds, such as 90% and 95%, against a monthly budget at the organization or project level to monitor monthly spend.  
  
Configure custom email recipients to integrate with mailing lists, incident management platforms, and messaging platforms. This can be configured in Platform settings.

## Do not ship your API key

It can be tempting to embed your API key directly in an application to avoid running a server for a mobile app or a similar use case. However, this makes the API key vulnerable to misuse.

## Conduct thorough code reviews

Before pushing code to public repositories, review it to make sure no sensitive information, such as API keys, is exposed.  
  
Use automated scanning tools that can flag potential leaks. You can also review [GitHub's secret scanning tutorial](https://docs.github.com/en/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories) for more guidance.  
  
When OpenAI detects an API key on the public internet, or leaked inside an app in an app store, the API key is disabled immediately.

### Implement key rotation

Periodically change your API keys by deleting old keys and creating new ones through the [API key dashboard](https://platform.openai.com/account/api-keys).

# Prevent account takeovers

An account takeover occurs when someone gains unauthorized access to your account, potentially uses OpenAI services through it, and leaves the account owner with the bill.

## Use strong, unique sign-in credentials

If you use a password, use a unique password that you do not reuse on other sites. We recommend using a password manager to generate and store passwords.  
  
Change your password right away if you think it was exposed, reused, or shared.

## Enable multi-factor authentication (MFA)

Enable multi-factor authentication (MFA) to add another verification step during sign-in. For more information, see: [Enabling or disabling multi-factor authentication (MFA)](https://help.openai.com/articles/7967234).  
  
Even if someone gets your password, they would still need the second factor to access your account.  
  
Enabling MFA does not cancel existing logins. To block any users who are already accessing your account, reset your password first, and then enable MFA.  
  
If you want hardware-backed account protection and do not already have a security key, eligible OpenAI users can learn about the OpenAI + Yubico YubiKey bundle. To learn more, see: [OpenAI + Yubico YubiKey bundle](https://help.openai.com/articles/20001269).

## Use Advanced Account Security

For eligible consumer ChatGPT accounts, Advanced Account Security adds stronger sign-in requirements and stricter account safeguards. For more information, see: [Advanced Account Security](https://help.openai.com/articles/20001221). It is not available for ChatGPT Enterprise users, enterprise-managed accounts, or accounts associated with an enterprise-managed domain.

## Be cautious with emails and links

Be cautious with emails that ask for credentials or direct users to web pages that require account details.  
  
Always double-check the email address and URL to make sure they are from a trusted source.

# Respond to a suspected compromise

If you think your API key has been compromised, or you suspect unauthorized activity on your account, act quickly.

## Delete your API keys

Delete your API keys through the [API key dashboard](https://platform.openai.com/account/api-keys).  
  
OpenAI also supports [tracking usage by API key](https://platform.openai.com/api-keys). This makes it easier to view usage by feature, team, product, or project by using separate API keys for each.

## Contact OpenAI Support

The sooner you report the issue, the sooner OpenAI can help resolve it and reduce potential damage. Contact OpenAI Support by opening a new chat on any Help Center page.

## Review account activity

Check the account for unfamiliar activity, such as unexpected API usage. The details you provide can help with account recovery.

## Log out of all sessions

You can log out of all active sessions across devices. For instructions, see: [Log out of all sessions](https://help.openai.com/articles/20001257).  
  
In ChatGPT:

1. Go to **Settings**.
2. Select **Security**.
3. Select **Active sessions**.
4. Find **Log out of all sessions**.
5. Select **Log out all**.
6. In the confirmation modal, select **Log out of all devices**.

This logs you out of all active sessions across devices, including your current session. It may take up to 30 minutes.  
  
On Platform, go to **Your Profile > Security** and select **Log out of all devices**.  
  
It may take up to 30 minutes for other ChatGPT sessions to be logged out.
