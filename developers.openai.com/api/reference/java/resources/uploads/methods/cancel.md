<!-- source: https://developers.openai.com/api/reference/java/resources/uploads/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Uploads](/api/reference/java/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel upload

[Upload](/api/reference/java/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) uploads().cancel(UploadCancelParamsparams = UploadCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads/{upload\_id}/cancel

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

##### ParametersExpand Collapse

UploadCancelParams params

Optional<String> uploadId

##### ReturnsExpand Collapse

class Upload:

The Upload object can accept byte chunks in the form of Parts.

String id

The Upload unique identifier, which can be referenced in API endpoints.

long bytes

The intended number of bytes to be uploaded.

long createdAt

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

long expiresAt

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

String filename

The name of the file to be uploaded.

JsonValue; object\_ "upload"constant"upload"constant

The object type, which is always “upload”.

String purpose

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

Status status

The status of the Upload.

One of the following:

PENDING("pending")

COMPLETED("completed")

CANCELLED("cancelled")

EXPIRED("expired")

Optional<[FileObject](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))> file

The `File` object represents a document that has been uploaded to OpenAI.

String id

The file identifier, which can be referenced in the API endpoints.

long bytes

The size of the file, in bytes.

long createdAt

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

String filename

The name of the file.

JsonValue; object\_ "file"constant"file"constant

The object type, which is always `file`.

Purpose purpose

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

ASSISTANTS("assistants")

ASSISTANTS\_OUTPUT("assistants\_output")

BATCH("batch")

BATCH\_OUTPUT("batch\_output")

FINE\_TUNE("fine-tune")

FINE\_TUNE\_RESULTS("fine-tune-results")

VISION("vision")

USER\_DATA("user\_data")

DeprecatedStatus status

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

UPLOADED("uploaded")

PROCESSED("processed")

ERROR("error")

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

DeprecatedOptional<String> statusDetails

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Cancel upload

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
import com.openai.models.uploads.Upload;
import com.openai.models.uploads.UploadCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Upload upload = client.uploads().cancel("upload_abc123");

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "cancelled",
  "expires_at": 1719127296

##### Returns Examples

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "cancelled",
  "expires_at": 1719127296
