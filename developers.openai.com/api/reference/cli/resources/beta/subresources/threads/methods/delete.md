<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/threads/methods/delete/ -->

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

# Delete thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

$ openai beta:threads delete

DELETE/threads/{thread\_id}

Delete a thread.

##### ParametersExpand Collapse

--thread-id: string

The ID of the thread to delete.

##### ReturnsExpand Collapse

thread\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "thread.deleted"

### Delete thread

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:threads delete \
  --api-key 'My API Key' \
  --thread-id thread_id

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
