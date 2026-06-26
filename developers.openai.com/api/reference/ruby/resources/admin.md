<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

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

##### [List audit logs](/api/reference/ruby/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

admin.organization.audit\_logs.list(\*\*kwargs) -> ConversationCursorPage<[AuditLogListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)) { id, effective\_at, type, 57 more } >

GET/organization/audit\_logs

##### ModelsExpand Collapse

class AuditLogListResponse { id, effective\_at, type, 57 more }

A log of a user action or configuration change within this organization.

id: String

The ID of this log.

effective\_at: Integer

The Unix timestamp (in seconds) of the event.

formatunixtime

type: :"api\_key.created" | :"api\_key.updated" | :"api\_key.deleted" | 56 more

The event type.

One of the following:

:"api\_key.created"

:"api\_key.updated"

:"api\_key.deleted"

:"certificate.created"

:"certificate.updated"

:"certificate.deleted"

:"certificates.activated"

:"certificates.deactivated"

:"checkpoint.permission.created"

:"checkpoint.permission.deleted"

:"external\_key.registered"

:"external\_key.removed"

:"group.created"

:"group.updated"

:"group.deleted"

:"invite.sent"

:"invite.accepted"

:"invite.deleted"

:"ip\_allowlist.created"

:"ip\_allowlist.updated"

:"ip\_allowlist.deleted"

:"ip\_allowlist.config.activated"

:"ip\_allowlist.config.deactivated"

:"login.succeeded"

:"login.failed"

:"logout.succeeded"

:"logout.failed"

:"organization.updated"

:"project.created"

:"project.updated"

:"project.archived"

:"project.deleted"

:"rate\_limit.updated"

:"rate\_limit.deleted"

:"resource.deleted"

:"tunnel.created"

:"tunnel.updated"

:"tunnel.deleted"

:"workload\_identity\_provider.created"

:"workload\_identity\_provider.updated"

:"workload\_identity\_provider.deleted"

:"workload\_identity\_provider\_mapping.created"

:"workload\_identity\_provider\_mapping.updated"

:"workload\_identity\_provider\_mapping.deleted"

:"role.created"

:"role.updated"

:"role.deleted"

:"role.assignment.created"

:"role.assignment.deleted"

:"role.bound\_to\_resource"

:"role.unbound\_from\_resource"

:"scim.enabled"

:"scim.disabled"

:"service\_account.created"

:"service\_account.updated"

:"service\_account.deleted"

:"user.added"

:"user.updated"

:"user.deleted"

actor: Actor{ api\_key, session, type}

The actor who performed the audit logged action.

api\_key: APIKey{ id, service\_account, type, user}

The API Key used to perform the audit logged action.

id: String

The tracking id of the API key.

service\_account: ServiceAccount{ id}

The service account that performed the audit logged action.

id: String

The service account id.

type: :user | :service\_account

The type of API key. Can be either `user` or `service_account`.

One of the following:

:user

:service\_account

user: User{ id, email}

The user who performed the audit logged action.

id: String

The user id.

email: String

The user email.

session: Session{ ip\_address, user}

The session in which the audit logged action was performed.

ip\_address: String

The IP address from which the action was performed.

user: User{ id, email}

The user who performed the audit logged action.

id: String

The user id.

email: String

The user email.

type: :session | :api\_key

The type of actor. Is either `session` or `api_key`.

One of the following:

:session

:api\_key

api\_key\_created: APIKeyCreated{ id, data}

The details for events with this `type`.

id: String

The tracking ID of the API key.

data: Data{ scopes}

The payload used to create the API key.

scopes: Array[String]

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

api\_key\_deleted: APIKeyDeleted{ id}

The details for events with this `type`.

id: String

The tracking ID of the API key.

api\_key\_updated: APIKeyUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The tracking ID of the API key.

changes\_requested: ChangesRequested{ scopes}

The payload used to update the API key.

scopes: Array[String]

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

certificate\_created: CertificateCreated{ id, name}

The details for events with this `type`.

id: String

The certificate ID.

name: String

The name of the certificate.

certificate\_deleted: CertificateDeleted{ id, certificate, name}

The details for events with this `type`.

id: String

The certificate ID.

certificate: String

The certificate content in PEM format.

name: String

The name of the certificate.

certificate\_updated: CertificateUpdated{ id, name}

The details for events with this `type`.

id: String

The certificate ID.

name: String

The name of the certificate.

certificates\_activated: CertificatesActivated{ certificates}

The details for events with this `type`.

certificates: Array[Certificate{ id, name}]

id: String

The certificate ID.

name: String

The name of the certificate.

certificates\_deactivated: CertificatesDeactivated{ certificates}

The details for events with this `type`.

certificates: Array[Certificate{ id, name}]

id: String

The certificate ID.

name: String

The name of the certificate.

checkpoint\_permission\_created: CheckpointPermissionCreated{ id, data}

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

id: String

The ID of the checkpoint permission.

data: Data{ fine\_tuned\_model\_checkpoint, project\_id}

The payload used to create the checkpoint permission.

fine\_tuned\_model\_checkpoint: String

The ID of the fine-tuned model checkpoint.

project\_id: String

The ID of the project that the checkpoint permission was created for.

checkpoint\_permission\_deleted: CheckpointPermissionDeleted{ id}

The details for events with this `type`.

id: String

The ID of the checkpoint permission.

external\_key\_registered: ExternalKeyRegistered{ id, data}

The details for events with this `type`.

id: String

The ID of the external key configuration.

data: untyped

The configuration for the external key.

external\_key\_removed: ExternalKeyRemoved{ id}

The details for events with this `type`.

id: String

The ID of the external key configuration.

group\_created: GroupCreated{ id, data}

The details for events with this `type`.

id: String

The ID of the group.

data: Data{ group\_name}

Information about the created group.

group\_name: String

The group name.

group\_deleted: GroupDeleted{ id}

The details for events with this `type`.

id: String

The ID of the group.

group\_updated: GroupUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The ID of the group.

changes\_requested: ChangesRequested{ group\_name}

The payload used to update the group.

group\_name: String

The updated group name.

invite\_accepted: InviteAccepted{ id}

The details for events with this `type`.

id: String

The ID of the invite.

invite\_deleted: InviteDeleted{ id}

The details for events with this `type`.

id: String

The ID of the invite.

invite\_sent: InviteSent{ id, data}

The details for events with this `type`.

id: String

The ID of the invite.

data: Data{ email, role}

The payload used to create the invite.

email: String

The email invited to the organization.

role: String

The role the email was invited to be. Is either `owner` or `member`.

ip\_allowlist\_config\_activated: IPAllowlistConfigActivated{ configs}

The details for events with this `type`.

configs: Array[Config{ id, name}]

The configurations that were activated.

id: String

The ID of the IP allowlist configuration.

name: String

The name of the IP allowlist configuration.

ip\_allowlist\_config\_deactivated: IPAllowlistConfigDeactivated{ configs}

The details for events with this `type`.

configs: Array[Config{ id, name}]

The configurations that were deactivated.

id: String

The ID of the IP allowlist configuration.

name: String

The name of the IP allowlist configuration.

ip\_allowlist\_created: IPAllowlistCreated{ id, allowed\_ips, name}

The details for events with this `type`.

id: String

The ID of the IP allowlist configuration.

allowed\_ips: Array[String]

The IP addresses or CIDR ranges included in the configuration.

name: String

The name of the IP allowlist configuration.

ip\_allowlist\_deleted: IPAllowlistDeleted{ id, allowed\_ips, name}

The details for events with this `type`.

id: String

The ID of the IP allowlist configuration.

allowed\_ips: Array[String]

The IP addresses or CIDR ranges that were in the configuration.

name: String

The name of the IP allowlist configuration.

ip\_allowlist\_updated: IPAllowlistUpdated{ id, allowed\_ips}

The details for events with this `type`.

id: String

The ID of the IP allowlist configuration.

allowed\_ips: Array[String]

The updated set of IP addresses or CIDR ranges in the configuration.

login\_failed: LoginFailed{ error\_code, error\_message}

The details for events with this `type`.

error\_code: String

The error code of the failure.

error\_message: String

The error message of the failure.

login\_succeeded: untyped

This event has no additional fields beyond the standard audit log attributes.

logout\_failed: LogoutFailed{ error\_code, error\_message}

The details for events with this `type`.

error\_code: String

The error code of the failure.

error\_message: String

The error message of the failure.

logout\_succeeded: untyped

This event has no additional fields beyond the standard audit log attributes.

organization\_updated: OrganizationUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The organization ID.

changes\_requested: ChangesRequested{ api\_call\_logging, api\_call\_logging\_project\_ids, description, 4 more}

The payload used to update the organization settings.

api\_call\_logging: String

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

api\_call\_logging\_project\_ids: String

The list of project ids if api\_call\_logging is set to `enabled_for_selected_projects`

description: String

The organization description.

name: String

The organization name.

threads\_ui\_visibility: String

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

title: String

The organization title.

usage\_dashboard\_visibility: String

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

project: Project{ id, name}

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

id: String

The project ID.

name: String

The project title.

project\_archived: ProjectArchived{ id}

The details for events with this `type`.

id: String

The project ID.

project\_created: ProjectCreated{ id, data}

The details for events with this `type`.

id: String

The project ID.

data: Data{ name, title}

The payload used to create the project.

name: String

The project name.

title: String

The title of the project as seen on the dashboard.

project\_deleted: ProjectDeleted{ id}

The details for events with this `type`.

id: String

The project ID.

project\_updated: ProjectUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The project ID.

changes\_requested: ChangesRequested{ title}

The payload used to update the project.

title: String

The title of the project as seen on the dashboard.

rate\_limit\_deleted: RateLimitDeleted{ id}

The details for events with this `type`.

id: String

The rate limit ID

rate\_limit\_updated: RateLimitUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The rate limit ID

changes\_requested: ChangesRequested{ batch\_1\_day\_max\_input\_tokens, max\_audio\_megabytes\_per\_1\_minute, max\_images\_per\_1\_minute, 3 more}

The payload used to update the rate limits.

batch\_1\_day\_max\_input\_tokens: Integer

The maximum batch input tokens per day. Only relevant for certain models.

max\_audio\_megabytes\_per\_1\_minute: Integer

The maximum audio megabytes per minute. Only relevant for certain models.

max\_images\_per\_1\_minute: Integer

The maximum images per minute. Only relevant for certain models.

max\_requests\_per\_1\_day: Integer

The maximum requests per day. Only relevant for certain models.

max\_requests\_per\_1\_minute: Integer

The maximum requests per minute.

max\_tokens\_per\_1\_minute: Integer

The maximum tokens per minute.

role\_assignment\_created: RoleAssignmentCreated{ id, principal\_id, principal\_type, 2 more}

The details for events with this `type`.

id: String

The identifier of the role assignment.

principal\_id: String

The principal (user or group) that received the role.

principal\_type: String

The type of principal (user or group) that received the role.

resource\_id: String

The resource the role assignment is scoped to.

resource\_type: String

The type of resource the role assignment is scoped to.

role\_assignment\_deleted: RoleAssignmentDeleted{ id, principal\_id, principal\_type, 2 more}

The details for events with this `type`.

id: String

The identifier of the role assignment.

principal\_id: String

The principal (user or group) that had the role removed.

principal\_type: String

The type of principal (user or group) that had the role removed.

resource\_id: String

The resource the role assignment was scoped to.

resource\_type: String

The type of resource the role assignment was scoped to.

role\_bound\_to\_resource: RoleBoundToResource{ id, connector\_id, connector\_name, 7 more}

The details for events with this `type`.

id: String

The ID of the resource the role was bound to. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id: String

The connector ID for a ChatGPT workspace connector resource.

connector\_name: String

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled: bool

Whether the connector is enabled for the role.

permissions: Array[String]

The permissions granted to the role for the resource.

resource\_id: String

The ID of the resource the role was bound to.

resource\_type: String

The type of resource the role was bound to.

role\_id: String

The ID of the role that was bound to the resource.

source: :role\_toggle | :role\_connector\_update | :role\_delete | 2 more

The connector role mutation path that produced the event.

One of the following:

:role\_toggle

:role\_connector\_update

:role\_delete

:workspace\_permissions

:connector\_publish

workspace\_id: String

The workspace ID for a ChatGPT workspace connector resource.

role\_created: RoleCreated{ id, permissions, resource\_id, 2 more}

The details for events with this `type`.

id: String

The role ID.

permissions: Array[String]

The permissions granted by the role.

resource\_id: String

The resource the role is scoped to.

resource\_type: String

The type of resource the role belongs to.

role\_name: String

The name of the role.

role\_deleted: RoleDeleted{ id}

The details for events with this `type`.

id: String

The role ID.

role\_unbound\_from\_resource: RoleUnboundFromResource{ id, connector\_id, connector\_name, 7 more}

The details for events with this `type`.

id: String

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id: String

The connector ID for a ChatGPT workspace connector resource.

connector\_name: String

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled: bool

Whether the connector is enabled for the role.

permissions: Array[String]

The permissions remaining for the role after the change.

resource\_id: String

The ID of the resource the role was unbound from.

resource\_type: String

The type of resource the role was unbound from.

role\_id: String

The ID of the role that was unbound from the resource.

source: :role\_toggle | :role\_connector\_update | :role\_delete | 2 more

The connector role mutation path that produced the event.

One of the following:

:role\_toggle

:role\_connector\_update

:role\_delete

:workspace\_permissions

:connector\_publish

workspace\_id: String

The workspace ID for a ChatGPT workspace connector resource.

role\_updated: RoleUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The role ID.

changes\_requested: ChangesRequested{ description, metadata, permissions\_added, 4 more}

The payload used to update the role.

description: String

The updated role description, when provided.

metadata: untyped

Additional metadata stored on the role.

permissions\_added: Array[String]

The permissions added to the role.

permissions\_removed: Array[String]

The permissions removed from the role.

resource\_id: String

The resource the role is scoped to.

resource\_type: String

The type of resource the role belongs to.

role\_name: String

The updated role name, when provided.

scim\_disabled: ScimDisabled{ id}

The details for events with this `type`.

id: String

The ID of the SCIM was disabled for.

scim\_enabled: ScimEnabled{ id}

The details for events with this `type`.

id: String

The ID of the SCIM was enabled for.

service\_account\_created: ServiceAccountCreated{ id, data}

The details for events with this `type`.

id: String

The service account ID.

data: Data{ role}

The payload used to create the service account.

role: String

The role of the service account. Is either `owner` or `member`.

service\_account\_deleted: ServiceAccountDeleted{ id}

The details for events with this `type`.

id: String

The service account ID.

service\_account\_updated: ServiceAccountUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The service account ID.

changes\_requested: ChangesRequested{ role}

The payload used to updated the service account.

role: String

The role of the service account. Is either `owner` or `member`.

user\_added: UserAdded{ id, data}

The details for events with this `type`.

id: String

The user ID.

data: Data{ role}

The payload used to add the user to the project.

role: String

The role of the user. Is either `owner` or `member`.

user\_deleted: UserDeleted{ id}

The details for events with this `type`.

id: String

The user ID.

user\_updated: UserUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The project ID.

changes\_requested: ChangesRequested{ role}

The payload used to update the user.

role: String

The role of the user. Is either `owner` or `member`.

workload\_identity\_provider\_mapping\_created: WorkloadIdentityProviderMappingCreated{ id, data, identity\_provider\_id}

The details for events with this `type`.

id: String

The workload identity provider mapping ID.

data: untyped

The payload used to create the workload identity provider mapping.

identity\_provider\_id: String

The workload identity provider ID.

workload\_identity\_provider\_mapping\_deleted: WorkloadIdentityProviderMappingDeleted{ id, identity\_provider\_id, project\_id, service\_account\_id}

The details for events with this `type`.

id: String

The workload identity provider mapping ID.

identity\_provider\_id: String

The workload identity provider ID.

project\_id: String

The project ID.

service\_account\_id: String

The mapped service account ID.

workload\_identity\_provider\_mapping\_updated: WorkloadIdentityProviderMappingUpdated{ id, changes\_requested, identity\_provider\_id}

The details for events with this `type`.

id: String

The workload identity provider mapping ID.

changes\_requested: untyped

The payload used to update the workload identity provider mapping.

identity\_provider\_id: String

The workload identity provider ID.

workload\_identity\_provider\_created: WorkloadIdentityProviderCreated{ id, data}

The details for events with this `type`.

id: String

The workload identity provider ID.

data: untyped

The payload used to create the workload identity provider.

workload\_identity\_provider\_deleted: WorkloadIdentityProviderDeleted{ id, name}

The details for events with this `type`.

id: String

The workload identity provider ID.

name: String

The workload identity provider name.

workload\_identity\_provider\_updated: WorkloadIdentityProviderUpdated{ id, changes\_requested}

The details for events with this `type`.

id: String

The workload identity provider ID.

changes\_requested: untyped

The payload used to update the workload identity provider.

#### AdminOrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

admin.organization.admin\_api\_keys.list(\*\*kwargs) -> CursorPage<[AdminAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more } >

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

admin.organization.admin\_api\_keys.create(\*\*kwargs) -> [AdminAPIKeyCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)) { value }

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

admin.organization.admin\_api\_keys.retrieve(key\_id) -> [AdminAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

admin.organization.admin\_api\_keys.delete(key\_id) -> [AdminAPIKeyDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

class AdminAPIKey { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: :"organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: Owner{ id, created\_at, name, 3 more}

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: String

The name of the user

object: String

The object type, which is always organization.user

role: String

Always `owner`

type: String

Always `user`

redacted\_value: String

The redacted value of the API key

last\_used\_at: Integer

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: String

The name of the API key

class AdminAPIKeyCreateResponse { value }

Represents an individual Admin API key in an org.

value: String

The value of the API key. Only shown on create.

class AdminAPIKeyDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.admin\_api\_key.deleted"

#### AdminOrganizationUsage

##### [Audio speeches](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

admin.organization.usage.audio\_speeches(\*\*kwargs) -> [UsageAudioSpeechesResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

admin.organization.usage.audio\_transcriptions(\*\*kwargs) -> [UsageAudioTranscriptionsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

admin.organization.usage.code\_interpreter\_sessions(\*\*kwargs) -> [UsageCodeInterpreterSessionsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/completions)

admin.organization.usage.completions(\*\*kwargs) -> [UsageCompletionsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/completions

##### [Embeddings](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

admin.organization.usage.embeddings(\*\*kwargs) -> [UsageEmbeddingsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/embeddings

##### [Images](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/images)

admin.organization.usage.images(\*\*kwargs) -> [UsageImagesResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/images

##### [Moderations](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/moderations)

admin.organization.usage.moderations(\*\*kwargs) -> [UsageModerationsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_moderations_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/moderations

##### [Vector stores](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

admin.organization.usage.vector\_stores(\*\*kwargs) -> [UsageVectorStoresResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_vector_stores_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

admin.organization.usage.file\_search\_calls(\*\*kwargs) -> [UsageFileSearchCallsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_file_search_calls_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

admin.organization.usage.web\_search\_calls(\*\*kwargs) -> [UsageWebSearchCallsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_web_search_calls_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/costs)

admin.organization.usage.costs(\*\*kwargs) -> [UsageCostsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_costs_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/costs

##### ModelsExpand Collapse

class UsageAudioSpeechesResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageAudioTranscriptionsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageCodeInterpreterSessionsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageCompletionsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageEmbeddingsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageImagesResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageModerationsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageVectorStoresResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageFileSearchCallsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageWebSearchCallsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageCostsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

#### AdminOrganizationInvites

##### [List invites](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/list)

admin.organization.invites.list(\*\*kwargs) -> ConversationCursorPage<[Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more } >

GET/organization/invites

##### [Create invite](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/create)

admin.organization.invites.create(\*\*kwargs) -> [Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

POST/organization/invites

##### [Retrieve invite](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

admin.organization.invites.retrieve(invite\_id) -> [Invite](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite%20%3E%20(schema)) { id, created\_at, email, 6 more }

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/ruby/resources/admin/subresources/organization/subresources/invites/methods/delete)

admin.organization.invites.delete(invite\_id) -> [InviteDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

class Invite { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the invite was sent.

formatunixtime

email: String

The email address of the individual to whom the invite was sent

object: :"organization.invite"

The object type, which is always `organization.invite`

projects: Array[Project{ id, role}]

The projects that were granted membership upon acceptance of the invite.

id: String

Project’s public ID

role: :member | :owner

Project membership role

One of the following:

:member

:owner

role: :owner | :reader

`owner` or `reader`

One of the following:

:owner

:reader

status: :accepted | :expired | :pending

`accepted`,`expired`, or `pending`

One of the following:

:accepted

:expired

:pending

accepted\_at: Integer

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

class InviteDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

#### AdminOrganizationUsers

##### [List users](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/list)

admin.organization.users.list(\*\*kwargs) -> ConversationCursorPage<[OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more } >

GET/organization/users

##### [Retrieve user](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/retrieve)

admin.organization.users.retrieve(user\_id) -> [OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/update)

admin.organization.users.update(user\_id, \*\*kwargs) -> [OrganizationUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/methods/delete)

admin.organization.users.delete(user\_id) -> [UserDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationUser { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: String

The identifier, which can be referenced in API endpoints

added\_at: Integer

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: :"organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: Integer

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: Integer

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: String

The developer persona metadata for the user.

email: String

The email address of the user

is\_default: bool

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: bool

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: bool

Whether the user is managed through SCIM.

is\_service\_account: bool

Whether the user is a service account.

name: String

The name of the user

projects: Projects{ data, object}

Projects associated with the user, if included.

data: Array[Data{ id, name, role}]

id: String

name: String

role: String

object: :list

role: String

`owner` or `reader`

technical\_level: String

The technical level metadata for the user.

user: User{ id, object, banned, 5 more}

Nested user details.

id: String

object: :user

banned: bool

banned\_at: Integer

formatunixtime

email: String

enabled: bool

name: String

picture: String

class UserDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.user.deleted"

#### AdminOrganizationUsersRoles

##### [List user organization role assignments](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

admin.organization.users.roles.list(user\_id, \*\*kwargs) -> NextCursorPage<[RoleListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

admin.organization.users.roles.create(user\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { object, role, user }

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

admin.organization.users.roles.retrieve(role\_id, \*\*kwargs) -> [RoleRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/ruby/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

admin.organization.users.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/users/{user\_id}/roles/{role\_id}

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

#### AdminOrganizationGroups

##### [List groups](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/list)

admin.organization.groups.list(\*\*kwargs) -> NextCursorPage<[Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more } >

GET/organization/groups

##### [Create group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/create)

admin.organization.groups.create(\*\*kwargs) -> [Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

POST/organization/groups

##### [Retrieve group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

admin.organization.groups.retrieve(group\_id) -> [Group](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/update)

admin.organization.groups.update(group\_id, \*\*kwargs) -> [GroupUpdateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)) { id, created\_at, is\_scim\_managed, name }

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/methods/delete)

admin.organization.groups.delete(group\_id) -> [GroupDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

class Group { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: :group | :tenant\_group

The type of the group.

One of the following:

:group

:tenant\_group

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: String

Display name of the group.

class GroupUpdateResponse { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: String

Identifier for the group.

created\_at: Integer

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: String

Updated display name for the group.

class GroupDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a group.

id: String

Identifier of the deleted group.

deleted: bool

Whether the group was deleted.

object: :"group.deleted"

Always `group.deleted`.

#### AdminOrganizationGroupsUsers

##### [List group users](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

admin.organization.groups.users.list(group\_id, \*\*kwargs) -> NextCursorPage<[OrganizationGroupUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema)) { id, email, name } >

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

admin.organization.groups.users.create(group\_id, \*\*kwargs) -> [UserCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema)) { group\_id, object, user\_id }

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

admin.organization.groups.users.retrieve(user\_id, \*\*kwargs) -> [UserRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema)) { id, email, is\_service\_account, 3 more }

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

admin.organization.groups.users.delete(user\_id, \*\*kwargs) -> [UserDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationGroupUser { id, email, name }

Represents an individual user returned when inspecting group membership.

id: String

The identifier, which can be referenced in API endpoints

email: String

The email address of the user.

name: String

The name of the user.

class UserCreateResponse { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: String

Identifier of the group the user was added to.

object: :"group.user"

Always `group.user`.

user\_id: String

Identifier of the user that was added.

class UserRetrieveResponse { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: String

Identifier for the user.

email: String

Email address of the user, or `null` for users without an email.

is\_service\_account: bool

Whether the user is a service account.

name: String

Display name of the user.

picture: String

URL of the user’s profile picture, if available.

user\_type: :user | :tenant\_user

The type of user.

One of the following:

:user

:tenant\_user

class UserDeleteResponse { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: bool

Whether the group membership was removed.

object: :"group.user.deleted"

Always `group.user.deleted`.

#### AdminOrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

admin.organization.groups.roles.list(group\_id, \*\*kwargs) -> NextCursorPage<[RoleListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more } >

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

admin.organization.groups.roles.create(group\_id, \*\*kwargs) -> [RoleCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema)) { group, object, role }

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.groups.roles.retrieve(role\_id, \*\*kwargs) -> [RoleRetrieveResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema)) { id, assignment\_sources, created\_at, 9 more }

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/ruby/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

admin.organization.groups.roles.delete(role\_id, \*\*kwargs) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { deleted, object }

DELETE/organization/groups/{group\_id}/roles/{role\_id}

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

#### AdminOrganizationRoles

##### [List organization roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/list)

admin.organization.roles.list(\*\*kwargs) -> NextCursorPage<[Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/organization/roles

##### [Create organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/create)

admin.organization.roles.create(\*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles

##### [Retrieve organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

admin.organization.roles.retrieve(role\_id) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/update)

admin.organization.roles.update(role\_id, \*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/delete)

admin.organization.roles.delete(role\_id) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

class Role { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: String

Identifier for the role.

description: String

Optional description of the role.

name: String

Unique name for the role.

object: :role

Always `role`.

permissions: Array[String]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: String

Resource type the role is bound to (for example `api.organization` or `api.project`).

class RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: String

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: :"role.deleted"

Always `role.deleted`.

#### AdminOrganizationData Retention

##### [Retrieve organization data retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

admin.organization.data\_retention.retrieve() -> [OrganizationDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/data_retention/methods/update)

admin.organization.data\_retention.update(\*\*kwargs) -> [OrganizationDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) { object, type }

POST/organization/data\_retention

##### ModelsExpand Collapse

class OrganizationDataRetention { object, type }

Represents the organization’s data retention control setting.

object: :"organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: :zero\_data\_retention | :modified\_abuse\_monitoring | :enhanced\_zero\_data\_retention | :enhanced\_modified\_abuse\_monitoring

The configured organization data retention type.

One of the following:

:zero\_data\_retention

:modified\_abuse\_monitoring

:enhanced\_zero\_data\_retention

:enhanced\_modified\_abuse\_monitoring

#### AdminOrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

admin.organization.spend\_alerts.list(\*\*kwargs) -> ConversationCursorPage<[OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more } >

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

admin.organization.spend\_alerts.create(\*\*kwargs) -> [OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

admin.organization.spend\_alerts.retrieve(alert\_id) -> [OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

admin.organization.spend\_alerts.update(alert\_id, \*\*kwargs) -> [OrganizationSpendAlert](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert%20%3E%20(schema)) { id, currency, interval, 3 more }

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/ruby/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

admin.organization.spend\_alerts.delete(alert\_id) -> [OrganizationSpendAlertDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.spend_alerts%20%3E%20(model)%20organization_spend_alert_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

class OrganizationSpendAlert { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: :"organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: Integer

The alert threshold amount, in cents.

class OrganizationSpendAlertDeleted { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: String

The deleted spend alert ID.

deleted: bool

Whether the spend alert was deleted.

object: :"organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

#### AdminOrganizationCertificates

##### [List organization certificates](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/list)

admin.organization.certificates.list(\*\*kwargs) -> ConversationCursorPage<[CertificateListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/certificates

##### [Upload certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/create)

admin.organization.certificates.create(\*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates

##### [Get certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

admin.organization.certificates.retrieve(certificate\_id, \*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/update)

admin.organization.certificates.update(certificate\_id, \*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/delete)

admin.organization.certificates.delete(certificate\_id) -> [CertificateDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema)) { id, object }

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/activate)

admin.organization.certificates.activate(\*\*kwargs) -> Page<[CertificateActivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

admin.organization.certificates.deactivate(\*\*kwargs) -> Page<[CertificateDeactivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

class Certificate { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: String

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails{ content, expires\_at, valid\_at}

content: String

The content of the certificate in PEM format.

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

object: :certificate | :"organization.certificate" | :"organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

:certificate

:"organization.certificate"

:"organization.project.certificate"

active: bool

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

class CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: :"organization.certificate"

The object type, which is always `organization.certificate`.

class CertificateDeleteResponse { id, object }

id: String

The ID of the certificate that was deleted.

object: :"certificate.deleted"

The object type, must be `certificate.deleted`.

class CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: :"organization.certificate"

The object type, which is always `organization.certificate`.

class CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: :"organization.certificate"

The object type, which is always `organization.certificate`.

#### AdminOrganizationProjects

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

#### AdminOrganizationProjectsUsers

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

#### AdminOrganizationProjectsUsersRoles

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

#### AdminOrganizationProjectsService Accounts

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

#### AdminOrganizationProjectsAPI Keys

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

#### AdminOrganizationProjectsRate Limits

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

#### AdminOrganizationProjectsModel Permissions

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

#### AdminOrganizationProjectsHosted Tool Permissions

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

#### AdminOrganizationProjectsGroups

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

#### AdminOrganizationProjectsGroupsRoles

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

#### AdminOrganizationProjectsRoles

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

#### AdminOrganizationProjectsData Retention

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

#### AdminOrganizationProjectsSpend Alerts

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

#### AdminOrganizationProjectsCertificates

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
