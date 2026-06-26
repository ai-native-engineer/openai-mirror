<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign organization role from group

client.Admin.Organization.Groups.Roles.Delete(ctx, groupID, roleID) (\*[AdminOrganizationGroupRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}/roles/{role\_id}

Unassigns an organization role from a group within the organization.

##### ParametersExpand Collapse

groupID string

roleID string

##### ReturnsExpand Collapse

type AdminOrganizationGroupRoleDeleteResponse struct{…}

Confirmation payload returned after unassigning a role.

Deleted bool

Whether the assignment was removed.

Object string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from group

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
  role, err := client.Admin.Organization.Groups.Roles.Delete(
    context.TODO(),
    "group_id",
    "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.Deleted)

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true
