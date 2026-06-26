<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/assistants/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Assistants](/api/reference/python/resources/beta/subresources/assistants)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete assistant

Deprecated

beta.assistants.delete(strassistant\_id)  -> [AssistantDeleted](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema))

DELETE/assistants/{assistant\_id}

Delete an assistant.

##### ParametersExpand Collapse

assistant\_id: str

##### ReturnsExpand Collapse

class AssistantDeleted: …

id: str

deleted: bool

object: Literal["assistant.deleted"]

### Delete assistant

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

response = client.beta.assistants.delete("asst_abc123")
print(response)

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true

##### Returns Examples

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true
