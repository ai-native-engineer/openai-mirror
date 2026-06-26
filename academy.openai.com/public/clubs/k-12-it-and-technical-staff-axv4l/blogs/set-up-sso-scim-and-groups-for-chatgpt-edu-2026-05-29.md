<!-- source: https://academy.openai.com/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/set-up-sso-scim-and-groups-for-chatgpt-edu-2026-05-29 -->

[K-12 IT & Technical Staff](/en/public/clubs/k-12-it-and-technical-staff-axv4l/overview)

[navigation.content](/en/public/clubs/k-12-it-and-technical-staff-axv4l/content)

Article

May 29, 2026

# Set Up SSO, SCIM, and Groups for ChatGPT EDU

![Set Up SSO, SCIM, and Groups for ChatGPT EDU](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/set-up-sso-scim-and-groups-for-chatgpt-edu-02afd621-6cc8-4913-bb7a-db9f18fecd73-1780074486564.jpeg?fit=scale-down&width=1200)

# K-12 Admins - Getting Started

## Use this guide to connect ChatGPT for EDU to your district identity systems

![Set Up SSO, SCIM, and Groups for ChatGPT EDU](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/set-up-sso-scim-and-groups-for-chatgpt-edu-02afd621-6cc8-4913-bb7a-db9f18fecd73-1780074486564.jpeg?fit=scale-down&width=1200)

Use this guide to connect ChatGPT for EDU to your district identity systems. The goal is to make access reliable at launch and easier to manage over time.

Audience: District IT administrators who manage identity, provisioning, domains, and access groups.

## District Identity Plan

For district-wide rollout, use centralized identity and provisioning in the following steps:

1. Verify Domain

2. Configure SSO

3. Set up SCIM Directory Sync

4. Push groups from the identity provider into ChatGPT.

5. Map groups to custom roles

## 1. Verify The District Domain

Domain verification confirms that your district controls the email domain and enables ChatGPT to route eligible users into your district-managed workspace.

* In Workspace Settings, go to Identity and Access.

* Add the district email domain you want to verify.

* ChatGPT will generate a DNS TXT record for that domain.

* Send the DNS TXT record to the team that manages your district’s DNS.

* Once the record has been added, return to ChatGPT and verify the domain.

## 2. Configure Single Sign-On (SSO)

Once your district domain is verified, configure Single Sign-On (SSO). ChatGPT supports common identity providers, as well as custom identity provider setups.

SSO controls how users sign in to ChatGPT. It should be treated as an authentication step, not a method for automatically adding users to the workspace.

1. In your workspace settings, begin configuring SSO with your district’s identity provider.

2. Start with a small group of invited test users.

3. Leave SSO enforcement turned off while testing the sign-in flow.

4. Confirm that each test user can successfully sign in to the workspace.

5. Turn on SSO enforcement only after testing is complete and your district is ready to require SSO for eligible users.

SSO applies to users associated with the verified domain who have been invited or provisioned into the managed workspace. It does not automatically apply to users who have not been added to the workspace.

## 3. Configure SCIM Directory Sync

Use SCIM for inviting users throughout your district to the workspace. SCIM is the recommended path because it supports both provisioning and deprovisioning.

Set up SCIM as a separate application from SSO in your identity provider. For example, if your district uses Microsoft Entra ID, you may have one app for SSO and a separate app for SCIM.

SCIM can push:

* Users.

* Group memberships.

* Changes when users are added or removed.

|  |
| --- |
| Note on Automatic Creation    Automatic account creation can bring users into the workspace when they create an account with a verified district domain. This can be useful in some contexts, but it does not provide automatic deprovisioning. For district-managed rollout, use SCIM instead of combining SCIM with automatic account creation. Running both can create contention and make access harder to manage.  ﻿ |

## 4. Push Groups From The Identity Provider

Create the important access groups in your identity provider first, then push them through SCIM. This keeps group membership tied to your central source of truth. Groups are useful since Administrators can map groups to custom roles and control app access.

Use names that make the purpose clear to both IT and workspace administrators.

|  |
| --- |
| Note on Local Groups  Local groups can be created directly in ChatGPT. They are useful for pilots, alpha-feature testing, or quick validation when you do not want to change the identity provider yet.  Do not use local groups as the main district access model. If a local group later becomes a SCIM-managed group, you may end up with duplicate group structures. Move long-term groups into the identity provider when they become part of the official rollout. |

## 5. Map Groups to Custom Roles

After groups appear in ChatGPT, map them to custom roles. Custom roles should be used for additional permissions, such as:

* Publishing GPTs to the workspace

* Publishing skills to the workspace

* Advanced model access

* Special app access

* Codex access

* Higher credit limits for a specific group

Default workspace settings should remain the baseline, whereas custom roles should be assigned only to groups that need extra permissions. Learn more about Role-Based Access Controls [here](https://help.openai.com/en/articles/11750701-rbac).

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo • May 12th, 2025 • Views 8.8K

Blog

[K-12 District Workspace Launch Checklist](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-district-workspace-launch-checklist-2026-05-29)

May 29th, 2026 • Views 101

Blog

[Manage Connected Applications in ChatGPT](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/manage-connected-applications-in-chatgpt-2026-05-29)

May 29th, 2026 • Views 173

Blog

[Configure Custom Roles for District Rollout](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/configure-custom-roles-for-district-rollout-2026-05-29)

May 29th, 2026 • Views 81

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo • May 12th, 2025 • Views 8.8K

Blog

[Manage Connected Applications in ChatGPT](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/manage-connected-applications-in-chatgpt-2026-05-29)

May 29th, 2026 • Views 173

Blog

[Configure Custom Roles for District Rollout](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/configure-custom-roles-for-district-rollout-2026-05-29)

May 29th, 2026 • Views 81

Blog

[K-12 District Workspace Launch Checklist](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-district-workspace-launch-checklist-2026-05-29)

May 29th, 2026 • Views 101
