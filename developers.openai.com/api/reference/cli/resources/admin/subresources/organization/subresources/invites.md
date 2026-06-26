<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/list)

$ openai admin:organization:invites list

GET/organization/invites

##### [Create invite](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/create)

$ openai admin:organization:invites create

POST/organization/invites

##### [Retrieve invite](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

$ openai admin:organization:invites retrieve

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/delete)

$ openai admin:organization:invites delete

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

invite: object { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the invite was sent.

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

"member"

"owner"

role: "owner" or "reader"

`owner` or `reader`

"owner"

"reader"

status: "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

"accepted"

"expired"

"pending"

accepted\_at: optional number

The Unix timestamp (in seconds) of when the invite was accepted.

expires\_at: optional number

The Unix timestamp (in seconds) of when the invite expires.
