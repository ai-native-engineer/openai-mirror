<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete/ -->

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

# Unassign organization role from user

client.Admin.Organization.Users.Roles.Delete(ctx, userID, roleID) (\*[AdminOrganizationUserRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/users/{user\_id}/roles/{role\_id}

Unassigns an organization role from a user within the organization.

##### ParametersExpand Collapse

userID string

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationUserRoleDeleteResponse struct{…}

Confirmation payload returned after unassigning a role.

Deleted bool

Whether the assignment was removed.

Object string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from user

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
  role, err := client.Admin.Organization.Users.Roles.Delete(
    context.TODO(),
    "user_id",
    "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.Deleted)

    "object": "user.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "user.role.deleted",
    "deleted": true
