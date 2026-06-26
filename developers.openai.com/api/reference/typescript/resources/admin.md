<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

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

##### [List audit logs](/api/reference/typescript/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

client.admin.organization.auditLogs.list(AuditLogListParams { actor\_emails, actor\_ids, after, 7 more } query?, RequestOptionsoptions?): ConversationCursorPage<[AuditLogListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)) { id, effective\_at, type, 57 more } >

GET/organization/audit\_logs

##### ModelsExpand Collapse

AuditLogListResponse { id, effective\_at, type, 57 more }

A log of a user action or configuration change within this organization.

id: string

The ID of this log.

effective\_at: number

The Unix timestamp (in seconds) of the event.

formatunixtime

type: "api\_key.created" | "api\_key.updated" | "api\_key.deleted" | 56 more

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

actor?: Actor | null

The actor who performed the audit logged action.

api\_key?: APIKey { id, service\_account, type, user }

The API Key used to perform the audit logged action.

id?: string

The tracking id of the API key.

service\_account?: ServiceAccount { id }

The service account that performed the audit logged action.

id?: string

The service account id.

type?: "user" | "service\_account"

The type of API key. Can be either `user` or `service_account`.

One of the following:

"user"

"service\_account"

user?: User { id, email }

The user who performed the audit logged action.

id?: string

The user id.

email?: string

The user email.

session?: Session { ip\_address, user }

The session in which the audit logged action was performed.

ip\_address?: string

The IP address from which the action was performed.

user?: User { id, email }

The user who performed the audit logged action.

id?: string

The user id.

email?: string

The user email.

type?: "session" | "api\_key"

The type of actor. Is either `session` or `api_key`.

One of the following:

"session"

"api\_key"

"api\_key.created"?: APIKeyCreated { id, data }

The details for events with this `type`.

id?: string

The tracking ID of the API key.

data?: Data { scopes }

The payload used to create the API key.

scopes?: Array<string>

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

"api\_key.deleted"?: APIKeyDeleted { id }

The details for events with this `type`.

id?: string

The tracking ID of the API key.

"api\_key.updated"?: APIKeyUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The tracking ID of the API key.

changes\_requested?: ChangesRequested { scopes }

The payload used to update the API key.

scopes?: Array<string>

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

"certificate.created"?: CertificateCreated { id, name }

The details for events with this `type`.

id?: string

The certificate ID.

name?: string

The name of the certificate.

"certificate.deleted"?: CertificateDeleted { id, certificate, name }

The details for events with this `type`.

id?: string

The certificate ID.

certificate?: string

The certificate content in PEM format.

name?: string

The name of the certificate.

"certificate.updated"?: CertificateUpdated { id, name }

The details for events with this `type`.

id?: string

The certificate ID.

name?: string

The name of the certificate.

"certificates.activated"?: CertificatesActivated { certificates }

The details for events with this `type`.

certificates?: Array<Certificate>

id?: string

The certificate ID.

name?: string

The name of the certificate.

"certificates.deactivated"?: CertificatesDeactivated { certificates }

The details for events with this `type`.

certificates?: Array<Certificate>

id?: string

The certificate ID.

name?: string

The name of the certificate.

"checkpoint.permission.created"?: CheckpointPermissionCreated { id, data }

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

id?: string

The ID of the checkpoint permission.

data?: Data { fine\_tuned\_model\_checkpoint, project\_id }

The payload used to create the checkpoint permission.

fine\_tuned\_model\_checkpoint?: string

The ID of the fine-tuned model checkpoint.

project\_id?: string

The ID of the project that the checkpoint permission was created for.

"checkpoint.permission.deleted"?: CheckpointPermissionDeleted { id }

The details for events with this `type`.

id?: string

The ID of the checkpoint permission.

"external\_key.registered"?: ExternalKeyRegistered { id, data }

The details for events with this `type`.

id?: string

The ID of the external key configuration.

data?: unknown

The configuration for the external key.

"external\_key.removed"?: ExternalKeyRemoved { id }

The details for events with this `type`.

id?: string

The ID of the external key configuration.

"group.created"?: GroupCreated { id, data }

The details for events with this `type`.

id?: string

The ID of the group.

data?: Data { group\_name }

Information about the created group.

group\_name?: string

The group name.

"group.deleted"?: GroupDeleted { id }

The details for events with this `type`.

id?: string

The ID of the group.

"group.updated"?: GroupUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The ID of the group.

changes\_requested?: ChangesRequested { group\_name }

The payload used to update the group.

group\_name?: string

The updated group name.

"invite.accepted"?: InviteAccepted { id }

The details for events with this `type`.

id?: string

The ID of the invite.

"invite.deleted"?: InviteDeleted { id }

The details for events with this `type`.

id?: string

The ID of the invite.

"invite.sent"?: InviteSent { id, data }

The details for events with this `type`.

id?: string

The ID of the invite.

data?: Data { email, role }

The payload used to create the invite.

email?: string

The email invited to the organization.

role?: string

The role the email was invited to be. Is either `owner` or `member`.

"ip\_allowlist.config.activated"?: IPAllowlistConfigActivated { configs }

The details for events with this `type`.

configs?: Array<Config>

The configurations that were activated.

id?: string

The ID of the IP allowlist configuration.

name?: string

The name of the IP allowlist configuration.

"ip\_allowlist.config.deactivated"?: IPAllowlistConfigDeactivated { configs }

The details for events with this `type`.

configs?: Array<Config>

The configurations that were deactivated.

id?: string

The ID of the IP allowlist configuration.

name?: string

The name of the IP allowlist configuration.

"ip\_allowlist.created"?: IPAllowlistCreated { id, allowed\_ips, name }

The details for events with this `type`.

id?: string

The ID of the IP allowlist configuration.

allowed\_ips?: Array<string>

The IP addresses or CIDR ranges included in the configuration.

name?: string

The name of the IP allowlist configuration.

"ip\_allowlist.deleted"?: IPAllowlistDeleted { id, allowed\_ips, name }

The details for events with this `type`.

id?: string

The ID of the IP allowlist configuration.

allowed\_ips?: Array<string>

The IP addresses or CIDR ranges that were in the configuration.

name?: string

The name of the IP allowlist configuration.

"ip\_allowlist.updated"?: IPAllowlistUpdated { id, allowed\_ips }

The details for events with this `type`.

id?: string

The ID of the IP allowlist configuration.

allowed\_ips?: Array<string>

The updated set of IP addresses or CIDR ranges in the configuration.

"login.failed"?: LoginFailed { error\_code, error\_message }

The details for events with this `type`.

error\_code?: string

The error code of the failure.

error\_message?: string

The error message of the failure.

"login.succeeded"?: unknown

This event has no additional fields beyond the standard audit log attributes.

"logout.failed"?: LogoutFailed { error\_code, error\_message }

The details for events with this `type`.

error\_code?: string

The error code of the failure.

error\_message?: string

The error message of the failure.

"logout.succeeded"?: unknown

This event has no additional fields beyond the standard audit log attributes.

"organization.updated"?: OrganizationUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The organization ID.

changes\_requested?: ChangesRequested { api\_call\_logging, api\_call\_logging\_project\_ids, description, 4 more }

The payload used to update the organization settings.

api\_call\_logging?: string

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

api\_call\_logging\_project\_ids?: string

The list of project ids if api\_call\_logging is set to `enabled_for_selected_projects`

description?: string

The organization description.

name?: string

The organization name.

threads\_ui\_visibility?: string

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

title?: string

The organization title.

usage\_dashboard\_visibility?: string

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

project?: Project { id, name }

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

id?: string

The project ID.

name?: string

The project title.

"project.archived"?: ProjectArchived { id }

The details for events with this `type`.

id?: string

The project ID.

"project.created"?: ProjectCreated { id, data }

The details for events with this `type`.

id?: string

The project ID.

data?: Data { name, title }

The payload used to create the project.

name?: string

The project name.

title?: string

The title of the project as seen on the dashboard.

"project.deleted"?: ProjectDeleted { id }

The details for events with this `type`.

id?: string

The project ID.

"project.updated"?: ProjectUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The project ID.

changes\_requested?: ChangesRequested { title }

The payload used to update the project.

title?: string

The title of the project as seen on the dashboard.

"rate\_limit.deleted"?: RateLimitDeleted { id }

The details for events with this `type`.

id?: string

The rate limit ID

"rate\_limit.updated"?: RateLimitUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The rate limit ID

changes\_requested?: ChangesRequested { batch\_1\_day\_max\_input\_tokens, max\_audio\_megabytes\_per\_1\_minute, max\_images\_per\_1\_minute, 3 more }

The payload used to update the rate limits.

batch\_1\_day\_max\_input\_tokens?: number

The maximum batch input tokens per day. Only relevant for certain models.

max\_audio\_megabytes\_per\_1\_minute?: number

The maximum audio megabytes per minute. Only relevant for certain models.

max\_images\_per\_1\_minute?: number

The maximum images per minute. Only relevant for certain models.

max\_requests\_per\_1\_day?: number

The maximum requests per day. Only relevant for certain models.

max\_requests\_per\_1\_minute?: number

The maximum requests per minute.

max\_tokens\_per\_1\_minute?: number

The maximum tokens per minute.

"role.assignment.created"?: RoleAssignmentCreated { id, principal\_id, principal\_type, 2 more }

The details for events with this `type`.

id?: string

The identifier of the role assignment.

principal\_id?: string

The principal (user or group) that received the role.

principal\_type?: string

The type of principal (user or group) that received the role.

resource\_id?: string

The resource the role assignment is scoped to.

resource\_type?: string

The type of resource the role assignment is scoped to.

"role.assignment.deleted"?: RoleAssignmentDeleted { id, principal\_id, principal\_type, 2 more }

The details for events with this `type`.

id?: string

The identifier of the role assignment.

principal\_id?: string

The principal (user or group) that had the role removed.

principal\_type?: string

The type of principal (user or group) that had the role removed.

resource\_id?: string

The resource the role assignment was scoped to.

resource\_type?: string

The type of resource the role assignment was scoped to.

"role.bound\_to\_resource"?: RoleBoundToResource { id, connector\_id, connector\_name, 7 more }

The details for events with this `type`.

id?: string

The ID of the resource the role was bound to. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id?: string

The connector ID for a ChatGPT workspace connector resource.

connector\_name?: string

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled?: boolean

Whether the connector is enabled for the role.

permissions?: Array<string>

The permissions granted to the role for the resource.

resource\_id?: string

The ID of the resource the role was bound to.

resource\_type?: string

The type of resource the role was bound to.

role\_id?: string

The ID of the role that was bound to the resource.

source?: "role\_toggle" | "role\_connector\_update" | "role\_delete" | 2 more

The connector role mutation path that produced the event.

One of the following:

"role\_toggle"

"role\_connector\_update"

"role\_delete"

"workspace\_permissions"

"connector\_publish"

workspace\_id?: string

The workspace ID for a ChatGPT workspace connector resource.

"role.created"?: RoleCreated { id, permissions, resource\_id, 2 more }

The details for events with this `type`.

id?: string

The role ID.

permissions?: Array<string>

The permissions granted by the role.

resource\_id?: string

The resource the role is scoped to.

resource\_type?: string

The type of resource the role belongs to.

role\_name?: string

The name of the role.

"role.deleted"?: RoleDeleted { id }

The details for events with this `type`.

id?: string

The role ID.

"role.unbound\_from\_resource"?: RoleUnboundFromResource { id, connector\_id, connector\_name, 7 more }

The details for events with this `type`.

id?: string

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id?: string

The connector ID for a ChatGPT workspace connector resource.

connector\_name?: string

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled?: boolean

Whether the connector is enabled for the role.

permissions?: Array<string>

The permissions remaining for the role after the change.

resource\_id?: string

The ID of the resource the role was unbound from.

resource\_type?: string

The type of resource the role was unbound from.

role\_id?: string

The ID of the role that was unbound from the resource.

source?: "role\_toggle" | "role\_connector\_update" | "role\_delete" | 2 more

The connector role mutation path that produced the event.

One of the following:

"role\_toggle"

"role\_connector\_update"

"role\_delete"

"workspace\_permissions"

"connector\_publish"

workspace\_id?: string

The workspace ID for a ChatGPT workspace connector resource.

"role.updated"?: RoleUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The role ID.

changes\_requested?: ChangesRequested { description, metadata, permissions\_added, 4 more }

The payload used to update the role.

description?: string

The updated role description, when provided.

metadata?: unknown

Additional metadata stored on the role.

permissions\_added?: Array<string>

The permissions added to the role.

permissions\_removed?: Array<string>

The permissions removed from the role.

resource\_id?: string

The resource the role is scoped to.

resource\_type?: string

The type of resource the role belongs to.

role\_name?: string

The updated role name, when provided.

"scim.disabled"?: ScimDisabled { id }

The details for events with this `type`.

id?: string

The ID of the SCIM was disabled for.

"scim.enabled"?: ScimEnabled { id }

The details for events with this `type`.

id?: string

The ID of the SCIM was enabled for.

"service\_account.created"?: ServiceAccountCreated { id, data }

The details for events with this `type`.

id?: string

The service account ID.

data?: Data { role }

The payload used to create the service account.

role?: string

The role of the service account. Is either `owner` or `member`.

"service\_account.deleted"?: ServiceAccountDeleted { id }

The details for events with this `type`.

id?: string

The service account ID.

"service\_account.updated"?: ServiceAccountUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The service account ID.

changes\_requested?: ChangesRequested { role }

The payload used to updated the service account.

role?: string

The role of the service account. Is either `owner` or `member`.

"user.added"?: UserAdded { id, data }

The details for events with this `type`.

id?: string

The user ID.

data?: Data { role }

The payload used to add the user to the project.

role?: string

The role of the user. Is either `owner` or `member`.

"user.deleted"?: UserDeleted { id }

The details for events with this `type`.

id?: string

The user ID.

"user.updated"?: UserUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The project ID.

changes\_requested?: ChangesRequested { role }

The payload used to update the user.

role?: string

The role of the user. Is either `owner` or `member`.

"workload\_identity\_provider\_mapping.created"?: WorkloadIdentityProviderMappingCreated { id, data, identity\_provider\_id }

The details for events with this `type`.

id?: string

The workload identity provider mapping ID.

data?: unknown

The payload used to create the workload identity provider mapping.

identity\_provider\_id?: string

The workload identity provider ID.

"workload\_identity\_provider\_mapping.deleted"?: WorkloadIdentityProviderMappingDeleted { id, identity\_provider\_id, project\_id, service\_account\_id }

The details for events with this `type`.

id?: string

The workload identity provider mapping ID.

identity\_provider\_id?: string

The workload identity provider ID.

project\_id?: string

The project ID.

service\_account\_id?: string

The mapped service account ID.

"workload\_identity\_provider\_mapping.updated"?: WorkloadIdentityProviderMappingUpdated { id, changes\_requested, identity\_provider\_id }

The details for events with this `type`.

id?: string

The workload identity provider mapping ID.

changes\_requested?: unknown

The payload used to update the workload identity provider mapping.

identity\_provider\_id?: string

The workload identity provider ID.

"workload\_identity\_provider.created"?: WorkloadIdentityProviderCreated { id, data }

The details for events with this `type`.

id?: string

The workload identity provider ID.

data?: unknown

The payload used to create the workload identity provider.

"workload\_identity\_provider.deleted"?: WorkloadIdentityProviderDeleted { id, name }

The details for events with this `type`.

id?: string

The workload identity provider ID.

name?: string

The workload identity provider name.

"workload\_identity\_provider.updated"?: WorkloadIdentityProviderUpdated { id, changes\_requested }

The details for events with this `type`.

id?: string

The workload identity provider ID.

changes\_requested?: unknown

The payload used to update the workload identity provider.

#### AdminOrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

client.admin.organization.adminAPIKeys.list(AdminAPIKeyListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more } >

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

client.admin.organization.adminAPIKeys.create(AdminAPIKeyCreateParams { name, expires\_in\_seconds } body, RequestOptionsoptions?): [AdminAPIKeyCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)) { value }

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

client.admin.organization.adminAPIKeys.retrieve(stringkeyID, RequestOptionsoptions?): [AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

client.admin.organization.adminAPIKeys.delete(stringkeyID, RequestOptionsoptions?): [AdminAPIKeyDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

AdminAPIKey { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: number | null

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: Owner { id, created\_at, name, 3 more }

id?: string

The identifier, which can be referenced in API endpoints

created\_at?: number

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name?: string

The name of the user

object?: string

The object type, which is always organization.user

role?: string

Always `owner`

type?: string

Always `user`

redacted\_value: string

The redacted value of the API key

last\_used\_at?: number | null

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name?: string | null

The name of the API key

AdminAPIKeyCreateResponse extends [AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }  { value }

Represents an individual Admin API key in an org.

value: string

The value of the API key. Only shown on create.

AdminAPIKeyDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.admin\_api\_key.deleted"

#### AdminOrganizationUsage

##### [Audio speeches](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

client.admin.organization.usage.audioSpeeches(UsageAudioSpeechesParams { start\_time, api\_key\_ids, bucket\_width, 7 more } query, RequestOptionsoptions?): [UsageAudioSpeechesResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

client.admin.organization.usage.audioTranscriptions(UsageAudioTranscriptionsParams { start\_time, api\_key\_ids, bucket\_width, 7 more } query, RequestOptionsoptions?): [UsageAudioTranscriptionsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

client.admin.organization.usage.codeInterpreterSessions(UsageCodeInterpreterSessionsParams { start\_time, bucket\_width, end\_time, 4 more } query, RequestOptionsoptions?): [UsageCodeInterpreterSessionsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/completions)

client.admin.organization.usage.completions(UsageCompletionsParams { start\_time, api\_key\_ids, batch, 8 more } query, RequestOptionsoptions?): [UsageCompletionsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/completions

##### [Embeddings](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

client.admin.organization.usage.embeddings(UsageEmbeddingsParams { start\_time, api\_key\_ids, bucket\_width, 7 more } query, RequestOptionsoptions?): [UsageEmbeddingsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/embeddings

##### [Images](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/images)

client.admin.organization.usage.images(UsageImagesParams { start\_time, api\_key\_ids, bucket\_width, 9 more } query, RequestOptionsoptions?): [UsageImagesResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/images

##### [Moderations](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/moderations)

client.admin.organization.usage.moderations(UsageModerationsParams { start\_time, api\_key\_ids, bucket\_width, 7 more } query, RequestOptionsoptions?): [UsageModerationsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_moderations_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/moderations

##### [Vector stores](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

client.admin.organization.usage.vectorStores(UsageVectorStoresParams { start\_time, bucket\_width, end\_time, 4 more } query, RequestOptionsoptions?): [UsageVectorStoresResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_vector_stores_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

client.admin.organization.usage.fileSearchCalls(UsageFileSearchCallsParams { start\_time, api\_key\_ids, bucket\_width, 7 more } query, RequestOptionsoptions?): [UsageFileSearchCallsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_file_search_calls_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

client.admin.organization.usage.webSearchCalls(UsageWebSearchCallsParams { start\_time, api\_key\_ids, bucket\_width, 8 more } query, RequestOptionsoptions?): [UsageWebSearchCallsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_web_search_calls_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/costs)

client.admin.organization.usage.costs(UsageCostsParams { start\_time, api\_key\_ids, bucket\_width, 5 more } query, RequestOptionsoptions?): [UsageCostsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_costs_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/costs

##### ModelsExpand Collapse

UsageAudioSpeechesResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageAudioTranscriptionsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageCodeInterpreterSessionsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageCompletionsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageEmbeddingsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageImagesResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageModerationsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageVectorStoresResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageFileSearchCallsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageWebSearchCallsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

UsageCostsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

#### AdminOrganizationInvites

##### [List invites](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/list)

client.admin.organization.invites.list(InviteListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more } >

GET/organization/invites

##### [Create invite](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/create)

client.admin.organization.invites.create(InviteCreateParams { email, role, projects } body, RequestOptionsoptions?): [Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

POST/organization/invites

##### [Retrieve invite](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

client.admin.organization.invites.retrieve(stringinviteID, RequestOptionsoptions?): [Invite](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/delete)

client.admin.organization.invites.delete(stringinviteID, RequestOptionsoptions?): [InviteDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

Invite { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: string

The email address of the individual to whom the invite was sent

object: "organization.invite"

The object type, which is always `organization.invite`

projects: Array<Project>

The projects that were granted membership upon acceptance of the invite.

id: string

Project’s public ID

role: "member" | "owner"

Project membership role

One of the following:

"member"

"owner"

role: "owner" | "reader"

`owner` or `reader`

One of the following:

"owner"

"reader"

status: "accepted" | "expired" | "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at?: number | null

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at?: number | null

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

InviteDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

#### AdminOrganizationUsers

##### [List users](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/methods/list)

client.admin.organization.users.list(UserListParams { after, emails, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[OrganizationUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more } >

GET/organization/users

##### [Retrieve user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/methods/retrieve)

client.admin.organization.users.retrieve(stringuserID, RequestOptionsoptions?): [OrganizationUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/methods/update)

client.admin.organization.users.update(stringuserID, UserUpdateParams { developer\_persona, role, role\_id, technical\_level } body, RequestOptionsoptions?): [OrganizationUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/methods/delete)

client.admin.organization.users.delete(stringuserID, RequestOptionsoptions?): [UserDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

OrganizationUser { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at?: number | null

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created?: number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona?: string | null

The developer persona metadata for the user.

email?: string | null

The email address of the user

is\_default?: boolean

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser?: boolean | null

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed?: boolean

Whether the user is managed through SCIM.

is\_service\_account?: boolean

Whether the user is a service account.

name?: string | null

The name of the user

projects?: Projects | null

Projects associated with the user, if included.

data: Array<Data>

id?: string | null

name?: string | null

role?: string | null

object: "list"

role?: string | null

`owner` or `reader`

technical\_level?: string | null

The technical level metadata for the user.

user?: User { id, object, banned, 5 more }

Nested user details.

id: string

object: "user"

banned?: boolean | null

banned\_at?: number | null

formatunixtime

email?: string | null

enabled?: boolean | null

name?: string | null

picture?: string | null

UserDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.user.deleted"

#### AdminOrganizationUsersRoles

##### [List user organization role assignments](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

client.admin.organization.users.roles.list(stringuserID, RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[RoleListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

client.admin.organization.users.roles.create(stringuserID, RoleCreateParams { role\_id } body, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

client.admin.organization.users.roles.retrieve(stringroleID, RoleRetrieveParams { user\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/typescript/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

client.admin.organization.users.roles.delete(stringroleID, RoleDeleteParams { user\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/users/{user\_id}/roles/{role\_id}

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

#### AdminOrganizationGroups

##### [List groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/list)

client.admin.organization.groups.list(GroupListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more } >

GET/organization/groups

##### [Create group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/create)

client.admin.organization.groups.create(GroupCreateParams { name } body, RequestOptionsoptions?): [Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

POST/organization/groups

##### [Retrieve group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

client.admin.organization.groups.retrieve(stringgroupID, RequestOptionsoptions?): [Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/update)

client.admin.organization.groups.update(stringgroupID, GroupUpdateParams { name } body, RequestOptionsoptions?): [GroupUpdateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)) { id, created\_at, is\_scim\_managed, name }

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/delete)

client.admin.organization.groups.delete(stringgroupID, RequestOptionsoptions?): [GroupDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

Group { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: "group" | "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

GroupUpdateResponse { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Updated display name for the group.

GroupDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a group.

id: string

Identifier of the deleted group.

deleted: boolean

Whether the group was deleted.

object: "group.deleted"

Always `group.deleted`.

#### AdminOrganizationGroupsUsers

##### [List group users](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

client.admin.organization.groups.users.list(stringgroupID, UserListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[OrganizationGroupUser](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name } >

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

client.admin.organization.groups.users.create(stringgroupID, UserCreateParams { user\_id } body, RequestOptionsoptions?): [UserCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)) { group\_id, object, user\_id }

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

client.admin.organization.groups.users.retrieve(stringuserID, UserRetrieveParams { group\_id } params, RequestOptionsoptions?): [UserRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)) { id, email, is\_service\_account, 3 more }

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

client.admin.organization.groups.users.delete(stringuserID, UserDeleteParams { group\_id } params, RequestOptionsoptions?): [UserDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

OrganizationGroupUser { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string | null

The email address of the user.

name: string

The name of the user.

UserCreateResponse { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

UserRetrieveResponse { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: string

Identifier for the user.

email: string | null

Email address of the user, or `null` for users without an email.

is\_service\_account: boolean | null

Whether the user is a service account.

name: string

Display name of the user.

picture: string | null

URL of the user’s profile picture, if available.

user\_type: "user" | "tenant\_user"

The type of user.

One of the following:

"user"

"tenant\_user"

UserDeleteResponse { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: boolean

Whether the group membership was removed.

object: "group.user.deleted"

Always `group.user.deleted`.

#### AdminOrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

client.admin.organization.groups.roles.list(stringgroupID, RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[RoleListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

client.admin.organization.groups.roles.create(stringgroupID, RoleCreateParams { role\_id } body, RequestOptionsoptions?): [RoleCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

client.admin.organization.groups.roles.retrieve(stringroleID, RoleRetrieveParams { group\_id } params, RequestOptionsoptions?): [RoleRetrieveResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

client.admin.organization.groups.roles.delete(stringroleID, RoleDeleteParams { group\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/roles/{role\_id}

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

#### AdminOrganizationRoles

##### [List organization roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/list)

client.admin.organization.roles.list(RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/organization/roles

##### [Create organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/create)

client.admin.organization.roles.create(RoleCreateParams { permissions, role\_name, description } body, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles

##### [Retrieve organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

client.admin.organization.roles.retrieve(stringroleID, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/update)

client.admin.organization.roles.update(stringroleID, RoleUpdateParams { description, permissions, role\_name } body, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/delete)

client.admin.organization.roles.delete(stringroleID, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

Role { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: string

Identifier for the role.

description: string | null

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: Array<string>

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).

RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

#### AdminOrganizationData Retention

##### [Retrieve organization data retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

client.admin.organization.dataRetention.retrieve(RequestOptionsoptions?): [OrganizationDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/typescript/resources/admin/subresources/organization/subresources/data_retention/methods/update)

client.admin.organization.dataRetention.update(DataRetentionUpdateParams { retention\_type } body, RequestOptionsoptions?): [OrganizationDataRetention](/api/reference/typescript/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

POST/organization/data\_retention

##### ModelsExpand Collapse

OrganizationDataRetention { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" | "modified\_abuse\_monitoring" | "enhanced\_zero\_data\_retention" | "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### AdminOrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

client.admin.organization.spendAlerts.list(SpendAlertListParams { after, before, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

client.admin.organization.spendAlerts.create(SpendAlertCreateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

client.admin.organization.spendAlerts.retrieve(stringalertID, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

client.admin.organization.spendAlerts.update(stringalertID, SpendAlertUpdateParams { currency, interval, notification\_channel, threshold\_amount } body, RequestOptionsoptions?): [OrganizationSpendAlert](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/typescript/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

client.admin.organization.spendAlerts.delete(stringalertID, RequestOptionsoptions?): [OrganizationSpendAlertDeleted](/api/reference/typescript/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

OrganizationSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

OrganizationSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

#### AdminOrganizationCertificates

##### [List organization certificates](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/list)

client.admin.organization.certificates.list(CertificateListParams { after, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[CertificateListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/certificates

##### [Upload certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/create)

client.admin.organization.certificates.create(CertificateCreateParams { certificate, name } body, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates

##### [Get certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

client.admin.organization.certificates.retrieve(stringcertificateID, CertificateRetrieveParams { include } query?, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/update)

client.admin.organization.certificates.update(stringcertificateID, CertificateUpdateParams { name } body, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/delete)

client.admin.organization.certificates.delete(stringcertificateID, RequestOptionsoptions?): [CertificateDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema)) { id, object }

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/activate)

client.admin.organization.certificates.activate(CertificateActivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateActivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

client.admin.organization.certificates.deactivate(CertificateDeactivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateDeactivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

Certificate { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: string

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails { content, expires\_at, valid\_at }

content?: string

The content of the certificate in PEM format.

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

object: "certificate" | "organization.certificate" | "organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

"certificate"

"organization.certificate"

"organization.project.certificate"

active?: boolean

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

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

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeleteResponse { id, object }

id: string

The ID of the certificate that was deleted.

object: "certificate.deleted"

The object type, must be `certificate.deleted`.

CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

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

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

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

object: "organization.certificate"

The object type, which is always `organization.certificate`.

#### AdminOrganizationProjects

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

#### AdminOrganizationProjectsUsers

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

#### AdminOrganizationProjectsUsersRoles

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

#### AdminOrganizationProjectsService Accounts

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

#### AdminOrganizationProjectsAPI Keys

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

#### AdminOrganizationProjectsRate Limits

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

#### AdminOrganizationProjectsModel Permissions

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

#### AdminOrganizationProjectsHosted Tool Permissions

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

#### AdminOrganizationProjectsGroups

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

#### AdminOrganizationProjectsGroupsRoles

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

#### AdminOrganizationProjectsRoles

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

#### AdminOrganizationProjectsData Retention

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

#### AdminOrganizationProjectsSpend Alerts

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

#### AdminOrganizationProjectsCertificates

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
