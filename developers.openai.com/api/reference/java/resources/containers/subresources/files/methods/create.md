<!-- source: https://developers.openai.com/api/reference/java/resources/containers/subresources/files/methods/create/ -->

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

# Create container file

[FileCreateResponse](/api/reference/java/resources/containers#(resource)%20containers.files%20%3E%20(model)%20FileCreateResponse%20%3E%20(schema)) containers().files().create(FileCreateParamsparams = FileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/containers/{container\_id}/files

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

##### ParametersExpand Collapse

FileCreateParams params

Optional<String> containerId

Optional<InputStream> file

The File object (not file name) to be uploaded.

Optional<String> fileId

Name of the file to create.

##### ReturnsExpand Collapse

class FileCreateResponse:

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

### Create container file

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
import com.openai.models.containers.files.FileCreateParams;
import com.openai.models.containers.files.FileCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileCreateResponse file = client.containers().files().create("container_id");

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
