<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

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

##### [List audit logs](/api/reference/cli/resources/admin/subresources/organization/subresources/audit_logs/methods/list)

$ openai admin:organization:audit-logs list

GET/organization/audit\_logs

#### OrganizationAdmin API Keys

##### [List all organization and project API keys.](/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

$ openai admin:organization:admin-api-keys list

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

$ openai admin:organization:admin-api-keys create

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

$ openai admin:organization:admin-api-keys retrieve

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

$ openai admin:organization:admin-api-keys delete

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

admin\_api\_key: object { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

expires\_at: number

The Unix timestamp (in seconds) of when the API key expires

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: object { id, created\_at, name, 3 more }

id: optional string

The identifier, which can be referenced in API endpoints

created\_at: optional number

The Unix timestamp (in seconds) of when the user was created

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

name: optional string

The name of the API key

#### OrganizationUsage

##### [Audio speeches](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

$ openai admin:organization:usage audio-speeches

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

$ openai admin:organization:usage audio-transcriptions

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

$ openai admin:organization:usage code-interpreter-sessions

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/completions)

$ openai admin:organization:usage completions

GET/organization/usage/completions

##### [Embeddings](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

$ openai admin:organization:usage embeddings

GET/organization/usage/embeddings

##### [Images](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/images)

$ openai admin:organization:usage images

GET/organization/usage/images

##### [Moderations](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/moderations)

$ openai admin:organization:usage moderations

GET/organization/usage/moderations

##### [Vector stores](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

$ openai admin:organization:usage vector-stores

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

$ openai admin:organization:usage file-search-calls

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

$ openai admin:organization:usage web-search-calls

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/costs)

$ openai admin:organization:usage costs

GET/organization/costs

#### OrganizationInvites

##### [List invites](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/list)

$ openai admin:organization:invites list

GET/organization/invites

##### [Create invite](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/create)

$ openai admin:organization:invites create

POST/organization/invites

##### [Retrieve invite](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/retrieve)

$ openai admin:organization:invites retrieve

GET/organization/invites/{invite\_id}

##### [Delete invite](/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/delete)

$ openai admin:organization:invites delete

DELETE/organization/invites/{invite\_id}

##### ModelsExpand Collapse

invite: object { id, created\_at, email, 6 more }

Represents an individual `invite` to the organization.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the invite was sent.

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

"member"

"owner"

role: "owner" or "reader"

`owner` or `reader`

"owner"

"reader"

status: "accepted" or "expired" or "pending"

`accepted`,`expired`, or `pending`

"accepted"

"expired"

"pending"

accepted\_at: optional number

The Unix timestamp (in seconds) of when the invite was accepted.

expires\_at: optional number

The Unix timestamp (in seconds) of when the invite expires.

#### OrganizationUsers

##### [List users](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/list)

$ openai admin:organization:users list

GET/organization/users

##### [Retrieve user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/retrieve)

$ openai admin:organization:users retrieve

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/update)

$ openai admin:organization:users update

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/delete)

$ openai admin:organization:users delete

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

organization\_user: object { id, added\_at, object, 13 more }

Represents an individual `user` within an organization.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the user was added.

object: "organization.user"

The object type, which is always `organization.user`

api\_key\_last\_used\_at: optional number

The Unix timestamp (in seconds) of the user’s last API key usage.

created: optional number

The Unix timestamp (in seconds) of when the user was created.

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

email: optional string

enabled: optional boolean

name: optional string

picture: optional string

#### OrganizationUsersRoles

##### [List user organization role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

$ openai admin:organization:users:roles list

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

$ openai admin:organization:users:roles create

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

$ openai admin:organization:users:roles retrieve

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

$ openai admin:organization:users:roles delete

DELETE/organization/users/{user\_id}/roles/{role\_id}

#### OrganizationGroups

##### [List groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/list)

$ openai admin:organization:groups list

GET/organization/groups

##### [Create group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/create)

$ openai admin:organization:groups create

POST/organization/groups

##### [Retrieve group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

$ openai admin:organization:groups retrieve

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/update)

$ openai admin:organization:groups update

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/delete)

$ openai admin:organization:groups delete

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

group: object { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

group\_type: "group" or "tenant\_group"

The type of the group.

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

#### OrganizationGroupsUsers

##### [List group users](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

$ openai admin:organization:groups:users list

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

$ openai admin:organization:groups:users create

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

$ openai admin:organization:groups:users retrieve

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

$ openai admin:organization:groups:users delete

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

organization\_group\_user: object { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string

The email address of the user.

name: string

The name of the user.

#### OrganizationGroupsRoles

##### [List group organization role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

$ openai admin:organization:groups:roles list

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

$ openai admin:organization:groups:roles create

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

$ openai admin:organization:groups:roles retrieve

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

$ openai admin:organization:groups:roles delete

DELETE/organization/groups/{group\_id}/roles/{role\_id}

#### OrganizationRoles

##### [List organization roles](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/list)

$ openai admin:organization:roles list

GET/organization/roles

##### [Create organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/create)

$ openai admin:organization:roles create

POST/organization/roles

##### [Retrieve organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

$ openai admin:organization:roles retrieve

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/update)

$ openai admin:organization:roles update

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/delete)

$ openai admin:organization:roles delete

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

role: object { id, description, name, 4 more }

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

#### OrganizationData Retention

##### [Retrieve organization data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

$ openai admin:organization:data-retention retrieve

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/data_retention/methods/update)

$ openai admin:organization:data-retention update

POST/organization/data\_retention

##### ModelsExpand Collapse

organization\_data\_retention: object { object, type }

Represents the organization’s data retention control setting.

object: "organization.data\_retention"

The object type, which is always `organization.data_retention`.

type: "zero\_data\_retention" or "modified\_abuse\_monitoring" or "enhanced\_zero\_data\_retention" or "enhanced\_modified\_abuse\_monitoring"

The configured organization data retention type.

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

#### OrganizationSpend Alerts

##### [List organization spend alerts](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/list)

$ openai admin:organization:spend-alerts list

GET/organization/spend\_alerts

##### [Create organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/create)

$ openai admin:organization:spend-alerts create

POST/organization/spend\_alerts

##### [Retrieve organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/retrieve)

$ openai admin:organization:spend-alerts retrieve

GET/organization/spend\_alerts/{alert\_id}

##### [Update organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/update)

$ openai admin:organization:spend-alerts update

POST/organization/spend\_alerts/{alert\_id}

##### [Delete organization spend alert](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_alerts/methods/delete)

$ openai admin:organization:spend-alerts delete

DELETE/organization/spend\_alerts/{alert\_id}

##### ModelsExpand Collapse

organization\_spend\_alert: object { id, currency, interval, 3 more }

Represents a spend alert configured at the organization level.

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

object: "organization.spend\_alert"

The object type, which is always `organization.spend_alert`.

threshold\_amount: number

The alert threshold amount, in cents.

organization\_spend\_alert\_deleted: object { id, deleted, object }

Confirmation payload returned after deleting an organization spend alert.

id: string

The deleted spend alert ID.

deleted: boolean

Whether the spend alert was deleted.

object: "organization.spend\_alert.deleted"

Always `organization.spend_alert.deleted`.

#### OrganizationCertificates

##### [List organization certificates](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/list)

$ openai admin:organization:certificates list

GET/organization/certificates

##### [Upload certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/create)

$ openai admin:organization:certificates create

POST/organization/certificates

##### [Get certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

$ openai admin:organization:certificates retrieve

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/update)

$ openai admin:organization:certificates update

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/delete)

$ openai admin:organization:certificates delete

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/activate)

$ openai admin:organization:certificates activate

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

$ openai admin:organization:certificates deactivate

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

certificate: object { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: string

The identifier, which can be referenced in API endpoints

certificate\_details: object { content, expires\_at, valid\_at }

content: optional string

The content of the certificate in PEM format.

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

name: string

The name of the certificate.

object: "certificate" or "organization.certificate" or "organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

"certificate"

"organization.certificate"

"organization.project.certificate"

active: optional boolean

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

#### OrganizationProjects

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

#### OrganizationProjectsUsers

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

#### OrganizationProjectsUsersRoles

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

#### OrganizationProjectsService Accounts

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

#### OrganizationProjectsAPI Keys

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

#### OrganizationProjectsRate Limits

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

#### OrganizationProjectsModel Permissions

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

#### OrganizationProjectsHosted Tool Permissions

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

#### OrganizationProjectsGroups

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

#### OrganizationProjectsGroupsRoles

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

#### OrganizationProjectsRoles

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

#### OrganizationProjectsData Retention

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

#### OrganizationProjectsSpend Alerts

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

#### OrganizationProjectsCertificates

##### [List project certificates](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

$ openai admin:organization:projects:certificates list

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

$ openai admin:organization:projects:certificates activate

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

$ openai admin:organization:projects:certificates deactivate

POST/organization/projects/{project\_id}/certificates/deactivate
