<!-- source: https://help.openai.com/en/articles/20001540-creating-and-managing-team-tasks-in-chatgpt -->

# Creating and managing team tasks in ChatGPT

Learn how to create, review, and maintain recurring work with your team in ChatGPT.

Team tasks let teammates share responsibility for recurring work in ChatGPT. Tasks run in the cloud on a schedule or supported trigger, using approved tools and workspace connections. Authorized teammates can review results, update instructions, and maintain tasks as their work changes.

Use team tasks for work that needs to happen regularly and that several people need to manage. For example, you could:

* Prepare a daily customer-change digest from approved sources.
* Post a weekly project update to an approved Slack channel, with progress, blockers, next steps, and source links.
* Prepare a meeting agenda and briefing from selected documents and recent updates.
* Create a recurring research brief from selected sources.

Shared ownership lets colleagues maintain a task when its creator is away. The information a task can access and the actions it can take depend on the configured connections and permissions.

Team tasks are available in ChatGPT Business and Enterprise workspaces. Workspace permissions determine which features and actions you can use. Enterprise admins can use role-based controls to decide who can create teams and who can create or update team tasks.

## Before you begin

* Use the workspace and team that should own the task.
* Confirm that the team can use the required apps and model.
* Identify the sources the task should use, the work it should do, and the result you expect.

# Choose a team

Open the **Teams** list in the workspace where you want the task to run, then select a team you belong to. For team creation, membership, and shared-resource setup, see: [Teams in ChatGPT](https://help.openai.com/articles/20001541).

Team tasks run in the cloud under the team’s service account, using the task’s saved instructions and the connections configured for the team. Creating a task for the team does not make it a task in your personal account.

## Understand access

Your ability to create or manage a task depends on your team membership and workspace permissions. A workspace permission doesn’t add you to a team or grant access to every task. Ask your workspace admin if you don’t have access to an action you need.

Team members can view, run, edit, pause, resume, or delete tasks according to the permissions for each action. Deleting the team itself requires the team owner. The actions you can take in a run’s conversation depend on your access to that run. For how workspace permissions and team roles work together, see: [Teams in ChatGPT](https://help.openai.com/articles/20001541).

Workspace admins manage approved connections to company tools and determine who can use them. Check the connected account and its access before using a connection for your team’s tasks.

# Set up workspace connections and instructions

Workspace admins set up workspace connections and control who can use them. The team owner selects which eligible workspace connections are enabled for the team. Tasks use the connected accounts’ permissions to access information and take permitted actions.

Each connection uses a designated account. That account’s permissions determine which data and actions are available. Team members can reuse approved access without each person connecting a personal account.

Before creating a task, ask your workspace admin to confirm that the required connections are available to your team. For example, a task that posts a project update to Slack needs access to its source documents and permission to post in the selected channel.

## Prepare the required connections

1. Identify the apps your task needs and the information or actions it should use.
2. Ask your workspace admin to configure the approved connections and make them available to your team.
3. Ask the team owner to select the workspace connections your task needs. If you’re the owner, select connections you have permission to access.
4. Review the connected accounts and confirm that they can access the required sources and destinations.
5. Add the plugins the task needs, then review the tools and instructions they provide.

If a plugin is disabled or no suitable connection is available, ask your workspace administrator about access.

Adding or sharing a plugin is separate from connecting an account. A plugin provides tools, skills, or instructions; the configured connection provides any required access to the app. Sharing a plugin doesn’t share your personal app connection.

Team members don’t each need to connect the same provider account for a task to use an enabled workspace connection. Workspace and connection permissions still apply.

Complete any required app sign-in before the task runs. An unattended run can’t complete a new app sign-in for you. This doesn’t remove any approval requirements for actions in connected apps.

## Write task instructions

Include the sources, output format, and review criteria in the task’s saved instructions. Add any guidance teammates need to maintain the recurring work. Sharing a Space with the team doesn’t make all of its content part of every run’s instructions. Team tasks don’t automatically inherit the creator’s personal saved memories, Custom Instructions, or chat history.

# Create a team task

1. Open the team that should own the task.
2. In the team’s **Scheduled** section, start a new task.
3. Confirm the owning **Team**, then enter a **Task name**.
4. Enter instructions that identify the sources to use, describe the work to do, and explain the result you expect.
5. Choose a **Trigger** and configure its timing or event conditions.
6. Review **Plugins** and the settings under **Advanced**, including **Model**.
7. Select **Create**.

Choose a model the team can use. A model available in your own account may be unavailable to the team’s service account.

## Choose timing or an event

Use **Schedule** for recurring work or **Date and time** for a one-time run. Each task keeps its own time zone. Review the saved timing and time zone before creating or updating the task.

Tasks can respond to supported activity in connected apps, such as a new Gmail email or Slack message. Choose a trigger available to your team and confirm that the required connection and permissions are in place.

For a Slack trigger, choose the channel to monitor. Describe the activity that should start the task and review its conditions before saving.

## Example: draft a weekly project update

You can use a team task to prepare a weekly draft from project documents:

1. Choose the team that owns the work and confirm that its connection can access the project documents.
2. In the task instructions, link to the documents and describe the output. For example: “Using these project documents, draft a weekly update with progress, blockers, and next steps. Include a source link for each update.”
3. Select **Schedule**, choose the timing, and create the task.
4. Select **Run now**, then open **Previous runs** to review the draft and check its source references.
5. If needed, select **Edit** to refine the instructions or settings, then run it again and review the result.

## Start from Slack or Microsoft Teams

Where your organization has enabled @ChatGPT, you can ask it to set up recurring work. Specify the team that should own the task, the work to do, and when it should run. Review the selected team and complete any requested connection setup.

For example: “Every weekday morning, prepare a customer-change digest from these approved sources for the account team.”

The Slack channel or Microsoft Teams conversation is an entry point. Check which team owns the task and which connections it uses; your personal chat-platform account does not automatically supply the team’s app access.

# Run a task and review results

1. Open the task’s details.
2. Select **Run now** to start a run using its saved instructions.
3. Open **Previous runs** and select a run to review its conversation and result.

You and other teammates with permission to reply can ask follow-up questions or refine the result in that run’s conversation. To change the instructions or settings used for future runs, select **Edit** on the task.

Access to a run doesn’t automatically give you access to its linked source documents or files created in connected apps. Those resources still use the connected app’s sharing permissions.

Review the result to check whether the requested work succeeded. If the task was meant to update a file or send a message, check that destination too. A **Completed** time-based schedule means it has no future runs scheduled; it does not confirm that an individual run completed the work successfully.

# Manage future runs

From the task’s management controls, use the actions available to your account:

* **Edit** to change the task’s saved instructions or settings.
* **Pause** to suspend future scheduled and event-triggered runs.
* **Resume** to enable future runs again.
* **Delete** to remove the task.

Check any run already in progress separately. Don’t rely on pausing or deleting a task to interrupt an active run.

# Understand usage and spending

Workspace administrators manage the applicable spending controls for team tasks. Personal scheduled-task limits don’t establish the spending limits for shared work.

If a task reports a usage or spending-limit error, record the message and ask your workspace administrator to review the applicable workspace settings.

Check the task’s run history before trying again, especially if the task sends messages or changes files.

# Troubleshoot a task

## An expected result is missing

1. Confirm that you are in the correct workspace and team, then open the task’s details.
2. Open **Previous runs** and look for the expected run. If it appears, open it and check the result and any error message.
3. Review the saved schedule or event conditions to check when the task should run.
4. If the run reports an app-access error, check the connection and the connected account’s permissions.
5. Before rerunning a task that sends messages or changes files, check what the earlier run already did.

If the issue continues, share the team and task names, the expected run time and time zone, the exact error message, and the steps you tried with your workspace administrator or Support.

## The selected model is unavailable

If the selected model becomes unavailable to the team, the task pauses.

1. Open the task’s editing controls.
2. In **Advanced**, choose an available **Model** and select **Save**.
3. Select **Resume** and check the next run.

## An app cannot access information or take an action

1. Check the connection configured for the team and identify the provider account behind it.
2. Confirm that the provider account can access the required information or perform the action.
3. Review the task’s plugin selection and saved instructions.

A request that succeeds in your personal chat may use a different connection. Sharing the plugin again does not, by itself, share your personal app connection or grant permissions in the connected app.

## An action or task is missing

Confirm that you are in the correct workspace and team, then ask your workspace administrator to check the relevant permissions. Permission to create a team does not give you access to every team or run.

# FAQ

## What is the difference between a team and a group?

A workspace group helps admins organize members, share resources, and manage feature access through assigned roles. Groups can be managed manually or synchronized from your organization’s identity provider.

A team brings people together in ChatGPT to share pages and Spaces and maintain recurring tasks. Workspace members can create teams when their permissions allow it. For example, an admin might use a group to give a department access to a feature, while coworkers create a team to share project resources and recurring work.

Team membership does not override workspace permissions. Learn more about [managing groups in ChatGPT Enterprise and Edu](https://help.openai.com/articles/9083985).

## Will my task run if ChatGPT is closed?

Yes. Team tasks run in the cloud, so you don’t need to keep ChatGPT open or your computer awake for a scheduled run. The task still needs the required connections and permissions.

## What instructions should I include in a task?

Include the sources to use, the work to do, the expected output, and any review criteria. Keep essential guidance in the saved task so teammates can review and maintain it. Don’t assume that ChatGPT will use every earlier run as context.

## How do I change what a task does in future runs?

Edit the task’s saved instructions or settings, then review the next run. Keep shared guidance in those saved instructions so other teammates can understand and maintain the task.

## Are failed runs retried automatically?

Some temporary execution errors are retried automatically. A failed app action within a run doesn’t necessarily trigger an automatic retry. Review the result and any errors in **Previous runs** before trying again.
