<!-- source: https://help.openai.com/en/articles/9083985-managing-groups-and-group-managers-in-chatgpt-enterprise-and-edu -->

# Managing groups and group managers in ChatGPT Enterprise and Edu

Learn how to organize workspace members into groups and delegate group administration in ChatGPT Enterprise.

Groups help workspace Owners and Admins organize members, share resources such as GPTs, projects, and apps, and assign custom roles for feature access. A member can belong to more than one group.

A group manager is a workspace member who can perform selected administrative tasks for a particular group. The designation does not change their built-in workspace role or seat type, make them a workspace Admin or Owner, or give them the tenant User manager role.

Groups are available in ChatGPT Enterprise and Edu. Group manager delegation is available in ChatGPT Enterprise.

## Before you begin

* Workspace Owners and Admins can create and manage manual groups and designate group managers.
* Membership for SCIM-synchronized groups is managed in your identity provider.
* A group manager can perform only the tasks delegated to them. The designation does not grant general group-management permissions.

# Create or manage a group

## Create a manual group

1. Open [Admin Console](https://admin.openai.com) and select your ChatGPT workspace.
2. Open **Members, groups & roles**.
3. Select **Groups**, then **Create group**.
4. Enter a group name and an optional description.
5. Add the workspace members you want to include, individually or in bulk.
6. Save the group.

You can also open workspace groups from **Workspace settings > Groups** in ChatGPT.

## Update a manual group

In **Admin Console**, select your workspace, open **Groups**, and select the group. Use the available edit or delete option to update the group.

If you manage the group from ChatGPT:

1. Go to **Workspace settings > Groups**.
2. Select the group.
3. Select **Manage**.
4. Update the group's settings, membership, or description, or delete the group.

These actions require a workspace Owner or Admin. Group manager delegation does not include creating or deleting groups.

## Manage a SCIM-synchronized group

Update SCIM-managed group membership in your identity provider. For tenant-wide SCIM, a global admin can assign a synchronized group to an eligible ChatGPT workspace through **Product access**. Its membership cannot be edited, and the synchronized group cannot be deleted, from the workspace.

For setup and synchronized-group guidance, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

# Assign a group manager in ChatGPT Enterprise

Workspace Owners and Admins can designate existing group members as managers. A group can have more than one manager.

1. Open [Admin Console](https://admin.openai.com) and select your workspace.
2. Open **Groups** and select the group.
3. Open **Group members**.
4. Change the person's **Group role** to **Group manager**.
5. Save the change if the page shows pending changes.

The designation and delegated permissions are separate settings. Review **Group manager permissions** to choose what the group's managers can do.

# Choose delegated permissions

Owners and Admins can configure supported group manager permissions. **Only a workspace Owner can enable or disable Edit permissions on assigned roles.** Members and group managers cannot configure delegation or grant themselves additional authority.

1. In **Admin Console**, select your workspace.
2. Open **Groups** and select the group.
3. Open **Group manager permissions**.
4. Turn on the permissions you want to delegate.

| **Permission** | **What it allows** | **Who can enable or disable it** |
| --- | --- | --- |
| View group analytics | View analytics for the group. | Owner or Admin |
| Manage spend controls | Manage group usage limits and approve or deny requests to increase limits. | Owner or Admin |
| Manage model access and defaults | Manage model access and default model settings for the group. | Owner or Admin |
| Edit permissions on assigned roles | Update permitted feature and model permissions on custom roles assigned to the group. | Owner only |

The toggles save as you change them. These settings apply to every manager of the group; they are not configured separately for each manager.

**Editing a custom role shared by several groups affects every group assigned to that role.** Use separate custom roles when groups need independent permission settings. Choosing a default model does not grant access to that model.

For custom-role behavior and assignment, see: [Managing feature access with role-based access control](https://help.openai.com/articles/11750701). For usage limits and increase requests, see: [Managing usage limits and overages in ChatGPT Enterprise and Edu](https://help.openai.com/articles/20001001).

# Change or remove delegated access

## Change the group's delegated permissions

An Owner or Admin can return to the group's **Group manager permissions** and adjust the toggles. Changes save as you make them and apply to all managers of that group. The Owner-only restriction on **Edit permissions on assigned roles** also applies when turning that permission off.

## Remove a manager designation

An Owner or Admin can remove the designation without removing the person from the group:

1. In **Admin Console**, select your workspace.
2. Open **Groups** and select the group.
3. Open **Group members**.
4. Change the person's **Group role** from **Group manager** to **Member**.
5. Save the change if the page shows pending changes.

# Understand the limits of delegation

Group manager permissions do not allow someone to:

* Create or delete groups or custom roles.
* Assign or unassign custom roles.
* Appoint or remove group managers.
* Change the group's delegation settings or grant themselves more authority.
* Administer the entire workspace or tenant through the group manager designation.

Group-specific actions apply only to groups the person manages. Editing a shared custom role has the broader effect described above. Group membership and delegated permissions do not override a member's seat type, plan, or product eligibility.

For built-in workspace roles and seat types, see: [Managing members, workspace roles, and seats](https://help.openai.com/articles/8266401).

# Group limits and visibility

* Maximum groups per workspace: 10,000.
* Maximum users per group: No limit.

Workspace members may see manual groups in supported sharing experiences. SCIM-managed groups appear when sharing GPTs or projects only if the workspace allows SCIM group discovery. Seeing a group does not give a member permission to browse or edit the full group directory.

**Can members request to join a group?**
No. A workspace Owner or Admin must add them to the group.

**Can someone belong to more than one group?**
Yes. If groups have custom roles, permissions from those roles can combine with the person's other assigned roles. For the rules, see: [Managing feature access with role-based access control](https://help.openai.com/articles/11750701).

**Are groups required to use custom roles?**
No. Custom roles can also be assigned directly to individual members where supported. Groups are recommended for managing access at scale.

**Does assigning a custom role to a group make its members workspace Admins?**
No. Custom roles control feature permissions. Built-in workspace roles, such as Admin or Owner, control workspace administration. A group manager designation is a separate way to delegate selected group tasks.
