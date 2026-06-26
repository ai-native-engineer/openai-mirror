<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create/ -->

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

# Create admin API key

admin.organization.admin\_api\_keys.create(\*\*kwargs) -> [AdminAPIKeyCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema)) { value }

POST/organization/admin\_api\_keys

Create an organization admin API key

##### ParametersExpand Collapse

name: String

expires\_in\_seconds: Integer

The number of seconds until the API key expires. Omit this field for a key that does not expire.

minimum1

maximum31536000

##### ReturnsExpand Collapse

class AdminAPIKeyCreateResponse { value }

Represents an individual Admin API key in an org.

value: String

The value of the API key. Only shown on create.

### Create admin API key

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

admin_api_key = openai.admin.organization.admin_api_keys.create(name: "New Admin Key")

puts(admin_api_key)

  "object": "organization.admin_api_key",
  "id": "key_xyz",
  "name": "New Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "expires_at": 1714063533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
  "value": "sk-admin-1234abcd"

##### Returns Examples

  "object": "organization.admin_api_key",
  "id": "key_xyz",
  "name": "New Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "expires_at": 1714063533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
  "value": "sk-admin-1234abcd"
