<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List group users

admin.organization.groups.users.list(strgroup\_id, UserListParams\*\*kwargs)  -> SyncNextCursorPage[[OrganizationGroupUser](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))]

GET/organization/groups/{group\_id}/users

Lists the users assigned to a group.

##### ParametersExpand Collapse

group\_id: str

after: Optional[str]

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

limit: Optional[int]

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

order: Optional[Literal["asc", "desc"]]

Specifies the sort order of users in the list.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

class OrganizationGroupUser: …

Represents an individual user returned when inspecting group membership.

id: str

The identifier, which can be referenced in API endpoints

email: Optional[str]

The email address of the user.

name: str

The name of the user.

### List group users

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
page = client.admin.organization.groups.users.list(
    group_id="group_id",
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null
