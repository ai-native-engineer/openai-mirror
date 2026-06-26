<!-- source: https://help.openai.com/en/articles/20001264-chatgpt-enterprise-admin-quickstart -->

# ChatGPT Enterprise admin quickstart

Set up a new ChatGPT Enterprise workspace with recommended setup guidance for identity, access, workspace settings, roles and permissions, security controls, and monitoring.

Updated: 2 days ago

Use this quickstart to prepare a new ChatGPT Enterprise workspace before inviting users broadly. It gives first-time Workspace Owners a recommended setup order, with links to deeper Help Center articles for each area.

# Before you begin

Confirm the following before you start:

* The Workspace Owners who will make workspace-wide setup decisions.
* The Workspace Admins who can manage user invites and groups, as well as view analytics and set up access to apps.
* Your identity provider, verified domains, and provisioning approach.
* Logic for organizing users into groups.
* The security, compliance, logging, retention, and network controls your organization requires.

# Setup checklist

Use this checklist to track the recommended setup order:

* [Confirm roles, seat types, and launch scope.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#1-confirm-roles-seat-types-and-launch-scope)
* [Verify domains and configure identity.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#2-verify-domains-and-configure-identity)
* [Set up SSO and SCIM before broad onboarding.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#3-set-up-sso-and-scim-before-broad-onboarding)
* [Create groups and assign RBAC/custom roles.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#4-create-groups-and-assign-rbac)
* [Configure workspace settings and user guidance.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#5-configure-workspace-settings-and-user-guidance)
* [Enable Apps, GPTs, connectors, and approved domains.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#6-enable-apps-gpts-and-approved-data-connections)
* [Enable Workspace Agents and Codex for the right teams.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#7-enable-codex-for-the-right-teams)
* [Configure security and compliance controls.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#8-configure-required-security-and-compliance-controls)
* [Monitor adoption, usage, and support readiness.](/en/articles/20001264-chatgpt-enterprise-admin-quickstart#9-monitor-adoption-usage-and-support-readiness)

# Complete the setup

## 1. Confirm roles, seat types, and launch scope

Decide who owns the rollout, who can administer the workspace, and which users need ChatGPT access, Codex access, or both.  
  
This helps avoid unclear ownership later, especially for identity decisions, security settings, usage limits, and user support.  
  
Read more:

* [Managing members, seat types, roles and access in ChatGPT Enterprise](https://help.openai.com/articles/8266401)
* [What is the difference between different roles on my ChatGPT Enterprise and Edu workspace?](https://help.openai.com/articles/8266431)

## 2. Verify domains and configure identity

Before inviting users in bulk, confirm that your organization owns its email domain and set up your identity controls.  
  
In ChatGPT, a **tenant** is your organization's top-level admin environment. It connects your company's ChatGPT workspaces and organizations to shared identity settings, such as verified domains and single sign-on.  
  
  
**Domain verification** lets ChatGPT recognize your organization's domain as trusted. It also enables identity features such as SSO, so users can access the right workspace using your company's authentication system.  
  
Use the **Global Admin Console** to manage tenant-level identity settings, including SSO and domain settings. Complete this setup early, before adding users at scale, so employees join the workspace with the right access controls already in place.  
  
Read more:

* [Domain Verification](https://help.openai.com/articles/8871611)
* [Global Admin Console](https://help.openai.com/articles/12289294)

## 3. Set up SSO and SCIM before broad onboarding

Decide how employees will sign in and how their accounts will be managed over time. For example, determine whether users will sign in with single sign-on, whether SSO should be required for all eligible users, and whether accounts will be added manually or managed automatically through Directory Sync.  
  
For most large Enterprise rollouts, set up SSO and Directory Sync (SCIM) before inviting users broadly. SSO lets employees use your company's identity provider to sign in, while SCIM keeps ChatGPT membership aligned with your source directory. It can automatically create, update, and remove workspace accounts and invitations as employees join, move teams, or leave the company.  
  
Synced groups can also support role assignment, helping admins manage access at scale instead of updating each user individually.  
  
Read more:

* [Getting started with identity and provisioning in ChatGPT Enterprise, Edu, and ChatGPT for Teachers](https://help.openai.com/articles/9672121)
* [SCIM Integration FAQ](https://help.openai.com/articles/10011769)
* [SSO Overview](https://help.openai.com/articles/10468051)
* [Understanding Your Ideal User Management Setup](https://help.openai.com/articles/10479654)

## 4. Create groups and assign RBAC

Before inviting users broadly, decide how you want to organize access across the workspace. Groups make it easier to manage permissions for many users at once, especially as people join, change teams, or leave the company.  
  
A group by itself does not automatically give users permissions in ChatGPT. Instead, groups can be assigned roles for tenant-level or workspace-level resources, and they can also be used to control who can access shared GPTs. This lets admins manage access by team, function, or responsibility instead of updating each user one by one.  
  
Set this up early so your workspace starts with a clear access model. If users are added before groups and roles are planned, admins may need to clean up inconsistent permissions later, and users may receive broader or narrower access than intended.  
  
Read more:

* [Groups in ChatGPT Enterprise and Edu](https://help.openai.com/articles/9083985)
* [RBAC](https://help.openai.com/articles/11750701)

## 5. Configure workspace settings and user guidance

Review your [general workspace settings](https://chatgpt.com/admin): workspace appearance, name, workspace identifiers, public display name, Workspace Instructions, and user-facing guidance before launch.  
  
Before launch, review the parts of the workspace that employees will see first: the workspace name, appearance, identifiers, public display name, Workspace Instructions, and any user-facing guidance.  
  
These details help users recognize that they are in your organization's approved ChatGPT Enterprise workspace, not a personal or unmanaged environment. They also give employees useful context before they begin working, such as how your organization expects ChatGPT to be used, what kinds of data are appropriate, and where to go for help.  
  
Use **Workspace Policy** to present your organization's AI policy, usage expectations, or other important guidance to members before they start using ChatGPT.  
  
Read more:

* [Managing workspace settings in ChatGPT Enterprise](https://help.openai.com/articles/8411955)

## 6. Enable Apps, GPTs, and approved data connections

ChatGPT regularly adds new features, capabilities, and ways to connect with external tools. Some of these features may require admin decisions about data access, sharing, external services, or write actions. Setting a baseline early helps users get the tools they need while keeping usage aligned with your organization's policies.  
  
Before launch, review which ChatGPT capabilities should be available to users on day one and which should be limited, staged, or enabled later. Workspace owners can control this in [Permissions and Roles](https://chatgpt.com/admin/permissions).  
  
For permissions, distinguish between the **default workspace role** and **role-based access control (RBAC)**. The default workspace role is the baseline role users receive when they join the workspace. Use it to define what most members should be able to do by default. RBAC is for more targeted access: admins can assign specific roles to users or groups for particular responsibilities, resources, or admin capabilities. In practice, use the default workspace role for the broad member experience, and use RBAC for specialized access such as builders, publishers, sensitive teams, or administrators.  
  
Because new functionality may become available over time, revisit these settings regularly as features are added and your organization's needs change.  
  
Read more:

* [Admin Controls, Security, and Compliance in apps](https://help.openai.com/articles/11509118)
* [Apps in ChatGPT](https://help.openai.com/articles/11487775)
* [ChatGPT apps with sync](https://help.openai.com/articles/10847137)
* [Configuring actions in GPTs](https://help.openai.com/articles/9442513)
* [Creating and editing GPTs](https://help.openai.com/articles/8554397)
* [Developer mode and MCP apps in ChatGPT](https://help.openai.com/articles/12584461)
* [Managing GPT access in Enterprise and Edu workspaces](https://help.openai.com/articles/8555535)

## 7. Enable Codex for the right teams

Codex is OpenAI's agent for working with code, files, and structured workflows. It can help users write, understand, review, and improve code, but it can also support work beyond traditional software development.  
  
Before launch, decide which users or groups should have access to Codex and what level of access they need. Codex capabilities may evolve over time, so focus on the broader access model rather than only the specific settings available today.  
  
Consider which teams should be able to use Codex, which users should manage Codex settings, and which activities should require additional review or approval. You may also want to define different access levels for general users, early adopters, administrators, or teams with more sensitive workflows.  
  
Use RBAC and groups to keep access targeted and easier to maintain. For example, you might create one group for Codex users and a smaller administrator group for people responsible for Codex rollout, settings, policies, reporting, and governance.  
  
Set this up before launch so Codex access starts from a clear baseline. As new Codex capabilities become available, revisit your access model and decide whether they should be enabled broadly, limited to specific groups, or introduced in phases.  
  
Read more:

* [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143)
* [Codex Security](https://help.openai.com/articles/20001107)
* [Deploy ChatGPT workspace agents to Slack - Admin Setup](https://help.openai.com/articles/20001236)
* [Using Codex with your ChatGPT plan](https://help.openai.com/articles/11369540)

## 8. Configure required security and compliance controls

Decide which controls are required for your organization's risk model. Not every organization needs every control, but required controls should be configured before users begin working with sensitive data in ChatGPT Enterprise.  
  
Common controls include:

* Compliance Logs Platform and Stateful Compliance API for audit, SIEM, eDiscovery, or DLP workflows.
* IP allowlisting for workspace access and Compliance API access.
* Lockdown Mode for teams that need stronger restrictions on web, search, browsing, and related networked capabilities.
* Enterprise Key Management for customer-managed encryption where available.
* Data residency or inference residency where required.
* Managed mobile access through ChatGPT for Intune, which requires an active tenant SSO connection.

Read more:

* [Data residency and inference residency for ChatGPT](https://help.openai.com/articles/9903489)
* [IP allowlisting for ChatGPT](https://help.openai.com/articles/12111596)
* [Lockdown Mode](https://help.openai.com/articles/20001061)
* [OpenAI Compliance Platform for Enterprise and Edu Customers](https://help.openai.com/articles/9261474)
* [OpenAI Enterprise Key Management (EKM) Overview](https://help.openai.com/articles/20000943)
* [Setting up ChatGPT for Intune](https://help.openai.com/articles/20001232)

## 9. Monitor adoption, usage, and support readiness

Launching the workspace is the beginning of ongoing administration, not the end of setup. After users start using ChatGPT, review workspace analytics regularly to understand adoption, engagement, and feature usage. These signals can help you see where ChatGPT is being used successfully, where teams may need more guidance, and whether any settings should be adjusted over time.  
  
Use impact surveys to gather direct feedback from employees about how ChatGPT is affecting their work. Analytics can show what is being used; surveys can help explain whether users are saving time, improving work quality, or running into friction.  
  
Review usage controls deliberately. Configure weekly per-user usage alerts or hard limits based on your organization's policies. Use monthly shared budgets only when a role should share one overall cap. In most cases, start with alerts so admins can monitor usage patterns before deciding whether a hard limit is needed.  
  
Finally, make sure admins know how to get help when issues come up. Before contacting Support, gather useful context such as the affected users, timing, screenshots, relevant conversation or GPT links, prompts, and sanitized files when relevant. This helps Support investigate faster and gives your internal admins a clearer process for handling workspace questions over time.  
  
Read more:

* [How can I contact support?](https://help.openai.com/articles/6614161)
* [Managing impact surveys in workspace analytics](https://help.openai.com/articles/20001149)
* [OpenAI Status](https://status.openai.com/)
* [Setting usage limits for custom roles in ChatGPT Enterprise](https://help.openai.com/articles/20001001)
* [Workspace analytics for ChatGPT Enterprise and Edu](https://help.openai.com/articles/10875114)

# What to do next

After the initial rollout, revisit these settings on a regular cadence:

* Review Owners, Admins, Analytics Viewers, and custom roles.
* Confirm SCIM groups still match your organization structure.
* Audit enabled Apps/connectors, write or open-world actions, allowed OAuth domains, Apps in GPTs, and GPT action domains.
* Review Workspace Agent and Codex access as teams expand usage.
* Review analytics and impact survey results with rollout stakeholders.
* Adjust usage alerts or limits based on observed usage patterns.
* Reconfirm security and compliance controls after major policy or product changes.
