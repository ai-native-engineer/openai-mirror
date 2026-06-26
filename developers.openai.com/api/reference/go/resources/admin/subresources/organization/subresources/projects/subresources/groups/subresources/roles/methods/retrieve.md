<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve/ -->

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

# Retrieve project group role

client.Admin.Organization.Projects.Groups.Roles.Get(ctx, projectID, groupID, roleID) (\*[AdminOrganizationProjectGroupRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleGetResponse%20%3E%20(schema)), error)

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

Retrieves a project role assigned to a group.

##### ParametersExpand Collapse

projectID string

groupID string

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationProjectGroupRoleGetResponse struct{…}

Detailed information about a role assignment entry returned when listing assignments.

ID string

Identifier for the role.

AssignmentSources []AdminOrganizationProjectGroupRoleGetResponseAssignmentSource

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

### Retrieve project group role

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
  role, err := client.Admin.Organization.Projects.Groups.Roles.Get(
    context.TODO(),
    "project_id",
    "group_id",
    "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.ID)

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
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

##### Returns Examples

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
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null
