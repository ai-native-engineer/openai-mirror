<!-- source: https://developers.openai.com/api/reference/typescript/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Vector Stores](/api/reference/typescript/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

client.vectorStores.delete(stringvectorStoreID, RequestOptionsoptions?): [VectorStoreDeleted](/api/reference/typescript/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### ParametersExpand Collapse

vectorStoreID: string

##### ReturnsExpand Collapse

VectorStoreDeleted { id, deleted, object }

id: string

deleted: boolean

object: "vector\_store.deleted"

### Delete vector store

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
  const deletedVectorStore = await openai.vectorStores.delete(
    "vs_abc123"
  );
  console.log(deletedVectorStore);

main();

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
