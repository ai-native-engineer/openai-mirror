<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign organization role from group

admin.organization.groups.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/roles/{role\_id}

Unassigns an organization role from a group within the organization.

##### ParametersExpand Collapse

group\_id: str

role\_id: str

##### ReturnsExpand Collapse

class RoleDeleteResponse: …

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: str

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign organization role from group

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
role = client.admin.organization.groups.roles.delete(
    role_id="role_id",
    group_id="group_id",
print(role.deleted)

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true
