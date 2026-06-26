<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/audit_logs/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Audit Logs](/api/reference/go/resources/admin/subresources/organization/subresources/audit_logs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List audit logs

client.Admin.Organization.AuditLogs.List(ctx, query) (\*ConversationCursorPage[[AdminOrganizationAuditLogListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20AdminOrganizationAuditLogListResponse%20%3E%20(schema))], error)

GET/organization/audit\_logs

List user actions and configuration changes within this organization.

##### ParametersExpand Collapse

query AdminOrganizationAuditLogListParams

ActorEmails param.Field[[]string]Optional

Return only events performed by users with these emails.

ActorIDs param.Field[[]string]Optional

Return only events performed by these actors. Can be a user ID, a service account ID, or an api key tracking ID.

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Before param.Field[string]Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

EffectiveAt param.Field[[AdminOrganizationAuditLogListParamsEffectiveAt](/api/reference/go/resources/admin/subresources/organization/subresources/audit_logs/methods/list#(resource)%20admin.organization.audit_logs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20effective_at%20%3E%20(schema))]Optional

Return only events whose `effective_at` (Unix seconds) is in this range.

Gt int64Optional

Return only events whose `effective_at` (Unix seconds) is greater than this value.

Gte int64Optional

Return only events whose `effective_at` (Unix seconds) is greater than or equal to this value.

Lt int64Optional

Return only events whose `effective_at` (Unix seconds) is less than this value.

Lte int64Optional

Return only events whose `effective_at` (Unix seconds) is less than or equal to this value.

EventTypes param.Field[[]string]Optional

Return only events with a `type` in one of these values. For example, `project.created`. For all options, see the documentation for the [audit log object](https://platform.openai.com/docs/api-reference/audit-logs/object).

const AdminOrganizationAuditLogListParamsEventTypeAPIKeyCreated AdminOrganizationAuditLogListParamsEventType = "api\_key.created"

const AdminOrganizationAuditLogListParamsEventTypeAPIKeyUpdated AdminOrganizationAuditLogListParamsEventType = "api\_key.updated"

const AdminOrganizationAuditLogListParamsEventTypeAPIKeyDeleted AdminOrganizationAuditLogListParamsEventType = "api\_key.deleted"

const AdminOrganizationAuditLogListParamsEventTypeCertificateCreated AdminOrganizationAuditLogListParamsEventType = "certificate.created"

const AdminOrganizationAuditLogListParamsEventTypeCertificateUpdated AdminOrganizationAuditLogListParamsEventType = "certificate.updated"

const AdminOrganizationAuditLogListParamsEventTypeCertificateDeleted AdminOrganizationAuditLogListParamsEventType = "certificate.deleted"

const AdminOrganizationAuditLogListParamsEventTypeCertificatesActivated AdminOrganizationAuditLogListParamsEventType = "certificates.activated"

const AdminOrganizationAuditLogListParamsEventTypeCertificatesDeactivated AdminOrganizationAuditLogListParamsEventType = "certificates.deactivated"

const AdminOrganizationAuditLogListParamsEventTypeCheckpointPermissionCreated AdminOrganizationAuditLogListParamsEventType = "checkpoint.permission.created"

const AdminOrganizationAuditLogListParamsEventTypeCheckpointPermissionDeleted AdminOrganizationAuditLogListParamsEventType = "checkpoint.permission.deleted"

const AdminOrganizationAuditLogListParamsEventTypeExternalKeyRegistered AdminOrganizationAuditLogListParamsEventType = "external\_key.registered"

const AdminOrganizationAuditLogListParamsEventTypeExternalKeyRemoved AdminOrganizationAuditLogListParamsEventType = "external\_key.removed"

const AdminOrganizationAuditLogListParamsEventTypeGroupCreated AdminOrganizationAuditLogListParamsEventType = "group.created"

const AdminOrganizationAuditLogListParamsEventTypeGroupUpdated AdminOrganizationAuditLogListParamsEventType = "group.updated"

const AdminOrganizationAuditLogListParamsEventTypeGroupDeleted AdminOrganizationAuditLogListParamsEventType = "group.deleted"

const AdminOrganizationAuditLogListParamsEventTypeInviteSent AdminOrganizationAuditLogListParamsEventType = "invite.sent"

const AdminOrganizationAuditLogListParamsEventTypeInviteAccepted AdminOrganizationAuditLogListParamsEventType = "invite.accepted"

const AdminOrganizationAuditLogListParamsEventTypeInviteDeleted AdminOrganizationAuditLogListParamsEventType = "invite.deleted"

const AdminOrganizationAuditLogListParamsEventTypeIPAllowlistCreated AdminOrganizationAuditLogListParamsEventType = "ip\_allowlist.created"

const AdminOrganizationAuditLogListParamsEventTypeIPAllowlistUpdated AdminOrganizationAuditLogListParamsEventType = "ip\_allowlist.updated"

const AdminOrganizationAuditLogListParamsEventTypeIPAllowlistDeleted AdminOrganizationAuditLogListParamsEventType = "ip\_allowlist.deleted"

const AdminOrganizationAuditLogListParamsEventTypeIPAllowlistConfigActivated AdminOrganizationAuditLogListParamsEventType = "ip\_allowlist.config.activated"

const AdminOrganizationAuditLogListParamsEventTypeIPAllowlistConfigDeactivated AdminOrganizationAuditLogListParamsEventType = "ip\_allowlist.config.deactivated"

const AdminOrganizationAuditLogListParamsEventTypeLoginSucceeded AdminOrganizationAuditLogListParamsEventType = "login.succeeded"

const AdminOrganizationAuditLogListParamsEventTypeLoginFailed AdminOrganizationAuditLogListParamsEventType = "login.failed"

const AdminOrganizationAuditLogListParamsEventTypeLogoutSucceeded AdminOrganizationAuditLogListParamsEventType = "logout.succeeded"

const AdminOrganizationAuditLogListParamsEventTypeLogoutFailed AdminOrganizationAuditLogListParamsEventType = "logout.failed"

const AdminOrganizationAuditLogListParamsEventTypeOrganizationUpdated AdminOrganizationAuditLogListParamsEventType = "organization.updated"

const AdminOrganizationAuditLogListParamsEventTypeProjectCreated AdminOrganizationAuditLogListParamsEventType = "project.created"

const AdminOrganizationAuditLogListParamsEventTypeProjectUpdated AdminOrganizationAuditLogListParamsEventType = "project.updated"

const AdminOrganizationAuditLogListParamsEventTypeProjectArchived AdminOrganizationAuditLogListParamsEventType = "project.archived"

const AdminOrganizationAuditLogListParamsEventTypeProjectDeleted AdminOrganizationAuditLogListParamsEventType = "project.deleted"

const AdminOrganizationAuditLogListParamsEventTypeRateLimitUpdated AdminOrganizationAuditLogListParamsEventType = "rate\_limit.updated"

const AdminOrganizationAuditLogListParamsEventTypeRateLimitDeleted AdminOrganizationAuditLogListParamsEventType = "rate\_limit.deleted"

const AdminOrganizationAuditLogListParamsEventTypeResourceDeleted AdminOrganizationAuditLogListParamsEventType = "resource.deleted"

const AdminOrganizationAuditLogListParamsEventTypeTunnelCreated AdminOrganizationAuditLogListParamsEventType = "tunnel.created"

const AdminOrganizationAuditLogListParamsEventTypeTunnelUpdated AdminOrganizationAuditLogListParamsEventType = "tunnel.updated"

const AdminOrganizationAuditLogListParamsEventTypeTunnelDeleted AdminOrganizationAuditLogListParamsEventType = "tunnel.deleted"

const AdminOrganizationAuditLogListParamsEventTypeWorkloadIdentityProviderCreated AdminOrganizationAuditLogListParamsEventType = "workload\_identity\_provider.created"

const AdminOrganizationAuditLogListParamsEventTypeWorkloadIdentityProviderUpdated AdminOrganizationAuditLogListParamsEventType = "workload\_identity\_provider.updated"

const AdminOrganizationAuditLogListParamsEventTypeWorkloadIdentityProviderDeleted AdminOrganizationAuditLogListParamsEventType = "workload\_identity\_provider.deleted"

const AdminOrganizationAuditLogListParamsEventTypeWorkloadIdentityProviderMappingCreated AdminOrganizationAuditLogListParamsEventType = "workload\_identity\_provider\_mapping.created"

const AdminOrganizationAuditLogListParamsEventTypeWorkloadIdentityProviderMappingUpdated AdminOrganizationAuditLogListParamsEventType = "workload\_identity\_provider\_mapping.updated"

const AdminOrganizationAuditLogListParamsEventTypeWorkloadIdentityProviderMappingDeleted AdminOrganizationAuditLogListParamsEventType = "workload\_identity\_provider\_mapping.deleted"

const AdminOrganizationAuditLogListParamsEventTypeRoleCreated AdminOrganizationAuditLogListParamsEventType = "role.created"

const AdminOrganizationAuditLogListParamsEventTypeRoleUpdated AdminOrganizationAuditLogListParamsEventType = "role.updated"

const AdminOrganizationAuditLogListParamsEventTypeRoleDeleted AdminOrganizationAuditLogListParamsEventType = "role.deleted"

const AdminOrganizationAuditLogListParamsEventTypeRoleAssignmentCreated AdminOrganizationAuditLogListParamsEventType = "role.assignment.created"

const AdminOrganizationAuditLogListParamsEventTypeRoleAssignmentDeleted AdminOrganizationAuditLogListParamsEventType = "role.assignment.deleted"

const AdminOrganizationAuditLogListParamsEventTypeRoleBoundToResource AdminOrganizationAuditLogListParamsEventType = "role.bound\_to\_resource"

const AdminOrganizationAuditLogListParamsEventTypeRoleUnboundFromResource AdminOrganizationAuditLogListParamsEventType = "role.unbound\_from\_resource"

const AdminOrganizationAuditLogListParamsEventTypeScimEnabled AdminOrganizationAuditLogListParamsEventType = "scim.enabled"

const AdminOrganizationAuditLogListParamsEventTypeScimDisabled AdminOrganizationAuditLogListParamsEventType = "scim.disabled"

const AdminOrganizationAuditLogListParamsEventTypeServiceAccountCreated AdminOrganizationAuditLogListParamsEventType = "service\_account.created"

const AdminOrganizationAuditLogListParamsEventTypeServiceAccountUpdated AdminOrganizationAuditLogListParamsEventType = "service\_account.updated"

const AdminOrganizationAuditLogListParamsEventTypeServiceAccountDeleted AdminOrganizationAuditLogListParamsEventType = "service\_account.deleted"

const AdminOrganizationAuditLogListParamsEventTypeUserAdded AdminOrganizationAuditLogListParamsEventType = "user.added"

const AdminOrganizationAuditLogListParamsEventTypeUserUpdated AdminOrganizationAuditLogListParamsEventType = "user.updated"

const AdminOrganizationAuditLogListParamsEventTypeUserDeleted AdminOrganizationAuditLogListParamsEventType = "user.deleted"

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

ProjectIDs param.Field[[]string]Optional

Return only events for these projects.

ResourceIDs param.Field[[]string]Optional

Return only events performed on these targets. For example, a project ID updated. For ChatGPT connector role events, use the workspace connector resource ID shown in `details.id`, such as `<workspace_id>__<connector_id>`.

TenantOnly param.Field[bool]Optional

Return only tenant-scoped events associated with this organization. Required for tenant-scoped events such as `role.bound_to_resource` and `role.unbound_from_resource`. When `true`, all supplied event types must be tenant-scoped.

##### ReturnsExpand Collapse

type AdminOrganizationAuditLogListResponse struct{…}

A log of a user action or configuration change within this organization.

ID string

The ID of this log.

EffectiveAt int64

The Unix timestamp (in seconds) of the event.

formatunixtime

Type AdminOrganizationAuditLogListResponseType

The event type.

One of the following:

const AdminOrganizationAuditLogListResponseTypeAPIKeyCreated AdminOrganizationAuditLogListResponseType = "api\_key.created"

const AdminOrganizationAuditLogListResponseTypeAPIKeyUpdated AdminOrganizationAuditLogListResponseType = "api\_key.updated"

const AdminOrganizationAuditLogListResponseTypeAPIKeyDeleted AdminOrganizationAuditLogListResponseType = "api\_key.deleted"

const AdminOrganizationAuditLogListResponseTypeCertificateCreated AdminOrganizationAuditLogListResponseType = "certificate.created"

const AdminOrganizationAuditLogListResponseTypeCertificateUpdated AdminOrganizationAuditLogListResponseType = "certificate.updated"

const AdminOrganizationAuditLogListResponseTypeCertificateDeleted AdminOrganizationAuditLogListResponseType = "certificate.deleted"

const AdminOrganizationAuditLogListResponseTypeCertificatesActivated AdminOrganizationAuditLogListResponseType = "certificates.activated"

const AdminOrganizationAuditLogListResponseTypeCertificatesDeactivated AdminOrganizationAuditLogListResponseType = "certificates.deactivated"

const AdminOrganizationAuditLogListResponseTypeCheckpointPermissionCreated AdminOrganizationAuditLogListResponseType = "checkpoint.permission.created"

const AdminOrganizationAuditLogListResponseTypeCheckpointPermissionDeleted AdminOrganizationAuditLogListResponseType = "checkpoint.permission.deleted"

const AdminOrganizationAuditLogListResponseTypeExternalKeyRegistered AdminOrganizationAuditLogListResponseType = "external\_key.registered"

const AdminOrganizationAuditLogListResponseTypeExternalKeyRemoved AdminOrganizationAuditLogListResponseType = "external\_key.removed"

const AdminOrganizationAuditLogListResponseTypeGroupCreated AdminOrganizationAuditLogListResponseType = "group.created"

const AdminOrganizationAuditLogListResponseTypeGroupUpdated AdminOrganizationAuditLogListResponseType = "group.updated"

const AdminOrganizationAuditLogListResponseTypeGroupDeleted AdminOrganizationAuditLogListResponseType = "group.deleted"

const AdminOrganizationAuditLogListResponseTypeInviteSent AdminOrganizationAuditLogListResponseType = "invite.sent"

const AdminOrganizationAuditLogListResponseTypeInviteAccepted AdminOrganizationAuditLogListResponseType = "invite.accepted"

const AdminOrganizationAuditLogListResponseTypeInviteDeleted AdminOrganizationAuditLogListResponseType = "invite.deleted"

const AdminOrganizationAuditLogListResponseTypeIPAllowlistCreated AdminOrganizationAuditLogListResponseType = "ip\_allowlist.created"

const AdminOrganizationAuditLogListResponseTypeIPAllowlistUpdated AdminOrganizationAuditLogListResponseType = "ip\_allowlist.updated"

const AdminOrganizationAuditLogListResponseTypeIPAllowlistDeleted AdminOrganizationAuditLogListResponseType = "ip\_allowlist.deleted"

const AdminOrganizationAuditLogListResponseTypeIPAllowlistConfigActivated AdminOrganizationAuditLogListResponseType = "ip\_allowlist.config.activated"

const AdminOrganizationAuditLogListResponseTypeIPAllowlistConfigDeactivated AdminOrganizationAuditLogListResponseType = "ip\_allowlist.config.deactivated"

const AdminOrganizationAuditLogListResponseTypeLoginSucceeded AdminOrganizationAuditLogListResponseType = "login.succeeded"

const AdminOrganizationAuditLogListResponseTypeLoginFailed AdminOrganizationAuditLogListResponseType = "login.failed"

const AdminOrganizationAuditLogListResponseTypeLogoutSucceeded AdminOrganizationAuditLogListResponseType = "logout.succeeded"

const AdminOrganizationAuditLogListResponseTypeLogoutFailed AdminOrganizationAuditLogListResponseType = "logout.failed"

const AdminOrganizationAuditLogListResponseTypeOrganizationUpdated AdminOrganizationAuditLogListResponseType = "organization.updated"

const AdminOrganizationAuditLogListResponseTypeProjectCreated AdminOrganizationAuditLogListResponseType = "project.created"

const AdminOrganizationAuditLogListResponseTypeProjectUpdated AdminOrganizationAuditLogListResponseType = "project.updated"

const AdminOrganizationAuditLogListResponseTypeProjectArchived AdminOrganizationAuditLogListResponseType = "project.archived"

const AdminOrganizationAuditLogListResponseTypeProjectDeleted AdminOrganizationAuditLogListResponseType = "project.deleted"

const AdminOrganizationAuditLogListResponseTypeRateLimitUpdated AdminOrganizationAuditLogListResponseType = "rate\_limit.updated"

const AdminOrganizationAuditLogListResponseTypeRateLimitDeleted AdminOrganizationAuditLogListResponseType = "rate\_limit.deleted"

const AdminOrganizationAuditLogListResponseTypeResourceDeleted AdminOrganizationAuditLogListResponseType = "resource.deleted"

const AdminOrganizationAuditLogListResponseTypeTunnelCreated AdminOrganizationAuditLogListResponseType = "tunnel.created"

const AdminOrganizationAuditLogListResponseTypeTunnelUpdated AdminOrganizationAuditLogListResponseType = "tunnel.updated"

const AdminOrganizationAuditLogListResponseTypeTunnelDeleted AdminOrganizationAuditLogListResponseType = "tunnel.deleted"

const AdminOrganizationAuditLogListResponseTypeWorkloadIdentityProviderCreated AdminOrganizationAuditLogListResponseType = "workload\_identity\_provider.created"

const AdminOrganizationAuditLogListResponseTypeWorkloadIdentityProviderUpdated AdminOrganizationAuditLogListResponseType = "workload\_identity\_provider.updated"

const AdminOrganizationAuditLogListResponseTypeWorkloadIdentityProviderDeleted AdminOrganizationAuditLogListResponseType = "workload\_identity\_provider.deleted"

const AdminOrganizationAuditLogListResponseTypeWorkloadIdentityProviderMappingCreated AdminOrganizationAuditLogListResponseType = "workload\_identity\_provider\_mapping.created"

const AdminOrganizationAuditLogListResponseTypeWorkloadIdentityProviderMappingUpdated AdminOrganizationAuditLogListResponseType = "workload\_identity\_provider\_mapping.updated"

const AdminOrganizationAuditLogListResponseTypeWorkloadIdentityProviderMappingDeleted AdminOrganizationAuditLogListResponseType = "workload\_identity\_provider\_mapping.deleted"

const AdminOrganizationAuditLogListResponseTypeRoleCreated AdminOrganizationAuditLogListResponseType = "role.created"

const AdminOrganizationAuditLogListResponseTypeRoleUpdated AdminOrganizationAuditLogListResponseType = "role.updated"

const AdminOrganizationAuditLogListResponseTypeRoleDeleted AdminOrganizationAuditLogListResponseType = "role.deleted"

const AdminOrganizationAuditLogListResponseTypeRoleAssignmentCreated AdminOrganizationAuditLogListResponseType = "role.assignment.created"

const AdminOrganizationAuditLogListResponseTypeRoleAssignmentDeleted AdminOrganizationAuditLogListResponseType = "role.assignment.deleted"

const AdminOrganizationAuditLogListResponseTypeRoleBoundToResource AdminOrganizationAuditLogListResponseType = "role.bound\_to\_resource"

const AdminOrganizationAuditLogListResponseTypeRoleUnboundFromResource AdminOrganizationAuditLogListResponseType = "role.unbound\_from\_resource"

const AdminOrganizationAuditLogListResponseTypeScimEnabled AdminOrganizationAuditLogListResponseType = "scim.enabled"

const AdminOrganizationAuditLogListResponseTypeScimDisabled AdminOrganizationAuditLogListResponseType = "scim.disabled"

const AdminOrganizationAuditLogListResponseTypeServiceAccountCreated AdminOrganizationAuditLogListResponseType = "service\_account.created"

const AdminOrganizationAuditLogListResponseTypeServiceAccountUpdated AdminOrganizationAuditLogListResponseType = "service\_account.updated"

const AdminOrganizationAuditLogListResponseTypeServiceAccountDeleted AdminOrganizationAuditLogListResponseType = "service\_account.deleted"

const AdminOrganizationAuditLogListResponseTypeUserAdded AdminOrganizationAuditLogListResponseType = "user.added"

const AdminOrganizationAuditLogListResponseTypeUserUpdated AdminOrganizationAuditLogListResponseType = "user.updated"

const AdminOrganizationAuditLogListResponseTypeUserDeleted AdminOrganizationAuditLogListResponseType = "user.deleted"

Actor AdminOrganizationAuditLogListResponseActorOptional

The actor who performed the audit logged action.

APIKey AdminOrganizationAuditLogListResponseActorAPIKeyOptional

The API Key used to perform the audit logged action.

ID stringOptional

The tracking id of the API key.

ServiceAccount AdminOrganizationAuditLogListResponseActorAPIKeyServiceAccountOptional

The service account that performed the audit logged action.

ID stringOptional

The service account id.

Type stringOptional

The type of API key. Can be either `user` or `service_account`.

One of the following:

const AdminOrganizationAuditLogListResponseActorAPIKeyTypeUser AdminOrganizationAuditLogListResponseActorAPIKeyType = "user"

const AdminOrganizationAuditLogListResponseActorAPIKeyTypeServiceAccount AdminOrganizationAuditLogListResponseActorAPIKeyType = "service\_account"

User AdminOrganizationAuditLogListResponseActorAPIKeyUserOptional

The user who performed the audit logged action.

ID stringOptional

The user id.

Email stringOptional

The user email.

Session AdminOrganizationAuditLogListResponseActorSessionOptional

The session in which the audit logged action was performed.

IPAddress stringOptional

The IP address from which the action was performed.

User AdminOrganizationAuditLogListResponseActorSessionUserOptional

The user who performed the audit logged action.

ID stringOptional

The user id.

Email stringOptional

The user email.

Type stringOptional

The type of actor. Is either `session` or `api_key`.

One of the following:

const AdminOrganizationAuditLogListResponseActorTypeSession AdminOrganizationAuditLogListResponseActorType = "session"

const AdminOrganizationAuditLogListResponseActorTypeAPIKey AdminOrganizationAuditLogListResponseActorType = "api\_key"

APIKeyCreated AdminOrganizationAuditLogListResponseAPIKeyCreatedOptional

The details for events with this `type`.

ID stringOptional

The tracking ID of the API key.

Data AdminOrganizationAuditLogListResponseAPIKeyCreatedDataOptional

The payload used to create the API key.

Scopes []stringOptional

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

APIKeyDeleted AdminOrganizationAuditLogListResponseAPIKeyDeletedOptional

The details for events with this `type`.

ID stringOptional

The tracking ID of the API key.

APIKeyUpdated AdminOrganizationAuditLogListResponseAPIKeyUpdatedOptional

The details for events with this `type`.

ID stringOptional

The tracking ID of the API key.

ChangesRequested AdminOrganizationAuditLogListResponseAPIKeyUpdatedChangesRequestedOptional

The payload used to update the API key.

Scopes []stringOptional

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

CertificateCreated AdminOrganizationAuditLogListResponseCertificateCreatedOptional

The details for events with this `type`.

ID stringOptional

The certificate ID.

Name stringOptional

The name of the certificate.

CertificateDeleted AdminOrganizationAuditLogListResponseCertificateDeletedOptional

The details for events with this `type`.

ID stringOptional

The certificate ID.

Certificate stringOptional

The certificate content in PEM format.

Name stringOptional

The name of the certificate.

CertificateUpdated AdminOrganizationAuditLogListResponseCertificateUpdatedOptional

The details for events with this `type`.

ID stringOptional

The certificate ID.

Name stringOptional

The name of the certificate.

CertificatesActivated AdminOrganizationAuditLogListResponseCertificatesActivatedOptional

The details for events with this `type`.

Certificates []AdminOrganizationAuditLogListResponseCertificatesActivatedCertificateOptional

ID stringOptional

The certificate ID.

Name stringOptional

The name of the certificate.

CertificatesDeactivated AdminOrganizationAuditLogListResponseCertificatesDeactivatedOptional

The details for events with this `type`.

Certificates []AdminOrganizationAuditLogListResponseCertificatesDeactivatedCertificateOptional

ID stringOptional

The certificate ID.

Name stringOptional

The name of the certificate.

CheckpointPermissionCreated AdminOrganizationAuditLogListResponseCheckpointPermissionCreatedOptional

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

ID stringOptional

The ID of the checkpoint permission.

Data AdminOrganizationAuditLogListResponseCheckpointPermissionCreatedDataOptional

The payload used to create the checkpoint permission.

FineTunedModelCheckpoint stringOptional

The ID of the fine-tuned model checkpoint.

ProjectID stringOptional

The ID of the project that the checkpoint permission was created for.

CheckpointPermissionDeleted AdminOrganizationAuditLogListResponseCheckpointPermissionDeletedOptional

The details for events with this `type`.

ID stringOptional

The ID of the checkpoint permission.

ExternalKeyRegistered AdminOrganizationAuditLogListResponseExternalKeyRegisteredOptional

The details for events with this `type`.

ID stringOptional

The ID of the external key configuration.

Data anyOptional

The configuration for the external key.

ExternalKeyRemoved AdminOrganizationAuditLogListResponseExternalKeyRemovedOptional

The details for events with this `type`.

ID stringOptional

The ID of the external key configuration.

GroupCreated AdminOrganizationAuditLogListResponseGroupCreatedOptional

The details for events with this `type`.

ID stringOptional

The ID of the group.

Data AdminOrganizationAuditLogListResponseGroupCreatedDataOptional

Information about the created group.

GroupName stringOptional

The group name.

GroupDeleted AdminOrganizationAuditLogListResponseGroupDeletedOptional

The details for events with this `type`.

ID stringOptional

The ID of the group.

GroupUpdated AdminOrganizationAuditLogListResponseGroupUpdatedOptional

The details for events with this `type`.

ID stringOptional

The ID of the group.

ChangesRequested AdminOrganizationAuditLogListResponseGroupUpdatedChangesRequestedOptional

The payload used to update the group.

GroupName stringOptional

The updated group name.

InviteAccepted AdminOrganizationAuditLogListResponseInviteAcceptedOptional

The details for events with this `type`.

ID stringOptional

The ID of the invite.

InviteDeleted AdminOrganizationAuditLogListResponseInviteDeletedOptional

The details for events with this `type`.

ID stringOptional

The ID of the invite.

InviteSent AdminOrganizationAuditLogListResponseInviteSentOptional

The details for events with this `type`.

ID stringOptional

The ID of the invite.

Data AdminOrganizationAuditLogListResponseInviteSentDataOptional

The payload used to create the invite.

Email stringOptional

The email invited to the organization.

Role stringOptional

The role the email was invited to be. Is either `owner` or `member`.

IPAllowlistConfigActivated AdminOrganizationAuditLogListResponseIPAllowlistConfigActivatedOptional

The details for events with this `type`.

Configs []AdminOrganizationAuditLogListResponseIPAllowlistConfigActivatedConfigOptional

The configurations that were activated.

ID stringOptional

The ID of the IP allowlist configuration.

Name stringOptional

The name of the IP allowlist configuration.

IPAllowlistConfigDeactivated AdminOrganizationAuditLogListResponseIPAllowlistConfigDeactivatedOptional

The details for events with this `type`.

Configs []AdminOrganizationAuditLogListResponseIPAllowlistConfigDeactivatedConfigOptional

The configurations that were deactivated.

ID stringOptional

The ID of the IP allowlist configuration.

Name stringOptional

The name of the IP allowlist configuration.

IPAllowlistCreated AdminOrganizationAuditLogListResponseIPAllowlistCreatedOptional

The details for events with this `type`.

ID stringOptional

The ID of the IP allowlist configuration.

AllowedIPs []stringOptional

The IP addresses or CIDR ranges included in the configuration.

Name stringOptional

The name of the IP allowlist configuration.

IPAllowlistDeleted AdminOrganizationAuditLogListResponseIPAllowlistDeletedOptional

The details for events with this `type`.

ID stringOptional

The ID of the IP allowlist configuration.

AllowedIPs []stringOptional

The IP addresses or CIDR ranges that were in the configuration.

Name stringOptional

The name of the IP allowlist configuration.

IPAllowlistUpdated AdminOrganizationAuditLogListResponseIPAllowlistUpdatedOptional

The details for events with this `type`.

ID stringOptional

The ID of the IP allowlist configuration.

AllowedIPs []stringOptional

The updated set of IP addresses or CIDR ranges in the configuration.

LoginFailed AdminOrganizationAuditLogListResponseLoginFailedOptional

The details for events with this `type`.

ErrorCode stringOptional

The error code of the failure.

ErrorMessage stringOptional

The error message of the failure.

LoginSucceeded anyOptional

This event has no additional fields beyond the standard audit log attributes.

LogoutFailed AdminOrganizationAuditLogListResponseLogoutFailedOptional

The details for events with this `type`.

ErrorCode stringOptional

The error code of the failure.

ErrorMessage stringOptional

The error message of the failure.

LogoutSucceeded anyOptional

This event has no additional fields beyond the standard audit log attributes.

OrganizationUpdated AdminOrganizationAuditLogListResponseOrganizationUpdatedOptional

The details for events with this `type`.

ID stringOptional

The organization ID.

ChangesRequested AdminOrganizationAuditLogListResponseOrganizationUpdatedChangesRequestedOptional

The payload used to update the organization settings.

APICallLogging stringOptional

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

APICallLoggingProjectIDs stringOptional

The list of project ids if api\_call\_logging is set to `enabled_for_selected_projects`

Description stringOptional

The organization description.

Name stringOptional

The organization name.

ThreadsUiVisibility stringOptional

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

Title stringOptional

The organization title.

UsageDashboardVisibility stringOptional

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

Project AdminOrganizationAuditLogListResponseProjectOptional

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

ID stringOptional

The project ID.

Name stringOptional

The project title.

ProjectArchived AdminOrganizationAuditLogListResponseProjectArchivedOptional

The details for events with this `type`.

ID stringOptional

The project ID.

ProjectCreated AdminOrganizationAuditLogListResponseProjectCreatedOptional

The details for events with this `type`.

ID stringOptional

The project ID.

Data AdminOrganizationAuditLogListResponseProjectCreatedDataOptional

The payload used to create the project.

Name stringOptional

The project name.

Title stringOptional

The title of the project as seen on the dashboard.

ProjectDeleted AdminOrganizationAuditLogListResponseProjectDeletedOptional

The details for events with this `type`.

ID stringOptional

The project ID.

ProjectUpdated AdminOrganizationAuditLogListResponseProjectUpdatedOptional

The details for events with this `type`.

ID stringOptional

The project ID.

ChangesRequested AdminOrganizationAuditLogListResponseProjectUpdatedChangesRequestedOptional

The payload used to update the project.

Title stringOptional

The title of the project as seen on the dashboard.

RateLimitDeleted AdminOrganizationAuditLogListResponseRateLimitDeletedOptional

The details for events with this `type`.

ID stringOptional

The rate limit ID

RateLimitUpdated AdminOrganizationAuditLogListResponseRateLimitUpdatedOptional

The details for events with this `type`.

ID stringOptional

The rate limit ID

ChangesRequested AdminOrganizationAuditLogListResponseRateLimitUpdatedChangesRequestedOptional

The payload used to update the rate limits.

Batch1DayMaxInputTokens int64Optional

The maximum batch input tokens per day. Only relevant for certain models.

MaxAudioMegabytesPer1Minute int64Optional

The maximum audio megabytes per minute. Only relevant for certain models.

MaxImagesPer1Minute int64Optional

The maximum images per minute. Only relevant for certain models.

MaxRequestsPer1Day int64Optional

The maximum requests per day. Only relevant for certain models.

MaxRequestsPer1Minute int64Optional

The maximum requests per minute.

MaxTokensPer1Minute int64Optional

The maximum tokens per minute.

RoleAssignmentCreated AdminOrganizationAuditLogListResponseRoleAssignmentCreatedOptional

The details for events with this `type`.

ID stringOptional

The identifier of the role assignment.

PrincipalID stringOptional

The principal (user or group) that received the role.

PrincipalType stringOptional

The type of principal (user or group) that received the role.

ResourceID stringOptional

The resource the role assignment is scoped to.

ResourceType stringOptional

The type of resource the role assignment is scoped to.

RoleAssignmentDeleted AdminOrganizationAuditLogListResponseRoleAssignmentDeletedOptional

The details for events with this `type`.

ID stringOptional

The identifier of the role assignment.

PrincipalID stringOptional

The principal (user or group) that had the role removed.

PrincipalType stringOptional

The type of principal (user or group) that had the role removed.

ResourceID stringOptional

The resource the role assignment was scoped to.

ResourceType stringOptional

The type of resource the role assignment was scoped to.

RoleBoundToResource AdminOrganizationAuditLogListResponseRoleBoundToResourceOptional

The details for events with this `type`.

ID stringOptional

The ID of the resource the role was bound to. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

ConnectorID stringOptional

The connector ID for a ChatGPT workspace connector resource.

ConnectorName stringOptional

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

Enabled boolOptional

Whether the connector is enabled for the role.

Permissions []stringOptional

The permissions granted to the role for the resource.

ResourceID stringOptional

The ID of the resource the role was bound to.

ResourceType stringOptional

The type of resource the role was bound to.

RoleID stringOptional

The ID of the role that was bound to the resource.

Source stringOptional

The connector role mutation path that produced the event.

One of the following:

const AdminOrganizationAuditLogListResponseRoleBoundToResourceSourceRoleToggle AdminOrganizationAuditLogListResponseRoleBoundToResourceSource = "role\_toggle"

const AdminOrganizationAuditLogListResponseRoleBoundToResourceSourceRoleConnectorUpdate AdminOrganizationAuditLogListResponseRoleBoundToResourceSource = "role\_connector\_update"

const AdminOrganizationAuditLogListResponseRoleBoundToResourceSourceRoleDelete AdminOrganizationAuditLogListResponseRoleBoundToResourceSource = "role\_delete"

const AdminOrganizationAuditLogListResponseRoleBoundToResourceSourceWorkspacePermissions AdminOrganizationAuditLogListResponseRoleBoundToResourceSource = "workspace\_permissions"

const AdminOrganizationAuditLogListResponseRoleBoundToResourceSourceConnectorPublish AdminOrganizationAuditLogListResponseRoleBoundToResourceSource = "connector\_publish"

WorkspaceID stringOptional

The workspace ID for a ChatGPT workspace connector resource.

RoleCreated AdminOrganizationAuditLogListResponseRoleCreatedOptional

The details for events with this `type`.

ID stringOptional

The role ID.

Permissions []stringOptional

The permissions granted by the role.

ResourceID stringOptional

The resource the role is scoped to.

ResourceType stringOptional

The type of resource the role belongs to.

RoleName stringOptional

The name of the role.

RoleDeleted AdminOrganizationAuditLogListResponseRoleDeletedOptional

The details for events with this `type`.

ID stringOptional

The role ID.

RoleUnboundFromResource AdminOrganizationAuditLogListResponseRoleUnboundFromResourceOptional

The details for events with this `type`.

ID stringOptional

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

ConnectorID stringOptional

The connector ID for a ChatGPT workspace connector resource.

ConnectorName stringOptional

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

Enabled boolOptional

Whether the connector is enabled for the role.

Permissions []stringOptional

The permissions remaining for the role after the change.

ResourceID stringOptional

The ID of the resource the role was unbound from.

ResourceType stringOptional

The type of resource the role was unbound from.

RoleID stringOptional

The ID of the role that was unbound from the resource.

Source stringOptional

The connector role mutation path that produced the event.

One of the following:

const AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSourceRoleToggle AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSource = "role\_toggle"

const AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSourceRoleConnectorUpdate AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSource = "role\_connector\_update"

const AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSourceRoleDelete AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSource = "role\_delete"

const AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSourceWorkspacePermissions AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSource = "workspace\_permissions"

const AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSourceConnectorPublish AdminOrganizationAuditLogListResponseRoleUnboundFromResourceSource = "connector\_publish"

WorkspaceID stringOptional

The workspace ID for a ChatGPT workspace connector resource.

RoleUpdated AdminOrganizationAuditLogListResponseRoleUpdatedOptional

The details for events with this `type`.

ID stringOptional

The role ID.

ChangesRequested AdminOrganizationAuditLogListResponseRoleUpdatedChangesRequestedOptional

The payload used to update the role.

Description stringOptional

The updated role description, when provided.

Metadata anyOptional

Additional metadata stored on the role.

PermissionsAdded []stringOptional

The permissions added to the role.

PermissionsRemoved []stringOptional

The permissions removed from the role.

ResourceID stringOptional

The resource the role is scoped to.

ResourceType stringOptional

The type of resource the role belongs to.

RoleName stringOptional

The updated role name, when provided.

ScimDisabled AdminOrganizationAuditLogListResponseScimDisabledOptional

The details for events with this `type`.

ID stringOptional

The ID of the SCIM was disabled for.

ScimEnabled AdminOrganizationAuditLogListResponseScimEnabledOptional

The details for events with this `type`.

ID stringOptional

The ID of the SCIM was enabled for.

ServiceAccountCreated AdminOrganizationAuditLogListResponseServiceAccountCreatedOptional

The details for events with this `type`.

ID stringOptional

The service account ID.

Data AdminOrganizationAuditLogListResponseServiceAccountCreatedDataOptional

The payload used to create the service account.

Role stringOptional

The role of the service account. Is either `owner` or `member`.

ServiceAccountDeleted AdminOrganizationAuditLogListResponseServiceAccountDeletedOptional

The details for events with this `type`.

ID stringOptional

The service account ID.

ServiceAccountUpdated AdminOrganizationAuditLogListResponseServiceAccountUpdatedOptional

The details for events with this `type`.

ID stringOptional

The service account ID.

ChangesRequested AdminOrganizationAuditLogListResponseServiceAccountUpdatedChangesRequestedOptional

The payload used to updated the service account.

Role stringOptional

The role of the service account. Is either `owner` or `member`.

UserAdded AdminOrganizationAuditLogListResponseUserAddedOptional

The details for events with this `type`.

ID stringOptional

The user ID.

Data AdminOrganizationAuditLogListResponseUserAddedDataOptional

The payload used to add the user to the project.

Role stringOptional

The role of the user. Is either `owner` or `member`.

UserDeleted AdminOrganizationAuditLogListResponseUserDeletedOptional

The details for events with this `type`.

ID stringOptional

The user ID.

UserUpdated AdminOrganizationAuditLogListResponseUserUpdatedOptional

The details for events with this `type`.

ID stringOptional

The project ID.

ChangesRequested AdminOrganizationAuditLogListResponseUserUpdatedChangesRequestedOptional

The payload used to update the user.

Role stringOptional

The role of the user. Is either `owner` or `member`.

WorkloadIdentityProviderMappingCreated AdminOrganizationAuditLogListResponseWorkloadIdentityProviderMappingCreatedOptional

The details for events with this `type`.

ID stringOptional

The workload identity provider mapping ID.

Data anyOptional

The payload used to create the workload identity provider mapping.

IdentityProviderID stringOptional

The workload identity provider ID.

WorkloadIdentityProviderMappingDeleted AdminOrganizationAuditLogListResponseWorkloadIdentityProviderMappingDeletedOptional

The details for events with this `type`.

ID stringOptional

The workload identity provider mapping ID.

IdentityProviderID stringOptional

The workload identity provider ID.

ProjectID stringOptional

The project ID.

ServiceAccountID stringOptional

The mapped service account ID.

WorkloadIdentityProviderMappingUpdated AdminOrganizationAuditLogListResponseWorkloadIdentityProviderMappingUpdatedOptional

The details for events with this `type`.

ID stringOptional

The workload identity provider mapping ID.

ChangesRequested anyOptional

The payload used to update the workload identity provider mapping.

IdentityProviderID stringOptional

The workload identity provider ID.

WorkloadIdentityProviderCreated AdminOrganizationAuditLogListResponseWorkloadIdentityProviderCreatedOptional

The details for events with this `type`.

ID stringOptional

The workload identity provider ID.

Data anyOptional

The payload used to create the workload identity provider.

WorkloadIdentityProviderDeleted AdminOrganizationAuditLogListResponseWorkloadIdentityProviderDeletedOptional

The details for events with this `type`.

ID stringOptional

The workload identity provider ID.

Name stringOptional

The workload identity provider name.

WorkloadIdentityProviderUpdated AdminOrganizationAuditLogListResponseWorkloadIdentityProviderUpdatedOptional

The details for events with this `type`.

ID stringOptional

The workload identity provider ID.

ChangesRequested anyOptional

The payload used to update the workload identity provider.

### List audit logs

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  page, err := client.Admin.Organization.AuditLogs.List(context.TODO(), openai.AdminOrganizationAuditLogListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

    "object": "list",
    "data": [
            "id": "audit_log-xxx_yyyymmdd",
            "type": "project.archived",
            "effective_at": 1722461446,
            "actor": {
                "type": "api_key",
                "api_key": {
                    "type": "user",
                    "user": {
                        "id": "user-xxx",
                        "email": "user@example.com"
            "project.archived": {
                "id": "proj_abc"
            "id": "audit_log-yyy__20240101",
            "type": "api_key.updated",
            "effective_at": 1720804190,
            "actor": {
                "type": "session",
                "session": {
                    "user": {
                        "id": "user-xxx",
                        "email": "user@example.com"
                    "ip_address": "127.0.0.1",
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "ja3": "a497151ce4338a12c4418c44d375173e",
                    "ja4": "q13d0313h3_55b375c5d22e_c7319ce65786",
                    "ip_address_details": {
                      "country": "US",
                      "city": "San Francisco",
                      "region": "California",
                      "region_code": "CA",
                      "asn": "1234",
                      "latitude": "37.77490",
                      "longitude": "-122.41940"
            "api_key.updated": {
                "id": "key_xxxx",
                "data": {
                    "scopes": ["resource_2.operation_2"]
    ],
    "first_id": "audit_log-xxx__20240101",
    "last_id": "audit_log_yyy__20240101",
    "has_more": true

##### Returns Examples

    "object": "list",
    "data": [
            "id": "audit_log-xxx_yyyymmdd",
            "type": "project.archived",
            "effective_at": 1722461446,
            "actor": {
                "type": "api_key",
                "api_key": {
                    "type": "user",
                    "user": {
                        "id": "user-xxx",
                        "email": "user@example.com"
            "project.archived": {
                "id": "proj_abc"
            "id": "audit_log-yyy__20240101",
            "type": "api_key.updated",
            "effective_at": 1720804190,
            "actor": {
                "type": "session",
                "session": {
                    "user": {
                        "id": "user-xxx",
                        "email": "user@example.com"
                    "ip_address": "127.0.0.1",
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "ja3": "a497151ce4338a12c4418c44d375173e",
                    "ja4": "q13d0313h3_55b375c5d22e_c7319ce65786",
                    "ip_address_details": {
                      "country": "US",
                      "city": "San Francisco",
                      "region": "California",
                      "region_code": "CA",
                      "asn": "1234",
                      "latitude": "37.77490",
                      "longitude": "-122.41940"
            "api_key.updated": {
                "id": "key_xxxx",
                "data": {
                    "scopes": ["resource_2.operation_2"]
    ],
    "first_id": "audit_log-xxx__20240101",
    "last_id": "audit_log_yyy__20240101",
    "has_more": true
