<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Fine Tuning](/api/reference/ruby/resources/fine_tuning)

[Checkpoints](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete checkpoint permission

fine\_tuning.checkpoints.permissions.delete(permission\_id, \*\*kwargs) -> [PermissionDeleteResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fine\_tuned\_model\_checkpoint: String

permission\_id: String

##### ReturnsExpand Collapse

class PermissionDeleteResponse { id, deleted, object }

id: String

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: bool

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

### Delete checkpoint permission

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

permission = openai.fine_tuning.checkpoints.permissions.delete(
  "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  fine_tuned_model_checkpoint: "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd"

puts(permission)

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true

##### Returns Examples

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true
