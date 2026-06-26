<!-- source: https://developers.openai.com/api/reference/ruby/resources/models/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Models](/api/reference/ruby/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List models

models.list() -> Page<[Model](/api/reference/ruby/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by } >

GET/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

##### ReturnsExpand Collapse

class Model { id, created, object, owned\_by }

Describes an OpenAI model offering that can be used with the API.

id: String

The model identifier, which can be referenced in the API endpoints.

created: Integer

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: :model

The object type, which is always “model”.

owned\_by: String

The organization that owns the model.

### List models

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

page = openai.models.list

puts(page)

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
