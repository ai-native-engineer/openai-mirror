<!-- source: https://help.openai.com/en/articles/20001249-set-up-the-snowflake-app-template-in-chatgpt -->

# Set up the Snowflake app template in ChatGPT

Learn how workspace admins can configure the Snowflake app template in ChatGPT using a Snowflake-managed MCP server.

Updated: 9 days ago

Use this guide if you are a ChatGPT workspace admin setting up the Snowflake app template for your organization. A template is not the final app that members use. It is a setup flow that creates a workspace-specific draft app after you provide the required Snowflake configuration.  
  
For Snowflake, most of the setup happens in Snowflake. You create a Snowflake-managed MCP server, grant the right role access to the MCP server and its underlying objects, then enter the managed MCP server URL or its component fields in the ChatGPT template setup flow. After ChatGPT creates the draft app, you can publish it and manage it like other workspace apps.

# What you are setting up

You are creating a workspace-specific Snowflake app in ChatGPT. The app connects to a Snowflake-managed MCP server that defines:

* Which actions ChatGPT can use, called tools.
* Which Snowflake data or objects those tools can access.
* Which Snowflake role users should authorize with.
* Which Snowflake database, schema, and MCP server name identify the connector endpoint.

ChatGPT can only discover and use the tools exposed by the MCP server and allowed by the Snowflake role that the user authorizes with.

# Before you start

You need:

* ChatGPT workspace admin or owner access.
* Snowflake access that can create MCP server objects and grant permissions.
* The Snowflake database and schema where the MCP server will live.
* A decision about what ChatGPT should be allowed to do, such as Cortex Search, Cortex Analyst, read-only SQL, or a specific procedure or function.
* A least-privilege Snowflake role that users will use when authorizing the app.
* The Snowflake account host prefix, including any region or cloud suffix.

## Values to prepare

* Snowflake host prefix: everything before .snowflakecomputing.com in the Snowflake account URL.
* Database: the database containing the MCP server.
* Schema: the schema containing the MCP server.
* MCP server name: the Snowflake MCP server object name.
* Full managed MCP server URL, if the ChatGPT setup screen asks for a URL.
* Snowflake role: the role users should use when authorizing the app.
* Tool list: the Snowflake objects and actions you want ChatGPT to use.

# Decide what ChatGPT can do

Pick only the capabilities you want to expose. Common options include:

* Search with Cortex Search to find answers in indexed Snowflake data or content.
* Q&A with Cortex Analyst through an approved semantic view.
* Read-only SQL for controlled query access.
* A Snowflake Agent, stored procedure, or UDF for specific workflows.

If you enable SQL, keep it read-only unless your organization has reviewed and approved write access.

# Create the Snowflake MCP server

In Snowflake, sign in with a role that can create the MCP server and grant access. Open a worksheet in the database and schema where the MCP server should be created.  
  
Create an MCP server that lists only the tools ChatGPT should use. Replace object names with your own Snowflake database, schema, services, views, warehouse, and server name.  
  
Example:

`CREATE MCP SERVER CHATGPT_SNOWFLAKE_MCP`  
 `FROM SPECIFICATION $$`  
 `tools:`  
 `- name: "support-search"`  
 `type: "CORTEX_SEARCH_SERVICE_QUERY"`  
 `identifier: "CHATGPT_APPS.TOOLS.SUPPORT_SEARCH_SERVICE"`  
 `title: "Support Search"`  
 `description: "Search support content for relevant customer issues."`  
 `- name: "sql-readonly"`  
 `type: "SYSTEM_EXECUTE_SQL"`  
 `title: "Read-only SQL"`  
 `description: "Run read-only SQL queries against approved Snowflake data."`  
 `config:`  
 `read_only: true`  
 `query_timeout: 600`  
 `warehouse: "CHATGPT_WH"`  
 `$$;`

Tool names should be stable and descriptive so ChatGPT can choose the right tool. Creating the MCP server does not automatically grant access to the underlying Snowflake objects.

# Grant the right Snowflake permissions

Choose the Snowflake role users will authorize with, then grant that role access to the database, schema, MCP server, and every underlying object used by the tools.  
  
Example:

`GRANT USAGE ON DATABASE CHATGPT_APPS TO ROLE CHATGPT_CONNECTOR_ROLE;`  
`GRANT USAGE ON SCHEMA CHATGPT_APPS.TOOLS TO ROLE CHATGPT_CONNECTOR_ROLE;`  
`GRANT USAGE ON MCP SERVER CHATGPT_APPS.TOOLS.CHATGPT_SNOWFLAKE_MCP TO ROLE CHATGPT_CONNECTOR_ROLE;`  
`GRANT USAGE ON CORTEX SEARCH SERVICE CHATGPT_APPS.TOOLS.SUPPORT_SEARCH_SERVICE TO ROLE CHATGPT_CONNECTOR_ROLE;`  
`GRANT USAGE ON WAREHOUSE CHATGPT_WH TO ROLE CHATGPT_CONNECTOR_ROLE;`

If the MCP server exposes a semantic view, UDF, stored procedure, or Cortex Agent, grant the required permissions for those objects too.

# Verify Snowflake is ready

Run:

`SHOW MCP SERVERS IN SCHEMA CHATGPT_APPS.TOOLS;`

Then run:

`DESCRIBE MCP SERVER CHATGPT_APPS.TOOLS.CHATGPT_SNOWFLAKE_MCP;`

Confirm:

* The server exists in the expected database and schema.
* The tool list is what you intended.
* Each tool identifier points to the right Snowflake object.
* The connecting role has USAGE on the MCP server.
* The connecting role has the needed permissions on each underlying object.

# Start the template setup in ChatGPT

1. In ChatGPT, switch to the workspace where the app should be available.
2. Open **Workspace settings > Apps**.
3. Select **Directory**.
4. Search for Snowflake.
5. Select the Snowflake app template and start setup.
6. Enter a clear app name and description, such as Snowflake or Snowflake - Analytics.
7. Enter the managed MCP server details requested by the setup flow.

If the setup screen asks for the full managed MCP server URL, use this format:

`https://<snowflake_host_prefix>.snowflakecomputing.com/api/v2/databases/{database}/schemas/{schema}/mcp-servers/{server}`

If the setup screen asks for separate fields, use the same values from that URL:

* Snowflake host prefix.
* Database.
* Schema.
* MCP server name.

# Create and publish the draft app

1. Save the Snowflake template setup in ChatGPT.
2. Create the draft app.
3. Review the draft app details, auth settings, and available actions.
4. Publish the draft app when ready.
5. Confirm the app appears in **Workspace settings > Apps > Enabled**.
6. Configure **User access** for the roles that should use it.
7. Review **Action control** for the exposed tools.
8. Review **App permissions** to choose when ChatGPT asks members before using the app.

These app permissions apply to ChatGPT conversations. Workspace Agents use per-agent controls set by the agent's builder to determine which app actions are available and when end users are asked to approve them. For agent behavior, see: [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/articles/20001143).

# Test the app

1. Start the connect flow from ChatGPT as an allowed test user.
2. Sign in to Snowflake and select the intended role if prompted.
3. Confirm that ChatGPT discovers the expected tools from the MCP server.
4. Run a low-risk read action first, such as a search or read-only query against approved data.
5. Confirm Snowflake permissions prevent access outside the approved role and objects.

# MCP server URL and OAuth behavior

ChatGPT connects to the full Snowflake-managed MCP server URL. ChatGPT uses the Snowflake host prefix from that URL to resolve Snowflake OAuth endpoints.  
  
Do not paste a Snowsight URL, the Snowflake account root URL by itself, or any URL with extra path segments. The MCP URL must include the database, schema, and MCP server path and must match your Snowflake objects exactly.

# Troubleshooting

* MCP server not found: re-check the full MCP server URL or the separate host prefix, database, schema, and server fields.
* No tools appear in ChatGPT: confirm the MCP server spec includes tools and the role has USAGE on the MCP server.
* A tool appears but fails when used: confirm the role has the right permission on the underlying Snowflake object.
* SQL tool fails: confirm the warehouse name is correct, the warehouse is available, the role has USAGE on it, and read\_only is true if you intended read-only access.
* Authorization fails: confirm the user can sign in to Snowflake and use the intended role.
* Hostname connection issue: use the correct Snowflake host prefix. Snowflake hostnames with underscores can cause issues; prefer hyphens.
