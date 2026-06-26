<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

vector\_stores.delete(vector\_store\_id) -> [VectorStoreDeleted](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### ParametersExpand Collapse

vector\_store\_id: String

##### ReturnsExpand Collapse

class VectorStoreDeleted { id, deleted, object }

id: String

deleted: bool

object: :"vector\_store.deleted"

### Delete vector store

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

vector_store_deleted = openai.vector_stores.delete("vector_store_id")

puts(vector_store_deleted)

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
