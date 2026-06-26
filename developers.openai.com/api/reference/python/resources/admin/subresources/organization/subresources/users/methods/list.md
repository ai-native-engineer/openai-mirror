<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/list/ -->

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

# List users

admin.organization.users.list(UserListParams\*\*kwargs)  -> SyncConversationCursorPage[[OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))]

GET/organization/users

Lists all of the users in the organization.

##### ParametersExpand Collapse

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

emails: Optional[Sequence[str]]

Filter by the email address of users.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

class OrganizationUser: …

Represents an individual `user` within an organization.

id: str

The identifier, which can be referenced in API endpoints

added\_at: int

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: Literal["organization.user"]

The object type, which is always `organization.user`

api\_key\_last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: Optional[int]

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: Optional[str]

The developer persona metadata for the user.

email: Optional[str]

The email address of the user

is\_default: Optional[bool]

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: Optional[bool]

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: Optional[bool]

Whether the user is managed through SCIM.

is\_service\_account: Optional[bool]

Whether the user is a service account.

name: Optional[str]

The name of the user

projects: Optional[Projects]

Projects associated with the user, if included.

data: List[ProjectsData]

id: Optional[str]

name: Optional[str]

role: Optional[str]

object: Literal["list"]

role: Optional[str]

`owner` or `reader`

technical\_level: Optional[str]

The technical level metadata for the user.

user: Optional[User]

Nested user details.

id: str

object: Literal["user"]

banned: Optional[bool]

banned\_at: Optional[int]

formatunixtime

email: Optional[str]

enabled: Optional[bool]

name: Optional[str]

picture: Optional[str]

### List users

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
page = client.admin.organization.users.list()
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false
