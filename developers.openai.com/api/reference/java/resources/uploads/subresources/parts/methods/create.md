<!-- source: https://developers.openai.com/api/reference/java/resources/uploads/subresources/parts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Uploads](/api/reference/java/resources/uploads)

[Parts](/api/reference/java/resources/uploads/subresources/parts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add upload part

[UploadPart](/api/reference/java/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)) uploads().parts().create(PartCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads/{upload\_id}/parts

Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

##### ParametersExpand Collapse

PartCreateParams params

Optional<String> uploadId

InputStream data

The chunk of bytes for this Part.

##### ReturnsExpand Collapse

class UploadPart:

The upload Part represents a chunk of bytes we can add to an Upload object.

String id

The upload Part unique identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

JsonValue; object\_ "upload.part"constant"upload.part"constant

The object type, which is always `upload.part`.

String uploadId

The ID of the Upload object that this Part was added to.

### Add upload part

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
import com.openai.models.uploads.parts.PartCreateParams;
import com.openai.models.uploads.parts.UploadPart;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PartCreateParams params = PartCreateParams.builder()
            .uploadId("upload_abc123")
            .data(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        UploadPart uploadPart = client.uploads().parts().create(params);

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"

##### Returns Examples

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"
