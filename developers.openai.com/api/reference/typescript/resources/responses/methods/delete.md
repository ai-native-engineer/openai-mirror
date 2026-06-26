<!-- source: https://developers.openai.com/api/reference/typescript/resources/responses/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Responses](/api/reference/typescript/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a model response

client.responses.delete(stringresponseID, RequestOptionsoptions?): void

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

responseID: string

### Delete a model response

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
const client = new OpenAI();

const response = await client.responses.delete("resp_123");
console.log(response);

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

##### Returns Examples

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
