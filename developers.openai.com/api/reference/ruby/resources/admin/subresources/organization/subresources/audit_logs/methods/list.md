<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/audit_logs/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Audit Logs](/api/reference/ruby/resources/admin/subresources/organization/subresources/audit_logs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List audit logs

admin.organization.audit\_logs.list(\*\*kwargs) -> ConversationCursorPage<[AuditLogListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.audit_logs%20%3E%20(model)%20audit_log_list_response%20%3E%20(schema)) { id, effective\_at, type, 57 more } >

GET/organization/audit\_logs

List user actions and configuration changes within this organization.

##### ParametersExpand Collapse

actor\_emails: Array[String]

Return only events performed by users with these emails.

actor\_ids: Array[String]

Return only events performed by these actors. Can be a user ID, a service account ID, or an api key tracking ID.

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: String

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

effective\_at: EffectiveAt{ gt, gte, lt, lte}

Return only events whose `effective_at` (Unix seconds) is in this range.

gt: Integer

Return only events whose `effective_at` (Unix seconds) is greater than this value.

gte: Integer

Return only events whose `effective_at` (Unix seconds) is greater than or equal to this value.

lt: Integer

Return only events whose `effective_at` (Unix seconds) is less than this value.

lte: Integer

Return only events whose `effective_at` (Unix seconds) is less than or equal to this value.

event\_types: Array[:"api\_key.created" | :"api\_key.updated" | :"api\_key.deleted" | 56 more]

Return only events with a `type` in one of these values. For example, `project.created`. For all options, see the documentation for the [audit log object](https://platform.openai.com/docs/api-reference/audit-logs/object).

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

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

project\_ids: Array[String]

Return only events for these projects.

resource\_ids: Array[String]

Return only events performed on these targets. For example, a project ID updated. For ChatGPT connector role events, use the workspace connector resource ID shown in `details.id`, such as `<workspace_id>__<connector_id>`.

tenant\_only: bool

Return only tenant-scoped events associated with this organization. Required for tenant-scoped events such as `role.bound_to_resource` and `role.unbound_from_resource`. When `true`, all supplied event types must be tenant-scoped.

##### ReturnsExpand Collapse

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

### List audit logs

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.audit_logs.list

puts(page)

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
