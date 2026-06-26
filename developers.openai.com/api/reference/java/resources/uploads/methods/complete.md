<!-- source: https://developers.openai.com/api/reference/java/resources/uploads/methods/complete/ -->

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

# Complete upload

[Upload](/api/reference/java/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) uploads().complete(UploadCompleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads/{upload\_id}/complete

Completes the [Upload](https://platform.openai.com/docs/api-reference/uploads/object).

Within the returned Upload object, there is a nested [File](https://platform.openai.com/docs/api-reference/files/object) object that is ready to use in the rest of the platform.

You can specify the order of the Parts by passing in an ordered list of the Part IDs.

The number of bytes uploaded upon completion must match the number of bytes initially specified when creating the Upload object. No Parts may be added after an Upload is completed.
Returns the Upload object with status `completed`, including an additional `file` property containing the created usable File object.

##### ParametersExpand Collapse

UploadCompleteParams params

Optional<String> uploadId

List<String> partIds

The ordered list of Part IDs.

Optional<String> md5

The optional md5 checksum for the file contents to verify if the bytes uploaded matches what you expect.

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

### Complete upload

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
import com.openai.models.uploads.UploadCompleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UploadCompleteParams params = UploadCompleteParams.builder()
            .uploadId("upload_abc123")
            .addPartId("string")
            .build();
        Upload upload = client.uploads().complete(params);

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "completed",
  "expires_at": 1719127296,
  "file": {
    "id": "file-xyz321",
    "object": "file",
    "bytes": 2147483648,
    "created_at": 1719186911,
    "expires_at": 1719127296,
    "filename": "training_examples.jsonl",
    "purpose": "fine-tune",

##### Returns Examples

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "completed",
  "expires_at": 1719127296,
  "file": {
    "id": "file-xyz321",
    "object": "file",
    "bytes": 2147483648,
    "created_at": 1719186911,
    "expires_at": 1719127296,
    "filename": "training_examples.jsonl",
    "purpose": "fine-tune",
