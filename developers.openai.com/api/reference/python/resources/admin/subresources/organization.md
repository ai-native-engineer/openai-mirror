<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

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

##### [List audit logs](/api/reference/python/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

admin.organization.audit\_logs.list(AuditLogListParams\*\*kwargs)  -> SyncConversationCursorPage[[AuditLogListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema))]

GET/organization/audit\_logs

##### ModelsExpand Collapse

class AuditLogListResponse: …

A log of a user action or configuration change within this organization.

id: str

The ID of this log.

effective\_at: int

The Unix timestamp (in seconds) of the event.

formatunixtime

type: Literal["api\_key.created", "api\_key.updated", "api\_key.deleted", 56 more]

The event type.

One of the following:

"api\_key.created"

"api\_key.updated"

"api\_key.deleted"

"certificate.created"

"certificate.updated"

"certificate.deleted"

"certificates.activated"

"certificates.deactivated"

"checkpoint.permission.created"

"checkpoint.permission.deleted"

"external\_key.registered"

"external\_key.removed"

"group.created"

"group.updated"

"group.deleted"

"invite.sent"

"invite.accepted"

"invite.deleted"

"ip\_allowlist.created"

"ip\_allowlist.updated"

"ip\_allowlist.deleted"

"ip\_allowlist.config.activated"

"ip\_allowlist.config.deactivated"

"login.succeeded"

"login.failed"

"logout.succeeded"

"logout.failed"

"organization.updated"

"project.created"

"project.updated"

"project.archived"

"project.deleted"

"rate\_limit.updated"

"rate\_limit.deleted"

"resource.deleted"

"tunnel.created"

"tunnel.updated"

"tunnel.deleted"

"workload\_identity\_provider.created"

"workload\_identity\_provider.updated"

"workload\_identity\_provider.deleted"

"workload\_identity\_provider\_mapping.created"

"workload\_identity\_provider\_mapping.updated"

"workload\_identity\_provider\_mapping.deleted"

"role.created"

"role.updated"

"role.deleted"

"role.assignment.created"

"role.assignment.deleted"

"role.bound\_to\_resource"

"role.unbound\_from\_resource"

"scim.enabled"

"scim.disabled"

"service\_account.created"

"service\_account.updated"

"service\_account.deleted"

"user.added"

"user.updated"

"user.deleted"

actor: Optional[Actor]

The actor who performed the audit logged action.

api\_key: Optional[ActorAPIKey]

The API Key used to perform the audit logged action.

id: Optional[str]

The tracking id of the API key.

service\_account: Optional[ActorAPIKeyServiceAccount]

The service account that performed the audit logged action.

id: Optional[str]

The service account id.

type: Optional[Literal["user", "service\_account"]]

The type of API key. Can be either `user` or `service_account`.

One of the following:

"user"

"service\_account"

user: Optional[ActorAPIKeyUser]

The user who performed the audit logged action.

id: Optional[str]

The user id.

email: Optional[str]

The user email.

session: Optional[ActorSession]

The session in which the audit logged action was performed.

ip\_address: Optional[str]

The IP address from which the action was performed.

user: Optional[ActorSessionUser]

The user who performed the audit logged action.

id: Optional[str]

The user id.

email: Optional[str]

The user email.

type: Optional[Literal["session", "api\_key"]]

The type of actor. Is either `session` or `api_key`.

One of the following:

"session"

"api\_key"

api\_key\_created: Optional[APIKeyCreated]

The details for events with this `type`.

id: Optional[str]

The tracking ID of the API key.

data: Optional[APIKeyCreatedData]

The payload used to create the API key.

scopes: Optional[List[str]]

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

api\_key\_deleted: Optional[APIKeyDeleted]

The details for events with this `type`.

id: Optional[str]

The tracking ID of the API key.

api\_key\_updated: Optional[APIKeyUpdated]

The details for events with this `type`.

id: Optional[str]

The tracking ID of the API key.

changes\_requested: Optional[APIKeyUpdatedChangesRequested]

The payload used to update the API key.

scopes: Optional[List[str]]

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

certificate\_created: Optional[CertificateCreated]

The details for events with this `type`.

id: Optional[str]

The certificate ID.

name: Optional[str]

The name of the certificate.

certificate\_deleted: Optional[CertificateDeleted]

The details for events with this `type`.

id: Optional[str]

The certificate ID.

certificate: Optional[str]

The certificate content in PEM format.

name: Optional[str]

The name of the certificate.

certificate\_updated: Optional[CertificateUpdated]

The details for events with this `type`.

id: Optional[str]

The certificate ID.

name: Optional[str]

The name of the certificate.

certificates\_activated: Optional[CertificatesActivated]

The details for events with this `type`.

certificates: Optional[List[CertificatesActivatedCertificate]]

id: Optional[str]

The certificate ID.

name: Optional[str]

The name of the certificate.

certificates\_deactivated: Optional[CertificatesDeactivated]

The details for events with this `type`.

certificates: Optional[List[CertificatesDeactivatedCertificate]]

id: Optional[str]

The certificate ID.

name: Optional[str]

The name of the certificate.

checkpoint\_permission\_created: Optional[CheckpointPermissionCreated]

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

id: Optional[str]

The ID of the checkpoint permission.

data: Optional[CheckpointPermissionCreatedData]

The payload used to create the checkpoint permission.

fine\_tuned\_model\_checkpoint: Optional[str]

The ID of the fine-tuned model checkpoint.

project\_id: Optional[str]

The ID of the project that the checkpoint permission was created for.

checkpoint\_permission\_deleted: Optional[CheckpointPermissionDeleted]

The details for events with this `type`.

id: Optional[str]

The ID of the checkpoint permission.

external\_key\_registered: Optional[ExternalKeyRegistered]

The details for events with this `type`.

id: Optional[str]

The ID of the external key configuration.

data: Optional[object]

The configuration for the external key.

external\_key\_removed: Optional[ExternalKeyRemoved]

The details for events with this `type`.

id: Optional[str]

The ID of the external key configuration.

group\_created: Optional[GroupCreated]

The details for events with this `type`.

id: Optional[str]

The ID of the group.

data: Optional[GroupCreatedData]

Information about the created group.

group\_name: Optional[str]

The group name.

group\_deleted: Optional[GroupDeleted]

The details for events with this `type`.

id: Optional[str]

The ID of the group.

group\_updated: Optional[GroupUpdated]

The details for events with this `type`.

id: Optional[str]

The ID of the group.

changes\_requested: Optional[GroupUpdatedChangesRequested]

The payload used to update the group.

group\_name: Optional[str]

The updated group name.

invite\_accepted: Optional[InviteAccepted]

The details for events with this `type`.

id: Optional[str]

The ID of the invite.

invite\_deleted: Optional[InviteDeleted]

The details for events with this `type`.

id: Optional[str]

The ID of the invite.

invite\_sent: Optional[InviteSent]

The details for events with this `type`.

id: Optional[str]

The ID of the invite.

data: Optional[InviteSentData]

The payload used to create the invite.

email: Optional[str]

The email invited to the organization.

role: Optional[str]

The role the email was invited to be. Is either `owner` or `member`.

ip\_allowlist\_config\_activated: Optional[IPAllowlistConfigActivated]

The details for events with this `type`.

configs: Optional[List[IPAllowlistConfigActivatedConfig]]

The configurations that were activated.

id: Optional[str]

The ID of the IP allowlist configuration.

name: Optional[str]

The name of the IP allowlist configuration.

ip\_allowlist\_config\_deactivated: Optional[IPAllowlistConfigDeactivated]

The details for events with this `type`.

configs: Optional[List[IPAllowlistConfigDeactivatedConfig]]

The configurations that were deactivated.

id: Optional[str]

The ID of the IP allowlist configuration.

name: Optional[str]

The name of the IP allowlist configuration.

ip\_allowlist\_created: Optional[IPAllowlistCreated]

The details for events with this `type`.

id: Optional[str]

The ID of the IP allowlist configuration.

allowed\_ips: Optional[List[str]]

The IP addresses or CIDR ranges included in the configuration.

name: Optional[str]

The name of the IP allowlist configuration.

ip\_allowlist\_deleted: Optional[IPAllowlistDeleted]

The details for events with this `type`.

id: Optional[str]

The ID of the IP allowlist configuration.

allowed\_ips: Optional[List[str]]

The IP addresses or CIDR ranges that were in the configuration.

name: Optional[str]

The name of the IP allowlist configuration.

ip\_allowlist\_updated: Optional[IPAllowlistUpdated]

The details for events with this `type`.

id: Optional[str]

The ID of the IP allowlist configuration.

allowed\_ips: Optional[List[str]]

The updated set of IP addresses or CIDR ranges in the configuration.

login\_failed: Optional[LoginFailed]

The details for events with this `type`.

error\_code: Optional[str]

The error code of the failure.

error\_message: Optional[str]

The error message of the failure.

login\_succeeded: Optional[object]

This event has no additional fields beyond the standard audit log attributes.

logout\_failed: Optional[LogoutFailed]

The details for events with this `type`.

error\_code: Optional[str]

The error code of the failure.

error\_message: Optional[str]

The error message of the failure.

logout\_succeeded: Optional[object]

This event has no additional fields beyond the standard audit log attributes.

organization\_updated: Optional[OrganizationUpdated]

The details for events with this `type`.

id: Optional[str]

The organization ID.

changes\_requested: Optional[OrganizationUpdatedChangesRequested]

The payload used to update the organization settings.

api\_call\_logging: Optional[str]

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

api\_call\_logging\_project\_ids: Optional[str]

The list of project ids if api\_call\_logging is set to `enabled_for_selected_projects`

description: Optional[str]

The organization description.

name: Optional[str]

The organization name.

threads\_ui\_visibility: Optional[str]

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

title: Optional[str]

The organization title.

usage\_dashboard\_visibility: Optional[str]

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

project: Optional[Project]

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

id: Optional[str]

The project ID.

name: Optional[str]

The project title.

project\_archived: Optional[ProjectArchived]

The details for events with this `type`.

id: Optional[str]

The project ID.

project\_created: Optional[ProjectCreated]

The details for events with this `type`.

id: Optional[str]

The project ID.

data: Optional[ProjectCreatedData]

The payload used to create the project.

name: Optional[str]

The project name.

title: Optional[str]

The title of the project as seen on the dashboard.

project\_deleted: Optional[ProjectDeleted]

The details for events with this `type`.

id: Optional[str]

The project ID.

project\_updated: Optional[ProjectUpdated]

The details for events with this `type`.

id: Optional[str]

The project ID.

changes\_requested: Optional[ProjectUpdatedChangesRequested]

The payload used to update the project.

title: Optional[str]

The title of the project as seen on the dashboard.

rate\_limit\_deleted: Optional[RateLimitDeleted]

The details for events with this `type`.

id: Optional[str]

The rate limit ID

rate\_limit\_updated: Optional[RateLimitUpdated]

The details for events with this `type`.

id: Optional[str]

The rate limit ID

changes\_requested: Optional[RateLimitUpdatedChangesRequested]

The payload used to update the rate limits.

batch\_1\_day\_max\_input\_tokens: Optional[int]

The maximum batch input tokens per day. Only relevant for certain models.

max\_audio\_megabytes\_per\_1\_minute: Optional[int]

The maximum audio megabytes per minute. Only relevant for certain models.

max\_images\_per\_1\_minute: Optional[int]

The maximum images per minute. Only relevant for certain models.

max\_requests\_per\_1\_day: Optional[int]

The maximum requests per day. Only relevant for certain models.

max\_requests\_per\_1\_minute: Optional[int]

The maximum requests per minute.

max\_tokens\_per\_1\_minute: Optional[int]

The maximum tokens per minute.

role\_assignment\_created: Optional[RoleAssignmentCreated]

The details for events with this `type`.

id: Optional[str]

The identifier of the role assignment.

principal\_id: Optional[str]

The principal (user or group) that received the role.

principal\_type: Optional[str]

The type of principal (user or group) that received the role.

resource\_id: Optional[str]

The resource the role assignment is scoped to.

resource\_type: Optional[str]

The type of resource the role assignment is scoped to.

role\_assignment\_deleted: Optional[RoleAssignmentDeleted]

The details for events with this `type`.

id: Optional[str]

The identifier of the role assignment.

principal\_id: Optional[str]

The principal (user or group) that had the role removed.

principal\_type: Optional[str]

The type of principal (user or group) that had the role removed.

resource\_id: Optional[str]

The resource the role assignment was scoped to.

resource\_type: Optional[str]

The type of resource the role assignment was scoped to.

role\_bound\_to\_resource: Optional[RoleBoundToResource]

The details for events with this `type`.

id: Optional[str]

The ID of the resource the role was bound to. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id: Optional[str]

The connector ID for a ChatGPT workspace connector resource.

connector\_name: Optional[str]

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled: Optional[bool]

Whether the connector is enabled for the role.

permissions: Optional[List[str]]

The permissions granted to the role for the resource.

resource\_id: Optional[str]

The ID of the resource the role was bound to.

resource\_type: Optional[str]

The type of resource the role was bound to.

role\_id: Optional[str]

The ID of the role that was bound to the resource.

source: Optional[Literal["role\_toggle", "role\_connector\_update", "role\_delete", 2 more]]

The connector role mutation path that produced the event.

One of the following:

"role\_toggle"

"role\_connector\_update"

"role\_delete"

"workspace\_permissions"

"connector\_publish"

workspace\_id: Optional[str]

The workspace ID for a ChatGPT workspace connector resource.

role\_created: Optional[RoleCreated]

The details for events with this `type`.

id: Optional[str]

The role ID.

permissions: Optional[List[str]]

The permissions granted by the role.

resource\_id: Optional[str]

The resource the role is scoped to.

resource\_type: Optional[str]

The type of resource the role belongs to.

role\_name: Optional[str]

The name of the role.

role\_deleted: Optional[RoleDeleted]

The details for events with this `type`.

id: Optional[str]

The role ID.

role\_unbound\_from\_resource: Optional[RoleUnboundFromResource]

The details for events with this `type`.

id: Optional[str]

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id: Optional[str]

The connector ID for a ChatGPT workspace connector resource.

connector\_name: Optional[str]

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled: Optional[bool]

Whether the connector is enabled for the role.

permissions: Optional[List[str]]

The permissions remaining for the role after the change.

resource\_id: Optional[str]

The ID of the resource the role was unbound from.

resource\_type: Optional[str]

The type of resource the role was unbound from.

role\_id: Optional[str]

The ID of the role that was unbound from the resource.

source: Optional[Literal["role\_toggle", "role\_connector\_update", "role\_delete", 2 more]]

The connector role mutation path that produced the event.

One of the following:

"role\_toggle"

"role\_connector\_update"

"role\_delete"

"workspace\_permissions"

"connector\_publish"

workspace\_id: Optional[str]

The workspace ID for a ChatGPT workspace connector resource.

role\_updated: Optional[RoleUpdated]

The details for events with this `type`.

id: Optional[str]

The role ID.

changes\_requested: Optional[RoleUpdatedChangesRequested]

The payload used to update the role.

description: Optional[str]

The updated role description, when provided.

metadata: Optional[object]

Additional metadata stored on the role.

permissions\_added: Optional[List[str]]

The permissions added to the role.

permissions\_removed: Optional[List[str]]

The permissions removed from the role.

resource\_id: Optional[str]

The resource the role is scoped to.

resource\_type: Optional[str]

The type of resource the role belongs to.

role\_name: Optional[str]

The updated role name, when provided.

scim\_disabled: Optional[ScimDisabled]

The details for events with this `type`.

id: Optional[str]

The ID of the SCIM was disabled for.

scim\_enabled: Optional[ScimEnabled]

The details for events with this `type`.

id: Optional[str]

The ID of the SCIM was enabled for.

service\_account\_created: Optional[ServiceAccountCreated]

The details for events with this `type`.

id: Optional[str]

The service account ID.

data: Optional[ServiceAccountCreatedData]

The payload used to create the service account.

role: Optional[str]

The role of the service account. Is either `owner` or `member`.

service\_account\_deleted: Optional[ServiceAccountDeleted]

The details for events with this `type`.

id: Optional[str]

The service account ID.

service\_account\_updated: Optional[ServiceAccountUpdated]

The details for events with this `type`.

id: Optional[str]

The service account ID.

changes\_requested: Optional[ServiceAccountUpdatedChangesRequested]

The payload used to updated the service account.

role: Optional[str]

The role of the service account. Is either `owner` or `member`.

user\_added: Optional[UserAdded]

The details for events with this `type`.

id: Optional[str]

The user ID.

data: Optional[UserAddedData]

The payload used to add the user to the project.

role: Optional[str]

The role of the user. Is either `owner` or `member`.

user\_deleted: Optional[UserDeleted]

The details for events with this `type`.

id: Optional[str]

The user ID.

user\_updated: Optional[UserUpdated]

The details for events with this `type`.

id: Optional[str]

The project ID.

changes\_requested: Optional[UserUpdatedChangesRequested]

The payload used to update the user.

role: Optional[str]

The role of the user. Is either `owner` or `member`.

workload\_identity\_provider\_mapping\_created: Optional[WorkloadIdentityProviderMappingCreated]

The details for events with this `type`.

id: Optional[str]

The workload identity provider mapping ID.

data: Optional[object]

The payload used to create the workload identity provider mapping.

identity\_provider\_id: Optional[str]

The workload identity provider ID.

workload\_identity\_provider\_mapping\_deleted: Optional[WorkloadIdentityProviderMappingDeleted]

The details for events with this `type`.

id: Optional[str]

The workload identity provider mapping ID.

identity\_provider\_id: Optional[str]

The workload identity provider ID.

project\_id: Optional[str]

The project ID.

service\_account\_id: Optional[str]

The mapped service account ID.

workload\_identity\_provider\_mapping\_updated: Optional[WorkloadIdentityProviderMappingUpdated]

The details for events with this `type`.

id: Optional[str]

The workload identity provider mapping ID.

changes\_requested: Optional[object]

The payload used to update the workload identity provider mapping.

identity\_provider\_id: Optional[str]

The workload identity provider ID.

workload\_identity\_provider\_created: Optional[WorkloadIdentityProviderCreated]

The details for events with this `type`.

id: Optional[str]

The workload identity provider ID.

data: Optional[object]

The payload used to create the workload identity provider.

workload\_identity\_provider\_deleted: Optional[WorkloadIdentityProviderDeleted]

The details for events with this `type`.

id: Optional[str]

The workload identity provider ID.

name: Optional[str]

The workload identity provider name.

workload\_identity\_provider\_updated: Optional[WorkloadIdentityProviderUpdated]

The details for events with this `type`.

id: Optional[str]

The workload identity provider ID.

changes\_requested: Optional[object]

The payload used to update the workload identity provider.

#### OrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

admin.organization.admin\_api\_keys.list(AdminAPIKeyListParams\*\*kwargs)  -> SyncCursorPage[[AdminAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))]

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

admin.organization.admin\_api\_keys.create(AdminAPIKeyCreateParams\*\*kwargs)  -> [AdminAPIKeyCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema))

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

admin.organization.admin\_api\_keys.retrieve(strkey\_id)  -> [AdminAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

admin.organization.admin\_api\_keys.delete(strkey\_id)  -> [AdminAPIKeyDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema))

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

class AdminAPIKey: …

Represents an individual Admin API key in an org.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: Literal["organization.admin\_api\_key"]

The object type, which is always `organization.admin_api_key`

owner: Owner

id: Optional[str]

The identifier, which can be referenced in API endpoints

created\_at: Optional[int]

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: Optional[str]

The name of the user

object: Optional[str]

The object type, which is always organization.user

role: Optional[str]

Always `owner`

type: Optional[str]

Always `user`

redacted\_value: str

The redacted value of the API key

last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: Optional[str]

The name of the API key

class AdminAPIKeyCreateResponse: …

Represents an individual Admin API key in an org.

value: str

The value of the API key. Only shown on create.

class AdminAPIKeyDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.admin\_api\_key.deleted"]

#### OrganizationUsage

##### [Audio speeches](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

admin.organization.usage.audio\_speeches(UsageAudioSpeechesParams\*\*kwargs)  -> [UsageAudioSpeechesResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema))

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

admin.organization.usage.audio\_transcriptions(UsageAudioTranscriptionsParams\*\*kwargs)  -> [UsageAudioTranscriptionsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema))

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

admin.organization.usage.code\_interpreter\_sessions(UsageCodeInterpreterSessionsParams\*\*kwargs)  -> [UsageCodeInterpreterSessionsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema))

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/completions)

admin.organization.usage.completions(UsageCompletionsParams\*\*kwargs)  -> [UsageCompletionsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema))

GET/organization/usage/completions

##### [Embeddings](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

admin.organization.usage.embeddings(UsageEmbeddingsParams\*\*kwargs)  -> [UsageEmbeddingsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema))

GET/organization/usage/embeddings

##### [Images](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/images)

admin.organization.usage.images(UsageImagesParams\*\*kwargs)  -> [UsageImagesResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema))

GET/organization/usage/images

##### [Moderations](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/moderations)

admin.organization.usage.moderations(UsageModerationsParams\*\*kwargs)  -> [UsageModerationsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_moderations_response%20%3E%20(schema))

GET/organization/usage/moderations

##### [Vector stores](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

admin.organization.usage.vector\_stores(UsageVectorStoresParams\*\*kwargs)  -> [UsageVectorStoresResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_vector_stores_response%20%3E%20(schema))

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

admin.organization.usage.file\_search\_calls(UsageFileSearchCallsParams\*\*kwargs)  -> [UsageFileSearchCallsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_file_search_calls_response%20%3E%20(schema))

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

admin.organization.usage.web\_search\_calls(UsageWebSearchCallsParams\*\*kwargs)  -> [UsageWebSearchCallsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_web_search_calls_response%20%3E%20(schema))

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/costs)

admin.organization.usage.costs(UsageCostsParams\*\*kwargs)  -> [UsageCostsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_costs_response%20%3E%20(schema))

GET/organization/costs

##### ModelsExpand Collapse

class UsageAudioSpeechesResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageAudioTranscriptionsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageCodeInterpreterSessionsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageCompletionsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageEmbeddingsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageImagesResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageModerationsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageVectorStoresResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageFileSearchCallsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageWebSearchCallsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

class UsageCostsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

#### OrganizationInvites

##### [List invites](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/list)

admin.organization.invites.list(InviteListParams\*\*kwargs)  -> SyncConversationCursorPage[[Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))]

GET/organization/invites

##### [Create invite](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/create)

admin.organization.invites.create(InviteCreateParams\*\*kwargs)  -> [Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))

POST/organization/invites

##### [Retrieve invite](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

admin.organization.invites.retrieve(strinvite\_id)  -> [Invite](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema))

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/python/resources/admin/subresources/organization/subresources/invites/methods/delete)

admin.organization.invites.delete(strinvite\_id)  -> [InviteDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema))

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

class Invite: …

Represents an individual `invite` to the organization.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: str

The email address of the individual to whom the invite was sent

object: Literal["organization.invite"]

The object type, which is always `organization.invite`

projects: List[Project]

The projects that were granted membership upon acceptance of the invite.

id: str

Project’s public ID

role: Literal["member", "owner"]

Project membership role

One of the following:

"member"

"owner"

role: Literal["owner", "reader"]

`owner` or `reader`

One of the following:

"owner"

"reader"

status: Literal["accepted", "expired", "pending"]

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at: Optional[int]

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

class InviteDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.invite.deleted"]

The object type, which is always `organization.invite.deleted`

#### OrganizationUsers

##### [List users](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/list)

admin.organization.users.list(UserListParams\*\*kwargs)  -> SyncConversationCursorPage[[OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))]

GET/organization/users

##### [Retrieve user](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/retrieve)

admin.organization.users.retrieve(struser\_id)  -> [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/update)

admin.organization.users.update(struser\_id, UserUpdateParams\*\*kwargs)  -> [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/delete)

admin.organization.users.delete(struser\_id)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationUser: …

Represents an individual `user` within an organization.

id: str

The identifier, which can be referenced in API endpoints

added\_at: int

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: Literal["organization.user"]

The object type, which is always `organization.user`

api\_key\_last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: Optional[int]

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: Optional[str]

The developer persona metadata for the user.

email: Optional[str]

The email address of the user

is\_default: Optional[bool]

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: Optional[bool]

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: Optional[bool]

Whether the user is managed through SCIM.

is\_service\_account: Optional[bool]

Whether the user is a service account.

name: Optional[str]

The name of the user

projects: Optional[Projects]

Projects associated with the user, if included.

data: List[ProjectsData]

id: Optional[str]

name: Optional[str]

role: Optional[str]

object: Literal["list"]

role: Optional[str]

`owner` or `reader`

technical\_level: Optional[str]

The technical level metadata for the user.

user: Optional[User]

Nested user details.

id: str

object: Literal["user"]

banned: Optional[bool]

banned\_at: Optional[int]

formatunixtime

email: Optional[str]

enabled: Optional[bool]

name: Optional[str]

picture: Optional[str]

class UserDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.user.deleted"]

#### OrganizationUsersRoles

##### [List user organization role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

admin.organization.users.roles.list(struser\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

admin.organization.users.roles.create(struser\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

admin.organization.users.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

admin.organization.users.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/users/{user\_id}/roles/{role\_id}

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

#### OrganizationGroups

##### [List groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/list)

admin.organization.groups.list(GroupListParams\*\*kwargs)  -> SyncNextCursorPage[[Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))]

GET/organization/groups

##### [Create group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/create)

admin.organization.groups.create(GroupCreateParams\*\*kwargs)  -> [Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

POST/organization/groups

##### [Retrieve group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

admin.organization.groups.retrieve(strgroup\_id)  -> [Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/update)

admin.organization.groups.update(strgroup\_id, GroupUpdateParams\*\*kwargs)  -> [GroupUpdateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema))

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/delete)

admin.organization.groups.delete(strgroup\_id)  -> [GroupDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

class Group: …

Details about an organization group.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: Literal["group", "tenant\_group"]

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: str

Display name of the group.

class GroupUpdateResponse: …

Response returned after updating a group.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: str

Updated display name for the group.

class GroupDeleteResponse: …

Confirmation payload returned after deleting a group.

id: str

Identifier of the deleted group.

deleted: bool

Whether the group was deleted.

object: Literal["group.deleted"]

Always `group.deleted`.

#### OrganizationGroupsUsers

##### [List group users](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

admin.organization.groups.users.list(strgroup\_id, UserListParams\*\*kwargs)  -> SyncNextCursorPage[[OrganizationGroupUser](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))]

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

admin.organization.groups.users.create(strgroup\_id, UserCreateParams\*\*kwargs)  -> [UserCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema))

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

admin.organization.groups.users.retrieve(struser\_id, UserRetrieveParams\*\*kwargs)  -> [UserRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema))

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

admin.organization.groups.users.delete(struser\_id, UserDeleteParams\*\*kwargs)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationGroupUser: …

Represents an individual user returned when inspecting group membership.

id: str

The identifier, which can be referenced in API endpoints

email: Optional[str]

The email address of the user.

name: str

The name of the user.

class UserCreateResponse: …

Confirmation payload returned after adding a user to a group.

group\_id: str

Identifier of the group the user was added to.

object: Literal["group.user"]

Always `group.user`.

user\_id: str

Identifier of the user that was added.

class UserRetrieveResponse: …

Details about a user returned from an organization group membership lookup.

id: str

Identifier for the user.

email: Optional[str]

Email address of the user, or `null` for users without an email.

is\_service\_account: Optional[bool]

Whether the user is a service account.

name: str

Display name of the user.

picture: Optional[str]

URL of the user’s profile picture, if available.

user\_type: Literal["user", "tenant\_user"]

The type of user.

One of the following:

"user"

"tenant\_user"

class UserDeleteResponse: …

Confirmation payload returned after removing a user from a group.

deleted: bool

Whether the group membership was removed.

object: Literal["group.user.deleted"]

Always `group.user.deleted`.

#### OrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

admin.organization.groups.roles.list(strgroup\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

admin.organization.groups.roles.create(strgroup\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.groups.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

admin.organization.groups.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/roles/{role\_id}

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

#### OrganizationRoles

##### [List organization roles](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/list)

admin.organization.roles.list(RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))]

GET/organization/roles

##### [Create organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/create)

admin.organization.roles.create(RoleCreateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/organization/roles

##### [Retrieve organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

admin.organization.roles.retrieve(strrole\_id)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/update)

admin.organization.roles.update(strrole\_id, RoleUpdateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/delete)

admin.organization.roles.delete(strrole\_id)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

class Role: …

Details about a role that can be assigned through the public Roles API.

id: str

Identifier for the role.

description: Optional[str]

Optional description of the role.

name: str

Unique name for the role.

object: Literal["role"]

Always `role`.

permissions: List[str]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: str

Resource type the role is bound to (for example `api.organization` or `api.project`).

class RoleDeleteResponse: …

Confirmation payload returned after deleting a role.

id: str

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: Literal["role.deleted"]

Always `role.deleted`.

#### OrganizationData Retention

##### [Retrieve organization data retention](/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

admin.organization.data\_retention.retrieve()  -> [OrganizationDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema))

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/python/resources/admin/subresources/organization/subresources/data_retention/methods/update)

admin.organization.data\_retention.update(DataRetentionUpdateParams\*\*kwargs)  -> [OrganizationDataRetention](/api/reference/python/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema))

POST/organization/data\_retention

##### ModelsExpand Collapse

class OrganizationDataRetention: …

Represents the organization’s data retention control setting.

object: Literal["organization.data\_retention"]

The object type, which is always `organization.data_retention`.

type: Literal["zero\_data\_retention", "modified\_abuse\_monitoring", "enhanced\_zero\_data\_retention", "enhanced\_modified\_abuse\_monitoring"]

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### OrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

admin.organization.spend\_alerts.list(SpendAlertListParams\*\*kwargs)  -> SyncConversationCursorPage[[OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))]

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

admin.organization.spend\_alerts.create(SpendAlertCreateParams\*\*kwargs)  -> [OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

admin.organization.spend\_alerts.retrieve(stralert\_id)  -> [OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

admin.organization.spend\_alerts.update(stralert\_id, SpendAlertUpdateParams\*\*kwargs)  -> [OrganizationSpendAlert](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema))

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/python/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

admin.organization.spend\_alerts.delete(stralert\_id)  -> [OrganizationSpendAlertDeleted](/api/reference/python/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema))

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class OrganizationSpendAlert: …

Represents a spend alert configured at the organization level.

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

object: Literal["organization.spend\_alert"]

The object type, which is always `organization.spend_alert`.

threshold\_amount: int

The alert threshold amount, in cents.

class OrganizationSpendAlertDeleted: …

Confirmation payload returned after deleting an organization spend alert.

id: str

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: Literal["organization.spend\_alert.deleted"]

Always `organization.spend_alert.deleted`.

#### OrganizationCertificates

##### [List organization certificates](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/list)

admin.organization.certificates.list(CertificateListParams\*\*kwargs)  -> SyncConversationCursorPage[[CertificateListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema))]

GET/organization/certificates

##### [Upload certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/create)

admin.organization.certificates.create(CertificateCreateParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

POST/organization/certificates

##### [Get certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

admin.organization.certificates.retrieve(strcertificate\_id, CertificateRetrieveParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/update)

admin.organization.certificates.update(strcertificate\_id, CertificateUpdateParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/delete)

admin.organization.certificates.delete(strcertificate\_id)  -> [CertificateDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema))

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/activate)

admin.organization.certificates.activate(CertificateActivateParams\*\*kwargs)  -> SyncPage[[CertificateActivateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema))]

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

admin.organization.certificates.deactivate(CertificateDeactivateParams\*\*kwargs)  -> SyncPage[[CertificateDeactivateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema))]

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

class Certificate: …

Represents an individual `certificate` uploaded to the organization.

id: str

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails

content: Optional[str]

The content of the certificate in PEM format.

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

object: Literal["certificate", "organization.certificate", "organization.project.certificate"]

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

"certificate"

"organization.certificate"

"organization.project.certificate"

active: Optional[bool]

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

class CertificateListResponse: …

Represents an individual certificate configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: Literal["organization.certificate"]

The object type, which is always `organization.certificate`.

class CertificateDeleteResponse: …

id: str

The ID of the certificate that was deleted.

object: Literal["certificate.deleted"]

The object type, must be `certificate.deleted`.

class CertificateActivateResponse: …

Represents an individual certificate configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: Literal["organization.certificate"]

The object type, which is always `organization.certificate`.

class CertificateDeactivateResponse: …

Represents an individual certificate configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: Literal["organization.certificate"]

The object type, which is always `organization.certificate`.

#### OrganizationProjects

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

#### OrganizationProjectsUsers

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

#### OrganizationProjectsUsersRoles

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

#### OrganizationProjectsService Accounts

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

#### OrganizationProjectsAPI Keys

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

#### OrganizationProjectsRate Limits

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

#### OrganizationProjectsModel Permissions

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

#### OrganizationProjectsHosted Tool Permissions

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

#### OrganizationProjectsGroups

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

#### OrganizationProjectsGroupsRoles

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

#### OrganizationProjectsRoles

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

#### OrganizationProjectsData Retention

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

#### OrganizationProjectsSpend Alerts

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

#### OrganizationProjectsCertificates

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
