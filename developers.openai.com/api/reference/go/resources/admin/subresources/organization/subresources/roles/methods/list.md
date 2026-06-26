<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/list/ -->

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

# List organization roles

client.Admin.Organization.Roles.List(ctx, query) (\*NextCursorPage[[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))], error)

GET/organization/roles

Lists the roles configured for the organization.

##### ParametersExpand Collapse

query AdminOrganizationRoleListParams

After param.Field[string]Optional

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing roles.

Limit param.Field[int64]Optional

A limit on the number of roles to return. Defaults to 1000.

minimum0

maximum1000

Order param.Field[[AdminOrganizationRoleListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/list#(resource)%20admin.organization.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order for the returned roles.

const AdminOrganizationRoleListParamsOrderAsc [AdminOrganizationRoleListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/list#(resource)%20admin.organization.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationRoleListParamsOrderDesc [AdminOrganizationRoleListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/list#(resource)%20admin.organization.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type Role struct{…}

Details about a role that can be assigned through the public Roles API.

ID string

Identifier for the role.

Description string

Optional description of the role.

Name string

Unique name for the role.

Object Role

Always `role`.

Permissions []string

Permissions granted by the role.

PredefinedRole bool

Whether the role is predefined and managed by OpenAI.

ResourceType string

Resource type the role is bound to (for example `api.organization` or `api.project`).

### List organization roles

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
  page, err := client.Admin.Organization.Roles.List(context.TODO(), openai.AdminOrganizationRoleListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "object": "role",
            "id": "role_01J1F8ROLE01",
            "name": "API Group Manager",
            "description": "Allows managing organization groups",
            "permissions": [
                "api.groups.read",
                "api.groups.write"
            ],
            "resource_type": "api.organization",
            "predefined_role": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "role",
            "id": "role_01J1F8ROLE01",
            "name": "API Group Manager",
            "description": "Allows managing organization groups",
            "permissions": [
                "api.groups.read",
                "api.groups.write"
            ],
            "resource_type": "api.organization",
            "predefined_role": false
    ],
    "has_more": false,
    "next": null
