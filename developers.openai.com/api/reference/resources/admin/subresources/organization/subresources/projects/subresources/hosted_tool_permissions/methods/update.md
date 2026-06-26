<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project hosted tool permissions

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

Updates hosted tool permissions for a project.

##### Path ParametersExpand Collapse

project\_id: string

##### Body ParametersJSONExpand Collapse

code\_interpreter: optional object { enabled }

The code interpreter permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

file\_search: optional object { enabled }

The file search permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

image\_generation: optional object { enabled }

The image generation permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

mcp: optional object { enabled }

The MCP permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

web\_search: optional object { enabled }

The web search permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

##### ReturnsExpand Collapse

ProjectHostedToolPermissions object { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

file\_search: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

image\_generation: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

mcp: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

web\_search: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

### Modify project hosted tool permissions

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/hosted_tool_permissions \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "file_search": {
          "enabled": true
      "image_generation": {
          "enabled": false
  }'

    "file_search": {
        "enabled": true
    "web_search": {
        "enabled": true
    "image_generation": {
        "enabled": false
    "mcp": {
        "enabled": true
    "code_interpreter": {
        "enabled": true

##### Returns Examples

    "file_search": {
        "enabled": true
    "web_search": {
        "enabled": true
    "image_generation": {
        "enabled": false
    "mcp": {
        "enabled": true
    "code_interpreter": {
        "enabled": true
