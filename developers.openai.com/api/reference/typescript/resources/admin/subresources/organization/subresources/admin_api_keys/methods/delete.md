<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete/ -->

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

# Delete admin API key

client.admin.organization.adminAPIKeys.delete(stringkeyID, RequestOptionsoptions?): [AdminAPIKeyDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/admin\_api\_keys/{key\_id}

Delete an organization admin API key

##### ParametersExpand Collapse

keyID: string

The ID of the API key to be deleted.

##### ReturnsExpand Collapse

AdminAPIKeyDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.admin\_api\_key.deleted"

### Delete admin API key

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

const adminAPIKey = await client.admin.organization.adminAPIKeys.delete('key_id');

console.log(adminAPIKey.id);

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true

##### Returns Examples

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true
