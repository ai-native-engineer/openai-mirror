<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete group

client.Admin.Organization.Groups.Delete(ctx, groupID) (\*[AdminOrganizationGroupDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20AdminOrganizationGroupDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}

Deletes a group from the organization.

##### ParametersExpand Collapse

groupID string

##### ReturnsExpand Collapse

type AdminOrganizationGroupDeleteResponse struct{…}

Confirmation payload returned after deleting a group.

ID string

Identifier of the deleted group.

Deleted bool

Whether the group was deleted.

Object GroupDeleted

Always `group.deleted`.

### Delete group

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
  group, err := client.Admin.Organization.Groups.Delete(context.TODO(), "group_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", group.ID)

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

##### Returns Examples

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true
