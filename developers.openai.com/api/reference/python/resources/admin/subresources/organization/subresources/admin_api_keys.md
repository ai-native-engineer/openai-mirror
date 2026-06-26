<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Admin API Keys

##### [List all organization and project API keys.](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

admin.organization.admin\_api\_keys.list(AdminAPIKeyListParams\*\*kwargs)  -> SyncCursorPage[[AdminAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))]

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

admin.organization.admin\_api\_keys.create(AdminAPIKeyCreateParams\*\*kwargs)  -> [AdminAPIKeyCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema))

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

admin.organization.admin\_api\_keys.retrieve(strkey\_id)  -> [AdminAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

admin.organization.admin\_api\_keys.delete(strkey\_id)  -> [AdminAPIKeyDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema))

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

class AdminAPIKey: …

Represents an individual Admin API key in an org.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: Literal["organization.admin\_api\_key"]

The object type, which is always `organization.admin_api_key`

owner: Owner

id: Optional[str]

The identifier, which can be referenced in API endpoints

created\_at: Optional[int]

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: Optional[str]

The name of the user

object: Optional[str]

The object type, which is always organization.user

role: Optional[str]

Always `owner`

type: Optional[str]

Always `user`

redacted\_value: str

The redacted value of the API key

last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: Optional[str]

The name of the API key

class AdminAPIKeyCreateResponse: …

Represents an individual Admin API key in an org.

value: str

The value of the API key. Only shown on create.

class AdminAPIKeyDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.admin\_api\_key.deleted"]
