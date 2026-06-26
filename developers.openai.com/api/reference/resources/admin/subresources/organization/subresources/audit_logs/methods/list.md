<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/audit_logs/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Audit Logs](/api/reference/resources/admin/subresources/organization/subresources/audit_logs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List audit logs

GET/organization/audit\_logs

List user actions and configuration changes within this organization.

##### Query ParametersExpand Collapse

actor\_emails: optional array of string

Return only events performed by users with these emails.

actor\_ids: optional array of string

Return only events performed by these actors. Can be a user ID, a service account ID, or an api key tracking ID.

after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: optional string

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

effective\_at: optional object { gt, gte, lt, lte }

Return only events whose `effective_at` (Unix seconds) is in this range.

gt: optional number

Return only events whose `effective_at` (Unix seconds) is greater than this value.

gte: optional number

Return only events whose `effective_at` (Unix seconds) is greater than or equal to this value.

lt: optional number

Return only events whose `effective_at` (Unix seconds) is less than this value.

lte: optional number

Return only events whose `effective_at` (Unix seconds) is less than or equal to this value.

event\_types: optional array of "api\_key.created" or "api\_key.updated" or "api\_key.deleted" or 56 more

Return only events with a `type` in one of these values. For example, `project.created`. For all options, see the documentation for the [audit log object](/docs/api-reference/audit-logs/object).

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

limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

project\_ids: optional array of string

Return only events for these projects.

resource\_ids: optional array of string

Return only events performed on these targets. For example, a project ID updated. For ChatGPT connector role events, use the workspace connector resource ID shown in `details.id`, such as `<workspace_id>__<connector_id>`.

tenant\_only: optional boolean

Return only tenant-scoped events associated with this organization. Required for tenant-scoped events such as `role.bound_to_resource` and `role.unbound_from_resource`. When `true`, all supplied event types must be tenant-scoped.

##### ReturnsExpand Collapse

data: array of object { id, effective\_at, type, 57 more }

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

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

### List audit logs

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/audit_logs \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"

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
