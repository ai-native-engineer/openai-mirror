<!-- source: https://developers.openai.com/api/reference/cli/resources/models/methods/retrieve/ -->

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

# Retrieve model

$ openai models retrieve

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### ParametersExpand Collapse

--model: string

The ID of the model to use for this request

##### ReturnsExpand Collapse

model: object { id, created, object, owned\_by }

Describes an OpenAI model offering that can be used with the API.

id: string

The model identifier, which can be referenced in the API endpoints.

created: number

The Unix timestamp (in seconds) when the model was created.

object: "model"

The object type, which is always “model”.

owned\_by: string

The organization that owns the model.

### Retrieve model

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai models retrieve \
  --api-key 'My API Key' \
  --model gpt-4o-mini

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
