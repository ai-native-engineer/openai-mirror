<!-- source: https://help.openai.com/en/articles/11165333-chatgpt-enterprise-and-edu-models-and-limits -->

# ChatGPT Enterprise and Edu models and limits

Understand which models are best suited for your tasks.

Updated: 4 hours ago

GPT‑6 Pro, powered by GPT‑6 Astra, is available in ChatGPT for Pro $100, Pro $200, Business and Enterprise plans. Enterprise access also depends on your workspace’s model-access permissions. Plus plans include GPT‑6 Astra in ChatGPT Work and Codex.

**Note**: Astra requires Codex CLI version **0.153.0 or newer**. Additionally, please update to the latest available ChatGPT Desktop app. If you do not see Astra available in Chat, Work or Codex in the desktop app, ensure that you update your app by clicking Menu > Check for Updates, even if you recently updated the app due to an automatic update notification or by clicking on the update icon in the sidebar.

*Enterprise and Edu members can use the models currently enabled for their workspace. Model availability and limits change over time, so the model picker and workspace settings are the source of truth for current access.*

For more information, please refer to our article: [*Retiring GPT-4o and other ChatGPT models*](https://help.openai.com/articles/20001051)

[ChatGPT Enterprise](https://openai.com/chatgpt/enterprise/) is a subscription plan which offers enterprise-grade security and privacy, access to eligible current models, native tools like apps, deep research, data analysis, file uploads, canvas, projects, search, advanced voice, and image generation, customization options, and much more.

[Learn how ChatGPT can transform your organization.](https://openai.com/contact-sales/)

If you are on ChatGPT flexible pricing, please refer to this [page](/en/articles/11481834-chatgpt-rate-card) for the latest rates on our models, features, and products.

Model access in Enterprise and Edu is controlled through workspace settings and RBAC. Admins and owners can review access in [workspace settings](https://chatgpt.com/admin/permissions). The options members see can vary by rollout and workspace configuration.

# Model picker

The model picker uses simplified controls to help members choose the balance of speed and reasoning effort that works best for their task. Note that the model options shown in the picker depend on workspace settings and rollout status.

* Instant — Fast responses for everyday work. The underlying model can change as newer models roll out.
* Medium — Standard reasoning for tasks that benefit from more deliberate analysis.
* High — Extended reasoning for more complex, multi-step work.
* Extra High — The highest available reasoning effort for especially demanding tasks.
* **Pro Standard —** A Pro-tier option with standard reasoning effort, when available.
* Pro Extended — A Pro-tier option with extended reasoning effort, when available.

On iOS and Android, the picker appears at the top of the conversation. On web, it appears in the message composer.

The picker labels do not change the underlying models, context windows, usage limits, or credit rates. For workspaces using flexible pricing, see the [ChatGPT Rate Card](/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu).

## Manage automatic routing for reasoning

Enterprise and Edu admins may have automatic-routing controls under Workspace settings > Models. Available controls and their names can vary by workspace and rollout.

To update this setting:

1. Go to **Workspace settings**.
2. Under Models, review the available automatic-routing controls.

Automatic routing applies only when the selected chat experience routes a request to reasoning. Members can still choose any reasoning options enabled for them.

## Unlimited access

The ChatGPT Enterprise plan offers virtually unlimited messages for eligible base models. However, usage must adhere to our [Services Agreement](https://openai.com/policies/services-agreement/), which prohibits, among other things:

* Abusive usage, such as automatically or programmatically extracting data.
* Sharing your account credentials or making your account available to anyone else.
* Reselling access or using ChatGPT to power third-party services.

We have guardrails in place to help prevent misuse and are always working to improve our systems. This may occasionally involve a temporary restriction on your usage. We will inform you when this happens, and if you think this might be a mistake, please don’t hesitate to reach out to our support team. If policy-violating behavior is not found, your access will be restored.

## Model access controls in workspace settings

In eligible ChatGPT Enterprise and Edu workspaces, GPT-6 Astra is off by default at launch. Workspace owners can enable it for the workspace or for specific roles through the model access controls in workspace settings.

Existing Early Model Access settings do not carry over to Astra. Having Early Model Access turned on does not automatically give members access to Astra.

If a member cannot see Astra in the model picker, check their model-access permissions and all assigned roles. A role that allows access can keep it enabled even if another role turns it off. You can only choose a workspace default from models available to your workspace.

The two-week admin preview process is not available for Astra at launch. Access will not automatically turn on two weeks after launch.

Choosing a starting or default model does not grant access to a model the member cannot use. For help managing roles, see [Role Based Access Controls for ChatGPT Enterprise](/en/articles/11750701-rbac/).

# Check a member’s model access

If a member’s model access differs from what you expect, admins can use Model Test to inspect which models the member can use and the settings that contribute to their access.

1. Open [**Admin console**](https://admin.openai.com) and select the ChatGPT workspace.
2. Open **Models**, then select **Test**.
3. Search for the member by name or email.
4. Review their effective model access, workspace defaults, model permissions, roles, and preferences.

Results reflect saved settings. Testing does not enable a model, change permissions or usage limits, or override the member’s seat type, workspace plan, or model eligibility.

Use the results to identify which workspace or role setting needs review.

For permission behavior, see: [Role-based access control in ChatGPT Enterprise](https://help.openai.com/articles/11750701).
