<!-- source: https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise -->

# Managing members, seat types, roles and access in ChatGPT Enterprise

Learn how to add and remove members, assign seat types and roles, and use groups to manage access in Enterprise and Edu workspaces.

Updated: 19 hours ago

**Note:** On April 2, 2026, we updated some features of the ChatGPT Enterprise plan.

* **We introduced a new seat type:** a **Codex seat** that offers codex-only access, based on flexible pricing.

  + This seat type is available to ChatGPT Enterprise plans, but not to ChatGPT [Edu](/en/articles/9377311), [Teachers](/en/articles/12844995), or [Healthcare](/en/articles/20001046) plans.
* **We updated the** [**Codex Rate Card**](/en/articles/20001106-codex-rate-card) to align with token-based usage pricing, billed in credits per million tokens.

  + As of April 23rd, the new pricing is applicable to all new and existing Enterprise, [Edu](/en/articles/9377311), [Teachers](/en/articles/12844995), and [Healthcare](/en/articles/20001046) plans.

# Overview

A workspace is a unique ChatGPT environment with its own settings, members, and resources.

Personal workspaces are tied to existing ChatGPT accounts, and contain chats, memory, context, apps, and other ChatGPT features specific to the user. Similarly, organizations can set up workspaces for their ChatGPT Enterprise accounts, containing information, features, and context applicable to the organization and its members.

Users can join a ChatGPT Enterprise workspace by invite. As a result, personal workspaces under Company's email addresses may be subject to deletion or merge into the enterprise workspace. New users who do not have ChatGPT accounts will have one created for them as a part of joining the ChatGPT Enterprise workspace.

When logging into their ChatGPT accounts, users can select which workspace is active for the current session. On ChatGPT web, workspaces are available from the profile menu. On mobile, workspaces are available in the sidebar.

# Managing ChatGPT Enterprise Workspaces

ChatGPT Enterprise workspace management is built around two key concepts:**roles** and**seats**.

Each workspace includes four built-in roles:

* **Owners** have full access, including billing, identity management, and workspace configuration, and can invite other roles, including additional owners.
* **Admins** help manage users, groups, and Codex access tokens, and perform routine administrative tasks.
* **Members** can fully use ChatGPT and create GPTs but have no admin privileges.
* **Analytics Viewers** are members who can also view workspace analytics.

ChatGPT Enterprise workspaces feature two types of seats - standard ChatGPT seats and Codex seats. Each seat type determines what a user can access. Read more about seat types [here](/en/articles/8265053-what-is-chatgpt-enterprise).

A workspace can include any combination of seat types – including only ChatGPT seats, only Codex seats, or a mix of both. Seats can be assigned to any role.

Review the table below for a high level overview of permissions by role.

Users can move between ChatGPT Enterprise workspaces they are a part of, and their personal workspace by using the workspace switcher.

# Managing Members

### Invite members

Anyone you invite should be an intended, ongoing member of your team. ChatGPT Enterprise workspaces are designed for consistent, collaborative use within an organization. Misuse of seat assignments in violation of the Services Agreement may lead to workspace deactivation or account suspension.

Owners and admins can invite members. You can add members from Workspace Settings by inviting by email, by uploading a bulk CSV, or by using [SCIM](/en/articles/10011769-scim-integration-faq). If you are using SCIM,

* Go to your Enterprise workspace.
* Go to **Workspace settings > Members**.
* Select **Invite member**.
* Import a CSV file or manually enter email addresses.
* Choose the role and seat type for each invite.

You can set a default seat type from Workspace settings >  [Identity & Access](https://chatgpt.com/admin/identity).

To add members in bulk, use a CSV with this format:

```
email,role,seat type  
  
For example:  
  
user1@company.com,member,Codex  
analyst1@company.com,member,ChatGPT  
admin@company.com,admin,Codex  
it@company.com,owner,ChatGPT
```

Accepted values for role and seat type are listed below. Note that values are case insensitive.

|  |  |
| --- | --- |
| role | owner, admin, member, analytics\_viewer |
| seat type | ChatGPT, Codex |

If a role is omitted, unrecognized, or unavailable to the person uploading the CSV, that user is added as a member. If seat type is omitted, the default seat type is used.

### Manage pending invites and join requests

Pending invites and join requests should show the selected seat type alongside the user record. Only admins and owners can approve or manage pending requests.

* Go to **Workspace settings >** [**Members**](https://chatgpt.com/admin/members).
* Open the **Pending Invites** or **Pending Requests** view, depending on what you want to review.
* Review the pending user, role, and seat type.
* Approve, resend, edit, or reject the item as needed.

### Change member roles

Only Owners can change member roles.

* Go to **Workspace settings >** [**Members**](https://chatgpt.com/admin/members).
* Find the member you want to update.
* Select the current role in the **Role** column.
* Select the new role.

### Change member seat types

To change member seat types (from standard ChatGPT seat to Codex seat and vice-versa) contact your OpenAI account manager.

If you change a user from a standard ChatGPT seat to a Codex seat, review the loss of ChatGPT workspace access before confirming.

Note that when a user is switched to a Codex seat, they will no longer have access to their Chats, memories, projects (including shared projects they were a part of) or other ChatGPT features. The history, settings and other data are not deleted, and are restored if they are switched back to a ChatGPT seat.

### Remove members

Owners and admins can remove members who are not managed through SCIM from the **Members** list.

* Go to **Workspace settings >** [**Members**](https://chatgpt.com/admin/members).
* Find the member you want to remove.
* Select the **more options menu (•••)**.
* Select **Remove member**.

If your workspace uses SCIM, remove SCIM-managed members through your identity provider. Newly provisioned users follow the workspace’s default seat type, so review that default before enabling or updating automated provisioning.

### Create and manage groups

Groups make it easier to manage access in larger workspaces.

To create a group:

* Open **Workspace settings >**  [**Groups**](https://chatgpt.com/admin/groups).
* Select **Create group**.
* Enter a group name and optional description.
* Add members individually or in bulk.
* Save the group.

To update an existing group:

* Open **Workspace settings >** [**Groups**](https://chatgpt.com/admin/groups).
* Select the group you want to update.
* Select **Manage**.
* Edit the group settings, membership, or description, or delete the group.

Only workspace owners and admins can create, edit, or delete groups.

### Use groups with feature access

Groups are especially useful when your workspace uses role-based access control.

To manage feature access with RBAC, go to **Workspace settings > Permissions & roles**. Use the **Workspace** tab to configure baseline permissions for members who do not have a custom role, and use **Custom roles** to tailor feature access for specific groups. A user’s effective permissions include permissions from custom roles assigned to the user or their groups.

Groups can be used to help manage access to:

* GPTs
* Projects
* Apps
* Other workspace permissions supported by RBAC

A user can belong to more than one group.

Users can also see groups in some sharing flows, such as GPT sharing, but regular users cannot create or edit groups.

Groups and [RBAC](/en/articles/11750701-rbac) do not override a member’s seat type.

Current group limits are:

* Maximum groups per workspace: 10,000
* Maximum users per group: no limit

# FAQ

## What is the difference between a seat type and a role?

A seat type controls which product surface a user can access. A role controls what administrative actions that user can perform in the workspace.

## If a user has a Codex-only seat and is granted access to other ChatGPT features through RBAC, can they use them?

No. A Codex-only seat still limits that user to Codex. Codex-specific RBAC permissions still apply.

## Can [SCIM](/en/articles/10011769-scim-integration-faq) assign a user’s seat type?

SCIM-provisioned users inherit the workspace’s default seat type.

## Are groups required for RBAC?

Yes. Groups are required if your workspace uses RBAC.

## Can members request to join a group?

No. Users must be added by a workspace owner or admin.

## Can members see groups?

They may see groups in some sharing experiences, but they cannot create or manage groups.
