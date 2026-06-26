<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/threads/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Threads](/api/reference/ruby/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete thread

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.delete(thread\_id) -> [ThreadDeleted](/api/reference/ruby/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/threads/{thread\_id}

Delete a thread.

##### ParametersExpand Collapse

thread\_id: String

##### ReturnsExpand Collapse

class ThreadDeleted { id, deleted, object }

id: String

deleted: bool

object: :"thread.deleted"

### Delete thread

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

thread_deleted = openai.beta.threads.delete("thread_id")

puts(thread_deleted)

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true

##### Returns Examples

  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
