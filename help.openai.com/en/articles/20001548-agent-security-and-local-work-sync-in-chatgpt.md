<!-- source: https://help.openai.com/en/articles/20001548-agent-security-and-local-work-sync-in-chatgpt -->

# Agent Security and local work sync in ChatGPT

Manage agent policies and continue local Work tasks across desktop, web, and mobile.

Agent Security is the area of the Admin Console where you manage agent policies and configuration. It replaces Policies & Config.

Local work sync lets members start a Work task in the desktop app and continue the same conversation on web or mobile. The task can use approved files and tools on a connected computer while the member follows along from another device. Steps that need the computer still require it to be online and connected.

Moving policies to Agent Security and enabling local work sync are separate changes. Moving or saving a policy does not turn on sync.

# Review your policies in Agent Security

Open Agent Security in the Admin Console and review the settings that apply to your workspace.

For policies that have migrated, the existing cloud policy becomes the Global baseline. Review that baseline against the controls your organization needs before enabling local work sync.

## Requirements and Defaults

* Requirements set limits that members cannot override.
* Defaults set starting values within those limits. A default does not override a requirement.

## Global and environment settings

* Global holds the policy baseline, including approval, web search, and managed tool settings.
* Local environment settings cover supported execution controls for work that runs on a connected computer, such as filesystem permissions and sandboxing.
* Codex Cloud environment settings cover supported execution controls for Codex cloud tasks. These policies apply only when Codex Cloud is enabled in workspace permissions.

When a Local or Codex Cloud environment has no override, it inherits the applicable Global settings from that policy.

Codex Cloud and Work Cloud are separate execution environments. Codex Cloud settings do not automatically apply to Work Cloud.

For local execution, mobile device management (MDM) and legacy managed-device requirements take priority over Agent Security. A device’s system requirements file ranks below Agent Security.

Workspaces with policies targeted to specific operating systems are not currently included in the Agent Security migration.

# Enable local work sync

Local work sync is available only where enabled for your workspace and rollout. Members need access to both local Work and cloud Work.

1. Open Workspace settings > Permissions & roles with an account that can manage the workspace’s Work permissions.
2. Enable both Local and Cloud Work access for the intended members, then save those changes.
3. Review your policies in Agent Security, including any controls your organization relies on for local work.
4. Turn on local work sync in Work permissions. Review the information and consent prompt before confirming.
5. Start a new Work task in the desktop app, then open it on web or mobile to continue the conversation.

Keep the computer online, connected, and signed in to the appropriate account and workspace when a task needs its local files or tools.

# What changes when sync is enabled?

## Do existing tasks start syncing?

No. Local work sync applies to new tasks. Existing tasks, including tasks in projects, are not migrated. They continue in the mode in which they were created: locally only, or in the cloud without access to local files. Start a new task to use local work sync.

## What happens if my computer goes offline?

If the computer is unavailable when you start a new turn in an existing synced task, that turn starts in a cloud container. It cannot access files or tools on the unavailable computer.

A running turn does not automatically switch from local execution to the cloud. Keep the computer connected while a turn is using it.

## What happens if an admin turns sync off?

Turning off local work sync interrupts running turns. Members can start a subsequent turn in an existing cloud conversation. That turn uses Work Cloud without access to local files.

## Does this change Codex?

Local work sync is a ChatGPT Work capability. Codex workflows and conversation history remain separate.

# Data and security

Synced Work tasks are coordinated in the cloud, even when a step runs on a local computer. Local execution does not mean that conversation content, tool results, or other task context stays only on that computer.

Synced Work supports data residency, inference residency, and Enterprise Key Management (EKM), subject to your workspace’s applicable configuration. Zero Data Retention (ZDR) is not supported. Do not enable local work sync if your organization requires ZDR.
