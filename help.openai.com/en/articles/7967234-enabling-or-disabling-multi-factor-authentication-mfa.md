<!-- source: https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa -->

# Enabling or disabling multi-factor authentication (MFA)

How to turn multi-factor authentication (MFA) on or off for your OpenAI account.

Updated: 3 days ago

# Overview

Multi-factor authentication (MFA) enhances account security by requiring a second step to verify your identity during sign-in. After MFA is enabled, it applies across OpenAI services, including ChatGPT and the API Platform.  
  
After MFA is enabled, you may be asked to complete an enabled verification method when you sign in.

# Availability

Your available MFA options may vary depending on your device, country, account tier, and how your account was created. OpenAI is working to make more options available over time.

# How MFA works

When MFA is enabled, you may be asked to verify your identity using a second method during sign-in. You can choose from available verification options, including:

* Authenticator app: Use one-time codes from an app such as Google Authenticator or Authy.
* Push notifications: Approve sign-ins by responding to a prompt sent to your trusted device.
* Text message: Receive a 6-digit code by SMS or WhatsApp.
* Passkey: Use a passkey as an additional form of MFA for your account.

For more information about passkeys, see: [Passkeys to secure your OpenAI account](https://help.openai.com/articles/20001039).  
  
Some passkeys can be stored on a compatible hardware security key. If you want to use a hardware security key and do not already have one, eligible OpenAI users can learn about the OpenAI + Yubico YubiKey bundle, available at preferred pricing. To learn more, see: [OpenAI + Yubico YubiKey bundle](https://help.openai.com/articles/20001269).

## Turn MFA on or off

You can manage MFA from ChatGPT or the API Platform.  
  
In ChatGPT:

1. Go to [ChatGPT settings](https://chatgpt.com/#settings/Security).
2. Select **Security**.
3. Under **Multi-factor authentication**, select the MFA option you want to enable or manage, then follow the setup or removal instructions.

# Complete MFA setup

Some MFA methods require additional setup. Depending on the method, you may be asked to:

* Scan a QR code with your authenticator app and enter a one-time code.
* Receive a code by SMS or WhatsApp and enter it to confirm.
* Enter your phone number before enabling SMS or WhatsApp.

After setup, MFA will be active the next time you sign in.  
  
If you have multiple MFA methods enabled, OpenAI defaults to the most secure option first. You can still choose any enabled method when signing in.

# Use another sign-in method

If you are unable to use your usual MFA method, you can choose another available option during sign-in. If you enrolled in Advanced Account Security and lost access to your passkeys or security keys, use your recovery key to regain access.

1. Sign in to ChatGPT.
2. Enter your password.
3. When prompted to verify your identity, select **Try another method**.
4. Select another available option, such as a passkey, push notification, authenticator app, text message, or email.

# FAQ

Use these answers for common MFA account questions.

## Does enabling MFA log you out of other devices?

No. Enabling MFA does not automatically log you out of other devices or sessions.  
  
To manually log out of all active sessions:

1. Go to [ChatGPT settings](https://chatgpt.com/#settings/Security).
2. Select **Security**.
3. Select **Log out of all devices**.

It may take up to 30 minutes for all sessions to be logged out.

## Can admins enforce MFA for a workspace or organization?

Not at this time. MFA cannot currently be enforced at the ChatGPT workspace or API Platform organization level.
