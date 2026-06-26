<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List all organization and project API keys.

GET/organization/admin\_api\_keys

List organization API keys

##### Query ParametersExpand Collapse

after: optional string

Return keys with IDs that come after this ID in the pagination order.

limit: optional number

Maximum number of keys to return.

order: optional "asc" or "desc"

Order results by creation time, ascending or descending.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

data: array of [AdminAPIKey](/api/reference/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: number

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: object { id, created\_at, name, 3 more }

id: optional string

The identifier, which can be referenced in API endpoints

created\_at: optional number

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: optional string

The name of the user

object: optional string

The object type, which is always organization.user

role: optional string

Always `owner`

type: optional string

Always `user`

redacted\_value: string

The redacted value of the API key

last\_used\_at: optional number

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: optional string

The name of the API key

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

### List all organization and project API keys.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/admin_api_keys?after=key_abc&limit=20 \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

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
