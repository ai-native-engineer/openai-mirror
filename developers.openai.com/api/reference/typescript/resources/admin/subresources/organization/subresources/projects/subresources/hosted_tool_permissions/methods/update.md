<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project hosted tool permissions

client.admin.organization.projects.hostedToolPermissions.update(stringprojectID, HostedToolPermissionUpdateParams { code\_interpreter, file\_search, image\_generation, 2 more } body, RequestOptionsoptions?): [ProjectHostedToolPermissions](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

Updates hosted tool permissions for a project.

##### ParametersExpand Collapse

projectID: string

body: HostedToolPermissionUpdateParams { code\_interpreter, file\_search, image\_generation, 2 more }

code\_interpreter?: [CodeInterpreter](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20code_interpreter%20%3E%20(schema)) | null

The code interpreter permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

file\_search?: [FileSearch](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20file_search%20%3E%20(schema)) | null

The file search permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

image\_generation?: [ImageGeneration](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20image_generation%20%3E%20(schema)) | null

The image generation permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

mcp?: [Mcp](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20mcp%20%3E%20(schema)) | null

The MCP permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

web\_search?: [WebSearch](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20web_search%20%3E%20(schema)) | null

The web search permission update.

enabled: boolean

Whether to enable the hosted tool for the project.

##### ReturnsExpand Collapse

ProjectHostedToolPermissions { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

file\_search: FileSearch { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

mcp: Mcp { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

web\_search: WebSearch { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

### Modify project hosted tool permissions

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const projectHostedToolPermissions =
  await client.admin.organization.projects.hostedToolPermissions.update('project_id');

console.log(projectHostedToolPermissions.code_interpreter);

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
