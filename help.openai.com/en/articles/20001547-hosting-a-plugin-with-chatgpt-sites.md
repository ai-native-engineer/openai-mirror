<!-- source: https://help.openai.com/en/articles/20001547-hosting-a-plugin-with-chatgpt-sites -->

# Hosting a plugin with ChatGPT Sites

Learn how to host MCP tools on a Site, use them through a plugin, and share access with your workspace.

You can host an MCP server in a new or existing ChatGPT Site and use the tools through a plugin in ChatGPT. For example, you could create a Site that contains a team handbook, and ask ChatGPT to add an MCP server to the site with tools for searching and accessing the handbook. ChatGPT then builds a plugin which you can use in other workflows, and in Business or Enterprise workspaces, share with other members of your workspace.

Hosting a plugin is available to all plans. Members of Business and Enterprise workspaces will need their administrators to enable permissions before you can publish sites, or share plugins. See the **Share access with your workspace** section below.

## Before you begin

* Use a Site you own, or work with its owner. The owner must publish the Site to create its plugin initially.
* Choose the information and actions the tools should expose. Review the Site's contents and tool behavior before giving other people access.

  + Review if you want other users to only read data from the site, or also expose write actions so that they can update information on the site.
* If you're in a workspace, ask your administrator to go to **Workspace settings > Permissions & roles**, select your role, and turn on these permissions so you can create and use the plugin:
* **Use plugins**: On by default in Enterprise workspaces.
* **Upload plugins**: Off by default in Enterprise workspaces.
* **Create plugins with MCPs**: Off by default in Enterprise workspaces.
* To invite coworkers to the plugin, your workspace role must allow **Share plugins**. Listing it in the workspace directory requires the separate **Publish plugins to workspace** permission.

For general Site creation and publishing, see: [Creating and managing ChatGPT Sites](https://help.openai.com/articles/20001339). For plugin creation, installation, and workspace controls, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

# Add tools to a Site

1. Start a new Site or open the Site you want to extend.
2. Ask ChatGPT or Codex to add an **MCP server** to the Site. Describe the information the tools should read and any changes they should be able to make.
3. Review the tools and test their behavior with sample data before sharing access.
4. Have the Site owner publish the Site to create the associated plugin. If the Site is already published, have the owner publish it again after adding the tools.

For example, if you have built an existing project dashboard, you could ask Codex to “Add tools to this project dashboard so my team can read milestones and update their status from chat.”

# Install and connect the plugin

After Codex completes the MCP server setup, it will create a plugin associated with that site, and display a plugin card for you to review and install.

1. Select **Install** on the new plugin's card.
2. Complete the connection flow for your account.
3. Mention the plugin in a ChatGPT or Codex chat on a supported surface.
4. Ask a question its tools can answer, such as “Summarize the milestones shown on my project dashboard.”
5. Check the response against the Site. If you added a tool that makes changes, try a sample update and open the Site to verify the result.

For plugins you created, you can also go to **Plugins**, select **Personal**, then select **Created by you**.

Installing the plugin does not replace required authorization or workspace access controls. Follow any approval requests shown for an action. For more information, see: [Managing app permissions in ChatGPT](https://help.openai.com/articles/20001495).

## Using the plugin

Mention the plugin in a chat window, and prompt it for answers.

![ChatGPT answering a purchasing-policy question using a Finance Team Handbook plugin.](https://images.ctfassets.net/j22is2dtoxu1/devday-20001547-hosting-plugin-screenshot/8e9e395ec30fd668d82478ff70584329/20001547-hosting-plugin-finance-team-handbook.png?q=80&fm=webp&w=1344)

# Share access with your workspace

If you’re a member of a Business or Enterprise workspace, you can share your plugin with team members. Recipients need access to both the plugin and its Site. Each person installs the plugin and completes their own connection. Pro and personal-account users can’t currently share their Site-hosted plugin directly with other ChatGPT users through invitations or a share link. Sharing the Site itself is separate and doesn’t share its plugin.

1. Go to **Plugins**.
2. Select **Personal**, then **Created by you**.
3. Open your plugin and select **Share**.
4. Add your coworkers and select **Invite**.
5. When prompted, give them viewer access to the Site.
6. Copy the plugin share link and send it to them.

Sharing the plugin does not give recipients permission to edit the plugin or publish it to the workspace directory. It also does not replace permissions or authorization required by any connected apps.

Before sharing, review what information the Site and its tools expose to viewers. For example, if your plugin will expose write specific tools, ensure that you are sharing with members that need that write permission.

# Update your tools

Ask ChatGPT or Codex to change the tools on the existing Site. For example: “Add a tool to export the dashboard's data as a CSV.” Test that Codex updated both the Site and the plugin. You will have to publish the site before the new action can be used. Check that the plugin shows the expected tools and test an affected action.

# Troubleshoot setup and updates

## No plugin appears after publishing

Confirm that the Site includes MCP tools and that the Site owner performed the publication that creates the plugin. If an editor added the tools, ask the owner to publish the Site, and confirm that the plugin shows new tool updates. The Site owner can also ask Codex to confirm that the plugin has the newest tools included.

## The plugin is installed but disconnected

Open the plugin and select **Connect** if shown, then complete the connection flow. If installation or connection was interrupted, return to the plugin card and try the incomplete step again. For general connection help, see: [Connecting and managing app accounts in ChatGPT](https://help.openai.com/articles/20001494).

## A coworker cannot use the tools

Check that they have access to the plugin and viewer access to the Site, have installed the plugin, and have completed their own connection. Also check any connected-app and workspace restrictions. Sharing access alone does not complete installation or authorization.

## New or changed tools are missing

Confirm that the owner published the updated Site and that the owner's connection is active. Then check the plugin's tool list and test the affected action.
