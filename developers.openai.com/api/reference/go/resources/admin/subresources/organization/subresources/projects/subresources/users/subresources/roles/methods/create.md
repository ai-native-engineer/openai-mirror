<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create/ -->

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

# Assign project role to user

client.Admin.Organization.Projects.Users.Roles.New(ctx, projectID, userID, body) (\*[AdminOrganizationProjectUserRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleNewResponse%20%3E%20(schema)), error)

POST/projects/{project\_id}/users/{user\_id}/roles

Assigns a project role to a user within a project.

##### ParametersExpand Collapse

projectID string

userID string

body AdminOrganizationProjectUserRoleNewParams

RoleID param.Field[string]

Identifier of the role to assign.

##### ReturnsExpand Collapse

type AdminOrganizationProjectUserRoleNewResponse struct{…}

Role assignment linking a user to a role.

Object UserRole

Always `user.role`.

Role [Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

ID string

Identifier for the role.

Description string

Optional description of the role.

Name string

Unique name for the role.

Object Role

Always `role`.

Permissions []string

Permissions granted by the role.

PredefinedRole bool

Whether the role is predefined and managed by OpenAI.

ResourceType string

Resource type the role is bound to (for example `api.organization` or `api.project`).

User [OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

Represents an individual `user` within an organization.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

Object OrganizationUser

The object type, which is always `organization.user`

APIKeyLastUsedAt int64Optional

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Created int64Optional

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

DeveloperPersona stringOptional

The developer persona metadata for the user.

Email stringOptional

The email address of the user

IsDefault boolOptional

Whether this is the organization’s default user.

IsScaleTierAuthorizedPurchaser boolOptional

Whether the user is an authorized purchaser for Scale Tier.

IsScimManaged boolOptional

Whether the user is managed through SCIM.

IsServiceAccount boolOptional

Whether the user is a service account.

Name stringOptional

The name of the user

Projects OrganizationUserProjectsOptional

Projects associated with the user, if included.

Data []OrganizationUserProjectsData

ID stringOptional

Name stringOptional

Role stringOptional

Object List

Role stringOptional

`owner` or `reader`

TechnicalLevel stringOptional

The technical level metadata for the user.

User OrganizationUserUserOptional

Nested user details.

ID string

Object User

Banned boolOptional

BannedAt int64Optional

formatunixtime

Email stringOptional

Enabled boolOptional

Name stringOptional

Picture stringOptional

### Assign project role to user

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
  role, err := client.Admin.Organization.Projects.Users.Roles.New(
    context.TODO(),
    "project_id",
    "user_id",
    openai.AdminOrganizationProjectUserRoleNewParams{
      RoleID: "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.Object)

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8PROJ",
        "name": "API Project Key Manager",
        "description": "Allows managing API keys for the project",
        "permissions": [
            "api.organization.projects.api_keys.read",
            "api.organization.projects.api_keys.write"
        ],
        "resource_type": "api.project",
        "predefined_role": false

##### Returns Examples

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8PROJ",
        "name": "API Project Key Manager",
        "description": "Allows managing API keys for the project",
        "permissions": [
            "api.organization.projects.api_keys.read",
            "api.organization.projects.api_keys.write"
        ],
        "resource_type": "api.project",
        "predefined_role": false
