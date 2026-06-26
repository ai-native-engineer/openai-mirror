<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project API key

admin.organization.projects.api\_keys.delete(strapi\_key\_id, APIKeyDeleteParams\*\*kwargs)  -> [APIKeyDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema))

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Deletes an API key from the project.

Returns confirmation of the key deletion, or an error if the key belonged to
a service account.

##### ParametersExpand Collapse

project\_id: str

api\_key\_id: str

##### ReturnsExpand Collapse

class APIKeyDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.project.api\_key.deleted"]

### Delete project API key

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
api_key = client.admin.organization.projects.api_keys.delete(
    api_key_id="api_key_id",
    project_id="project_id",
print(api_key.id)

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true
