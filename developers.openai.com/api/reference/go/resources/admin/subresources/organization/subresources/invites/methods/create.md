<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/create/ -->

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

# Create invite

client.Admin.Organization.Invites.New(ctx, body) (\*[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)), error)

POST/organization/invites

Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

##### ParametersExpand Collapse

body AdminOrganizationInviteNewParams

Email param.Field[string]

Send an email to this address

Role param.Field[[AdminOrganizationInviteNewParamsRole](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/create#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20role%20%3E%20(schema))]

`owner` or `reader`

const AdminOrganizationInviteNewParamsRoleReader [AdminOrganizationInviteNewParamsRole](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/create#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20role%20%3E%20(schema)) = "reader"

const AdminOrganizationInviteNewParamsRoleOwner [AdminOrganizationInviteNewParamsRole](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/create#(resource)%20admin.organization.invites%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20role%20%3E%20(schema)) = "owner"

Projects param.Field[[]AdminOrganizationInviteNewParamsProject]Optional

An array of projects to which membership is granted at the same time the org invite is accepted. If omitted, the user will be invited to the default project for compatibility with legacy behavior. If empty list is passed, the user will not be invited to any projects, including the default one.

ID string

Project’s public ID

Role string

Project membership role

One of the following:

const AdminOrganizationInviteNewParamsProjectRoleMember AdminOrganizationInviteNewParamsProjectRole = "member"

const AdminOrganizationInviteNewParamsProjectRoleOwner AdminOrganizationInviteNewParamsProjectRole = "owner"

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

### Create invite

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
  invite, err := client.Admin.Organization.Invites.New(context.TODO(), openai.AdminOrganizationInviteNewParams{
    Email: "email",
    Role: openai.AdminOrganizationInviteNewParamsRoleReader,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", invite.ID)

  "object": "organization.invite",
  "id": "invite-def",
  "email": "anotheruser@example.com",
  "role": "reader",
  "status": "pending",
  "created_at": 1711471533,
  "expires_at": 1711471533,
  "accepted_at": null,
  "projects": [
      "id": "project-xyz",
      "role": "member"
      "id": "project-abc",
      "role": "owner"
  ]

##### Returns Examples

  "object": "organization.invite",
  "id": "invite-def",
  "email": "anotheruser@example.com",
  "role": "reader",
  "status": "pending",
  "created_at": 1711471533,
  "expires_at": 1711471533,
  "accepted_at": null,
  "projects": [
      "id": "project-xyz",
      "role": "member"
      "id": "project-abc",
      "role": "owner"
  ]
