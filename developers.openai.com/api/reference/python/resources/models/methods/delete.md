<!-- source: https://developers.openai.com/api/reference/python/resources/models/methods/delete/ -->

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

# Delete a fine-tuned model

models.delete(strmodel)  -> [ModelDeleted](/api/reference/python/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema))

DELETE/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### ParametersExpand Collapse

model: str

##### ReturnsExpand Collapse

class ModelDeleted: …

id: str

deleted: bool

object: str

### Delete a fine-tuned model

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

client.models.delete("ft:gpt-4o-mini:acemeco:suffix:abc123")

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true

##### Returns Examples

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
