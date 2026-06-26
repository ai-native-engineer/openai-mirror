<!-- source: https://academy.openai.com/public/clubs/admins-6o6xf/resources/inviting-and-managing-your-team -->

[Admins](/en/public/clubs/admins-6o6xf/overview)

[navigation.content](/en/public/clubs/admins-6o6xf/content)

Article

July 8, 2025 · Last updated on June 1, 2026

# Inviting and managing your team

![Inviting and managing your team](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-10--32d896ee-286a-4cc8-9eeb-5a045412d7ca-1754316122967.jpeg?fit=scale-down&width=1200)

# Leaders & Admins

# Foundations

## Learn how to manage user access.

![Inviting and managing your team](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Admins-Cover-Images-10--32d896ee-286a-4cc8-9eeb-5a045412d7ca-1754316122967.jpeg?fit=scale-down&width=1200)

## **Inviting and managing your team**

### **Roles and permissions**

In both ChatGPT Enterprise and ChatGPT Business, there are three roles: **Owner, Admin, and Member**.

* **Owners** have full control over the workspace, including billing, settings, and identity management. They can invite or assign Admins/Owners, manage all available organization-wide settings, and access billing details.

* **Admins** can manage users (e.g. invite/remove members), as well as manage some organization-wide settings, like Connectors. Enterprise Admins can also organize users into groups and view usage analytics.

* **Members** are end-users who can use ChatGPT and create custom GPTs (provided that you workspace owner allows it). In ChatGPT Business, they can also invite or remove other members -  whereas ChatGPT Enterprise restricts user management to Admins/Owners for tighter control.

See more about roles in [ChatGPT Enterprise](https://help.openai.com/en/articles/8266431-what-is-the-difference-between-different-roles-on-my-chatgpt-enterprise-workspace) and [ChatGPT Business](https://help.openai.com/en/articles/8798607-what-roles-are-there-in-a-chatgpt-team-workspace).

### **User access and onboarding strategy**

Decide how employees will be added to the ChatGPT workspace and how they'll log in.
**Enable single sign-on:** Enabling SSO lets users log in with corporate credentials and enforces your organization’s authentication policies.. This simplifies user login and improves security. Decide on this early so you can configure SSO and test before org-wide onboarding.

* ﻿[Guide: Setting up Single Sign On](https://help.openai.com/en/articles/9534785-configuring-sso-for-chatgpt-enterprise)﻿

* ﻿[SCIM integration](https://help.openai.com/en/articles/9627404-openai-scim-integration-faq): Automate the provisioning and deprovisioning of user accounts in ChatGPT Enterprise with [supported IDPs](https://help.openai.com/en/articles/9627404-openai-scim-integration-faq) or custom SCIM implementations.

* Reach out to **[[email protected]](/cdn-cgi/l/email-protection)** with any issues or questions

**Verify your company domain:** Verifying your company’s email domain means only users with that domain can join the workspace, providing an extra layer of access control. See: [Domain Verification for ChatGPT](https://help.openai.com/en/articles/8871611-domain-verification)﻿

**Bulk user provisioning:** Decide if you will onboard users gradually or all at once. ChatGPT Business allows bulk inviting via CSV, which is useful for initial rollout. Enterprise goes further by supporting [**SCIM provisioning**](https://help.openai.com/en/articles/9627404-openai-scim-integration-faq) (automated user provisioning/de-provisioning through your identity provider).

**Merging accounts:** If some employees already use ChatGPT (Free/Plus/Pro) with a company email, decide whether to have them merge their account into the new workspace or keep it separate. Learn more about [migrating accounts to ChatGPT Business workspaces](https://help.openai.com/en/articles/8801890-can-i-migrate-or-merge-my-chatgpt-free-or-plus-workspace-over-to-my-chatgpt-team-workspace) and [migrating accounts to ChatGPT Enterprise workspaces](https://help.openai.com/en/articles/10479654-understanding-your-ideal-user-management-setup#h_41adf246c2).

**User offboarding:** Plan how you will remove users who leave the company or should no longer have access.

* In ChatGPT Business, any user can remove other users from the workspace.

* In ChatGPT Enterprise, only Admins/Owners can remove users. Decide who will be responsible for periodic audits of the member list and ensure there’s a process to promptly remove departing employees’ access. SCIM can help automate the deprovisioning process.

### **Account security and authentication**

**Enforce strong authentication:** ChatGPT supports multi-factor authentication (MFA) for added login security.  Enterprise SSO will delegate authentication security to your identity provider, so if you have MFA or conditional access policies in your IdP, those will apply. **See:** [**Enabling or disabling Multi-Factor Authentication (MFA)**](https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa).

**Compliance API:** ChatGPT Enterprise also supports audit logging via the[**Compliance API**](https://help.openai.com/en/articles/9261474-compliance-api-for-enterprise-customers) for conversations – consider using this to track logins and usage patterns as part of your security oversight.

Table Of Contents

[Data governance and compliance](/en/public/clubs/admins-6o6xf/resources/data-governance-and-compliance)

[Measuring impact and ROI](/en/public/clubs/admins-6o6xf/resources/measuring-impact-and-roi)

[Automate provisioning and unlock actionable analytics with SCIM](/en/public/clubs/admins-6o6xf/resources/scim)

[Empowering and supporting your team](/en/public/clubs/admins-6o6xf/resources/empowering-and-supporting-your-team)

Jul 5th, 2025 • Views 16K

[Planning your ChatGPT rollout](/en/public/clubs/admins-6o6xf/resources/planning-your-chatgpt-rollout)

Jul 11th, 2025 • Views 5.8K

[Communicating about ChatGPT Enterprise to your team](/en/public/clubs/admins-6o6xf/resources/team-communication)

Aug 5th, 2025 • Views 12.2K

[Feature controls and integrations with your tools](/en/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

Jul 10th, 2025 • Views 7.1K

[Empowering and supporting your team](/en/public/clubs/admins-6o6xf/resources/empowering-and-supporting-your-team)

Jul 5th, 2025 • Views 16K

[Communicating about ChatGPT Enterprise to your team](/en/public/clubs/admins-6o6xf/resources/team-communication)

Aug 5th, 2025 • Views 12.2K

[Feature controls and integrations with your tools](/en/public/clubs/admins-6o6xf/resources/feature-controls-and-integrations-with-your-tools)

Jul 10th, 2025 • Views 7.1K

[Planning your ChatGPT rollout](/en/public/clubs/admins-6o6xf/resources/planning-your-chatgpt-rollout)

Jul 11th, 2025 • Views 5.8K
