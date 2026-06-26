<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Hosted Tool Permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project hosted tool permissions

client.Admin.Organization.Projects.HostedToolPermissions.Update(ctx, projectID, body) (\*[ProjectHostedToolPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

Updates hosted tool permissions for a project.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectHostedToolPermissionUpdateParams

CodeInterpreter param.Field[[AdminOrganizationProjectHostedToolPermissionUpdateParamsCodeInterpreter](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20code_interpreter%20%3E%20(schema))]Optional

The code interpreter permission update.

Enabled bool

Whether to enable the hosted tool for the project.

FileSearch param.Field[[AdminOrganizationProjectHostedToolPermissionUpdateParamsFileSearch](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20file_search%20%3E%20(schema))]Optional

The file search permission update.

Enabled bool

Whether to enable the hosted tool for the project.

ImageGeneration param.Field[[AdminOrganizationProjectHostedToolPermissionUpdateParamsImageGeneration](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20image_generation%20%3E%20(schema))]Optional

The image generation permission update.

Enabled bool

Whether to enable the hosted tool for the project.

Mcp param.Field[[AdminOrganizationProjectHostedToolPermissionUpdateParamsMcp](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20mcp%20%3E%20(schema))]Optional

The MCP permission update.

Enabled bool

Whether to enable the hosted tool for the project.

WebSearch param.Field[[AdminOrganizationProjectHostedToolPermissionUpdateParamsWebSearch](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(method)%20update%20%3E%20(params)%20default%20%3E%20(param)%20web_search%20%3E%20(schema))]Optional

The web search permission update.

Enabled bool

Whether to enable the hosted tool for the project.

##### ReturnsExpand Collapse

type ProjectHostedToolPermissions struct{…}

Represents hosted tool permissions for a project.

CodeInterpreter ProjectHostedToolPermissionsCodeInterpreter

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

FileSearch ProjectHostedToolPermissionsFileSearch

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

ImageGeneration ProjectHostedToolPermissionsImageGeneration

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

Mcp ProjectHostedToolPermissionsMcp

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

WebSearch ProjectHostedToolPermissionsWebSearch

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

### Modify project hosted tool permissions

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  projectHostedToolPermissions, err := client.Admin.Organization.Projects.HostedToolPermissions.Update(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectHostedToolPermissionUpdateParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectHostedToolPermissions.CodeInterpreter)

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
