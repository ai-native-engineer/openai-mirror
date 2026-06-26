<!-- source: https://help.openai.com/en/articles/20001250-set-up-the-databricks-app-template-in-chatgpt -->

# Set up the Databricks app template in ChatGPT

Learn how workspace admins can configure the Databricks app template in ChatGPT using their organization's own Databricks OAuth app connection.

Updated: 2 days ago

Use this guide if you are a ChatGPT workspace admin setting up the Databricks app template for your organization. A template is not the final app that members use. It is a setup flow that creates a workspace-specific draft app after you provide the required Databricks configuration.  
  
For Databricks, most of the setup happens in the Databricks Account Console. You create a custom OAuth app connection, register the ChatGPT callback URL, copy the generated client credentials, then paste those values into the ChatGPT template setup flow. After ChatGPT creates the draft app, you can publish it and manage it like other workspace apps.

# What you are setting up

You are creating a workspace-specific Databricks app in ChatGPT. The app uses:

* A Databricks OAuth app connection created in your Databricks Account Console.
* The Databricks OAuth client ID and client secret.
* The exact callback URL copied from ChatGPT.
* Databricks scopes that match the connector capabilities you want to enable.
* Any Databricks provider details requested by the ChatGPT setup flow, such as workspace host, account host, account ID, or warehouse.

# Before you start

You need:

* ChatGPT workspace admin or owner access.
* Databricks account admin access. Workspace admin access may be enough for some tasks, but custom app connections are configured from the Databricks Account Console.
* The Databricks Account Console open in a separate tab.
* The Databricks app template setup screen open in ChatGPT so you can copy the exact callback URL.
* A decision about whether the app needs general Databricks API access or only Databricks SQL access.
* A secure place to handle the Databricks client secret.

Do not invent the callback URL. Copy the exact callback URL shown in ChatGPT.

## Values to prepare

* Callback URL: copy this from the ChatGPT template setup flow.
* Databricks OAuth client ID.
* Databricks OAuth client secret.
* Databricks access scopes, such as ALL APIs or SQL.
* Databricks workspace or account fields requested by the ChatGPT setup flow.

# Publish and manage the app in ChatGPT

Creating the draft app does not automatically make it available to members. After reviewing the draft:

1. Publish the draft app.
2. Confirm the app appears in **Workspace settings > Apps > Enabled**.
3. Configure **User access** for the roles that should use it.
4. Review **Action control** for the Databricks actions exposed by the app.
5. Review **App permissions** to choose when ChatGPT asks members before using the app.
6. Ask an allowed test user to open Apps in ChatGPT and confirm the app appears.

These app permissions apply to ChatGPT conversations. Workspace Agents use per-agent controls set by the agent's builder to determine which app actions are available and when end users are asked to approve them. For agent behavior, see: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).

# Start the template setup in ChatGPT

1. In ChatGPT, switch to the workspace where the app should be available.
2. Open **Workspace settings > Apps**.
3. Select **Directory**.
4. Search for Databricks.
5. Select the Databricks app template and start setup.
6. Enter a clear app name and description, such as Databricks or Databricks - Data Platform.
7. In the OAuth client section, copy the callback URL from ChatGPT. Keep this tab open.

Example callback URL: https://chatgpt.com/connector/oauth/<callback\_id>  
  
Do not remove the callback ID, add a trailing slash, or replace it with a generic ChatGPT URL.

# Create the OAuth app connection in Databricks

1. Open the Databricks Account Console for your Databricks account.
2. In the left sidebar, open **Settings**.
3. Open the **App connections** tab.
4. Select **Add connection**.
5. Enter an application name, such as ChatGPT Databricks Connector.
6. In **Redirect URLs**, paste the exact callback URL copied from ChatGPT.
7. Under **Access scopes**, choose the scopes the app needs.
8. Use ALL APIs for a general Databricks app that needs Databricks APIs beyond SQL.
9. Use SQL only for an app limited to Databricks SQL APIs.
10. Leave token TTLs at the Databricks defaults unless your organization has a specific policy.
11. Enable **Generate a client secret**. ChatGPT needs a confidential OAuth client for this flow.
12. Create the connection.

## Copy credentials from Databricks

1. In the Connection created dialog, copy the **Client ID**.
2. Copy the **Client secret** immediately and store it securely.
3. If you close the dialog before copying the secret, create or rotate the OAuth app credentials and use the new secret.

Databricks shows the secret only once. Treat it like a credential and do not include it in screenshots, tickets, comments, or chats.

# Finish setup in ChatGPT

1. Return to the ChatGPT template setup tab.
2. Paste the Databricks Client ID into OAuth client ID.
3. Paste the Databricks Client secret into OAuth client secret.
4. Leave Scopes unchanged unless you intentionally need to override the template defaults.
5. Fill any Databricks provider fields required by the setup flow, such as workspace host, account host, account ID, warehouse, or other Databricks-specific values.
6. Create the draft app.

# Test the app as a user

1. Start the connect flow from ChatGPT as an allowed test user.
2. Confirm that the browser opens the expected Databricks account or workspace.
3. Approve the requested scopes.
4. Verify that the browser returns to ChatGPT and the app shows as connected.
5. Run a low-risk read action first, such as fetching current user information or querying an approved Databricks SQL resource.
6. If write actions are enabled, test with a clearly low-risk Databricks workflow before broader rollout.

# Manage access

Databricks and ChatGPT both contribute to access control.  
  
In ChatGPT, workspace admins manage whether the published app is available, which workspace roles can use it, which actions are enabled, and when ChatGPT asks users before using the app.  
  
In Databricks, admins manage which users can authorize the OAuth app and which Databricks resources those users can access. Provider permissions still apply after the app is enabled in ChatGPT.

# Troubleshooting

* Redirect URI mismatch: confirm the Databricks Redirect URL exactly matches the callback URL shown in ChatGPT, including path and callback ID.
* Secret missing: Databricks secrets are one-time display. Generate a new client secret if it was not copied.
* OAuth app not available immediately: Databricks says OAuth application updates can take up to 30 minutes to process.
* Insufficient scope: if ChatGPT can authenticate but Databricks API calls fail, confirm the Databricks app has ALL APIs when the app needs non-SQL APIs.
* SQL actions fail: confirm SQL scope, warehouse configuration, and Databricks permissions.
* Wrong workspace: create and publish the app in the same ChatGPT workspace where users will connect it.
* Users cannot connect: confirm the user has Databricks access and is allowed to authorize the OAuth app.

# References

* [Databricks docs: Authentication using OAuth user-to-machine](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m)
* [Databricks docs: Manage OAuth app connections](https://www.notion.so/3568e50b62b080ba8aacfd85ac925a93?pvs=1)
