<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Roles](/api/reference/go/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

client.Admin.Organization.Roles.Delete(ctx, roleID) (\*[AdminOrganizationRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20AdminOrganizationRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### ParametersExpand Collapse

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationRoleDeleteResponse struct{…}

Confirmation payload returned after deleting a role.

ID string

Identifier of the deleted role.

Deleted bool

Whether the role was deleted.

Object RoleDeleted

Always `role.deleted`.

### Delete organization role

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
  role, err := client.Admin.Organization.Roles.Delete(context.TODO(), "role_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.ID)

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true
