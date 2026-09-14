<!-- source: https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt -->

# Managing feature access with role-based access control in ChatGPT

Learn how to configure workspace defaults and custom roles, assign feature permissions, and understand a member's access.

Updated: 4 hours ago

Role-based access control (RBAC) lets workspace owners configure feature access with reusable custom roles. A member can receive roles directly and through group memberships, and can have more than one role.

Custom roles control feature permissions. Built-in workspace roles, such as Member, Admin, and Owner, determine what someone can administer. For built-in roles and seat types, see: [Managing members, workspace roles, and seats](https://help.openai.com/articles/8266401).

RBAC is available for ChatGPT Enterprise, Edu, Healthcare, and Teachers in all supported countries. Configure RBAC on the web through **Workspace settings > Permissions & roles** in ChatGPT, or the supported role and permission controls in [Admin Console](https://admin.openai.com).

## Before you begin

* Workspace Owners can create, delete, assign, and unassign custom roles, and manage workspace-wide permission defaults.
* Workspace Admins may be able to view or update existing roles through supported administration surfaces. They cannot create, delete, assign, or unassign custom roles.
* Members and Analytics viewers cannot manage workspace-wide RBAC settings.
* Group manager delegation is available in ChatGPT Enterprise. Only a workspace Owner can enable or disable **Edit permissions on assigned roles** for group managers.

A tenant global admin does not automatically receive a role in a ChatGPT workspace. Custom roles do not grant Admin key access. Only workspace Owners and Admins can create workspace Admin keys, and sensitive compliance permissions require an Owner. For details, see: [Managing Admin keys in Admin Console](https://help.openai.com/articles/20001407).

# Understand workspace defaults and custom roles

Workspace settings provide the baseline for eligible permissions. An ordinary custom role can use these states:

| **State** | **Effect** |
| Default | Inherits the workspace setting. |
| On | Grants the permission through that role. |
| Off | Denies the permission through that role. Another assigned role can still grant it. |

Permissions from ordinary roles combine additively. If any assigned role grants access, either explicitly or by inheriting an enabled workspace setting, the member retains access. This applies to roles assigned directly and through groups.

If every applicable ordinary role is set to **Off**, access is denied through ordinary RBAC. If all applicable roles use **Default**, the workspace setting applies. Some permissions, including certain Work and plugin controls, have only **On** and **Off**.

Seat type, plan, and product eligibility still apply. Lockdown Mode is evaluated separately and can restrict a capability even when an ordinary role grants it.

# Set workspace permission defaults

1. Open your ChatGPT workspace.
2. Go to **Workspace settings > Permissions & roles**.
3. Open the **Workspace** tab.
4. Review the available permissions and configure the workspace baseline.

The available controls are listed in **Permissions & roles**. A workspace default applies to an eligible custom-role permission when that role uses **Default**.

You can control app access on a per-app basis. An app's UI cannot be disabled independently.

# Create or edit a custom role

Workspace Owners can create custom roles.

1. Go to **Workspace settings > Permissions & roles**.
2. Open **Custom roles**.
3. Select **Create role**.
4. Enter a name and description, then select **Save**.
5. On the role's permission page, choose **Default**, **On**, or **Off** for each eligible permission. For two-state permissions, choose **On** or **Off**.

To edit an existing role, open it in **Custom roles** and update its permitted settings. Administration permissions depend on your workspace role and the supported surface, as described above.

**Changes to a custom role affect every group assigned to it.** Use separate roles when groups need independent permission settings.

# Assign a custom role

Workspace Owners can assign roles directly to individual members where available, or to groups created manually or synchronized through SCIM. Groups are recommended for managing access at scale. For group setup, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

## Assign a role to groups

1. Go to **Workspace settings > Permissions & roles**.
2. Open **Custom roles** and select the role.
3. Open **Role assignments**.
4. Select **+ Add**.
5. Choose one or more groups.
6. Select **Done**.

Members receive permissions from all applicable direct and group role assignments. Changes can take up to 5 minutes to take effect.

## Assign a role directly to a member

Where direct assignments are available, open the member's profile, go to **Direct roles**, and select **Assign direct role**. Choose the custom role to assign. A direct role combines with roles the member receives through groups.

## Delegate editing of assigned roles

In ChatGPT Enterprise, a workspace Owner can allow group managers to edit permitted settings on custom roles assigned to their group. Group managers cannot create or delete roles or assign or unassign them. Editing a role shared by multiple groups affects all of those groups.

For manager assignment, delegated permission settings, and removal, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

# Configure model access and security exceptions

## Model access

Owners can control eligible model access through workspace settings or custom roles. A role cannot make a model available if the workspace is not eligible for it. Choosing a starting or default model does not grant access.

In eligible Enterprise and Edu workspaces, GPT-6 Astra is off by default at launch. Configure Astra access separately; previous Early Model Access settings do not carry over. Review all assigned roles, because a role that allows access can keep it enabled even when another role is set to **Off**.

For current model availability, client requirements, and access details, see: [ChatGPT Enterprise and Edu models and limits](https://help.openai.com/articles/11165333).

## Lockdown Mode

Workspaces with Lockdown Mode role support can create a custom role for members who need it. Lockdown Mode is a role-level security configuration, not a single permission toggle.

A Lockdown Mode role can restrict network-enabled capabilities, including live web search, deep research, agent mode, Canvas networking, and some app, MCP, or connector behavior, depending on workspace settings. These restrictions can apply even when an ordinary role grants the capability.

Before assigning a Lockdown Mode role, review which apps and actions it allows. Members must also have the necessary permissions in each connected source system; ChatGPT app access does not override those source permissions.

For details, see: [Lockdown Mode](https://help.openai.com/articles/20001061).

# Check a member's effective access

Review the member's seat type, plan eligibility, workspace defaults, and all direct and group role assignments. Allow up to 5 minutes for recent RBAC changes to apply.

The following examples use ordinary roles unless stated otherwise:

| **Configuration** | **Result** |
| Workspace Web search is On; the member's only ordinary role uses Default. | Web search is allowed through that role. |
| One ordinary role sets Web search to Off; another sets it to On. | Web search is allowed because one role grants access. |
| Every applicable ordinary role sets Web search to Off. | Ordinary RBAC does not grant access, even if the workspace baseline is On. |
| An ordinary role allows a network-enabled capability; a Lockdown Mode role restricts it. | The Lockdown Mode restriction applies. |

For model access, admins on Business, Enterprise, Healthcare, and Edu can use **Test** in the **Models** section of [Admin Console](https://admin.openai.com). It shows effective model access and the contributing settings. It does not grant access or change permissions. For the procedure, see: [ChatGPT Enterprise and Edu models and limits](https://help.openai.com/articles/11165333).

**Does turning a permission Off in one role remove a member's access?**
Not if another applicable ordinary role grants the permission. Review both direct assignments and roles received through groups. Lockdown Mode and product eligibility are evaluated separately.

**Can RBAC override a member's seat type?**
No. RBAC controls features within the access allowed by the seat type and workspace plan. A Codex-only seat does not gain ChatGPT access from a custom role.

**What if a permission only has On and Off?**
Configure **On** or **Off** explicitly for the workspace and relevant roles. **Default** is available only for eligible permissions.
