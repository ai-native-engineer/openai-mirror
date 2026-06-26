<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list/ -->

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

# List project groups

client.Admin.Organization.Projects.Groups.List(ctx, projectID, query) (\*NextCursorPage[[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/groups

Lists the groups that have access to a project.

##### ParametersExpand Collapse

projectID string

query AdminOrganizationProjectGroupListParams

After param.Field[string]Optional

Cursor for pagination. Provide the ID of the last group from the previous response to fetch the next page.

Limit param.Field[int64]Optional

A limit on the number of project groups to return. Defaults to 20.

minimum0

maximum100

Order param.Field[[AdminOrganizationProjectGroupListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for the returned groups.

const AdminOrganizationProjectGroupListParamsOrderAsc [AdminOrganizationProjectGroupListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationProjectGroupListParamsOrderDesc [AdminOrganizationProjectGroupListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

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

### List project groups

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
  page, err := client.Admin.Organization.Projects.Groups.List(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectGroupListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "object": "project.group",
            "project_id": "proj_abc123",
            "group_id": "group_01J1F8ABCDXYZ",
            "group_name": "Support Team",
            "created_at": 1711471533
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "project.group",
            "project_id": "proj_abc123",
            "group_id": "group_01J1F8ABCDXYZ",
            "group_name": "Support Team",
            "created_at": 1711471533
    ],
    "has_more": false,
    "next": null
