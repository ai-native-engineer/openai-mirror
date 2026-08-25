<!-- source: https://help.openai.com/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup -->

# Deploy ChatGPT workspace agents to Slack - Admin Setup

Set up Slack for ChatGPT workspace agents by configuring the required apps, permissions, and workspace settings.

ChatGPT workspace agents can be deployed to Slack, allowing users to interact with agents in Slack.

As an admin, enabling Slack deployment requires completion of three steps:

1. Add the **Workspace Agents in Slack** app in ChatGPT
2. Add the **ChatGPT Agents** app in Slack
3. Enable group management for all users in Slack settings

This page documents the process needed to enable Slack deployment as an admin. This admin setup only makes Slack deployment available for the workspace; each agent's Slack channel and reply behavior are configured later when that agent is added to Slack.

# Pre-requisites

* Your [Slack workspace must allow](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace) installation of the ChatGPT Agents app for Slack
* You must be using a [paid Slack plan](https://app.slack.com/plans)
* You must have a Business, Edu, or Enterprise ChatGPT account.

# Enabling the Workspace Agents in Slack app in ChatGPT

Install the **Workspace agents in Slack** app from [ChatGPT workspace settings](http://chatgpt.com/admin/ca#available?connector=connector_OdO9DCSRc2wYX4lGC3Ko7jbg5f7QpNum), then enable the app for your workspace.

![Workspace Agents in Slack - Admin Setup](https://images.ctfassets.net/j22is2dtoxu1/46YlHY8Cra1H4OwomVqLEC/a2c25b6eef2bf47747f379b3530a0905/Screenshot_2026-05-08_at_9.28.37%C3%A2__AM.png?q=80&fm=webp&w=944)

This is an additional ChatGPT app that must be enabled alongside the regular Slack app in ChatGPT.

# Enabling the ChatGPT Agents app in Slack

Install the **ChatGPT Agents** app in Slack by clicking [this link](https://www.chatgpt.com/chatgpt-agents-slack-app-install). You will be required to sign into your ChatGPT account if you haven’t already signed in. You will be presented with the add ChatGPT Agents to Slack modal, shown below. Review the information presented and click Continue to Slack to proceed.

You will then be directed to the Slack authentication flow, where you can review and grant the app the required permissions. Depending on your workspace settings, this may require an approval [from a Slack admin](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace).

Note that if your Slack workspace uses Slack Enterprise Grid, you need to follow [these instructions](/en/articles/20001199-chatgpt-agents-app-in-slack#installation-for-slack-enterprise-grid-organizations) to create the required org-level Slack approval and workspace-level Slack connection.

# Enable anyone to create user groups in Slack settings

Slack user group management must be enabled for all Slack users in order to use workspace agents in Slack. This is because workspace agents create a user group to @mention each agent that is deployed to Slack.

![Workspace Agents in Slack 2](https://images.ctfassets.net/j22is2dtoxu1/1fJ7nwRGjgVmq9qUMavHYF/cab388db5bab7a4eecf361db5d48ef9a/CleanShot_2026-05-08_at_10.24.20_2x.png?q=80&fm=webp&w=1344)

To enable user group management, follow [these instructions](https://slack.com/help/articles/115004952926-Manage-user-groups-from-the-admin-dashboard) in the Slack help center.
