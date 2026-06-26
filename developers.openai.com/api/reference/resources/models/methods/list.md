<!-- source: https://developers.openai.com/api/reference/resources/models/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Models](/api/reference/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List models

GET/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

##### ReturnsExpand Collapse

data: array of [Model](/api/reference/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by }

id: string

The model identifier, which can be referenced in the API endpoints.

created: number

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: "model"

The object type, which is always “model”.

owned\_by: string

The organization that owns the model.

object: "list"

### List models

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

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
