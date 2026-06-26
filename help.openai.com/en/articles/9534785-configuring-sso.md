<!-- source: https://help.openai.com/en/articles/9534785-configuring-sso -->

# Configuring SSO

This document walks through configuring SSO for ChatGPT and API Platform

Updated: 3 days ago

# Prerequisites

In order to set up SSO, you must:

1. Have an OpenAI plan with a [Global Admin Console](/en/articles/12289294-global-admin-console)
2. Be a Global Admin

Before proceeding, please review our [SSO Overview](/en/articles/10468051) and [User Management](/en/articles/10479654-understanding-your-ideal-user-management-setup) documentation pages to ensure you are familiar with our SSO architecture.  
  
If you previously configured SSO for an API Platform organization or ChatGPT workspace, your SSO settings should already be available to configure at [OpenAI Identity](https://admin.openai.com/identity) page. If the workspace or org for which you want to enable SSO is *not* shown in your Global Admin Console, please reach out to support@openai.com.

**⚠️ Your users will be locked out if SSO is not set up correctly!**

An incorrect setup can result in your users being locked out of orgs and workspaces where SSO is set to required. We recommend that you, as the global admin, maintain SSO as Optional in the Admin Portal.   
  
During setup, keep two separate logged in windows open:

1. One logged in through an incognito window
2. One logged in through your standard browser

This allows you to test the login process and your SSO/Domain Verification setup on one window, and to revert the changes if needed via the second window.

## Testing SSO

If you would like to test the setup process without risking an impact on your users, you can do so via the application [here](https://workos-openai-explore.vercel.app/#).  
  
Completing a successful connection on this test application will not tie back to your production org, nor will it save the connection (so you can reuse the same parameters in your production instance once you're ready). This means that it is safe to use as a sandbox or playground while you familiarize yourself with the requirements and work out any missing prerequisites.

# Enabling SSO

To get started, navigate to the [OpenAI Identity](https://admin.openai.com/identity) page from the Global Admin Console. You can also reach that page from the link on the "[Identity & Provisioning](https://chatgpt.com/admin/identity)" page underneath your "Manage Workspace" settings in ChatGPT or the [Identity](https://platform.openai.com/settings/organization/identity) tab in your API Platform organization settings.  
  
Some of the examples below will showcase the setup in Okta, but the same logic should be applicable to all SAML IdP's.

## Domain Verification

In order to enable SSO, we require that you first verify at least one domain.

Important: Remember to review the [downstream impact](/en/articles/10479654-understanding-your-ideal-user-management-setup#h_e98d30d493) that domain verification may have upon users with that domain.

Click the "+ Add Domain" button and enter your DNS to get started:

![Verify a new domain dialog with example.com entered and Submit available](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9ecef106d30e779b5eafef4e/ad450fe091597c93bb5b910811696272/Screenshot-2B2025-01-28-2Bat-2B11_58_52-E2-80-AFAM.png)

Once submitted, we provide a key for you to verify ownership of your domain. Navigate to your DNS provider, and add a TXT record with the provided value:

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-74b353f91705a65dfdbc5d71/15c6875572c6e2e0ef6fded2db11410f/Screenshot-2B2025-01-28-2Bat-2B11_59_59-E2-80-AFAM.png)

Your TXT record must be reachable via a DNS lookup in order for the verification check to succeed.  
  
After completing this in your DNS provider, return to the setup page and click the "Check" button. If your domain ownership was validated successfully, you will see the status updated to "Verified."

![Domain management page with company.abc listed as Verified](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9c8fbb47cf425194b89592a4/2865c91dd537ae45cd7c7de278f04c3a/Screenshot-2B2025-01-28-2Bat-2B12_02_42-E2-80-AFPM.png)

You can add up to 99 verified domains per Admin Portal, and we provide a 7-day period for you to complete the verification check before marking a domain as expired. Domains can only be verified on a single Admin Portal. If you need to verify the same domain on an organization or workspace not in your Admin Portal, please contact Support.

# Configuring Your Application

After successfully verifying your domain, you can proceed with the SSO setup by configuring your IdP application.  
  
To get started, click the "Set up SSO" button:

![OpenAI Admin Identity & Access page with Single Sign-On section and Set up SSO button](https://images.ctfassets.net/j22is2dtoxu1/1VYxWrradMFnVfFDrDNJ4q/cc0f9f13b29c3006885032e515b300be/set_up_sso.png)

## Selecting your Identity Provider

You have the option to select from a list of the most popular IdP's that natively support SAML integrations. If you do not see your IdP in the list, or if you would like to use an OIDC connection, you can choose the appropriate Custom connection button shown at the bottom:

![Identity provider selection screen for SSO setup with common providers plus Custom SAML and Custom OIDC](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a9b1ad48388f582ab2d3ee01/30b6d25b4a56ebfcf8a6c5b7e21bfd76/Screenshot-2B2025-04-07-2Bat-2B1_36_31-E2-80-AFAM.png)

## Creating/Connecting the Application

You can now follow the step-by-step configuration wizard to help create and connect your IdP application with us. Depending upon the IdP you are using, your instructions may vary slightly, but the general setup remains the same:

![OpenAI Configure Single Sign-On page with Okta selected and step 1 Create a SAML Integration](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-befb1024d2ed141f8777b311/e599a0a4ea4c3a2b8100af72f1db0fff/Screenshot-2B2025-04-07-2Bat-2B2_07_20-E2-80-AFAM.png)

Note that the URL's provided in the creation step will be unique to your organization:

![Configure SAML step with Single sign-on URL and Audience URI values to copy into Okta](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-841fbb430f23a3785d7ddac1/4a1b041ca0e9769d55a2868de8ca32e9/Screenshot-2B2025-04-07-2Bat-2B2_10_54-E2-80-AFAM.png)

***Important****: If you choose to reset a healthy SSO connection, these URL values will change. When setting up SSO again, you will need to make sure to update them in your application accordingly.*

Once you've completed the URL setup, you can proceed to defining the attribute mapping for users authenticated through your application.

## Attribute Mapping

The attribute mapping you define in your SSO application ultimately determines which OpenAI accounts are authenticated and how your users appear in OpenAI products. Our current user model supports three properties:

1. Email Address (required in the SAML response, determines which account is accessed)
2. First Name (optional, but recommended)
3. Last Name (optional, but recommended)

Note: We do **not** support decrypting SAML Responses. Please ensure that you are not encrypting your response or assertion to guarantee we're able to correctly identify the attributes.

Depending on your IdP, the exact attribute mapping will vary. We recommend adhering to the exact mapping depicted for your IdP in the setup wizard, e.g. Okta would be:

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-86994d2d2fb45637eb74857f/4efbd1c2c0e847bbd58c18b58be3e803/Screenshot-2B2025-04-07-2Bat-2B9_30_29-E2-80-AFAM.png)

If you are seeing new users come through with their email addresses set to their display name, please review your attribute mapping and confirm that you are not encrypting your responses.  
  
Alternatively, if new users are being asked to enter their name and birthday, this likely indicates we're not identifying a proper name value from your attribute response.

## Email Changes

Occasionally, a user's email address may get updated in your IdP, e.g.

* A legal name change following a marriage
* Their company was acquired and they have a new domain
* etc.

If this changes the value of the emailaddress claim in the SSO SAMLResponse, a different OpenAI user tied to the new email address will be accessed (and created if not previously existing) upon successful SSO. This user will need to be invited to the Org or Workspace separately from the original user.

## Primary Email Addresses

In some cases, you may have users with multiple different email addresses. This is a common scenario in larger companies that have distributed mailing systems or for Edu customers with different schools, e.g.

* [user\_a@main\_school.edu](mailto:user_a@main_school.edu)
* [user\_a@business\_main\_school.edu](mailto:user_a@business_main_school.edu)

In this situation, we recommend ensuring that your SAML response only includes a single email address in its attributes, as including multiple emails can cause confusion when we attempt to tie it to a new or existing user.  
  
Additionally, if the users have a static email address (e.g. a UPN), we recommend utilizing this in your attribute mapping to ensure they will have a stable OpenAI user account that will not be impacted when their other email addresses may be changed.

## Provision IdP Application Access

Once you have successfully created your attribute mapping, the wizard will walk you through the steps to provision access to the appropriate users via the desired groups.  
  
Please review our recommendations on [User Management](/en/articles/10479654-understanding-your-ideal-user-management-setup) for best practices.

## Setting IdP Metadata

At this point in the setup, you have two separate options for defining your IdP's metadata: Dynamic Configuration and Manual Configuration.

## Dynamic Configuration

This is the recommended and most straightforward option. With Dynamic Configuration, you simply need to provide the Metadata URL (now populated by the SSO URL and Entity ID you configured earlier) associated with your application. The setup wizard will show you where you can find this in your IdP:

![Okta SAML app Sign On tab with Metadata URL and Copy action for uploading identity provider metadata](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f6b6c12b479c10eeef6ae6eb/6f1d1b94f85c5a1aa8fe385c87e0bb85/Screenshot-2B2025-04-07-2Bat-2B9_47_02-E2-80-AFAM.png)

## Manual Configuration

As the name implies, Manual Configuration requires a bit more work. Depending upon your IdP, you will need to enter the corresponding SSO URL and IdP issuer, along with an x.509 certificate:

![SSO setup step 5 with Manual configuration selected for entering identity provider metadata](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2bbe3eb8463d99fc1534f9f4/5f8227f5f6f2fa4998d0cb4414e814aa/Screenshot-2B2025-04-07-2Bat-2B9_45_28-E2-80-AFAM.png)

## IdP-Initiated Login

If you would like for your users to be able to click a tile on their dashboard and be automatically authenticated, you can configure IdP-initiated auth to your application as part of the setup process. While the exact process will vary depending upon your IdP, the general process will utilize a provided URL in the form of:

* ChatGPT: <https://chatgpt.com/auth/login?sso=true&connection=conn_0123abc>
* API Platform: <https://platform.openai.com/enterprise/conn_01ABC02DEF/login>

As an example, Okta will walk you through creating a new Bookmark Application with this URL:

![Okta Create Bookmark App step with Platform label and an OpenAI enterprise login URL entered](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-93ad488172dd85f36f09c597/55db738968c87ee93cf3f755fb331517/Screenshot-2B2025-04-07-2Bat-2B11_38_04-E2-80-AFAM.png)

Whereas Entra ID will allow you to enter the provided "Sign on URL" into the appropriate form:

![Microsoft Entra Basic SAML Configuration with Identifier and Reply URL fields filled for SSO setup](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-852a1cdc6e1ea8461e72a4cd/f77f7543a9eedb5720e0e3b1a5121f5b/Screenshot-2B2025-04-07-2Bat-2B11_31_53-E2-80-AFAM.png)

**Important**: If you choose to reset a healthy SSO connection, these URL values *will* change.

This means that when you configure the new connection, you will also need to update your Sign on URL accordingly, or else users will not be able to authenticate via their tiles.

## Completing Setup

Once you've configured your IdP's metadata, you can click "Continue" to proceed with setting up any optional bookmark apps. The final mandatory configuration step will be on the "Test Single Sign-On" page:

![OpenAI Configure Single Sign-On Step 8 with Continue to sign-in button for testing Okta SSO](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6596006d7747e8be446bad83/26359b636bf8812ea22b0a307bc92fde/Screenshot-2B2025-04-07-2Bat-2B9_52_38-E2-80-AFAM.png)

After hitting "Continue to sign-in," the wizard will attempt to test your new connection. If everything is successful, you will have effectively enabled SSO. You should now see this reflected on your configuration page:

![OpenAI Single Sign-On test succeeded confirmation page](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-950428c8f7f006e93886fe21/c3abde951cff2f07dc51c77193d17c72/test_connection.png)

![Connection activated for ChatGPT with Okta, with test sign-in and valid metadata configuration](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6ea500653783fda88c27dc47/091a8fc02a0e2d66a70d848cda47b61f/manage_sso_view.png)

Users in your IdP group with corresponding accounts or invitations should now be able to login with SSO:

* They can navigate to chatgpt.com or platform.openai.com, enter their email, and then authenticate after we forward them to their IdP
* They can use the Bookmark Tile URL you (optionally) configured during the setup

If you find that your users are unable to authenticate successfully, and you run into trouble reverting the changes, please reach out to Support for immediate assistance.  
  
Remember that enabling SSO on the API Platform applies the domain verification across all users with that domain. This means that, even if the users do not belong to your Enterprise organization, they will still be required to be part of your IdP group in order to access their personal organizations.

# Troubleshooting Logins

If after enabling SSO, you're encountering issues logging in, you can review our [FAQ and Troubleshooting](/en/articles/10489721-login-and-authentication-faq-s-and-troubleshooting-sso-scim-and-domain-verification) page for assistance to identify common errors. If you don't find a sufficient answer there, please don't hesitate to reach out to Support.
