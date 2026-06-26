<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/retrieve/ -->

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

# Retrieve invite

client.Admin.Organization.Invites.Get(ctx, inviteID) (\*[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)), error)

GET/organization/invites/{invite\_id}

Retrieves an invite.

##### ParametersExpand Collapse

inviteID string

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

### Retrieve invite

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
  invite, err := client.Admin.Organization.Invites.Get(context.TODO(), "invite_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", invite.ID)

    "object": "organization.invite",
    "id": "invite-abc",
    "email": "user@example.com",
    "role": "owner",
    "status": "accepted",
    "created_at": 1711471533,
    "expires_at": 1711471533,
    "accepted_at": 1711471533

##### Returns Examples

    "object": "organization.invite",
    "id": "invite-abc",
    "email": "user@example.com",
    "role": "owner",
    "status": "accepted",
    "created_at": 1711471533,
    "expires_at": 1711471533,
    "accepted_at": 1711471533
