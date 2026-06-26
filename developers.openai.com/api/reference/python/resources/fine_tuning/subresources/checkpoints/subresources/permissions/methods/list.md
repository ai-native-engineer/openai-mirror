<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list/ -->

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

# List checkpoint permissions

fine\_tuning.checkpoints.permissions.list(strfine\_tuned\_model\_checkpoint, PermissionListParams\*\*kwargs)  -> SyncConversationCursorPage[[PermissionListResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_list_response%20%3E%20(schema))]

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fine\_tuned\_model\_checkpoint: str

after: Optional[str]

Identifier for the last permission ID from the previous pagination request.

limit: Optional[int]

Number of permissions to retrieve.

order: Optional[Literal["ascending", "descending"]]

The order in which to retrieve permissions.

One of the following:

"ascending"

"descending"

project\_id: Optional[str]

The ID of the project to get permissions for.

##### ReturnsExpand Collapse

class PermissionListResponse: …

The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

id: str

The permission identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: Literal["checkpoint.permission"]

The object type, which is always “checkpoint.permission”.

project\_id: str

The project identifier that the permission is for.

### List checkpoint permissions

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
page = client.fine_tuning.checkpoints.permissions.list(
    fine_tuned_model_checkpoint="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
page = page.data[0]
print(page.id)

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
