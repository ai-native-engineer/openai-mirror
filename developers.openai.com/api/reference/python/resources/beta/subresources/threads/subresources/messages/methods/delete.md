<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Threads](/api/reference/python/resources/beta/subresources/threads)

[Messages](/api/reference/python/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.messages.delete(strmessage\_id, MessageDeleteParams\*\*kwargs)  -> [MessageDeleted](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema))

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### ParametersExpand Collapse

thread\_id: str

message\_id: str

##### ReturnsExpand Collapse

class MessageDeleted: …

id: str

deleted: bool

object: Literal["thread.message.deleted"]

### Delete message

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

deleted_message = client.beta.threads.messages.delete(
  message_id="msg_abc12",
  thread_id="thread_abc123",
print(deleted_message)

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
