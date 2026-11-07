<!-- source: https://help.openai.com/en/articles/20001506-using-openai-models-in-cursor -->

# Using OpenAI models in Cursor

Learn how to use OpenAI models in Cursor with your own API key, the Codex IDE extension, or an AI gateway provider.

Updated: 11 days ago

OpenAI is planning to wind down our contract providing OpenAI models to [Cursor](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/). We have proposed a transition period of November 12, 2026. During that period, we would continue providing Cursor access to the OpenAI models it uses today. Cursor may choose to end access sooner. We will share the official termination date as soon as it is confirmed between both companies.

To continue using OpenAI models inside the Cursor app, choose the option that best fits your workflow:

* **Bring your own OpenAI API key** — continue using OpenAI models in Cursor’s local Chat and Agent features, billed at [OpenAI API prices](https://developers.openai.com/api/docs/pricing).
* **Use the Codex IDE extension** — use Codex directly inside Cursor with a [ChatGPT subscription](https://learn.chatgpt.com/docs/pricing) or an OpenAI API key.
* **Use an AI gateway provider** — connect Cursor to OpenAI models through an account you have with a compatible provider such as Amazon Bedrock, Azure, or another OpenAI-compatible gateway.

The following guidance is directional and Cursor might change the functionality and availability of these features over time. Please refer to Cursor’s official documentation for the latest information.

These options cover local work in the Cursor desktop app. Cursor doesn’t support “Bring your own key” in Cursor Tab, Auto, Cloud or Background Agents, Automations, the Cursor CLI, or Cursor’s API and SDK. Those features use models supplied or routed by Cursor and cannot use your OpenAI API key or gateway credentials.

## Bring your own OpenAI API key

Cursor supports using your own OpenAI API key for OpenAI models in its local Chat and Agent features. Requests are sent through your OpenAI API account and billed separately from your Cursor or ChatGPT subscription.

To configure your key:

1. [Create an OpenAI API key](https://platform.openai.com/api-keys). API access requires an OpenAI API account with billing configured.
2. Open **Cursor Settings**, then select **Models**.
3. Find the OpenAI API key setting, paste your key, and save or verify it.
4. Enable the OpenAI model you want to use.
5. Select that model in Cursor Chat or Agent.

Available models and usage limits depend on your OpenAI API organization.

Your OpenAI API key applies only to supported local Chat and Agent requests. It does not apply to:

* Cursor Tab and autocomplete
* Auto model selection and routing
* Cloud or Background Agents
* Automations
* Cursor CLI
* Cursor API or SDK
* Cursor-provided or proprietary models

A ChatGPT subscription does not include OpenAI API usage. If you use an API key, [usage is billed through your OpenAI API account](https://developers.openai.com/api/docs/pricing).

## Use the Codex IDE extension in Cursor

The [Codex IDE extension](https://developers.openai.com/codex/ide) lets you use the Codex agent directly inside Cursor. It runs as a separate extension and does not depend on OpenAI models being available through Cursor’s own model picker.

To get started:

1. Open the Codex IDE extension page linked above and select Cursor to install the extension.
2. Open Codex from the **Activity Bar**.
3. Select **Sign in with ChatGPT** to use an eligible ChatGPT subscription, or select **Use API Key** to use an OpenAI API account.
4. Open your project and start a task from the Codex panel.

You can move the Codex panel to the right side of the editor using Cursor’s layout controls. Enable the **Secondary Side Bar** from the **View > Appearance** menu, then drag the Codex view into it.

The Codex extension provides its own agent experience inside Cursor. It does not change the model used by Cursor Chat, Agent, Tab, Auto, Cloud Agents, or other Cursor services. See [Codex authentication](https://developers.openai.com/codex/auth) for the available sign-in methods.

## Use an AI gateway provider

You can also connect Cursor to OpenAI models through a compatible AI gateway or hosting provider. This can be useful if your organization already manages model access and billing through Amazon Bedrock, Azure, or another gateway.

Cursor can connect through provider-specific settings or through a custom OpenAI-compatible base URL. Services such as OpenRouter or Vercel AI Gateway may work when configured with a compatible API, but available models and features depend on the provider.

The exact configuration varies, but the general setup is:

1. Provision the OpenAI model with your provider.
2. Create the required credentials, endpoint, and model or deployment name.
3. Open **Cursor Settings**, then select **Models**.
4. Choose the provider integration, or configure the OpenAI API settings with the gateway’s custom base URL.
5. Enter the endpoint and credentials supplied by your provider.
6. Add or enable the corresponding model in Cursor.
7. Test the model in a local Chat or Agent session.

For Amazon Bedrock, see [Use OpenAI models with Amazon Bedrock](https://developers.openai.com/api/docs/guides/amazon-bedrock).

Gateway compatibility varies. A custom endpoint must support the API format Cursor expects, and some model-specific controls may not be available or forwarded through a custom base URL. Gateway credentials also cover only supported local Chat and Agent requests; they do not apply to Cursor Tab, Auto, Cloud or Background Agents, Automations, the Cursor CLI, or Cursor’s API and SDK.
