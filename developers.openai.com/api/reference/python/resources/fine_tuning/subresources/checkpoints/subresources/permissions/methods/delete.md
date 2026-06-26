<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Fine Tuning](/api/reference/python/resources/fine_tuning)

[Checkpoints](/api/reference/python/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete checkpoint permission

fine\_tuning.checkpoints.permissions.delete(strpermission\_id, PermissionDeleteParams\*\*kwargs)  -> [PermissionDeleteResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_delete_response%20%3E%20(schema))

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fine\_tuned\_model\_checkpoint: str

permission\_id: str

##### ReturnsExpand Collapse

class PermissionDeleteResponse: …

id: str

The ID of the fine-tuned model checkpoint permission that was deleted.

deleted: bool

Whether the fine-tuned model checkpoint permission was successfully deleted.

object: Literal["checkpoint.permission"]

The object type, which is always “checkpoint.permission”.

### Delete checkpoint permission

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
permission = client.fine_tuning.checkpoints.permissions.delete(
    permission_id="cp_zc4Q7MP6XxulcVzj4MZdwsAB",
    fine_tuned_model_checkpoint="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
print(permission.id)

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true

##### Returns Examples

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true
