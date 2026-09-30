<!-- source: https://help.openai.com/en/articles/20001554-manage-dots-in-chatgpt-workspaces -->

# Manage dots in ChatGPT workspaces

Learn how to manage dots access, computer capabilities, connected apps, and messaging in your Enterprise workspace.

Updated: 2 hours ago

## What can workspace owners control?

Workspace owners can control who can use dots and which capabilities are available to them. These settings apply to eligible ChatGPT Enterprise workspaces during the dots beta.

# Access and permissions

## How do I enable dots for members?

Set permissions for the workspace, or use custom roles to give specific members or groups different access.

1. Open **Workspace settings > Permissions & roles**.
2. Go to **Permissions > Workspace default > Workspace capabilities**.
3. Find **Use dots (Beta)**, then review the dots permissions and computer capabilities below.
4. Save your settings. Review any custom roles that apply to the members you want to enable.

Dots access is off by default for Enterprise. The other dots permissions below take effect only when a member has access to dots.

## What do the dots permissions control?

| **Setting** | **What it controls** |
| --- | --- |
| **Use dots (Beta)** | Allows members to use dots. Off by default for Enterprise. |
| **Add dots to Slack and Microsoft Teams** | Allows a dot to join supported Slack or Microsoft Teams workspaces and post with its own identity, where available. Members must complete setup after permission is enabled. |
| **Allow local computer access** | Allows a dot to use a member’s local files and run commands on their computer. The member must also connect their computer, keep it online, and keep the ChatGPT app open. Off by default for Enterprise. |
| **Use custom rules for dots** | Allows members to add or edit rules that guide their dot’s actions and confirmations. Off by default for Enterprise. |

Local computer access is unavailable in workspaces with Codex or ChatGPT Work policies that target a specific operating system. Dots can still work on their cloud computers when the relevant cloud capabilities are enabled.

Default action rules still apply when custom rules are unavailable. Custom rules cannot override built-in safeguards, and disabling custom rules does not make every action require approval.

# Cloud computer and password manager

## What do the cloud computer settings control?

Under **Workspace capabilities**, find the three cloud controls in **Cloud computer capabilities**. **Use password manager** appears as a separate control.

| **Setting** | **What it controls** |
| --- | --- |
| **Cloud browser use** | Allows dots and Work Cloud tasks to open and interact with websites using a browser. |
| **Cloud network access** | Allows code and shell commands run by dots and Work Cloud tasks on cloud computers to access the internet. |
| **Cloud computer use** | Allows dots and Work Cloud tasks to interact with the desktop and applications on cloud computers. |
| **Use password manager** | Allows members to use the password manager with dots and Work Cloud. This setting is separate from Cloud browser use. |

These controls apply to both dots and tasks in Work Cloud. They apply to dots even when Work or Work Cloud is disabled. Existing workspace defaults and custom-role settings for browser and network access carry over.

A dot’s cloud computer does not automatically inherit a member’s local VPN, browser sign-ins, or device policies. Access to a website can also require the member to sign in on the cloud computer.

# Connected apps

## How do app access and approvals work?

Enabling dots does not grant access to every app or website. Supported app connections that a member already uses in ChatGPT may be available to their dot.

* Plugin controls determine which apps are available and which actions they can perform.
* App permissions determine when an app action requires approval.
* Each connected service’s authorization also limits what the dot can access or do.

Review these settings separately from dots access. For setup details, see [Manage app capabilities](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors#step-2-manage-capabilities).

# Messaging

## How do I allow dots in Slack and Microsoft Teams?

The **Add dots to Slack and Microsoft Teams** permission allows members to connect their dots to supported communication channels where available. Turning it on does not install a Slack app or connect a member’s dot.

For Slack, both **Use dots (Beta)** and **Add dots to Slack and Microsoft Teams** must be enabled for the member. If the Slack workspace requires app approval, a Slack workspace owner or app manager must approve the installation and permissions. Each member then completes their dot’s Slack setup.

Only a dot’s owner can direct it. Other people’s direct messages or mentions do not start work for that dot. When a dot posts in a channel, other channel members can see its messages.

Phone messaging through iMessage, RCS, or WhatsApp is unavailable for Enterprise at launch.

# Managing access

## How do I remove a member’s access to dots?

To remove a member’s access, review **Use dots (Beta)** in the workspace default and all roles assigned directly to the member or through groups, then remove every applicable grant. A role that grants access can still allow the member to use dots even if another role has the permission turned off.

App authorizations and website sessions are managed separately. For help reviewing a member’s roles and permissions, see [Managing feature access with role-based access control in ChatGPT](/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt).

## Do workspace model settings apply to dots?

No. Enterprise model controls and default model settings do not apply to dots.
