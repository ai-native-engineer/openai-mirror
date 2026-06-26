<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

[Files](/api/reference/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store file

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](/docs/api-reference/files/delete) endpoint.

##### Path ParametersExpand Collapse

vector\_store\_id: string

file\_id: string

##### ReturnsExpand Collapse

VectorStoreFileDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.file.deleted"

### Delete vector store file

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/vector_stores/vs_abc123/files/file-abc123 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "OpenAI-Beta: assistants=v2" \
  -X DELETE

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true

##### Returns Examples

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true
