<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project API key

client.admin.organization.projects.apiKeys.delete(stringapiKeyID, APIKeyDeleteParams { project\_id } params, RequestOptionsoptions?): [APIKeyDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Deletes an API key from the project.

Returns confirmation of the key deletion, or an error if the key belonged to
a service account.

##### ParametersExpand Collapse

apiKeyID: string

params: APIKeyDeleteParams { project\_id }

project\_id: string

The ID of the project.

##### ReturnsExpand Collapse

APIKeyDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.api\_key.deleted"

### Delete project API key

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

const apiKey = await client.admin.organization.projects.apiKeys.delete('api_key_id', {
  project_id: 'project_id',

console.log(apiKey.id);

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true
