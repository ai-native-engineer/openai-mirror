<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete user

client.Admin.Organization.Users.Delete(ctx, userID) (\*[AdminOrganizationUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20AdminOrganizationUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/users/{user\_id}

Deletes a user from the organization.

##### ParametersExpand Collapse

userID string

##### ReturnsExpand Collapse

type AdminOrganizationUserDeleteResponse struct{…}

ID string

Deleted bool

Object OrganizationUserDeleted

### Delete user

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
  user, err := client.Admin.Organization.Users.Delete(context.TODO(), "user_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", user.ID)

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true
