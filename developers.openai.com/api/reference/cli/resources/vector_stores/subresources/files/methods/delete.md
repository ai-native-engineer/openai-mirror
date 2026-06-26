<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Vector Stores](/api/reference/cli/resources/vector_stores)

[Files](/api/reference/cli/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store file

$ openai vector-stores:files delete

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

##### ParametersExpand Collapse

--vector-store-id: string

The ID of the vector store that the file belongs to.

--file-id: string

The ID of the file to delete.

##### ReturnsExpand Collapse

vector\_store\_file\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.file.deleted"

### Delete vector store file

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai vector-stores:files delete \
  --api-key 'My API Key' \
  --vector-store-id vector_store_id \
  --file-id file_id

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true

##### Returns Examples

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true
