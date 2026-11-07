<!-- source: https://help.openai.com/en/articles/11165333-chatgpt-enterprise-and-edu-models-and-limits -->

# ChatGPT Enterprise and Edu models and limits

Understand which models are best suited for your tasks.

Updated: 7 days ago

GPT-6 is rolling out in Chat to eligible Enterprise workspaces. If you don’t see **GPT-6** in the model menu, it may not be available for your workspace yet.

GPT‑6 Pro, powered by GPT‑6 Astra, is available in ChatGPT for Pro $100, Pro $200, Business and Enterprise plans. Enterprise access also depends on your workspace’s model-access permissions. Plus plans include GPT‑6 Astra in ChatGPT Work and Codex.

Astra requires Codex CLI version **0.153.0 or newer**. If you do not see Astra in Chat, Work, or Codex in the desktop app, open **Menu > Check for Updates** and install the latest available version. Check manually even if you recently updated through an automatic update notification or the update icon in the sidebar.

[ChatGPT Enterprise](https://openai.com/chatgpt/enterprise/) is a subscription plan which offers enterprise-grade security and privacy, access to eligible current models, native tools like apps, deep research, data analysis, file uploads, canvas, projects, search, advanced voice, and image generation, customization options, and much more.

[Learn how ChatGPT can transform your organization.](https://openai.com/contact-sales/)

For rates, see the [credit-based rate card](https://help.openai.com/articles/11481834) or the [Enterprise token-based rate card](https://help.openai.com/articles/20001415), depending on your agreement. For billing concepts and eligibility, see: [Token-based billing for ChatGPT Enterprise](https://help.openai.com/articles/20001520).

Model access in Enterprise and Edu is controlled through workspace settings and RBAC. Admins and owners can review access in [workspace settings](https://chatgpt.com/admin/permissions). The options members see can vary by rollout and workspace configuration.

## GPT-6 in Enterprise Chat

**GPT-6** in Chat uses your workspace’s existing **GPT-6 Sol** access setting for **Instant** through **Extra High**. Workspaces with Sol enabled can receive access during the rollout.

Admins can turn off Sol access. A member’s access still depends on model eligibility, workspace settings, and all assigned roles. **Pro** remains GPT-6 Pro and uses the separate **GPT-6 Astra** access control.

With GPT-6 in Chat, Intelligent UI can combine text, visuals, and interactive elements when useful. Responses may begin while ChatGPT continues thinking, followed by more detail. These capabilities are rolling out on the web and supported updated apps at **Instant** through **Extra High**, subject to workspace access. They are not available with **Pro** effort.

For supported clients and the **Layout and visuals** setting on the web, see: [GPT-6 and other models in ChatGPT](https://help.openai.com/articles/20001354).

# Models in Work and Codex

**GPT-6 Sol**, GPT-6.1 Sol, and GPT-6 Luna are separate model options for Work and Codex. In Chat, **GPT-6 Sol** powers **GPT-6** at **Instant** through **Extra High** as it rolls out to eligible Enterprise workspaces. GPT-6.1 Sol and GPT-6 Luna are not selectable in regular Chat. Model access can be off by default. An admin must enable any model that is disabled before members can use it. Workspace settings and assigned roles determine each member’s access.

Your workspace’s settings determine which options are available to you.

The slider shows only models and reasoning options available to you.

The models a member can use depend on the workspace’s model-access settings and assigned roles. Check the model picker for enabled options. If a model is missing, admins can use Model Test, described below, to review the member’s access and the settings that determine it.

For more about these experiences, see: [ChatGPT Work and Codex](https://help.openai.com/articles/20001275).

# Model picker in Chat

In the model menu, **GPT-6** replaces **Latest.** Existing **Latest** selections move to **GPT-6** at the same effort; explicit **GPT-5.6 Sol** selections stay on GPT-5.6. When **GPT-6** is selected, **GPT-6 Sol** powers **Instant** through **Extra High**; **Pro** uses GPT-6 Pro, powered by **GPT-6 Astra**. Available options depend on workspace settings, model access, and rollout status.

* **Instant —** Fast responses for everyday work. Powered by **GPT-6 Sol** when **GPT-6** is selected.
* **Medium —** Standard reasoning for tasks that benefit from more deliberate analysis.
* **High —** Extended reasoning for more complex, multi-step work.
* **Extra High —** The highest available reasoning effort for especially demanding tasks.
* **Pro** — Uses GPT-6 Pro, powered by GPT-6 Astra. Depending on availability, Pro reasoning controls may include **Pro Standard** for standard reasoning and **Pro Extended** for extended reasoning.

On iOS and Android, the picker appears at the top of the conversation. On web, it appears in the message composer.

In ChatGPT Enterprise and Edu workspaces that aren’t configured for specialized medical routing, **Instant** no longer automatically switches to a higher thinking level.

To use a higher thinking level in Chat, select an available option in the model picker. The options you see depend on your workspace’s model-access settings and assigned roles.

Legacy models may still route requests automatically for safety or personal finance features.

For help managing access, see: [Role-based access control in ChatGPT Enterprise](https://help.openai.com/articles/11750701).

For credit-based workspaces, see: [ChatGPT Rate Card (Business, Enterprise/Edu credit-based pricing)](https://help.openai.com/articles/11481834). For Enterprise agreements with token-based USD billing, see: [ChatGPT Rate Card (Enterprise token-based pricing)](https://help.openai.com/articles/20001415).

## Note on unlimited access

The ChatGPT Enterprise plan offers virtually unlimited messages for eligible base models. Model access and virtually unlimited messages do not mean zero-dollar usage. On Enterprise agreements with token-based USD billing, usage, including Instant, is billable at your applicable rates. However, usage must adhere to our [Services Agreement](https://openai.com/policies/services-agreement/), which prohibits, among other things:

* Abusive usage, such as automatically or programmatically extracting data.
* Sharing your account credentials or making your account available to anyone else.
* Reselling access or using ChatGPT to power third-party services.

We have guardrails in place to help prevent misuse and are always working to improve our systems. This may occasionally involve a temporary restriction on your usage. We will inform you when this happens, and if you think this might be a mistake, please don’t hesitate to reach out to our support team. If policy-violating behavior is not found, your access will be restored.

## GPT-6 Astra access controls

In eligible ChatGPT Enterprise and Edu workspaces, **GPT-6 Astra** is off by default at launch. Workspace owners can enable it for the workspace or for specific roles through the model access controls in workspace settings.

Existing Early Model Access settings do not carry over to Astra. Having Early Model Access turned on does not automatically give members access to Astra.

If a member cannot see Astra in the model picker, check their model-access permissions and all assigned roles. A role that allows access can keep it enabled even if another role turns it off. You can only choose a workspace default from models available to your workspace.

The two-week admin preview process is not available for Astra at launch. Access will not automatically turn on two weeks after launch.

Choosing a starting or default model does not grant access to a model the member cannot use. For help managing roles, see: [Role Based Access Controls for ChatGPT Enterprise](https://help.openai.com/articles/11750701).

# Check a member’s model access

If a member’s model access differs from what you expect, admins can use Model Test to inspect which models the member can use and the settings that contribute to their access.

1. Open [**Admin console**](https://admin.openai.com) and select the ChatGPT workspace.
2. Open **Models**, then select **Test**.
3. Search for the member by name or email.
4. Review their effective model access, workspace defaults, model permissions, roles, and preferences.

Results reflect saved settings. Testing does not enable a model, change permissions or usage limits, or override the member’s seat type, workspace plan, or model eligibility.

Use the results to identify which workspace or role setting needs review.

For permission behavior, see: [Role-based access control in ChatGPT Enterprise](https://help.openai.com/articles/11750701).
