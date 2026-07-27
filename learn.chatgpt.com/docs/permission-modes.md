<!-- source: https://learn.chatgpt.com/docs/permission-modes -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionOverview

## Permission modes

Permissions control how ChatGPT (in the desktop app) and Codex (in the CLI or IDE) handle local actions, such as editing files, running commands, and using the internet. The mode you choose sets the boundary
for what ChatGPT can do on its own and what needs review.

For most work, start with **Ask for approval**. It lets ChatGPT work within the
current workspace and pauses before reaching beyond that boundary.

Select different modes below to understand how each one works.

Ask Codex anything.

Ask for approval

Ask for approvalApprove for meFull accessCustom (config.toml)

5.6 Sol Extended

#### Ask for approval

Codex can read and edit files in the current workspace and run routine local commands. It asks before using the internet or going beyond the workspace boundary.

Sandbox
:   `workspace-write`

Approvals policy
:   `on-request`

Reviewer
:   `user`

## Enable modes

When you’re using the ChatGPT desktop app for the first time, you need to enable modes in application settings.

**Ask for approval** is always available. To add **Approve for me** (called
**Auto-review** in settings) or **Full access** to the permissions menu, open
**Settings > General** in the ChatGPT desktop app, then turn on the mode under
**Permissions**. Enabling a mode makes it available in the menu; it doesn’t
select the mode or change an existing chat.

Permissions

Default permissions

By default, ChatGPT can read and edit files in its workspace. It can ask for additional access when needed

Auto-review

ChatGPT can read and edit files in its workspace. ChatGPT automatically reviews requests for additional access. Auto-review can make mistakes. Learn more about elevated risks.

Full access

When ChatGPT runs with full access, it can edit any file on your computer and run commands with network, without your approval. This significantly increases the risk of data loss, leaks, or unexpected behavior. Learn more about elevated risks.

The available modes can depend on your local configuration and your
organization’s requirements. A mode that isn’t allowed appears disabled.

## How permissions work

Two controls work together:

* The **sandbox** defines which files and network resources ChatGPT can access.
* **Approvals** determine when ChatGPT pauses before an action or sends the
  request to automatic review.

Changing who reviews a request doesn’t expand the sandbox. For example,
**Approve for me** keeps the same workspace boundary as **Ask for approval**;
it sends requests to cross that boundary to automatic review.

Use the permissions control below the composer in the ChatGPT desktop app or
IDE extension.

* ![](/images/codex/icons/app-hand.svg)Ask for approvalAlways ask to edit external files and use the internet
* ![](/images/codex/icons/app-shield-code.svg)Approve for meOnly ask for actions detected as potentially unsafe![](/images/codex/icons/app-check-md.svg)
* ![](/images/codex/icons/app-shield-exclamation.svg)Full accessDisabled by requirements.toml
* ![](/images/codex/icons/app-settings-cog.svg)Custom (config.toml)Uses permissions defined in config.toml

Do anything

![](/images/codex/icons/plus.svg)![](/images/codex/icons/app-shield-code.svg)Approve for me

![](/images/codex/icons/app-mic.svg)![](/images/codex/icons/arrow-up.svg)

In the CLI, enter `/permissions`. For technical details, see
[Sandbox](/codex/sandboxing), [automatic review](/codex/sandboxing/auto-review), or
[permission profiles](/codex/permissions).
