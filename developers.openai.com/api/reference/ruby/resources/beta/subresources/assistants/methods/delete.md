<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/assistants/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Assistants](/api/reference/ruby/resources/beta/subresources/assistants)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete assistant

Deprecated

beta.assistants.delete(assistant\_id) -> [AssistantDeleted](/api/reference/ruby/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/assistants/{assistant\_id}

Delete an assistant.

##### ParametersExpand Collapse

assistant\_id: String

##### ReturnsExpand Collapse

class AssistantDeleted { id, deleted, object }

id: String

deleted: bool

object: :"assistant.deleted"

### Delete assistant

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

assistant_deleted = openai.beta.assistants.delete("assistant_id")

puts(assistant_deleted)

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true

##### Returns Examples

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true
