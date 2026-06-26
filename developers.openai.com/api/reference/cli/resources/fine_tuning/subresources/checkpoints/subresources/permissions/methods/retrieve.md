<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve/ -->

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

# List checkpoint permissions

Deprecated: Retrieve is deprecated. Please swap to the paginated list method instead.

$ openai fine-tuning:checkpoints:permissions retrieve

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

--fine-tuned-model-checkpoint: string

The ID of the fine-tuned model checkpoint to get permissions for.

--after: optional string

Identifier for the last permission ID from the previous pagination request.

--limit: optional number

Number of permissions to retrieve.

--order: optional "ascending" or "descending"

The order in which to retrieve permissions.

--project-id: optional string

The ID of the project to get permissions for.

##### ReturnsExpand Collapse

FineTuningCheckpointPermissionGetResponse: object { data, has\_more, object, 2 more }

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

### List checkpoint permissions

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai fine-tuning:checkpoints:permissions retrieve \
  --api-key 'My API Key' \
  --fine-tuned-model-checkpoint ft-AF1WoRqd3aJAHsqc9NY7iL8F

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
