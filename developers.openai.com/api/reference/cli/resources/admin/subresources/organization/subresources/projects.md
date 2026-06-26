<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Projects

##### [List projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/list)

$ openai admin:organization:projects list

GET/organization/projects

##### [Create project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/create)

$ openai admin:organization:projects create

POST/organization/projects

##### [Retrieve project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/retrieve)

$ openai admin:organization:projects retrieve

GET/organization/projects/{project\_id}

##### [Modify project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/update)

$ openai admin:organization:projects update

POST/organization/projects/{project\_id}

##### [Archive project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/methods/archive)

$ openai admin:organization:projects archive

POST/organization/projects/{project\_id}/archive

##### ModelsExpand Collapse

project: object { id, created\_at, object, 4 more }

Represents an individual project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the project was created.

object: "organization.project"

The object type, which is always `organization.project`

archived\_at: optional number

The Unix timestamp (in seconds) of when the project was archived or `null`.

external\_key\_id: optional string

The external key associated with the project.

name: optional string

The name of the project. This appears in reporting.

status: optional string

`active` or `archived`

#### ProjectsUsers

##### [List project users](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

$ openai admin:organization:projects:users list

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

$ openai admin:organization:projects:users create

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

$ openai admin:organization:projects:users retrieve

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

$ openai admin:organization:projects:users update

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

$ openai admin:organization:projects:users delete

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

project\_user: object { id, added\_at, object, 3 more }

Represents an individual user in a project.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the project was added.

object: "organization.project.user"

The object type, which is always `organization.project.user`

role: string

`owner` or `member`

email: optional string

The email address of the user

name: optional string

The name of the user

#### ProjectsUsersRoles

##### [List project user role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

$ openai admin:organization:projects:users:roles list

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

$ openai admin:organization:projects:users:roles create

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:users:roles retrieve

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

$ openai admin:organization:projects:users:roles delete

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

#### ProjectsService Accounts

##### [List project service accounts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

$ openai admin:organization:projects:service-accounts list

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

$ openai admin:organization:projects:service-accounts create

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

$ openai admin:organization:projects:service-accounts retrieve

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

$ openai admin:organization:projects:service-accounts update

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

$ openai admin:organization:projects:service-accounts delete

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

project\_service\_account: object { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created

name: string

The name of the service account

object: "organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: "owner" or "member"

`owner` or `member`

"owner"

"member"

#### ProjectsAPI Keys

##### [List project API keys](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

$ openai admin:organization:projects:api-keys list

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

$ openai admin:organization:projects:api-keys retrieve

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

$ openai admin:organization:projects:api-keys delete

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

project\_api\_key: object { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

last\_used\_at: number

The Unix timestamp (in seconds) of when the API key was last used.

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

name: string

The name of the service account.

role: string

The service account’s project role.

type: optional "user" or "service\_account"

`user` or `service_account`

"user"

"service\_account"

user: optional object { id, created\_at, email, 2 more }

The user that owns a project API key.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the user was created.

email: string

The email address of the user.

name: string

The name of the user.

role: string

The user’s project role.

redacted\_value: string

The redacted value of the API key

#### ProjectsRate Limits

##### [List project rate limits](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

$ openai admin:organization:projects:rate-limits list-rate-limits

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

$ openai admin:organization:projects:rate-limits update-rate-limit

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

project\_rate\_limit: object { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

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

##### [Retrieve project model permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

$ openai admin:organization:projects:model-permissions retrieve

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

$ openai admin:organization:projects:model-permissions update

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

$ openai admin:organization:projects:model-permissions delete

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

project\_model\_permissions: object { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: "allow\_list" or "deny\_list"

Whether the project uses an allowlist or a denylist.

"allow\_list"

"deny\_list"

model\_ids: array of string

The model IDs included in the model permissions policy.

object: "project.model\_permissions"

The object type, which is always `project.model_permissions`.

project\_model\_permissions\_deleted: object { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: boolean

Whether the project model permissions were deleted.

object: "project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

#### ProjectsHosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

$ openai admin:organization:projects:hosted-tool-permissions retrieve

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

$ openai admin:organization:projects:hosted-tool-permissions update

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

project\_hosted\_tool\_permissions: object { code\_interpreter, file\_search, image\_generation, 2 more }

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

##### [List project groups](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

$ openai admin:organization:projects:groups list

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

$ openai admin:organization:projects:groups create

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

$ openai admin:organization:projects:groups retrieve

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

$ openai admin:organization:projects:groups delete

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

project\_group: object { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" or "tenant\_group"

The type of the group.

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

#### ProjectsGroupsRoles

##### [List project group role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

$ openai admin:organization:projects:groups:roles list

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

$ openai admin:organization:projects:groups:roles create

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:groups:roles retrieve

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

$ openai admin:organization:projects:groups:roles delete

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

#### ProjectsRoles

##### [List project roles](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

$ openai admin:organization:projects:roles list

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

$ openai admin:organization:projects:roles create

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:roles retrieve

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

$ openai admin:organization:projects:roles update

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

$ openai admin:organization:projects:roles delete

DELETE/projects/{project\_id}/roles/{role\_id}

#### ProjectsData Retention

##### [Retrieve project data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

$ openai admin:organization:projects:data-retention retrieve

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

$ openai admin:organization:projects:data-retention update

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

project\_data\_retention: object { object, type }

Represents a project’s data retention control setting.

object: "project.data\_retention"

The object type, which is always `project.data_retention`.

type: "organization\_default" or "none" or "zero\_data\_retention" or 3 more

The configured project data retention type.

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### ProjectsSpend Alerts

##### [List project spend alerts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/list)

$ openai admin:organization:projects:spend-alerts list

GET/organization/projects/{project\_id}/spend\_alerts

##### [Create project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/create)

$ openai admin:organization:projects:spend-alerts create

POST/organization/projects/{project\_id}/spend\_alerts

##### [Retrieve project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/retrieve)

$ openai admin:organization:projects:spend-alerts retrieve

GET/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Update project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/update)

$ openai admin:organization:projects:spend-alerts update

POST/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### [Delete project spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_alerts/methods/delete)

$ openai admin:organization:projects:spend-alerts delete

DELETE/organization/projects/{project\_id}/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

project\_spend\_alert: object { id, currency, interval, 3 more }

Represents a spend alert configured at the project level.

id: string

The identifier, which can be referenced in API endpoints.

currency: "USD"

The currency for the threshold amount.

"USD"

interval: "month"

The time interval for evaluating spend against the threshold.

"month"

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

project\_spend\_alert\_deleted: object { id, deleted, object }

Confirmation payload returned after deleting a project spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "project.spend\_alert.deleted"

Always `project.spend_alert.deleted`.

#### ProjectsCertificates

##### [List project certificates](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

$ openai admin:organization:projects:certificates list

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

$ openai admin:organization:projects:certificates activate

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

$ openai admin:organization:projects:certificates deactivate

POST/organization/projects/{project\_id}/certificates/deactivate
