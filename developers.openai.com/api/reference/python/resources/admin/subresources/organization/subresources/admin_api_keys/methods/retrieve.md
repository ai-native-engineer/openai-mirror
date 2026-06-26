<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve/ -->

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

# Retrieve admin API key

admin.organization.admin\_api\_keys.retrieve(strkey\_id)  -> [AdminAPIKey](/api/reference/python/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))

GET/organization/admin\_api\_keys/{key\_id}

Retrieve a single organization API key

##### ParametersExpand Collapse

key\_id: str

The ID of the API key.

##### ReturnsExpand Collapse

class AdminAPIKey: …

Represents an individual Admin API key in an org.

id: str

The identifier, which can be referenced in API endpoints

created\_at: int

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: Literal["organization.admin\_api\_key"]

The object type, which is always `organization.admin_api_key`

owner: Owner

id: Optional[str]

The identifier, which can be referenced in API endpoints

created\_at: Optional[int]

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name: Optional[str]

The name of the user

object: Optional[str]

The object type, which is always organization.user

role: Optional[str]

Always `owner`

type: Optional[str]

Always `user`

redacted\_value: str

The redacted value of the API key

last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name: Optional[str]

The name of the API key

### Retrieve admin API key

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
admin_api_key = client.admin.organization.admin_api_keys.retrieve(
    "key_id",
print(admin_api_key.id)

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
