<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/list/ -->

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

# List invites

client.Admin.Organization.Invites.List(ctx, query) (\*ConversationCursorPage[[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))], error)

GET/organization/invites

Returns a list of invites in the organization.

##### ParametersExpand Collapse

query AdminOrganizationInviteListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

type Invite struct{…}

Represents an individual `invite` to the organization.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

Email string

The email address of the individual to whom the invite was sent

Object OrganizationInvite

The object type, which is always `organization.invite`

Projects []InviteProject

The projects that were granted membership upon acceptance of the invite.

ID string

Project’s public ID

Role string

Project membership role

One of the following:

const InviteProjectRoleMember InviteProjectRole = "member"

const InviteProjectRoleOwner InviteProjectRole = "owner"

Role InviteRole

`owner` or `reader`

One of the following:

const InviteRoleOwner InviteRole = "owner"

const InviteRoleReader InviteRole = "reader"

Status InviteStatus

`accepted`,`expired`, or `pending`

One of the following:

const InviteStatusAccepted InviteStatus = "accepted"

const InviteStatusExpired InviteStatus = "expired"

const InviteStatusPending InviteStatus = "pending"

AcceptedAt int64Optional

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

ExpiresAt int64Optional

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

### List invites

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
  page, err := client.Admin.Organization.Invites.List(context.TODO(), openai.AdminOrganizationInviteListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "object": "organization.invite",
      "id": "invite-abc",
      "email": "user@example.com",
      "role": "owner",
      "status": "accepted",
      "created_at": 1711471533,
      "expires_at": 1711471533,
      "accepted_at": 1711471533
  ],
  "first_id": "invite-abc",
  "last_id": "invite-abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.invite",
      "id": "invite-abc",
      "email": "user@example.com",
      "role": "owner",
      "status": "accepted",
      "created_at": 1711471533,
      "expires_at": 1711471533,
      "accepted_at": 1711471533
  ],
  "first_id": "invite-abc",
  "last_id": "invite-abc",
  "has_more": false
