<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/assistants/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Assistants](/api/reference/typescript/resources/beta/subresources/assistants)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete assistant

Deprecated

client.beta.assistants.delete(stringassistantID, RequestOptionsoptions?): [AssistantDeleted](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/assistants/{assistant\_id}

Delete an assistant.

##### ParametersExpand Collapse

assistantID: string

##### ReturnsExpand Collapse

AssistantDeleted { id, deleted, object }

id: string

deleted: boolean

object: "assistant.deleted"

### Delete assistant

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
  const response = await openai.beta.assistants.delete("asst_abc123");

  console.log(response);
main();

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true

##### Returns Examples

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true
