<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project API keys

admin.organization.projects.api\_keys.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more } >

GET/organization/projects/{project\_id}/api\_keys

Returns a list of API keys in the project.

##### ParametersExpand Collapse

project\_id: String

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

class ProjectAPIKey { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: Integer

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: String

The name of the API key

object: :"organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: Owner{ service\_account, type, user}

service\_account: ServiceAccount{ id, created\_at, name, role}

The service account that owns a project API key.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: String

The name of the service account.

role: String

The service account’s project role.

type: :user | :service\_account

`user` or `service_account`

One of the following:

:user

:service\_account

user: User{ id, created\_at, email, 2 more}

The user that owns a project API key.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: String

The email address of the user.

name: String

The name of the user.

role: String

The user’s project role.

redacted\_value: String

The redacted value of the API key

### List project API keys

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.projects.api_keys.list("project_id")

puts(page)

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
