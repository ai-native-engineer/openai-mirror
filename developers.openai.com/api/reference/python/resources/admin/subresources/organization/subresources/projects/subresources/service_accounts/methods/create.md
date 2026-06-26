<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project service account

admin.organization.projects.service\_accounts.create(strproject\_id, ServiceAccountCreateParams\*\*kwargs)  -> [ServiceAccountCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts

Creates a new service account in the project. This also returns an unredacted API key for the service account.

##### ParametersExpand Collapse

project\_id: str

name: str

The name of the service account being created.

##### ReturnsExpand Collapse

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

### Create project service account

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
service_account = client.admin.organization.projects.service_accounts.create(
    project_id="project_id",
    name="name",
print(service_account.id)

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"
