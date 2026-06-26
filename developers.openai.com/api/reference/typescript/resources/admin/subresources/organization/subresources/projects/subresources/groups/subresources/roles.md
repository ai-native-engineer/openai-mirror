<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project group role assignments](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

client.admin.organization.projects.groups.roles.list(stringgroupID, RoleListParams { project\_id, after, limit, order } params, RequestOptionsoptions?): NextCursorPage<[RoleListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

client.admin.organization.projects.groups.roles.create(stringgroupID, RoleCreateParams { project\_id, role\_id } params, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

client.admin.organization.projects.groups.roles.retrieve(stringroleID, RoleRetrieveParams { project\_id, group\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

client.admin.organization.projects.groups.roles.delete(stringroleID, RoleDeleteParams { project\_id, group\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

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
