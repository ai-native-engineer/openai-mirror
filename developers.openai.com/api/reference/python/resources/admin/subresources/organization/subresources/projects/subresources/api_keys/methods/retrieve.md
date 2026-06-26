<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve/ -->

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

# Retrieve project API key

admin.organization.projects.api\_keys.retrieve(strapi\_key\_id, APIKeyRetrieveParams\*\*kwargs)  -> [ProjectAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Retrieves an API key in the project.

##### ParametersExpand Collapse

project\_id: str

api\_key\_id: str

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

### Retrieve project API key

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
project_api_key = client.admin.organization.projects.api_keys.retrieve(
    api_key_id="api_key_id",
    project_id="project_id",
print(project_api_key.id)

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

##### Returns Examples

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
