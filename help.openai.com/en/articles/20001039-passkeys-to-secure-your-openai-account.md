<!-- source: https://help.openai.com/en/articles/20001039-passkeys-to-secure-your-openai-account -->

# Passkeys to secure your OpenAI account

Learn how passkeys work and how to add or manage passkeys for your OpenAI account.

Updated: 2 days ago

# Overview

Passkeys provide a secure and convenient way to sign in to your OpenAI account without relying on passwords. They use cryptographic credentials stored on your device or a security key, such as a YubiKey, and are protected by built-in security methods like biometrics (Face ID, Touch ID), a device PIN, or a hardware key touch.  
  
If you want to use a hardware security key and do not already have one, eligible OpenAI users can learn about the OpenAI + Yubico YubiKey bundle, available at preferred pricing. See: [OpenAI + Yubico YubiKey bundle](https://help.openai.com/articles/20001269).

# How passkeys work

When you create a passkey, your device stores a credential that can be used to authenticate your OpenAI account.  
  
Depending on your account and configuration, passkeys can be used to:

* Sign in to your account.
* Verify your identity as a multi-factor authentication (MFA) method.

# How to enable passkeys

1. Sign in to ChatGPT on web.
2. Go to **Settings**.
3. Select **Security**.
4. Under **Passkeys**, select **Add passkey** and follow the on-screen instructions.

# Managing passkeys

After a passkey is created, you can:

* Add additional passkeys.
* Remove passkeys.

You can manage passkeys from **Settings > Security** under **Passkeys**.

# Signing in with a passkey

If you have set up a passkey, it will be the default way to sign in after you enter your email. A passkey lets you sign in securely without entering your password or using an MFA code.  
  
If you prefer to use your password instead, select **Try another method** to choose a different sign-in option.  
  
A passkey may also be used as an additional verification step during sign-in, depending on your account settings.

# Accessing your account another way

If you are unable to use a passkey, you can sign in using another authentication method:

* Start signing in to ChatGPT.
* When prompted to verify your identity, select **Try another method**.
* Follow the on-screen instructions and choose an available verification option.

If you are setting up Advanced Account Security and are asked to set up your passkeys again, return to **Settings > Security** and **Passkeys**, add or re-create your passkeys, and then continue setup. Advanced Account Security requires at least two secure sign-in methods, including one that works across devices, such as a synced passkey or a security key.

# Additional information

* You may not see the option to add a passkey to your OpenAI account yet. Passkey availability depends on how your account was created, whether your account has an email address, and the sign-in method you use. If your account does not have an email address, Security keys & passkeys will not appear in Security settings, and passkey login is not available for that account. If your account is managed by an organization that uses single sign-on (SSO), you will continue to sign in through your organization, and your passkey will function as your multi-factor authentication (MFA) method.
* Passkeys may be tied to a specific device or synced across devices, depending on your setup. If your passkey is only stored locally and not synced, losing access to that device may prevent you from using it.
* If you have created a synced passkey, for example, using a provider like iCloud Keychain, it may be available across multiple devices signed in to the same account.
* Some platforms also support using passkeys from a nearby device. For example, if you are signing in on a laptop that does not have a passkey saved, you might be able to complete sign-in using a passkey on your phone by scanning a QR code or approving a prompt.
* Passkey behavior may vary depending on your device, browser, and passkey provider.
