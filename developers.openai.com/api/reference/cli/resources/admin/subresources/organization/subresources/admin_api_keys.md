<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/ -->

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

# Admin API Keys

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
