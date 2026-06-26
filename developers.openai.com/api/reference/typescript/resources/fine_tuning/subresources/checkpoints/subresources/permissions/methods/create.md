<!-- source: https://developers.openai.com/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Fine Tuning](/api/reference/typescript/resources/fine_tuning)

[Checkpoints](/api/reference/typescript/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create checkpoint permissions

client.fineTuning.checkpoints.permissions.create(stringfineTunedModelCheckpoint, PermissionCreateParams { project\_ids } body, RequestOptionsoptions?): Page<[PermissionCreateResponse](/api/reference/typescript/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### ParametersExpand Collapse

fineTunedModelCheckpoint: string

body: PermissionCreateParams { project\_ids }

project\_ids: Array<string>

The project identifiers to grant access to.

##### ReturnsExpand Collapse

PermissionCreateResponse { id, created\_at, object, project\_id }

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: string

The permission identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: string

The project identifier that the permission is for.

### Create checkpoint permissions

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
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

// Automatically fetches more pages as needed.
for await (const permissionCreateResponse of client.fineTuning.checkpoints.permissions.create(
  'ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd',
  { project_ids: ['string'] },
)) {
  console.log(permissionCreateResponse.id);

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "has_more": false
