<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project API keys

admin.organization.projects.api\_keys.list(strproject\_id, APIKeyListParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))]

GET/organization/projects/{project\_id}/api\_keys

Returns a list of API keys in the project.

##### ParametersExpand Collapse

project\_id: str

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

class ProjectAPIKey: …

Represents an individual API key in a project.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: str

The name of the API key

object: Literal["organization.project.api\_key"]

The object type, which is always `organization.project.api_key`

owner: Owner

service\_account: Optional[OwnerServiceAccount]

The service account that owns a project API key.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: str

The name of the service account.

role: str

The service account’s project role.

type: Optional[Literal["user", "service\_account"]]

`user` or `service_account`

One of the following:

"user"

"service\_account"

user: Optional[OwnerUser]

The user that owns a project API key.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: str

The email address of the user.

name: str

The name of the user.

role: str

The user’s project role.

redacted\_value: str

The redacted value of the API key

### List project API keys

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
page = client.admin.organization.projects.api_keys.list(
    project_id="project_id",
page = page.data[0]
print(page.id)

    "object": "list",
    "data": [
            "object": "organization.project.api_key",
            "redacted_value": "sk-abc...def",
            "name": "My API Key",
            "created_at": 1711471533,
            "last_used_at": 1711471534,
            "id": "key_abc",
            "owner": {
                "type": "user",
                "user": {
                    "id": "user_abc",
                    "name": "First Last",
                    "email": "user@example.com",
                    "role": "owner",
                    "created_at": 1711471533
    ],
    "first_id": "key_abc",
    "last_id": "key_xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.project.api_key",
            "redacted_value": "sk-abc...def",
            "name": "My API Key",
            "created_at": 1711471533,
            "last_used_at": 1711471534,
            "id": "key_abc",
            "owner": {
                "type": "user",
                "user": {
                    "id": "user_abc",
                    "name": "First Last",
                    "email": "user@example.com",
                    "role": "owner",
                    "created_at": 1711471533
    ],
    "first_id": "key_abc",
    "last_id": "key_xyz",
    "has_more": false
