<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

admin.organization.projects.service\_accounts.api\_keys.create(service\_account\_id, \*\*kwargs) -> [APIKeyCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### ParametersExpand Collapse

project\_id: String

service\_account\_id: String

name: String

API key name.

scopes: Array[String]

API key scopes.

##### ReturnsExpand Collapse

class APIKeyCreateResponse { id, created\_at, name, 2 more }

id: String

created\_at: Integer

formatunixtime

name: String

object: :"organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: String

### Create project service account API key

Ruby

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

api_key = openai.admin.organization.projects.service_accounts.api_keys.create(
  "service_account_id",
  project_id: "project_id"
)

puts(api_key)

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
