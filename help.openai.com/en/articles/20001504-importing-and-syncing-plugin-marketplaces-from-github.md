<!-- source: https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github -->

# Importing and syncing plugin marketplaces from GitHub

Learn how to import a plugin marketplace from GitHub, manage workspace access, and keep its plugins up to date.

Updated: 16 days ago

Workspace admins can import a plugin marketplace from GitHub into their workspace directory. A marketplace is a JSON catalog that lists the plugins to import. After import, daily sync keeps the plugins up to date with changes from the repository.

Marketplace sync imports plugin content - it does not connect workspace members' accounts or grant access to the apps included in a plugin.

For an introduction to plugins and their included apps, see: [Plugins in ChatGPT and Codex](https://help.openai.com/articles/20001256).

## Before you begin

* Use a GitHub account that can read the marketplace repository and every other repository it references. Public and private repositories on github.com are supported.
* Complete any GitHub organization approval required for the importing account to access those repositories.
* Review the repository content. Import processes all valid plugins without a separate approval step for each one, and future syncs can add new plugins.

New plugins start with **Available** installation and authentication on install. New marketplaces have automatic daily sync enabled. After import, review each plugin's workspace settings and required apps.

# Import a marketplace

1. Go to [Admin Console](https://admin.openai.com), select the intended ChatGPT workspace, and open **Plugins**. Then select **Add** and choose **Import marketplace**.
2. In **Source**, enter the repository URL, such as `https://github.com/example/team-plugins`. Use the repository URL only, without a branch or folder URL.
3. If the marketplace is in a subdirectory, enter that directory in **Path**. For example, enter `team-tools` for `team-tools/.agents/plugins/marketplace.json`. Leave **Path** empty for the repository root. Do not enter the manifest filename.
4. Optionally enter a **Branch, tag, or commit**. Leave it empty to use the repository's default branch. Use a branch to receive future commits. A fixed commit stays at that revision.
5. Select **Import marketplace** and authorize GitHub access when prompted.
6. Review **Import results**, then open each imported plugin to configure its installation policy and any required apps.

The initial import can take up to 1 hour for very large marketplaces. Subsequent daily syncs typically take a few minutes.

If a plugin cannot be imported, the report explains the error. Other valid plugins can still be imported.

## Supported formats

The selected directory must contain a supported manifest:

* `.agents/plugins/marketplace.json` for a Codex marketplace.
* `.claude-plugin/marketplace.json` for a Claude-compatible marketplace.
* `.claude-plugin/plugin.json` for a standalone Claude plugin when no marketplace manifest is present.

Marketplace entries can reference plugin folders in the same repository or supported GitHub repository sources. Other Git hosts and package-registry sources, such as npm, are not supported by workspace import.

For supported formats, JSON examples, and source fields, see: [Plugin Management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

# Configure workspace access

GitHub supplies the plugin content, while workspace settings control installation and authentication. Import and sync do not apply repository policy values, such as `AVAILABLE` or `ON_USE`. Configure these settings for each plugin in your workspace.

Use **Installation policy** to choose **Available** or **Installed** for each eligible role. Required apps must also be enabled, and members must have access to the connected service and complete any required authentication.

Syncing a plugin update or moving an existing plugin to GitHub management preserves its workspace policies. Importing a plugin does not grant app access or connect members' accounts.

For workspace navigation, app access, and workspace controls, see: [Admin controls, security, and compliance for plugins and apps](https://help.openai.com/articles/11509118).

# Keep plugins up to date

New marketplaces check for updates daily. To request an update without waiting for automatic sync:

1. Go to [Admin Console](https://admin.openai.com), select the intended ChatGPT workspace, and open **Plugins**.
2. Open **Marketplaces** and select the marketplace.
3. Select **Sync now**.

Sync can add new marketplace entries and update existing plugins. Review repository changes before merging them, because automatic sync can import new plugins without another import step.

## Review sync results

After a sync, review its status and saved report. **Completed — N errors** means the sync finished, but some plugins could not be processed.

If an update to an existing plugin is invalid, its last working version is retained. Other valid updates can still complete. Fix the reported problem in GitHub, then select **Sync now** to retry.

If your admin view shows **Refresh** for an individually imported plugin, use it to refresh that plugin. **Refresh plugin list** only reloads the displayed list; it does not sync from GitHub.

## Understand removal and deletion

Removing an entry from the repository does not delete its imported workspace copy. The plugin is marked **No longer in source**.

Deleting the marketplace in ChatGPT deletes all plugins imported from it. Do not delete a marketplace to reconnect GitHub or change ownership.

# Reconnect or change GitHub access

Marketplace sync uses the GitHub connection of the admin who imported it. That account needs continued access to the marketplace repository and any referenced repositories.

## Reconnect the original account

1. Confirm that the GitHub account used for the import still has access to all required repositories.
2. Ask the admin who originally imported the marketplace to open the GitHub plugin in ChatGPT and reconnect their account.

## Transfer to a new admin

The new workspace admin can import the same marketplace using their own GitHub connection:

1. Go to [Admin Console](https://admin.openai.com), select the intended ChatGPT workspace, and open **Plugins**. Then select **Add > Import marketplace**.
2. Enter the same **Source**, **Path**, and **Branch, tag, or commit** values used for the existing marketplace.
3. Select **Import marketplace** and authorize GitHub access when prompted.

Future syncs use the new admin's GitHub connection. The new admin's account must be able to read the marketplace repository and every repository it references.

# Move an existing plugin to GitHub management

You can use a marketplace to manage an existing workspace plugin that was uploaded as an archive or is not yet managed by a GitHub source. The existing plugin must be in the same workspace and have the same plugin name. A plugin managed by a different GitHub source cannot be taken over this way.

To identify the existing plugin in your marketplace:

1. Go to [Admin Console](https://admin.openai.com), select the intended ChatGPT workspace, and open **Plugins**. Open the plugin.
2. Copy the plugin ID after `/admin/plugins/` in its URL.
3. Add that ID as `pluginId` beside `name` and `source` in the matching entry of the marketplace's `plugins` array. Do not add it to the plugin's `plugin.json` file.

The plugin keeps its ID, sharing, and workspace policies. GitHub becomes the source for future updates, so later archive uploads cannot replace it.

For a migration example and requirements, see: [Plugin Management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

# Reference an existing app

A plugin can reference an existing app in `.app.json` at the plugin root. Include the leading dot in the filename, and use the app's ID rather than a plugin ID. For a native plugin, set the `apps` field in `.codex-plugin/plugin.json` to `./.app.json`.

The reference does not create an app or grant additional permissions. The app's existing workspace access, authentication, action controls, and connected-service permissions still apply.

For the JSON format, see: [Plugin Management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Understand the Desktop only label

A plugin marked **Desktop only** cannot run in ChatGPT on the web. Imported plugins can receive this label when they declare MCP servers, for example in `mcp.json` or `.mcp.json`, even when a server uses a remote HTTPS URL.

Adding an `.app.json` reference does not by itself remove the **Desktop only** label. Any referenced app must still be available to the member's role, and its normal access and authentication requirements apply.
