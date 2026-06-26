<!-- source: https://developers.openai.com/api/reference/java/resources/admin/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Admin

#### AdminOrganization

#### AdminOrganizationAudit Logs

List user actions and configuration changes within this organization.

##### [List audit logs](/api/reference/java/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

AuditLogListPage admin().organization().auditLogs().list(AuditLogListParamsparams = AuditLogListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/audit\_logs

#### AdminOrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

AdminApiKeyListPage admin().organization().adminApiKeys().list(AdminApiKeyListParamsparams = AdminApiKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

[AdminApiKeyCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminApiKeyCreateResponse%20%3E%20(schema)) admin().organization().adminApiKeys().create(AdminApiKeyCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

[AdminApiKey](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) admin().organization().adminApiKeys().retrieve(AdminApiKeyRetrieveParamsparams = AdminApiKeyRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

[AdminApiKeyDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminApiKeyDeleteResponse%20%3E%20(schema)) admin().organization().adminApiKeys().delete(AdminApiKeyDeleteParamsparams = AdminApiKeyDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

class AdminApiKey:

Represents an individual Admin API key in an org.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

JsonValue; object\_ "organization.admin\_api\_key"constant"organization.admin\_api\_key"constant

The object type, which is always `organization.admin_api_key`

Owner owner

Optional<String> id

The identifier, which can be referenced in API endpoints

Optional<Long> createdAt

The Unix timestamp (in seconds) of when the user was created

formatunixtime

Optional<String> name

The name of the user

Optional<String> object\_

The object type, which is always organization.user

Optional<String> role

Always `owner`

Optional<String> type

Always `user`

String redactedValue

The redacted value of the API key

Optional<Long> lastUsedAt

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

Optional<String> name

The name of the API key

#### AdminOrganizationUsage

##### [Audio speeches](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

[UsageAudioSpeechesResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageAudioSpeechesResponse%20%3E%20(schema)) admin().organization().usage().audioSpeeches(UsageAudioSpeechesParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

[UsageAudioTranscriptionsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageAudioTranscriptionsResponse%20%3E%20(schema)) admin().organization().usage().audioTranscriptions(UsageAudioTranscriptionsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

[UsageCodeInterpreterSessionsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageCodeInterpreterSessionsResponse%20%3E%20(schema)) admin().organization().usage().codeInterpreterSessions(UsageCodeInterpreterSessionsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/completions)

[UsageCompletionsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageCompletionsResponse%20%3E%20(schema)) admin().organization().usage().completions(UsageCompletionsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/completions

##### [Embeddings](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

[UsageEmbeddingsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageEmbeddingsResponse%20%3E%20(schema)) admin().organization().usage().embeddings(UsageEmbeddingsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/embeddings

##### [Images](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/images)

[UsageImagesResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageImagesResponse%20%3E%20(schema)) admin().organization().usage().images(UsageImagesParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/images

##### [Moderations](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/moderations)

[UsageModerationsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageModerationsResponse%20%3E%20(schema)) admin().organization().usage().moderations(UsageModerationsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/moderations

##### [Vector stores](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

[UsageVectorStoresResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageVectorStoresResponse%20%3E%20(schema)) admin().organization().usage().vectorStores(UsageVectorStoresParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

[UsageFileSearchCallsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageFileSearchCallsResponse%20%3E%20(schema)) admin().organization().usage().fileSearchCalls(UsageFileSearchCallsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

[UsageWebSearchCallsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageWebSearchCallsResponse%20%3E%20(schema)) admin().organization().usage().webSearchCalls(UsageWebSearchCallsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/costs)

[UsageCostsResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageCostsResponse%20%3E%20(schema)) admin().organization().usage().costs(UsageCostsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/costs

#### AdminOrganizationInvites

##### [List invites](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/list)

InviteListPage admin().organization().invites().list(InviteListParamsparams = InviteListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/invites

##### [Create invite](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/create)

[Invite](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) admin().organization().invites().create(InviteCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/invites

##### [Retrieve invite](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

[Invite](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) admin().organization().invites().retrieve(InviteRetrieveParamsparams = InviteRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/delete)

[InviteDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20InviteDeleteResponse%20%3E%20(schema)) admin().organization().invites().delete(InviteDeleteParamsparams = InviteDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

class Invite:

Represents an individual `invite` to the organization.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

String email

The email address of the individual to whom the invite was sent

JsonValue; object\_ "organization.invite"constant"organization.invite"constant

The object type, which is always `organization.invite`

List<Project> projects

The projects that were granted membership upon acceptance of the invite.

String id

Project’s public ID

Role role

Project membership role

One of the following:

MEMBER("member")

OWNER("owner")

Role role

`owner` or `reader`

One of the following:

OWNER("owner")

READER("reader")

Status status

`accepted`,`expired`, or `pending`

One of the following:

ACCEPTED("accepted")

EXPIRED("expired")

PENDING("pending")

Optional<Long> acceptedAt

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

#### AdminOrganizationUsers

##### [List users](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/list)

UserListPage admin().organization().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users

##### [Retrieve user](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/retrieve)

[OrganizationUser](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) admin().organization().users().retrieve(UserRetrieveParamsparams = UserRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/update)

[OrganizationUser](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) admin().organization().users().update(UserUpdateParamsparams = UserUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/delete)

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().users().delete(UserDeleteParamsparams = UserDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationUser:

Represents an individual `user` within an organization.

String id

The identifier, which can be referenced in API endpoints

long addedAt

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

JsonValue; object\_ "organization.user"constant"organization.user"constant

The object type, which is always `organization.user`

Optional<Long> apiKeyLastUsedAt

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Optional<Long> created

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

Optional<String> developerPersona

The developer persona metadata for the user.

Optional<String> email

The email address of the user

Optional<Boolean> isDefault

Whether this is the organization’s default user.

Optional<Boolean> isScaleTierAuthorizedPurchaser

Whether the user is an authorized purchaser for Scale Tier.

Optional<Boolean> isScimManaged

Whether the user is managed through SCIM.

Optional<Boolean> isServiceAccount

Whether the user is a service account.

Optional<String> name

The name of the user

Optional<Projects> projects

Projects associated with the user, if included.

List<Data> data

Optional<String> id

Optional<String> name

Optional<String> role

JsonValue; object\_ "list"constant"list"constant

Optional<String> role

`owner` or `reader`

Optional<String> technicalLevel

The technical level metadata for the user.

Optional<User> user

Nested user details.

String id

JsonValue; object\_ "user"constant"user"constant

Optional<Boolean> banned

Optional<Long> bannedAt

formatunixtime

Optional<String> email

Optional<Boolean> enabled

Optional<String> name

Optional<String> picture

#### AdminOrganizationUsersRoles

##### [List user organization role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

RoleListPage admin().organization().users().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().users().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().users().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().users().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/users/{user\_id}/roles/{role\_id}

#### AdminOrganizationGroups

##### [List groups](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/list)

GroupListPage admin().organization().groups().list(GroupListParamsparams = GroupListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups

##### [Create group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/create)

[Group](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) admin().organization().groups().create(GroupCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups

##### [Retrieve group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

[Group](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) admin().organization().groups().retrieve(GroupRetrieveParamsparams = GroupRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/update)

[GroupUpdateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20GroupUpdateResponse%20%3E%20(schema)) admin().organization().groups().update(GroupUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/delete)

[GroupDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20GroupDeleteResponse%20%3E%20(schema)) admin().organization().groups().delete(GroupDeleteParamsparams = GroupDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

class Group:

Details about an organization group.

String id

Identifier for the group.

long createdAt

Unix timestamp (in seconds) when the group was created.

formatunixtime

GroupType groupType

The type of the group.

One of the following:

GROUP("group")

TENANT\_GROUP("tenant\_group")

boolean isScimManaged

Whether the group is managed through SCIM and controlled by your identity provider.

String name

Display name of the group.

#### AdminOrganizationGroupsUsers

##### [List group users](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

UserListPage admin().organization().groups().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

[UserCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserCreateResponse%20%3E%20(schema)) admin().organization().groups().users().create(UserCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

[UserRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserRetrieveResponse%20%3E%20(schema)) admin().organization().groups().users().retrieve(UserRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().groups().users().delete(UserDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationGroupUser:

Represents an individual user returned when inspecting group membership.

String id

The identifier, which can be referenced in API endpoints

Optional<String> email

The email address of the user.

String name

The name of the user.

#### AdminOrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

RoleListPage admin().organization().groups().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().groups().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().groups().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().groups().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}/roles/{role\_id}

#### AdminOrganizationRoles

##### [List organization roles](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/list)

RoleListPage admin().organization().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/roles

##### [Create organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/create)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/roles

##### [Retrieve organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().retrieve(RoleRetrieveParamsparams = RoleRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/update)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().update(RoleUpdateParamsparams = RoleUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().roles().delete(RoleDeleteParamsparams = RoleDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

class Role:

Details about a role that can be assigned through the public Roles API.

String id

Identifier for the role.

Optional<String> description

Optional description of the role.

String name

Unique name for the role.

JsonValue; object\_ "role"constant"role"constant

Always `role`.

List<String> permissions

Permissions granted by the role.

boolean predefinedRole

Whether the role is predefined and managed by OpenAI.

String resourceType

Resource type the role is bound to (for example `api.organization` or `api.project`).

#### AdminOrganizationData Retention

##### [Retrieve organization data retention](/api/reference/java/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

[OrganizationDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) admin().organization().dataRetention().retrieve(DataRetentionRetrieveParamsparams = DataRetentionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/java/resources/admin/subresources/organization/subresources/data_retention/methods/update)

[OrganizationDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) admin().organization().dataRetention().update(DataRetentionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/data\_retention

##### ModelsExpand Collapse

class OrganizationDataRetention:

Represents the organization’s data retention control setting.

JsonValue; object\_ "organization.data\_retention"constant"organization.data\_retention"constant

The object type, which is always `organization.data_retention`.

Type type

The configured organization data retention type.

One of the following:

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")

#### AdminOrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

SpendAlertListPage admin().organization().spendAlerts().list(SpendAlertListParamsparams = SpendAlertListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().create(SpendAlertCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().retrieve(SpendAlertRetrieveParamsparams = SpendAlertRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

[OrganizationSpendAlert](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) admin().organization().spendAlerts().update(SpendAlertUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/java/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

[OrganizationSpendAlertDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) admin().organization().spendAlerts().delete(SpendAlertDeleteParamsparams = SpendAlertDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class OrganizationSpendAlert:

Represents a spend alert configured at the organization level.

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

JsonValue; object\_ "organization.spend\_alert"constant"organization.spend\_alert"constant

The object type, which is always `organization.spend_alert`.

long thresholdAmount

The alert threshold amount, in cents.

class OrganizationSpendAlertDeleted:

Confirmation payload returned after deleting an organization spend alert.

String id

The deleted spend alert ID.

boolean deleted

Whether the spend alert was deleted.

JsonValue; object\_ "organization.spend\_alert.deleted"constant"organization.spend\_alert.deleted"constant

Always `organization.spend_alert.deleted`.

#### AdminOrganizationCertificates

##### [List organization certificates](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/list)

CertificateListPage admin().organization().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/certificates

##### [Upload certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/create)

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().create(CertificateCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates

##### [Get certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().retrieve(CertificateRetrieveParamsparams = CertificateRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/update)

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().update(CertificateUpdateParamsparams = CertificateUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/delete)

[CertificateDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20CertificateDeleteResponse%20%3E%20(schema)) admin().organization().certificates().delete(CertificateDeleteParamsparams = CertificateDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/activate)

CertificateActivatePage admin().organization().certificates().activate(CertificateActivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

CertificateDeactivatePage admin().organization().certificates().deactivate(CertificateDeactivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

class Certificate:

Represents an individual `certificate` uploaded to the organization.

String id

The identifier, which can be referenced in API endpoints

CertificateDetails certificateDetails

Optional<String> content

The content of the certificate in PEM format.

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

Optional<Long> validAt

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

long createdAt

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

Optional<String> name

The name of the certificate.

Object object\_

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

CERTIFICATE("certificate")

ORGANIZATION\_CERTIFICATE("organization.certificate")

ORGANIZATION\_PROJECT\_CERTIFICATE("organization.project.certificate")

Optional<Boolean> active

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

#### AdminOrganizationProjects

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

#### AdminOrganizationProjectsUsers

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

#### AdminOrganizationProjectsUsersRoles

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

#### AdminOrganizationProjectsService Accounts

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

#### AdminOrganizationProjectsAPI Keys

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

#### AdminOrganizationProjectsRate Limits

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

#### AdminOrganizationProjectsModel Permissions

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

#### AdminOrganizationProjectsHosted Tool Permissions

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

#### AdminOrganizationProjectsGroups

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

#### AdminOrganizationProjectsGroupsRoles

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

#### AdminOrganizationProjectsRoles

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

#### AdminOrganizationProjectsData Retention

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

#### AdminOrganizationProjectsSpend Alerts

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

#### AdminOrganizationProjectsCertificates

##### [List project certificates](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

CertificateListPage admin().organization().projects().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

CertificateActivatePage admin().organization().projects().certificates().activate(CertificateActivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

CertificateDeactivatePage admin().organization().projects().certificates().deactivate(CertificateDeactivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/certificates/deactivate
