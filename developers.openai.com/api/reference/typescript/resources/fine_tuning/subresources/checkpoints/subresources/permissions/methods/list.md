<!-- source: https://developers.openai.com/api/reference/typescript/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list/ -->

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

# List checkpoint permissions

client.fineTuning.checkpoints.permissions.list(stringfineTunedModelCheckpoint, PermissionListParams { after, limit, order, project\_id } query?, RequestOptionsoptions?): ConversationCursorPage<[PermissionListResponse](/api/reference/typescript/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema)) { id, created\_at, object, project\_id } >

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fineTunedModelCheckpoint: string

query: PermissionListParams { after, limit, order, project\_id }

after?: string

Identifier for the last permission ID from the previous pagination request.

limit?: number

Number of permissions to retrieve.

order?: "ascending" | "descending"

The order in which to retrieve permissions.

One of the following:

"ascending"

"descending"

project\_id?: string

The ID of the project to get permissions for.

##### ReturnsExpand Collapse

PermissionListResponse { id, created\_at, object, project\_id }

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

### List checkpoint permissions

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
for await (const permissionListResponse of client.fineTuning.checkpoints.permissions.list(
  'ft-AF1WoRqd3aJAHsqc9NY7iL8F',
)) {
  console.log(permissionListResponse.id);

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
      "object": "checkpoint.permission",
      "id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "project_id": "proj_iqGMw1llN8IrBb6SvvY5A1oF"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "checkpoint.permission",
      "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1721764867,
      "project_id": "proj_abGMw1llN8IrBb6SvvY5A1iH"
      "object": "checkpoint.permission",
      "id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1721764800,
      "project_id": "proj_iqGMw1llN8IrBb6SvvY5A1oF"
  ],
  "first_id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "cp_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": false
