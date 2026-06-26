<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list/ -->

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

# List group users

client.Admin.Organization.Groups.Users.List(ctx, groupID, query) (\*NextCursorPage[[OrganizationGroupUser](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))], error)

GET/organization/groups/{group\_id}/users

Lists the users assigned to a group.

##### ParametersExpand Collapse

groupID string

query AdminOrganizationGroupUserListParams

After param.Field[string]Optional

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

Limit param.Field[int64]Optional

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

Order param.Field[[AdminOrganizationGroupUserListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Specifies the sort order of users in the list.

const AdminOrganizationGroupUserListParamsOrderAsc [AdminOrganizationGroupUserListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationGroupUserListParamsOrderDesc [AdminOrganizationGroupUserListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type OrganizationGroupUser struct{…}

Represents an individual user returned when inspecting group membership.

ID string

The identifier, which can be referenced in API endpoints

Email string

The email address of the user.

Name string

The name of the user.

### List group users

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
  page, err := client.Admin.Organization.Groups.Users.List(
    context.TODO(),
    "group_id",
    openai.AdminOrganizationGroupUserListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null
