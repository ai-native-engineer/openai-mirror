<!-- source: https://developers.openai.com/api/reference/python/resources/models/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Models](/api/reference/python/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve model

models.retrieve(strmodel)  -> [Model](/api/reference/python/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema))

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### ParametersExpand Collapse

model: str

##### ReturnsExpand Collapse

class Model: …

Describes an OpenAI model offering that can be used with the API.

id: str

The model identifier, which can be referenced in the API endpoints.

created: int

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: Literal["model"]

The object type, which is always “model”.

owned\_by: str

The organization that owns the model.

### Retrieve model

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

client.models.retrieve("VAR_chat_model_id")

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
