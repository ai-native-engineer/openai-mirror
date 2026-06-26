<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/list)

admin.organization.invites.list(InviteListParams\*\*kwargs)  -> SyncConversationCursorPage[[Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))]

GET/organization/invites

##### [Create invite](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/create)

admin.organization.invites.create(InviteCreateParams\*\*kwargs)  -> [Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))

POST/organization/invites

##### [Retrieve invite](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

admin.organization.invites.retrieve(strinvite\_id)  -> [Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/delete)

admin.organization.invites.delete(strinvite\_id)  -> [InviteDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema))

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

class Invite: …

Represents an individual `invite` to the organization.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: str

The email address of the individual to whom the invite was sent

object: Literal["organization.invite"]

The object type, which is always `organization.invite`

projects: List[Project]

The projects that were granted membership upon acceptance of the invite.

id: str

Project’s public ID

role: Literal["member", "owner"]

Project membership role

One of the following:

"member"

"owner"

role: Literal["owner", "reader"]

`owner` or `reader`

One of the following:

"owner"

"reader"

status: Literal["accepted", "expired", "pending"]

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at: Optional[int]

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

class InviteDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.invite.deleted"]

The object type, which is always `organization.invite.deleted`
