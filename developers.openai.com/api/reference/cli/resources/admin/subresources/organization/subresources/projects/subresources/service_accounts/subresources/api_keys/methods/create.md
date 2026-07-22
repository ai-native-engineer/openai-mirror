<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

$ openai admin:organization:projects:service-accounts:api-keys create

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--service-account-id: string

The ID of the service account.

--name: optional string

API key name.

--scope: optional array of string

API key scopes.

##### ReturnsExpand Collapse

AdminOrganizationProjectServiceAccountAPIKeyNewResponse: object { id, created\_at, name, 2 more }

id: string

created\_at: number

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string

### Create project service account API key

CLI Tool

openai admin:organization:projects:service-accounts:api-keys create \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --service-account-id service_account_id

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
