<!-- source: https://academy.openai.com/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/manage-connected-applications-in-chatgpt-2026-05-29 -->

[K-12 IT & Technical Staff](/en/public/clubs/k-12-it-and-technical-staff-axv4l/overview)

[navigation.content](/en/public/clubs/k-12-it-and-technical-staff-axv4l/content)

Article

May 29, 2026

# Manage Connected Applications in ChatGPT

![Manage Connected Applications in ChatGPT](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/manage-connected-applications-in-chatgpt-a0e0db73-5ad2-41fd-8250-17bef00fa7e8-1780075499762.jpeg?fit=scale-down&width=1200)

# K-12 Admins - Getting Started

## Decide the apps ChatGPT can connect to

![Manage Connected Applications in ChatGPT](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/manage-connected-applications-in-chatgpt-a0e0db73-5ad2-41fd-8250-17bef00fa7e8-1780075499762.jpeg?fit=scale-down&width=1200)

## Decide What ChatGPT Can Connect To

Apps allow ChatGPT to retrieve information and write back to tools such as Google Drive, Outlook, Gmail, SharePoint, Box, Dropbox, Asana, or other connected tools. This lets users work with the files, messages, and project context they already rely on, so ChatGPT can give more relevant answers and help complete tasks without switching tools.

Turning on an app in the admin settings makes it available to the selected users or roles. For most apps, the end user still needs to authenticate to their own account before ChatGPT can start retrieving content.

## Review App Access Before Enabling

Before enabling an app, review:

* The users/roles that should see an app

* The actions the app can perform.

* Whether the app is read-only or can take action.

* Whether the source system contains sensitive district information.

* The availability of syncing.

* The ability to use an app within a GPT or agent.

App data pulled into ChatGPT is treated like workspace conversation data under the district’s OpenAI agreement. It is not used to train OpenAI models.

## Use Role-Based App Access

Apps can be made available to the whole workspace or to specific custom roles. Use role-based access when an app should be limited to a smaller group.

Examples:

* Give curriculum teams access to a curriculum content store.

* Give central office staff access to a policy document repository.

* Limit sensitive operational systems to specific approved roles.

* Keep pilot apps available only to a test group.

If a user belongs to a custom role that does not include an app, they may not see that app even if other workspace users do.

## Review App Actions

Many apps expose specific actions, such as search, fetch, profile, or recent files. Workspace owners can review and disable actions that are not appropriate.

For example, if recent-file listing is not needed, disable it and leave search or fetch available. This gives the district more granular control over how ChatGPT interacts with connected systems.

## Decide Whether To Enable Sync

Some apps support sync. When sync is enabled, ChatGPT can index information the user has access to so retrieval is faster and more specific.

If sync is not enabled, ChatGPT makes a one-time request to the connected system when the user asks for information.

|  |  |
| --- | --- |
| Use Sync When | Avoid Sync When |
| * Faster retrieval matters.  * The content source is approved for indexing.  * The district understands what content is included.  ﻿ | * The source contains highly sensitive information.  * The app is still being piloted.  * The district has not completed data governance review. |

## Apps Inside GPTs and Projects

Apps can also be made available inside projects and custom GPTs. This is useful when a district GPT needs to retrieve approved content from a specific source.

Example: A district policy assistant could use approved documents in SharePoint to answer staff questions from current district policy documents.

Before enabling apps inside GPTs, confirm:

* The GPT has a clear purpose.

* The app source is approved.

* The GPT is shared only with the right audience.

* The GPT does not use unapproved actions or domains.

Blog

[Set Up SSO, SCIM, and Groups for ChatGPT EDU](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/set-up-sso-scim-and-groups-for-chatgpt-edu-2026-05-29)

May 29th, 2026 • Views 101

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo • May 12th, 2025 • Views 8.8K

Blog

[Configure Custom Roles for District Rollout](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/configure-custom-roles-for-district-rollout-2026-05-29)

May 29th, 2026 • Views 81

Blog

[K-12 District Workspace Launch Checklist](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-district-workspace-launch-checklist-2026-05-29)

May 29th, 2026 • Views 101

Blog

[Set Up SSO, SCIM, and Groups for ChatGPT EDU](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/set-up-sso-scim-and-groups-for-chatgpt-edu-2026-05-29)

May 29th, 2026 • Views 101

Blog

[Configure Custom Roles for District Rollout](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/configure-custom-roles-for-district-rollout-2026-05-29)

May 29th, 2026 • Views 81

Blog

[K-12 District Workspace Launch Checklist](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-district-workspace-launch-checklist-2026-05-29)

May 29th, 2026 • Views 101

Blog

[K-12: Prompt Pack for IT Staff (Technology Directors, Coordinators, and Support Teams)](/en/public/clubs/k-12-it-and-technical-staff-axv4l/blogs/k-12-prompt-pack-for-it-staff)

By Juliann Igo • May 12th, 2025 • Views 8.8K
