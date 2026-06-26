<!-- source: https://developers.openai.com/api/reference/java/resources/files/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Files](/api/reference/java/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete file

[FileDeleted](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)) files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/files/{file\_id}

Delete a file and remove it from all vector stores.

##### ParametersExpand Collapse

FileDeleteParams params

Optional<String> fileId

##### ReturnsExpand Collapse

class FileDeleted:

String id

boolean deleted

JsonValue; object\_ "file"constant"file"constant

### Delete file

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
import com.openai.models.files.FileDeleteParams;
import com.openai.models.files.FileDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileDeleted fileDeleted = client.files().delete("file_id");

  "id": "file-abc123",
  "object": "file",
  "deleted": true

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "deleted": true
