<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add group user

client.Admin.Organization.Groups.Users.New(ctx, groupID, body) (\*[AdminOrganizationGroupUserNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserNewResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### ParametersExpand Collapse

groupID string

body AdminOrganizationGroupUserNewParams

UserID param.Field[string]

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

type AdminOrganizationGroupUserNewResponse struct{…}

Confirmation payload returned after adding a user to a group.

GroupID string

Identifier of the group the user was added to.

Object GroupUser

Always `group.user`.

UserID string

Identifier of the user that was added.

### Add group user

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
  user, err := client.Admin.Organization.Groups.Users.New(
    context.TODO(),
    "group_id",
    openai.AdminOrganizationGroupUserNewParams{
      UserID: "user_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", user.GroupID)

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
