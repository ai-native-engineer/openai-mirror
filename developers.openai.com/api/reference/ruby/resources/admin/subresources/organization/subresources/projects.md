<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/ -->

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

# Projects

##### [List projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/list)

admin.organization.projects.list(\*\*kwargs) -> ConversationCursorPage<[Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more } >

GET/organization/projects

##### [Create project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/create)

admin.organization.projects.create(\*\*kwargs) -> [Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects

##### [Retrieve project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

admin.organization.projects.retrieve(project\_id) -> [Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/update)

admin.organization.projects.update(project\_id, \*\*kwargs) -> [Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/archive)

admin.organization.projects.archive(project\_id) -> [Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

class Project { id, created\_at, object, 4 more }

Represents an individual project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: :"organization.project"

The object type, which is always `organization.project`

archived\_at: Integer

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id: String

The external key associated with the project.

name: String

The name of the project. This appears in reporting.

status: String

`active` or `archived`

#### ProjectsUsers

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

#### ProjectsUsersRoles

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

#### ProjectsService Accounts

##### [List project service accounts](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

admin.organization.projects.service\_accounts.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectServiceAccount](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more } >

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

admin.organization.projects.service\_accounts.create(project\_id, \*\*kwargs) -> [ServiceAccountCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)) { id, api\_key, created\_at, 3 more }

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

admin.organization.projects.service\_accounts.retrieve(service\_account\_id, \*\*kwargs) -> [ProjectServiceAccount](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

admin.organization.projects.service\_accounts.update(service\_account\_id, \*\*kwargs) -> [ProjectServiceAccount](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

admin.organization.projects.service\_accounts.delete(service\_account\_id, \*\*kwargs) -> [ServiceAccountDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

class ProjectServiceAccount { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: String

The name of the service account

object: :"organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: :owner | :member

`owner` or `member`

One of the following:

:owner

:member

class ServiceAccountCreateResponse { id, api\_key, created\_at, 3 more }

id: String

api\_key: APIKey{ id, created\_at, name, 2 more}

id: String

created\_at: Integer

formatunixtime

name: String

object: :"organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: String

created\_at: Integer

formatunixtime

name: String

object: :"organization.project.service\_account"

role: :member

Service accounts can only have one role of type `member`

class ServiceAccountDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.project.service\_account.deleted"

#### ProjectsAPI Keys

##### [List project API keys](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

admin.organization.projects.api\_keys.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more } >

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

admin.organization.projects.api\_keys.retrieve(api\_key\_id, \*\*kwargs) -> [ProjectAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more }

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

admin.organization.projects.api\_keys.delete(api\_key\_id, \*\*kwargs) -> [APIKeyDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

class ProjectAPIKey { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: Integer

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: String

The name of the API key

object: :"organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: Owner{ service\_account, type, user}

service\_account: ServiceAccount{ id, created\_at, name, role}

The service account that owns a project API key.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: String

The name of the service account.

role: String

The service account’s project role.

type: :user | :service\_account

`user` or `service_account`

One of the following:

:user

:service\_account

user: User{ id, created\_at, email, 2 more}

The user that owns a project API key.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: String

The email address of the user.

name: String

The name of the user.

role: String

The user’s project role.

redacted\_value: String

The redacted value of the API key

class APIKeyDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.project.api\_key.deleted"

#### ProjectsRate Limits

##### [List project rate limits](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

admin.organization.projects.rate\_limits.list\_rate\_limits(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectRateLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more } >

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

admin.organization.projects.rate\_limits.update\_rate\_limit(rate\_limit\_id, \*\*kwargs) -> [ProjectRateLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

class ProjectRateLimit { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

Represents a project rate limit config.

id: String

The identifier, which can be referenced in API endpoints.

max\_requests\_per\_1\_minute: Integer

The maximum requests per minute.

max\_tokens\_per\_1\_minute: Integer

The maximum tokens per minute.

model: String

The model this rate limit applies to.

object: :"project.rate\_limit"

The object type, which is always `project.rate_limit`

batch\_1\_day\_max\_input\_tokens: Integer

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute: Integer

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute: Integer

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day: Integer

The maximum requests per day. Only present for relevant models.

#### ProjectsModel Permissions

##### [Retrieve project model permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

admin.organization.projects.model\_permissions.retrieve(project\_id) -> [ProjectModelPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

admin.organization.projects.model\_permissions.update(project\_id, \*\*kwargs) -> [ProjectModelPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

admin.organization.projects.model\_permissions.delete(project\_id) -> [ProjectModelPermissionsDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

class ProjectModelPermissions { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: :allow\_list | :deny\_list

Whether the project uses an allowlist or a denylist.

One of the following:

:allow\_list

:deny\_list

model\_ids: Array[String]

The model IDs included in the model permissions policy.

object: :"project.model\_permissions"

The object type, which is always `project.model_permissions`.

class ProjectModelPermissionsDeleted { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: bool

Whether the project model permissions were deleted.

object: :"project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

#### ProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

admin.organization.projects.hosted\_tool\_permissions.retrieve(project\_id) -> [ProjectHostedToolPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

admin.organization.projects.hosted\_tool\_permissions.update(project\_id, \*\*kwargs) -> [ProjectHostedToolPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

class ProjectHostedToolPermissions { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

file\_search: FileSearch{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

mcp: Mcp{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

web\_search: WebSearch{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

#### ProjectsGroups

##### [List project groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

admin.organization.projects.groups.list(project\_id, \*\*kwargs) -> NextCursorPage<[ProjectGroup](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more } >

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

admin.organization.projects.groups.create(project\_id, \*\*kwargs) -> [ProjectGroup](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

admin.organization.projects.groups.retrieve(group\_id, \*\*kwargs) -> [ProjectGroup](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) { created\_at, group\_id, group\_name, 3 more }

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

admin.organization.projects.groups.delete(group\_id, \*\*kwargs) -> [GroupDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

class ProjectGroup { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: Integer

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: String

Identifier of the group that has access to the project.

group\_name: String

Display name of the group.

group\_type: :group | :tenant\_group

The type of the group.

One of the following:

:group

:tenant\_group

object: :"project.group"

Always `project.group`.

project\_id: String

Identifier of the project.

class GroupDeleteResponse { deleted, object }

Confirmation payload returned after removing a group from a project.

deleted: bool

Whether the group membership in the project was removed.

object: :"project.group.deleted"

Always `project.group.deleted`.

#### ProjectsGroupsRoles

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

#### ProjectsRoles

##### [List project roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

admin.organization.projects.roles.list(project\_id, \*\*kwargs) -> NextCursorPage<[Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

admin.organization.projects.roles.create(project\_id, \*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

admin.organization.projects.roles.retrieve(role\_id, \*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

admin.organization.projects.roles.update(role\_id, \*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

admin.organization.projects.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/projects/{project\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: String

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: :"role.deleted"

Always `role.deleted`.

#### ProjectsData Retention

##### [Retrieve project data retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

admin.organization.projects.data\_retention.retrieve(project\_id) -> [ProjectDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

admin.organization.projects.data\_retention.update(project\_id, \*\*kwargs) -> [ProjectDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

class ProjectDataRetention { object, type }

Represents a project’s data retention control setting.

object: :"project.data\_retention"

The object type, which is always `project.data_retention`.

type: :organization\_default | :none | :zero\_data\_retention | 3 more

The configured project data retention type.

One of the following:

:organization\_default

:none

:zero\_data\_retention

:modified\_abuse\_monitoring

:enhanced\_zero\_data\_retention

:enhanced\_modified\_abuse\_monitoring

#### ProjectsSpend Alerts

##### [List project spend alerts](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

admin.organization.projects.spend\_alerts.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

admin.organization.projects.spend\_alerts.create(project\_id, \*\*kwargs) -> [ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

admin.organization.projects.spend\_alerts.retrieve(alert\_id, \*\*kwargs) -> [ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

admin.organization.projects.spend\_alerts.update(alert\_id, \*\*kwargs) -> [ProjectSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

admin.organization.projects.spend\_alerts.delete(alert\_id, \*\*kwargs) -> [ProjectSpendAlertDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class ProjectSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: String

The identifier, which can be referenced in API endpoints.

currency: :USD

The currency for the threshold amount.

interval: :month

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel{ recipients, type, subject\_prefix}

Email notification settings for a spend alert.

recipients: Array[String]

Email addresses that receive the spend alert notification.

type: :email

The notification channel type. Currently only `email` is supported.

subject\_prefix: String

Optional subject prefix for alert emails.

object: :"project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: Integer

The alert threshold amount, in cents.

class ProjectSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: String

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: :"project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

#### ProjectsCertificates

##### [List project certificates](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

admin.organization.projects.certificates.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[CertificateListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

admin.organization.projects.certificates.activate(project\_id, \*\*kwargs) -> Page<[CertificateActivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

admin.organization.projects.certificates.deactivate(project\_id, \*\*kwargs) -> Page<[CertificateDeactivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/deactivate

##### ModelsExpand Collapse

class CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.

class CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.

class CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.
