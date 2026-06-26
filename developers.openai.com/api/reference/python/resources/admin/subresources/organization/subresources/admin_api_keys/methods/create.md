<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create admin API key

admin.organization.admin\_api\_keys.create(AdminAPIKeyCreateParams\*\*kwargs)  -> [AdminAPIKeyCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_create_response%20%3E%20(schema))

POST/organization/admin\_api\_keys

Create an organization admin API key

##### ParametersExpand Collapse

name: str

expires\_in\_seconds: Optional[int]

The number of seconds until the API key expires. Omit this field for a key that does not expire.

minimum1

maximum31536000

##### ReturnsExpand Collapse

class AdminAPIKeyCreateResponse: …

Represents an individual Admin API key in an org.

value: str

The value of the API key. Only shown on create.

### Create admin API key

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
admin_api_key = client.admin.organization.admin_api_keys.create(
    name="New Admin Key",
print(admin_api_key)

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
