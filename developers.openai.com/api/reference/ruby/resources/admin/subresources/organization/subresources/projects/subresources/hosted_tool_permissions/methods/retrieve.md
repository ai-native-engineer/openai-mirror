<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project hosted tool permissions

admin.organization.projects.hosted\_tool\_permissions.retrieve(project\_id) -> [ProjectHostedToolPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

Returns hosted tool permissions for a project.

##### ParametersExpand Collapse

project\_id: String

##### ReturnsExpand Collapse

class ProjectHostedToolPermissions { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

file\_search: FileSearch{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

mcp: Mcp{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

web\_search: WebSearch{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

### Retrieve project hosted tool permissions

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_hosted_tool_permissions = openai.admin.organization.projects.hosted_tool_permissions.retrieve("project_id")

puts(project_hosted_tool_permissions)

    "file_search": {
        "enabled": true
    "web_search": {
        "enabled": true
    "image_generation": {
        "enabled": true
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
        "enabled": true
    "mcp": {
        "enabled": true
    "code_interpreter": {
        "enabled": true
