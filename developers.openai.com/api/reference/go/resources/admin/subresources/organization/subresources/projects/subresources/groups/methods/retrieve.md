<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project group

client.Admin.Organization.Projects.Groups.Get(ctx, projectID, groupID, query) (\*[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/groups/{group\_id}

Retrieves a project’s group.

##### ParametersExpand Collapse

projectID string

groupID string

query AdminOrganizationProjectGroupGetParams

GroupType param.Field[[AdminOrganizationProjectGroupGetParamsGroupType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20group_type%20%3E%20(schema))]Optional

The type of group to retrieve.

const AdminOrganizationProjectGroupGetParamsGroupTypeGroup [AdminOrganizationProjectGroupGetParamsGroupType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20group_type%20%3E%20(schema)) = "group"

const AdminOrganizationProjectGroupGetParamsGroupTypeTenantGroup [AdminOrganizationProjectGroupGetParamsGroupType](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20group_type%20%3E%20(schema)) = "tenant\_group"

##### ReturnsExpand Collapse

type ProjectGroup struct{…}

Details about a group’s membership in a project.

CreatedAt int64

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

GroupID string

Identifier of the group that has access to the project.

GroupName string

Display name of the group.

GroupType ProjectGroupGroupType

The type of the group.

One of the following:

const ProjectGroupGroupTypeGroup ProjectGroupGroupType = "group"

const ProjectGroupGroupTypeTenantGroup ProjectGroupGroupType = "tenant\_group"

Object ProjectGroup

Always `project.group`.

ProjectID string

Identifier of the project.

### Retrieve project group

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
  projectGroup, err := client.Admin.Organization.Projects.Groups.Get(
    context.TODO(),
    "project_id",
    "group_id",
    openai.AdminOrganizationProjectGroupGetParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectGroup.GroupID)

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "group_type": "group",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "group_type": "group",
    "created_at": 1711471533
