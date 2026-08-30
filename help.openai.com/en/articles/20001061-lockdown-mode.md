<!-- source: https://help.openai.com/en/articles/20001061-lockdown-mode -->

# Lockdown Mode

Learn how Lockdown Mode limits access to the web and external services to help reduce data exfiltration risk from prompt injection attacks.

Lockdown Mode may be available to eligible personal accounts, self-serve ChatGPT Business accounts, and supported managed workspaces. Availability depends on your account, workspace, current product rollout, and administrator settings.

Lockdown Mode is an optional advanced security setting that limits many tools and capabilities in OpenAI products that can connect to the web or external services. It is designed to reduce the risk of data exfiltration from [prompt injection](https://openai.com/safety/prompt-injections/) attacks by limiting outbound network requests, at the expense of disabling or limiting some useful features.

Lockdown Mode is not intended for everyone. It is designed for people and organizations that handle sensitive data and want stricter protection from data exfiltration risks related to [prompt injection](https://openai.com/safety/prompt-injections/).

## Availability

Lockdown Mode requires a signed-in account and is available only where supported for your plan, workspace, product surface, and administrator configuration.

# How Lockdown Mode helps reduce data exfiltration risk

[Prompt injection](https://openai.com/safety/prompt-injections/) is a challenging research problem. We are continually working to harden our multi-layered security and safety systems to protect users from such attacks.

Lockdown Mode builds on protections across the model, product, and system levels. This includes sandboxing, [protections against URL-based data exfiltration](https://openai.com/index/ai-agent-link-safety/), monitoring and enforcement, and enterprise controls like role-based access and audit logs.

Lockdown Mode is designed to help prevent the final stage of data exfiltration from a [prompt injection](https://openai.com/safety/prompt-injections/) attack by limiting outbound network requests that could transfer sensitive data to an attacker. Lockdown Mode does not prevent prompt injections from appearing in the content ChatGPT processes. For example, a prompt injection could appear in cached web content or in an uploaded file, and could still affect the behavior or accuracy of a response.

Lockdown Mode disables or limits the following capabilities of OpenAI products:

* Live web browsing: Web browsing is limited to cached content. Search results may be limited, unavailable, or stale.
* Image support: ChatGPT may not display images in regular responses or retrieve images from the web. Users can still upload image files, and image generation remains available where it is otherwise available.
* Deep research: Deep research is disabled.
* Agent mode: Agent mode is disabled.
* Canvas networking: Users cannot approve Canvas-generated code to access the network.
* File downloads: ChatGPT cannot download files for data analysis. ChatGPT can still operate on your manually uploaded files.

Lockdown Mode does not change memory, file uploads, the ability to share a conversation, or whether your conversations may be used to improve models. Many of these settings are separately configurable by workspace admins.

Lockdown Mode does not affect network access in Codex.

# Apps

How apps and connectors work in Lockdown Mode depends on your account type and workspace settings.

For personal accounts and self-serve ChatGPT Business accounts, Lockdown Mode blocks live access to external services and connector write actions when those actions conflict with its security protections. Individual accounts cannot configure app sync. In an eligible managed workspace, access to an existing administrator-managed source also depends on workspace permissions and the current Lockdown Mode policy. Some connected experiences, including Finances in ChatGPT and shopping-agent experiences, are unavailable in Lockdown Mode.

For managed workspaces, apps, MCPs, and connectors are controlled by workspace settings and role-based access controls. Lockdown Mode does not automatically disable every app in these workspaces. Workspace admins should enable only the trusted apps and actions that members using Lockdown Mode need.

For managed workspace troubleshooting, review the member's role and app settings together. A member may be unable to use an app, connector, MCP, or action if:

* the member or group is assigned to a Lockdown Mode role that limits the required capability
* the app is not assigned to the member, group, or role
* the required read or write action is not enabled
* the member does not have access to the underlying file, repository, channel, record, or source system
* another role grants the required capability, but a Lockdown Mode role still restricts it. A workspace owner must remove the member or group from the Lockdown Mode role to restore access.

App access in ChatGPT does not override permissions in the connected source system. For more information about assigning roles, see: [RBAC](https://help.openai.com/articles/11750701).

When configuring apps for members using Lockdown Mode, admins should consider the data exfiltration risk of each app and action.

## High risk

These apps and actions are not recommended for users in Lockdown Mode:

* Read or write actions for untrusted apps are not recommended. Enable only apps you trust.
* Write actions for trusted apps with broad or uncertain visibility are not recommended. Avoid enabling write actions, even for trusted apps, if you cannot confirm that the side effect is hidden from a malicious actor.

## Medium risk

Use these with caution for users in Lockdown Mode:

* Administrator-managed indexed sources can reduce some outbound network requests because content is retrieved from an existing index rather than a live provider call. They can still expose sensitive information, and availability in Lockdown Mode depends on the workspace, source, and security policy.
* Read actions for trusted apps are lower risk as a possible data exfiltration sink because they do not create write-side effects. They can still act as sources of sensitive data that a malicious actor may try to exfiltrate.
* Write actions for trusted apps with limited visibility are higher risk than read actions because they create side effects. Enable these only when you are confident that any side effect is visible only to people you trust, not to a malicious actor.

Eligible Enterprise and Edu administrators may use available Compliance Platform records to review supported app activity, subject to workspace configuration and permissions. For details, see: [OpenAI Compliance Platform for Enterprise and Edu Customers](https://help.openai.com/articles/9261474).

# Turn on Lockdown Mode

## Personal and self-serve ChatGPT Business accounts

For eligible personal accounts and self-serve ChatGPT Business accounts:

1. Go to **Settings**.
2. Select **Security**.
3. Under **Advanced security**, turn on **Lockdown Mode**.
4. In the confirmation modal, select **Turn on**.

Lockdown Mode and Developer Mode cannot be used at the same time. Turning on Lockdown Mode turns off Developer Mode. Turning on Developer Mode later turns off Lockdown Mode.

When Lockdown Mode is on, you can turn it off for one chat. On the web, select the **LOCKDOWN MODE** label in the composer, then select **Turn off for this chat**.

To change the setting from the chat menu:

1. Open the more options menu (**•••**).
2. Select **Lockdown**.
3. Select **Disabled** to turn it off for this chat, or **Enabled** to turn it back on.

To open your account’s **Security** settings, select **Manage lockdown** in the composer dialog.

## Managed workspaces

Workspace admins can create a custom role and designate it as a “Lockdown Mode” role, then assign members or groups to it.

# FAQ

## Who can turn on Lockdown Mode?

Users on eligible personal accounts and self-serve ChatGPT Business accounts can turn on Lockdown Mode in **Settings** > **Security** when it is available for their account. Workspace admins can enable Lockdown Mode for managed workspace members using role-based access controls.

## Does Lockdown Mode turn off training?

No. Lockdown Mode does not change whether your conversations may be used to improve models. You can manage this separately in data controls. Workspace data controls continue to depend on the workspace plan and settings.

## Can I use image generation in Lockdown Mode?

Yes. Lockdown Mode limits image support in regular ChatGPT responses and web-derived images, but it does not turn off image generation.

## Can I turn off Lockdown Mode for one chat?

Yes. Select the **LOCKDOWN MODE** label in the web composer, then select **Turn off for this chat**. You can also change the setting from the chat menu as described above. Either option changes only the current chat.

## Does Lockdown Mode affect Codex?

No. Lockdown Mode does not affect network access in Codex.

## Does Lockdown Mode prevent all prompt injection attacks?

Lockdown Mode is designed to substantially reduce the risk of [prompt injection](https://openai.com/safety/prompt-injections/)-based data exfiltration in ChatGPT and supported OpenAI products, but it does not guarantee data exfiltration cannot happen. Risk may remain through enabled Apps, unforeseen combinations of capabilities, or newly discovered techniques.

Lockdown Mode also does not prevent all other effects of [prompt injection](https://openai.com/safety/prompt-injections/) attacks. For example, a malicious instruction hidden in an uploaded file could still affect ChatGPT’s behavior and cause an incorrect answer.

## Is prompt injection a major risk?

Prompt injection is a known security risk when an AI system processes untrusted content. Lockdown Mode can reduce some data-exfiltration paths, but it does not prevent every prompt-injection attack or eliminate all security risks.

## Does Lockdown Mode change what gets logged in the Compliance API Logs Platform?

Lockdown Mode does not by itself change which Compliance Platform records are available. Compliance access and retention depend on the eligible workspace, administrator permissions, and applicable product settings.
