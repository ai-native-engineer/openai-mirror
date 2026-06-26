<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

DELETE/threads/{thread\_id}

Delete a thread.

##### Path ParametersExpand Collapse

thread\_id: string

##### ReturnsExpand Collapse

ThreadDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "thread.deleted"

### Delete thread

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/threads/thread_abc123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v2" \
  -X DELETE

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
