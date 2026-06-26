<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/update/ -->

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

# Update group

client.Admin.Organization.Groups.Update(ctx, groupID, body) (\*[AdminOrganizationGroupUpdateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20AdminOrganizationGroupUpdateResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}

Updates a group’s information.

##### ParametersExpand Collapse

groupID string

body AdminOrganizationGroupUpdateParams

Name param.Field[string]

New display name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

type AdminOrganizationGroupUpdateResponse struct{…}

Response returned after updating a group.

ID string

Identifier for the group.

CreatedAt int64

Unix timestamp (in seconds) when the group was created.

formatunixtime

IsScimManaged bool

Whether the group is managed through SCIM and controlled by your identity provider.

Name string

Updated display name for the group.

### Update group

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
  group, err := client.Admin.Organization.Groups.Update(
    context.TODO(),
    "group_id",
    openai.AdminOrganizationGroupUpdateParams{
      Name: "x",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", group.ID)

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false
