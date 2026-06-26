<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/groups/ -->

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

# Groups

##### [List groups](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/list)

GET/organization/groups

##### [Create group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/create)

POST/organization/groups

##### [Retrieve group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/update)

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/delete)

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

Group object { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: "group" or "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

GroupUpdateResponse object { id, created\_at, is\_scim\_managed, name }

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

GroupDeleteResponse object { id, deleted, object }

Confirmation payload returned after deleting a group.

id: string

Identifier of the deleted group.

deleted: boolean

Whether the group was deleted.

object: "group.deleted"

Always `group.deleted`.

#### GroupsUsers

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

#### GroupsRoles

##### [List group organization role assignments](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

DELETE/organization/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleCreateResponse object { group, object, role }

Role assignment linking a group to a role.

group: object { id, created\_at, name, 2 more }

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

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

RoleRetrieveResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleDeleteResponse object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.
