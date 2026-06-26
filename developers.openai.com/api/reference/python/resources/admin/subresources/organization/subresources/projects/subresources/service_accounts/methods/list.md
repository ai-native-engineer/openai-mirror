<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/list/ -->

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

# List project service accounts

admin.organization.projects.service\_accounts.list(strproject\_id, ServiceAccountListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectServiceAccount](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema))]

GET/organization/projects/{project\_id}/service\_accounts

Returns a list of service accounts in the project.

##### ParametersExpand Collapse

project\_id: str

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List project service accounts

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
page = client.admin.organization.projects.service_accounts.list(
    project_id="project_id",
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "object": "organization.project.service_account",
            "id": "svc_acct_abc",
            "name": "Service Account",
            "role": "owner",
            "created_at": 1711471533
    ],
    "first_id": "svc_acct_abc",
    "last_id": "svc_acct_xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.project.service_account",
            "id": "svc_acct_abc",
            "name": "Service Account",
            "role": "owner",
            "created_at": 1711471533
    ],
    "first_id": "svc_acct_abc",
    "last_id": "svc_acct_xyz",
    "has_more": false
