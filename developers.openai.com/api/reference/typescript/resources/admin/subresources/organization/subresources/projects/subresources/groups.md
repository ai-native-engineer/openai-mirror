<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Groups

##### [List project groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

client.admin.organization.projects.groups.list(stringprojectID, GroupListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[ProjectGroup](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more } >

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

client.admin.organization.projects.groups.create(stringprojectID, GroupCreateParams { group\_id, role } body, RequestOptionsoptions?): [ProjectGroup](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

client.admin.organization.projects.groups.retrieve(stringgroupID, GroupRetrieveParams { project\_id, group\_type } params, RequestOptionsoptions?): [ProjectGroup](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

client.admin.organization.projects.groups.delete(stringgroupID, GroupDeleteParams { project\_id } params, RequestOptionsoptions?): [GroupDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

ProjectGroup { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" | "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

GroupDeleteResponse { deleted, object }

Confirmation payload returned after removing a group from a project.

deleted: boolean

Whether the group membership in the project was removed.

object: "project.group.deleted"

Always `project.group.deleted`.

#### GroupsRoles

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
