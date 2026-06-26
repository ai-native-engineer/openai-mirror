<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List project users](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

admin.organization.projects.users.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more } >

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

admin.organization.projects.users.create(project\_id, \*\*kwargs) -> [ProjectUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

admin.organization.projects.users.retrieve(user\_id, \*\*kwargs) -> [ProjectUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

admin.organization.projects.users.update(user\_id, \*\*kwargs) -> [ProjectUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

admin.organization.projects.users.delete(user\_id, \*\*kwargs) -> [UserDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

class ProjectUser { id, added\_at, object, 3 more }

Represents an individual user in a project.

id: String

The identifier, which can be referenced in API endpoints

added\_at: Integer

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

object: :"organization.project.user"

The object type, which is always `organization.project.user`

role: String

`owner` or `member`

email: String

The email address of the user

name: String

The name of the user

class UserDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.project.user.deleted"

#### UsersRoles

##### [List project user role assignments](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

admin.organization.projects.users.roles.list(user\_id, \*\*kwargs) -> NextCursorPage<[RoleListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

admin.organization.projects.users.roles.create(user\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

admin.organization.projects.users.roles.retrieve(role\_id, \*\*kwargs) -> [RoleRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

admin.organization.projects.users.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

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

class RoleCreateResponse { object, role, user }

Role assignment linking a user to a role.

object: :"user.role"

Always `user.role`.

role: [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

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
