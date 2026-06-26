<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Users](/api/reference/python/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete user

admin.organization.users.delete(struser\_id)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/users/{user\_id}

Deletes a user from the organization.

##### ParametersExpand Collapse

user\_id: str

##### ReturnsExpand Collapse

class UserDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.user.deleted"]

### Delete user

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
user = client.admin.organization.users.delete(
    "user_id",
print(user.id)

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true
