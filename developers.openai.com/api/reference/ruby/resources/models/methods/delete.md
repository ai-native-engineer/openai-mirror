<!-- source: https://developers.openai.com/api/reference/ruby/resources/models/methods/delete/ -->

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

# Delete a fine-tuned model

models.delete(model) -> [ModelDeleted](/api/reference/ruby/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### ParametersExpand Collapse

model: String

##### ReturnsExpand Collapse

class ModelDeleted { id, deleted, object }

id: String

deleted: bool

object: String

### Delete a fine-tuned model

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

model_deleted = openai.models.delete("ft:gpt-4o-mini:acemeco:suffix:abc123")

puts(model_deleted)

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true

##### Returns Examples

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
