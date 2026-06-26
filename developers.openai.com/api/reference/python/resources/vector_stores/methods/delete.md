<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Vector Stores](/api/reference/python/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

vector\_stores.delete(strvector\_store\_id)  -> [VectorStoreDeleted](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema))

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### ParametersExpand Collapse

vector\_store\_id: str

##### ReturnsExpand Collapse

class VectorStoreDeleted: …

id: str

deleted: bool

object: Literal["vector\_store.deleted"]

### Delete vector store

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

deleted_vector_store = client.vector_stores.delete(
  vector_store_id="vs_abc123"
print(deleted_vector_store)

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
