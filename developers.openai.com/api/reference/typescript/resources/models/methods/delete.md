<!-- source: https://developers.openai.com/api/reference/typescript/resources/models/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Models](/api/reference/typescript/resources/models)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a fine-tuned model

client.models.delete(stringmodel, RequestOptionsoptions?): [ModelDeleted](/api/reference/typescript/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

##### ParametersExpand Collapse

model: string

##### ReturnsExpand Collapse

ModelDeleted { id, deleted, object }

id: string

deleted: boolean

object: string

### Delete a fine-tuned model

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const model = await openai.models.delete("ft:gpt-4o-mini:acemeco:suffix:abc123");
  
  console.log(model);
main();

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true

##### Returns Examples

  "id": "ft:gpt-4o-mini:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
