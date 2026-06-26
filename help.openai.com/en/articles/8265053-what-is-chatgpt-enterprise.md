<!-- source: https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise -->

# What is ChatGPT Enterprise?

Learn what ChatGPT Enterprise includes, how organizations and members get access, how workspaces and seat types behave, and what happens when you migrate from an individual paid plan.

Updated: 3 days ago

**Note:** On April 2, 2026, we updated some features of the ChatGPT Enterprise plan.

* **We introduced a new seat type:** a **Codex seat** that offers codex-only access, based on flexible pricing.

  + This seat type is available to ChatGPT Enterprise plans, but not to ChatGPT [Edu](/en/articles/9377311), [Teachers](/en/articles/12844995), or [Healthcare](/en/articles/20001046) plans.
* **We updated the** [**Codex Rate Card**](/en/articles/20001106-codex-rate-card) to align with token-based usage pricing, billed in credits per million tokens.

  + As of April 23rd, the new pricing is applicable to all new and existing Enterprise, [Edu](/en/articles/9377311), [Teachers](/en/articles/12844995), and [Healthcare](/en/articles/20001046) plans.

# Overview

ChatGPT Enterprise is a managed ChatGPT plan for organizations. It combines enterprise-grade privacy and security with centralized admin controls and access to advanced ChatGPT capabilities.  
  
ChatGPT Enterprise includes:

* Enterprise-grade privacy and security controls.
* Centralized member management and workspace administration.
* Advanced tools and higher-usage workflows for work use cases.
* Admin features such as domain verification, SSO, SCIM, and usage insights.
* Longer context windows, advanced data analysis and customization options

**Note**: ChatGPT Enterprise accounts may be referred to in the Help Center as Enterprise/Edu. Edu accounts are a variant of the ChatGPT Enterprise plan specific to educational institutions, Read more about [ChatGPT Edu at OpenAI.](/en/articles/9377311)

ChatGPT Enterprise is built around 2 types of seats: standard ChatGPT seats and Codex seats. Each seat type determines what a user can access and how you are billed for that user.  
  
  
**Standard ChatGPT seats** include access to ChatGPT as well as features such as GPTs, Projects, Apps, Company Knowledge, ChatGPT Agent, Deep Research, as well as Codex.The seats include baseline access, and you can use [flexible pricing](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) and purchase workspace credits usage beyond the included rate limits for [Codex](https://developers.openai.com/api/docs/pricing) and for ChatGPT [models](/en/articles/12003714-chatgpt-business-models-limits).  
  
  
**Codex seats** provide access to Codex only – they do not include ChatGPT access. These seats are usage-based seats, with no fixed cost per user per month. Using Codex requires workspace credits - learn more about credits in the [Codex rate card](https://chatgpt.com/admin/ca), and how credits can be used for [flexible pricing](/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans).  
  
If a user on a Codex seat tries to access ChatGPT in the Enterprise workspace, they will be notified that ChatGPT access is not available for their seat type. Upgrading to a standard ChatGPT seat provides access to both Codex and ChatGPT. You can learn more about changing seat types [here](/en/articles/8266401).  
  
Codex seats are governed by workspace-level admin controls, just like standard ChatGPT seats.  
  
Read more about Codex in our [developer docs](https://developers.openai.com/codex).

## Availability

ChatGPT Enterprise is purchased at the organization level. Individual users do not sign up for Enterprise directly.  
  
Members usually get access after a workspace **owner** or **admin** invites them or provisions them through their organization’s identity system, and are assigned a seat type aligned with business needs. [Read about](/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise#managing-members) workspace roles and permissions.  
  
Workspace settings can also control which models and tools are available to members. For more on admin controls, see [Managing workspace settings in ChatGPT Enterprise](/en/articles/8411955). For model availability and limits, see [ChatGPT Enterprise and Edu models and limits](/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits).

### Get access for your organization

If your organization wants to purchase ChatGPT Enterprise:

* Contact the [OpenAI sales team.](https://openai.com/contact-sales)
* Select **ChatGPT Enterprise** as the product of interest in the appropriate field.
* Fill out additional details and click **Submit**. An OpenAI representative will work closely with you to understand your needs and fit the right solution for your organization.

If your organization already has ChatGPT Enterprise, contact your workspace owner, admin, or IT team for access.

### Join and use a workspace

A ChatGPT Enterprise workspace is a dedicated environment for your organization inside ChatGPT.  
  
When you join a workspace:

* Your workspace conversations, files, and GPTs are managed under your organization’s policies.
* Your organization controls workspace settings, permissions, and access rules.
* Your Enterprise workspace remains separate from any personal workspace unless your organization requires a merge.
* What you can use depends on your seat type, workspace settings, and any role-based access controls your admin has configured.

If you have access to more than one workspace, you can switch between them at any time:

* Select your profile icon in ChatGPT.
* Select the workspace you want to use.

Switching workspaces changes the environment you are working in. It does not move or copy data between workspaces.

### Personal-workspace merges

Some organizations require members to merge their personal workspace into the Enterprise workspace when they accept an invite.  
  
If your organization requires a merge:

* Your personal chats, files, and custom GPTs move into the organization’s control.
* The merge is permanent and cannot be undone.
* Your content is then governed by your organization’s workspace policies.

If your organization does not require a merge, your personal workspace and Enterprise workspace stay fully separate.

### Individual paid subscriptions after migration

If you migrate into a ChatGPT Enterprise workspace from an individual paid ChatGPT subscription tied to the same account:

* The individual paid subscription is canceled automatically.
* You receive a partial refund for the unused portion of that subscription period.

### ChatGPT workspace access and API Platform access

A ChatGPT Enterprise workspace and an API Platform organization are separate membership systems.  
  
Being a member of your company’s ChatGPT Enterprise workspace does**not** automatically make you a member of your company’s API Platform organization.  
  
In practice, this means:

* ChatGPT Enterprise access is managed through the workspace.
* API Platform access is managed through the API organization.
* A user can have one, the other, or both.

If you need API Platform access, contact the administrator or owner who manages that organization.  
  
Read additional Help Center articles about managing your ChatGPT Enterprise account.

* [Managing workspace settings in ChatGPT Enterprise](/en/articles/8411955)
* [Managing members, seat types, roles, and groups in ChatGPT Enterprise and Edu](/en/articles/8266401?preview)
* [ChatGPT Enterprise and Edu models and limits](/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits)

# FAQ

## Does workspace membership also give me API access?

No. ChatGPT workspace membership and API Platform organization membership are managed separately.

## Does switching workspaces move my data?

No. Switching workspaces only changes which environment you are using.

## Can a personal-workspace merge be undone?

No. If your organization requires a merge, the move into the Enterprise workspace is permanent.

## Why do I only have access to Codex?

Your workspace admin may have assigned you a Codex-only seat. That seat type limits access to Codex, even if you are part of a role or group with broader permissions.

## Can I change my own seat type?

No. Seat types are assigned by workspace owners or admins.
