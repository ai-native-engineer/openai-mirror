<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete admin API key

admin.organization.admin\_api\_keys.delete(strkey\_id)  -> [AdminAPIKeyDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema))

DELETE/organization/admin\_api\_keys/{key\_id}

Delete an organization admin API key

##### ParametersExpand Collapse

key\_id: str

The ID of the API key to be deleted.

##### ReturnsExpand Collapse

class AdminAPIKeyDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.admin\_api\_key.deleted"]

### Delete admin API key

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
admin_api_key = client.admin.organization.admin_api_keys.delete(
    "key_id",
print(admin_api_key.id)

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true

##### Returns Examples

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true
