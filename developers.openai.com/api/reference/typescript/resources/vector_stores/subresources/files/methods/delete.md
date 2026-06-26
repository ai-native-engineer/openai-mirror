<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Vector Stores](/api/reference/typescript/resources/vector_stores)

[Files](/api/reference/typescript/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store file

client.vectorStores.files.delete(stringfileID, FileDeleteParams { vector\_store\_id } params, RequestOptionsoptions?): [VectorStoreFileDeleted](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

##### ParametersExpand Collapse

fileID: string

params: FileDeleteParams { vector\_store\_id }

vector\_store\_id: string

The ID of the vector store that the file belongs to.

##### ReturnsExpand Collapse

VectorStoreFileDeleted { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.file.deleted"

### Delete vector store file

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const deletedVectorStoreFile = await openai.vectorStores.files.delete(
    "file-abc123",
    { vector_store_id: "vs_abc123" }
  );
  console.log(deletedVectorStoreFile);

main();

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true

##### Returns Examples

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true
