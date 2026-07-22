<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# API Keys

##### [Create project service account API key](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create)

admin.organization.projects.service\_accounts.api\_keys.create(strservice\_account\_id, APIKeyCreateParams\*\*kwargs)  -> [APIKeyCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

##### ModelsExpand Collapse

class APIKeyCreateResponse: …

id: str

created\_at: int

formatunixtime

name: str

object: Literal["organization.project.service\_account.api\_key"]

The object type, which is always `organization.project.service_account.api_key`

value: str
