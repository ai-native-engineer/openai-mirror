<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project role

client.Admin.Organization.Projects.Roles.New(ctx, projectID, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/projects/{project\_id}/roles

Creates a custom role for a project.

##### ParametersExpand Collapse

projectID string

body AdminOrganizationProjectRoleNewParams

Permissions param.Field[[]string]

Permissions to grant to the role.

RoleName param.Field[string]

Unique name for the role.

Description param.Field[string]Optional

Optional description of the role.

##### ReturnsExpand Collapse

type Role struct{…}

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

### Create project role

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
  role, err := client.Admin.Organization.Projects.Roles.New(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectRoleNewParams{
      Permissions: []string{"string"},
      RoleName: "role_name",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.ID)

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
