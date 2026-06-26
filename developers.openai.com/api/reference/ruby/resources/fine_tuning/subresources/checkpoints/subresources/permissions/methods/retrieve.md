<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve/ -->

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

# List checkpoint permissions

Deprecated: Retrieve is deprecated. Please swap to the paginated list method instead.

fine\_tuning.checkpoints.permissions.retrieve(fine\_tuned\_model\_checkpoint, \*\*kwargs) -> [PermissionRetrieveResponse](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20permission_retrieve_response%20%3E%20(schema)) { data, has\_more, object, 2 more }

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

fine\_tuned\_model\_checkpoint: String

after: String

Identifier for the last permission ID from the previous pagination request.

limit: Integer

Number of permissions to retrieve.

order: :ascending | :descending

The order in which to retrieve permissions.

One of the following:

:ascending

:descending

project\_id: String

The ID of the project to get permissions for.

##### ReturnsExpand Collapse

class PermissionRetrieveResponse { data, has\_more, object, 2 more }

data: Array[Data{ id, created\_at, object, project\_id}]

id: String

The permission identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the permission was created.

formatunixtime

object: :"checkpoint.permission"

The object type, which is always “checkpoint.permission”.

project\_id: String

The project identifier that the permission is for.

has\_more: bool

object: :list

first\_id: String

last\_id: String

### List checkpoint permissions

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

permission = openai.fine_tuning.checkpoints.permissions.retrieve("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(permission)

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
