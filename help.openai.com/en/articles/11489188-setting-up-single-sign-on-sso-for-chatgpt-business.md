<!-- source: https://help.openai.com/en/articles/11489188-setting-up-single-sign-on-sso-for-chatgpt-business -->

# Setting up single sign-on (SSO) for ChatGPT Business

Set up SSO for a ChatGPT Business workspace, verify your domain, manage member access, and understand plan limits.

Single sign-on (SSO) lets members sign in to a ChatGPT Business workspace through your identity provider. Standalone Business workspaces continue to use their existing ChatGPT workspace settings. If those settings are editable, a workspace owner can complete the setup below. If they are read-only or show **Cloud Console ↗**, ask a global admin to manage the existing shared connection in Admin Console. Do not create a second connection.

For tenant-managed identity settings, see: [Managing your tenant in Admin Console](https://help.openai.com/articles/12289294).

For an overview of accounts, tenants, and product access, see: [Getting started with OpenAI identity and access for managed workspaces](https://help.openai.com/articles/9047883).

# Check what you need

Before you begin, make sure:

* Your ChatGPT Business subscription is active.
* You are a workspace owner.
* You can verify an email domain used by your members.
* You can access the identity provider you plan to connect.

SSO and domain verification are included with ChatGPT Business. Business supports Security Assertion Markup Language (SAML) and OpenID Connect (OIDC).

# Set up SSO for your Business workspace

1. Sign in to your ChatGPT Business workspace as a workspace owner.
2. Open **Workspace settings > Identity & access**, then select **Identity & provisioning**.
3. Confirm that the domain and SSO settings are editable before continuing.
4. Under **Verified Domains**, add and verify an email domain used by your members.
5. Under **Single Sign-On (SSO)**, select **Set up SSO** and choose a supported SAML or OIDC option.
6. Configure the identity-provider application using the values shown for your workspace.
7. Assign a test user in your identity provider and confirm that they can sign in.
8. Invite members using the email addresses associated with their identity-provider accounts.

For DNS records, verification timing, and domain conflicts, see: [Verifying your domain for OpenAI identity](https://help.openai.com/articles/8871611). A ChatGPT Business workspace can verify more than one email domain.

# Understand Business access and plan limits

SSO controls how someone signs in; it does not invite them to your workspace or grant access to another ChatGPT workspace, an API organization, or an Ads account. Workspace owners or admins must manage invitations, members, and available seats separately in ChatGPT.

To invite contractors or collaborators from another domain, a workspace owner can turn on **Allow External Domain Invites**. Workspace owners or admins can then invite them. This setting affects new invitations only.

If your workspace requires SSO, that requirement applies to email domains covered by its sign-in policy. Invited members from other domains may still use another permitted sign-in method.

A standalone ChatGPT Business plan does not include SCIM, synchronized groups, or automatic directory provisioning. When available, **Enable automatic account creation** can add eligible members after they sign in with a verified-domain email. This setting is separate from SCIM and does not require SSO.

Automatic account creation does not reactivate a removed or deactivated membership; a workspace owner or admin must invite the person again. If the same verified domain is mapped to multiple workspaces, automatic account creation may invite the person to more than one workspace. Review each workspace’s settings before enabling it.

If your tenant also has an eligible ChatGPT Enterprise workspace, ask a global admin whether your Business workspace is available under Product access for supported group assignments. Continue managing Business workspace members in ChatGPT. For tenant-wide directory setup and supported group assignments, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

# Protect existing accounts and administrator access

Invite each person using the email address already associated with their OpenAI account. Signing in through SSO with the same email preserves the existing account and chat history. A different identity-provider email can create a separate account or make existing chat history appear missing.

ChatGPT Business admins cannot require someone to merge or delete a personal workspace. For existing accounts and subscriptions, see: [Onboarding employees with existing ChatGPT accounts](https://help.openai.com/articles/10479654).

Before changing sign-in requirements, confirm that another authorized workspace owner or approved recovery method is available. Transfer ownership before the only owner leaves, and renew signing certificates before they expire. If an SSO failure locks everyone out, contact OpenAI Support for help restoring access.

If you upgrade to Enterprise or cancel your Business subscription, review the migration and available sign-in methods with your account team before changing domains or account access.

# Resolve a sign-in or domain issue

If a domain is already verified by another workspace or tenant, contact your IT team, OpenAI account team, or OpenAI Support before changing an existing connection.

If someone cannot sign in, check the invitation email, identity-provider assignment, verified domain, and workspace membership.

For additional errors, see: [Troubleshooting SSO, workspace access, and domain verification](https://help.openai.com/articles/10489721).

For shared tenant identity, see: [Single sign-on (SSO) setup for OpenAI products](https://help.openai.com/articles/9534785).

────────────────────────────────────────────────────────────
