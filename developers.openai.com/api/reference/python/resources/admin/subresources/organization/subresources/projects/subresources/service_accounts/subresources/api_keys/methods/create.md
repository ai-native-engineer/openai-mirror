<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

admin.organization.projects.service\_accounts.api\_keys.create(strservice\_account\_id, APIKeyCreateParams\*\*kwargs)  -> [APIKeyCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20api_key_create_response%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### ParametersExpand Collapse

project\_id: str

service\_account\_id: str

name: Optional[str]

API key name.

scopes: Optional[Sequence[str]]

API key scopes.

##### ReturnsExpand Collapse

class APIKeyCreateResponse: …

id: str

created\_at: int

formatunixtime

name: str

object: Literal["organization.project.service\_account.api\_key"]

The object type, which is always `organization.project.service_account.api_key`

value: str

### Create project service account API key

Python

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
)
api_key = client.admin.organization.projects.service_accounts.api_keys.create(
    service_account_id="service_account_id",
    project_id="project_id",
)
print(api_key.id)

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
