<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/list)

client.Admin.Organization.Invites.List(ctx, query) (\*ConversationCursorPage[[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))], error)

GET/organization/invites

##### [Create invite](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/create)

client.Admin.Organization.Invites.New(ctx, body) (\*[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)), error)

POST/organization/invites

##### [Retrieve invite](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

client.Admin.Organization.Invites.Get(ctx, inviteID) (\*[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)), error)

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/delete)

client.Admin.Organization.Invites.Delete(ctx, inviteID) (\*[AdminOrganizationInviteDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20AdminOrganizationInviteDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

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
