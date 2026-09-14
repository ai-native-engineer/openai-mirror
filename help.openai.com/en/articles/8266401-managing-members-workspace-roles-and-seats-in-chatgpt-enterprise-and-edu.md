<!-- source: https://help.openai.com/en/articles/8266401-managing-members-workspace-roles-and-seats-in-chatgpt-enterprise-and-edu -->

# Managing members, workspace roles, and seats in ChatGPT Enterprise and Edu

Learn how to choose workspace roles and manage members and seat types in ChatGPT Enterprise.

A workspace is a ChatGPT environment with its own members, settings, and resources. Workspace roles, seat types, and feature permissions control different parts of a person's access:

| **To change** | **Use** | **Where to learn more** |
| --- | --- | --- |
| What someone can administer | A built-in workspace role | Choose a workspace role below. |
| Which products someone can access | A seat type | Choose a seat type below. |
| Which people belong to a group or administer it | Group membership or a group manager designation | [Managing groups and group managers](https://help.openai.com/articles/9083985). |
| Which features someone can use | Workspace defaults and custom roles | [Managing feature access with role-based access control](https://help.openai.com/articles/11750701). |

The built-in workspace roles below apply to ChatGPT Enterprise and Edu. The seat-type and member-management instructions in this article describe ChatGPT Enterprise. Group manager delegation is available in ChatGPT Enterprise.

# Choose a workspace role

Each workspace has four built-in roles:

* **Member:** Uses the features allowed by their seat type, plan, and permissions. The Member role does not grant administrative privileges.
* **Analytics viewer:** Has member access and can also view workspace analytics.
* **Admin:** Helps manage members and groups, manages Codex access tokens, and performs supported administrative tasks.
* **Owner:** Manages workspace configuration, billing, identity settings, membership, and custom roles. Owners can invite additional owners.

The table shows permissions granted by each built-in role. A role does not override seat type, plan, or feature eligibility. For example, a Codex-only seat does not gain ChatGPT access from its workspace role.

| **Permission** | **Member** | **Analytics viewer** | **Admin** | **Owner** |
| --- | --- | --- | --- | --- |
| Use core chat functionality | Yes | Yes | Yes | Yes |
| View workspace users | Yes | Yes | Yes | Yes |
| View workspace analytics | — | Yes | Yes | Yes |
| Invite new members | — | — | Yes | Yes |
| Invite new admins or owners | — | — | — | Yes |
| Cancel an invitation | — | — | Yes | Yes |
| Remove a user | — | — | Yes | Yes |
| Change a user's workspace role | — | — | — | Yes |
| View groups in supported experiences | Yes | Yes | Yes | Yes |
| Manage groups | — | — | Yes | Yes |
| View plan information in Billing | — | — | Yes | Yes |
| View invoices in Billing | — | — | — | Yes |
| View and manage Identity & Provisioning | — | — | — | Yes |
| View and manage workspace settings | — | — | — | Yes |
| Create a GPT | Yes | Yes | Yes | Yes |
| View and manage GPT settings | — | — | — | Yes |
| View and manage apps | — | — | Yes | Yes |

Group visibility in sharing experiences does not grant permission to browse or edit the full group directory. For availability and visibility rules, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

In ChatGPT Enterprise, an owner or admin can also designate a member as a group manager. This is an additional designation for selected group tasks; it does not replace a built-in workspace role or change a seat type. For assignment and delegated permissions, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

# Choose a seat type in ChatGPT Enterprise

ChatGPT Enterprise supports standard ChatGPT seats and Codex seats. A Codex seat provides Codex-only access. A workspace can have either seat type or a mix of both, and seats can be assigned to any built-in role.

For product access by seat type, see: [What is ChatGPT Enterprise?](https://help.openai.com/articles/8265053). For current token-based Codex usage pricing, billed in credits per million tokens, see: [Codex rate card](https://help.openai.com/articles/20001106).

# Manage members in ChatGPT Enterprise

## Invite members

Anyone you invite should be an intended, ongoing member of your team. ChatGPT Enterprise workspaces are designed for consistent, collaborative use within an organization. Misuse of seat assignments in violation of the Services Agreement may lead to workspace deactivation or account suspension.

Owners and Admins can invite members by email, CSV upload, or SCIM. Only Owners can invite new Admins or Owners.

1. Open your Enterprise workspace.
2. Go to **Workspace settings > Members**.
3. Select **Invite member**.
4. Enter email addresses or upload a CSV file.
5. Choose a workspace role and seat type for each invitation.

Set the default seat type in **Workspace settings > Identity & Access**. If you use SCIM, newly provisioned users inherit this default seat type.

For a CSV upload, use the following columns and format:

`email,role,seat type`
`user1@company.com,member,Codex`
`analyst1@company.com,member,ChatGPT`
`admin@company.com,admin,Codex`
`it@company.com,owner,ChatGPT`

| **Column** | **Accepted values** |
| role | owner, admin, member, analytics\_viewer |
| seat type | ChatGPT, Codex |

Values are case-insensitive. If a role is omitted, unrecognized, or unavailable to the person uploading the CSV, the user is added as a Member. If the seat type is omitted, the workspace default is used.

Inviting members may have contract-specific billing and credit implications. For Enterprise seat additions, true-ups, and shared credits, see: [Flexible pricing for the Enterprise, Edu, and Business plans](https://help.openai.com/articles/11487671).

## Manage invitations and join requests

Owners and Admins can manage pending invitations and join requests.

1. Go to **Workspace settings > Members**.
2. Open **Pending Invites** or **Pending Requests**.
3. Review the person's workspace role and seat type.
4. Approve, resend, edit, or reject the item as needed.

## Change a member's workspace role

Only Owners can change built-in workspace roles.

1. Go to **Workspace settings > Members**.
2. Find the member you want to update.
3. Select their current role in the **Role** column.
4. Select the new workspace role.

## Change a member's seat type

Workspace Owners can change seat types where the option is available.

**Changing from a ChatGPT seat to a Codex seat removes access to chats, memories, projects, shared projects, and other ChatGPT features in that workspace.** The person's history, settings, and other data are not deleted. Access is restored if they are switched back to a ChatGPT seat.

1. Go to **Workspace settings > Members**.
2. Find the member and open the **more options menu (•••)**.
3. Select **Change seat type**.
4. Choose **ChatGPT** or **Codex** and review the access change before confirming.

If **Change seat type** is unavailable, contact your OpenAI account team.

## Remove a member

Owners and Admins can remove members who are not managed through SCIM.

1. Go to **Workspace settings > Members**.
2. Find the member you want to remove.
3. Select the **more options menu (•••)**.
4. Select **Remove member**.

Remove SCIM-managed members through your identity provider. Review the default seat type before enabling or changing automated provisioning. For setup, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

# Join or switch workspaces

Users join an Enterprise workspace by invitation. Joining can require a personal workspace associated with the company's email domain to be merged into the Enterprise workspace or deleted. A user without an existing ChatGPT account has one created as part of joining.

Personal workspaces contain the user's chats, memory, context, apps, and other personal ChatGPT resources. Enterprise workspaces contain the organization's resources and settings.

Users who belong to multiple workspaces can select an active workspace. On ChatGPT web, use the profile menu. On mobile, use the sidebar. Users can switch to a personal workspace if they still have one.

**Can a custom role give a Codex-only seat access to ChatGPT?**
No. A Codex-only seat remains limited to Codex. Codex-specific RBAC permissions still apply. For feature permissions, see: [Managing feature access with role-based access control](https://help.openai.com/articles/11750701).

**Can SCIM assign a user's seat type?**
SCIM-provisioned users inherit the workspace's default seat type. Set that default before provisioning users.

**How do I give someone administrative access to one group?**
In ChatGPT Enterprise, an Owner or Admin can designate an existing group member as a group manager and delegate supported tasks. Only an Owner can enable or disable **Edit permissions on assigned roles**. For the steps, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).
