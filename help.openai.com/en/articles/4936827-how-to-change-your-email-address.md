<!-- source: https://help.openai.com/en/articles/4936827-how-to-change-your-email-address -->

# How to change your email address

Instructions for OpenAI users and Administrators to change account email address

Updated: 2 days ago

# Options & Eligibility

Generally, users who are members of shared workspaces will need to go through their OpenAI Enterprise or Business Administrators to change their account email addresses.

| Option | Eligibility |
| --- | --- |
| Self-serve via ChatGPT Account Settings | 1. User never signed in with SSO **and** 2. User is not part of an Enterprise Workspace or Organisation  3. The current email domain has not been verified for an Enterprise, or Education, or Business customer \*.  Prerequisite: If the User had signed up with Google, Microsoft, or Apple, they will first be asked to create a Password. |
| By Administrator via SCIM | If [SCIM](/en/articles/10011769-scim-integration-faq#what-happens-if-a-user-updates-their-email-in-the-idp) is configured for the workspace, User Identity management is owned by the Administrator. |
| By Administrator via Global Admin Console | 1. User should not be SCIM managed 2. User should be part of the workspace connected to the Enterprise or Business workspace   Global Admin Console Administrators can perform the change for individual User profiles via Admin Console. |

For Enterprise-grade changes (SCIM or via Admin Console), if the current and the new email address have mismatched domains, then both of the domains must be verified in the Global Admin Console.

Please note that ChatGPT and the API Platform share the same account. Updating your email in ChatGPT updates the email you use to sign in to both ChatGPT and the API Platform.   
  
  
*\* If you are trying to change from a work email to a personal email and getting an error, it is likely that the domain has been verified by your company or institution, and you will not be able to change this account to your personal email address.*

# **Self-Service email address change**

1. Sign in to ChatGPT on web (You can’t change your email address from the ChatGPT iOS or Android apps)
2. Go to **Settings**.
3. Select **Account**.
4. Click your **email address**
5. Enter your new email address and complete the verification steps.

After you change your email, you’ll be signed out. Sign back in using your **new** email address.

## **For users who signed up with phone number**

If you signed up with only a phone number, add an email address in ChatGPT on web by going to Settings -> Account -> Email -> Add. After you add an email, you can update it later if your account is otherwise eligible for email changes.

## **For users who signed up with social login**

If you originally signed up using a social login method (such as Google, Apple, or Microsoft), you can change your email address after adding a password to your account.  
  
To do this:

1. Sign in to ChatGPT using your social login.
2. Go to **Settings** and select **Account**.
3. Add a password to your account.
4. Once a password is set, you’ll be able to update your email address.

This allows social login users to manage their email address in the same way as password-based accounts.

## **If you can’t change your email**

If you don’t have access to the change-email option, you can create a new account with the email address you want to use.

If you need to keep access to the same API Platform organization, create the new account and then add it to your existing org through the **Members** page.

⚠️ We cannot transfer over your ChatGPT history or workspaces to a new account.

Please note that this creates a brand new User account with new workspaces and organizations and unfortunately, all your prior work will be lost.

## What if my account has an active ChatGPT Plus subscription?

If you can sign in to your account, change your email using the steps above.

If you **cannot** sign in to the account that has the active subscription (for example, you no longer have access to the email address on the account), the available option is:

1. Cancel the subscription on the account you can’t access.
2. Create a new account and subscribe again using the email address you do have access to.

For help canceling a Plus subscription see [How do I cancel my ChatGPT Plus subscription](/en/articles/7232927-how-do-i-cancel-my-chatgpt-plus-subscription)?

## **What happens to my ChatGPT data when my email address is changed?**

Changing the email address associated with your ChatGPT account does **not** affect the contents of your account.

All of your existing data will remain intact, including:

* Chat history
* Projects
* Custom GPTs
* Workspace membership
* Settings and preferences

Only the email address used to sign in will change. Your account, its history, and all associated content will remain exactly as they were before the email update

# Administrative Email Changes

We do not allow Enterprise or Business users to self-serve email changes. Instead, Global Administrators must perform any Enterprise or Business user email change via the [Global Admin Console](/en/articles/12289294-global-admin-console). To do so, the Global administrators must:

1. Visit https://admin.openai.com/people
2. Click the `...` menu button, which appears when hovering over the row for a user.

   1. ![Image showing the Edit Email button](https://images.ctfassets.net/j22is2dtoxu1/5O2PqaAh087rm55CX6xfiF/af6bf319546571b83ab4944d5e0140c0/change_emails.png)
3. Select the "Edit email" option and enter in the new, valid email address  
     
   Note: The desired email domain must be verified in the tenant and not currently or previously in use by another OpenAI user. Please contact support@openai.com for additional support. Additionally, users will be automatically logged out when their email is updated.

# **Email change rate limits**

* You can change your email address up to two times within a 24-hour period.
* You can change your email address up to 20 times over the lifetime of your account.
* You cannot use your previous email address to create a new account.
* You cannot change your email address to an email address that already has an existing OpenAI account.
