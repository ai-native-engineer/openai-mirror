<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/ -->

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

# Groups

##### [List groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/list)

admin.organization.groups.list(\*\*kwargs) -> NextCursorPage<[Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more } >

GET/organization/groups

##### [Create group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/create)

admin.organization.groups.create(\*\*kwargs) -> [Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

POST/organization/groups

##### [Retrieve group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

admin.organization.groups.retrieve(group\_id) -> [Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/update)

admin.organization.groups.update(group\_id, \*\*kwargs) -> [GroupUpdateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)) { id, created\_at, is\_scim\_managed, name }

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/delete)

admin.organization.groups.delete(group\_id) -> [GroupDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

class Group { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: :group | :tenant\_group

The type of the group.

One of the following:

:group

:tenant\_group

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: String

Display name of the group.

class GroupUpdateResponse { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: String

Updated display name for the group.

class GroupDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a group.

id: String

Identifier of the deleted group.

deleted: bool

Whether the group was deleted.

object: :"group.deleted"

Always `group.deleted`.

#### GroupsUsers

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

#### GroupsRoles

##### [List group organization role assignments](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

admin.organization.groups.roles.list(group\_id, \*\*kwargs) -> NextCursorPage<[RoleListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

admin.organization.groups.roles.create(group\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.groups.roles.retrieve(role\_id, \*\*kwargs) -> [RoleRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

admin.organization.groups.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleListResponse { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: String

Identifier for the role.

assignment\_sources: Array[AssignmentSource{ principal\_id, principal\_type}]

Principals from which the role assignment is inherited, when available.

principal\_id: String

principal\_type: String

created\_at: Integer

When the role was created.

formatunixtime

created\_by: String

Identifier of the actor who created the role.

created\_by\_user\_obj: Hash[Symbol, untyped]

User details for the actor that created the role, when available.

description: String

Description of the role.

metadata: Hash[Symbol, untyped]

Arbitrary metadata stored on the role.

name: String

Name of the role.

permissions: Array[String]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: String

Resource type the role applies to.

updated\_at: Integer

When the role was last updated.

formatunixtime

class RoleCreateResponse { group, object, role }

Role assignment linking a group to a role.

group: Group{ id, created\_at, name, 2 more}

Summary information about a group returned in role assignment responses.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: String

Display name of the group.

object: :group

Always `group`.

scim\_managed: bool

Whether the group is managed through SCIM.

object: :"group.role"

Always `group.role`.

role: [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

class RoleRetrieveResponse { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: String

Identifier for the role.

assignment\_sources: Array[AssignmentSource{ principal\_id, principal\_type}]

Principals from which the role assignment is inherited, when available.

principal\_id: String

principal\_type: String

created\_at: Integer

When the role was created.

formatunixtime

created\_by: String

Identifier of the actor who created the role.

created\_by\_user\_obj: Hash[Symbol, untyped]

User details for the actor that created the role, when available.

description: String

Description of the role.

metadata: Hash[Symbol, untyped]

Arbitrary metadata stored on the role.

name: String

Name of the role.

permissions: Array[String]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: String

Resource type the role applies to.

updated\_at: Integer

When the role was last updated.

formatunixtime

class RoleDeleteResponse { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: String

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.
