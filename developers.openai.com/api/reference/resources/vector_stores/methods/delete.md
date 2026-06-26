<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### Path ParametersExpand Collapse

vector\_store\_id: string

##### ReturnsExpand Collapse

VectorStoreDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.deleted"

### Delete vector store

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/vector_stores/vs_abc123 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Beta: assistants=v2" \
  -X DELETE

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
