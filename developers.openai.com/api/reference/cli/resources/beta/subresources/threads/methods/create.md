<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/threads/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Threads](/api/reference/cli/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

$ openai beta:threads create

POST/threads

Create a thread.

##### ParametersExpand Collapse

--message: optional array of object { content, role, attachments, metadata }

A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.

--metadata: optional map[string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

--tool-resources: optional object { code\_interpreter, file\_search }

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

##### ReturnsExpand Collapse

thread: object { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the thread was created.

metadata: map[string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread"

The object type, which is always `thread`.

tool\_resources: object { code\_interpreter, file\_search }

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: optional object { file\_ids }

file\_ids: optional array of string

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: optional object { vector\_store\_ids }

vector\_store\_ids: optional array of string

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

### Create thread

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:threads create \
  --api-key 'My API Key'

200 example

  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  "object": "thread",
  "tool_resources": {
    "code_interpreter": {
      "file_ids": [
        "string"
      ]
    "file_search": {
      "vector_store_ids": [
        "string"
      ]

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  "object": "thread",
  "tool_resources": {
    "code_interpreter": {
      "file_ids": [
        "string"
      ]
    "file_search": {
      "vector_store_ids": [
        "string"
      ]
