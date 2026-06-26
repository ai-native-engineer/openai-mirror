<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete/ -->

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

# Delete checkpoint permission

$ openai fine-tuning:checkpoints:permissions delete

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

--fine-tuned-model-checkpoint: string

The ID of the fine-tuned model checkpoint to delete a permission for.

--permission-id: string

The ID of the fine-tuned model checkpoint permission to delete.

##### ReturnsExpand Collapse

FineTuningCheckpointPermissionDeleteResponse: object { id, deleted, object }

id: string

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: boolean

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: "checkpoint.permission"

The object type, which is always “checkpoint.permission”.

### Delete checkpoint permission

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai fine-tuning:checkpoints:permissions delete \
  --api-key 'My API Key' \
  --fine-tuned-model-checkpoint ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd \
  --permission-id cp_zc4Q7MP6XxulcVzj4MZdwsAB

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true

##### Returns Examples

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true
