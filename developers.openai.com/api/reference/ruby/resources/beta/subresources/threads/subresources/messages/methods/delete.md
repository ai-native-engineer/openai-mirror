<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/threads/subresources/messages/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Threads](/api/reference/ruby/resources/beta/subresources/threads)

[Messages](/api/reference/ruby/resources/beta/subresources/threads/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete message

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.messages.delete(message\_id, \*\*kwargs) -> [MessageDeleted](/api/reference/ruby/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}/messages/{message\_id}

Deletes a message.

##### ParametersExpand Collapse

thread\_id: String

message\_id: String

##### ReturnsExpand Collapse

class MessageDeleted { id, deleted, object }

id: String

deleted: bool

object: :"thread.message.deleted"

### Delete message

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

message_deleted = openai.beta.threads.messages.delete("message_id", thread_id: "thread_id")

puts(message_deleted)

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true

##### Returns Examples

  "id": "msg_abc123",
  "object": "thread.message.deleted",
  "deleted": true
