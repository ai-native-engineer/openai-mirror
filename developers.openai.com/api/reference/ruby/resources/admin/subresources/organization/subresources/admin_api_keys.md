<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Admin API Keys

##### [List all organization and project API keys.](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

admin.organization.admin\_api\_keys.list(\*\*kwargs) -> CursorPage<[AdminAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more } >

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

admin.organization.admin\_api\_keys.create(\*\*kwargs) -> [AdminAPIKeyCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)) { value }

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

admin.organization.admin\_api\_keys.retrieve(key\_id) -> [AdminAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

admin.organization.admin\_api\_keys.delete(key\_id) -> [AdminAPIKeyDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

class AdminAPIKey { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: :"organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: Owner{ id, created\_at, name, 3 more}

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: String

The name of the user

object: String

The object type, which is always organization.user

role: String

Always `owner`

type: String

Always `user`

redacted\_value: String

The redacted value of the API key

last\_used\_at: Integer

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: String

The name of the API key

class AdminAPIKeyCreateResponse { value }

Represents an individual Admin API key in an org.

value: String

The value of the API key. Only shown on create.

class AdminAPIKeyDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.admin\_api\_key.deleted"
