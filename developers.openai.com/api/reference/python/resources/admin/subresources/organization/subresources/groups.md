<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/ -->

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

# Groups

##### [List groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/list)

admin.organization.groups.list(GroupListParams\*\*kwargs)  -> SyncNextCursorPage[[Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))]

GET/organization/groups

##### [Create group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/create)

admin.organization.groups.create(GroupCreateParams\*\*kwargs)  -> [Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

POST/organization/groups

##### [Retrieve group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

admin.organization.groups.retrieve(strgroup\_id)  -> [Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/update)

admin.organization.groups.update(strgroup\_id, GroupUpdateParams\*\*kwargs)  -> [GroupUpdateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema))

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/delete)

admin.organization.groups.delete(strgroup\_id)  -> [GroupDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

class Group: …

Details about an organization group.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: Literal["group", "tenant\_group"]

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: str

Display name of the group.

class GroupUpdateResponse: …

Response returned after updating a group.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: str

Updated display name for the group.

class GroupDeleteResponse: …

Confirmation payload returned after deleting a group.

id: str

Identifier of the deleted group.

deleted: bool

Whether the group was deleted.

object: Literal["group.deleted"]

Always `group.deleted`.

#### GroupsUsers

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

#### GroupsRoles

##### [List group organization role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

admin.organization.groups.roles.list(strgroup\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

admin.organization.groups.roles.create(strgroup\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.groups.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

admin.organization.groups.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleListResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleCreateResponse: …

Role assignment linking a group to a role.

group: Group

Summary information about a group returned in role assignment responses.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: str

Display name of the group.

object: Literal["group"]

Always `group`.

scim\_managed: bool

Whether the group is managed through SCIM.

object: Literal["group.role"]

Always `group.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

class RoleRetrieveResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleDeleteResponse: …

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: str

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.
