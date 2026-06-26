<!-- source: https://developers.openai.com/api/reference/typescript/resources/models/methods/list/ -->

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

# List models

client.models.list(RequestOptionsoptions?): Page<[Model](/api/reference/typescript/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by } >

GET/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

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

### List models

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
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
main();

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
