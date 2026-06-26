<!-- source: https://help.openai.com/en/articles/20001221-advanced-account-security -->

# Advanced Account Security

Learn how to enroll in Advanced Account Security, what protections it adds, and who can use it.

Updated: 2 days ago

# Overview

Advanced Account Security is an optional security setting for consumer ChatGPT accounts. It adds stronger sign-in requirements and stricter account safeguards to help reduce the risk of account takeover, unauthorized access, and data exposure.

## Availability

Advanced Account Security is available for eligible personal ChatGPT accounts in [supported regions of ChatGPT](https://help.openai.com/articles/7947663).  
  
It is not available for:

* Enterprise-managed accounts.
* Accounts associated with verified and claimed domains.

Availability for workspace-linked accounts may depend on account configuration. If **Advanced Account Security** does not appear in **Settings > Security** on ChatGPT web, it is not currently available for that account.  
  
If an account later becomes enterprise-managed, Advanced Account Security may be disabled for that account.

## Before you begin

To enroll, you need at least two secure sign-in methods, including one that works across devices. These can include passkeys, FIDO-compatible security keys, or a combination of both.  
  
You also need to save the recovery keys provided during setup. Recovery keys are required to regain access if you lose access to your passkeys or security keys. Be prepared to store recovery keys in a secure location prior to enrolling.  
  
Because Advanced Account Security disables standard SMS and email account recovery, losing access to all sign-in methods and recovery keys may result in losing access to your account.

## Sign-in method examples once enrolled

Valid setup examples can include:

* A passkey and a compatible hardware security key.
* Two compatible passkeys, if at least one works across devices.
* Two compatible hardware security keys.

A passkey saved only on one device may not meet the cross-device requirement. If setup asks you to set up your passkeys again, set them up again before continuing. The setup flow will show whether your sign-in methods meet the requirements.

# Enroll in Advanced Account Security

You can start enrollment in Advanced Account Security on web, Android, and iOS platforms.

1. In ChatGPT, go to **Settings**.
2. Select **Security**.
3. Select **Advanced Account Security**.

   1. Users on mobile platforms will be redirected to a web browser to complete enrollment.
4. Select **Enroll**.
5. On the secure setup page, select **Continue**.
6. Add at least two secure sign-in methods, including one that works across devices.
7. Save your recovery keys and confirm that you saved them.

After initial setup, you are signed out of all devices. Sign in again with one of your passkeys or security keys.

# What changes when Advanced Account Security is enabled

When Advanced Account Security is enabled:

* Passkeys and security keys are used for sign-in.
* Password sign-in is disabled.
* Email and SMS sign-in codes are disabled.
* Email account recovery is disabled.
* Email login notifications are enabled.
* Active sessions are shorter, so you may need to sign in again more often.

  + You can review active sessions, log out of individual sessions, and log out of all sessions from [**Active sessions**](https://help.openai.com/articles/20001257) in **Security** settings.
* Conversations are not used to train OpenAI models while Advanced Account Security is enabled.

# Recovery keys and account access

Recovery keys help you regain access to your account if you lose your sign-in methods.  
  
Keep your recovery keys stored somewhere safe. Each recovery key can only be used once.  
  
If you use a valid recovery key, account recovery begins. For security, your account is unlocked 48 hours after you enter a valid recovery key. After that waiting period, follow the prompts to complete account recovery.  
  
If you lose your recovery keys, or if you think someone else has them, replace them. Replacing recovery keys invalidates the old keys.  
  
To replace recovery keys:

1. In ChatGPT, go to **Settings**.
2. Select **Security**.
3. Select **Advanced Account Security**.
4. Under **Recovery keys**, select **Manage**.
5. Select **Replace recovery keys**.
6. Save the new recovery keys and confirm that you saved them.

OpenAI Support can help explain available recovery options. However, OpenAI Support cannot use standard email account recovery, reset your password, remove Advanced Account Security, or add or remove sign-in methods to restore routine access while Advanced Account Security is enabled.

# Order a YubiKey

During enrollment, eligible users in the US, UK, and EEA may see a prompt to **Order a YubiKey**. YubiKeys are optional hardware security keys made by [Yubico](https://www.yubico.com/openai-and-yubico/). You can use any FIDO-compatible security key with Advanced Account Security, and you can also use passkeys.  
  
The YubiKey bundle is optional and is not required to use Advanced Account Security. For details about what is included, preferred pricing, availability, and Yubico order support, see: [OpenAI + Yubico YubiKey bundle](https://help.openai.com/articles/20001269).

# Disable Advanced Account Security

You can disable Advanced Account Security later. You may be asked to complete a secure sign-in flow before disabling it.  
  
To disable Advanced Account Security:

1. Go to **Settings**.
2. Select **Security**.
3. Select **Advanced Account Security**.
4. Select **Disable**.
5. Complete any secure sign-in prompts.

If you disable Advanced Account Security, your account returns to standard sign-in and recovery settings.  
  
This means:

* Password sign-in is enabled again.
* Email and SMS sign-in codes are enabled again.
* Email account recovery is enabled again.
* Login attempt email alerts are turned off.
* Recovery keys are removed.
* Passkeys and security keys remain on your account, but they are no longer required to sign in.

# FAQ

## How do I know if I should enroll in Advanced Account Security?

Advanced Account Security adds stronger protections against unauthorized account access. However, it also introduces stricter recovery requirements and may increase the risk of permanently losing access to your account if you lose your sign-in methods and recovery keys.  
  
This feature is designed for users who may be at increased risk of digital attacks, or for users who want the highest available level of account security and are comfortable taking on additional responsibility for account recovery.

## Who can use Advanced Account Security?

Advanced Account Security is available for eligible personal ChatGPT accounts in supported regions. It is not available for ChatGPT Enterprise users, enterprise-managed accounts, or accounts associated with an enterprise-managed domain.  
  
Availability for ChatGPT Business and other workspace-linked accounts can depend on account configuration and rollout. If Advanced Account Security does not appear in **Settings > Security**, it is not currently available for that account.

## Is Advanced Account Security available in ChatGPT Enterprise or ChatGPT Business?

Advanced Account Security is not available for ChatGPT Enterprise users, enterprise-managed accounts, or accounts associated with an enterprise-managed domain.  
  
Availability for ChatGPT Business and other workspace-linked accounts can depend on account configuration and rollout. If Advanced Account Security does not appear in **Settings > Security** on ChatGPT web, it is not currently available for that account.

## Do I need a YubiKey to use Advanced Account Security?

No. A YubiKey is optional. You can use passkeys, compatible FIDO security keys, or a combination of both, as long as you meet the setup requirements. For more information about the optional YubiKey bundle, see: [OpenAI + Yubico YubiKey bundle](https://help.openai.com/articles/20001269).

## Can I still sign in with a password?

No. Password sign-in is disabled while Advanced Account Security is enabled.

## What happens if I lose access to my sign-in methods?

Use your recovery keys to start account recovery. If you lose access to all sign-in methods and recovery keys, you may lose access to your account.

## Can OpenAI Support recover my account if I lose all sign-in methods and recovery keys?

OpenAI Support can help explain available options, but standard email account recovery is not available while Advanced Account Security is enabled. OpenAI Support cannot reset your password, remove Advanced Account Security, or add or remove sign-in methods to restore routine access.

## Does Advanced Account Security affect model training?

Yes. Conversations are not used to train OpenAI models while Advanced Account Security is enabled.

## Can I turn off Advanced Account Security later?

Yes. You can disable Advanced Account Security later. Disabling it removes the additional protections and restores standard sign-in and recovery options.
