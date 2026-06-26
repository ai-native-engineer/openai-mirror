<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project hosted tool permissions

[ProjectHostedToolPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) admin().organization().projects().hostedToolPermissions().update(HostedToolPermissionUpdateParamsparams = HostedToolPermissionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

Updates hosted tool permissions for a project.

##### ParametersExpand Collapse

HostedToolPermissionUpdateParams params

Optional<String> projectId

Optional<CodeInterpreter> codeInterpreter

The code interpreter permission update.

boolean enabled

Whether to enable the hosted tool for the project.

Optional<FileSearch> fileSearch

The file search permission update.

boolean enabled

Whether to enable the hosted tool for the project.

Optional<ImageGeneration> imageGeneration

The image generation permission update.

boolean enabled

Whether to enable the hosted tool for the project.

Optional<Mcp> mcp

The MCP permission update.

boolean enabled

Whether to enable the hosted tool for the project.

Optional<WebSearch> webSearch

The web search permission update.

boolean enabled

Whether to enable the hosted tool for the project.

##### ReturnsExpand Collapse

class ProjectHostedToolPermissions:

Represents hosted tool permissions for a project.

CodeInterpreter codeInterpreter

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

FileSearch fileSearch

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

ImageGeneration imageGeneration

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

Mcp mcp

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

WebSearch webSearch

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

### Modify project hosted tool permissions

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.hostedtoolpermissions.HostedToolPermissionUpdateParams;
import com.openai.models.admin.organization.projects.hostedtoolpermissions.ProjectHostedToolPermissions;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectHostedToolPermissions projectHostedToolPermissions = client.admin().organization().projects().hostedToolPermissions().update("project_id");

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
