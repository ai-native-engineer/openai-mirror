<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Invites](/api/reference/go/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete invite

client.Admin.Organization.Invites.Delete(ctx, inviteID) (\*[AdminOrganizationInviteDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20AdminOrganizationInviteDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/invites/{invite\_id}

Delete an invite. If the invite has already been accepted, it cannot be deleted.

##### ParametersExpand Collapse

inviteID string

##### ReturnsExpand Collapse

type AdminOrganizationInviteDeleteResponse struct{…}

ID string

Deleted bool

Object OrganizationInviteDeleted

The object type, which is always `organization.invite.deleted`

### Delete invite

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
  invite, err := client.Admin.Organization.Invites.Delete(context.TODO(), "invite_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", invite.ID)

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true

##### Returns Examples

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true
