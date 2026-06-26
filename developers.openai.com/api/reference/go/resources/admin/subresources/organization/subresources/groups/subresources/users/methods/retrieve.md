<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve/ -->

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

# Retrieve group user

client.Admin.Organization.Groups.Users.Get(ctx, groupID, userID) (\*[AdminOrganizationGroupUserGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserGetResponse%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}/users/{user\_id}

Retrieves a user in a group.

##### ParametersExpand Collapse

groupID string

userID string

##### ReturnsExpand Collapse

type AdminOrganizationGroupUserGetResponse struct{…}

Details about a user returned from an organization group membership lookup.

ID string

Identifier for the user.

Email string

Email address of the user, or `null` for users without an email.

IsServiceAccount bool

Whether the user is a service account.

Name string

Display name of the user.

Picture string

URL of the user’s profile picture, if available.

UserType AdminOrganizationGroupUserGetResponseUserType

The type of user.

One of the following:

const AdminOrganizationGroupUserGetResponseUserTypeUser AdminOrganizationGroupUserGetResponseUserType = "user"

const AdminOrganizationGroupUserGetResponseUserTypeTenantUser AdminOrganizationGroupUserGetResponseUserType = "tenant\_user"

### Retrieve group user

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
  user, err := client.Admin.Organization.Groups.Users.Get(
    context.TODO(),
    "group_id",
    "user_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", user.ID)

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

##### Returns Examples

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"
