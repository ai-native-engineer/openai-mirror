<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve user organization role

client.Admin.Organization.Users.Roles.Get(ctx, userID, roleID) (\*[AdminOrganizationUserRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleGetResponse%20%3E%20(schema)), error)

GET/organization/users/{user\_id}/roles/{role\_id}

Retrieves an organization role assigned to a user.

##### ParametersExpand Collapse

userID string

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationUserRoleGetResponse struct{…}

Detailed information about a role assignment entry returned when listing assignments.

ID string

Identifier for the role.

AssignmentSources []AdminOrganizationUserRoleGetResponseAssignmentSource

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

### Retrieve user organization role

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
  role, err := client.Admin.Organization.Users.Roles.Get(
    context.TODO(),
    "user_id",
    "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.ID)

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null

##### Returns Examples

    "id": "role_01J1F8ROLE01",
    "name": "API Group Manager",
    "permissions": [
        "api.groups.read",
        "api.groups.write"
    ],
    "resource_type": "api.organization",
    "predefined_role": false,
    "description": "Allows managing organization groups",
    "created_at": 1711471533,
    "updated_at": 1711472599,
    "created_by": "user_abc123",
    "created_by_user_obj": null,
    "metadata": {},
    "assignment_sources": null
