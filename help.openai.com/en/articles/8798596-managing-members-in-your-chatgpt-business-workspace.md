<!-- source: https://help.openai.com/en/articles/8798596-managing-members-in-your-chatgpt-business-workspace -->

# Managing members, seat types, and roles in ChatGPT Business

Learn how to access your workspace, switch between workspaces, manage members, roles, and seat types, and use workspace discovery in ChatGPT Business.

Updated: 1 hour ago

***Note:*** *Starting June 24, 2026, Codex seats will no longer be available to new ChatGPT Business plans, or to Business workspaces that never added a Codex seat prior to June 24 2026. Business workspaces that had added a Codex seat prior to June 24, 2026, including pending invites as of June 24 can continue to manage and add usage-based Codex seats.*

## Overview

A workspace is a unique ChatGPT environment with its own settings, members, and resources.   
  
Personal workspaces are tied to existing ChatGPT accounts, and contain chats, memory, context, apps, and other ChatGPT features specific to the user. Similarly, organizations can set up workspaces for their ChatGPT Business accounts, containing information, features, and context applicable to the organization and its members.   
  
Users can join a ChatGPT Business workspace by invite, and have the option of keeping their personal and Business workspaces separate, or merge them. New users who do not have ChatGPT accounts will have one created for them as a part of joining the ChatGPT Business workspace.   
  
When logging into their ChatGPT accounts, users can select which workspace is active for the current session. On ChatGPT web, workspaces are available from the **profile menu**. On mobile, workspaces are available in the sidebar.

## Managing ChatGPT Business Workspaces

ChatGPT Business management is built around two key concepts: **roles** and **seats**. There are three different roles in a ChatGPT Business workspace:

* **Owners** have full access, including billing, identity management, and workspace configuration, and can invite other roles, including additional owners.
* **Admins** help manage users and groups and perform routine administrative tasks.
* **Members** can fully use ChatGPT and create GPTs but have no admin privileges.

Each role has a set of permissions that allow modification of workspace settings. Owners and admins are the most permissive role type, while members and analytics viewers have a limited set of permissions.   
  
ChatGPT Business workspaces feature two types of seats - standard ChatGPT seats and Codex seats.  
  
A Business workspace that had a Codex seat before June 24, 2026, can include only standard ChatGPT seats, only Codex seats, or a mix of both. New self-serve Business workspaces cannot add a first Codex seat. Each seat type determines what a user can access, and seats can be assigned to any role. Read more about seat types [here](/en/articles/8792828-what-is-chatgpt-business).  
  
Review the table below for a high level overview of permissions by role.

| **Capability** | **Analytics Viewer** | **Member** | **Admin** | **Owner** |
| --- | --- | --- | --- | --- |
| [Core chat functionality](https://chat.openai.com/) | ✔️ | ✔️ | ✔️ | ✔️ |
| View [all users](https://chatgpt.com/admin) | ✔️ | ✔️ | ✔️ | ✔️ |
| View [workspace analytics](https://help.openai.com/articles/10875114) | ✔️ |  | ✔️ | ✔️ |
| [Invite new Members](https://chat.openai.com/admin) |  | ✔️ | ✔️ | ✔️ |
| Switch user [seat type](https://chatgpt.com/admin/billing) |  |  | ✔️ | ✔️ |
| [Invite new Admins/Owners](https://chat.openai.com/admin) |  |  |  | ✔️ |
| [Cancel an invitation](https://chat.openai.com/admin) |  |  | ✔️ | ✔️ |
| [Remove a user](https://chat.openai.com/admin) |  |  | ✔️ | ✔️ |
| [Modify a user’s role](https://chat.openai.com/admin) |  |  |  | ✔️ |
| View [Groups](https://chatgpt.com/admin/groups) | ✔️ | ✔️ | ✔️ | ✔️ |
| Manage [Groups](https://chat.openai.com/admin/groups) |  |  | ✔️ | ✔️ |
| View plan information in [Billing](https://chat.openai.com/admin/billing) |  |  | ✔️ | ✔️ |
| View invoices in [Billing](https://chat.openai.com/admin/billing) |  |  |  | ✔️ |
| Set spend [controls](https://chatgpt.com/admin/billing) |  |  | ✔️ | ✔️ |
| View and manage [Identity & Provisioning](https://chat.openai.com/admin/identity) |  |  |  | ✔️ |
| View and manage [Workspace settings](https://chat.openai.com/admin/settings) |  |  | ✔️ | ✔️ |
| [Create a GPT](https://chat.openai.com/gpts/editor) | ✔️ | ✔️ | ✔️ | ✔️ |
| View and manage [GPT settings](https://chat.openai.com/admin/gpts) |  |  |  | ✔️ |
| View and Manage [Apps](https://chatgpt.com/admin/ca) |  |  | ✔️ | ✔️ |

Users can move between ChatGPT Business workspaces they are a part of, and their personal workspace by using the workspace switcher.  
  
The rest of this article focuses on member and workspace management. To learn more about switching seat types, merging personal and Business workspaces, and other workspace migration topics, refer to our article: [Managing workspace lifecycle and migration in ChatGPT Business](/en/articles/8801890)

## Managing ChatGPT Business memberships

### Invite members

Anyone you invite should be an intended, ongoing member of your team. Business workspaces are designed for consistent, collaborative use within an organization. Misuse of seat assignments in violation of the Services Agreement may lead to workspace deactivation or account suspension.  
  
Codex is available as a seat type for new invites only in Business workspaces that had a Codex seat before June 24, 2026.

* Go to the Business workspace.
* Go to **Workspace settings > Members**.
* Select **Invite member**.
* Import a CSV file or manually enter email addresses.
* Choose the role and seat type for each invite.
* Review the default seat type if your workspace uses one, then send the invites.

To add members in bulk, use a CSV with this format:

```
email,role,seat type  
  
For example:  
  
user1@company.com,member,Codex  
analyst1@company.com,member,ChatGPT  
admin@company.com,admin,Codex  
it@company.com,owner,ChatGPT
```

Accepted values for role and seat\_type listed below. Note that values are **case insensitive.**

|  |  |
| --- | --- |
| role | member, admin, owner |
| seat type | ChatGPT, Codex |

If a role is omitted, unrecognized, or unavailable to the person uploading the CSV, that user is added as a member. If seat type is omitted, the default seat type is used.

### Manage pending invites and join requests

Pending invites and join requests should show the selected seat type alongside the user record. Only admins and owners can approve or manage pending requests.

* Go to **Workspace settings > Members**.
* Open the **Invites** or **Requests** view, depending on what you want to review.
* Review the pending user, role, and seat type.
* Approve, resend, edit, or reject the item as needed.

### Change member roles

Only Owners can change member roles.

* Go to **Workspace settings > Members**.
* Find the member you want to update.
* Select the current role in the **Role** column.
* Select the new role.

### Change member seat types

Only owners can change member seat types.

***Note:*** *Starting June 24, 2026, Codex seats will no longer be available to new ChatGPT Business plans, or to Business workspaces that never added a Codex seat prior to June 24 2026. Business workspaces that had added a Codex seat prior to June 24, 2026, including pending invites as of June 24 can continue to manage and add usage-based Codex seats.*

* Go to **Workspace settings > Members**.
* Find the member you want to update.
* Select the current value in the **Seat type** column.
* Select the new seat type and confirm the change.

If you change a user from a standard ChatGPT seat to a Codex seat, review the loss of ChatGPT workspace access before confirming.  
  
Standard ChatGPT seats are subject to a 2-seat minimum per workspace. When you add your first standard ChatGPT seat to a Codex-only workspace, you will be prompted to purchase 2 seats, using the saved payment method.  
  
If your Business workspace had a Codex seat before June 24, 2026, you can add additional Codex seats. If the workspace currently has only standard ChatGPT seats, you will be prompted to purchase credits for Codex usage using your saved payment method. [Read more.](/en/articles/8792536?preview)

### Remove members

Owners and admins can remove members from the **Members** list.

* Go to **Workspace settings > Members**.
* Find the member you want to remove.
* Select the **more options menu (•••)**.
* Select **Remove member**.

### Default seat types for new members

Workspace owners can set a default seat type for new members joining the workspace. Set the default by accessing **Workspace settings →** [**Identity & access**](https://chatgpt.com/admin/identity)**.** For workspaces created before April 2, 2026, by default the default seat type is a standard ChatGPT seat.  
  
For workspaces created from April 2 through June 23, 2026, the default seat type is based on the initial seat purchase type.

* If initial seats purchased were Codex, the default seat type is Codex seats.
* If initial seats purchased were standard, the default seat type is standard ChatGPT seats.

For new self-serve Business workspaces created on or after June 24, 2026, the default seat type is a standard ChatGPT seat.  
  
Any member that joins a workspace will be assigned to the default seat type unless overridden. Only workspace owners can change the seat type applied to a member.

### Changing the default workspace seat type

Owners can change the default workspace seat type via **Workspace settings**.  
  
Codex can be selected as the default only in Business workspaces that had a Codex seat before June 24, 2026.

* Go to **Workspace settings →** [**Identity & access**](https://chatgpt.com/admin/identity).
* Under **User provisioning**, change the default seat type

## Workspace discovery in ChatGPT Business

Workspace discovery helps people at your company find and join your ChatGPT workspace using a verified email address on your domain. This reduces manual onboarding and gets new teammates working in ChatGPT faster. Admins and owners control whether discovery is available, how the workspace appears, and who can join, from **Workspace settings →** [**Identity & access**](https://chatgpt.com/admin/identity).  
  
If someone signs up with a verified company email, they can see your workspace during the join flow and submit a request to join. Admins can review join requests from **Workspace settings →** [**Members**](https://chatgpt.com/admin/members). If you want a fully automated experience, you can allow people with your company domain to join without approval.  
  
Until you customize the workspace name, new users see a generic workspace name. Updating the workspace name makes it easier for coworkers to recognize the correct workspace.  
  
For default behavior by workspace type:

* ChatGPT Business: workspace discovery is on by default.
* ChatGPT Enterprise/Edu: workspace discovery is off by default.

### Turn workspace discovery on or off

* Go to **Workspace settings →** [**Identity & access**](https://chatgpt.com/admin/identity).
* Under User Provisioning, turn **Enable workspace discovery** on or off.
* You can optionally toggle **Automatically accept join requests**

### Update the workspace name

* Go to **Workspace settings**.
* Select the pencil icon next to the workspace name.
* Update the workspace name, then save the change.

Changes to the workspace name may take time to take effect.

### Update the workspace display name

You can separately update the workspace display name to ensure new members of your organization can easily find and join the workspace. To do so:

* Go to **Workspace settings →** [**Identity & access**](https://chatgpt.com/admin/identity).
* Under User Provisioning, change the **Discoverable name**.

### Access workspace settings from Codex

If you are an admin working primarily in Codex, use the **Workspace settings** entry point in [Codex web](https://chatgpt.com/codex) to open the ChatGPT Business admin console. To return to Codex, click the **Back to Codex** link on the top left.

# FAQ

## Can I use ChatGPT Business on my phone?

Yes. ChatGPT Business is available on iPhone and Android.

## Can a workspace include both standard ChatGPT and Codex users?

Yes, if the Business workspace had a Codex seat before June 24, 2026. These workspaces can include standard ChatGPT seats, Codex seats, or both. New self-serve Business workspaces cannot add a first Codex seat.

## Can a Codex-only user use ChatGPT in the workspace?

No. A Codex-only user does not have ChatGPT workspace access. They should be redirected to Codex or shown a message that chat is not available in that workspace.

## Why does an invite or join email mention Codex instead of ChatGPT?

In a Codex-only workspace, automated emails can highlight Codex rather than ChatGPT because the invited user is receiving Codex access rather than standard ChatGPT workspace access.

## Who can join my workspace?

Anyone you invite can join as long as they are an intended, ongoing member of your team.

## Can I restrict members from adding additional members?

Members can invite other members using the default seat type - currently, it is not possible to restrict members from adding additional members. Admins/owners can manage pending invites from **Workspace settings →** [**Members**](https://chatgpt.com/admin/members)**.**

## How many members can a workspace handle?

A ChatGPT Business workspace can have a maximum of 1,000 members. A minimum of 2 ChatGPT seats are required.  
  
In a Business workspace that had a Codex seat before June 24, 2026, there is no minimum number of Codex seats. New self-serve Business workspaces cannot add a first Codex seat.  
  
If you are considering setting up a ChatGPT Business workspace of more than 250 members, or you need even larger deployments, consider [ChatGPT Enterprise](/en/articles/8265053-what-is-chatgpt-enterprise).
