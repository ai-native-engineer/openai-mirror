<!-- source: https://help.openai.com/en/articles/20001554-managing-dots-in-chatgpt-workspaces -->

# Managing dots in ChatGPT workspaces

Learn how to manage dots access, personal dots, computer capabilities, connected apps, and messaging in your eligible ChatGPT workspace.

Updated: 7 hours ago

## Overview

### Workspace controls

Workspace owners can control who can use dots and which capabilities are available to them. These settings apply to eligible ChatGPT Enterprise, Edu, and Healthcare workspaces. There is no separate admin setting to turn off proactive research. Dots are not available for workspaces with UAE data or inference residency.

## Access and permissions

### Enabling dots for members

Set permissions for the workspace, or use custom roles to give specific members or groups different access. Dots also require compatible [Agent Security policies](https://learn.chatgpt.com/docs/enterprise/agent-security). Ask your workspace security administrator to review Admin Console > Agent Security > Global > Requirements. Allowed approval policies must include on-request, and Allowed approval reviewers must include [auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review). Before saving changes, keep your other allowed values and existing defaults, and check other saved policies for conflicts.

1. Open **Workspace settings > Permissions & roles**.
2. Select **Permissions**, then **Workspace** **default**.
3. Open **Workspace capabilities**.
4. Find **Use** **dots**, then review the dots permissions and computer capabilities below.
5. Save your settings. Review any custom roles that apply to the members you want to enable.

During admin preview, dots are off by default. The preview runs until November 18, 2026, when dots become available by default unless your workspace admin opts out. Workspace admins can enable access during the preview. Enabling access does not automatically create dots for members. Members create their own dot through onboarding. Review effective workspace and role permissions before and after that transition. The other dots permissions below take effect only when a member has access to dots.

### Dots permissions

| **Setting** | **What it controls** |
| --- | --- |
| **Use dots** | Allows members to use dots. Admins control access during admin preview and after default enablement. |
| **Add dots to Slack and Microsoft Teams** | Allows a dot to join supported Slack or Microsoft Teams workspaces and post with its own identity, where available. Dots in Microsoft Teams have limited availability. Members must complete setup after permission is enabled. |
| **Allow local computer access** | Allows a dot to use a member’s local files and run commands on their computer. The member must also connect their computer, keep it online, and keep the ChatGPT app open. Off by default for Enterprise. |
| **Use custom rules for dots** | Allows members to add or edit rules that guide their dot’s actions and confirmations. Off by default for Enterprise. |

Local computer access is unavailable in workspaces with Codex or ChatGPT Work policies that target a specific operating system. Dots can still work on their cloud computers when the relevant cloud capabilities are enabled.

Default action rules still apply when custom rules are unavailable. Custom rules cannot override built-in safeguards, and disabling custom rules does not make every action require approval.

## Cloud computer and password manager

### Cloud computer settings

Under **Workspace capabilities**, find the three cloud controls in **Cloud computer capabilities**. **Use password manager** appears as a separate control.

| **Setting** | **What it controls** |
| --- | --- |
| **Cloud browser use** | Allows dots and Work Cloud tasks to open and interact with websites using a browser. |
| **Cloud network access** | Allows code and shell commands run by dots and Work Cloud tasks on cloud computers to access the internet. |
| **Cloud computer use** | Allows dots and Work Cloud tasks to interact with the desktop and applications on cloud computers. |
| **Use password manager** | Allows members to use the password manager with dots and Work Cloud. This setting is separate from Cloud browser use. |

These controls apply to both dots and tasks in Work Cloud. They apply to dots even when Work or Work Cloud is disabled. Existing workspace defaults and custom-role settings for browser and network access carry over. Website allow and block lists in Agent security apply to a dot’s cloud browser. Support for applying Agent security’s broader network policies to dot cloud tasks is still in development.

A dot’s cloud computer does not automatically inherit a member’s local VPN, browser sign-ins, or device policies. Access to a website can also require the member to sign in on the cloud computer.

## Connected apps

### App access and approvals

Enabling dots does not grant access to every app or website. Supported app connections that a member already uses in ChatGPT may be available to their dot.

* Plugin controls determine which apps are available and which actions they can perform.
* App permissions determine when an app action requires approval.
* Each connected service’s authorization also limits what the dot can access or do.

Review these settings separately from dots access. For setup details, see [Manage app capabilities](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors#step-2-manage-capabilities).

## Messaging

### Allowing dots in Slack and Microsoft Teams

The **Add dots to Slack and Microsoft Teams** permission allows members to connect their dots to supported communication channels where available. Dots in Microsoft Teams have limited availability. Turning it on does not install a Slack app or connect a member’s dot.

For Slack, both **Use dots** and **Add dots to Slack and Microsoft Teams** must be enabled for the member. If the Slack workspace requires app approval, a Slack workspace owner or app manager must approve the installation and permissions. Each member then completes their dot’s Slack setup.

Only a dot’s owner can direct it. Other people’s direct messages or mentions do not start work for that dot. When a dot posts in a channel, other channel members can see its messages.

Phone messaging through iMessage, RCS, or WhatsApp is unavailable for Enterprise.

## Managing personal dots

Workspace owners and admins can review all personal dots created in their workspace. Each dot’s details include its creator, active or paused status, saved cost tier, and service account identity or dot ID. The inventory also shows Slack or Microsoft Teams connection status. Where an attached-computer list is shown, it does not indicate whether those computers are currently online.

### Pausing and resuming a personal dot

Workspace owners and admins can pause or resume a personal dot. When an admin pauses a dot, its owner cannot resume it until the admin removes that pause.

Resuming a dot restores its owner’s previous pause state. If the owner had already paused it, the dot stays paused until the owner resumes it. Where dot billing applies, an admin pause stops billing for that dot; billing resumes when the dot returns to an active state.

Pausing a dot does not delete its stored information or undo completed actions. Separate Work or Codex tasks and independently scheduled tasks may continue. Review and stop those tasks separately when needed.

These per-dot management controls apply to personal dots. Connection status is informational; it does not provide controls to revoke Slack, Microsoft Teams, or connected-computer access. Shared-dot management is not included.

## Deleting a personal dot

Workspace owners can delete a personal dot. Deletion removes it from the workspace inventory and pauses billing for that dot. After deletion is complete, the member can create a new dot where they have access. A replacement does not restore the deleted dot’s context. Removing or deprovisioning a member revokes their access but does not automatically delete their dot. If a workspace owner cannot delete a former member’s dot, contact Support.

Deleting a dot starts deletion of its own information; it does not delete separately stored files or conversations. For details, see [Dots privacy, security, and safety FAQs](https://help.openai.com/articles/20001529).

## Reviewing usage and admin activity

Workspace analytics shows total active dot users and enabled-dot counts. Enabled dots are dots that are not paused; an enabled-dot count is different from an active-user count. For daily active users (DAU), a member must send at least one message to their dot that day. Background work without a user message does not count.

Workspace audit logs capture admin actions, including pause, resume, delete, management actions, and saved-tier changes. To investigate an admin pause, use the dot ID shown in the dot’s details to find the matching audit event. For authorized access to workspace compliance logs, see [OpenAI Compliance Platform for](https://help.openai.com/articles/9261474) [Enterprise](https://help.openai.com/articles/9261474) [and Edu](https://help.openai.com/articles/9261474).

## Managing access

### Removing a member’s access to dots

To remove a member’s access, review **Use dots** in the workspace default and all roles assigned directly to the member or through groups, then remove every applicable grant. A role that grants access can still allow the member to use dots even if another role has the permission turned off.

Removing every applicable dots grant hides the dot from the member, pauses it, and marks it disabled. Disabled dots are excluded from the current inventory filters. The member cannot resume it until permission is restored. Restoring permission returns it to its previous pause state. Where dot billing applies, revocation stops billing and an active dot resumes billing after access is restored. Removing access does not delete the dot’s information.

App authorizations and website sessions are managed separately. For help reviewing a member’s roles and permissions, see [Managing feature access with role-based access control in ChatGPT](https://help.openai.com/articles/11750701).

Offboarding requires a separate review of the member’s connections, work, and data:

* Review apps and plugins, website sign-ins, local computers, and the dot’s Slack identity. Disabling that identity does not revoke access through the member’s connected Slack account.
* Check visible active tasks, schedules, and delegated Work or Codex tasks. Decide what needs to stop or transfer.
* Review deletion of dot context separately from files and tasks stored elsewhere.

Members can use Pause, Activity, and Scheduled for their own dots. Workspace admins do not gain access to those personal views. If the member is unavailable, removing access or deleting a dot does not confirm that all delegated or scheduled work has stopped.

Support can explain available controls, but cannot operate workspace dots or independently verify which work has stopped or remains active.

### Workspace model settings

Enterprise model controls and default model settings do not apply to dots.

## Residency and data controls

Dots access and workspace data controls are separate. For supported dot regions and the scope of storage and inference residency, see [Data residency and inference residency for ChatGPT](https://help.openai.com/articles/9903489). For memory, deletion, and model-training settings, see [Dots privacy, security, and safety FAQs](https://help.openai.com/articles/20001529).
