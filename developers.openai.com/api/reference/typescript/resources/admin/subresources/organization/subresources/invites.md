<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/list)

client.admin.organization.invites.list(InviteListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more } >

GET/organization/invites

##### [Create invite](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/create)

client.admin.organization.invites.create(InviteCreateParams { email, role, projects } body, RequestOptionsoptions?): [Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

POST/organization/invites

##### [Retrieve invite](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

client.admin.organization.invites.retrieve(stringinviteID, RequestOptionsoptions?): [Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/delete)

client.admin.organization.invites.delete(stringinviteID, RequestOptionsoptions?): [InviteDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

Invite { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: string

The email address of the individual to whom the invite was sent

object: "organization.invite"

The object type, which is always `organization.invite`

projects: Array<Project>

The projects that were granted membership upon acceptance of the invite.

id: string

Project’s public ID

role: "member" | "owner"

Project membership role

One of the following:

"member"

"owner"

role: "owner" | "reader"

`owner` or `reader`

One of the following:

"owner"

"reader"

status: "accepted" | "expired" | "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at?: number | null

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at?: number | null

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

InviteDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`
