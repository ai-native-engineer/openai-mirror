<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

client.admin.organization.projects.serviceAccounts.apiKeys.create(stringserviceAccountID, APIKeyCreateParams { project\_id, name, scopes } params, RequestOptionsoptions?): [APIKeyCreateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### ParametersExpand Collapse

serviceAccountID: string

params: APIKeyCreateParams { project\_id, name, scopes }

project\_id: string

Path param: The ID of the project.

name?: string

Body param: API key name.

scopes?: Array<string>

Body param: API key scopes.

##### ReturnsExpand Collapse

APIKeyCreateResponse { id, created\_at, name, 2 more }

id: string

created\_at: number

formatunixtime

name: string

object: "organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: string

### Create project service account API key

TypeScript

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const apiKey = await client.admin.organization.projects.serviceAccounts.apiKeys.create(
  'service_account_id',
  { project_id: 'project_id' },
);

console.log(apiKey.id);

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
