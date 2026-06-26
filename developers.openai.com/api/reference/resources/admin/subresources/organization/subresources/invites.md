<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/list)

GET/organization/invites

##### [Create invite](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/create)

POST/organization/invites

##### [Retrieve invite](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/delete)

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

Invite object { id, created\_at, email, 6 more }

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

projects: array of object { id, role }

The projects that were granted membership upon acceptance of the invite.

id: string

Project’s public ID

role: "member" or "owner"

Project membership role

One of the following:

"member"

"owner"

role: "owner" or "reader"

`owner` or `reader`

One of the following:

"owner"

"reader"

status: "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at: optional number

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: optional number

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

InviteDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`
