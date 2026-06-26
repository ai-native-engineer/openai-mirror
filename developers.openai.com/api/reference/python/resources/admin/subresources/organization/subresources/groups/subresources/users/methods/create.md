<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

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

# Add group user

admin.organization.groups.users.create(strgroup\_id, UserCreateParams\*\*kwargs)  -> [UserCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_create_response%20%3E%20(schema))

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### ParametersExpand Collapse

group\_id: str

user\_id: str

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

class UserCreateResponse: …

Confirmation payload returned after adding a user to a group.

group\_id: str

Identifier of the group the user was added to.

object: Literal["group.user"]

Always `group.user`.

user\_id: str

Identifier of the user that was added.

### Add group user

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
user = client.admin.organization.groups.users.create(
    group_id="group_id",
    user_id="user_id",
print(user.group_id)

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
