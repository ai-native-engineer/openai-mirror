<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/update/ -->

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

# Modify user

admin.organization.users.update(struser\_id, UserUpdateParams\*\*kwargs)  -> [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

POST/organization/users/{user\_id}

Modifies a user’s role in the organization.

##### ParametersExpand Collapse

user\_id: str

developer\_persona: Optional[str]

Developer persona metadata.

role: Optional[str]

`owner` or `reader`

role\_id: Optional[str]

Role ID to assign to the user.

technical\_level: Optional[str]

Technical level metadata.

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

### Modify user

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
organization_user = client.admin.organization.users.update(
    user_id="user_id",
print(organization_user.id)

    "object": "organization.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
