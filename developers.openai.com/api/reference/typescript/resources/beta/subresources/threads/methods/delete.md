<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Threads](/api/reference/typescript/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.beta.threads.delete(stringthreadID, RequestOptionsoptions?): [ThreadDeleted](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}

Delete a thread.

##### ParametersExpand Collapse

threadID: string

##### ReturnsExpand Collapse

ThreadDeleted { id, deleted, object }

id: string

deleted: boolean

object: "thread.deleted"

### Delete thread

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
  const response = await openai.beta.threads.delete("thread_abc123");

  console.log(response);
main();

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
