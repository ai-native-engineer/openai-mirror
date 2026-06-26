<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List all organization and project API keys.

admin.organization.admin\_api\_keys.list(\*\*kwargs) -> CursorPage<[AdminAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more } >

GET/organization/admin\_api\_keys

List organization API keys

##### ParametersExpand Collapse

after: String

Return keys with IDs that come after this ID in the pagination order.

limit: Integer

Maximum number of keys to return.

order: :asc | :desc

Order results by creation time, ascending or descending.

One of the following:

:asc

:desc

##### ReturnsExpand Collapse

class AdminAPIKey { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: :"organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: Owner{ id, created\_at, name, 3 more}

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: String

The name of the user

object: String

The object type, which is always organization.user

role: String

Always `owner`

type: String

Always `user`

redacted\_value: String

The redacted value of the API key

last\_used\_at: Integer

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: String

The name of the API key

### List all organization and project API keys.

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

page = openai.admin.organization.admin_api_keys.list

puts(page)

  "object": "list",
  "data": [
      "object": "organization.admin_api_key",
      "id": "key_abc",
      "name": "Main Admin Key",
      "redacted_value": "sk-admin...def",
      "created_at": 1711471533,
      "expires_at": 1714063533,
      "last_used_at": 1711471534,
      "owner": {
        "type": "service_account",
        "object": "organization.service_account",
        "id": "sa_456",
        "name": "My Service Account",
        "created_at": 1711471533,
        "role": "member"
  ],
  "first_id": "key_abc",
  "last_id": "key_abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.admin_api_key",
      "id": "key_abc",
      "name": "Main Admin Key",
      "redacted_value": "sk-admin...def",
      "created_at": 1711471533,
      "expires_at": 1714063533,
      "last_used_at": 1711471534,
      "owner": {
        "type": "service_account",
        "object": "organization.service_account",
        "id": "sa_456",
        "name": "My Service Account",
        "created_at": 1711471533,
        "role": "member"
  ],
  "first_id": "key_abc",
  "last_id": "key_abc",
  "has_more": false
