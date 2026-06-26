<!-- source: https://developers.openai.com/api/reference/cli/resources/models/methods/delete/ -->

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

# Delete a fine-tuned model

$ openai models delete

DELETE/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### ParametersExpand Collapse

--model: string

The model to delete

##### ReturnsExpand Collapse

model\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: string

### Delete a fine-tuned model

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai models delete \
  --api-key 'My API Key' \
  --model ft:gpt-4o-mini:acemeco:suffix:abc123

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true

##### Returns Examples

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
