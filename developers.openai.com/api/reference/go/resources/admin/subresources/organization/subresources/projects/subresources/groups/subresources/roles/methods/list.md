<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project group role assignments

client.Admin.Organization.Projects.Groups.Roles.List(ctx, projectID, groupID, query) (\*NextCursorPage[[AdminOrganizationProjectGroupRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleListResponse%20%3E%20(schema))], error)

GET/projects/{project\_id}/groups/{group\_id}/roles

Lists the project roles assigned to a group within a project.

##### ParametersExpand Collapse

projectID string

groupID string

query AdminOrganizationProjectGroupRoleListParams

After param.Field[string]Optional

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing project roles.

Limit param.Field[int64]Optional

A limit on the number of project role assignments to return.

minimum0

maximum1000

Order param.Field[[AdminOrganizationProjectGroupRoleListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for the returned project roles.

const AdminOrganizationProjectGroupRoleListParamsOrderAsc [AdminOrganizationProjectGroupRoleListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationProjectGroupRoleListParamsOrderDesc [AdminOrganizationProjectGroupRoleListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list#(resource)%20admin.organization.projects.groups.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type AdminOrganizationProjectGroupRoleListResponse struct{…}

Detailed information about a role assignment entry returned when listing assignments.

ID string

Identifier for the role.

AssignmentSources []AdminOrganizationProjectGroupRoleListResponseAssignmentSource

Principals from which the role assignment is inherited, when available.

PrincipalID string

PrincipalType string

CreatedAt int64

When the role was created.

formatunixtime

CreatedBy string

Identifier of the actor who created the role.

CreatedByUserObj map[string, any]

User details for the actor that created the role, when available.

Description string

Description of the role.

Metadata map[string, any]

Arbitrary metadata stored on the role.

Name string

Name of the role.

Permissions []string

Permissions associated with the role.

PredefinedRole bool

Whether the role is predefined by OpenAI.

ResourceType string

Resource type the role applies to.

UpdatedAt int64

When the role was last updated.

formatunixtime

### List project group role assignments

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
  page, err := client.Admin.Organization.Projects.Groups.Roles.List(
    context.TODO(),
    "project_id",
    "group_id",
    openai.AdminOrganizationProjectGroupRoleListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "id": "role_01J1F8PROJ",
            "name": "API Project Key Manager",
            "permissions": [
                "api.organization.projects.api_keys.read",
                "api.organization.projects.api_keys.write"
            ],
            "resource_type": "api.project",
            "predefined_role": false,
            "description": "Allows managing API keys for the project",
            "created_at": 1711471533,
            "updated_at": 1711472599,
            "created_by": "user_abc123",
            "created_by_user_obj": {
                "id": "user_abc123",
                "name": "Ada Lovelace",
                "email": "ada@example.com"
            "metadata": {}
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "role_01J1F8PROJ",
            "name": "API Project Key Manager",
            "permissions": [
                "api.organization.projects.api_keys.read",
                "api.organization.projects.api_keys.write"
            ],
            "resource_type": "api.project",
            "predefined_role": false,
            "description": "Allows managing API keys for the project",
            "created_at": 1711471533,
            "updated_at": 1711472599,
            "created_by": "user_abc123",
            "created_by_user_obj": {
                "id": "user_abc123",
                "name": "Ada Lovelace",
                "email": "ada@example.com"
            "metadata": {}
    ],
    "has_more": false,
    "next": null
