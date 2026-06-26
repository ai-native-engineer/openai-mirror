<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project API key

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Retrieves an API key in the project.

##### Path ParametersExpand Collapse

project\_id: string

api\_key\_id: string

##### ReturnsExpand Collapse

ProjectAPIKey object { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: number

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: string

The name of the API key

object: "organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: object { service\_account, type, user }

service\_account: optional object { id, created\_at, name, role }

The service account that owns a project API key.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: string

The name of the service account.

role: string

The service account’s project role.

type: optional "user" or "service\_account"

`user` or `service_account`

One of the following:

"user"

"service\_account"

user: optional object { id, created\_at, email, 2 more }

The user that owns a project API key.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: string

The email address of the user.

name: string

The name of the user.

role: string

The user’s project role.

redacted\_value: string

The redacted value of the API key

### Retrieve project API key

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/projects/proj_abc/api_keys/key_abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

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
