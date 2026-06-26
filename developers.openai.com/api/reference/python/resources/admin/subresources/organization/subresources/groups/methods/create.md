<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/create/ -->

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

# Create group

admin.organization.groups.create(GroupCreateParams\*\*kwargs)  -> [Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))

POST/organization/groups

Creates a new group in the organization.

##### ParametersExpand Collapse

name: str

Human readable name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

class Group: …

Details about an organization group.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: Literal["group", "tenant\_group"]

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: bool

Whether the group is managed through SCIM and controlled by your identity provider.

name: str

Display name of the group.

### Create group

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
group = client.admin.organization.groups.create(
    name="x",
print(group.id)

    "object": "group",
    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "object": "group",
    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false
