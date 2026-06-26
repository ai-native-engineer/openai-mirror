<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Users](/api/reference/typescript/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List user organization role assignments](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

client.admin.organization.users.roles.list(stringuserID, RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[RoleListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

client.admin.organization.users.roles.create(stringuserID, RoleCreateParams { role\_id } body, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

client.admin.organization.users.roles.retrieve(stringroleID, RoleRetrieveParams { user\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

client.admin.organization.users.roles.delete(stringroleID, RoleDeleteParams { user\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/users/{user\_id}/roles/{role\_id}

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

RoleCreateResponse { object, role, user }

Role assignment linking a user to a role.

object: "user.role"

Always `user.role`.

role: [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

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
