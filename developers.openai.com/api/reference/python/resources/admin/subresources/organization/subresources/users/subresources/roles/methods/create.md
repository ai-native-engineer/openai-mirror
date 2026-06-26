<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Users](/api/reference/python/resources/admin/subresources/organization/subresources/users)

[Roles](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign organization role to user

admin.organization.users.roles.create(struser\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/organization/users/{user\_id}/roles

Assigns an organization role to a user within the organization.

##### ParametersExpand Collapse

user\_id: str

role\_id: str

Identifier of the role to assign.

##### ReturnsExpand Collapse

class RoleCreateResponse: …

Role assignment linking a user to a role.

object: Literal["user.role"]

Always `user.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

id: str

Identifier for the role.

description: Optional[str]

Optional description of the role.

name: str

Unique name for the role.

object: Literal["role"]

Always `role`.

permissions: List[str]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: str

Resource type the role is bound to (for example `api.organization` or `api.project`).

user: [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

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

### Assign organization role to user

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
role = client.admin.organization.users.roles.create(
    user_id="user_id",
    role_id="role_id",
print(role.object)

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8ROLE01",
        "name": "API Group Manager",
        "description": "Allows managing organization groups",
        "permissions": [
            "api.groups.read",
            "api.groups.write"
        ],
        "resource_type": "api.organization",
        "predefined_role": false

##### Returns Examples

    "object": "user.role",
    "user": {
        "object": "organization.user",
        "id": "user_abc123",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "role": "owner",
        "added_at": 1711470000
    "role": {
        "object": "role",
        "id": "role_01J1F8ROLE01",
        "name": "API Group Manager",
        "description": "Allows managing organization groups",
        "permissions": [
            "api.groups.read",
            "api.groups.write"
        ],
        "resource_type": "api.organization",
        "predefined_role": false
