<!-- source: https://developers.openai.com/api/reference/java/resources/containers/subresources/files/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Containers](/api/reference/java/resources/containers)

[Files](/api/reference/java/resources/containers/subresources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve container file

[FileRetrieveResponse](/api/reference/java/resources/containers#(resource)%20containers.files%20%3E%20(model)%20FileRetrieveResponse%20%3E%20(schema)) containers().files().retrieve(FileRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/containers/{container\_id}/files/{file\_id}

Retrieve Container File

##### ParametersExpand Collapse

FileRetrieveParams params

String containerId

Optional<String> fileId

##### ReturnsExpand Collapse

class FileRetrieveResponse:

String id

Unique identifier for the file.

long bytes

Size of the file in bytes.

String containerId

The container this file belongs to.

long createdAt

Unix timestamp (in seconds) when the file was created.

formatunixtime

JsonValue; object\_ "container.file"constant"container.file"constant

The type of this object (`container.file`).

String path

Path of the file in the container.

String source

Source of the file (e.g., `user`, `assistant`).

### Retrieve container file

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
import com.openai.models.containers.files.FileRetrieveParams;
import com.openai.models.containers.files.FileRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileRetrieveParams params = FileRetrieveParams.builder()
            .containerId("container_id")
            .fileId("file_id")
            .build();
        FileRetrieveResponse file = client.containers().files().retrieve(params);

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file",
    "created_at": 1747848842,
    "bytes": 880,
    "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
    "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
    "source": "user"

##### Returns Examples

    "id": "cfile_682e0e8a43c88191a7978f477a09bdf5",
    "object": "container.file",
    "created_at": 1747848842,
    "bytes": 880,
    "container_id": "cntr_682e0e7318108198aa783fd921ff305e08e78805b9fdbb04",
    "path": "/mnt/data/88e12fa445d32636f190a0b33daed6cb-tsconfig.json",
    "source": "user"
