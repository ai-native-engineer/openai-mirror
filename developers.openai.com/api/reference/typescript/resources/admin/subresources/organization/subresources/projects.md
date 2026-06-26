<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/ -->

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

# Projects

##### [List projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/methods/list)

client.admin.organization.projects.list(ProjectListParams { after, include\_archived, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[Project](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more } >

GET/organization/projects

##### [Create project](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/methods/create)

client.admin.organization.projects.create(ProjectCreateParams { name, external\_key\_id, geography } body, RequestOptionsoptions?): [Project](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects

##### [Retrieve project](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

client.admin.organization.projects.retrieve(stringprojectID, RequestOptionsoptions?): [Project](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/methods/update)

client.admin.organization.projects.update(stringprojectID, ProjectUpdateParams { external\_key\_id, geography, name } body, RequestOptionsoptions?): [Project](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/methods/archive)

client.admin.organization.projects.archive(stringprojectID, RequestOptionsoptions?): [Project](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

Project { id, created\_at, object, 4 more }

Represents an individual project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: "organization.project"

The object type, which is always `organization.project`

archived\_at?: number | null

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id?: string | null

The external key associated with the project.

name?: string | null

The name of the project. This appears in reporting.

status?: string | null

`active` or `archived`

#### ProjectsUsers

##### [List project users](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

client.admin.organization.projects.users.list(stringprojectID, UserListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more } >

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

client.admin.organization.projects.users.create(stringprojectID, UserCreateParams { role, email, user\_id } body, RequestOptionsoptions?): [ProjectUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

client.admin.organization.projects.users.retrieve(stringuserID, UserRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

client.admin.organization.projects.users.update(stringuserID, UserUpdateParams { project\_id, role } params, RequestOptionsoptions?): [ProjectUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

client.admin.organization.projects.users.delete(stringuserID, UserDeleteParams { project\_id } params, RequestOptionsoptions?): [UserDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

ProjectUser { id, added\_at, object, 3 more }

Represents an individual user in a project.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

object: "organization.project.user"

The object type, which is always `organization.project.user`

role: string

`owner` or `member`

email?: string | null

The email address of the user

name?: string | null

The name of the user

UserDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.user.deleted"

#### ProjectsUsersRoles

##### [List project user role assignments](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

client.admin.organization.projects.users.roles.list(stringuserID, RoleListParams { project\_id, after, limit, order } params, RequestOptionsoptions?): NextCursorPage<[RoleListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

client.admin.organization.projects.users.roles.create(stringuserID, RoleCreateParams { project\_id, role\_id } params, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

client.admin.organization.projects.users.roles.retrieve(stringroleID, RoleRetrieveParams { project\_id, user\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

client.admin.organization.projects.users.roles.delete(stringroleID, RoleDeleteParams { project\_id, user\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

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

#### ProjectsService Accounts

##### [List project service accounts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

client.admin.organization.projects.serviceAccounts.list(stringprojectID, ServiceAccountListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectServiceAccount](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more } >

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

client.admin.organization.projects.serviceAccounts.create(stringprojectID, ServiceAccountCreateParams { name } body, RequestOptionsoptions?): [ServiceAccountCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)) { id, api\_key, created\_at, 3 more }

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

client.admin.organization.projects.serviceAccounts.retrieve(stringserviceAccountID, ServiceAccountRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectServiceAccount](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

client.admin.organization.projects.serviceAccounts.update(stringserviceAccountID, ServiceAccountUpdateParams { project\_id, name, role } params, RequestOptionsoptions?): [ProjectServiceAccount](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

client.admin.organization.projects.serviceAccounts.delete(stringserviceAccountID, ServiceAccountDeleteParams { project\_id } params, RequestOptionsoptions?): [ServiceAccountDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

ProjectServiceAccount { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: string

The name of the service account

object: "organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: "owner" | "member"

`owner` or `member`

One of the following:

"owner"

"member"

ServiceAccountCreateResponse { id, api\_key, created\_at, 3 more }

id: string

api\_key: APIKey | null

id: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account"

role: "member"

Service accounts can only have one role of type `member`

ServiceAccountDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.service\_account.deleted"

#### ProjectsAPI Keys

##### [List project API keys](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

client.admin.organization.projects.apiKeys.list(stringprojectID, APIKeyListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more } >

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

client.admin.organization.projects.apiKeys.retrieve(stringapiKeyID, APIKeyRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more }

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

client.admin.organization.projects.apiKeys.delete(stringapiKeyID, APIKeyDeleteParams { project\_id } params, RequestOptionsoptions?): [APIKeyDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

ProjectAPIKey { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: number | null

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: string

The name of the API key

object: "organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: Owner { service\_account, type, user }

service\_account?: ServiceAccount { id, created\_at, name, role }

The service account that owns a project API key.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: string

The name of the service account.

role: string

The service account’s project role.

type?: "user" | "service\_account"

`user` or `service_account`

One of the following:

"user"

"service\_account"

user?: User { id, created\_at, email, 2 more }

The user that owns a project API key.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: string

The email address of the user.

name: string

The name of the user.

role: string

The user’s project role.

redacted\_value: string

The redacted value of the API key

APIKeyDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.api\_key.deleted"

#### ProjectsRate Limits

##### [List project rate limits](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

client.admin.organization.projects.rateLimits.listRateLimits(stringprojectID, RateLimitListRateLimitsParams { after, before, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectRateLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more } >

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

client.admin.organization.projects.rateLimits.updateRateLimit(stringrateLimitID, RateLimitUpdateRateLimitParams { project\_id, batch\_1\_day\_max\_input\_tokens, max\_audio\_megabytes\_per\_1\_minute, 4 more } params, RequestOptionsoptions?): [ProjectRateLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

ProjectRateLimit { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

Represents a project rate limit config.

id: string

The identifier, which can be referenced in API endpoints.

max\_requests\_per\_1\_minute: number

The maximum requests per minute.

max\_tokens\_per\_1\_minute: number

The maximum tokens per minute.

model: string

The model this rate limit applies to.

object: "project.rate\_limit"

The object type, which is always `project.rate_limit`

batch\_1\_day\_max\_input\_tokens?: number

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute?: number

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute?: number

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day?: number

The maximum requests per day. Only present for relevant models.

#### ProjectsModel Permissions

##### [Retrieve project model permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

client.admin.organization.projects.modelPermissions.retrieve(stringprojectID, RequestOptionsoptions?): [ProjectModelPermissions](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

client.admin.organization.projects.modelPermissions.update(stringprojectID, ModelPermissionUpdateParams { mode, model\_ids } body, RequestOptionsoptions?): [ProjectModelPermissions](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

client.admin.organization.projects.modelPermissions.delete(stringprojectID, RequestOptionsoptions?): [ProjectModelPermissionsDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

ProjectModelPermissions { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: "allow\_list" | "deny\_list"

Whether the project uses an allowlist or a denylist.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: Array<string>

The model IDs included in the model permissions policy.

object: "project.model\_permissions"

The object type, which is always `project.model_permissions`.

ProjectModelPermissionsDeleted { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: boolean

Whether the project model permissions were deleted.

object: "project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

#### ProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

client.admin.organization.projects.hostedToolPermissions.retrieve(stringprojectID, RequestOptionsoptions?): [ProjectHostedToolPermissions](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

client.admin.organization.projects.hostedToolPermissions.update(stringprojectID, HostedToolPermissionUpdateParams { code\_interpreter, file\_search, image\_generation, 2 more } body, RequestOptionsoptions?): [ProjectHostedToolPermissions](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

ProjectHostedToolPermissions { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

file\_search: FileSearch { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

mcp: Mcp { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

web\_search: WebSearch { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

#### ProjectsGroups

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

#### ProjectsGroupsRoles

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

#### ProjectsRoles

##### [List project roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

client.admin.organization.projects.roles.list(stringprojectID, RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

client.admin.organization.projects.roles.create(stringprojectID, RoleCreateParams { permissions, role\_name, description } body, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

client.admin.organization.projects.roles.retrieve(stringroleID, RoleRetrieveParams { project\_id } params, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

client.admin.organization.projects.roles.update(stringroleID, RoleUpdateParams { project\_id, description, permissions, role\_name } params, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

client.admin.organization.projects.roles.delete(stringroleID, RoleDeleteParams { project\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/projects/{project\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

#### ProjectsData Retention

##### [Retrieve project data retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

client.admin.organization.projects.dataRetention.retrieve(stringprojectID, RequestOptionsoptions?): [ProjectDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

client.admin.organization.projects.dataRetention.update(stringprojectID, DataRetentionUpdateParams { retention\_type } body, RequestOptionsoptions?): [ProjectDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

ProjectDataRetention { object, type }

Represents a project’s data retention control setting.

object: "project.data\_retention"

The object type, which is always `project.data_retention`.

type: "organization\_default" | "none" | "zero\_data\_retention" | 3 more

The configured project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### ProjectsSpend Alerts

##### [List project spend alerts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

client.admin.organization.projects.spendAlerts.list(stringprojectID, SpendAlertListParams { after, before, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

client.admin.organization.projects.spendAlerts.create(stringprojectID, SpendAlertCreateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

client.admin.organization.projects.spendAlerts.retrieve(stringalertID, SpendAlertRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

client.admin.organization.projects.spendAlerts.update(stringalertID, SpendAlertUpdateParams { project\_id, currency, interval, 2 more } params, RequestOptionsoptions?): [ProjectSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

client.admin.organization.projects.spendAlerts.delete(stringalertID, SpendAlertDeleteParams { project\_id } params, RequestOptionsoptions?): [ProjectSpendAlertDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

ProjectSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

interval: "month"

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: Array<string>

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix?: string | null

Optional subject prefix for alert emails.

object: "project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

ProjectSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

#### ProjectsCertificates

##### [List project certificates](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

client.admin.organization.projects.certificates.list(stringprojectID, CertificateListParams { after, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[CertificateListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

client.admin.organization.projects.certificates.activate(stringprojectID, CertificateActivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateActivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

client.admin.organization.projects.certificates.deactivate(stringprojectID, CertificateDeactivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateDeactivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/deactivate

##### ModelsExpand Collapse

CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.
