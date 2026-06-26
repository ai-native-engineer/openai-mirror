<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project user role

client.Admin.Organization.Projects.Users.Roles.Get(ctx, projectID, userID, roleID) (\*[AdminOrganizationProjectUserRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleGetResponse%20%3E%20(schema)), error)

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

Retrieves a project role assigned to a user.

##### ParametersExpand Collapse

projectID string

userID string

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationProjectUserRoleGetResponse struct{…}

Detailed information about a role assignment entry returned when listing assignments.

ID string

Identifier for the role.

AssignmentSources []AdminOrganizationProjectUserRoleGetResponseAssignmentSource

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

### Retrieve project user role

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
  role, err := client.Admin.Organization.Projects.Users.Roles.Get(
    context.TODO(),
    "project_id",
    "user_id",
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
