<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List group users](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

admin.organization.groups.users.list(strgroup\_id, UserListParams\*\*kwargs)  -> SyncNextCursorPage[[OrganizationGroupUser](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))]

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

admin.organization.groups.users.create(strgroup\_id, UserCreateParams\*\*kwargs)  -> [UserCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema))

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

admin.organization.groups.users.retrieve(struser\_id, UserRetrieveParams\*\*kwargs)  -> [UserRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema))

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

admin.organization.groups.users.delete(struser\_id, UserDeleteParams\*\*kwargs)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationGroupUser: …

Represents an individual user returned when inspecting group membership.

id: str

The identifier, which can be referenced in API endpoints

email: Optional[str]

The email address of the user.

name: str

The name of the user.

class UserCreateResponse: …

Confirmation payload returned after adding a user to a group.

group\_id: str

Identifier of the group the user was added to.

object: Literal["group.user"]

Always `group.user`.

user\_id: str

Identifier of the user that was added.

class UserRetrieveResponse: …

Details about a user returned from an organization group membership lookup.

id: str

Identifier for the user.

email: Optional[str]

Email address of the user, or `null` for users without an email.

is\_service\_account: Optional[bool]

Whether the user is a service account.

name: str

Display name of the user.

picture: Optional[str]

URL of the user’s profile picture, if available.

user\_type: Literal["user", "tenant\_user"]

The type of user.

One of the following:

"user"

"tenant\_user"

class UserDeleteResponse: …

Confirmation payload returned after removing a user from a group.

deleted: bool

Whether the group membership was removed.

object: Literal["group.user.deleted"]

Always `group.user.deleted`.
