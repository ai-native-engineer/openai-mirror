<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List group users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

OrganizationGroupUser object { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string

The email address of the user.

name: string

The name of the user.

UserCreateResponse object { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

UserRetrieveResponse object { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: string

Identifier for the user.

email: string

Email address of the user, or `null` for users without an email.

is\_service\_account: boolean

Whether the user is a service account.

name: string

Display name of the user.

picture: string

URL of the user’s profile picture, if available.

user\_type: "user" or "tenant\_user"

The type of user.

One of the following:

"user"

"tenant\_user"

UserDeleteResponse object { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: boolean

Whether the group membership was removed.

object: "group.user.deleted"

Always `group.user.deleted`.
