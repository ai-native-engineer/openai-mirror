<!-- source: https://developers.openai.com/api/reference/resources/models/methods/retrieve/ -->

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

# Retrieve model

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### Path ParametersExpand Collapse

model: string

##### ReturnsExpand Collapse

Model object { id, created, object, owned\_by }

Describes an OpenAI model offering that can be used with the API.

id: string

The model identifier, which can be referenced in the API endpoints.

created: number

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: "model"

The object type, which is always “model”.

owned\_by: string

The organization that owns the model.

### Retrieve model

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/models/VAR_chat_model_id \
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
