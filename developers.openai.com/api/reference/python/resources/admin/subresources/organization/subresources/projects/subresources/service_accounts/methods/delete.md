<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete/ -->

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

# Delete project service account

admin.organization.projects.service\_accounts.delete(strservice\_account\_id, ServiceAccountDeleteParams\*\*kwargs)  -> [ServiceAccountDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Deletes a service account from the project.

Returns confirmation of service account deletion, or an error if the project
is archived (archived projects have no service accounts).

##### ParametersExpand Collapse

project\_id: str

service\_account\_id: str

##### ReturnsExpand Collapse

class ServiceAccountDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.service\_account.deleted"]

### Delete project service account

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
service_account = client.admin.organization.projects.service_accounts.delete(
    service_account_id="service_account_id",
    project_id="project_id",
print(service_account.id)

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true
