<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### Path ParametersExpand Collapse

project\_id: string

service\_account\_id: string

##### Body ParametersJSONExpand Collapse

name: optional string

API key name.

scopes: optional array of string

API key scopes.

##### ReturnsExpand Collapse

id: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string

### Create project service account API key

HTTP

curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/service_accounts/svc_acct_abc/api_keys \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "name": "Production App",
      "scopes": ["api.responses.write"]
  }'

    "object": "organization.project.service_account.api_key",
    "value": "sk-abcdefghijklmnop123",
    "name": "Production App",
    "created_at": 1711471533,
    "id": "key_abc"

    "object": "organization.project.service_account.api_key",
    "value": "sk-abcdefghijklmnop123",
    "name": "Production App",
    "created_at": 1711471533,
    "id": "key_abc"
