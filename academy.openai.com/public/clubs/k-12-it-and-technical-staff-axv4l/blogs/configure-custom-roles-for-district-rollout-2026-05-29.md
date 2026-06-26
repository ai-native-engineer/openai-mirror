<!-- source: https://academy.openai.com/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/configure-custom-roles-for-district-rollout-2026-05-29 -->

[K-12 IT & Technical Staff](/en/public/clubs/k-12-it-and-technical-staff-axv4l/overview)

[navigation.content](/en/public/clubs/k-12-it-and-technical-staff-axv4l/content)

Article

May 29, 2026

# Configure Custom Roles for District Rollout

![Configure Custom Roles for District Rollout](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/configure-custom-roles-for-district-rollout-c1d66ba9-b753-4daf-a8b5-3bcc2b20b3f0-1780074794513.jpeg?fit=scale-down&width=1200)

# K-12 Admins - Getting Started

## Use custom roles when a group needs more access than the default workspace settings

![Configure Custom Roles for District Rollout](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/configure-custom-roles-for-district-rollout-c1d66ba9-b753-4daf-a8b5-3bcc2b20b3f0-1780074794513.jpeg?fit=scale-down&width=1200)

Use custom roles when a group needs more access than the default workspace settings. Keep the default workspace role conservative, then add narrowly scoped roles for publishing, advanced access, app access, and testing.

This article answers two questions for district IT and instructional technology teams:

1. What custom roles should we create?

2. How do we manage governance as usage grows across the district?

## Default Workspace Role

Most teachers and staff should stay in the default workspace role. This role should support everyday teaching, planning, collaboration, and approved classroom workflows without giving every user district-wide publishing or advanced administrative permissions.

Recommended default settings to turn on:

- Create/manage own GPTs

- Use approved skills

- Users use approved projects and workspace settings

Recommended default settings to turn off:

- Workspace-wide GPT publishing is off for general users.

- External GPT publishing is off for general users.

- Third-party GPTs require owner approval.

## Create These Custom Roles

Create a small set of custom roles that you are able to manage effectively to provide access to the right features for the right groups of people. Some examples of roles common in successful rollouts:

1. Agent/GPT Publishers

Purpose: Small group of trusted members to publish agents and GPTs for the district workspace.

|  |  |  |
| --- | --- | --- |
| Ideal Profile | Settings to turn ON | Settings to turn OFF  ﻿ |
| * Instructional Tech Leads  * Curriculum Leaders  * Central Office Teams | * Create and manage GPTs  * Publish GPTs to workspace  * Enable agent building  * Enable agent sharing  * Enable agent publishing | * Unrestricted third-party GPT access  * Publish GPTs externally |

|  |
| --- |
| Recommendation: This role prevents the workspace GPT directory from becoming crowded with one-off personal tools. Teachers can still create GPTs for themselves, while only approved publishers can place GPTs in front of the whole district. |

2. Skills Publishers

Purpose: Let a trusted group publish reusable skills across the workspace.

|  |  |
| --- | --- |
| Ideal Profile | Settings to turn ON |
| * Instructional Tech Leads  * Curriculum Teams creating repeatable workflows  * Central Office Staff | * Use skills  * Create skills  * Publish or install skills for workspace |

|  |
| --- |
| Recommendation: Skills should be tested individually before they are shared broadly. Publish only skills that solve repeatable district workflows, such as formatting district communications, converting reports into classroom resources, or applying approved templates. |

3. Advanced Access Pilot Group

Purpose: Give a limited group access to higher-credit or advanced features for evaluation and high-value workflows.

|  |  |
| --- | --- |
| Ideal Profile | Settings for role (choose what’s most appropriate) |
| * Pilot teacher group  * Curriculum designers  * Technical staff  * Approved power users | * Turn on any advanced model access  * Higher credits  * Early access testing  * Advanced apps  * New connectors |

|  |
| --- |
| Recommendation: Set a review date for the test role and determine whether default permissions need to change. Do not let pilot access become permanent by accident. |

Other Useful Roles

You may need more specialized role types beyond those above:

|  |  |  |
| --- | --- | --- |
| Type | When to Use | Examples |
| App Access Groups | Connected apps should be used only by a subset of users | - App Access - Google Drive Curriculum.  - App Access - SharePoint Policy Library.  - App Access - Box Operations. |
| School/Department Publisher Groups | When schools or departments are maintaining local GPTs, agents, or skills | - High School GPT Publishers.  - Curriculum Skills Publishers.  - Student Support Agent Publisher |

Note for All Custom Roles

|  |
| --- |
| Custom roles do not inherit default workspace settings. Treat every custom role as a full permission set, not a small add-on. |

Checklist for custom roles:

* Clear owner

* Specific purpose

* Mapped to a group (ideally SCIM-managed)

* Correct credit limit applied

* Keeps the permissions the user still needs

If a user belongs to multiple custom roles, the permissions can combine. For credit limits, the user receives the more generous limit.

Blog

[K-12 District Workspace Launch Checklist](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-district-workspace-launch-checklist-2026-05-29)

May 29th, 2026 • Views 101

Blog

[Manage Connected Applications in ChatGPT](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/manage-connected-applications-in-chatgpt-2026-05-29)

May 29th, 2026 • Views 173

Blog

[Set Up SSO, SCIM, and Groups for ChatGPT EDU](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/set-up-sso-scim-and-groups-for-chatgpt-edu-2026-05-29)

May 29th, 2026 • Views 101

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo • May 12th, 2025 • Views 8.8K

Blog

[K-12 District Workspace Launch Checklist](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-district-workspace-launch-checklist-2026-05-29)

May 29th, 2026 • Views 101

Blog

[Set Up SSO, SCIM, and Groups for ChatGPT EDU](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/set-up-sso-scim-and-groups-for-chatgpt-edu-2026-05-29)

May 29th, 2026 • Views 101

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo • May 12th, 2025 • Views 8.8K

Blog

[Manage Connected Applications in ChatGPT](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/manage-connected-applications-in-chatgpt-2026-05-29)

May 29th, 2026 • Views 173
