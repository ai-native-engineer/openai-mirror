<!-- source: https://help.openai.com/en/articles/4936812-managing-members-in-an-api-organization -->

# Managing members in an API organization

Add and remove members, manage invitations and roles, and use SCIM groups to control access to your API organization.

Updated: yesterday

For manually managed API organization memberships, you can add and remove people in API Platform. If your organization uses synchronized groups, manage access through Admin Console.

# Choose where to manage members

For manual membership changes in API Platform, you need permission to manage members. Organization owners have this access by default. Readers do not have member-management access by default.

If the **People** page says your organization is managed in Cloud Console and its member controls are read-only, select **Open Cloud Console** to open Admin Console. For organizations that use tenant-wide SCIM, follow the group-access steps below. If you need access and your organization has no SCIM group assignment, contact your global admin.

Organization membership and project access are separate. Review the projects a person needs when adding them. For project roles and permissions, see: [Managing projects in the API platform](https://help.openai.com/articles/9186755).

API organization roles and membership are separate from ChatGPT workspace roles and membership.

# Add a member in API Platform

1. Open [API Platform settings](https://platform.openai.com/settings/organization/people) and select the organization you want to manage.
2. Go to **People > Members**.
3. Select **Add member**.
4. Enter the person’s email address in **Emails**. If **Select user** is available, you can select an existing tenant user instead, or use **Enter user email**.
5. Under **Role**, select **Owner** or **Reader**.
6. Under **Invite to projects**, select at least 1 project. Review any project that is already selected.
7. Select **Invite**. If a message says existing tenant users will be added directly, review it, then select **Add** or **Add and invite**.

Ask invited recipients to open the invitation email and follow the link to join. Existing tenant users who are added directly do not need to accept an invitation.

Choose **Owner** for someone who needs to manage the organization. Choose **Reader** for someone who needs API access without the default organization-owner permissions. The selected projects grant the **Member** project role.

# Manage pending invitations

1. In API Platform settings, go to **People > Invitations** for the organization.
2. Find the person’s invitation.
3. To send the invitation again, select **Resend**. To cancel it, select **Remove**, then select **Remove** in **Confirm removal**.

**Resend** is unavailable after an invitation expires. For an expired manual invitation, remove it and send a new invitation. SCIM invitations cannot be removed in API Platform. Invitations managed through your tenant have no action controls here.

# Change a member’s roles

1. In API Platform settings, go to **People > Members** for the organization.
2. Select **Roles** beside the person.
3. Select or clear the relevant role checkboxes, then select **Save**.

Review any warning before removing an owner role. Demoting an owner can invalidate their admin API keys. To change which projects someone can use, manage their project membership separately.

# Remove a member

Before removing a member, review whether their active API keys are in use. Removing the member may disrupt API access that uses those keys.

1. In API Platform settings, go to **People > Members** for the organization.
2. Find the person and select **Remove**.
3. Review **Confirm removal**, then select **Remove**.

When you can remove your own membership, your row shows **Leave**. If you are the organization’s only owner, transfer ownership before leaving or having your membership removed.

You cannot remove a SCIM-managed member with this control. Change their group membership or access assignment through the system that manages it.

# Manage access through SCIM groups

If your tenant uses tenant-wide SCIM (System for Cross-domain Identity Management), global admins can assign synchronized groups to API organizations in Admin Console. To add a person to an existing group, update their membership in your identity provider.

To give a synchronized group access to an API organization:

1. In Admin Console, go to **Users & groups > SCIM Groups**.
2. Open the group, then open **Product access**.
3. Select **Add product access**.
4. Under **Product**, select **API Platform**.
5. Under **Organization access**, select the organization in **Org**.
6. Under **Project access**, select a project. Select **Add project** to include more projects.
7. Select **Save**.

Group members are provisioned directly without accepting an API organization invitation. To change the group’s project assignments, use **Edit** on its product access assignment. **Remove** removes the assignment for the group, so use your identity provider to remove just one person from the group.

SCIM manages the organization memberships it creates or takes over, including memberships originally added manually. Removing a person’s last qualifying assignment can remove their organization membership and associated project memberships. Manual memberships that SCIM has not taken over remain separately managed.

For setup requirements and offboarding checks, see: [SCIM provisioning and management](https://help.openai.com/articles/10011769).

# Troubleshoot member access

## Member controls are unavailable

Confirm that you selected the correct organization and have permission to manage members. If the page directs you to Admin Console, use your organization’s group-based access process or contact your global admin.

## You cannot add a person

Check that the email address is valid and at least 1 project is selected. If the person already belongs to the organization, find them under **Members**. If they have a pending invitation, use **Invitations** to manage it.

## A member cannot access a project

Check the person’s project membership and role. For SCIM group access, check both their identity-provider group membership and the group’s project assignment in Admin Console.
