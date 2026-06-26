<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Vector Stores](/api/reference/java/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store

[VectorStoreDeleted](/api/reference/java/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_deleted%20%3E%20(schema)) vectorStores().delete(VectorStoreDeleteParamsparams = VectorStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/vector\_stores/{vector\_store\_id}

Delete a vector store.

##### ParametersExpand Collapse

VectorStoreDeleteParams params

Optional<String> vectorStoreId

##### ReturnsExpand Collapse

class VectorStoreDeleted:

String id

boolean deleted

JsonValue; object\_ "vector\_store.deleted"constant"vector\_store.deleted"constant

### Delete vector store

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStoreDeleteParams;
import com.openai.models.vectorstores.VectorStoreDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStoreDeleted vectorStoreDeleted = client.vectorStores().delete("vector_store_id");

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true

##### Returns Examples

  id: "vs_abc123",
  object: "vector_store.deleted",
  deleted: true
