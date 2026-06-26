<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Threads](/api/reference/cli/resources/beta/subresources/threads)

[Messages](/api/reference/cli/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

$ openai beta:threads:messages delete

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### ParametersExpand Collapse

--thread-id: string

The ID of the thread to which this message belongs.

--message-id: string

The ID of the message to delete.

##### ReturnsExpand Collapse

message\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "thread.message.deleted"

### Delete message

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:threads:messages delete \
  --api-key 'My API Key' \
  --thread-id thread_id \
  --message-id message_id

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
