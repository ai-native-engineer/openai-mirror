<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/assistants/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Assistants](/api/reference/cli/resources/beta/subresources/assistants)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete assistant

Deprecated

$ openai beta:assistants delete

DELETE/assistants/{assistant\_id}

Delete an assistant.

##### ParametersExpand Collapse

--assistant-id: string

The ID of the assistant to delete.

##### ReturnsExpand Collapse

assistant\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "assistant.deleted"

### Delete assistant

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:assistants delete \
  --api-key 'My API Key' \
  --assistant-id assistant_id

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true

##### Returns Examples

  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true
