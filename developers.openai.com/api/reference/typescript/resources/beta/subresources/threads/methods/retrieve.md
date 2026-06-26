<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/threads/methods/retrieve/ -->

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

# Retrieve thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.beta.threads.retrieve(stringthreadID, RequestOptionsoptions?): [Thread](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

GET/threads/{thread\_id}

Retrieves a thread.

##### ParametersExpand Collapse

threadID: string

##### ReturnsExpand Collapse

Thread { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread"

The object type, which is always `thread`.

tool\_resources: ToolResources | null

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter?: CodeInterpreter { file\_ids }

file\_ids?: Array<string>

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search?: FileSearch { vector\_store\_ids }

vector\_store\_ids?: Array<string>

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

### Retrieve thread

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
  const myThread = await openai.beta.threads.retrieve(
    "thread_abc123"
  );

  console.log(myThread);

main();

  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {},
  "tool_resources": {
    "code_interpreter": {
      "file_ids": []

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {},
  "tool_resources": {
    "code_interpreter": {
      "file_ids": []
