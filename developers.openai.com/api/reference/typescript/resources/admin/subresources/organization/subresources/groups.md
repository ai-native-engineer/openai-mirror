<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/ -->

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

# Groups

##### [List groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/list)

client.admin.organization.groups.list(GroupListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more } >

GET/organization/groups

##### [Create group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/create)

client.admin.organization.groups.create(GroupCreateParams { name } body, RequestOptionsoptions?): [Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

POST/organization/groups

##### [Retrieve group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

client.admin.organization.groups.retrieve(stringgroupID, RequestOptionsoptions?): [Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/update)

client.admin.organization.groups.update(stringgroupID, GroupUpdateParams { name } body, RequestOptionsoptions?): [GroupUpdateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)) { id, created\_at, is\_scim\_managed, name }

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/delete)

client.admin.organization.groups.delete(stringgroupID, RequestOptionsoptions?): [GroupDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

Group { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: "group" | "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

GroupUpdateResponse { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Updated display name for the group.

GroupDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a group.

id: string

Identifier of the deleted group.

deleted: boolean

Whether the group was deleted.

object: "group.deleted"

Always `group.deleted`.

#### GroupsUsers

##### [List group users](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

client.admin.organization.groups.users.list(stringgroupID, UserListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[OrganizationGroupUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name } >

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

client.admin.organization.groups.users.create(stringgroupID, UserCreateParams { user\_id } body, RequestOptionsoptions?): [UserCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)) { group\_id, object, user\_id }

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

client.admin.organization.groups.users.retrieve(stringuserID, UserRetrieveParams { group\_id } params, RequestOptionsoptions?): [UserRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)) { id, email, is\_service\_account, 3 more }

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

client.admin.organization.groups.users.delete(stringuserID, UserDeleteParams { group\_id } params, RequestOptionsoptions?): [UserDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

OrganizationGroupUser { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string | null

The email address of the user.

name: string

The name of the user.

UserCreateResponse { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

UserRetrieveResponse { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: string

Identifier for the user.

email: string | null

Email address of the user, or `null` for users without an email.

is\_service\_account: boolean | null

Whether the user is a service account.

name: string

Display name of the user.

picture: string | null

URL of the user’s profile picture, if available.

user\_type: "user" | "tenant\_user"

The type of user.

One of the following:

"user"

"tenant\_user"

UserDeleteResponse { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: boolean

Whether the group membership was removed.

object: "group.user.deleted"

Always `group.user.deleted`.

#### GroupsRoles

##### [List group organization role assignments](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

client.admin.organization.groups.roles.list(stringgroupID, RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[RoleListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

client.admin.organization.groups.roles.create(stringgroupID, RoleCreateParams { role\_id } body, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

client.admin.organization.groups.roles.retrieve(stringroleID, RoleRetrieveParams { group\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

client.admin.organization.groups.roles.delete(stringroleID, RoleDeleteParams { group\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: Array<AssignmentSource> | null

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number | null

When the role was created.

formatunixtime

created\_by: string | null

Identifier of the actor who created the role.

created\_by\_user\_obj: Record<string, unknown> | null

User details for the actor that created the role, when available.

description: string | null

Description of the role.

metadata: Record<string, unknown> | null

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: Array<string>

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number | null

When the role was last updated.

formatunixtime

RoleCreateResponse { group, object, role }

Role assignment linking a group to a role.

group: Group { id, created\_at, name, 2 more }

Summary information about a group returned in role assignment responses.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: string

Display name of the group.

object: "group"

Always `group`.

scim\_managed: boolean

Whether the group is managed through SCIM.

object: "group.role"

Always `group.role`.

role: [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

RoleRetrieveResponse { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: Array<AssignmentSource> | null

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number | null

When the role was created.

formatunixtime

created\_by: string | null

Identifier of the actor who created the role.

created\_by\_user\_obj: Record<string, unknown> | null

User details for the actor that created the role, when available.

description: string | null

Description of the role.

metadata: Record<string, unknown> | null

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: Array<string>

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number | null

When the role was last updated.

formatunixtime

RoleDeleteResponse { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.
