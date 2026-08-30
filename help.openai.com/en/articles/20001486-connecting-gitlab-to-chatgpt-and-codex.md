<!-- source: https://help.openai.com/en/articles/20001486-connecting-gitlab-to-chatgpt-and-codex -->

# Connecting GitLab to ChatGPT and Codex

Access your GitLab projects in ChatGPT and Codex to analyze, cite, and take actions on code, merge requests, issues, and CI/CD.

GitLab in ChatGPT and Codex is currently in beta.

The GitLab plugin lets ChatGPT and Codex retrieve up-to-date GitLab data and, when permitted, take actions in projects the connected user can access. It works with projects, groups, repository files, branches, commits, merge requests, issues, pipelines, jobs, and related discussions.

The GitLab plugin includes a GitLab app for GitLab.com and a [GitLab Self-Managed app template](https://help.openai.com/articles/20001487). The plugin is the package that users install, and the app is the connection that accesses GitLab data and actions.

For GitLab Self-Managed or GitLab Dedicated, a workspace admin must create and publish a workspace-specific app from the template before members can connect. Read more about [app templates](https://help.openai.com/articles/20001247), and read about setting up the [GitLab app template](https://help.openai.com/articles/20001487).

The earlier GitLab Issues app with individual sync is no longer available. Follow the setup steps in this article to connect the current GitLab app, which retrieves data through API requests related to your prompt.

## Availability

Availability may vary by plan and workspace configuration. Workspace admins configure the GitLab plugin in ChatGPT and control its availability, who can use it, which actions are enabled, and when approval is required.

# What the GitLab plugin can do

## Read from GitLab

ChatGPT and Codex can:

* Inspect projects and groups.
* Browse repository trees and read files.
* Compare branches, commits, and diffs.
* Review merge requests, approvals, issues, notes, and discussions.
* Check pipelines, jobs, logs, and test reports.

## Take actions in GitLab

Depending on workspace settings and GitLab permissions, ChatGPT and Codex can:

* Create branches and commits.
* Create, update, or delete repository files.
* Create or update merge requests and issues.
* Add notes or discussions.
* Approve merge requests, rebase them, or merge them.
* Apply suggestions.
* Create pipelines, or play and retry jobs and pipelines.

Available actions depend on the workspace’s **Role access**, **Configure actions**, and **Configure approvals** settings, plus the OAuth scopes granted and the connected user’s GitLab permissions.

# Set up GitLab in ChatGPT

## Connect to GitLab.com

1. Open ChatGPT.
2. Open the **Plugin directory**.
3. Search for **GitLab**.
4. Select **Install Plugin**.
5. On **GitLab**, select **Connect**.

If prompted, authorize ChatGPT in GitLab. The GitLab plugin acts as your GitLab user under the OAuth scopes you grant, so ChatGPT and Codex can access only the GitLab projects and groups you can access.

Once connected, use GitLab in ChatGPT or Codex to inspect a project, file, merge request, issue, or pipeline, or to request an allowed action.

For help installing and managing plugins, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

## Connect to GitLab Self-Managed or GitLab Dedicated

A workspace admin must configure and publish the GitLab Self-Managed app template before users connect. For instructions, see: [Setting up the GitLab Self-Managed app template for ChatGPT and Codex](https://help.openai.com/articles/20001487).

## Disconnect GitLab

1. Open ChatGPT.
2. Go to **Settings > Plugins**.
3. Open **GitLab**.
4. Select **Uninstall**.

# Data and privacy

## How ChatGPT and Codex work with GitLab

ChatGPT and Codex use the GitLab plugin to make API requests related to your prompt. For example, they may list a repository tree, fetch a specific file, read a merge request diff or discussion, inspect an issue, or check a pipeline and job log. If an enabled action can change GitLab, ChatGPT or Codex can perform it only when workspace settings, required approvals, and the connected user’s GitLab permissions allow it.

## Model training and GitLab content

By default, content sent by customers using business offerings, including ChatGPT Business, Enterprise, Edu, and the API, is not used to improve our models. For more information about how OpenAI uses business data, see: [Enterprise Privacy](https://openai.com/enterprise-privacy/).

When you use an individual subscription, OpenAI may use your content to train its models if **Improve the model for everyone** is turned on. For more information about how your data is stored and used, see: [Data Controls FAQ](https://help.openai.com/articles/7730893).

GitLab content follows the same workspace data controls whether you use the app in ChatGPT or Codex.

# FAQ

## What can the GitLab plugin read?

It can retrieve GitLab data available to the connected user, including projects and groups; repository trees, files, branches, commits, and diffs; merge requests, issues, notes, and discussions; and CI/CD pipelines, jobs, logs, and test reports. Exact availability depends on enabled actions and GitLab permissions.

## Can ChatGPT and Codex take actions in GitLab?

Yes, when workspace admins enable the relevant actions and any required approval is granted. Depending on configuration and your GitLab permissions, ChatGPT and Codex can create branches and commits; create, update, or delete repository files; create or update merge requests and issues; add notes or discussions; approve or merge merge requests; apply suggestions; and create pipelines or play and retry jobs and pipelines.

## How can admins limit what the plugin can do?

In ChatGPT, workspace admins can use **Role access** to control who can use the app, **Configure actions** to enable or disable actions, and **Configure approvals** to require confirmation for selected actions. GitLab’s own project and group permissions remain in effect.

## Can ChatGPT or Codex read a specific file or merge request diff?

Yes. Give the project and filename or path, branch or ref, merge request URL or internal ID (IID), or the code behavior you are looking for. ChatGPT or Codex can retrieve the relevant file, repository tree, commit, diff, or merge request details when the plugin action is enabled and you have access.

## Why don’t I see a project?

ChatGPT and Codex can access only projects visible to the connected GitLab user. Check that you connected the intended GitLab account, have access to the project or group in GitLab, and selected the correct app for GitLab.com, GitLab Self-Managed, or GitLab Dedicated.

## Does the GitLab plugin support GitLab Self-Managed or GitLab Dedicated?

The standard GitLab app connects to [GitLab.com](https://gitlab.com/) and can be used in ChatGPT and Codex. For GitLab Self-Managed or GitLab Dedicated, a workspace admin must configure and publish the GitLab Self-Managed app template before users connect. For instructions, see: [Setting up the GitLab Self-Managed app template for ChatGPT and Codex](https://help.openai.com/articles/20001487).

## What if my GitLab instance blocks network traffic?

If your GitLab Self-Managed or GitLab Dedicated instance restricts network traffic:

* Ask your network admin to allowlist OpenAI’s ChatGPT integrations egress ranges so the GitLab plugin can reach your GitLab HTTPS host and API.
* If you use Codex project environments, also allowlist the Codex cloud egress ranges.
* For Codex code review, allow outbound HTTPS webhook requests to Codex. If webhook deliveries fail, review GitLab’s [outbound request filtering settings](https://docs.gitlab.com/security/webhooks/).

For the addresses to allowlist, see: [OpenAI IP egress ranges](https://developers.openai.com/api/docs/guides/ip-addresses).
