<!-- source: https://developers.openai.com/api/reference/ruby/resources/models/methods/retrieve/ -->

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

# Retrieve model

models.retrieve(model) -> [Model](/api/reference/ruby/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by }

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### ParametersExpand Collapse

model: String

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

### Retrieve model

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

model = openai.models.retrieve("gpt-4o-mini")

puts(model)

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
