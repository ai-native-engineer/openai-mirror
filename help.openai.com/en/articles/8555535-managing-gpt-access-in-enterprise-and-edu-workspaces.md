<!-- source: https://help.openai.com/en/articles/8555535-managing-gpt-access-in-enterprise-and-edu-workspaces -->

# Managing GPT access in Enterprise and Edu workspaces

How GPT access, collaboration, and usage are managed within Enterprise and Edu workspaces.

Updated: 2 days ago

*As of February 13, 2026, models GPT-4o, GPT-4.1, GPT-4.1 mini, OpenAI o4-mini, and GPT-5 (Instant and Thinking) have been retired from ChatGPT and are no longer available. API access remains unchanged.*  
  
*For more information, please refer to our article:* [*Retiring GPT-4o and other ChatGPT models*](https://help.openai.com/articles/20001051)

# Overview

This article explains how GPT-related workspace controls affect building, sharing, access, and governance in Enterprise and Edu workspaces. It is intended for workspace owners and admins who manage GPT access for their organization.

## Availability

Availability for GPT features varies by plan and workspace permissions. For general availability details, see: [GPTs in ChatGPT](https://help.openai.com/articles/8554407).

# Permission and roles (RBAC)

The following can be configured in **Workspace settings** > **Permission & roles**. You may set them at the workspace level or assign them through custom roles:

* Who can **create or edit** GPTs through workspace settings and role permissions.
* Whether GPTs **can be shared**, and whether sharing is limited to invite-only, workspace-only, or broader sharing levels.
* Whether users can access **third-party GPTs**, only owner-approved third-party GPTs, or no third-party GPTs.

For more on configuring workspace permissions and custom roles, see: [RBAC (Role-based access controls)](https://help.openai.comarticles/11750701).

# Workspace-level controls

The following can be configured in **Workspace settings** > **GPTs**. They are applied at the workspace level and cannot be customized for individual roles at this time.

## Apps

Workspace admins can control whether apps can be used in GPTs created in the workspace. If apps are disabled, GPTs created in your workspace cannot use apps. This setting does not apply to third-party GPTs.

## Actions

Workspace owners can also restrict GPT actions to specific allowed domains for GPTs created in the workspace. If no domains are added, GPT actions are not allowed. Allowing a parent domain also allows its subdomains.  
  
If a GPT uses actions that do not comply with workspace domain restrictions, those actions may be rejected or unavailable until they are updated or removed.  
  
For instructions on configuring apps or actions in a GPT, see: [Creating and editing GPTs](https://help.openai.com/articles/8554397) and [Configuring actions in GPTs](https://help.openai.com/articles/9442513).

# Collaboration and ownership

In managed workspaces, GPTs can support collaboration through sharing permissions. Depending on the permission level assigned, collaborators may be able to:

* Use a GPT with **Can chat**.
* View its configuration with **Can view settings**.
* Update it with **Can edit**.

GPTs also have an owner. Some workspace-level GPT management actions, including ownership changes and certain workspace approval actions, are restricted to workspace owners.  
  
For steps to share a GPT and assign permissions, see: [Sharing and publishing GPTs](https://help.openai.com/articles/8798878).

## Ownership continuity

If the owner of a GPT is deactivated or removed from a managed workspace through the normal workspace removal flow, the GPT is not left without an owner. Ownership is transferred to a workspace owner, and the GPT is marked as unassigned so workspace owners can review or reassign it if needed.  
  
If the original creator is later re-added to the workspace, ownership can be restored automatically to that person. Workspace owners can also manually reassign GPT ownership to another workspace member at any time.

## SCIM-managed group sharing

Workspace owners can control whether SCIM-managed groups appear in GPT sharing flows. For setup steps and behavior details, see: [SCIM Integration FAQ](https://help.openai.com/articles/10011769).

# Compliance

Conversations with GPTs are available in the Compliance Platform. For specific details, see: [OpenAI Compliance Platform](https://chatgpt.com/admin/api-reference)

# Reporting

[Workspace analytics](https://chatgpt.com/admin/usage) includes a GPTs section where eligible viewers can track GPT adoption and other metrics.  
  
For more on available metrics and information on workspace analytics, see: [Workspace Analytics in ChatGPT Enterprise and Edu](/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu).
