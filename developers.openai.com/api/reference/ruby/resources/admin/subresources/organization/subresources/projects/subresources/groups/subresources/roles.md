<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project group role assignments](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

admin.organization.projects.groups.roles.list(group\_id, \*\*kwargs) -> NextCursorPage<[RoleListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

admin.organization.projects.groups.roles.create(group\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.projects.groups.roles.retrieve(role\_id, \*\*kwargs) -> [RoleRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

admin.organization.projects.groups.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

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
