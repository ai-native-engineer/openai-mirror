<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# API Keys

##### [Create project service account API key](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create)

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

##### ModelsExpand Collapse

APIKeyCreateResponse object { id, created\_at, name, 2 more }

id: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string
