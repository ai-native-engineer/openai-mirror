<!-- source: https://developers.openai.com/api/reference/cli/resources/models/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Models](/api/reference/cli/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List models

$ openai models list

GET/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

##### ReturnsExpand Collapse

ListModelsResponse: object { data, object }

data: array of [Model](/api/reference/cli/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by }

id: string

The model identifier, which can be referenced in the API endpoints.

created: number

The Unix timestamp (in seconds) when the model was created.

object: "model"

The object type, which is always “model”.

owned\_by: string

The organization that owns the model.

object: "list"

### List models

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai models list \
  --api-key 'My API Key'

  "object": "list",
  "data": [
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
      "id": "model-id-1",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner",
      "id": "model-id-2",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
  ]

##### Returns Examples

  "object": "list",
  "data": [
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
      "id": "model-id-1",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner",
      "id": "model-id-2",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
  ]
