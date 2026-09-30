<!-- source: https://help.openai.com/en/articles/20001538-setting-up-and-managing-chatgpt-in-slack-and-microsoft-teams -->

# Setting up and managing @ChatGPT in Slack and Microsoft Teams

Set up your organization’s @ChatGPT assistant, configure its company connections, and verify access in Slack and Microsoft Teams.

Set up your organization’s @ChatGPT assistant, configure its company connections, and verify access in Slack and Microsoft Teams.

This guide is for ChatGPT workspace administrators and Slack or Microsoft Teams administrators setting up their organization’s @ChatGPT assistant. The steps use the OpenAI admin console.

Set up the messaging connection first, test a basic conversation, and then add approved company connections. Validate the result with an intended user before making the assistant available more broadly.

For @ChatGPT’s account, context, personal authorization, and information-sharing behavior, see: [Using @ChatGPT in Slack and Microsoft Teams](https://help.openai.com/articles/20001537).

For other ways to use ChatGPT with Slack or Microsoft Teams, see: [ChatGPT with Slack and Microsoft Teams](https://help.openai.com/articles/20001536).

This feature is available to Business, Edu, and Enterprise accounts.

## Usage and billing

Usage for requests handled through @ChatGPT’s service account is attributed to that account. When a member authorizes work that uses their personal connections, that work runs under their account and usage is attributed to them.

## How access works

@ChatGPT has its own service account. It uses the company connections your organization configures for the assistant. The connected account’s permissions determine which information it can read and which actions it can take. Choose access appropriate for the people who can use @ChatGPT.

The assistant does not automatically inherit each requester’s access to apps or private files. Some requests may need a person’s separate authorization. Replies in shared conversations are visible to their participants.

## Before you begin

Identify the ChatGPT workspace and the Slack workspace or Microsoft Teams tenant you want to connect.

Agree on the responsibilities for setup:

* A ChatGPT workspace administrator or owner connects the messaging platform and configures the assistant.
* A Slack or Teams administrator approves the app and manages its availability in that platform.
* Each company tool needs a connection owner who can approve its access and resolve connection problems.

A surface is the configuration that connects @ChatGPT to a messaging workspace or tenant. Use a separate surface for each Slack workspace in an Enterprise Grid organization and for each Microsoft Teams tenant.

# Set up Slack

## Connect the workspace

1. Open the OpenAI admin console and select the intended ChatGPT workspace.
2. Open **Agents,** click **Add** in the top right, and follow the Slack setup prompts.
3. Connect the intended Slack workspace and review the requested permissions.
4. Have the Slack workspace owner or authorized app manager complete app approval if required. Note that if the ChatGPT app was already installed, you may see a warning banner at this stage about missing scopes. Follow the instructions [here](https://help.openai.com/articles/20001536#existing-users-of-the-chatgpt-app-in-slack) to resolve this.
5. Return to the admin console for the next step.

## Create and test the surface

1. In **New surface**, choose the connected Slack workspace and enter a recognizable name.
2. Select **Create surface** to save the configuration.
3. To limit channel access, open the surface, select **Selected channels only**, and add your test channels. Select **Save channel restrictions**.
4. Add @ChatGPT to an approved test channel.
5. Mention @ChatGPT in a fresh thread and ask it to summarize a short set of notes included in the message.
6. Confirm that it responds, and test a direct message separately.

Channel restrictions apply to Slack channels. They do not restrict direct messages. Account for both paths when deciding which company connections to make available.

# Set up Microsoft Teams

Connect your Microsoft Teams tenant in the OpenAI admin console, then install the ChatGPT app for the intended users or groups.

## Connect the tenant

1. Open the OpenAI admin console and select the intended ChatGPT workspace.
2. Open **Agents** and follow the Microsoft Teams connection prompts.
3. Sign in with the authorized Microsoft account, review the requested permissions, and complete organizational consent when prompted.

## Install the app and confirm readiness

1. Select [**Open Teams admin center**](https://admin.teams.microsoft.com/policies/manage-apps/a37eb519-d163-49a2-8df3-7b27851f3e5f) to open the ChatGPT app page.
2. Open **Users and groups** and select **Install app**.
3. Choose the intended users or groups and complete installation.
4. Confirm that Teams policies allow those users to use the app.
5. Return to the OpenAI admin console. When the connection shows **Ready**, select **Done**.

If setup is still pending after installation, open a one-on-one chat with ChatGPT in Teams and send a message. Return to the admin console and check the status again.

Selecting **Done** while the connection is still pending only closes the setup dialog. Return to check the status, and continue when it shows **Ready**.

## Create and test the surface

1. In **New surface**, confirm that the connected tenant matches the tenant where you installed the app, and enter a recognizable name.
2. Select **Create surface**.
3. Mention @ChatGPT in an approved Teams channel and confirm a response to a request that includes the information it needs.

If your approved setup includes personal chat or file support, test those paths separately. A successful channel response does not confirm that every Teams feature is configured.

# Connect @ChatGPT to your company tools

After setting up @ChatGPT in Slack or Microsoft Teams, connect the company tools it should use to help your team. These connections let the assistant find company information and perform supported actions when responding to requests.

Use workspace connections to give @ChatGPT approved access to company tools. Review the connected account’s permissions for the people who can use the assistant.

## Add a tool and review its permissions

Add each company tool as a plugin and connect it using the account approved for @ChatGPT.

1. Open the surface’s **Plugins** section.
2. Select **Add plugin** and choose the tool required for your workflow.
3. Follow its supported connection prompts using the approved account.
4. Review the resources and actions that account can access in the connected service.
5. Confirm the connection owner.

Start with read access when that is sufficient for the workflow. If the assistant needs to create or change content, approve the required actions and identify the intended destination, such as a shared folder or project.

Connecting a tool does not grant access to every company resource. The connected account’s permissions still determine what it can access.

A request for someone’s personal authorization is separate from a shared connection. Replies posted to shared conversations are visible to their participants, so review the intended audience before approving access.

## Set instructions for the assistant

@ChatGPT is designed to not require any additional instructions from admins. However, you can use **Instructions** to describe how it should use connected tools, how it should understand company-specific terminology, and any preferred destinations for its work. Select **Save instructions** when finished.

For example, you could specify where project updates should be saved or which company source the assistant should consult for a particular task.

Keep instructions separate from access controls. Grant resource permissions in the connected service and configure connection access through the supported administration controls.

# Enable Codex in Slack

These steps apply where Codex Cloud is available through @ChatGPT in Slack.

1. Enable Codex Cloud for your ChatGPT workspace.
2. If your workspace uses Codex Cloud role-based access control, grant access to the @ChatGPT surface’s service account and the members who will request coding tasks.
3. Publish a cloud environment and share it with your workspace.
4. Confirm that each requesting member can use the environment and access any repositories that require authentication.
5. Ask an intended member to start a coding task through @ChatGPT in Slack, and confirm that the task starts.

For environment setup instructions, see: [Codex Cloud developer guide](https://developers.openai.com/codex/environments/cloud-environments).

For this workflow, @ChatGPT uses its service account to find environments, and the coding task runs as the requesting member. The service account doesn’t need its own GitHub connection to find environments.

# Set a spend cap

@ChatGPT supports a per-surface default spend limit and the ability to override the default for each surface.

To configure the default, if your account supports usage limits:

1. In the admin console, go to **Usage limits** and select the **Shared agents** tab.
2. Click the pencil icon in the @ChatGPT row, under **Default spend limit**
3. Enter the limit and approve the change.

This sets a default usage cap for each surface’s service account. Workspace spending limits still apply.

To configure an override:

1. In the admin console, Go to **Agents** and select the surface you want to override the limit for.
2. Navigate to the **Spend controls** tab
3. Click **Edit spend cap**, specify the override limit and duration, and approve.

Removing the override restores the inherited limit. Work attributed to a member’s account is subject to that member’s limits.

# Validate the setup

Test with an intended user. Repeat the checks for each platform and conversation type you plan to support.

1. Conversation: Ask a question in the approved conversation and confirm a response.
2. Source access: Ask for a known approved resource by name and by direct link.
3. Access limits: Use a harmless test resource outside the intended scope to check that the assistant cannot access it.
4. Actions: If write actions are enabled, test an approved, reversible action in the designated destination and inspect the result.
5. Output access: Have another intended participant open any generated file.

A visible response or file link does not establish that the recipient can open the file. Check the destination’s sharing permissions separately.

Tell members where @ChatGPT is available, what company tools it can use, and who handles access problems. Share the member guide with them: [Using @ChatGPT in Slack and Microsoft Teams](https://help.openai.com/articles/20001537).

# Maintain connections and access

Have the connection owner maintain the connected account and credentials using your organization’s account-management process.

Review the setup when app permissions, source permissions, connection owners, or the intended audience change. After reconnecting or changing access, repeat the relevant conversation, source, action, and output checks.

## Turn @ChatGPT off or on

Turn off a surface to pause responses while preserving its configuration.

1. Go to **Agents** and select the surface.
2. In **Overview**, turn off **@ChatGPT** and confirm the change.

To enable the surface again, return to **Overview** and turn on **@ChatGPT**.

## Delete a surface

Deleting a surface permanently removes its configuration and managed service account. It leaves the messaging installation in place.

1. Go to **Agents** and select the surface.
2. In **Overview**, select **Delete**. If that control isn’t shown, open **Manage agent** and select **Delete agent**.
3. Review the **Delete surface** confirmation, then select **Delete** to confirm.

## Remove a messaging connection

If **Remove connection** is available, delete any surfaces that use the messaging connection before removing it. Disabled surfaces still block removal.

Removing the connection deletes its saved messaging authorization and workspace registration. You’ll need to authorize it again before using it for a new surface. This is separate from removing a workspace connection to a company tool.

# Troubleshoot the setup

## Check installation and assignment

If members cannot find or use @ChatGPT, confirm the workspace or tenant, app approval, user assignment, and surface configuration. In Slack, check that the assistant has been added to the channel. In Teams, check that the app is installed for the intended users and that the connection shows **Ready**.

## Enable a connection for @ChatGPT

If a connection shows **Not enabled for @ChatGPT**, enable it before creating the surface.

Turning on **@ChatGPT agents** also enables the connection for team automations and service accounts and sets role access to **All roles**. Review the intended audience before making this change.

1. Go to **Workspace connections** and select the connection.
2. Under **Availability**, turn on **@ChatGPT agents**. The change saves automatically.
3. Return to **Agents** and select the connection again.

Turning off **@ChatGPT agents** later doesn’t automatically turn off access for team automations or service accounts or remove the role access granted by this setting.

## Check a failed response

Retry a simple request in a fresh thread using information supplied in the message. This helps separate basic conversation access from a problem with a company connection. In Slack, have an administrator check the ChatGPT app details page for missing permissions and complete any required approval.

## Check a failed company connection

Have the connection owner confirm that the account is active, its credentials remain valid, and its source permissions still cover the requested resource. Check personal authorization separately when the request needs a member’s connection.

If a direct link works but searching by name fails, include both results when reporting the issue.

## Check access for Codex in Slack

If @ChatGPT can’t find an environment, check its workspace sharing and the service account’s Codex Cloud access. If it finds the environment but can’t start the coding task, check the requesting member’s Codex Cloud, environment, and repository access.

## Restore access to a generated file

Check the file’s owner, location, and sharing settings in the connected service. The file may belong to the account used by @ChatGPT. Have the owner grant the intended audience access through your organization’s approved process, then ask an affected participant to open it again.

## Collect details for support

Include the ChatGPT workspace, Slack workspace or Teams tenant, affected user, message link, approximate time, expected result, actual result, error text, and recent configuration changes.

Include relevant audit evidence when available. Do not send passwords, access tokens, or other credentials.
