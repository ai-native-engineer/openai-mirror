<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# API Keys

##### [List project API keys](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

admin.organization.projects.api\_keys.list(strproject\_id, APIKeyListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))]

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

admin.organization.projects.api\_keys.retrieve(strapi\_key\_id, APIKeyRetrieveParams\*\*kwargs)  -> [ProjectAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

admin.organization.projects.api\_keys.delete(strapi\_key\_id, APIKeyDeleteParams\*\*kwargs)  -> [APIKeyDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

class ProjectAPIKey: …

Represents an individual API key in a project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: str

The name of the API key

object: Literal["organization.project.api\_key"]

The object type, which is always `organization.project.api_key`

owner: Owner

service\_account: Optional[OwnerServiceAccount]

The service account that owns a project API key.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: str

The name of the service account.

role: str

The service account’s project role.

type: Optional[Literal["user", "service\_account"]]

`user` or `service_account`

One of the following:

"user"

"service\_account"

user: Optional[OwnerUser]

The user that owns a project API key.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: str

The email address of the user.

name: str

The name of the user.

role: str

The user’s project role.

redacted\_value: str

The redacted value of the API key

class APIKeyDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.api\_key.deleted"]
