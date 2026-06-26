<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create/ -->

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

# Assign organization role to group

client.Admin.Organization.Groups.Roles.New(ctx, groupID, body) (\*[AdminOrganizationGroupRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleNewResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}/roles

Assigns an organization role to a group within the organization.

##### ParametersExpand Collapse

groupID string

body AdminOrganizationGroupRoleNewParams

RoleID param.Field[string]

Identifier of the role to assign.

##### ReturnsExpand Collapse

type AdminOrganizationGroupRoleNewResponse struct{…}

Role assignment linking a group to a role.

Group AdminOrganizationGroupRoleNewResponseGroup

Summary information about a group returned in role assignment responses.

ID string

Identifier for the group.

CreatedAt int64

Unix timestamp (in seconds) when the group was created.

formatunixtime

Name string

Display name of the group.

Object Group

Always `group`.

ScimManaged bool

Whether the group is managed through SCIM.

Object GroupRole

Always `group.role`.

Role [Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

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

### Assign organization role to group

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
  role, err := client.Admin.Organization.Groups.Roles.New(
    context.TODO(),
    "group_id",
    openai.AdminOrganizationGroupRoleNewParams{
      RoleID: "role_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", role.Group)

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
    "role": {
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

##### Returns Examples

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
    "role": {
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
