<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete group

admin.organization.groups.delete(strgroup\_id)  -> [GroupDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}

Deletes a group from the organization.

##### ParametersExpand Collapse

group\_id: str

##### ReturnsExpand Collapse

class GroupDeleteResponse: …

Confirmation payload returned after deleting a group.

id: str

Identifier of the deleted group.

deleted: bool

Whether the group was deleted.

object: Literal["group.deleted"]

Always `group.deleted`.

### Delete group

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
group = client.admin.organization.groups.delete(
    "group_id",
print(group.id)

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

##### Returns Examples

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true
