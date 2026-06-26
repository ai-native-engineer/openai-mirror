<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/audit_logs/ -->

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

# Audit Logs

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
