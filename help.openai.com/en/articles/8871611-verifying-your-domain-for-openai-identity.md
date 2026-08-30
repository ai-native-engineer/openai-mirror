<!-- source: https://help.openai.com/en/articles/8871611-verifying-your-domain-for-openai-identity -->

# Verifying your domain for OpenAI identity

Learn how to verify a company or school domain, review where it applies, and avoid sign-in conflicts.

Domain verification confirms that your company or institution controls an email domain. A verified domain can support your tenant’s identity settings and single sign-on (SSO).

Verifying a domain does not automatically enable SSO, invite users, configure System for Cross-domain Identity Management (SCIM), or give someone access to a ChatGPT workspace, API Platform organization, or Ads account.

Domain verification can also support a GPT Builder Profile that uses a verified website. It does not give a personal ChatGPT account permission to create or publish new GPTs. For builder-profile requirements, see: [Sharing and publishing GPTs](https://help.openai.com/articles/8798878).

# Check your tenant before you start

Before verifying a domain, identify:

* The tenant that should manage the domain and its identity settings.
* A global admin for a tenant-managed domain or a workspace owner for a standalone ChatGPT Business workspace.
* The DNS administrator who can add a public TXT record.
* Existing ChatGPT workspaces, API organizations, Ads accounts, and users associated with the domain.
* Any active SSO connection, existing account-migration policy, or administrator recovery method.

If another tenant already verified the domain, contact your account team or OpenAI Support before trying to remove it or change sign-in settings.

For a standalone ChatGPT Business workspace, a workspace owner can verify the domain under **Identity & access** in ChatGPT. If the settings are read-only or show **Cloud Console ↗**, ask a global admin to manage the shared tenant domain.

# Verify a domain in Admin Console

1. Sign in to Admin Console with an account that has the required global admin permissions.
2. Select the tenant that should manage the domain.
3. Open **Global settings** > **Access** > **Domains**.
4. Select **Add domain**. An earlier Admin Console view may show **Add Domain**.
5. Enter the exact domain or subdomain your company or school controls, then select **Add**.
6. Copy the DNS TXT verification value shown by OpenAI.
7. At your DNS provider, create a TXT record with that value. Set the record name to @, or leave it blank if your provider requires that.
8. Return to Admin Console, select **Check Domain**, and confirm that the domain shows **Verified**.

OpenAI must be able to read the TXT record through public DNS. DNS propagation can take up to 24 hours. If a verification attempt expires before you finish, start a new attempt and complete it within the new 7-day window. A completed domain verification does not expire.

![Verify your domain dialog showing the DNS TXT name and verification value, with a Check Domain button.](https://images.ctfassets.net/j22is2dtoxu1/lbas_img_2pBsrAz7PpSWLDYAVPOqNY_rwTQQ651WJBjqBahk5uk/6568a306997daa252c43291d46c4d1bc/lbas_img_2pBsrAz7PpSWLDYAVPOqNY_rwTQQ651WJBjqBahk5uk.jpg?q=80&fm=webp&w=550)

Some customers need OpenAI Support to verify a domain. If the add (+) button is unavailable, or your company or school cannot publish the required TXT record, contact your OpenAI account team or Support.

If a standalone ChatGPT Business workspace manages its own identity, a workspace owner can complete the equivalent steps under **Identity & access** in ChatGPT. The final verification button may be labeled **Check**. For Business-specific instructions, see: [Setting up single sign-on for ChatGPT Business](https://help.openai.com/articles/11489188).

# Review where the verified domain applies

In **Global settings**, open **Access** > **Domains** to review which products are associated with the verified domain. A newly verified domain can initially apply to all eligible ChatGPT workspaces and API organizations.

1. Open the menu for the verified domain and select **Manage eligibility**.
2. Choose whether the domain applies to all eligible workspaces and API organizations or to selected ChatGPT workspaces.
3. Review whether **All API Orgs** is selected. Domain eligibility applies to API organizations together, not to one API organization at a time.
4. Select **Save** after confirming that the resulting access matches your intended settings.

Review domain eligibility before you enforce SSO, change onboarding settings, or invite users. A verified domain and an active identity-provider connection do not automatically grant membership in any product.

# Understand sign-in and account impacts

A domain generally can be verified for only one tenant. Connected ChatGPT workspaces and API organizations should use the tenant where the domain is already verified. If another tenant has verified it, contact OpenAI Support instead of creating a replacement tenant or changing a working identity-provider connection.

Verifying a work domain does not delete an existing personal ChatGPT workspace or merge its chats. Before changing sign-in policies, review how existing work-email accounts and product memberships could be affected.

Domain verification and domain claiming are different. Verifying a domain does not claim it. Domain claiming is available only for approved use cases and requires a separate request through OpenAI Support or your account team.

A parent domain does not automatically verify its subdomains. Verify each exact email domain used by your identity provider or product.

If an eligible workspace-level SCIM connection supports changing a managed user’s email address, verify both the old and new email domains for the same ChatGPT workspace and its tenant. Tenant-wide SCIM cannot change existing account email addresses. SCIM remains a separate setup from SSO and domain verification.

For users who already have personal or work accounts, see: [Onboarding employees with existing ChatGPT accounts](https://help.openai.com/articles/10479654).

To configure sign-in after verifying your domain, see: [Single sign-on (SSO) setup for OpenAI products](https://help.openai.com/articles/9534785).

# Resolve a domain verification issue

* If the TXT record cannot be found, confirm that its name and value exactly match the instructions in Admin Console.
* If the record was added recently, allow time for public DNS propagation and select **Check Domain** again.
* If the domain is already verified, ask whether another tenant has verified it before changing existing settings.
* If a subdomain is not recognized, verify that specific subdomain rather than assuming its parent domain covers it.
* If people cannot sign in after a domain change, check the selected tenant, domain eligibility, identity-provider assignment, SSO policy, and product membership.

For sign-in errors and additional recovery steps, see: [Troubleshooting SSO, workspace access, and domain verification](https://help.openai.com/articles/10489721).

If your company or school cannot complete verification or recover access, contact [OpenAI Support](https://help.openai.com/articles/6614161).

────────────────────────────────────────────────────────────
