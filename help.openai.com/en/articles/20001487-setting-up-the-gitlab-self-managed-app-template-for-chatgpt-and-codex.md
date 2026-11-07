<!-- source: https://help.openai.com/en/articles/20001487-setting-up-the-gitlab-self-managed-app-template-for-chatgpt-and-codex -->

# Setting up the GitLab Self-Managed app template for ChatGPT and Codex

Learn how workspace admins can configure the GitLab Self-Managed app template for a GitLab Self-Managed or GitLab Dedicated instance by using their organization’s GitLab OAuth application.

Updated: 18 days ago

GitLab in ChatGPT and Codex is currently in beta.

Use the [GitLab Self-Managed app template](https://help.openai.com/articles/20001247) to create a workspace-specific draft app for a GitLab Self-Managed or GitLab Dedicated instance. Provide the GitLab hostname and OAuth application credentials, review the draft app, and then publish it for eligible workspace members. After publication, the app’s enabled actions are available in ChatGPT conversations and Codex sessions.

For an overview of supported GitLab behavior, availability, permissions, data use, and network requirements, see: [Connecting GitLab to ChatGPT and Codex](https://help.openai.com/articles/20001486).

## What you are setting up

You are creating a workspace-specific app from the GitLab Self-Managed app template. The app uses:

* A GitLab OAuth application registered on your GitLab Self-Managed or GitLab Dedicated host.
* The GitLab OAuth **Application ID** and **Secret** for user authorization.
* The required OAuth scopes: api, write\_repository, and openid.
* Your GitLab hostname, such as gitlab.example.com, to derive the web, API, authorization, and token endpoints.

# Before you begin

You need:

* ChatGPT workspace admin or owner access.
* GitLab permission to create the OAuth application: group Owner access for a group-owned app, or instance administrator access for an instance-wide app.
* The GitLab hostname only, without https://, a port, or a path. Use a GitLab Self-Managed or GitLab Dedicated host, not gitlab.com.
* A decision about which GitLab actions ChatGPT and Codex should support, such as repository search, merge request workflows, issue workflows, file edits, or broader Codex workflows.

Keep ChatGPT and GitLab open in separate tabs. Copy the exact **Redirect URI** shown in ChatGPT; do not create or modify it.

To open the **Apps** page from [Admin console](https://admin.openai.com), select the intended ChatGPT workspace, open **Plugins**, and select **Manage Legacy Apps**.

## Values to prepare

* GitLab hostname: for example, gitlab.example.com.
* **Redirect URI**: copy this from the ChatGPT template setup flow.
* GitLab OAuth **Application ID**.
* GitLab OAuth **Secret**.
* OAuth scopes: copy these from the ChatGPT template setup flow.

# Start the template setup in ChatGPT

1. In ChatGPT, switch to the workspace where the app should be available.
2. Go to **Workspace settings > Apps**.
3. In **Directory**, find **GitLab**, open its **GitLab Self-Managed app template**, and select **Enable**.
4. Enter a clear app name and description.
5. Enter the GitLab hostname, such as gitlab.example.com.
6. Copy the **Redirect URI** shown in ChatGPT, and keep this tab open.

Example: https://chatgpt.com/connector/oauth/<redirect\_id>. Do not remove the redirect ID, add a trailing slash, or replace the URI with a generic ChatGPT URL.

# Create the GitLab OAuth application in GitLab

## Choose where to create the application

1. Open your GitLab host, such as https://gitlab.example.com.
2. Choose whether to create an instance-wide application or a group-owned application. This choice determines who manages the application; project access still follows the authorizing user’s GitLab permissions and the granted OAuth scopes.
3. For an instance-wide application, go to **Admin > Applications**. For a group-owned application, go to the group’s **Settings > Applications**.

## Add the application details

1. Select **New application** or **Add new application**.
2. Enter a clear app name, such as GitLab Self-Managed or GitLab Dedicated.
3. In **Redirect URI**, paste the exact URI copied from ChatGPT.
4. Keep **Confidential** enabled for this server-side OAuth application.

## Configure access and save

1. For an instance-wide application, GitLab recommends selecting **Trusted**. This skips the user authorization prompt.
2. Select the api, write\_repository, and openid scopes.
3. Review who can manage the application, and confirm that authorizing GitLab users have the appropriate group and project permissions.
4. Save the application.

## OAuth scope requirements

The template requests the following OAuth scopes for enabled GitLab actions in ChatGPT and Codex:

* api: required for GitLab API operations exposed by the app, including merge request, issue, and CI/CD actions.
* write\_repository: required for repository write operations over Git.
* openid: required for OpenID Connect identity and membership information.

## Copy the GitLab OAuth credentials

In the saved GitLab application, copy the **Application ID** and **Secret**. Treat the **Secret** as a credential. If it is exposed, renew it in GitLab and create a new workspace app.

# Finish setup in ChatGPT

1. Return to the ChatGPT template setup tab.
2. Paste the GitLab **Application ID** into **OAuth client ID**.
3. Paste the GitLab **Secret** into **OAuth client secret**.
4. Confirm that the GitLab hostname contains only the hostname, such as gitlab.example.com.
5. Select **Create draft**.
6. Open the draft app details and review **Configure actions**. In Enterprise and Edu, review **Role access** to confirm that the intended roles can use the app. In Business, manage app availability across the workspace.

# Publish and manage the app for ChatGPT and Codex

Creating the draft app does not automatically make it available to members. After reviewing the draft:

1. Select **Publish** for the draft app.
2. Go to [**Admin Console**](https://admin.openai.com), select the intended ChatGPT workspace, and open **Plugins**. Confirm that **GitLab** is available for the workspace.
3. In Enterprise and Edu, review **Role access** to confirm that the intended roles can use GitLab. In Business, manage app availability across the workspace.
4. In **Configure actions**, review the available read and write actions.
5. In **Configure approvals**, choose when users must approve an action before ChatGPT or Codex uses the app.
6. Ask a test user with access to open **GitLab** from the [**Plugin directory**](https://help.openai.com/articles/20001256) or **Settings > Plugins**. Confirm that the user can install the plugin and connect to the app created from the **GitLab** Self-Managed template.

These app approval settings apply to ChatGPT conversations and Codex threads.

# Set up GitLab activity for Codex code review

After the app is published, configure GitLab activity in Codex if you plan to use Codex code review. This activity setup configures the required webhook events.

1. Open [Codex connector settings](https://chatgpt.com/codex/cloud/settings/connectors).
2. Configure a workspace service account. Let Codex create the account, or provide a personal access token for an existing service account.
3. Enable **GitLab activity** for the project or one of its parent groups.
4. If Codex needs to run coding tasks or use project-specific setup, create a [project environment](https://chatgpt.com/codex/cloud/settings/environments?provider=gitlab).

The GitLab app uses user OAuth for reads and enabled actions in ChatGPT and Codex. For Codex review writes on GitLab Self-Managed or GitLab Dedicated, the workspace-managed service-account token determines the identity and projects where Codex can comment or react.

Read more: [Review GitLab merge requests with Codex](https://learn.chatgpt.com/docs/third-party/gitlab).

# Connect and test the GitLab app

1. As a user with access, open **GitLab** from the [**Plugin directory**](https://help.openai.com/articles/20001256) or **Settings > Plugins**. Select **Install Plugin**, and then select **Connect**.
2. If your workspace has more than one GitLab app, choose the app for this GitLab Self-Managed or GitLab Dedicated host.
3. Authorize the GitLab OAuth application when prompted.
4. Run a small read action first in ChatGPT or Codex, such as listing accessible projects or fetching a known merge request.
5. If write actions are enabled, test them in a low-risk project and in each product where you plan to use them before broader rollout.

# Hostname and OAuth behavior

The app uses the hostname to derive GitLab endpoints. Enter only the host, such as gitlab.example.com. Do not include https://, an API or repository path, a port, or gitlab.com. This template is for GitLab Self-Managed or GitLab Dedicated. For GitLab.com (SaaS), use the GitLab app.

# Troubleshooting GitLab Self-Managed app setup

* **Redirect URI mismatch:** Confirm that the GitLab OAuth application's Redirect URI exactly matches the Redirect URI shown in ChatGPT.
* **ChatGPT cannot create or save the draft app:** Confirm that the hostname, Application ID, Secret, and Redirect URI are present.
* **Authentication succeeds but project calls fail:** Confirm that the authorizing GitLab user can access the project and that the OAuth application has the template scopes.
* **API returns 403 or insufficient permissions:** Confirm that the connected GitLab account has the required project or group permissions and that the OAuth application includes the required template scopes.
* **No projects are accessible:** Confirm that the user has project access, is connected to the intended GitLab instance, and selected the correct GitLab app in ChatGPT or Codex.

# Related GitLab documentation

* [GitLab docs: Configure GitLab as an OAuth 2.0 identity provider](https://docs.gitlab.com/integration/oauth_provider/)
* [GitLab docs: Access token scopes](https://docs.gitlab.com/security/tokens/access_token_scopes/)
* [GitLab docs: OAuth 2.0 identity provider API](https://docs.gitlab.com/api/oauth2/)
* [GitLab docs: Personal access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/)
* [GitLab docs: Roles and permissions](https://docs.gitlab.com/user/permissions/)
* [GitLab docs: Webhooks](https://docs.gitlab.com/user/project/integrations/webhooks/)
