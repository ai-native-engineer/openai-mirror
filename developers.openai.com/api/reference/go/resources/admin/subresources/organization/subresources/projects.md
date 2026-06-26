<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Projects

##### [List projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/list)

client.Admin.Organization.Projects.List(ctx, query) (\*ConversationCursorPage[[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema))], error)

GET/organization/projects

##### [Create project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/create)

client.Admin.Organization.Projects.New(ctx, body) (\*[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)), error)

POST/organization/projects

##### [Retrieve project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

client.Admin.Organization.Projects.Get(ctx, projectID) (\*[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/update)

client.Admin.Organization.Projects.Update(ctx, projectID, body) (\*[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/methods/archive)

client.Admin.Organization.Projects.Archive(ctx, projectID) (\*[Project](/api/reference/go/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

type Project struct{…}

Represents an individual project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

Object OrganizationProject

The object type, which is always `organization.project`

ArchivedAt int64Optional

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

ExternalKeyID stringOptional

The external key associated with the project.

Name stringOptional

The name of the project. This appears in reporting.

Status stringOptional

`active` or `archived`

#### ProjectsUsers

##### [List project users](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

client.Admin.Organization.Projects.Users.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

client.Admin.Organization.Projects.Users.New(ctx, projectID, body) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

client.Admin.Organization.Projects.Users.Get(ctx, projectID, userID) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

client.Admin.Organization.Projects.Users.Update(ctx, projectID, userID, body) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

client.Admin.Organization.Projects.Users.Delete(ctx, projectID, userID) (\*[AdminOrganizationProjectUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20AdminOrganizationProjectUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

type ProjectUser struct{…}

Represents an individual user in a project.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

Object OrganizationProjectUser

The object type, which is always `organization.project.user`

Role string

`owner` or `member`

Email stringOptional

The email address of the user

Name stringOptional

The name of the user

#### ProjectsUsersRoles

##### [List project user role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

client.Admin.Organization.Projects.Users.Roles.List(ctx, projectID, userID, query) (\*NextCursorPage[[AdminOrganizationProjectUserRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleListResponse%20%3E%20(schema))], error)

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

client.Admin.Organization.Projects.Users.Roles.New(ctx, projectID, userID, body) (\*[AdminOrganizationProjectUserRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleNewResponse%20%3E%20(schema)), error)

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

client.Admin.Organization.Projects.Users.Roles.Get(ctx, projectID, userID, roleID) (\*[AdminOrganizationProjectUserRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleGetResponse%20%3E%20(schema)), error)

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

client.Admin.Organization.Projects.Users.Roles.Delete(ctx, projectID, userID, roleID) (\*[AdminOrganizationProjectUserRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

#### ProjectsService Accounts

##### [List project service accounts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

client.Admin.Organization.Projects.ServiceAccounts.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectServiceAccount](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

client.Admin.Organization.Projects.ServiceAccounts.New(ctx, projectID, body) (\*[AdminOrganizationProjectServiceAccountNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20AdminOrganizationProjectServiceAccountNewResponse%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

client.Admin.Organization.Projects.ServiceAccounts.Get(ctx, projectID, serviceAccountID) (\*[ProjectServiceAccount](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

client.Admin.Organization.Projects.ServiceAccounts.Update(ctx, projectID, serviceAccountID, body) (\*[ProjectServiceAccount](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

client.Admin.Organization.Projects.ServiceAccounts.Delete(ctx, projectID, serviceAccountID) (\*[AdminOrganizationProjectServiceAccountDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20AdminOrganizationProjectServiceAccountDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

type ProjectServiceAccount struct{…}

Represents an individual service account in a project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

Name string

The name of the service account

Object OrganizationProjectServiceAccount

The object type, which is always `organization.project.service_account`

Role ProjectServiceAccountRole

`owner` or `member`

One of the following:

const ProjectServiceAccountRoleOwner ProjectServiceAccountRole = "owner"

const ProjectServiceAccountRoleMember ProjectServiceAccountRole = "member"

#### ProjectsAPI Keys

##### [List project API keys](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

client.Admin.Organization.Projects.APIKeys.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

client.Admin.Organization.Projects.APIKeys.Get(ctx, projectID, apiKeyID) (\*[ProjectAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

client.Admin.Organization.Projects.APIKeys.Delete(ctx, projectID, apiKeyID) (\*[AdminOrganizationProjectAPIKeyDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20AdminOrganizationProjectAPIKeyDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

type ProjectAPIKey struct{…}

Represents an individual API key in a project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

LastUsedAt int64

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

Name string

The name of the API key

Object OrganizationProjectAPIKey

The object type, which is always `organization.project.api_key`

Owner ProjectAPIKeyOwner

ServiceAccount ProjectAPIKeyOwnerServiceAccountOptional

The service account that owns a project API key.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

Name string

The name of the service account.

Role string

The service account’s project role.

Type stringOptional

`user` or `service_account`

One of the following:

const ProjectAPIKeyOwnerTypeUser ProjectAPIKeyOwnerType = "user"

const ProjectAPIKeyOwnerTypeServiceAccount ProjectAPIKeyOwnerType = "service\_account"

User ProjectAPIKeyOwnerUserOptional

The user that owns a project API key.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

Email string

The email address of the user.

Name string

The name of the user.

Role string

The user’s project role.

RedactedValue string

The redacted value of the API key

#### ProjectsRate Limits

##### [List project rate limits](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

client.Admin.Organization.Projects.RateLimits.ListRateLimits(ctx, projectID, query) (\*ConversationCursorPage[[ProjectRateLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

client.Admin.Organization.Projects.RateLimits.UpdateRateLimit(ctx, projectID, rateLimitID, body) (\*[ProjectRateLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

type ProjectRateLimit struct{…}

Represents a project rate limit config.

ID string

The identifier, which can be referenced in API endpoints.

MaxRequestsPer1Minute int64

The maximum requests per minute.

MaxTokensPer1Minute int64

The maximum tokens per minute.

Model string

The model this rate limit applies to.

Object ProjectRateLimit

The object type, which is always `project.rate_limit`

Batch1DayMaxInputTokens int64Optional

The maximum batch input tokens per day. Only present for relevant models.

MaxAudioMegabytesPer1Minute int64Optional

The maximum audio megabytes per minute. Only present for relevant models.

MaxImagesPer1Minute int64Optional

The maximum images per minute. Only present for relevant models.

MaxRequestsPer1Day int64Optional

The maximum requests per day. Only present for relevant models.

#### ProjectsModel Permissions

##### [Retrieve project model permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

client.Admin.Organization.Projects.ModelPermissions.Get(ctx, projectID) (\*[ProjectModelPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

client.Admin.Organization.Projects.ModelPermissions.Update(ctx, projectID, body) (\*[ProjectModelPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

client.Admin.Organization.Projects.ModelPermissions.Delete(ctx, projectID) (\*[ProjectModelPermissionsDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

type ProjectModelPermissions struct{…}

Represents the model allowlist or denylist policy for a project.

Mode ProjectModelPermissionsMode

Whether the project uses an allowlist or a denylist.

One of the following:

const ProjectModelPermissionsModeAllowList ProjectModelPermissionsMode = "allow\_list"

const ProjectModelPermissionsModeDenyList ProjectModelPermissionsMode = "deny\_list"

ModelIDs []string

The model IDs included in the model permissions policy.

Object ProjectModelPermissions

The object type, which is always `project.model_permissions`.

type ProjectModelPermissionsDeleted struct{…}

Confirmation payload returned after deleting project model permissions.

Deleted bool

Whether the project model permissions were deleted.

Object ProjectModelPermissionsDeleted

The object type, which is always `project.model_permissions.deleted`.

#### ProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

client.Admin.Organization.Projects.HostedToolPermissions.Get(ctx, projectID) (\*[ProjectHostedToolPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

client.Admin.Organization.Projects.HostedToolPermissions.Update(ctx, projectID, body) (\*[ProjectHostedToolPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

type ProjectHostedToolPermissions struct{…}

Represents hosted tool permissions for a project.

CodeInterpreter ProjectHostedToolPermissionsCodeInterpreter

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

FileSearch ProjectHostedToolPermissionsFileSearch

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

ImageGeneration ProjectHostedToolPermissionsImageGeneration

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

Mcp ProjectHostedToolPermissionsMcp

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

WebSearch ProjectHostedToolPermissionsWebSearch

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

#### ProjectsGroups

##### [List project groups](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

client.Admin.Organization.Projects.Groups.List(ctx, projectID, query) (\*NextCursorPage[[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

client.Admin.Organization.Projects.Groups.New(ctx, projectID, body) (\*[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

client.Admin.Organization.Projects.Groups.Get(ctx, projectID, groupID, query) (\*[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

client.Admin.Organization.Projects.Groups.Delete(ctx, projectID, groupID) (\*[AdminOrganizationProjectGroupDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20AdminOrganizationProjectGroupDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

type ProjectGroup struct{…}

Details about a group’s membership in a project.

CreatedAt int64

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

GroupID string

Identifier of the group that has access to the project.

GroupName string

Display name of the group.

GroupType ProjectGroupGroupType

The type of the group.

One of the following:

const ProjectGroupGroupTypeGroup ProjectGroupGroupType = "group"

const ProjectGroupGroupTypeTenantGroup ProjectGroupGroupType = "tenant\_group"

Object ProjectGroup

Always `project.group`.

ProjectID string

Identifier of the project.

#### ProjectsGroupsRoles

##### [List project group role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

client.Admin.Organization.Projects.Groups.Roles.List(ctx, projectID, groupID, query) (\*NextCursorPage[[AdminOrganizationProjectGroupRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleListResponse%20%3E%20(schema))], error)

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

client.Admin.Organization.Projects.Groups.Roles.New(ctx, projectID, groupID, body) (\*[AdminOrganizationProjectGroupRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleNewResponse%20%3E%20(schema)), error)

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

client.Admin.Organization.Projects.Groups.Roles.Get(ctx, projectID, groupID, roleID) (\*[AdminOrganizationProjectGroupRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleGetResponse%20%3E%20(schema)), error)

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

client.Admin.Organization.Projects.Groups.Roles.Delete(ctx, projectID, groupID, roleID) (\*[AdminOrganizationProjectGroupRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

#### ProjectsRoles

##### [List project roles](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

client.Admin.Organization.Projects.Roles.List(ctx, projectID, query) (\*NextCursorPage[[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))], error)

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

client.Admin.Organization.Projects.Roles.New(ctx, projectID, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

client.Admin.Organization.Projects.Roles.Get(ctx, projectID, roleID) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

client.Admin.Organization.Projects.Roles.Update(ctx, projectID, roleID, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

client.Admin.Organization.Projects.Roles.Delete(ctx, projectID, roleID) (\*[AdminOrganizationProjectRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20AdminOrganizationProjectRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/roles/{role\_id}

#### ProjectsData Retention

##### [Retrieve project data retention](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

client.Admin.Organization.Projects.DataRetention.Get(ctx, projectID) (\*[ProjectDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

client.Admin.Organization.Projects.DataRetention.Update(ctx, projectID, body) (\*[ProjectDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

type ProjectDataRetention struct{…}

Represents a project’s data retention control setting.

Object ProjectDataRetention

The object type, which is always `project.data_retention`.

Type ProjectDataRetentionType

The configured project data retention type.

One of the following:

const ProjectDataRetentionTypeOrganizationDefault ProjectDataRetentionType = "organization\_default"

const ProjectDataRetentionTypeNone ProjectDataRetentionType = "none"

const ProjectDataRetentionTypeZeroDataRetention ProjectDataRetentionType = "zero\_data\_retention"

const ProjectDataRetentionTypeModifiedAbuseMonitoring ProjectDataRetentionType = "modified\_abuse\_monitoring"

const ProjectDataRetentionTypeEnhancedZeroDataRetention ProjectDataRetentionType = "enhanced\_zero\_data\_retention"

const ProjectDataRetentionTypeEnhancedModifiedAbuseMonitoring ProjectDataRetentionType = "enhanced\_modified\_abuse\_monitoring"

#### ProjectsSpend Alerts

##### [List project spend alerts](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

client.Admin.Organization.Projects.SpendAlerts.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

client.Admin.Organization.Projects.SpendAlerts.New(ctx, projectID, body) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

client.Admin.Organization.Projects.SpendAlerts.Get(ctx, projectID, alertID) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

client.Admin.Organization.Projects.SpendAlerts.Update(ctx, projectID, alertID, body) (\*[ProjectSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

client.Admin.Organization.Projects.SpendAlerts.Delete(ctx, projectID, alertID) (\*[ProjectSpendAlertDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

type ProjectSpendAlert struct{…}

Represents a spend alert configured at the project level.

ID string

The identifier, which can be referenced in API endpoints.

Currency ProjectSpendAlertCurrency

The currency for the threshold amount.

Interval ProjectSpendAlertInterval

The time interval for evaluating spend against the threshold.

NotificationChannel ProjectSpendAlertNotificationChannel

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

Object ProjectSpendAlert

The object type, which is always `project.spend_alert`.

ThresholdAmount int64

The alert threshold amount, in cents.

type ProjectSpendAlertDeleted struct{…}

Confirmation payload returned after deleting a project spend alert.

ID string

The deleted spend alert ID.

Deleted bool

Whether the spend alert was deleted.

Object ProjectSpendAlertDeleted

Always `project.spend_alert.deleted`.

#### ProjectsCertificates

##### [List project certificates](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

client.Admin.Organization.Projects.Certificates.List(ctx, projectID, query) (\*ConversationCursorPage[[AdminOrganizationProjectCertificateListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateListResponse%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

client.Admin.Organization.Projects.Certificates.Activate(ctx, projectID, body) (\*Page[[AdminOrganizationProjectCertificateActivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateActivateResponse%20%3E%20(schema))], error)

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

client.Admin.Organization.Projects.Certificates.Deactivate(ctx, projectID, body) (\*Page[[AdminOrganizationProjectCertificateDeactivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateDeactivateResponse%20%3E%20(schema))], error)

POST/organization/projects/{project\_id}/certificates/deactivate
