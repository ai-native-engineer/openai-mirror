<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/methods/list/ -->

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

# List groups

admin.organization.groups.list(GroupListParams\*\*kwargs)  -> SyncNextCursorPage[[Group](/api/reference/python/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))]

GET/organization/groups

Lists all groups in the organization.

##### ParametersExpand Collapse

after: Optional[str]

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group\_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

limit: Optional[int]

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

order: Optional[Literal["asc", "desc"]]

Specifies the sort order of the returned groups.

One of the following:

"asc"

"desc"

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

### List groups

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
page = client.admin.organization.groups.list()
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null
