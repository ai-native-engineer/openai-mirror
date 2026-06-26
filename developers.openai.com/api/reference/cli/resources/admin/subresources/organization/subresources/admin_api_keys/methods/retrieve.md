<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve admin API key

$ openai admin:organization:admin-api-keys retrieve

GET/organization/admin\_api\_keys/{key\_id}

Retrieve a single organization API key

##### ParametersExpand Collapse

--key-id: string

The ID of the API key.

##### ReturnsExpand Collapse

admin\_api\_key: object { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

expires\_at: number

The Unix timestamp (in seconds) of when the API key expires

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: object { id, created\_at, name, 3 more }

id: optional string

The identifier, which can be referenced in API endpoints

created\_at: optional number

The Unix timestamp (in seconds) of when the user was created

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

name: optional string

The name of the API key

### Retrieve admin API key

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:admin-api-keys retrieve \
  --admin-api-key 'My Admin API Key' \
  --key-id key_id

  "object": "organization.admin_api_key",
  "id": "key_abc",
  "name": "Main Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"

##### Returns Examples

  "object": "organization.admin_api_key",
  "id": "key_abc",
  "name": "Main Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
