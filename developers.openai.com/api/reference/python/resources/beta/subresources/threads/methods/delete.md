<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/threads/methods/delete/ -->

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

# Delete thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.delete(strthread\_id)  -> [ThreadDeleted](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema))

DELETE/threads/{thread\_id}

Delete a thread.

##### ParametersExpand Collapse

thread\_id: str

##### ReturnsExpand Collapse

class ThreadDeleted: …

id: str

deleted: bool

object: Literal["thread.deleted"]

### Delete thread

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

response = client.beta.threads.delete("thread_abc123")
print(response)

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
