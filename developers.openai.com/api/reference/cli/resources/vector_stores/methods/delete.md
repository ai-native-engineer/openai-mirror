<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Vector Stores](/api/reference/cli/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

$ openai vector-stores delete

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### ParametersExpand Collapse

--vector-store-id: string

The ID of the vector store to delete.

##### ReturnsExpand Collapse

vector\_store\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.deleted"

### Delete vector store

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai vector-stores delete \
  --api-key 'My API Key' \
  --vector-store-id vector_store_id

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
