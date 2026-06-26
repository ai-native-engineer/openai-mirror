<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/audit_logs/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Audit Logs](/api/reference/java/resources/admin/subresources/organization/subresources/audit_logs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List audit logs

AuditLogListPage admin().organization().auditLogs().list(AuditLogListParamsparams = AuditLogListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/audit\_logs

List user actions and configuration changes within this organization.

##### ParametersExpand Collapse

AuditLogListParams params

Optional<List<String>> actorEmails

Return only events performed by users with these emails.

Optional<List<String>> actorIds

Return only events performed by these actors. Can be a user ID, a service account ID, or an api key tracking ID.

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<String> before

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Optional<[EffectiveAt](/api/reference/java/resources/admin/subresources/organization/subresources/audit_logs/methods/list#(resource)%20admin.organization.audit_logs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20effective_at%20%3E%20(schema))> effectiveAt

Return only events whose `effective_at` (Unix seconds) is in this range.

Optional<Long> gt

Return only events whose `effective_at` (Unix seconds) is greater than this value.

Optional<Long> gte

Return only events whose `effective_at` (Unix seconds) is greater than or equal to this value.

Optional<Long> lt

Return only events whose `effective_at` (Unix seconds) is less than this value.

Optional<Long> lte

Return only events whose `effective_at` (Unix seconds) is less than or equal to this value.

Optional<List<EventType>> eventTypes

Return only events with a `type` in one of these values. For example, `project.created`. For all options, see the documentation for the [audit log object](https://platform.openai.com/docs/api-reference/audit-logs/object).

API\_KEY\_CREATED("api\_key.created")

API\_KEY\_UPDATED("api\_key.updated")

API\_KEY\_DELETED("api\_key.deleted")

CERTIFICATE\_CREATED("certificate.created")

CERTIFICATE\_UPDATED("certificate.updated")

CERTIFICATE\_DELETED("certificate.deleted")

CERTIFICATES\_ACTIVATED("certificates.activated")

CERTIFICATES\_DEACTIVATED("certificates.deactivated")

CHECKPOINT\_PERMISSION\_CREATED("checkpoint.permission.created")

CHECKPOINT\_PERMISSION\_DELETED("checkpoint.permission.deleted")

EXTERNAL\_KEY\_REGISTERED("external\_key.registered")

EXTERNAL\_KEY\_REMOVED("external\_key.removed")

GROUP\_CREATED("group.created")

GROUP\_UPDATED("group.updated")

GROUP\_DELETED("group.deleted")

INVITE\_SENT("invite.sent")

INVITE\_ACCEPTED("invite.accepted")

INVITE\_DELETED("invite.deleted")

IP\_ALLOWLIST\_CREATED("ip\_allowlist.created")

IP\_ALLOWLIST\_UPDATED("ip\_allowlist.updated")

IP\_ALLOWLIST\_DELETED("ip\_allowlist.deleted")

IP\_ALLOWLIST\_CONFIG\_ACTIVATED("ip\_allowlist.config.activated")

IP\_ALLOWLIST\_CONFIG\_DEACTIVATED("ip\_allowlist.config.deactivated")

LOGIN\_SUCCEEDED("login.succeeded")

LOGIN\_FAILED("login.failed")

LOGOUT\_SUCCEEDED("logout.succeeded")

LOGOUT\_FAILED("logout.failed")

ORGANIZATION\_UPDATED("organization.updated")

PROJECT\_CREATED("project.created")

PROJECT\_UPDATED("project.updated")

PROJECT\_ARCHIVED("project.archived")

PROJECT\_DELETED("project.deleted")

RATE\_LIMIT\_UPDATED("rate\_limit.updated")

RATE\_LIMIT\_DELETED("rate\_limit.deleted")

RESOURCE\_DELETED("resource.deleted")

TUNNEL\_CREATED("tunnel.created")

TUNNEL\_UPDATED("tunnel.updated")

TUNNEL\_DELETED("tunnel.deleted")

WORKLOAD\_IDENTITY\_PROVIDER\_CREATED("workload\_identity\_provider.created")

WORKLOAD\_IDENTITY\_PROVIDER\_UPDATED("workload\_identity\_provider.updated")

WORKLOAD\_IDENTITY\_PROVIDER\_DELETED("workload\_identity\_provider.deleted")

WORKLOAD\_IDENTITY\_PROVIDER\_MAPPING\_CREATED("workload\_identity\_provider\_mapping.created")

WORKLOAD\_IDENTITY\_PROVIDER\_MAPPING\_UPDATED("workload\_identity\_provider\_mapping.updated")

WORKLOAD\_IDENTITY\_PROVIDER\_MAPPING\_DELETED("workload\_identity\_provider\_mapping.deleted")

ROLE\_CREATED("role.created")

ROLE\_UPDATED("role.updated")

ROLE\_DELETED("role.deleted")

ROLE\_ASSIGNMENT\_CREATED("role.assignment.created")

ROLE\_ASSIGNMENT\_DELETED("role.assignment.deleted")

ROLE\_BOUND\_TO\_RESOURCE("role.bound\_to\_resource")

ROLE\_UNBOUND\_FROM\_RESOURCE("role.unbound\_from\_resource")

SCIM\_ENABLED("scim.enabled")

SCIM\_DISABLED("scim.disabled")

SERVICE\_ACCOUNT\_CREATED("service\_account.created")

SERVICE\_ACCOUNT\_UPDATED("service\_account.updated")

SERVICE\_ACCOUNT\_DELETED("service\_account.deleted")

USER\_ADDED("user.added")

USER\_UPDATED("user.updated")

USER\_DELETED("user.deleted")

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<List<String>> projectIds

Return only events for these projects.

Optional<List<String>> resourceIds

Return only events performed on these targets. For example, a project ID updated. For ChatGPT connector role events, use the workspace connector resource ID shown in `details.id`, such as `<workspace_id>__<connector_id>`.

Optional<Boolean> tenantOnly

Return only tenant-scoped events associated with this organization. Required for tenant-scoped events such as `role.bound_to_resource` and `role.unbound_from_resource`. When `true`, all supplied event types must be tenant-scoped.

##### ReturnsExpand Collapse

class AuditLogListResponse:

A log of a user action or configuration change within this organization.

String id

The ID of this log.

long effectiveAt

The Unix timestamp (in seconds) of the event.

formatunixtime

Type type

The event type.

One of the following:

API\_KEY\_CREATED("api\_key.created")

API\_KEY\_UPDATED("api\_key.updated")

API\_KEY\_DELETED("api\_key.deleted")

CERTIFICATE\_CREATED("certificate.created")

CERTIFICATE\_UPDATED("certificate.updated")

CERTIFICATE\_DELETED("certificate.deleted")

CERTIFICATES\_ACTIVATED("certificates.activated")

CERTIFICATES\_DEACTIVATED("certificates.deactivated")

CHECKPOINT\_PERMISSION\_CREATED("checkpoint.permission.created")

CHECKPOINT\_PERMISSION\_DELETED("checkpoint.permission.deleted")

EXTERNAL\_KEY\_REGISTERED("external\_key.registered")

EXTERNAL\_KEY\_REMOVED("external\_key.removed")

GROUP\_CREATED("group.created")

GROUP\_UPDATED("group.updated")

GROUP\_DELETED("group.deleted")

INVITE\_SENT("invite.sent")

INVITE\_ACCEPTED("invite.accepted")

INVITE\_DELETED("invite.deleted")

IP\_ALLOWLIST\_CREATED("ip\_allowlist.created")

IP\_ALLOWLIST\_UPDATED("ip\_allowlist.updated")

IP\_ALLOWLIST\_DELETED("ip\_allowlist.deleted")

IP\_ALLOWLIST\_CONFIG\_ACTIVATED("ip\_allowlist.config.activated")

IP\_ALLOWLIST\_CONFIG\_DEACTIVATED("ip\_allowlist.config.deactivated")

LOGIN\_SUCCEEDED("login.succeeded")

LOGIN\_FAILED("login.failed")

LOGOUT\_SUCCEEDED("logout.succeeded")

LOGOUT\_FAILED("logout.failed")

ORGANIZATION\_UPDATED("organization.updated")

PROJECT\_CREATED("project.created")

PROJECT\_UPDATED("project.updated")

PROJECT\_ARCHIVED("project.archived")

PROJECT\_DELETED("project.deleted")

RATE\_LIMIT\_UPDATED("rate\_limit.updated")

RATE\_LIMIT\_DELETED("rate\_limit.deleted")

RESOURCE\_DELETED("resource.deleted")

TUNNEL\_CREATED("tunnel.created")

TUNNEL\_UPDATED("tunnel.updated")

TUNNEL\_DELETED("tunnel.deleted")

WORKLOAD\_IDENTITY\_PROVIDER\_CREATED("workload\_identity\_provider.created")

WORKLOAD\_IDENTITY\_PROVIDER\_UPDATED("workload\_identity\_provider.updated")

WORKLOAD\_IDENTITY\_PROVIDER\_DELETED("workload\_identity\_provider.deleted")

WORKLOAD\_IDENTITY\_PROVIDER\_MAPPING\_CREATED("workload\_identity\_provider\_mapping.created")

WORKLOAD\_IDENTITY\_PROVIDER\_MAPPING\_UPDATED("workload\_identity\_provider\_mapping.updated")

WORKLOAD\_IDENTITY\_PROVIDER\_MAPPING\_DELETED("workload\_identity\_provider\_mapping.deleted")

ROLE\_CREATED("role.created")

ROLE\_UPDATED("role.updated")

ROLE\_DELETED("role.deleted")

ROLE\_ASSIGNMENT\_CREATED("role.assignment.created")

ROLE\_ASSIGNMENT\_DELETED("role.assignment.deleted")

ROLE\_BOUND\_TO\_RESOURCE("role.bound\_to\_resource")

ROLE\_UNBOUND\_FROM\_RESOURCE("role.unbound\_from\_resource")

SCIM\_ENABLED("scim.enabled")

SCIM\_DISABLED("scim.disabled")

SERVICE\_ACCOUNT\_CREATED("service\_account.created")

SERVICE\_ACCOUNT\_UPDATED("service\_account.updated")

SERVICE\_ACCOUNT\_DELETED("service\_account.deleted")

USER\_ADDED("user.added")

USER\_UPDATED("user.updated")

USER\_DELETED("user.deleted")

Optional<Actor> actor

The actor who performed the audit logged action.

Optional<ApiKey> apiKey

The API Key used to perform the audit logged action.

Optional<String> id

The tracking id of the API key.

Optional<ServiceAccount> serviceAccount

The service account that performed the audit logged action.

Optional<String> id

The service account id.

Optional<Type> type

The type of API key. Can be either `user` or `service_account`.

One of the following:

USER("user")

SERVICE\_ACCOUNT("service\_account")

Optional<User> user

The user who performed the audit logged action.

Optional<String> id

The user id.

Optional<String> email

The user email.

Optional<Session> session

The session in which the audit logged action was performed.

Optional<String> ipAddress

The IP address from which the action was performed.

Optional<User> user

The user who performed the audit logged action.

Optional<String> id

The user id.

Optional<String> email

The user email.

Optional<Type> type

The type of actor. Is either `session` or `api_key`.

One of the following:

SESSION("session")

API\_KEY("api\_key")

Optional<ApiKeyCreated> apiKeyCreated

The details for events with this `type`.

Optional<String> id

The tracking ID of the API key.

Optional<Data> data

The payload used to create the API key.

Optional<List<String>> scopes

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

Optional<ApiKeyDeleted> apiKeyDeleted

The details for events with this `type`.

Optional<String> id

The tracking ID of the API key.

Optional<ApiKeyUpdated> apiKeyUpdated

The details for events with this `type`.

Optional<String> id

The tracking ID of the API key.

Optional<ChangesRequested> changesRequested

The payload used to update the API key.

Optional<List<String>> scopes

A list of scopes allowed for the API key, e.g. `["api.model.request"]`

Optional<CertificateCreated> certificateCreated

The details for events with this `type`.

Optional<String> id

The certificate ID.

Optional<String> name

The name of the certificate.

Optional<CertificateDeleted> certificateDeleted

The details for events with this `type`.

Optional<String> id

The certificate ID.

Optional<String> certificate

The certificate content in PEM format.

Optional<String> name

The name of the certificate.

Optional<CertificateUpdated> certificateUpdated

The details for events with this `type`.

Optional<String> id

The certificate ID.

Optional<String> name

The name of the certificate.

Optional<CertificatesActivated> certificatesActivated

The details for events with this `type`.

Optional<List<Certificate>> certificates

Optional<String> id

The certificate ID.

Optional<String> name

The name of the certificate.

Optional<CertificatesDeactivated> certificatesDeactivated

The details for events with this `type`.

Optional<List<Certificate>> certificates

Optional<String> id

The certificate ID.

Optional<String> name

The name of the certificate.

Optional<CheckpointPermissionCreated> checkpointPermissionCreated

The project and fine-tuned model checkpoint that the checkpoint permission was created for.

Optional<String> id

The ID of the checkpoint permission.

Optional<Data> data

The payload used to create the checkpoint permission.

Optional<String> fineTunedModelCheckpoint

The ID of the fine-tuned model checkpoint.

Optional<String> projectId

The ID of the project that the checkpoint permission was created for.

Optional<CheckpointPermissionDeleted> checkpointPermissionDeleted

The details for events with this `type`.

Optional<String> id

The ID of the checkpoint permission.

Optional<ExternalKeyRegistered> externalKeyRegistered

The details for events with this `type`.

Optional<String> id

The ID of the external key configuration.

Optional<JsonValue> data

The configuration for the external key.

Optional<ExternalKeyRemoved> externalKeyRemoved

The details for events with this `type`.

Optional<String> id

The ID of the external key configuration.

Optional<GroupCreated> groupCreated

The details for events with this `type`.

Optional<String> id

The ID of the group.

Optional<Data> data

Information about the created group.

Optional<String> groupName

The group name.

Optional<GroupDeleted> groupDeleted

The details for events with this `type`.

Optional<String> id

The ID of the group.

Optional<GroupUpdated> groupUpdated

The details for events with this `type`.

Optional<String> id

The ID of the group.

Optional<ChangesRequested> changesRequested

The payload used to update the group.

Optional<String> groupName

The updated group name.

Optional<InviteAccepted> inviteAccepted

The details for events with this `type`.

Optional<String> id

The ID of the invite.

Optional<InviteDeleted> inviteDeleted

The details for events with this `type`.

Optional<String> id

The ID of the invite.

Optional<InviteSent> inviteSent

The details for events with this `type`.

Optional<String> id

The ID of the invite.

Optional<Data> data

The payload used to create the invite.

Optional<String> email

The email invited to the organization.

Optional<String> role

The role the email was invited to be. Is either `owner` or `member`.

Optional<IpAllowlistConfigActivated> ipAllowlistConfigActivated

The details for events with this `type`.

Optional<List<Config>> configs

The configurations that were activated.

Optional<String> id

The ID of the IP allowlist configuration.

Optional<String> name

The name of the IP allowlist configuration.

Optional<IpAllowlistConfigDeactivated> ipAllowlistConfigDeactivated

The details for events with this `type`.

Optional<List<Config>> configs

The configurations that were deactivated.

Optional<String> id

The ID of the IP allowlist configuration.

Optional<String> name

The name of the IP allowlist configuration.

Optional<IpAllowlistCreated> ipAllowlistCreated

The details for events with this `type`.

Optional<String> id

The ID of the IP allowlist configuration.

Optional<List<String>> allowedIps

The IP addresses or CIDR ranges included in the configuration.

Optional<String> name

The name of the IP allowlist configuration.

Optional<IpAllowlistDeleted> ipAllowlistDeleted

The details for events with this `type`.

Optional<String> id

The ID of the IP allowlist configuration.

Optional<List<String>> allowedIps

The IP addresses or CIDR ranges that were in the configuration.

Optional<String> name

The name of the IP allowlist configuration.

Optional<IpAllowlistUpdated> ipAllowlistUpdated

The details for events with this `type`.

Optional<String> id

The ID of the IP allowlist configuration.

Optional<List<String>> allowedIps

The updated set of IP addresses or CIDR ranges in the configuration.

Optional<LoginFailed> loginFailed

The details for events with this `type`.

Optional<String> errorCode

The error code of the failure.

Optional<String> errorMessage

The error message of the failure.

Optional<JsonValue> loginSucceeded

This event has no additional fields beyond the standard audit log attributes.

Optional<LogoutFailed> logoutFailed

The details for events with this `type`.

Optional<String> errorCode

The error code of the failure.

Optional<String> errorMessage

The error message of the failure.

Optional<JsonValue> logoutSucceeded

This event has no additional fields beyond the standard audit log attributes.

Optional<OrganizationUpdated> organizationUpdated

The details for events with this `type`.

Optional<String> id

The organization ID.

Optional<ChangesRequested> changesRequested

The payload used to update the organization settings.

Optional<String> apiCallLogging

How your organization logs data from supported API calls. One of `disabled`, `enabled_per_call`, `enabled_for_all_projects`, or `enabled_for_selected_projects`

Optional<String> apiCallLoggingProjectIds

The list of project ids if api\_call\_logging is set to `enabled_for_selected_projects`

Optional<String> description

The organization description.

Optional<String> name

The organization name.

Optional<String> threadsUiVisibility

Visibility of the threads page which shows messages created with the Assistants API and Playground. One of `ANY_ROLE`, `OWNERS`, or `NONE`.

Optional<String> title

The organization title.

Optional<String> usageDashboardVisibility

Visibility of the usage dashboard which shows activity and costs for your organization. One of `ANY_ROLE` or `OWNERS`.

Optional<Project> project

The project that the action was scoped to. Absent for actions not scoped to projects. Note that any admin actions taken via Admin API keys are associated with the default project.

Optional<String> id

The project ID.

Optional<String> name

The project title.

Optional<ProjectArchived> projectArchived

The details for events with this `type`.

Optional<String> id

The project ID.

Optional<ProjectCreated> projectCreated

The details for events with this `type`.

Optional<String> id

The project ID.

Optional<Data> data

The payload used to create the project.

Optional<String> name

The project name.

Optional<String> title

The title of the project as seen on the dashboard.

Optional<ProjectDeleted> projectDeleted

The details for events with this `type`.

Optional<String> id

The project ID.

Optional<ProjectUpdated> projectUpdated

The details for events with this `type`.

Optional<String> id

The project ID.

Optional<ChangesRequested> changesRequested

The payload used to update the project.

Optional<String> title

The title of the project as seen on the dashboard.

Optional<RateLimitDeleted> rateLimitDeleted

The details for events with this `type`.

Optional<String> id

The rate limit ID

Optional<RateLimitUpdated> rateLimitUpdated

The details for events with this `type`.

Optional<String> id

The rate limit ID

Optional<ChangesRequested> changesRequested

The payload used to update the rate limits.

Optional<Long> batch1DayMaxInputTokens

The maximum batch input tokens per day. Only relevant for certain models.

Optional<Long> maxAudioMegabytesPer1Minute

The maximum audio megabytes per minute. Only relevant for certain models.

Optional<Long> maxImagesPer1Minute

The maximum images per minute. Only relevant for certain models.

Optional<Long> maxRequestsPer1Day

The maximum requests per day. Only relevant for certain models.

Optional<Long> maxRequestsPer1Minute

The maximum requests per minute.

Optional<Long> maxTokensPer1Minute

The maximum tokens per minute.

Optional<RoleAssignmentCreated> roleAssignmentCreated

The details for events with this `type`.

Optional<String> id

The identifier of the role assignment.

Optional<String> principalId

The principal (user or group) that received the role.

Optional<String> principalType

The type of principal (user or group) that received the role.

Optional<String> resourceId

The resource the role assignment is scoped to.

Optional<String> resourceType

The type of resource the role assignment is scoped to.

Optional<RoleAssignmentDeleted> roleAssignmentDeleted

The details for events with this `type`.

Optional<String> id

The identifier of the role assignment.

Optional<String> principalId

The principal (user or group) that had the role removed.

Optional<String> principalType

The type of principal (user or group) that had the role removed.

Optional<String> resourceId

The resource the role assignment was scoped to.

Optional<String> resourceType

The type of resource the role assignment was scoped to.

Optional<RoleBoundToResource> roleBoundToResource

The details for events with this `type`.

Optional<String> id

The ID of the resource the role was bound to. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

Optional<String> connectorId

The connector ID for a ChatGPT workspace connector resource.

Optional<String> connectorName

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

Optional<Boolean> enabled

Whether the connector is enabled for the role.

Optional<List<String>> permissions

The permissions granted to the role for the resource.

Optional<String> resourceId

The ID of the resource the role was bound to.

Optional<String> resourceType

The type of resource the role was bound to.

Optional<String> roleId

The ID of the role that was bound to the resource.

Optional<Source> source

The connector role mutation path that produced the event.

One of the following:

ROLE\_TOGGLE("role\_toggle")

ROLE\_CONNECTOR\_UPDATE("role\_connector\_update")

ROLE\_DELETE("role\_delete")

WORKSPACE\_PERMISSIONS("workspace\_permissions")

CONNECTOR\_PUBLISH("connector\_publish")

Optional<String> workspaceId

The workspace ID for a ChatGPT workspace connector resource.

Optional<RoleCreated> roleCreated

The details for events with this `type`.

Optional<String> id

The role ID.

Optional<List<String>> permissions

The permissions granted by the role.

Optional<String> resourceId

The resource the role is scoped to.

Optional<String> resourceType

The type of resource the role belongs to.

Optional<String> roleName

The name of the role.

Optional<RoleDeleted> roleDeleted

The details for events with this `type`.

Optional<String> id

The role ID.

Optional<RoleUnboundFromResource> roleUnboundFromResource

The details for events with this `type`.

Optional<String> id

The ID of the resource the role was unbound from. ChatGPT workspace connector resources use `<workspace_id>__<connector_id>`.

Optional<String> connectorId

The connector ID for a ChatGPT workspace connector resource.

Optional<String> connectorName

The connector display name for a ChatGPT workspace connector resource, or the connector ID when the display name could not be resolved.

Optional<Boolean> enabled

Whether the connector is enabled for the role.

Optional<List<String>> permissions

The permissions remaining for the role after the change.

Optional<String> resourceId

The ID of the resource the role was unbound from.

Optional<String> resourceType

The type of resource the role was unbound from.

Optional<String> roleId

The ID of the role that was unbound from the resource.

Optional<Source> source

The connector role mutation path that produced the event.

One of the following:

ROLE\_TOGGLE("role\_toggle")

ROLE\_CONNECTOR\_UPDATE("role\_connector\_update")

ROLE\_DELETE("role\_delete")

WORKSPACE\_PERMISSIONS("workspace\_permissions")

CONNECTOR\_PUBLISH("connector\_publish")

Optional<String> workspaceId

The workspace ID for a ChatGPT workspace connector resource.

Optional<RoleUpdated> roleUpdated

The details for events with this `type`.

Optional<String> id

The role ID.

Optional<ChangesRequested> changesRequested

The payload used to update the role.

Optional<String> description

The updated role description, when provided.

Optional<JsonValue> metadata

Additional metadata stored on the role.

Optional<List<String>> permissionsAdded

The permissions added to the role.

Optional<List<String>> permissionsRemoved

The permissions removed from the role.

Optional<String> resourceId

The resource the role is scoped to.

Optional<String> resourceType

The type of resource the role belongs to.

Optional<String> roleName

The updated role name, when provided.

Optional<ScimDisabled> scimDisabled

The details for events with this `type`.

Optional<String> id

The ID of the SCIM was disabled for.

Optional<ScimEnabled> scimEnabled

The details for events with this `type`.

Optional<String> id

The ID of the SCIM was enabled for.

Optional<ServiceAccountCreated> serviceAccountCreated

The details for events with this `type`.

Optional<String> id

The service account ID.

Optional<Data> data

The payload used to create the service account.

Optional<String> role

The role of the service account. Is either `owner` or `member`.

Optional<ServiceAccountDeleted> serviceAccountDeleted

The details for events with this `type`.

Optional<String> id

The service account ID.

Optional<ServiceAccountUpdated> serviceAccountUpdated

The details for events with this `type`.

Optional<String> id

The service account ID.

Optional<ChangesRequested> changesRequested

The payload used to updated the service account.

Optional<String> role

The role of the service account. Is either `owner` or `member`.

Optional<UserAdded> userAdded

The details for events with this `type`.

Optional<String> id

The user ID.

Optional<Data> data

The payload used to add the user to the project.

Optional<String> role

The role of the user. Is either `owner` or `member`.

Optional<UserDeleted> userDeleted

The details for events with this `type`.

Optional<String> id

The user ID.

Optional<UserUpdated> userUpdated

The details for events with this `type`.

Optional<String> id

The project ID.

Optional<ChangesRequested> changesRequested

The payload used to update the user.

Optional<String> role

The role of the user. Is either `owner` or `member`.

Optional<WorkloadIdentityProviderMappingCreated> workloadIdentityProviderMappingCreated

The details for events with this `type`.

Optional<String> id

The workload identity provider mapping ID.

Optional<JsonValue> data

The payload used to create the workload identity provider mapping.

Optional<String> identityProviderId

The workload identity provider ID.

Optional<WorkloadIdentityProviderMappingDeleted> workloadIdentityProviderMappingDeleted

The details for events with this `type`.

Optional<String> id

The workload identity provider mapping ID.

Optional<String> identityProviderId

The workload identity provider ID.

Optional<String> projectId

The project ID.

Optional<String> serviceAccountId

The mapped service account ID.

Optional<WorkloadIdentityProviderMappingUpdated> workloadIdentityProviderMappingUpdated

The details for events with this `type`.

Optional<String> id

The workload identity provider mapping ID.

Optional<JsonValue> changesRequested

The payload used to update the workload identity provider mapping.

Optional<String> identityProviderId

The workload identity provider ID.

Optional<WorkloadIdentityProviderCreated> workloadIdentityProviderCreated

The details for events with this `type`.

Optional<String> id

The workload identity provider ID.

Optional<JsonValue> data

The payload used to create the workload identity provider.

Optional<WorkloadIdentityProviderDeleted> workloadIdentityProviderDeleted

The details for events with this `type`.

Optional<String> id

The workload identity provider ID.

Optional<String> name

The workload identity provider name.

Optional<WorkloadIdentityProviderUpdated> workloadIdentityProviderUpdated

The details for events with this `type`.

Optional<String> id

The workload identity provider ID.

Optional<JsonValue> changesRequested

The payload used to update the workload identity provider.

### List audit logs

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.auditlogs.AuditLogListPage;
import com.openai.models.admin.organization.auditlogs.AuditLogListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AuditLogListPage page = client.admin().organization().auditLogs().list();

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
