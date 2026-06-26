<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Invites

##### [List invites](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/list)

admin.organization.invites.list(\*\*kwargs) -> ConversationCursorPage<[Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more } >

GET/organization/invites

##### [Create invite](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/create)

admin.organization.invites.create(\*\*kwargs) -> [Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

POST/organization/invites

##### [Retrieve invite](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

admin.organization.invites.retrieve(invite\_id) -> [Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/delete)

admin.organization.invites.delete(invite\_id) -> [InviteDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

class Invite { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: String

The email address of the individual to whom the invite was sent

object: :"organization.invite"

The object type, which is always `organization.invite`

projects: Array[Project{ id, role}]

The projects that were granted membership upon acceptance of the invite.

id: String

Project’s public ID

role: :member | :owner

Project membership role

One of the following:

:member

:owner

role: :owner | :reader

`owner` or `reader`

One of the following:

:owner

:reader

status: :accepted | :expired | :pending

`accepted`,`expired`, or `pending`

One of the following:

:accepted

:expired

:pending

accepted\_at: Integer

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

class InviteDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.invite.deleted"

The object type, which is always `organization.invite.deleted`
