<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve/ -->

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

# Retrieve group user

admin.organization.groups.users.retrieve(struser\_id, UserRetrieveParams\*\*kwargs)  -> [UserRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20user_retrieve_response%20%3E%20(schema))

GET/organization/groups/{group\_id}/users/{user\_id}

Retrieves a user in a group.

##### ParametersExpand Collapse

group\_id: str

user\_id: str

##### ReturnsExpand Collapse

class UserRetrieveResponse: …

Details about a user returned from an organization group membership lookup.

id: str

Identifier for the user.

email: Optional[str]

Email address of the user, or `null` for users without an email.

is\_service\_account: Optional[bool]

Whether the user is a service account.

name: str

Display name of the user.

picture: Optional[str]

URL of the user’s profile picture, if available.

user\_type: Literal["user", "tenant\_user"]

The type of user.

One of the following:

"user"

"tenant\_user"

### Retrieve group user

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
user = client.admin.organization.groups.users.retrieve(
    user_id="user_id",
    group_id="group_id",
print(user.id)

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

##### Returns Examples

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"
