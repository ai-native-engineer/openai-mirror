<!-- source: https://help.openai.com/en/articles/10479654-understanding-your-ideal-user-management-setup -->

# Understanding Your Ideal User Management Setup

This document is intended to help admins deploy SSO, and potentially SCIM, in a way that works best with their use-case.

Updated: 54 minutes ago

Please review our ["SSO Overview"](/en/articles/10468051-sso-overview) page to familiarize yourself with the key concepts discussed in this document.  
  
Prior to verifying your domains, it’s important to consider a few different questions:

* How would you like to provision invitations to new users?
* How would you like to handle existing consumer (personal/Plus/Pro) users?
* What do you want your user login flow to look like?

We'll take a look at each of these questions in more detail to help ensure you're choosing the option that best fits your needs.

# Inviting New Users

We currently offer four different methods for provisioning invitations to users:

1. [System for Cross-domain Identity Management (SCIM)](#scim)
2. [Direct Invitations from ChatGPT or API Platform](#direct-invitations-from-chatgpt-or-api-platform)
3. [ChatGPT only: Automatic Account Creation (AAC)](#automatic-account-creation-aac)
4. [Platform only: API Platform Admin Invites Endpoint](#api-platform-admin-invites-endpoint)

It's worth noting that we differentiate between cases where invitation emails are actively sent and cases where an invitation is silently associated with a user's email in our backend.  
  
Invitation emails are actively sent when:

* A new user is invited for the first time through SCIM.
* A user is invited directly from ChatGPT or the API Platform.

Invitations are silently associated when:

* A SCIM user was removed from your IdP group and then re-added.
* Automatic Account Creation applies.

In the latter case, users will not see the invitations in their inbox, but they will still be properly directed to the corresponding workspace/organization when they try logging in.

## SCIM

SCIM is available in both [ChatGPT](/en/articles/9627404-openai-chatgpt-scim-integration-faq) and the [API Platform](/en/articles/10011769-openai-platform-scim-integration-faq). SCIM allows identity providers (e.g. Okta, Entra ID, etc.) to exchange user identity data with OpenAI, automating the provisioning of invitations (and the de-provisioning of user accounts) based on organizational changes.

While SCIM is also configured through your IdP, it can be setup independently of SSO. Therefore, domain verification/SSO are not requirements for SCIM.

If you decide to use both SCIM and SSO, the important distinction to make is:

* SCIM only provisions invitations
* SSO handles the authentication and user creation

We consider SCIM to be the most robust and scalable solution for overall user management. Depending upon your ideal implementation, we generally recommend the following architecture as best practice if you are deploying across both ChatGPT and the API Platform:

![IdP setup diagram comparing one shared SAML app versus separate SCIM apps for ChatGPT and API Platform users](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-bf44d65589ce005ade2cf657/ab931049a6603fd3a1ec93ae539a91d2/Screenshot_2025-08-04_at_10_09_14_E2_80_AFAM.png)

With this setup, you can easily manage both invitations ***and*** access (to ChatGPT and the API Platform) separately. This setup has the added benefit that any necessary changes can be performed centrally by your administration teams directly in your IdP.

If you are implementing SCIM across multiple applications (i.e. ChatGPT vs. API Platform vs. other accounts), your SCIM Applications should be unique. Even if your target user-base is identical, it is highly recommended that each SCIM implementation should reference a unique application in your IdP.

If you do not meet this requirement, it can lead to inconsistency issues that ultimately result in invalid memberships.

## Direct Invitations from ChatGPT or API Platform

Admins can directly invite users by email from the respective [ChatGPT](https://chatgpt.com/admin) and [Platform](https://platform.openai.com/settings/organization/members) "Members" pages. In ChatGPT, this method also supports bulk invitations via an uploaded CSV:

![Workspace invite modal with CSV upload, email entry, and Resend emails for existing invites selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a2f86d393dd0a6a6c72dcb83/80154e6e689d599e558364a046268c51/Screenshot_2025-01-29_at_11_14_31_E2_80_AFAM.png)

While typically not scalable, we often recommend using direction invitations as you're getting started in a new workspace/organization. Unlike SCIM, there is no potential delay for the invitations reaching user inboxes, so it's the most effective option for providing quick access, modifying permissions, and general testing.  
  
Additionally, you can always enable SCIM down the line and bucket your existing users underneath the SCIM application. So there is no concern that directly invited users would be excluded from future automation unless desired.

## Automatic Account Creation (AAC)

Contrary to the other options, AAC is only available in the [Identity page of ChatGPT](https://chatgpt.com/admin/identity) and requires SSO to have first been enabled:

![Automatic account creation setting for verified-domain users turned off](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f9ba92c698ee6e7c694b7375/41709363ba37b1cd64c50907b54ac044/Screenshot_2025-01-29_at_11_23_05_E2_80_AFAM.png)

As shown above, AAC guarantees that users signing up or logging in with a verified email domain will automatically be added to your Enterprise workspace. The users will not receive an invitation email, and the process is entirely automated. This has its pros and cons.  
  
If your policy is to allow open-door access to any user with your verified domain, AAC is a great option that avoids the added overhead of configuring and managing a SCIM application.  
  
However, AAC is not ideal if you require a more locked-down, approval-based approach to user access.

⚠️ WARNING ⚠️  
  
It's important to keep in mind that enabling AAC will effectively force merge all consumer (personal/Plus/Pro) users underneath your domain into your Enterprise workspace. More on this can be found below in the ["Handling Existing Users"](#handling-existing-consumer-users) section.  
  
Note that, even if the users are not members of your IdP access group and are unable to successfully access the workspace if SSO is enforced, they still take up a seat in your Enterprise account in this scenario.

For this reason, we generally recommend SCIM or direct invitations in most cases rather than AAC. And to help avoid potential avenues of confusion, we recommend leaving AAC turned off if you do plan to use SCIM.

## API Platform Admin Invites Endpoint

Our API Platform supports an [Invites Endpoint](https://platform.openai.com/docs/api-reference/invite), which allows you to programmatically invite users to your API organization.  
  
Compared to SCIM, the major benefit of the endpoint is that it allows you to specify the project(s) the invited user should belong to:

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-59a9a64289c25a65e12cf6e2/d27e5042a90bf59344f8437988f26a8e/Screenshot_2025-01-29_at_11_33_41_E2_80_AFAM.png)

This provides an additional layer of granularity and control, without requiring the manual work of individual direct invitations.

# Handling Existing Consumer Users

We define consumer users as those on a personal, Plus, or Pro subscription. It's often the case that there will be existing consumer users with your verified domain who have had accounts prior to your Enterprise contract. As verifying your domain and enabling SSO can have a downstream impact on these consumer users, it's important to determine the desired outcome beforehand.

## Impact on ChatGPT Consumer Users

On the ChatGPT side, the impact to consumers is largely determined by two factors:

1. Will they be invited to the Enterprise workspace?
2. Will you enforce SSO?

The resulting behavior can be seen below:

| Pending Invite? | SSO Enforced? | Result |
| --- | --- | --- |
| Yes | Yes | Consumer user accounts will be forced to merge to Enterprise, and can only log in with SSO. |
| Yes | No | Consumer user accounts will be forced to merge to Enterprise, and users can authenticate with SSO or social login. |
| No | Yes | No impact: Consumer users maintain access to their personal workspaces through password or social authentication. |
| No | No | No impact: Consumer users maintain access to their personal workspaces through password or social authentication. |

If your goal is to ultimately prevent any consumer accounts, please reach out to your Account Director to discuss potential options.

### Account Merge

The prerequisites to trigger an automatic account merge of the consumer account into an Enterprise account are as follows:

1. The user's domain is verified.
2. The user has received an invitation to the Enterprise workspace where their domain is verified.

   * Note: If you've enabled AAC, this condition will always be true for any user with your verified domain.

When these conditions are met, then the next time the user logs into or refreshes ChatGPT, they should see the following modal:

![ChatGPT Enterprise invite flow with options to transfer chat history and GPTs or export and delete the old workspace](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6d001a1a4f866bb489597b1d/080500d97c87e9fb3028a08a639cd02b/Screenshot_2025-01-30_at_11_18_00_E2_80_AFAM.png)

As the image highlights, we will automatically refund any existing Plus or Pro subscriptions prior to the merge. Users will have the option to transfer their existing chat history and GPT's, or else export their chat history via email and start their Enterprise workspace as a "clean slate."

* Note: If the destination Enterprise or Edu workspace has Data Residency enabled, Personal workspace data cannot be transferred. Users can only export their chats and delete the Personal workspace. See [Email invitations and account migrations](/en/articles/9672121-getting-started-with-identity-and-provisioning-in-chatgpt-enterprise-edu-and-chatgpt-for-teachers#email-invitations-and-account-migrations) for details.

Once the consumer account has been merged, there is no way of restoring it. If your users chose the "Transfer existing chat history and GPTs" option but did not see this reflected on their Enterprise workspace, please reach out to Support.

## Impact on API Platform Consumer Users

Because SSO on the Platform is still domain-based (versus ChatGPT, where SSO is specific to the workspace where it's been enabled), your consumer users will be impacted as soon as you verify your domain and enable SSO on *any* organization.  
  
The consumer users will lose the ability to authenticate with passwords, as we identify the domain match and forward them to your IdP. If they are members of your IdP, they can authenticate successfully. Alternatively, they can log in with a social OAuth option if that is available to them. **If not, then you have effectively locked them out of their consumer accounts.**  
  
See the [User Login Flow](#user-login-flow) section for a more in-depth guide to this workflow.

# Recommended Identity and Provisioning Patterns

Now that we've laid out the fundamental behavior tied to our identity authentication and invitation provisioning, it may be helpful to review some of the more common implementation patterns available to Enterprise users:

![Comparison table of four Enterprise user management setups by provisioning, authentication, and user experience](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d689cda57c33180a6856f273/74eb2bc1521b6596c1b831ef12f67fa3/Screenshot_2025-01-30_at_12_09_40_E2_80_AFPM.png)

# User Login Flow

We've already discussed the impact of pending invitations and SSO enforcement, so this section is meant to help visualize the expected flow/checks we perform when a user types in their email address to login.

## ChatGPT Login Flow

Note: This diagram excludes login attempts through a Social method or through the Tile URL.

![Flowchart of ChatGPT login paths for personal accounts, password sign-in, workspace picker, and SSO redirection](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-7ee9def3fd3b73f5c83a6e66/84de4bc673e17f099dbae65350f27c68/ChatGPT_Login_Flow.png)

## API Platform Login Flow

Note: This diagram excludes login attempts through a Social method or through the Tile URL.

![Flowchart for platform login and SSO outcomes based on verified domain and IdP access group membership](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1853c6462b0e8c2311cac757/b3df3e348118d89c0bc23f6adeb86d3f/API_Platform_Login_Flow.png)

# Next Steps

Now that you have an idea on your ideal implementation, you can follow the respective documentation to enable SCIM or SSO:

* [ChatGPT SCIM Integration](/en/articles/9627404-openai-chatgpt-scim-integration-faq)
* [API Platform SCIM Integration](/en/articles/10011769-openai-platform-scim-integration-faq)
* [Enabling SSO on ChatGPT](/en/articles/10472980-enabling-sso-on-chatgpt)
* [Enabling SSO on the API Platform](/en/articles/10479310-enabling-sso-on-the-api-platform)
