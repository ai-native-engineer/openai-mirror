<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

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

##### [List audit logs](/api/reference/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

GET/organization/audit\_logs

##### ModelsExpand Collapse

AuditLogListResponse object { id, effective\_at, type, 57 more }

A log of a user action or configuration change within this organization.

id: string

The ID of this log.

effective\_at: number

The Unix timestamp (in seconds) of the event.

formatunixtime

type: "api\_key.created" or "api\_key.updated" or "api\_key.deleted" or 56 more

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

actor: optional object { api\_key, session, type }

The actor who performed the audit logged action.

api\_key: optional object { id, service\_account, type, user }

The API Key used to perform the audit logged action.

id: optional string

The tracking id of the API key.

service\_account: optional object { id }

The service account that performed the audit logged action.

id: optional string

The service account id.

type: optional "user" or "service\_account"

The type of API key. Can be either `user` or `service_account`.

One of the following:

"user"

"service\_account"

user: optional object { id, email }

The user who performed the audit logged action.

id: optional string

The user id.

email: optional string

The user email.

session: optional object { ip\_address, user }

The session in which the audit logged action was performed.

ip\_address: optional string

The IP address from which the action was performed.

user: optional object { id, email }

The user who performed the audit logged action.

id: optional string

The user id.

email: optional string

The user email.

type: optional "session" or "api\_key"

The type of actor. Is either `session` or `api_key`.

One of the following:

"session"

"api\_key"

"api\_key.created": optional object { id, data }

The details for events with this `type`.

id: optional string

The tracking ID of the API key.

data: optional object { scopes }

The payload used to create the API key.

scopes: optional array of string

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

"api\_key.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The tracking ID of the API key.

"api\_key.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The tracking ID of the API key.

changes\_requested: optional object { scopes }

The payload used to update the API key.

scopes: optional array of string

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

"certificate.created": optional object { id, name }

The details for events with this `type`.

id: optional string

The certificate ID.

name: optional string

The name of the certificate.

"certificate.deleted": optional object { id, certificate, name }

The details for events with this `type`.

id: optional string

The certificate ID.

certificate: optional string

The certificate content in PEM format.

name: optional string

The name of the certificate.

"certificate.updated": optional object { id, name }

The details for events with this `type`.

id: optional string

The certificate ID.

name: optional string

The name of the certificate.

"certificates.activated": optional object { certificates }

The details for events with this `type`.

certificates: optional array of object { id, name }

id: optional string

The certificate ID.

name: optional string

The name of the certificate.

"certificates.deactivated": optional object { certificates }

The details for events with this `type`.

certificates: optional array of object { id, name }

id: optional string

The certificate ID.

name: optional string

The name of the certificate.

"checkpoint.permission.created": optional object { id, data }

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

id: optional string

The ID of the checkpoint permission.

data: optional object { fine\_tuned\_model\_checkpoint, project\_id }

The payload used to create the checkpoint permission.

fine\_tuned\_model\_checkpoint: optional string

The ID of the fine-tuned model checkpoint.

project\_id: optional string

The ID of the project that the checkpoint permission was created for.

"checkpoint.permission.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the checkpoint permission.

"external\_key.registered": optional object { id, data }

The details for events with this `type`.

id: optional string

The ID of the external key configuration.

data: optional unknown

The configuration for the external key.

"external\_key.removed": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the external key configuration.

"group.created": optional object { id, data }

The details for events with this `type`.

id: optional string

The ID of the group.

data: optional object { group\_name }

Information about the created group.

group\_name: optional string

The group name.

"group.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the group.

"group.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The ID of the group.

changes\_requested: optional object { group\_name }

The payload used to update the group.

group\_name: optional string

The updated group name.

"invite.accepted": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the invite.

"invite.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the invite.

"invite.sent": optional object { id, data }

The details for events with this `type`.

id: optional string

The ID of the invite.

data: optional object { email, role }

The payload used to create the invite.

email: optional string

The email invited to the organization.

role: optional string

The role the email was invited to be. Is either `owner` or `member`.

"ip\_allowlist.config.activated": optional object { configs }

The details for events with this `type`.

configs: optional array of object { id, name }

The configurations that were activated.

id: optional string

The ID of the IP allowlist configuration.

name: optional string

The name of the IP allowlist configuration.

"ip\_allowlist.config.deactivated": optional object { configs }

The details for events with this `type`.

configs: optional array of object { id, name }

The configurations that were deactivated.

id: optional string

The ID of the IP allowlist configuration.

name: optional string

The name of the IP allowlist configuration.

"ip\_allowlist.created": optional object { id, allowed\_ips, name }

The details for events with this `type`.

id: optional string

The ID of the IP allowlist configuration.

allowed\_ips: optional array of string

The IP addresses or CIDR ranges included in the configuration.

name: optional string

The name of the IP allowlist configuration.

"ip\_allowlist.deleted": optional object { id, allowed\_ips, name }

The details for events with this `type`.

id: optional string

The ID of the IP allowlist configuration.

allowed\_ips: optional array of string

The IP addresses or CIDR ranges that were in the configuration.

name: optional string

The name of the IP allowlist configuration.

"ip\_allowlist.updated": optional object { id, allowed\_ips }

The details for events with this `type`.

id: optional string

The ID of the IP allowlist configuration.

allowed\_ips: optional array of string

The updated set of IP addresses or CIDR ranges in the configuration.

"login.failed": optional object { error\_code, error\_message }

The details for events with this `type`.

error\_code: optional string

The error code of the failure.

error\_message: optional string

The error message of the failure.

"login.succeeded": optional unknown

This event has no additional fields beyond the standard audit log attributes.

"logout.failed": optional object { error\_code, error\_message }

The details for events with this `type`.

error\_code: optional string

The error code of the failure.

error\_message: optional string

The error message of the failure.

"logout.succeeded": optional unknown

This event has no additional fields beyond the standard audit log attributes.

"organization.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The organization ID.

changes\_requested: optional object { api\_call\_logging, api\_call\_logging\_project\_ids, description, 4 more }

The payload used to update the organization settings.

api\_call\_logging: optional string

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

api\_call\_logging\_project\_ids: optional string

The list of project ids if api\_call\_logging is set to `enabled_for_selected_projects`

description: optional string

The organization description.

name: optional string

The organization name.

threads\_ui\_visibility: optional string

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

title: optional string

The organization title.

usage\_dashboard\_visibility: optional string

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

project: optional object { id, name }

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

id: optional string

The project ID.

name: optional string

The project title.

"project.archived": optional object { id }

The details for events with this `type`.

id: optional string

The project ID.

"project.created": optional object { id, data }

The details for events with this `type`.

id: optional string

The project ID.

data: optional object { name, title }

The payload used to create the project.

name: optional string

The project name.

title: optional string

The title of the project as seen on the dashboard.

"project.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The project ID.

"project.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The project ID.

changes\_requested: optional object { title }

The payload used to update the project.

title: optional string

The title of the project as seen on the dashboard.

"rate\_limit.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The rate limit ID

"rate\_limit.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The rate limit ID

changes\_requested: optional object { batch\_1\_day\_max\_input\_tokens, max\_audio\_megabytes\_per\_1\_minute, max\_images\_per\_1\_minute, 3 more }

The payload used to update the rate limits.

batch\_1\_day\_max\_input\_tokens: optional number

The maximum batch input tokens per day. Only relevant for certain models.

max\_audio\_megabytes\_per\_1\_minute: optional number

The maximum audio megabytes per minute. Only relevant for certain models.

max\_images\_per\_1\_minute: optional number

The maximum images per minute. Only relevant for certain models.

max\_requests\_per\_1\_day: optional number

The maximum requests per day. Only relevant for certain models.

max\_requests\_per\_1\_minute: optional number

The maximum requests per minute.

max\_tokens\_per\_1\_minute: optional number

The maximum tokens per minute.

"role.assignment.created": optional object { id, principal\_id, principal\_type, 2 more }

The details for events with this `type`.

id: optional string

The identifier of the role assignment.

principal\_id: optional string

The principal (user or group) that received the role.

principal\_type: optional string

The type of principal (user or group) that received the role.

resource\_id: optional string

The resource the role assignment is scoped to.

resource\_type: optional string

The type of resource the role assignment is scoped to.

"role.assignment.deleted": optional object { id, principal\_id, principal\_type, 2 more }

The details for events with this `type`.

id: optional string

The identifier of the role assignment.

principal\_id: optional string

The principal (user or group) that had the role removed.

principal\_type: optional string

The type of principal (user or group) that had the role removed.

resource\_id: optional string

The resource the role assignment was scoped to.

resource\_type: optional string

The type of resource the role assignment was scoped to.

"role.bound\_to\_resource": optional object { id, connector\_id, connector\_name, 7 more }

The details for events with this `type`.

id: optional string

The ID of the resource the role was bound to. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id: optional string

The connector ID for a ChatGPT workspace connector resource.

connector\_name: optional string

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled: optional boolean

Whether the connector is enabled for the role.

permissions: optional array of string

The permissions granted to the role for the resource.

resource\_id: optional string

The ID of the resource the role was bound to.

resource\_type: optional string

The type of resource the role was bound to.

role\_id: optional string

The ID of the role that was bound to the resource.

source: optional "role\_toggle" or "role\_connector\_update" or "role\_delete" or 2 more

The connector role mutation path that produced the event.

One of the following:

"role\_toggle"

"role\_connector\_update"

"role\_delete"

"workspace\_permissions"

"connector\_publish"

workspace\_id: optional string

The workspace ID for a ChatGPT workspace connector resource.

"role.created": optional object { id, permissions, resource\_id, 2 more }

The details for events with this `type`.

id: optional string

The role ID.

permissions: optional array of string

The permissions granted by the role.

resource\_id: optional string

The resource the role is scoped to.

resource\_type: optional string

The type of resource the role belongs to.

role\_name: optional string

The name of the role.

"role.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The role ID.

"role.unbound\_from\_resource": optional object { id, connector\_id, connector\_name, 7 more }

The details for events with this `type`.

id: optional string

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

connector\_id: optional string

The connector ID for a ChatGPT workspace connector resource.

connector\_name: optional string

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

enabled: optional boolean

Whether the connector is enabled for the role.

permissions: optional array of string

The permissions remaining for the role after the change.

resource\_id: optional string

The ID of the resource the role was unbound from.

resource\_type: optional string

The type of resource the role was unbound from.

role\_id: optional string

The ID of the role that was unbound from the resource.

source: optional "role\_toggle" or "role\_connector\_update" or "role\_delete" or 2 more

The connector role mutation path that produced the event.

One of the following:

"role\_toggle"

"role\_connector\_update"

"role\_delete"

"workspace\_permissions"

"connector\_publish"

workspace\_id: optional string

The workspace ID for a ChatGPT workspace connector resource.

"role.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The role ID.

changes\_requested: optional object { description, metadata, permissions\_added, 4 more }

The payload used to update the role.

description: optional string

The updated role description, when provided.

metadata: optional unknown

Additional metadata stored on the role.

permissions\_added: optional array of string

The permissions added to the role.

permissions\_removed: optional array of string

The permissions removed from the role.

resource\_id: optional string

The resource the role is scoped to.

resource\_type: optional string

The type of resource the role belongs to.

role\_name: optional string

The updated role name, when provided.

"scim.disabled": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the SCIM was disabled for.

"scim.enabled": optional object { id }

The details for events with this `type`.

id: optional string

The ID of the SCIM was enabled for.

"service\_account.created": optional object { id, data }

The details for events with this `type`.

id: optional string

The service account ID.

data: optional object { role }

The payload used to create the service account.

role: optional string

The role of the service account. Is either `owner` or `member`.

"service\_account.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The service account ID.

"service\_account.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The service account ID.

changes\_requested: optional object { role }

The payload used to updated the service account.

role: optional string

The role of the service account. Is either `owner` or `member`.

"user.added": optional object { id, data }

The details for events with this `type`.

id: optional string

The user ID.

data: optional object { role }

The payload used to add the user to the project.

role: optional string

The role of the user. Is either `owner` or `member`.

"user.deleted": optional object { id }

The details for events with this `type`.

id: optional string

The user ID.

"user.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The project ID.

changes\_requested: optional object { role }

The payload used to update the user.

role: optional string

The role of the user. Is either `owner` or `member`.

"workload\_identity\_provider\_mapping.created": optional object { id, data, identity\_provider\_id }

The details for events with this `type`.

id: optional string

The workload identity provider mapping ID.

data: optional unknown

The payload used to create the workload identity provider mapping.

identity\_provider\_id: optional string

The workload identity provider ID.

"workload\_identity\_provider\_mapping.deleted": optional object { id, identity\_provider\_id, project\_id, service\_account\_id }

The details for events with this `type`.

id: optional string

The workload identity provider mapping ID.

identity\_provider\_id: optional string

The workload identity provider ID.

project\_id: optional string

The project ID.

service\_account\_id: optional string

The mapped service account ID.

"workload\_identity\_provider\_mapping.updated": optional object { id, changes\_requested, identity\_provider\_id }

The details for events with this `type`.

id: optional string

The workload identity provider mapping ID.

changes\_requested: optional unknown

The payload used to update the workload identity provider mapping.

identity\_provider\_id: optional string

The workload identity provider ID.

"workload\_identity\_provider.created": optional object { id, data }

The details for events with this `type`.

id: optional string

The workload identity provider ID.

data: optional unknown

The payload used to create the workload identity provider.

"workload\_identity\_provider.deleted": optional object { id, name }

The details for events with this `type`.

id: optional string

The workload identity provider ID.

name: optional string

The workload identity provider name.

"workload\_identity\_provider.updated": optional object { id, changes\_requested }

The details for events with this `type`.

id: optional string

The workload identity provider ID.

changes\_requested: optional unknown

The payload used to update the workload identity provider.

#### OrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

AdminAPIKey object { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: number

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: object { id, created\_at, name, 3 more }

id: optional string

The identifier, which can be referenced in API endpoints

created\_at: optional number

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: optional string

The name of the user

object: optional string

The object type, which is always organization.user

role: optional string

Always `owner`

type: optional string

Always `user`

redacted\_value: string

The redacted value of the API key

last\_used\_at: optional number

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: optional string

The name of the API key

AdminAPIKeyCreateResponse = [AdminAPIKey](/api/reference/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

value: string

The value of the API key. Only shown on create.

AdminAPIKeyDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.admin\_api\_key.deleted"

#### OrganizationUsage

##### [Audio speeches](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/completions)

GET/organization/usage/completions

##### [Embeddings](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

GET/organization/usage/embeddings

##### [Images](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/images)

GET/organization/usage/images

##### [Moderations](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/moderations)

GET/organization/usage/moderations

##### [Vector stores](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/costs)

GET/organization/costs

##### ModelsExpand Collapse

UsageAudioSpeechesResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageAudioTranscriptionsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageCodeInterpreterSessionsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageCompletionsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageEmbeddingsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageImagesResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageModerationsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageVectorStoresResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageFileSearchCallsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageWebSearchCallsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

UsageCostsResponse object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

#### OrganizationInvites

##### [List invites](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/list)

GET/organization/invites

##### [Create invite](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/create)

POST/organization/invites

##### [Retrieve invite](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/resources/admin/subresources/organization/subresources/invites/methods/delete)

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

Invite object { id, created\_at, email, 6 more }

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

projects: array of object { id, role }

The projects that were granted membership upon acceptance of the invite.

id: string

Project’s public ID

role: "member" or "owner"

Project membership role

One of the following:

"member"

"owner"

role: "owner" or "reader"

`owner` or `reader`

One of the following:

"owner"

"reader"

status: "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

One of the following:

"accepted"

"expired"

"pending"

accepted\_at: optional number

The Unix timestamp (in seconds) of when the invite was accepted.

formatunixtime

expires\_at: optional number

The Unix timestamp (in seconds) of when the invite expires.

formatunixtime

InviteDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

#### OrganizationUsers

##### [List users](/api/reference/resources/admin/subresources/organization/subresources/users/methods/list)

GET/organization/users

##### [Retrieve user](/api/reference/resources/admin/subresources/organization/subresources/users/methods/retrieve)

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/resources/admin/subresources/organization/subresources/users/methods/update)

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/resources/admin/subresources/organization/subresources/users/methods/delete)

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

OrganizationUser object { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: optional number

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: optional number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: optional string

The developer persona metadata for the user.

email: optional string

The email address of the user

is\_default: optional boolean

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: optional boolean

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: optional boolean

Whether the user is managed through SCIM.

is\_service\_account: optional boolean

Whether the user is a service account.

name: optional string

The name of the user

projects: optional object { data, object }

Projects associated with the user, if included.

data: array of object { id, name, role }

id: optional string

name: optional string

role: optional string

object: "list"

role: optional string

`owner` or `reader`

technical\_level: optional string

The technical level metadata for the user.

user: optional object { id, object, banned, 5 more }

Nested user details.

id: string

object: "user"

banned: optional boolean

banned\_at: optional number

formatunixtime

email: optional string

enabled: optional boolean

name: optional string

picture: optional string

UserDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.user.deleted"

#### OrganizationUsersRoles

##### [List user organization role assignments](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

DELETE/organization/users/{user\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleCreateResponse object { object, role, user }

Role assignment linking a user to a role.

object: "user.role"

Always `user.role`.

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

RoleRetrieveResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleDeleteResponse object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

#### OrganizationGroups

##### [List groups](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/list)

GET/organization/groups

##### [Create group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/create)

POST/organization/groups

##### [Retrieve group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/update)

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/resources/admin/subresources/organization/subresources/groups/methods/delete)

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

Group object { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: "group" or "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

GroupUpdateResponse object { id, created\_at, is\_scim\_managed, name }

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

GroupDeleteResponse object { id, deleted, object }

Confirmation payload returned after deleting a group.

id: string

Identifier of the deleted group.

deleted: boolean

Whether the group was deleted.

object: "group.deleted"

Always `group.deleted`.

#### OrganizationGroupsUsers

##### [List group users](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

OrganizationGroupUser object { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string

The email address of the user.

name: string

The name of the user.

UserCreateResponse object { group\_id, object, user\_id }

Confirmation payload returned after adding a user to a group.

group\_id: string

Identifier of the group the user was added to.

object: "group.user"

Always `group.user`.

user\_id: string

Identifier of the user that was added.

UserRetrieveResponse object { id, email, is\_service\_account, 3 more }

Details about a user returned from an organization group membership lookup.

id: string

Identifier for the user.

email: string

Email address of the user, or `null` for users without an email.

is\_service\_account: boolean

Whether the user is a service account.

name: string

Display name of the user.

picture: string

URL of the user’s profile picture, if available.

user\_type: "user" or "tenant\_user"

The type of user.

One of the following:

"user"

"tenant\_user"

UserDeleteResponse object { deleted, object }

Confirmation payload returned after removing a user from a group.

deleted: boolean

Whether the group membership was removed.

object: "group.user.deleted"

Always `group.user.deleted`.

#### OrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

DELETE/organization/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleCreateResponse object { group, object, role }

Role assignment linking a group to a role.

group: object { id, created\_at, name, 2 more }

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

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

RoleRetrieveResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleDeleteResponse object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

#### OrganizationRoles

##### [List organization roles](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/list)

GET/organization/roles

##### [Create organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/create)

POST/organization/roles

##### [Retrieve organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/update)

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/resources/admin/subresources/organization/subresources/roles/methods/delete)

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

Role object { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: string

Identifier for the role.

description: string

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: array of string

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).

RoleDeleteResponse object { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

#### OrganizationData Retention

##### [Retrieve organization data retention](/api/reference/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/resources/admin/subresources/organization/subresources/data_retention/methods/update)

POST/organization/data\_retention

##### ModelsExpand Collapse

OrganizationDataRetention object { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

One of the following:

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### OrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

OrganizationSpendAlert object { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

interval: "month"

The time interval for evaluating spend against the threshold.

notification\_channel: object { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: array of string

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix: optional string

Optional subject prefix for alert emails.

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

OrganizationSpendAlertDeleted object { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

#### OrganizationCertificates

##### [List organization certificates](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/list)

GET/organization/certificates

##### [Upload certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/create)

POST/organization/certificates

##### [Get certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/update)

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/delete)

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/activate)

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

Certificate object { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: string

The identifier, which can be referenced in API endpoints

certificate\_details: object { content, expires\_at, valid\_at }

content: optional string

The content of the certificate in PEM format.

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "certificate" or "organization.certificate" or "organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

"certificate"

"organization.certificate"

"organization.project.certificate"

active: optional boolean

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

CertificateListResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeleteResponse object { id, object }

id: string

The ID of the certificate that was deleted.

object: "certificate.deleted"

The object type, must be `certificate.deleted`.

CertificateActivateResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeactivateResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

#### OrganizationProjects

##### [List projects](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/list)

GET/organization/projects

##### [Create project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/create)

POST/organization/projects

##### [Retrieve project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/update)

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/resources/admin/subresources/organization/subresources/projects/methods/archive)

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

Project object { id, created\_at, object, 4 more }

Represents an individual project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: "organization.project"

The object type, which is always `organization.project`

archived\_at: optional number

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id: optional string

The external key associated with the project.

name: optional string

The name of the project. This appears in reporting.

status: optional string

`active` or `archived`

#### OrganizationProjectsUsers

##### [List project users](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

ProjectUser object { id, added\_at, object, 3 more }

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

email: optional string

The email address of the user

name: optional string

The name of the user

UserDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.user.deleted"

#### OrganizationProjectsUsersRoles

##### [List project user role assignments](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleCreateResponse object { object, role, user }

Role assignment linking a user to a role.

object: "user.role"

Always `user.role`.

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

RoleRetrieveResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleDeleteResponse object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

#### OrganizationProjectsService Accounts

##### [List project service accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

ProjectServiceAccount object { id, created\_at, name, 2 more }

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

role: "owner" or "member"

`owner` or `member`

One of the following:

"owner"

"member"

ServiceAccountCreateResponse object { id, api\_key, created\_at, 3 more }

id: string

api\_key: object { id, created\_at, name, 2 more }

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

ServiceAccountDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.service\_account.deleted"

#### OrganizationProjectsAPI Keys

##### [List project API keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

ProjectAPIKey object { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: number

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: string

The name of the API key

object: "organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: object { service\_account, type, user }

service\_account: optional object { id, created\_at, name, role }

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

type: optional "user" or "service\_account"

`user` or `service_account`

One of the following:

"user"

"service\_account"

user: optional object { id, created\_at, email, 2 more }

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

APIKeyDeleteResponse object { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.api\_key.deleted"

#### OrganizationProjectsRate Limits

##### [List project rate limits](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

ProjectRateLimit object { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

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

batch\_1\_day\_max\_input\_tokens: optional number

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute: optional number

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute: optional number

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day: optional number

The maximum requests per day. Only present for relevant models.

#### OrganizationProjectsModel Permissions

##### [Retrieve project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

ProjectModelPermissions object { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: "allow\_list" or "deny\_list"

Whether the project uses an allowlist or a denylist.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: array of string

The model IDs included in the model permissions policy.

object: "project.model\_permissions"

The object type, which is always `project.model_permissions`.

ProjectModelPermissionsDeleted object { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: boolean

Whether the project model permissions were deleted.

object: "project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

#### OrganizationProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

ProjectHostedToolPermissions object { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

file\_search: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

image\_generation: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

mcp: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

web\_search: object { enabled }

Permission state for a single hosted tool on a project.

enabled: boolean

Whether the hosted tool is enabled for the project.

#### OrganizationProjectsGroups

##### [List project groups](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

ProjectGroup object { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" or "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

GroupDeleteResponse object { deleted, object }

Confirmation payload returned after removing a group from a project.

deleted: boolean

Whether the group membership in the project was removed.

object: "project.group.deleted"

Always `project.group.deleted`.

#### OrganizationProjectsGroupsRoles

##### [List project group role assignments](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleCreateResponse object { group, object, role }

Role assignment linking a group to a role.

group: object { id, created\_at, name, 2 more }

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

role: [Role](/api/reference/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

RoleRetrieveResponse object { id, assignment\_sources, created\_at, 9 more }

Detailed information about a role assignment entry returned when listing assignments.

id: string

Identifier for the role.

assignment\_sources: array of object { principal\_id, principal\_type }

Principals from which the role assignment is inherited, when available.

principal\_id: string

principal\_type: string

created\_at: number

When the role was created.

formatunixtime

created\_by: string

Identifier of the actor who created the role.

created\_by\_user\_obj: map[unknown]

User details for the actor that created the role, when available.

description: string

Description of the role.

metadata: map[unknown]

Arbitrary metadata stored on the role.

name: string

Name of the role.

permissions: array of string

Permissions associated with the role.

predefined\_role: boolean

Whether the role is predefined by OpenAI.

resource\_type: string

Resource type the role applies to.

updated\_at: number

When the role was last updated.

formatunixtime

RoleDeleteResponse object { deleted, object }

Confirmation payload returned after unassigning a role.

deleted: boolean

Whether the assignment was removed.

object: string

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

#### OrganizationProjectsRoles

##### [List project roles](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

DELETE/projects/{project\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleDeleteResponse object { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

#### OrganizationProjectsData Retention

##### [Retrieve project data retention](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

ProjectDataRetention object { object, type }

Represents a project’s data retention control setting.

object: "project.data\_retention"

The object type, which is always `project.data_retention`.

type: "organization\_default" or "none" or "zero\_data\_retention" or 3 more

The configured project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### OrganizationProjectsSpend Alerts

##### [List project spend alerts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

ProjectSpendAlert object { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

interval: "month"

The time interval for evaluating spend against the threshold.

notification\_channel: object { recipients, type, subject\_prefix }

Email notification settings for a spend alert.

recipients: array of string

Email addresses that receive the spend alert notification.

type: "email"

The notification channel type. Currently only `email` is supported.

subject\_prefix: optional string

Optional subject prefix for alert emails.

object: "project.spend\_alert"

The object type, which is always `project.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

ProjectSpendAlertDeleted object { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

#### OrganizationProjectsCertificates

##### [List project certificates](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

POST/organization/projects/{project\_id}/certificates/deactivate

##### ModelsExpand Collapse

CertificateListResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

CertificateActivateResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

CertificateDeactivateResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.
