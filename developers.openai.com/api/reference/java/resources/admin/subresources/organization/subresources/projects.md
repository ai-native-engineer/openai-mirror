<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Projects

##### [List projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/list)

ProjectListPage admin().organization().projects().list(ProjectListParamsparams = ProjectListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects

##### [Create project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/create)

[Project](/api/reference/java/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) admin().organization().projects().create(ProjectCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects

##### [Retrieve project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

[Project](/api/reference/java/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) admin().organization().projects().retrieve(ProjectRetrieveParamsparams = ProjectRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/update)

[Project](/api/reference/java/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) admin().organization().projects().update(ProjectUpdateParamsparams = ProjectUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/methods/archive)

[Project](/api/reference/java/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) admin().organization().projects().archive(ProjectArchiveParamsparams = ProjectArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

class Project:

Represents an individual project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

JsonValue; object\_ "organization.project"constant"organization.project"constant

The object type, which is always `organization.project`

Optional<Long> archivedAt

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

Optional<String> externalKeyId

The external key associated with the project.

Optional<String> name

The name of the project. This appears in reporting.

Optional<String> status

`active` or `archived`

#### ProjectsUsers

##### [List project users](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

UserListPage admin().organization().projects().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

[ProjectUser](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) admin().organization().projects().users().create(UserCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

[ProjectUser](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) admin().organization().projects().users().retrieve(UserRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

[ProjectUser](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) admin().organization().projects().users().update(UserUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().projects().users().delete(UserDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

class ProjectUser:

Represents an individual user in a project.

String id

The identifier, which can be referenced in API endpoints

long addedAt

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

JsonValue; object\_ "organization.project.user"constant"organization.project.user"constant

The object type, which is always `organization.project.user`

String role

`owner` or `member`

Optional<String> email

The email address of the user

Optional<String> name

The name of the user

#### ProjectsUsersRoles

##### [List project user role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

RoleListPage admin().organization().projects().users().roles().list(RoleListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().projects().users().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().projects().users().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().projects().users().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

#### ProjectsService Accounts

##### [List project service accounts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

ServiceAccountListPage admin().organization().projects().serviceAccounts().list(ServiceAccountListParamsparams = ServiceAccountListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

[ServiceAccountCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20ServiceAccountCreateResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().create(ServiceAccountCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

[ProjectServiceAccount](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) admin().organization().projects().serviceAccounts().retrieve(ServiceAccountRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

[ProjectServiceAccount](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) admin().organization().projects().serviceAccounts().update(ServiceAccountUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

[ServiceAccountDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20ServiceAccountDeleteResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().delete(ServiceAccountDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

class ProjectServiceAccount:

Represents an individual service account in a project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

String name

The name of the service account

JsonValue; object\_ "organization.project.service\_account"constant"organization.project.service\_account"constant

The object type, which is always `organization.project.service_account`

Role role

`owner` or `member`

One of the following:

OWNER("owner")

MEMBER("member")

#### ProjectsAPI Keys

##### [List project API keys](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

ApiKeyListPage admin().organization().projects().apiKeys().list(ApiKeyListParamsparams = ApiKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

[ProjectApiKey](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) admin().organization().projects().apiKeys().retrieve(ApiKeyRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

[ApiKeyDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20ApiKeyDeleteResponse%20%3E%20(schema)) admin().organization().projects().apiKeys().delete(ApiKeyDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

class ProjectApiKey:

Represents an individual API key in a project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

Optional<Long> lastUsedAt

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

String name

The name of the API key

JsonValue; object\_ "organization.project.api\_key"constant"organization.project.api\_key"constant

The object type, which is always `organization.project.api_key`

Owner owner

Optional<ServiceAccount> serviceAccount

The service account that owns a project API key.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

String name

The name of the service account.

String role

The service account’s project role.

Optional<Type> type

`user` or `service_account`

One of the following:

USER("user")

SERVICE\_ACCOUNT("service\_account")

Optional<User> user

The user that owns a project API key.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

String email

The email address of the user.

String name

The name of the user.

String role

The user’s project role.

String redactedValue

The redacted value of the API key

#### ProjectsRate Limits

##### [List project rate limits](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

RateLimitListRateLimitsPage admin().organization().projects().rateLimits().listRateLimits(RateLimitListRateLimitsParamsparams = RateLimitListRateLimitsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

[ProjectRateLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) admin().organization().projects().rateLimits().updateRateLimit(RateLimitUpdateRateLimitParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

class ProjectRateLimit:

Represents a project rate limit config.

String id

The identifier, which can be referenced in API endpoints.

long maxRequestsPer1Minute

The maximum requests per minute.

long maxTokensPer1Minute

The maximum tokens per minute.

String model

The model this rate limit applies to.

JsonValue; object\_ "project.rate\_limit"constant"project.rate\_limit"constant

The object type, which is always `project.rate_limit`

Optional<Long> batch1DayMaxInputTokens

The maximum batch input tokens per day. Only present for relevant models.

Optional<Long> maxAudioMegabytesPer1Minute

The maximum audio megabytes per minute. Only present for relevant models.

Optional<Long> maxImagesPer1Minute

The maximum images per minute. Only present for relevant models.

Optional<Long> maxRequestsPer1Day

The maximum requests per day. Only present for relevant models.

#### ProjectsModel Permissions

##### [Retrieve project model permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

[ProjectModelPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) admin().organization().projects().modelPermissions().retrieve(ModelPermissionRetrieveParamsparams = ModelPermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

[ProjectModelPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) admin().organization().projects().modelPermissions().update(ModelPermissionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

[ProjectModelPermissionsDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) admin().organization().projects().modelPermissions().delete(ModelPermissionDeleteParamsparams = ModelPermissionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

class ProjectModelPermissions:

Represents the model allowlist or denylist policy for a project.

Mode mode

Whether the project uses an allowlist or a denylist.

One of the following:

ALLOW\_LIST("allow\_list")

DENY\_LIST("deny\_list")

List<String> modelIds

The model IDs included in the model permissions policy.

JsonValue; object\_ "project.model\_permissions"constant"project.model\_permissions"constant

The object type, which is always `project.model_permissions`.

class ProjectModelPermissionsDeleted:

Confirmation payload returned after deleting project model permissions.

boolean deleted

Whether the project model permissions were deleted.

JsonValue; object\_ "project.model\_permissions.deleted"constant"project.model\_permissions.deleted"constant

The object type, which is always `project.model_permissions.deleted`.

#### ProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

[ProjectHostedToolPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) admin().organization().projects().hostedToolPermissions().retrieve(HostedToolPermissionRetrieveParamsparams = HostedToolPermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

[ProjectHostedToolPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) admin().organization().projects().hostedToolPermissions().update(HostedToolPermissionUpdateParamsparams = HostedToolPermissionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

class ProjectHostedToolPermissions:

Represents hosted tool permissions for a project.

CodeInterpreter codeInterpreter

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

FileSearch fileSearch

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

ImageGeneration imageGeneration

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

Mcp mcp

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

WebSearch webSearch

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

#### ProjectsGroups

##### [List project groups](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

GroupListPage admin().organization().projects().groups().list(GroupListParamsparams = GroupListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

[ProjectGroup](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) admin().organization().projects().groups().create(GroupCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

[ProjectGroup](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) admin().organization().projects().groups().retrieve(GroupRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

[GroupDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20GroupDeleteResponse%20%3E%20(schema)) admin().organization().projects().groups().delete(GroupDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

class ProjectGroup:

Details about a group’s membership in a project.

long createdAt

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

String groupId

Identifier of the group that has access to the project.

String groupName

Display name of the group.

GroupType groupType

The type of the group.

One of the following:

GROUP("group")

TENANT\_GROUP("tenant\_group")

JsonValue; object\_ "project.group"constant"project.group"constant

Always `project.group`.

String projectId

Identifier of the project.

#### ProjectsGroupsRoles

##### [List project group role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

RoleListPage admin().organization().projects().groups().roles().list(RoleListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().projects().groups().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().projects().groups().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().projects().groups().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

#### ProjectsRoles

##### [List project roles](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

RoleListPage admin().organization().projects().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().projects().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().projects().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().projects().roles().update(RoleUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().projects().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/projects/{project\_id}/roles/{role\_id}

#### ProjectsData Retention

##### [Retrieve project data retention](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

[ProjectDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) admin().organization().projects().dataRetention().retrieve(DataRetentionRetrieveParamsparams = DataRetentionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

[ProjectDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) admin().organization().projects().dataRetention().update(DataRetentionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

class ProjectDataRetention:

Represents a project’s data retention control setting.

JsonValue; object\_ "project.data\_retention"constant"project.data\_retention"constant

The object type, which is always `project.data_retention`.

Type type

The configured project data retention type.

One of the following:

ORGANIZATION\_DEFAULT("organization\_default")

NONE("none")

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")

#### ProjectsSpend Alerts

##### [List project spend alerts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

SpendAlertListPage admin().organization().projects().spendAlerts().list(SpendAlertListParamsparams = SpendAlertListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().create(SpendAlertCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().retrieve(SpendAlertRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

[ProjectSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert%20%3E%20(schema)) admin().organization().projects().spendAlerts().update(SpendAlertUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

[ProjectSpendAlertDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.spend_alerts%20%3E%20(model)%20project_spend_alert_deleted%20%3E%20(schema)) admin().organization().projects().spendAlerts().delete(SpendAlertDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class ProjectSpendAlert:

Represents a spend alert configured at the project level.

String id

The identifier, which can be referenced in API endpoints.

Currency currency

The currency for the threshold amount.

Interval interval

The time interval for evaluating spend against the threshold.

NotificationChannel notificationChannel

Email notification settings for a spend alert.

List<String> recipients

Email addresses that receive the spend alert notification.

JsonValue; type "email"constant"email"constant

The notification channel type. Currently only `email` is supported.

Optional<String> subjectPrefix

Optional subject prefix for alert emails.

JsonValue; object\_ "project.spend\_alert"constant"project.spend\_alert"constant

The object type, which is always `project.spend_alert`.

long thresholdAmount

The alert threshold amount, in cents.

class ProjectSpendAlertDeleted:

Confirmation payload returned after deleting a project spend alert.

String id

The deleted spend alert ID.

boolean deleted

Whether the spend alert was deleted.

JsonValue; object\_ "project.spend\_alert.deleted"constant"project.spend\_alert.deleted"constant

Always `project.spend_alert.deleted`.

#### ProjectsCertificates

##### [List project certificates](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

CertificateListPage admin().organization().projects().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

CertificateActivatePage admin().organization().projects().certificates().activate(CertificateActivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

CertificateDeactivatePage admin().organization().projects().certificates().deactivate(CertificateDeactivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/certificates/deactivate
