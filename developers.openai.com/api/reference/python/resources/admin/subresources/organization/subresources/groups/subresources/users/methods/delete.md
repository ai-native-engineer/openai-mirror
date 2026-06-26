<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete/ -->

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

# Remove group user

admin.organization.groups.users.delete(struser\_id, UserDeleteParams\*\*kwargs)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/users/{user\_id}

Removes a user from a group.

##### ParametersExpand Collapse

group\_id: str

user\_id: str

##### ReturnsExpand Collapse

class UserDeleteResponse: …

Confirmation payload returned after removing a user from a group.

deleted: bool

Whether the group membership was removed.

object: Literal["group.user.deleted"]

Always `group.user.deleted`.

### Remove group user

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
user = client.admin.organization.groups.users.delete(
    user_id="user_id",
    group_id="group_id",
print(user.deleted)

    "object": "group.user.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.user.deleted",
    "deleted": true
