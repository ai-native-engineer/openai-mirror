<!-- source: https://developers.openai.com/api/reference/java/resources/vector_stores/subresources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Vector Stores](/api/reference/java/resources/vector_stores)

[Files](/api/reference/java/resources/vector_stores/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete vector store file

[VectorStoreFileDeleted](/api/reference/java/resources/vector_stores#(resource)%20vector_stores.files%20%3E%20(model)%20vector_store_file_deleted%20%3E%20(schema)) vectorStores().files().delete(FileDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/vector\_stores/{vector\_store\_id}/files/{file\_id}

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

##### ParametersExpand Collapse

FileDeleteParams params

String vectorStoreId

Optional<String> fileId

##### ReturnsExpand Collapse

class VectorStoreFileDeleted:

String id

boolean deleted

JsonValue; object\_ "vector\_store.file.deleted"constant"vector\_store.file.deleted"constant

### Delete vector store file

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
import com.openai.models.vectorstores.files.FileDeleteParams;
import com.openai.models.vectorstores.files.VectorStoreFileDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileDeleteParams params = FileDeleteParams.builder()
            .vectorStoreId("vector_store_id")
            .fileId("file_id")
            .build();
        VectorStoreFileDeleted vectorStoreFileDeleted = client.vectorStores().files().delete(params);

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true

##### Returns Examples

  id: "file-abc123",
  object: "vector_store.file.deleted",
  deleted: true
