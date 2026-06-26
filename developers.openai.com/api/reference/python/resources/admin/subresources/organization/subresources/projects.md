<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Projects

##### [List projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/list)

admin.organization.projects.list(ProjectListParams\*\*kwargs)  -> SyncConversationCursorPage[[Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))]

GET/organization/projects

##### [Create project](/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/create)

admin.organization.projects.create(ProjectCreateParams\*\*kwargs)  -> [Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

POST/organization/projects

##### [Retrieve project](/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

admin.organization.projects.retrieve(strproject\_id)  -> [Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/update)

admin.organization.projects.update(strproject\_id, ProjectUpdateParams\*\*kwargs)  -> [Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/python/resources/admin/subresources/organization/subresources/projects/methods/archive)

admin.organization.projects.archive(strproject\_id)  -> [Project](/api/reference/python/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

class Project: …

Represents an individual project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: Literal["organization.project"]

The object type, which is always `organization.project`

archived\_at: Optional[int]

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id: Optional[str]

The external key associated with the project.

name: Optional[str]

The name of the project. This appears in reporting.

status: Optional[str]

`active` or `archived`

#### ProjectsUsers

##### [List project users](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

admin.organization.projects.users.list(strproject\_id, UserListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectUser](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))]

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

admin.organization.projects.users.create(strproject\_id, UserCreateParams\*\*kwargs)  -> [ProjectUser](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

admin.organization.projects.users.retrieve(struser\_id, UserRetrieveParams\*\*kwargs)  -> [ProjectUser](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

admin.organization.projects.users.update(struser\_id, UserUpdateParams\*\*kwargs)  -> [ProjectUser](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

admin.organization.projects.users.delete(struser\_id, UserDeleteParams\*\*kwargs)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

class ProjectUser: …

Represents an individual user in a project.

id: str

The identifier, which can be referenced in API endpoints

added\_at: int

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

object: Literal["organization.project.user"]

The object type, which is always `organization.project.user`

role: str

`owner` or `member`

email: Optional[str]

The email address of the user

name: Optional[str]

The name of the user

class UserDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.user.deleted"]

#### ProjectsUsersRoles

##### [List project user role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

admin.organization.projects.users.roles.list(struser\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

admin.organization.projects.users.roles.create(struser\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

admin.organization.projects.users.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

admin.organization.projects.users.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleListResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleCreateResponse: …

Role assignment linking a user to a role.

object: Literal["user.role"]

Always `user.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

Represents an individual `user` within an organization.

class RoleRetrieveResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleDeleteResponse: …

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: str

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

#### ProjectsService Accounts

##### [List project service accounts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

admin.organization.projects.service\_accounts.list(strproject\_id, ServiceAccountListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))]

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

admin.organization.projects.service\_accounts.create(strproject\_id, ServiceAccountCreateParams\*\*kwargs)  -> [ServiceAccountCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

admin.organization.projects.service\_accounts.retrieve(strservice\_account\_id, ServiceAccountRetrieveParams\*\*kwargs)  -> [ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

admin.organization.projects.service\_accounts.update(strservice\_account\_id, ServiceAccountUpdateParams\*\*kwargs)  -> [ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

admin.organization.projects.service\_accounts.delete(strservice\_account\_id, ServiceAccountDeleteParams\*\*kwargs)  -> [ServiceAccountDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

class ProjectServiceAccount: …

Represents an individual service account in a project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: str

The name of the service account

object: Literal["organization.project.service\_account"]

The object type, which is always `organization.project.service_account`

role: Literal["owner", "member"]

`owner` or `member`

One of the following:

"owner"

"member"

class ServiceAccountCreateResponse: …

id: str

api\_key: Optional[APIKey]

id: str

created\_at: int

formatunixtime

name: str

object: Literal["organization.project.service\_account.api\_key"]

The object type, which is always `organization.project.service_account.api_key`

value: str

created\_at: int

formatunixtime

name: str

object: Literal["organization.project.service\_account"]

role: Literal["member"]

Service accounts can only have one role of type `member`

class ServiceAccountDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.service\_account.deleted"]

#### ProjectsAPI Keys

##### [List project API keys](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

admin.organization.projects.api\_keys.list(strproject\_id, APIKeyListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))]

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

admin.organization.projects.api\_keys.retrieve(strapi\_key\_id, APIKeyRetrieveParams\*\*kwargs)  -> [ProjectAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

admin.organization.projects.api\_keys.delete(strapi\_key\_id, APIKeyDeleteParams\*\*kwargs)  -> [APIKeyDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

class ProjectAPIKey: …

Represents an individual API key in a project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: str

The name of the API key

object: Literal["organization.project.api\_key"]

The object type, which is always `organization.project.api_key`

owner: Owner

service\_account: Optional[OwnerServiceAccount]

The service account that owns a project API key.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: str

The name of the service account.

role: str

The service account’s project role.

type: Optional[Literal["user", "service\_account"]]

`user` or `service_account`

One of the following:

"user"

"service\_account"

user: Optional[OwnerUser]

The user that owns a project API key.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: str

The email address of the user.

name: str

The name of the user.

role: str

The user’s project role.

redacted\_value: str

The redacted value of the API key

class APIKeyDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.api\_key.deleted"]

#### ProjectsRate Limits

##### [List project rate limits](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

admin.organization.projects.rate\_limits.list\_rate\_limits(strproject\_id, RateLimitListRateLimitsParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectRateLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))]

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

admin.organization.projects.rate\_limits.update\_rate\_limit(strrate\_limit\_id, RateLimitUpdateRateLimitParams\*\*kwargs)  -> [ProjectRateLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

class ProjectRateLimit: …

Represents a project rate limit config.

id: str

The identifier, which can be referenced in API endpoints.

max\_requests\_per\_1\_minute: int

The maximum requests per minute.

max\_tokens\_per\_1\_minute: int

The maximum tokens per minute.

model: str

The model this rate limit applies to.

object: Literal["project.rate\_limit"]

The object type, which is always `project.rate_limit`

batch\_1\_day\_max\_input\_tokens: Optional[int]

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute: Optional[int]

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute: Optional[int]

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day: Optional[int]

The maximum requests per day. Only present for relevant models.

#### ProjectsModel Permissions

##### [Retrieve project model permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

admin.organization.projects.model\_permissions.retrieve(strproject\_id)  -> [ProjectModelPermissions](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema))

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

admin.organization.projects.model\_permissions.update(strproject\_id, ModelPermissionUpdateParams\*\*kwargs)  -> [ProjectModelPermissions](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema))

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

admin.organization.projects.model\_permissions.delete(strproject\_id)  -> [ProjectModelPermissionsDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

class ProjectModelPermissions: …

Represents the model allowlist or denylist policy for a project.

mode: Literal["allow\_list", "deny\_list"]

Whether the project uses an allowlist or a denylist.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: List[str]

The model IDs included in the model permissions policy.

object: Literal["project.model\_permissions"]

The object type, which is always `project.model_permissions`.

class ProjectModelPermissionsDeleted: …

Confirmation payload returned after deleting project model permissions.

deleted: bool

Whether the project model permissions were deleted.

object: Literal["project.model\_permissions.deleted"]

The object type, which is always `project.model_permissions.deleted`.

#### ProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

admin.organization.projects.hosted\_tool\_permissions.retrieve(strproject\_id)  -> [ProjectHostedToolPermissions](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema))

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

admin.organization.projects.hosted\_tool\_permissions.update(strproject\_id, HostedToolPermissionUpdateParams\*\*kwargs)  -> [ProjectHostedToolPermissions](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema))

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

class ProjectHostedToolPermissions: …

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

file\_search: FileSearch

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

mcp: Mcp

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

web\_search: WebSearch

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

#### ProjectsGroups

##### [List project groups](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

admin.organization.projects.groups.list(strproject\_id, GroupListParams\*\*kwargs)  -> SyncNextCursorPage[[ProjectGroup](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))]

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

admin.organization.projects.groups.create(strproject\_id, GroupCreateParams\*\*kwargs)  -> [ProjectGroup](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

admin.organization.projects.groups.retrieve(strgroup\_id, GroupRetrieveParams\*\*kwargs)  -> [ProjectGroup](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

admin.organization.projects.groups.delete(strgroup\_id, GroupDeleteParams\*\*kwargs)  -> [GroupDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

class ProjectGroup: …

Details about a group’s membership in a project.

created\_at: int

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: str

Identifier of the group that has access to the project.

group\_name: str

Display name of the group.

group\_type: Literal["group", "tenant\_group"]

The type of the group.

One of the following:

"group"

"tenant\_group"

object: Literal["project.group"]

Always `project.group`.

project\_id: str

Identifier of the project.

class GroupDeleteResponse: …

Confirmation payload returned after removing a group from a project.

deleted: bool

Whether the group membership in the project was removed.

object: Literal["project.group.deleted"]

Always `project.group.deleted`.

#### ProjectsGroupsRoles

##### [List project group role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

admin.organization.projects.groups.roles.list(strgroup\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

admin.organization.projects.groups.roles.create(strgroup\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.projects.groups.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

admin.organization.projects.groups.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleListResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleCreateResponse: …

Role assignment linking a group to a role.

group: Group

Summary information about a group returned in role assignment responses.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: str

Display name of the group.

object: Literal["group"]

Always `group`.

scim\_managed: bool

Whether the group is managed through SCIM.

object: Literal["group.role"]

Always `group.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

class RoleRetrieveResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleDeleteResponse: …

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: str

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

#### ProjectsRoles

##### [List project roles](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

admin.organization.projects.roles.list(strproject\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))]

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

admin.organization.projects.roles.create(strproject\_id, RoleCreateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

admin.organization.projects.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

admin.organization.projects.roles.update(strrole\_id, RoleUpdateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

admin.organization.projects.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/projects/{project\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleDeleteResponse: …

Confirmation payload returned after deleting a role.

id: str

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: Literal["role.deleted"]

Always `role.deleted`.

#### ProjectsData Retention

##### [Retrieve project data retention](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

admin.organization.projects.data\_retention.retrieve(strproject\_id)  -> [ProjectDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema))

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

admin.organization.projects.data\_retention.update(strproject\_id, DataRetentionUpdateParams\*\*kwargs)  -> [ProjectDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema))

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

class ProjectDataRetention: …

Represents a project’s data retention control setting.

object: Literal["project.data\_retention"]

The object type, which is always `project.data_retention`.

type: Literal["organization\_default", "none", "zero\_data\_retention", 3 more]

The configured project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### ProjectsSpend Alerts

##### [List project spend alerts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

admin.organization.projects.spend\_alerts.list(strproject\_id, SpendAlertListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))]

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

admin.organization.projects.spend\_alerts.create(strproject\_id, SpendAlertCreateParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

admin.organization.projects.spend\_alerts.retrieve(stralert\_id, SpendAlertRetrieveParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

admin.organization.projects.spend\_alerts.update(stralert\_id, SpendAlertUpdateParams\*\*kwargs)  -> [ProjectSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

admin.organization.projects.spend\_alerts.delete(stralert\_id, SpendAlertDeleteParams\*\*kwargs)  -> [ProjectSpendAlertDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class ProjectSpendAlert: …

Represents a spend alert configured at the project level.

id: str

The identifier, which can be referenced in API endpoints.

currency: Literal["USD"]

The currency for the threshold amount.

interval: Literal["month"]

The time interval for evaluating spend against the threshold.

notification\_channel: NotificationChannel

Email notification settings for a spend alert.

recipients: List[str]

Email addresses that receive the spend alert notification.

type: Literal["email"]

The notification channel type. Currently only `email` is supported.

subject\_prefix: Optional[str]

Optional subject prefix for alert emails.

object: Literal["project.spend\_alert"]

The object type, which is always `project.spend_alert`.

threshold\_amount: int

The alert threshold amount, in cents.

class ProjectSpendAlertDeleted: …

Confirmation payload returned after deleting a project spend alert.

id: str

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: Literal["project.spend\_alert.deleted"]

Always `project.spend_alert.deleted`.

#### ProjectsCertificates

##### [List project certificates](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

admin.organization.projects.certificates.list(strproject\_id, CertificateListParams\*\*kwargs)  -> SyncConversationCursorPage[[CertificateListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema))]

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

admin.organization.projects.certificates.activate(strproject\_id, CertificateActivateParams\*\*kwargs)  -> SyncPage[[CertificateActivateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema))]

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

admin.organization.projects.certificates.deactivate(strproject\_id, CertificateDeactivateParams\*\*kwargs)  -> SyncPage[[CertificateDeactivateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema))]

POST/organization/projects/{project\_id}/certificates/deactivate

##### ModelsExpand Collapse

class CertificateListResponse: …

Represents an individual certificate configured at the project level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.project.certificate"]

The object type, which is always `organization.project.certificate`.

class CertificateActivateResponse: …

Represents an individual certificate configured at the project level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.project.certificate"]

The object type, which is always `organization.project.certificate`.

class CertificateDeactivateResponse: …

Represents an individual certificate configured at the project level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.project.certificate"]

The object type, which is always `organization.project.certificate`.
