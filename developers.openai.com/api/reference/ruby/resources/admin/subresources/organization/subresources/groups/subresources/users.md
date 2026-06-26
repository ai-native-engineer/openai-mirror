<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List group users](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

admin.organization.groups.users.list(group\_id, \*\*kwargs) -> NextCursorPage<[OrganizationGroupUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name } >

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

admin.organization.groups.users.create(group\_id, \*\*kwargs) -> [UserCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)) { group\_id, object, user\_id }

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

admin.organization.groups.users.retrieve(user\_id, \*\*kwargs) -> [UserRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)) { id, email, is\_service\_account, 3 more }

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

admin.organization.groups.users.delete(user\_id, \*\*kwargs) -> [UserDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationGroupUser { id, email, name }

Represents an individual user returned when inspecting group membership.

id: String

The identifier, which can be referenced in API endpoints

email: String

The email address of the user.

name: String

The name of the user.

class UserCreateResponse { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: String

Identifier of the group the user was added to.

object: :"group.user"

Always `group.user`.

user\_id: String

Identifier of the user that was added.

class UserRetrieveResponse { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: String

Identifier for the user.

email: String

Email address of the user, or `null` for users without an email.

is\_service\_account: bool

Whether the user is a service account.

name: String

Display name of the user.

picture: String

URL of the user’s profile picture, if available.

user\_type: :user | :tenant\_user

The type of user.

One of the following:

:user

:tenant\_user

class UserDeleteResponse { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: bool

Whether the group membership was removed.

object: :"group.user.deleted"

Always `group.user.deleted`.
