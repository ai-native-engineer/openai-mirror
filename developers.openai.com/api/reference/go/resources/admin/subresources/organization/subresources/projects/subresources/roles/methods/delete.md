<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete/ -->

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

# Delete project role

client.Admin.Organization.Projects.Roles.Delete(ctx, projectID, roleID) (\*[AdminOrganizationProjectRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20AdminOrganizationProjectRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/roles/{role\_id}

Deletes a custom role from a project.

##### ParametersExpand Collapse

projectID string

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationProjectRoleDeleteResponse struct{…}

Confirmation payload returned after deleting a role.

ID string

Identifier of the deleted role.

Deleted bool

Whether the role was deleted.

Object RoleDeleted

Always `role.deleted`.

### Delete project role

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
  role, err := client.Admin.Organization.Projects.Roles.Delete(
    context.TODO(),
    "project_id",
    "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.ID)

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true
