<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Fine Tuning](/api/reference/cli/resources/fine_tuning)

[Checkpoints](/api/reference/cli/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create checkpoint permissions

$ openai fine-tuning:checkpoints:permissions create

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### ParametersExpand Collapse

--fine-tuned-model-checkpoint: string

The ID of the fine-tuned model checkpoint to create a permission for.

--project-id: array of string

The project identifiers to grant access to.

##### ReturnsExpand Collapse

ListFineTuningCheckpointPermissionResponse: object { data, has\_more, object, 2 more }

data: array of object { id, created\_at, object, project\_id }

id: string

The permission identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the permission was created.

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: string

The project identifier that the permission is for.

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

### Create checkpoint permissions

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai fine-tuning:checkpoints:permissions create \
  --api-key 'My API Key' \
  --fine-tuned-model-checkpoint ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd \
  --project-id string

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
