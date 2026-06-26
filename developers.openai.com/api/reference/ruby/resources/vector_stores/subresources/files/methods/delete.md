<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

[Files](/api/reference/ruby/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store file

vector\_stores.files.delete(file\_id, \*\*kwargs) -> [VectorStoreFileDeleted](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

##### ParametersExpand Collapse

vector\_store\_id: String

file\_id: String

##### ReturnsExpand Collapse

class VectorStoreFileDeleted { id, deleted, object }

id: String

deleted: bool

object: :"vector\_store.file.deleted"

### Delete vector store file

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

vector_store_file_deleted = openai.vector_stores.files.delete("file_id", vector_store_id: "vector_store_id")

puts(vector_store_file_deleted)

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true

##### Returns Examples

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true
