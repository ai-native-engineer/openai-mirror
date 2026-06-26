<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Admin API Keys

##### [List all organization and project API keys.](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

client.admin.organization.adminAPIKeys.list(AdminAPIKeyListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more } >

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

client.admin.organization.adminAPIKeys.create(AdminAPIKeyCreateParams { name, expires\_in\_seconds } body, RequestOptionsoptions?): [AdminAPIKeyCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)) { value }

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

client.admin.organization.adminAPIKeys.retrieve(stringkeyID, RequestOptionsoptions?): [AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

client.admin.organization.adminAPIKeys.delete(stringkeyID, RequestOptionsoptions?): [AdminAPIKeyDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

AdminAPIKey { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: number | null

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: Owner { id, created\_at, name, 3 more }

id?: string

The identifier, which can be referenced in API endpoints

created\_at?: number

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name?: string

The name of the user

object?: string

The object type, which is always organization.user

role?: string

Always `owner`

type?: string

Always `user`

redacted\_value: string

The redacted value of the API key

last\_used\_at?: number | null

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name?: string | null

The name of the API key

AdminAPIKeyCreateResponse extends [AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }  { value }

Represents an individual Admin API key in an org.

value: string

The value of the API key. Only shown on create.

AdminAPIKeyDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.admin\_api\_key.deleted"
