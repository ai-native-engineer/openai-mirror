<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve/ -->

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

# Retrieve project hosted tool permissions

[ProjectHostedToolPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) admin().organization().projects().hostedToolPermissions().retrieve(HostedToolPermissionRetrieveParamsparams = HostedToolPermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

Returns hosted tool permissions for a project.

##### ParametersExpand Collapse

HostedToolPermissionRetrieveParams params

Optional<String> projectId

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

### Retrieve project hosted tool permissions

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
import com.openai.models.admin.organization.projects.hostedtoolpermissions.HostedToolPermissionRetrieveParams;
import com.openai.models.admin.organization.projects.hostedtoolpermissions.ProjectHostedToolPermissions;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectHostedToolPermissions projectHostedToolPermissions = client.admin().organization().projects().hostedToolPermissions().retrieve("project_id");

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
