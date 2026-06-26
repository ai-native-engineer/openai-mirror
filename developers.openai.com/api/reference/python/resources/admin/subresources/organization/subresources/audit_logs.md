<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/audit_logs/ -->

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

# Audit Logs

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
