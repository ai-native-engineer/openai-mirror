<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project hosted tool permissions

admin.organization.projects.hosted\_tool\_permissions.update(strproject\_id, HostedToolPermissionUpdateParams\*\*kwargs)  -> [ProjectHostedToolPermissions](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema))

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

Updates hosted tool permissions for a project.

##### ParametersExpand Collapse

project\_id: str

code\_interpreter: Optional[[CodeInterpreter](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20code_interpreter%20%3E%20(schema))]

The code interpreter permission update.

enabled: bool

Whether to enable the hosted tool for the project.

file\_search: Optional[[FileSearch](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20file_search%20%3E%20(schema))]

The file search permission update.

enabled: bool

Whether to enable the hosted tool for the project.

image\_generation: Optional[[ImageGeneration](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20image_generation%20%3E%20(schema))]

The image generation permission update.

enabled: bool

Whether to enable the hosted tool for the project.

mcp: Optional[[Mcp](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20mcp%20%3E%20(schema))]

The MCP permission update.

enabled: bool

Whether to enable the hosted tool for the project.

web\_search: Optional[[WebSearch](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20web_search%20%3E%20(schema))]

The web search permission update.

enabled: bool

Whether to enable the hosted tool for the project.

##### ReturnsExpand Collapse

class ProjectHostedToolPermissions: …

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

file\_search: FileSearch

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

mcp: Mcp

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

web\_search: WebSearch

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

### Modify project hosted tool permissions

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
project_hosted_tool_permissions = client.admin.organization.projects.hosted_tool_permissions.update(
    project_id="project_id",
print(project_hosted_tool_permissions.code_interpreter)

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
