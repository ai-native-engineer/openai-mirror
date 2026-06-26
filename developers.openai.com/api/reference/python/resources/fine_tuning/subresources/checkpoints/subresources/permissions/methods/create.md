<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create/ -->

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

# Create checkpoint permissions

fine\_tuning.checkpoints.permissions.create(strfine\_tuned\_model\_checkpoint, PermissionCreateParams\*\*kwargs)  -> SyncPage[[PermissionCreateResponse](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_create_response%20%3E%20(schema))]

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### ParametersExpand Collapse

fine\_tuned\_model\_checkpoint: str

project\_ids: Sequence[str]

The project identifiers to grant access to.

##### ReturnsExpand Collapse

class PermissionCreateResponse: …

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

### Create checkpoint permissions

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
page = client.fine_tuning.checkpoints.permissions.create(
    fine_tuned_model_checkpoint="ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
    project_ids=["string"],
page = page.data[0]
print(page.id)

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
