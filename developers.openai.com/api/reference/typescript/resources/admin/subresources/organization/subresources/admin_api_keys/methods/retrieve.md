<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve admin API key

client.admin.organization.adminAPIKeys.retrieve(stringkeyID, RequestOptionsoptions?): [AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more }

GET/organization/admin\_api\_keys/{key\_id}

Retrieve a single organization API key

##### ParametersExpand Collapse

keyID: string

The ID of the API key.

##### ReturnsExpand Collapse

AdminAPIKey { id, created\_at, expires\_at, 5 more }

Represents an individual Admin API key in an org.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

expires\_at: number | null

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

object: "organization.admin\_api\_key"

The object type, which is always `organization.admin_api_key`

owner: Owner { id, created\_at, name, 3 more }

id?: string

The identifier, which can be referenced in API endpoints

created\_at?: number

The Unix timestamp (in seconds) of when the user was created

formatunixtime

name?: string

The name of the user

object?: string

The object type, which is always organization.user

role?: string

Always `owner`

type?: string

Always `user`

redacted\_value: string

The redacted value of the API key

last\_used\_at?: number | null

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

name?: string | null

The name of the API key

### Retrieve admin API key

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const adminAPIKey = await client.admin.organization.adminAPIKeys.retrieve('key_id');

console.log(adminAPIKey.id);

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
