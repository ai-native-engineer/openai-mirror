<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# API Keys

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
