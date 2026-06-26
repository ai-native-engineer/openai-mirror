<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/list/ -->

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

# List groups

client.Admin.Organization.Groups.List(ctx, query) (\*NextCursorPage[[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))], error)

GET/organization/groups

Lists all groups in the organization.

##### ParametersExpand Collapse

query AdminOrganizationGroupListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group\_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

Limit param.Field[int64]Optional

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

Order param.Field[[AdminOrganizationGroupListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/list#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Specifies the sort order of the returned groups.

const AdminOrganizationGroupListParamsOrderAsc [AdminOrganizationGroupListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/list#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationGroupListParamsOrderDesc [AdminOrganizationGroupListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/list#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type Group struct{…}

Details about an organization group.

ID string

Identifier for the group.

CreatedAt int64

Unix timestamp (in seconds) when the group was created.

formatunixtime

GroupType GroupGroupType

The type of the group.

One of the following:

const GroupGroupTypeGroup GroupGroupType = "group"

const GroupGroupTypeTenantGroup GroupGroupType = "tenant\_group"

IsScimManaged bool

Whether the group is managed through SCIM and controlled by your identity provider.

Name string

Display name of the group.

### List groups

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
  page, err := client.Admin.Organization.Groups.List(context.TODO(), openai.AdminOrganizationGroupListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null
