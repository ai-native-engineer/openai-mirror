<!-- source: https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq -->

# Custom GPT retirement and migration FAQ

Learn about custom GPT retirement, the migration to plugins, and the planned timeline and guidance for Enterprise and personal accounts.

Updated: yesterday

# Overview

We're planning to retire custom GPTs, and encourage you to consider using plugins as replacements for GPTs you create or rely on. Plugins can bring reusable instructions and connected apps together, so your guidance can work alongside the tools and information a task needs.

To help you make the move, we’re planning to help you migrate your GPTs to plugins. This FAQ explains how to prepare, what users and admins can expect, and how the transition applies to personal accounts. For more information about plugins, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

## Does this change affect all ChatGPT Plans?

The transition affects all ChatGPT plans. The detailed dates and admin guidance below describe the Enterprise transition; plan-specific availability and exceptions may vary.

If you use several accounts or workspaces, check where the GPT was created and the notice provided to that workspace. Your workspace admin or account team can help confirm the timeline that applies.

## Could a public GPT I use be affected if I am on another plan?

Yes. Public GPTs created in affected Enterprise workspaces are included in the Enterprise transition, even if you access them from a personal account or another workspace. What matters is where the GPT was created, not only your own plan. Check any notice on the GPT and guidance from its creator. Access to a public GPT does not guarantee access to its replacement plugin.

The sections below explain the planned migration and what to check before switching. Workspace admin permissions and controls apply to Enterprise workspaces; personal accounts may have different access and available options.

# Timing and what to do now

## Is my GPT already gone?

No. The announcement gives you time to prepare for a future retirement. Existing GPTs remain usable until the retirement date, subject to their existing access and workspace permissions.

After a GPT is migrated, the original remains usable until retirement but becomes read-only. Finish essential edits before migrating and maintain the replacement plugin afterward.

## Which dates should I plan around?

For affected Enterprise workspaces, the planned milestones are described below. Note that the dates are subject to change.

* Sep 11, 2026: Admin notice to help organizations prepare.
* Sep 17, 2026: Target for the migration experience and user banner. This is a target, not a guarantee that the option is available in every workspace.
* Sep 25, 2026 (planned): Creation of new custom GPTs ends. Publish any drafts you need to migrate before this cutoff; public sharing is not required. Existing GPTs remain usable until retirement.
* Dec 11, 2026: Scheduled retirement. Custom GPTs stop running.

The other plans may follow the same transition timeline, with in-product announcements coordinated with Enterprise. This does not guarantee that migration is available to every account or workspace on the target date. Follow the notices for your plan, account or workspace. Restrictions on creating or publishing GPTs are separate from retirement of existing GPTs.

## Do I need to take action immediately?

You can start preparing now. Identify the GPTs you rely on, who created each one, and who needs access to the replacement. Record the instructions, reference material, integrations, and a few familiar prompts so you can test the migrated workflow. In an Enterprise workspace, coordinate this preparation with your admin.

Allow extra time for GPTs that use custom actions. Those integrations do not transfer automatically.

When migration becomes available for your account or workspace, migrate and test the workflows you want to keep before retirement. The announcement date is a chance to prepare; existing GPTs remain usable until their retirement date.

## Why don't I see a migration option?

For Enterprise workspaces, migration is targeted for Sep 17, 2026. Before it is available in your workspace, a missing migration option does not by itself indicate a problem.

Migration may not be available to your account yet, or plugin access may be disabled. For an Enterprise workspace, ask your admin to check that plugins are enabled, the GPT is published, and you are its creator or a workspace admin. Permission to use someone else's GPT does not give you permission to migrate it.

For other accounts, follow the guidance in your in-product notice.

# Migrating and testing

## Who can migrate a GPT?

In the planned Enterprise workflow, a GPT’s creator or a workspace admin can migrate it when migration is available and plugins are enabled. The GPT must be published; drafts cannot be migrated directly. Publishing does not require sharing it publicly. Permission to use someone else’s GPT does not give you permission to migrate it.

Built-in migration does not require **Upload plugins** or **Upload plugins with custom MCP servers**. Rebuilding an integration is a separate task and may require additional permissions.

## How do I start migration?

When migration is available in your Enterprise workspace, open your published GPT and select its migration button, or ask a workspace admin for help. Then test the replacement plugin and review its sharing settings before asking others to switch. For a personal account, follow the migration instructions in your in-product notice.

## What transfers to the plugin?

Under the planned migration workflow, the GPT's instructions become a skill within the new [plugin](https://help.openai.com/articles/20001256). Connected apps are added to the plugin as apps.

Review the migrated reference files, templates, examples, and tools before relying on the replacement. Conversation starters and previous chats may not copy. The GPT's selected model does not carry over; in Enterprise workspaces, Enterprise defaults apply.

## What happens to custom actions?

GPT custom actions do not transfer through the migration workflow. The person maintaining the workflow will need to assess and rebuild required integrations using a supported connector or custom MCP server.

Work with the appropriate technical and security teams to review the replacement and its permissions. Test the integration before switching. A rebuilt integration should not be assumed to provide every capability of the original action.

## Will the plugin work exactly like my GPT?

A migrated plugin may respond differently. Before sharing it more widely, compare familiar prompts and at least one harder case. Check that it:

* Selects the right skill and follows your instructions.
* Uses the expected reference material.
* Produces complete answers or files in the required format.
* Has the tools and integrations the workflow needs.

Resolve differences that affect the workflow before asking the wider team to switch.

## What happens to the original GPT after migration?

The original GPT remains usable until retirement, but becomes read-only after migration and its creator cannot delete it. Make future changes to the plugin.

At retirement, custom GPTs are scheduled to stop running and leave the GPT directory. Migrated GPT links are planned to redirect to the replacement for people who have access. A redirect does not grant access to the plugin.

# Sharing and access

## Will everyone who used the GPT automatically have access to the plugin?

The replacement plugin starts private. Test and review it before sharing. After sharing, ask an intended user to install and test the replacement.

In an Enterprise workspace, sharing with people or groups requires **Share plugins**. Publishing to the workspace directory requires **Publish plugins to workspace**. These are separate permissions.

## What do I need to use a migrated plugin?

You need access to the replacement plugin and an account where plugins are available. In an Enterprise workspace, you also need **Use plugins** permission and a workspace policy that lets you install the plugin or installs it for you.

Any included apps still require their own app access, account authorization, and action approvals. Installing a plugin or connecting an account does not give you additional permissions to files or data in the connected service.

For workspace settings, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

## How do I use the replacement?

Once the plugin is available to you and installed, select an available plugin or skill for your task. In ChatGPT, you can use an @ mention or open **+** and select **More**, where supported.

ChatGPT may also use a relevant installed skill automatically when its description matches your request. Automatic selection depends on the task and available capabilities; the plugin will not necessarily run on every request.

## Was this article helpful?
