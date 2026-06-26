<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/retrieve/ -->

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

# Retrieve group

client.Admin.Organization.Groups.Get(ctx, groupID) (\*[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}

Retrieves a group.

##### ParametersExpand Collapse

groupID string

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

### Retrieve group

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
  group, err := client.Admin.Organization.Groups.Get(context.TODO(), "group_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", group.ID)

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"
