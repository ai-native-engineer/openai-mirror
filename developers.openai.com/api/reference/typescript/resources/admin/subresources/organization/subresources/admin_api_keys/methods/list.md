<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list/ -->

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

# List all organization and project API keys.

client.admin.organization.adminAPIKeys.list(AdminAPIKeyListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[AdminAPIKey](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) { id, created\_at, expires\_at, 5 more } >

GET/organization/admin\_api\_keys

List organization API keys

##### ParametersExpand Collapse

query: AdminAPIKeyListParams { after, limit, order }

after?: string | null

Return keys with IDs that come after this ID in the pagination order.

limit?: number

Maximum number of keys to return.

order?: "asc" | "desc"

Order results by creation time, ascending or descending.

One of the following:

"asc"

"desc"

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

### List all organization and project API keys.

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

// Automatically fetches more pages as needed.
for await (const adminAPIKey of client.admin.organization.adminAPIKeys.list()) {
  console.log(adminAPIKey.id);

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
