<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Projects

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

#### ProjectsUsers

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

#### ProjectsUsersRoles

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

#### ProjectsService Accounts

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

#### ProjectsAPI Keys

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

#### ProjectsRate Limits

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

#### ProjectsModel Permissions

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

#### ProjectsHosted Tool Permissions

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

#### ProjectsGroups

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

#### ProjectsGroupsRoles

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

#### ProjectsRoles

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

#### ProjectsData Retention

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

#### ProjectsSpend Alerts

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

#### ProjectsCertificates

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
