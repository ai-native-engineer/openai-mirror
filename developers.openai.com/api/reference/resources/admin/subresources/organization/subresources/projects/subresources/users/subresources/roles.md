<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project user role assignments](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

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

RoleCreateResponse object { object, role, user }

Role assignment linking a user to a role.

object: "user.role"

Always `user.role`.

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

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
