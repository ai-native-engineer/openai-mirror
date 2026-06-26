<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create/ -->

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

# Create admin API key

$ openai admin:organization:admin-api-keys create

POST/organization/admin\_api\_keys

Create an organization admin API key

##### ParametersExpand Collapse

--name: string

--expires-in-seconds: optional number

The number of seconds until the API key expires. Omit this field for a key that does not expire.

##### ReturnsExpand Collapse

AdminOrganizationAdminAPIKeyNewResponse: [AdminAPIKey](/api/reference/cli/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

value: string

The value of the API key. Only shown on create.

### Create admin API key

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:admin-api-keys create \
  --admin-api-key 'My Admin API Key' \
  --name 'New Admin Key'

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
