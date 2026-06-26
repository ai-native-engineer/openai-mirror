<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/threads/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Threads](/api/reference/python/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.retrieve(strthread\_id)  -> [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

GET/threads/{thread\_id}

Retrieves a thread.

##### ParametersExpand Collapse

thread\_id: str

##### ReturnsExpand Collapse

class Thread: …

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread"]

The object type, which is always `thread`.

tool\_resources: Optional[ToolResources]

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ToolResourcesCodeInterpreter]

file\_ids: Optional[List[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ToolResourcesFileSearch]

vector\_store\_ids: Optional[List[str]]

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

### Retrieve thread

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

my_thread = client.beta.threads.retrieve("thread_abc123")
print(my_thread)

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
