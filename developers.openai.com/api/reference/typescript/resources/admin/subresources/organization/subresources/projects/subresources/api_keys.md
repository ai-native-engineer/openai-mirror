<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# API Keys

##### [List project API keys](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

client.admin.organization.projects.apiKeys.list(stringprojectID, APIKeyListParams { after, limit } query?, RequestOptionsoptions?): ConversationCursorPage<[ProjectAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more } >

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

client.admin.organization.projects.apiKeys.retrieve(stringapiKeyID, APIKeyRetrieveParams { project\_id } params, RequestOptionsoptions?): [ProjectAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more }

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

client.admin.organization.projects.apiKeys.delete(stringapiKeyID, APIKeyDeleteParams { project\_id } params, RequestOptionsoptions?): [APIKeyDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

ProjectAPIKey { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: number | null

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: string

The name of the API key

object: "organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: Owner { service\_account, type, user }

service\_account?: ServiceAccount { id, created\_at, name, role }

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

type?: "user" | "service\_account"

`user` or `service_account`

One of the following:

"user"

"service\_account"

user?: User { id, created\_at, email, 2 more }

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

APIKeyDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.api\_key.deleted"
