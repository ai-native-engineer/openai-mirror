<!-- source: https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise -->

# Managing workspace settings in ChatGPT Enterprise

Learn what workspace owners and admins can manage in Workspace settings, including appearance, seat defaults, permissions, analytics, and identity controls.

Updated: 3 days ago

# Overview

**Workspace settings** is the main admin surface for managing how ChatGPT is used in your organization.  
  
From this area, workspace owners and admins can manage members, seat defaults, feature access, GPT governance, apps, analytics, and identity controls. Owners can also update the workspace name and image. To learn more about roles and permissions in the ChatGPT Enterprise workspace, see: [Managing members, seat types, roles, and groups in ChatGPT Enterprise and Edu](https://help.openai.com/articles/8266401).  
  
Workspace settings are available to all roles, but only owners and admins can control and modify key settings for the workspace, such as permissions, seat types, spend controls, and access to ChatGPT and Codex features.  
  
To open Workspace settings, select your profile icon in ChatGPT, then select [**Workspace settings**](https://chatgpt.com/admin).

# General

Use [**General**](https://chatgpt.com/admin) to manage workspace-wide configuration and identity details such as:

* Workspace name and image.
* Workspace and organization identifiers.
* The workspace AI policy modal.

## Update the workspace name or image

To update the workspace name or workspace image:

1. Go to **Workspace settings > General**.
2. Move your pointer over the workspace name, then select the edit icon.
3. Update the workspace name, the workspace image, or both.
4. Select **Save**.

Changes apply across the workspace for all members.

## Manage the AI policy modal

Owners and admins can use the workspace policy area in **General** to define organization-specific AI policy guidance.  
  
When enabled or updated:

* The policy modal is shown to users every 30 days.
* The policy modal is also shown when the policy content is updated.

# Members

Use [**Members**](https://chatgpt.com/admin/members) to:

* Invite members.
* Remove members.
* Manage member roles.
* Assign or change member seat types where supported.
* Review pending invitations and requests.

You can also control whether members can view member and group assignment lists, including assigned roles.  
  
For access management guidance, see: [Managing members, seat types, roles, and groups in ChatGPT Enterprise and Edu](https://help.openai.com/articles/8266401).

# Groups

Use [**Groups**](https://chatgpt.com/admin/groups) to:

* Create and delete groups.
* Add or remove members from groups.
* Review group membership.

Groups are especially useful if your workspace uses role-based access control.

# Permissions & roles

Use [**Permissions & roles**](https://chatgpt.com/admin/permissions) to control workspace-wide feature access and role-based access settings.  
  
This area can be used to manage items such as:

* Available models.
* GPT creation and sharing controls.
* Canvas.
* Projects.
* Memory.
* Link sharing.

Depending on your setup, some controls may be applied workspace-wide, while others can be managed through role-based access control.

# Billing

Use [**Billing**](https://admin.openai.com/billing) in the [global admin console](https://admin.openai.com) to review invoices, seat information, and other billing-related workspace details.

# GPTs

Use [**GPTs**](https://chatgpt.com/admin/gpts) to manage custom GPTs created in the workspace, including:

* Reviewing GPT ownership.
* Transferring ownership.
* Deleting GPTs.
* Managing GPT actions.

# Apps

Use [**Apps**](https://chatgpt.com/admin/ca) to manage external tools and integrations available in your workspace. This can include:

* Enabling or disabling apps organization-wide.
* Assigning app access to specific members or roles where supported.
* Enabling sync for supported apps.
* Creating and deploying custom MCP apps for your organization.

# Workspace analytics

Use [**Workspace analytics**](https://chatgpt.com/admin/usage) to review adoption and engagement trends, such as:

* Daily and weekly active users.
* Messages per user.
* Total messages.
* Total seats.
* GPT usage.

For more information about Workspace analytics, see: [Workspace analytics for ChatGPT Enterprise and Edu](https://help.openai.com/articles/10875114).

# Identity & access

Use [**Identity & access**](https://chatgpt.com/admin/identity) to manage how people access the workspace, including:

* Login configuration.
* Provisioning.
* Identity management.
* IP allowlists.

If your organization uses SCIM, newly provisioned users follow the workspace’s default seat type where supported. Review that default before turning on or updating automated provisioning.

# FAQ

## Who can update the workspace name and image?

Only workspace owners.

## Can I set a default seat type for new users?

Owners and admins can set a default seat type for newly provisioned users. SCIM-provisioned users follow that default.

## Where are shared-link controls managed for the workspace?

Workspace-level link-sharing controls are managed in [**Workspace settings > Permissions & roles**](https://chatgpt.com/admin/permissions).
