<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Organization

#### OrganizationAudit Logs

List user actions and configuration changes within this organization.

##### [List audit logs](/api/reference/go/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

client.Admin.Organization.AuditLogs.List(ctx, query) (\*ConversationCursorPage[[AdminOrganizationAuditLogListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20AdminOrganizationAuditLogListResponse%20%3E%20(schema))], error)

GET/organization/audit\_logs

#### OrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

client.Admin.Organization.AdminAPIKeys.List(ctx, query) (\*CursorPage[[AdminAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))], error)

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

client.Admin.Organization.AdminAPIKeys.New(ctx, body) (\*[AdminOrganizationAdminAPIKeyNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminOrganizationAdminAPIKeyNewResponse%20%3E%20(schema)), error)

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

client.Admin.Organization.AdminAPIKeys.Get(ctx, keyID) (\*[AdminAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)), error)

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

client.Admin.Organization.AdminAPIKeys.Delete(ctx, keyID) (\*[AdminOrganizationAdminAPIKeyDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminOrganizationAdminAPIKeyDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

type AdminAPIKey struct{…}

Represents an individual Admin API key in an org.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

Object OrganizationAdminAPIKey

The object type, which is always `organization.admin_api_key`

Owner AdminAPIKeyOwner

ID stringOptional

The identifier, which can be referenced in API endpoints

CreatedAt int64Optional

The Unix timestamp (in seconds) of when the user was created

formatunixtime

Name stringOptional

The name of the user

Object stringOptional

The object type, which is always organization.user

Role stringOptional

Always `owner`

Type stringOptional

Always `user`

RedactedValue string

The redacted value of the API key

LastUsedAt int64Optional

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

Name stringOptional

The name of the API key

#### OrganizationUsage

##### [Audio speeches](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

client.Admin.Organization.Usage.AudioSpeeches(ctx, query) (\*[AdminOrganizationUsageAudioSpeechesResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageAudioSpeechesResponse%20%3E%20(schema)), error)

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

client.Admin.Organization.Usage.AudioTranscriptions(ctx, query) (\*[AdminOrganizationUsageAudioTranscriptionsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageAudioTranscriptionsResponse%20%3E%20(schema)), error)

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

client.Admin.Organization.Usage.CodeInterpreterSessions(ctx, query) (\*[AdminOrganizationUsageCodeInterpreterSessionsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageCodeInterpreterSessionsResponse%20%3E%20(schema)), error)

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/completions)

client.Admin.Organization.Usage.Completions(ctx, query) (\*[AdminOrganizationUsageCompletionsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageCompletionsResponse%20%3E%20(schema)), error)

GET/organization/usage/completions

##### [Embeddings](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

client.Admin.Organization.Usage.Embeddings(ctx, query) (\*[AdminOrganizationUsageEmbeddingsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageEmbeddingsResponse%20%3E%20(schema)), error)

GET/organization/usage/embeddings

##### [Images](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/images)

client.Admin.Organization.Usage.Images(ctx, query) (\*[AdminOrganizationUsageImagesResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageImagesResponse%20%3E%20(schema)), error)

GET/organization/usage/images

##### [Moderations](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/moderations)

client.Admin.Organization.Usage.Moderations(ctx, query) (\*[AdminOrganizationUsageModerationsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageModerationsResponse%20%3E%20(schema)), error)

GET/organization/usage/moderations

##### [Vector stores](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

client.Admin.Organization.Usage.VectorStores(ctx, query) (\*[AdminOrganizationUsageVectorStoresResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageVectorStoresResponse%20%3E%20(schema)), error)

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

client.Admin.Organization.Usage.FileSearchCalls(ctx, query) (\*[AdminOrganizationUsageFileSearchCallsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageFileSearchCallsResponse%20%3E%20(schema)), error)

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

client.Admin.Organization.Usage.WebSearchCalls(ctx, query) (\*[AdminOrganizationUsageWebSearchCallsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageWebSearchCallsResponse%20%3E%20(schema)), error)

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/costs)

client.Admin.Organization.Usage.Costs(ctx, query) (\*[AdminOrganizationUsageCostsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageCostsResponse%20%3E%20(schema)), error)

GET/organization/costs

#### OrganizationInvites

##### [List invites](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/list)

client.Admin.Organization.Invites.List(ctx, query) (\*ConversationCursorPage[[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))], error)

GET/organization/invites

##### [Create invite](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/create)

client.Admin.Organization.Invites.New(ctx, body) (\*[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)), error)

POST/organization/invites

##### [Retrieve invite](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

client.Admin.Organization.Invites.Get(ctx, inviteID) (\*[Invite](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)), error)

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/go/resources/admin/subresources/organization/subresources/invites/methods/delete)

client.Admin.Organization.Invites.Delete(ctx, inviteID) (\*[AdminOrganizationInviteDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20AdminOrganizationInviteDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

type Invite struct{…}

Represents an individual `invite` to the organization.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

Email string

The email address of the individual to whom the invite was sent

Object OrganizationInvite

The object type, which is always `organization.invite`

Projects []InviteProject

The projects that were granted membership upon acceptance of the invite.

ID string

Project’s public ID

Role string

Project membership role

One of the following:

const InviteProjectRoleMember InviteProjectRole = "member"

const InviteProjectRoleOwner InviteProjectRole = "owner"

Role InviteRole

`owner` or `reader`

One of the following:

const InviteRoleOwner InviteRole = "owner"

const InviteRoleReader InviteRole = "reader"

Status InviteStatus

`accepted`,`expired`, or `pending`

One of the following:

const InviteStatusAccepted InviteStatus = "accepted"

const InviteStatusExpired InviteStatus = "expired"

const InviteStatusPending InviteStatus = "pending"

AcceptedAt int64Optional

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

ExpiresAt int64Optional

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

#### OrganizationUsers

##### [List users](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/list)

client.Admin.Organization.Users.List(ctx, query) (\*ConversationCursorPage[[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))], error)

GET/organization/users

##### [Retrieve user](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/retrieve)

client.Admin.Organization.Users.Get(ctx, userID) (\*[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)), error)

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/update)

client.Admin.Organization.Users.Update(ctx, userID, body) (\*[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)), error)

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/delete)

client.Admin.Organization.Users.Delete(ctx, userID) (\*[AdminOrganizationUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20AdminOrganizationUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

type OrganizationUser struct{…}

Represents an individual `user` within an organization.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

Object OrganizationUser

The object type, which is always `organization.user`

APIKeyLastUsedAt int64Optional

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Created int64Optional

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

DeveloperPersona stringOptional

The developer persona metadata for the user.

Email stringOptional

The email address of the user

IsDefault boolOptional

Whether this is the organization’s default user.

IsScaleTierAuthorizedPurchaser boolOptional

Whether the user is an authorized purchaser for Scale Tier.

IsScimManaged boolOptional

Whether the user is managed through SCIM.

IsServiceAccount boolOptional

Whether the user is a service account.

Name stringOptional

The name of the user

Projects OrganizationUserProjectsOptional

Projects associated with the user, if included.

Data []OrganizationUserProjectsData

ID stringOptional

Name stringOptional

Role stringOptional

Object List

Role stringOptional

`owner` or `reader`

TechnicalLevel stringOptional

The technical level metadata for the user.

User OrganizationUserUserOptional

Nested user details.

ID string

Object User

Banned boolOptional

BannedAt int64Optional

formatunixtime

Email stringOptional

Enabled boolOptional

Name stringOptional

Picture stringOptional

#### OrganizationUsersRoles

##### [List user organization role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

client.Admin.Organization.Users.Roles.List(ctx, userID, query) (\*NextCursorPage[[AdminOrganizationUserRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleListResponse%20%3E%20(schema))], error)

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

client.Admin.Organization.Users.Roles.New(ctx, userID, body) (\*[AdminOrganizationUserRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleNewResponse%20%3E%20(schema)), error)

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

client.Admin.Organization.Users.Roles.Get(ctx, userID, roleID) (\*[AdminOrganizationUserRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleGetResponse%20%3E%20(schema)), error)

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

client.Admin.Organization.Users.Roles.Delete(ctx, userID, roleID) (\*[AdminOrganizationUserRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/users/{user\_id}/roles/{role\_id}

#### OrganizationGroups

##### [List groups](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/list)

client.Admin.Organization.Groups.List(ctx, query) (\*NextCursorPage[[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))], error)

GET/organization/groups

##### [Create group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/create)

client.Admin.Organization.Groups.New(ctx, body) (\*[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)), error)

POST/organization/groups

##### [Retrieve group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

client.Admin.Organization.Groups.Get(ctx, groupID) (\*[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/update)

client.Admin.Organization.Groups.Update(ctx, groupID, body) (\*[AdminOrganizationGroupUpdateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20AdminOrganizationGroupUpdateResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/delete)

client.Admin.Organization.Groups.Delete(ctx, groupID) (\*[AdminOrganizationGroupDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20AdminOrganizationGroupDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

type Group struct{…}

Details about an organization group.

ID string

Identifier for the group.

CreatedAt int64

Unix timestamp (in seconds) when the group was created.

formatunixtime

GroupType GroupGroupType

The type of the group.

One of the following:

const GroupGroupTypeGroup GroupGroupType = "group"

const GroupGroupTypeTenantGroup GroupGroupType = "tenant\_group"

IsScimManaged bool

Whether the group is managed through SCIM and controlled by your identity provider.

Name string

Display name of the group.

#### OrganizationGroupsUsers

##### [List group users](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

client.Admin.Organization.Groups.Users.List(ctx, groupID, query) (\*NextCursorPage[[OrganizationGroupUser](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))], error)

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

client.Admin.Organization.Groups.Users.New(ctx, groupID, body) (\*[AdminOrganizationGroupUserNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserNewResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

client.Admin.Organization.Groups.Users.Get(ctx, groupID, userID) (\*[AdminOrganizationGroupUserGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserGetResponse%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

client.Admin.Organization.Groups.Users.Delete(ctx, groupID, userID) (\*[AdminOrganizationGroupUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

type OrganizationGroupUser struct{…}

Represents an individual user returned when inspecting group membership.

ID string

The identifier, which can be referenced in API endpoints

Email string

The email address of the user.

Name string

The name of the user.

#### OrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

client.Admin.Organization.Groups.Roles.List(ctx, groupID, query) (\*NextCursorPage[[AdminOrganizationGroupRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleListResponse%20%3E%20(schema))], error)

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

client.Admin.Organization.Groups.Roles.New(ctx, groupID, body) (\*[AdminOrganizationGroupRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleNewResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

client.Admin.Organization.Groups.Roles.Get(ctx, groupID, roleID) (\*[AdminOrganizationGroupRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleGetResponse%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

client.Admin.Organization.Groups.Roles.Delete(ctx, groupID, roleID) (\*[AdminOrganizationGroupRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}/roles/{role\_id}

#### OrganizationRoles

##### [List organization roles](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/list)

client.Admin.Organization.Roles.List(ctx, query) (\*NextCursorPage[[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))], error)

GET/organization/roles

##### [Create organization role](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/create)

client.Admin.Organization.Roles.New(ctx, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/organization/roles

##### [Retrieve organization role](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

client.Admin.Organization.Roles.Get(ctx, roleID) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/update)

client.Admin.Organization.Roles.Update(ctx, roleID, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/go/resources/admin/subresources/organization/subresources/roles/methods/delete)

client.Admin.Organization.Roles.Delete(ctx, roleID) (\*[AdminOrganizationRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20AdminOrganizationRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

type Role struct{…}

Details about a role that can be assigned through the public Roles API.

ID string

Identifier for the role.

Description string

Optional description of the role.

Name string

Unique name for the role.

Object Role

Always `role`.

Permissions []string

Permissions granted by the role.

PredefinedRole bool

Whether the role is predefined and managed by OpenAI.

ResourceType string

Resource type the role is bound to (for example `api.organization` or `api.project`).

#### OrganizationData Retention

##### [Retrieve organization data retention](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

client.Admin.Organization.DataRetention.Get(ctx) (\*[OrganizationDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)), error)

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/go/resources/admin/subresources/organization/subresources/data_retention/methods/update)

client.Admin.Organization.DataRetention.Update(ctx, body) (\*[OrganizationDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)), error)

POST/organization/data\_retention

##### ModelsExpand Collapse

type OrganizationDataRetention struct{…}

Represents the organization’s data retention control setting.

Object OrganizationDataRetention

The object type, which is always `organization.data_retention`.

Type OrganizationDataRetentionType

The configured organization data retention type.

One of the following:

const OrganizationDataRetentionTypeZeroDataRetention OrganizationDataRetentionType = "zero\_data\_retention"

const OrganizationDataRetentionTypeModifiedAbuseMonitoring OrganizationDataRetentionType = "modified\_abuse\_monitoring"

const OrganizationDataRetentionTypeEnhancedZeroDataRetention OrganizationDataRetentionType = "enhanced\_zero\_data\_retention"

const OrganizationDataRetentionTypeEnhancedModifiedAbuseMonitoring OrganizationDataRetentionType = "enhanced\_modified\_abuse\_monitoring"

#### OrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

client.Admin.Organization.SpendAlerts.List(ctx, query) (\*ConversationCursorPage[[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))], error)

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

client.Admin.Organization.SpendAlerts.New(ctx, body) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

client.Admin.Organization.SpendAlerts.Get(ctx, alertID) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

client.Admin.Organization.SpendAlerts.Update(ctx, alertID, body) (\*[OrganizationSpendAlert](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)), error)

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/go/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

client.Admin.Organization.SpendAlerts.Delete(ctx, alertID) (\*[OrganizationSpendAlertDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)), error)

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

type OrganizationSpendAlert struct{…}

Represents a spend alert configured at the organization level.

ID string

The identifier, which can be referenced in API endpoints.

Currency OrganizationSpendAlertCurrency

The currency for the threshold amount.

Interval OrganizationSpendAlertInterval

The time interval for evaluating spend against the threshold.

NotificationChannel OrganizationSpendAlertNotificationChannel

Email notification settings for a spend alert.

Recipients []string

Email addresses that receive the spend alert notification.

Type Email

The notification channel type. Currently only `email` is supported.

SubjectPrefix stringOptional

Optional subject prefix for alert emails.

Object OrganizationSpendAlert

The object type, which is always `organization.spend_alert`.

ThresholdAmount int64

The alert threshold amount, in cents.

type OrganizationSpendAlertDeleted struct{…}

Confirmation payload returned after deleting an organization spend alert.

ID string

The deleted spend alert ID.

Deleted bool

Whether the spend alert was deleted.

Object OrganizationSpendAlertDeleted

Always `organization.spend_alert.deleted`.

#### OrganizationCertificates

##### [List organization certificates](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/list)

client.Admin.Organization.Certificates.List(ctx, query) (\*ConversationCursorPage[[AdminOrganizationCertificateListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateListResponse%20%3E%20(schema))], error)

GET/organization/certificates

##### [Upload certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/create)

client.Admin.Organization.Certificates.New(ctx, body) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

POST/organization/certificates

##### [Get certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

client.Admin.Organization.Certificates.Get(ctx, certificateID, query) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/update)

client.Admin.Organization.Certificates.Update(ctx, certificateID, body) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/delete)

client.Admin.Organization.Certificates.Delete(ctx, certificateID) (\*[AdminOrganizationCertificateDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/activate)

client.Admin.Organization.Certificates.Activate(ctx, body) (\*Page[[AdminOrganizationCertificateActivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateActivateResponse%20%3E%20(schema))], error)

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

client.Admin.Organization.Certificates.Deactivate(ctx, body) (\*Page[[AdminOrganizationCertificateDeactivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateDeactivateResponse%20%3E%20(schema))], error)

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

type Certificate struct{…}

Represents an individual `certificate` uploaded to the organization.

ID string

The identifier, which can be referenced in API endpoints

CertificateDetails CertificateCertificateDetails

Content stringOptional

The content of the certificate in PEM format.

ExpiresAt int64Optional

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

ValidAt int64Optional

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

Name string

The name of the certificate.

Object CertificateObject

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

const CertificateObjectCertificate CertificateObject = "certificate"

const CertificateObjectOrganizationCertificate CertificateObject = "organization.certificate"

const CertificateObjectOrganizationProjectCertificate CertificateObject = "organization.project.certificate"

Active boolOptional

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

#### OrganizationProjects

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

#### OrganizationProjectsUsers

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

#### OrganizationProjectsUsersRoles

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

#### OrganizationProjectsService Accounts

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

#### OrganizationProjectsAPI Keys

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

#### OrganizationProjectsRate Limits

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

#### OrganizationProjectsModel Permissions

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

#### OrganizationProjectsHosted Tool Permissions

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

#### OrganizationProjectsGroups

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

#### OrganizationProjectsGroupsRoles

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

#### OrganizationProjectsRoles

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

#### OrganizationProjectsData Retention

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

#### OrganizationProjectsSpend Alerts

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

#### OrganizationProjectsCertificates

##### [List project certificates](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

client.Admin.Organization.Projects.Certificates.List(ctx, projectID, query) (\*ConversationCursorPage[[AdminOrganizationProjectCertificateListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateListResponse%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

client.Admin.Organization.Projects.Certificates.Activate(ctx, projectID, body) (\*Page[[AdminOrganizationProjectCertificateActivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateActivateResponse%20%3E%20(schema))], error)

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

client.Admin.Organization.Projects.Certificates.Deactivate(ctx, projectID, body) (\*Page[[AdminOrganizationProjectCertificateDeactivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateDeactivateResponse%20%3E%20(schema))], error)

POST/organization/projects/{project\_id}/certificates/deactivate
