<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

admin.organization.roles.delete(strrole\_id)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### ParametersExpand Collapse

role\_id: str

##### ReturnsExpand Collapse

class RoleDeleteResponse: …

Confirmation payload returned after deleting a role.

id: str

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: Literal["role.deleted"]

Always `role.deleted`.

### Delete organization role

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
role = client.admin.organization.roles.delete(
    "role_id",
print(role.id)

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true
