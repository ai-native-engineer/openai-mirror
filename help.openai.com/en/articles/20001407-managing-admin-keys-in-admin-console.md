<!-- source: https://help.openai.com/en/articles/20001407-managing-admin-keys-in-admin-console -->

# Managing Admin keys in Admin Console

Create and manage workspace-scoped Admin keys for supported ChatGPT and Codex administration APIs.

Admin keys let authorized workspace owners and admins connect tools and services to supported ChatGPT and Codex administration APIs. Depending on the workspace and permissions you select, a key can support analytics, user and group management, invitations, usage limits, compliance and activity logs, or service-account administration.

Each Admin key applies to one ChatGPT workspace. It does not grant access to other workspaces, tenant-wide administration, API Platform organizations, Ads accounts, models, or model inference.

For help selecting your tenant or workspace, see: [Managing your tenant in Admin Console](https://help.openai.com/articles/12289294).

# Check workspace availability and access

Admin keys are available for eligible managed ChatGPT workspaces, including ChatGPT Enterprise, ChatGPT Edu, and ChatGPT for Healthcare workspaces. You must have the **Owner** or **Admin** role in the specific workspace you want to manage.

Access depends on the **Owner** or **Admin** role assigned in the selected ChatGPT workspace. Being a global admin, an API Platform organization owner, or a user with a custom workspace role does not grant Admin key access on its own.

For details about built-in workspace roles, see: [Managing members, seat types, roles and access in ChatGPT Enterprise](https://help.openai.com/articles/8266401).

# Understand access by role

* Workspace owners can create keys with **All**, **Read only**, or **Custom** permissions. They can edit or revoke any Admin key in their workspace.
* Workspace admins create custom-scoped keys by choosing the available access level for each permission category. The resulting key is labeled **Custom**. They can edit or revoke only keys they created, and only when the key’s permissions are available to their current role.
* Global admins who do not have the **Owner** or **Admin** role in the selected workspace cannot create or manage that workspace’s Admin keys.

# Choose Admin key permissions

## Owner permission presets

Workspace owners can choose one of these permission presets:

* **All** grants the available admin permissions for the selected workspace, including owner-only permissions when available.
* **Read only** grants the available read-only permissions for the selected workspace.
* **Custom** lets you choose the available access level for each permission category.

## Admin permissions by category

Workspace admins do not see the **All**, **Read only**, or **Custom** preset selector. Under **Permissions**, they choose **None**, **Read**, or **Write** for each available category. The resulting key is labeled **Custom**.

Depending on your workspace, available categories can include **Apps**, **Usage limits**, **Group Management**, **Users**, **Invitations**, **Codex analytics API**, **Enterprise analytics API**, **Workspace analytics**, **Costs**, and **Service accounts**. Some categories support only **Read** or **Write**, and some appear only when the related feature is available.

Common permission mappings include:

* **Codex analytics API > Read**: `codex.enterprise.analytics.read`.
* **Usage limits > Read**: `chatgpt.enterprise.usage_limit.read`.
* **Usage limits > Write**: `chatgpt.enterprise.usage_limit.write` and `chatgpt.enterprise.usage_limit.read`.
* **Users > Read**: `chatgpt.enterprise.user.read`, where available.

Broad compliance permissions, **Conversation messages**, and **Roles and permissions** are available only to workspace owners when supported. Workspace admins may still be able to select individual activity-log categories, such as audit or authentication logs.

# Create an Admin key

1. Sign in to [**Admin Console**](https://admin.openai.com).
2. Select your tenant if needed, then select the ChatGPT workspace where you have the **Owner** or **Admin** role.
3. Open **Credentials**, then select **Admin keys**.
4. Select **Create new admin key** and enter a descriptive name.
5. Choose an expiration: **Never**, **30 days**, **60 days**, **90 days**, or **Custom**. A custom expiration can be between 1 and 365 days.
6. Choose the permissions your integration needs. Workspace owners can select **All**, **Read only**, or **Custom**; workspace admins select the available permission for each category.
7. Select **Submit**, then copy and securely store the secret. You cannot view the secret again.

Workspace owner keys can default to **All** permissions, and expiration can default to **Never**. Review both settings before you create a key.

# Review, edit, or revoke an Admin key

Open the ChatGPT workspace in Admin Console, then go to **Credentials > Admin keys**. Review each key’s name, status, tracking ID, redacted secret, creator, permissions, last-used date, and expiration.

* To change a key’s name or permissions, open its more options menu (•••), select **Edit**, make your changes, and select **Save changes**.
* To stop using a key, open its more options menu (•••), select **Revoke**, and confirm with **Revoke admin key**.

Workspace owners can edit or revoke any key for the selected workspace. Workspace admins can edit or revoke only keys they created, and only when the key’s permissions are available to their current role. Ask a workspace owner to manage keys with owner-only permissions. Existing expiration dates cannot be changed.

Revoked keys stop working after the change takes effect. Create a replacement and update any affected integrations before revoking a key that is still in use.

# Understand compliance and sensitive data

Some Admin key permissions can expose sensitive workspace activity or content. Only workspace owners can grant broad compliance access or access to **Conversation messages**.

Workspace admins may be able to grant access to supported individual log categories, including audit, authentication, or app logs. Review each category carefully; individual logs can still contain sensitive information.

For information about compliance APIs and data access, see: [OpenAI Compliance Platform for Enterprise and Edu Customers](https://help.openai.com/articles/9261474).

ChatGPT workspace Admin API requests use `https://api.chatgpt.com/v1`. For example, use `/manage/workspaces/{workspace_id}/users` to list current workspace members. Endpoints under `/v1/organization/` manage API Platform organizations and require an API Platform organization Admin key.

For endpoint paths, request and response schemas, and required scopes, see the [Admin API reference](https://chatgpt.com/public/admin/api-reference).

# Distinguish Admin keys from other credentials

* Workspace Admin keys authenticate supported ChatGPT and Codex administration APIs for one ChatGPT workspace. They do not grant access to model inference.
* Codex service-account access tokens authenticate a non-human workspace identity for Codex automation. They do not authenticate Admin API requests. For setup guidance, see: [Create and manage Codex service accounts](https://developers.openai.com/codex/enterprise/service-accounts).
* API Platform organization Admin keys are managed separately in the API Platform and do not administer ChatGPT workspaces.

If you need a key for an API Platform organization, open [API Platform organization Admin keys](https://platform.openai.com/settings/organization/admin-keys). Use workspace-specific ChatGPT Admin API endpoints with a workspace Admin key; API Platform organization endpoints require separate credentials.

# Troubleshoot access and missing permissions

* Confirm you signed in with the correct OpenAI account and selected the intended tenant and ChatGPT workspace.
* Check that your workspace membership is active and your workspace role is **Owner** or **Admin**.
* Make sure your ChatGPT workspace is eligible for Admin keys. Availability can vary by plan and rollout.
* If a permission category is missing, confirm that the feature is available in the selected workspace and that your role allows access. If the required category is still unavailable, contact OpenAI Support instead of selecting an unrelated permission.
* If you cannot edit or revoke a key, confirm that you created it and that its permissions are available to your current role. Ask a workspace owner to manage keys with owner-only permissions.
* If a previously working key stops working, check its **Status** and **Expiration**, confirm that it has not expired or been revoked, and verify that its creator still has an active workspace role with the required permissions.

If the issue continues, contact OpenAI Support. Include the tenant ID, workspace name or ID, and a screenshot if requested, but never share an Admin key secret.

# Protect your Admin keys

* Choose **Custom** permissions and grant only the access your integration needs.
* Set an expiration when possible. **Never** means the key has no scheduled expiration. A key can still stop working if it is revoked, its creator loses the required workspace access, or the creator’s account is deactivated.
* Use separate keys for different integrations or workflows.
* Store secrets in a [secure secret manager](https://developers.openai.com/api/reference/overview#authentication). Never send them through email, chat, or a support request.
* Review usage and expiration regularly, and revoke keys you no longer need.
