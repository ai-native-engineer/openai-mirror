<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

[Messages](/api/reference/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### Path ParametersExpand Collapse

thread\_id: string

message\_id: string

##### ReturnsExpand Collapse

MessageDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "thread.message.deleted"

### Delete message

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/threads/thread_abc123/messages/msg_abc123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v2"

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
