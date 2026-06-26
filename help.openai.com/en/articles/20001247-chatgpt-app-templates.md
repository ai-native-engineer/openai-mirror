<!-- source: https://help.openai.com/en/articles/20001247-chatgpt-app-templates -->

# ChatGPT app templates

Learn how workspace admins and owners can turn an app template into a workspace-specific app for their organization.

Updated: 9 days ago

# Overview

App templates are a setup path for Business and Enterprise workspaces that need a workspace-specific version of a ChatGPT app or connector. Instead of enabling one shared app from the directory, a workspace admin or owner starts from an OpenAI-provided template, adds the details unique to their organization, and creates a draft app for review.  
  
Templates are useful when OpenAI can provide the common app behavior, but each workspace must provide provider-specific configuration. Depending on the template, that configuration can include a tenant or host name, OAuth client credentials, callback URLs, scopes, webhook details, managed MCP server URLs, or other provider settings. For example, a GitHub Enterprise template may create the workspace-specific connector Codex uses to reach that organization's GitHub Enterprise host.  
  
After setup, members do not use the original template. They use the published workspace app created from it. Admins can then manage that app like other ChatGPT apps, including role access, action controls, app permissions, and provider authorization.  
  
  
[Codex plugins](https://developers.openai.com/codex/plugins) can also include app templates or apps created from templates. If a plugin includes an app template, a workspace admin or owner still needs to create and publish the workspace-specific app before members can connect it in ChatGPT, and use it through that plugin. When the plugin runs, it uses the app instance available in that workspace rather than asking members to configure the original template themselves. If the required template has not been set up yet, members may need an admin to complete setup first. The plugin cannot use an app template by itself.  
  
Use this article for the general template flow. For provider-specific setup, see:

* [GitHub Enterprise](https://help.openai.com/articles/20001248)
* [Snowflake](https://help.openai.com/articles/20001249)
* [Databricks](https://help.openai.com/articles/20001250)

Templates are useful when the same app pattern can work across many organizations, but each organization needs its own configuration.  
  
Common examples include:

* The provider URL includes a company tenant, account, organization, or workspace hostname.
* The organization needs to bring its own OAuth client or provider credentials.
* The provider requires customer-specific callback URL setup.
* The app should use the same implementation pattern, while each workspace controls access, actions, and security settings separately.

## How templates differ from [regular apps](https://help.openai.com/articles/11487775)

A regular app can usually be enabled directly from the app directory. A template starts a setup flow instead.  
  
The usual flow is:

1. An admin finds a template in the app directory.
2. The admin enters the required workspace-specific configuration.
3. ChatGPT creates a draft app for the workspace.
4. The admin reviews and publishes the draft.
5. The admin configures access and action settings for the published app.

Members use the published workspace app, not the original template.

# Find and set up an app template

1. Open **Workspace settings > Apps**.
2. Select **Directory**.
3. Search for the provider or app name.
4. Look for entries marked as templates.
5. Select **Enable** to start the setup flow.

The setup flow asks for the details needed to create the workspace-specific app. The exact fields depend on the template.  
  
For example, a GitHub Enterprise template may ask for details such as:

* App name and description.
* GitHub Enterprise hostname.
* Callback URL configuration.
* OAuth client ID and client secret.
* GitHub App private key.
* Requested scopes.
* Webhook setup details.

Review each field carefully before creating the draft. If your organization manages OAuth or provider credentials centrally, coordinate with the team that owns those credentials.  
  
See app-specific instructions: [GitHub](https://help.openai.com/articles/20001248), [Snowflake](https://help.openai.com/articles/20001249), and [Databricks](https://help.openai.com/articles/20001250).

## OAuth client setup

Some templates require your organization to bring its own OAuth client. When this is required, create or configure the OAuth app in the external provider's admin console, then copy the callback URL from ChatGPT into the provider's redirect or callback URL settings.  
  
Enter the OAuth client ID and secret in ChatGPT only after confirming that the provider configuration matches the template setup instructions.  
  
If the template includes default scopes, keep the defaults unless your organization has reviewed the provider permissions and has a clear reason to change them.

## Create a draft

After entering the required information, select **Create draft**.  
  
Creating a draft does not automatically make the app available to members. Review the draft, publish it, and configure access and action settings before asking members to use it.

## Publish and manage the resulting app

After publishing, manage the workspace-specific app from **Workspace settings > Apps > Enabled**.  
  
Recommended post-publish checks:

1. Confirm the app appears in **Enabled apps**.
2. Set **User access** for the roles that should use the app.
3. Review **Action control** for read and write actions.
4. Review **App permissions** to choose when ChatGPT asks members before using the app.
5. Ask an allowed test user to open Apps in ChatGPT and confirm the app appears.
6. If the app requires provider authentication, have the test user connect their provider account.
7. Run a low-risk test prompt to confirm the app works as expected.

These app permissions apply to ChatGPT conversations. Workspace Agents use per-agent controls set by the agent's builder to determine which app actions are available and when end users are asked to approve them. For agent behavior, see: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).

## If a template can only be used once

Some templates may create only one app per workspace. If a template was already used, the **Enable** button may be unavailable. In that case, manage the existing draft or published app instead of creating another one from the same template.

# What members see

Members see the published app created from the template. Whether a member can see or use it depends on workspace settings and provider authorization. If the app is included in a plugin, members may encounter it through that plugin, but the same workspace access and provider authorization requirements still apply.  
  
Check that:

* The app is published.
* The app is enabled for the workspace.
* The member's workspace role has access.
* The member is in the correct workspace.
* The member has the required permissions in the external provider.

Published apps will appear in the ChatGPT app directory, in the workspace specific section.

# Troubleshooting

If setup fails or the app does not appear, confirm the following:

1. The tenant, account, or workspace hostname is correct.
2. The callback URL was copied exactly into the provider configuration.
3. The OAuth client ID and client secret are correct.
4. Requested scopes match what the provider OAuth app allows.
5. A draft was created.
6. The draft was published.
7. Role access allows the test user to see the app.
8. Provider-side permissions allow the data or action being tested.

## Security notes

* Treat OAuth client secrets and provider credentials as sensitive information.
* Review requested scopes before creating the draft.
* Use **Action control** after publishing to limit what the app can do.
* Use **App permissions** to decide when ChatGPT asks members before using the app.
* Note that provider permissions still apply after the app is enabled in ChatGPT.
