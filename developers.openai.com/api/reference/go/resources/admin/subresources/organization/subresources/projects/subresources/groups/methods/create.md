<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create/ -->

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

# Add project group

client.Admin.Organization.Projects.Groups.New(ctx, projectID, body) (\*[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/groups

Grants a group access to a project.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectGroupNewParams

GroupID param.Field[string]

Identifier of the group to add to the project.

Role param.Field[string]

Identifier of the project role to grant to the group.

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

### Add project group

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
  projectGroup, err := client.Admin.Organization.Projects.Groups.New(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectGroupNewParams{
      GroupID: "group_id",
      Role: "role",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectGroup.GroupID)

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533
