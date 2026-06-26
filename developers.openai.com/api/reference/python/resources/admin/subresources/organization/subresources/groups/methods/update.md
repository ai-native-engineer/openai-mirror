<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/update/ -->

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

# Update group

admin.organization.groups.update(strgroup\_id, GroupUpdateParams\*\*kwargs)  -> [GroupUpdateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema))

POST/organization/groups/{group\_id}

Updates a group’s information.

##### ParametersExpand Collapse

group\_id: str

name: str

New display name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

class GroupUpdateResponse: …

Response returned after updating a group.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: str

Updated display name for the group.

### Update group

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
group = client.admin.organization.groups.update(
    group_id="group_id",
    name="x",
print(group.id)

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false
