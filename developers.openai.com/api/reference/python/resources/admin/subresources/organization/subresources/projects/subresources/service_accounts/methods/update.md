<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update/ -->

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

# Update project service account

admin.organization.projects.service\_accounts.update(strservice\_account\_id, ServiceAccountUpdateParams\*\*kwargs)  -> [ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Updates a service account in the project.

##### ParametersExpand Collapse

project\_id: str

service\_account\_id: str

name: Optional[str]

The updated service account name.

role: Optional[Literal["member", "owner"]]

The updated service account role.

One of the following:

"member"

"owner"

##### ReturnsExpand Collapse

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

### Update project service account

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
project_service_account = client.admin.organization.projects.service_accounts.update(
    service_account_id="service_account_id",
    project_id="project_id",
print(project_service_account.id)

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Updated service account",
    "role": "member",
    "created_at": 1711471533

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Updated service account",
    "role": "member",
    "created_at": 1711471533
