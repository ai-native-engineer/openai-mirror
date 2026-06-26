<!-- source: https://developers.openai.com/api/reference/typescript/resources/models/methods/retrieve/ -->

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

# Retrieve model

client.models.retrieve(stringmodel, RequestOptionsoptions?): [Model](/api/reference/typescript/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by }

GET/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

##### ParametersExpand Collapse

model: string

##### ReturnsExpand Collapse

Model { id, created, object, owned\_by }

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
  const model = await openai.models.retrieve("VAR_chat_model_id");

  console.log(model);

main();

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"

##### Returns Examples

  "id": "VAR_chat_model_id",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
