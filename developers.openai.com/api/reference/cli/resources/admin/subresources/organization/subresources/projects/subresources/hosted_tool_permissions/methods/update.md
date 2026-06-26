<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project hosted tool permissions

$ openai admin:organization:projects:hosted-tool-permissions update

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

Updates hosted tool permissions for a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--code-interpreter: optional object { enabled }

The code interpreter permission update.

--file-search: optional object { enabled }

The file search permission update.

--image-generation: optional object { enabled }

The image generation permission update.

--mcp: optional object { enabled }

The MCP permission update.

--web-search: optional object { enabled }

The web search permission update.

##### ReturnsExpand Collapse

project\_hosted\_tool\_permissions: object { code\_interpreter, file\_search, image\_generation, 2 more }

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

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:hosted-tool-permissions update \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

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
