<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project role

admin.organization.projects.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/projects/{project\_id}/roles/{role\_id}

Deletes a custom role from a project.

##### ParametersExpand Collapse

project\_id: str

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

### Delete project role

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
role = client.admin.organization.projects.roles.delete(
    role_id="role_id",
    project_id="project_id",
print(role.id)

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true
