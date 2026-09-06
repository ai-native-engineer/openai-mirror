<!-- source: https://help.openai.com/en/articles/20001512-using-zendesk-in-chatgpt-and-codex -->

# Using Zendesk in ChatGPT and Codex

Learn how to connect the OpenAI-developed Zendesk plugin and use it with your support information.

Updated: 2 days ago

## Overview

The Zendesk plugin is designed to help you review support tickets and customer history, find relevant knowledge, and prepare replies. The capabilities available to you depend on your product surface, workspace settings and Zendesk permissions.

## Before you begin

You need access to the Zendesk plugin in the ChatGPT account or workspace you plan to use and a Zendesk account for the organization you want to connect. In a managed workspace, an administrator may need to enable the plugin and its required app.

Installing the plugin does not grant additional Zendesk permissions. You must complete the required authorization using your own Zendesk account.

## Connect Zendesk in ChatGPT

1. Switch to the ChatGPT account or workspace where Zendesk is available.
2. Open Plugins and find the Zendesk plugin developed by OpenAI.
3. Select Install or Connect. If asked to connect an app, select **Connect Zendesk.**
4. Enter only your organization's Zendesk subdomain. For example, enter **acme**, without **https://** or **.zendesk.com.**
5. Continue to Zendesk and confirm that the authorization page belongs to your organization's tenant.
6. Sign in with your own Zendesk account, review the requested permissions, and authorize the connection.
7. Return to ChatGPT and check that Zendesk is installed or connected.

Each person who uses the individually authorized connection needs to connect their own Zendesk account.

## Check the connection

Start a new chat and select or mention Zendesk when it is available. Try a read-only request:

*List the five most recently updated Zendesk tickets. Include the ticket ID, subject, status and updated time. Do not modify anything.*

For general plugin selection in supported Codex task views, see [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256). Available capabilities and setup controls can differ by surface.

## Review actions before making changes

Finding or summarizing a ticket is different from sending a reply or changing a record. A requested action must be supported by the app, allowed by your workspace and Zendesk account, and meet any approval requirements. Review the intended target and change before authorizing an action.

## Troubleshooting

### Zendesk is missing or disabled

Check that you are using the intended account or workspace. In a managed workspace, ask its administrator to review the Zendesk plugin and required app settings. Availability depends on the account and current rollout.

### Setup asks for a client ID or secret

Check that you selected the OpenAI-developed Zendesk plugin. Zendesk BYOC entries and listings marked **Custom** or **Template** use a different setup flow. Return to the first-party listing if that is the connection you intend to use.

### Sign-in fails or information is missing

Confirm the tenant subdomain and Zendesk account. Check that the same account can access the requested information in Zendesk and has the permissions required for the action. If the issue continues, contact support with the failed step, exact error and time of the attempt. Do not include passwords, OAuth tokens or client secrets.
