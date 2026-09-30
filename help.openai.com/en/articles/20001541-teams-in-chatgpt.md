<!-- source: https://help.openai.com/en/articles/20001541-teams-in-chatgpt -->

# Teams in ChatGPT

Learn how to create a team and share pages, Spaces, and recurring work with your coworkers.

A team in ChatGPT brings together people in your workspace who work on the same projects. Add your colleagues once, then share a page or an entire Space with the team instead of sharing with each person separately.

A team defines who works together. A Space holds the content and context they share. You can share multiple Spaces with a team, and a Space can include multiple teams. For example, you can:

* Create a launch team for product, engineering, design, operations, and marketing, then share the launch Space and relevant pages.
* Bring sales, solutions engineering, and customer success into an account team to share account plans and handoff materials.
* Use a standing marketing or operations team to share campaign briefs, research, and planning Spaces across projects.

You can also create team tasks for recurring work, such as a weekly project update or customer-change digest. Authorized teammates can review results, update instructions, and maintain the task together.

Teams are available in ChatGPT Business and Enterprise workspaces. Use a team in the workspace where you and your coworkers are members. Your workspace’s settings and permissions determine the capabilities available to you.

# Understand what a team shares

Use your team to bring together shared pages, Spaces, tasks, and other supported resources.

## Spaces and instructions

Share a page or Space with your team so coworkers can collaborate on the same work. A team can have access to multiple Spaces, and a Space can include multiple teams. Members’ ability to view or edit content depends on the sharing permissions and any other access they have.

When you create a team task, provide the instructions and source references it needs. Sharing a Space with the team doesn’t automatically make all of its content part of every task.

## Plugins and connections

A plugin shared with a team can be used by its members as well as its tasks. A plugin provides tools or skills; any required app access depends on the connection used.

Sharing a plugin doesn’t share your personal app connection. Team tasks use connections configured for the team, and the connected provider account determines which information and actions they can access. Team members don’t each need to connect the same provider account for a task to use an enabled workspace connection.

For more information about plugins, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

## Tasks and results

Team members can manage tasks and review available runs when their workspace permissions allow it, including runs completed before they joined. Tasks use their saved instructions and the connections configured for the team. They don’t automatically inherit the creator’s personal saved memories, Custom Instructions, or chat history.

# Teams, workspaces, and groups

Your workspace contains your organization’s members, settings, and administrative controls. A team brings together people within that workspace for shared work. Creating or joining a team doesn’t make you a workspace administrator.

Workspace groups help admins organize members, share resources, and assign custom roles for feature access. Groups can be managed manually or synchronized from an identity provider. A team gives coworkers a shared membership for collaborating on pages, Spaces, and tasks. Team membership, content sharing, and tool permissions are managed separately.

For example, an admin could use a group to give a department access to a feature. Coworkers could then create a team to share project resources and manage a recurring update.

Team membership doesn’t override workspace permissions. For group administration, see: [Managing groups and group managers](https://help.openai.com/articles/9083985).

# Create a team

Create a team in the workspace where its members and shared work belong. If you don’t have permission to create teams, ask your workspace administrator about access.

1. Open the **Teams** list.
2. Select **Create team**.
3. Enter a **Name** and, optionally, a **Description**.
4. Select **Create team** to finish.

You become the team owner. The team has its own service account for running tasks in the cloud, using its configured connections.

# Add members or join a team

Team members can invite coworkers from the same workspace.

1. Open the team and select **Invite**.
2. Search by **Name or email** and select the coworkers to add.
3. Select **Add member** or **Add members**.

To share a team join link, open the options for **Invite** and select **Copy link**. Other members of the same workspace can join by opening the link; joining doesn’t require a separate approval from the team owner. The team’s name and member list can be visible to workspace members who open its link before joining.

Before inviting coworkers or sharing a join link, review the team’s existing tasks, run history, and configured connections. Share pages and Spaces with the team separately, and review each resource’s sharing permissions.

# Workspace RBAC and team permissions

In Enterprise workspaces, role-based access control (RBAC) lets admins control who can create teams and who can create or update team tasks. Feature permissions, team membership, and connection access are managed separately.

Permission to create teams doesn’t add you to a team or give you access to every team. What you can do within a team also depends on your membership and team role.

Workspace owners can assign custom roles to individual workspace members or workspace groups. For setup, see: [Managing feature access with role-based access control](https://help.openai.com/articles/11750701).

# Understand member and owner access

Team members can invite coworkers and remove members who aren’t the owner. Members can also manage the team’s tasks according to the permissions for each action.

Only the team owner can delete the team. Workspace admins manage workspace connections and determine who can use them. The team owner chooses which eligible workspace connections are enabled for the team. Being a team owner doesn’t grant workspace administrator permissions.

To leave a team as a member, open **Members** and select **Leave team**. Leaving removes access granted through that team; any separate access you have to a shared resource still applies. The team owner can’t be removed through the ordinary member-removal flow.

# Use a team task

For example, a project team could set up a weekly task to gather progress, blockers, and next steps from approved sources, then post an update to a shared Slack channel. Teammates can review the output and refine the saved instructions. The task needs access to its sources and permission to post in that channel.

Tasks run in the cloud, so the creator doesn’t need to keep ChatGPT open.

For connection setup, triggers, run history, and troubleshooting, see: [Creating and managing team tasks in ChatGPT](https://help.openai.com/articles/20001540).

# FAQ

## How is a team different from a Space?

A team is a group of people who share access to work and responsibility for tasks. A Space holds the content and context they collaborate on. You can share multiple Spaces with a team, and a Space can include multiple teams.

## Do I need to create a task to use a team?

No. You can use a team to share pages, Spaces, and other supported resources with the same colleagues. Create a team task when you want ChatGPT to repeat a job on a schedule or in response to a supported trigger.

## Is this Microsoft Teams or a separate ChatGPT plan?

No. Teams in ChatGPT let you organize people and shared work within your existing ChatGPT workspace. Microsoft Teams is a separate Microsoft app.

## Does joining a team share my personal chats or app accounts?

Joining a team doesn’t automatically share your personal chats or app connections. Review the resources shared with the team and the connections configured for its tasks. Sharing a plugin and granting access to a connected account are separate actions.

## Can I add someone from another workspace?

Teams bring together members of the same workspace. A team join link doesn’t invite someone into the workspace itself.

## Does team membership sync with workspace groups or Slack or Microsoft Teams channels?

No. Team membership can’t currently be imported from those groups or channels, and later membership changes don’t sync automatically. Add or remove team members directly in ChatGPT.
