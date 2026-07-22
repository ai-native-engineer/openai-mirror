<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

# API Keys

##### [Create project service account API key](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create)

client.admin.organization.projects.serviceAccounts.apiKeys.create(stringserviceAccountID, APIKeyCreateParams { project\_id, name, scopes } params, RequestOptionsoptions?): [APIKeyCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

##### ModelsExpand Collapse

APIKeyCreateResponse { id, created\_at, name, 2 more }

id: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string
