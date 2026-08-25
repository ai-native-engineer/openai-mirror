<!-- source: https://help.openai.com/en/articles/20001199-chatgpt-agents-app-in-slack -->

# ChatGPT Agents App in Slack

Install and use ChatGPT workspace agents in Slack, including channel access, agent setup, and enterprise administration.

**Note**: Admins need to [set up Slack](/en/articles/20001236-deploy-chatgpt-workspace-agents-to-slack-admin-setup) before workspace members can create workspace agents.

The ChatGPT Agents app brings the power of ChatGPT workspace agents to Slack. This allows you to build a ChatGPT workspace agent and interact with it from Slack by deploying it to Slack channels. It can respond to your teams’ questions, perform productive tasks using connections to other systems, and output files to you in Slack.

Slack Enterprise Grid organizations can use ChatGPT Agents across multiple workspaces. After connecting Slack through an approved workspace, users can invoke any agent added to one of their Slack workspaces.

# What you can do

* **Access your agents in private channels**: You can interact with your agents in private settings — connect them to your private systems and use them to send emails, update documents, and more without ever leaving Slack.
* **Configure your agent to respond in public channels**: You can configure your agents to automatically respond to messages in public channels. For example, you could configure a company knowledge agent to automatically respond in a help channel.
* **Schedule your agent to send messages in Slack**: You can set up your agent to operate on a schedule, and send its results to a Slack channel.

Responses from ChatGPT Agents may be inaccurate.

# ChatGPT Agents app installation

**Note, installation instructions are different for Slack organizations that use Slack Enterprise Grid. See instructions below for these organizations.**

## Pre-requisites

* Your [Slack workspace must allow](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace) installation of the ChatGPT Agents app for Slack
* You must be using a [paid Slack plan](https://app.slack.com/plans).
* Your Slack workspace permissions must allow all members to create [user groups](https://slack.com/help/articles/212906697-Create-and-edit-user-groups).
* You must have a Business, Edu, or Enterprise ChatGPT account.
* Enterprise admins must additionally enable the **Workspace agents in Slack** app from [Admin app settings](https://chatgpt.com/admin/ca), including any RBAC configuration required to control user group access. Note that the Slack app in ChatGPT is enabled by default for Business accounts.

## Installation

Start installing the ChatGPT Agents app in Slack by clicking on [this link](https://www.chatgpt.com/chatgpt-agents-slack-app-install)*.* You will be required to sign into your ChatGPT account, if you haven’t already signed in. Then, you will be presented with the Add ChatGPT to Slack modal, shown below. Review the information presented and click Continue to Slack to proceed.

![Agents Slack 1](https://images.ctfassets.net/j22is2dtoxu1/1jdTsGcDbh3SDLEYIWjPmq/7af9ef7768ef0bcdc3d44489f992b61b/Screenshot_2026-04-21_at_8.38.24%C3%A2__PM.png?q=80&fm=webp&w=1344)

You will then be directed to the Slack authentication flow, where you can review and grant the app the required permissions. Depending on your workspace settings, this may require an approval [from a Slack admin](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace).

Once the app has been successfully installed, you can navigate to the “Agents” tab in the ChatGPT sidebar to create agents. Note that this feature is gated by admin-controlled permissions, so if you don’t see this tab, you may need to ask your workspace admin to enable Agents.

![Slack Screenshots 01](https://images.ctfassets.net/j22is2dtoxu1/2lRz0nRg6EggXQivue7IcY/e9dc8bc71e50ff38b5675c2a0ea9e018/Slack_Screenshots_01.png?q=80&fm=webp&w=1344)

Once you’ve built an agent, you can enable your agent to interact in Slack by clicking the “Add channel” button. If you’re collaborating on an agent someone else owns, you can publish changes that keep the existing Slack channel setup unchanged, but the agent owner must add, remove, or change Slack channels.

![Slack Screenshots 02](https://images.ctfassets.net/j22is2dtoxu1/7fkbxXlzCycKiHGfPhrAGd/755dc910a9cf112d4b8a72525855e3cc/Slack_Screenshots_02.png?q=80&fm=webp&w=1344)

You’ll be asked to select a handle that will be used to let you chat with your agent from Slack. This handle will need to be unique from other user groups in your Slack workspace.

![Slack Screenshots 03](https://images.ctfassets.net/j22is2dtoxu1/3psiceJzW27PeWMgbP3ky1/f030d397a4090dbdc76e56f89351d147/Slack_Screenshots_03.png?q=80&fm=webp&w=1344)

Next, provide the channel where you want to interact with your agent. If you wish to deploy your agent to a private Slack channel, you need to add the ChatGPT Agents Slack app to the Slack channel by navigating to Slack channel > Integrations > Add apps

![Screenshot 2026-04-21 at 8.43.41 PM](https://images.ctfassets.net/j22is2dtoxu1/5ugvIRYCkgf6kzNZL765go/05d0a36288b8733894b650aa806549f0/Screenshot_2026-04-21_at_8.43.41%C3%A2__PM.png?q=80&fm=webp&w=1344)

After this is complete, you can click into the channel button to configure schedules, choose how your agent responds, and give your agent additional instructions for the Slack channel. Under “When should this agent respond?”, choose “Respond to all relevant messages” or “Only reply when @mentioned.” If you select “Only reply when @mentioned” and see “Agent will follow up in the thread when there are relevant replies,” the agent can continue in that Slack thread when relevant replies are added after it has been mentioned.

![Slack Screenshots 05](https://images.ctfassets.net/j22is2dtoxu1/0jbTAMv7VNCqnHgqcED4t/ed5dacd7d9db8e7a12d457027032f1b0/Slack_Screenshots_05.png?q=80&fm=webp&w=1344)

# Installation for Slack Enterprise Grid organizations

For Slack Enterprise Grid organizations, ChatGPT workspace agents on Slack require both org-level Slack approval and a workspace-level Slack connection. After setup, users can invoke any agent added to one of their Slack workspaces.

Setting this up requires three stages:

* A Slack admin must approve and configure the ChatGPT Agents Slack app at the Enterprise Grid organization level.
* A Slack admin must add the app to one or more Slack workspaces.
* Team members must connect Slack from inside ChatGPT through one approved workspace.

If you skip the workspace step, Slack handle creation for your agents may fail. If you do not provide org-level approval, workspace agents may function with reduced capabilities.

## Pre-requisites

* You must have a Slack admin account for your organization
* You must be using a [paid Slack plan](https://app.slack.com/plans/T08GN60BBV2) with Enterprise Grid.
* You must have a Business, Edu, or Enterprise ChatGPT account.
* Enterprise admins must additionally enable the Slack app from [Admin app settings](https://chatgpt.com/admin/ca), including any required RBAC. Note that the Slack app in ChatGPT is enabled by default for Business accounts.

## Slack admin installation

### Step 1: Approve the ChatGPT Agents Slack app at the org level through OAuth

Use a Slack Org Admin, Org Owner, or Integrations Admin account to complete the ChatGPT Agents Slack app installation from the Enterprise Grid org context, not from an individual workspace selector. This can be initiated in ChatGPT by navigating to the ChatGPT Agent builder, creating a dummy agent, and creating a Slack channel. Docs for [this are here](https://help.openai.com/articles/20001199#slack-admin-installation).

This gives Slack the org-level approval required for the app to work on channels and workspaces across the org.

### Step 2: Add the app to the workspaces where people will actually use it

After the org-level install is complete, go back to Slack Admin and add the app to every workspace where ChatGPT workspace agents should be available.

### Step 3: Ensure members can manage user groups

As a Slack admin, navigate to: <https://app.slack.com/admin/permissions/account-types>

Confirm the permission for creating and editing user groups is available to members in the workspaces where ChatGPT workspace agents will run.

This is required because ChatGPT Agents creates and manages Slack user groups for agent handles. If this permission is blocked, builders will hit an error stating “Ask a Slack admin to allow members to manage user groups. Open Slack settings”

### Step 4: Verify the app is available in the intended workspace

Before telling team members to connect, sanity-check that:

* the ChatGPT Agents Slack app is approved for the Enterprise Grid org
* the app has been added to the intended workspace
* user-group permissions are enabled in that workspace

If you want a short admin checklist, it is:

* Org-level OAuth approval first
* Add to one or more workspaces second
* Enable member management of user groups third

## Slack team member installation

### Step 1: Open ChatGPT from your workspace context

Make sure you are using ChatGPT inside the workspace where you want to build and run agents.

Note: ChatGPT workspace agents aren’t currently available on personal accounts.

### Step 2: Connect Slack on an allowed workspace

When ChatGPT prompts you to connect to Slack, choose the specific Slack workspace that you want your agents on.

Ensure you connect a Slack workspace and not a Slack organization.

### Step 3: Finish agent Slack setup

Once Slack is connected at the workspace level, you can:

* Give your agent a Slack handle in the ChatGPT Agent builder
* Add the agent to multiple Slack channels
* Interact with and schedule your agents on Slack channels.

If you see a permissions error while creating the Slack handle, that usually means the Slack admin still needs to allow members to manage user groups in Slack.

### Step 4: If you experience an error, reconnect the correct workspace

If Slack was previously connected to a different workspace or to an organization, reconnect and select the admin-approved Slack workspace in the workspace dropdown when completing the Slack authorization flow.

A connection that points at the org instead of a specific workspace can look valid at first, but still fail when ChatGPT tries to create the Slack handle or sync the Slack user group.

## Troubleshooting

If the builder sees “Reconnect Slack and choose the Slack workspace where you want to create this handle,” the Slack connection is likely tied to the org instead of a specific workspace.

If the builder sees “Your workspace is not set up to use Slack with ChatGPT Agents. Ask your admin to set it up,” the admin needs to update Slack’s Account types permissions.

If Slack works when connecting but not for handle creation, check both of these:

* the app was added to the desired workspace
* the workspace allows members to create and edit user groups

## Recommended rollout note

For Enterprise Grid organizations, admins approve the app once at the organization level, then add it to the workspaces where agents should be available.

Team members connect Slack from ChatGPT through one approved workspace. After connecting, users can invoke any agent added to one of their Slack workspaces.

Slack docs:

* [Manage apps in an Enterprise organization](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization)
* [Manage user groups from the Admin dashboard](https://slack.com/intl/en-gb/help/articles/115004952926-Manage-user-groups-from-the-Admin-dashboard)
* [Enterprise organizations](https://docs.slack.dev/enterprise/)
* [Migrating existing apps to an Enterprise org](https://docs.slack.dev/enterprise/migrating-to-organization-wide-deployment/)

# Privacy and security

ChatGPT respects Slack’s existing permissions — only the messages and files you already have access to in Slack are searchable.

Note that Enterprise admins may use the compliance API to access user conversations synced to your ChatGPT account from the ChatGPT app for Slack. See the [Compliance API](/en/articles/12462158-chatgpt-app-in-slack#h_a6011401b0) section below.

See more details on our privacy policy [here](https://openai.com/policies/row-privacy-policy/).
