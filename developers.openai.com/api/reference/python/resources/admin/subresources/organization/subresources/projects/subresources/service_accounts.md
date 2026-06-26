<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/ -->

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

# Service Accounts

##### [List project service accounts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list)

admin.organization.projects.service\_accounts.list(strproject\_id, ServiceAccountListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))]

GET/organization/projects/{project\_id}/service\_accounts

##### [Create project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create)

admin.organization.projects.service\_accounts.create(strproject\_id, ServiceAccountCreateParams\*\*kwargs)  -> [ServiceAccountCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts

##### [Retrieve project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve)

admin.organization.projects.service\_accounts.retrieve(strservice\_account\_id, ServiceAccountRetrieveParams\*\*kwargs)  -> [ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Update project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update)

admin.organization.projects.service\_accounts.update(strservice\_account\_id, ServiceAccountUpdateParams\*\*kwargs)  -> [ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### [Delete project service account](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete)

admin.organization.projects.service\_accounts.delete(strservice\_account\_id, ServiceAccountDeleteParams\*\*kwargs)  -> [ServiceAccountDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse

class ProjectServiceAccount: …

Represents an individual service account in a project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: str

The name of the service account

object: Literal["organization.project.service\_account"]

The object type, which is always `organization.project.service_account`

role: Literal["owner", "member"]

`owner` or `member`

One of the following:

"owner"

"member"

class ServiceAccountCreateResponse: …

id: str

api\_key: Optional[APIKey]

id: str

created\_at: int

formatunixtime

name: str

object: Literal["organization.project.service\_account.api\_key"]

The object type, which is always `organization.project.service_account.api_key`

value: str

created\_at: int

formatunixtime

name: str

object: Literal["organization.project.service\_account"]

role: Literal["member"]

Service accounts can only have one role of type `member`

class ServiceAccountDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.service\_account.deleted"]
