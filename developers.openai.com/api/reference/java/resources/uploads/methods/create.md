<!-- source: https://developers.openai.com/api/reference/java/resources/uploads/methods/create/ -->

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

# Create upload

[Upload](/api/reference/java/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) uploads().create(UploadCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads

Creates an intermediate [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object
that you can add [Parts](https://platform.openai.com/docs/api-reference/uploads/part-object) to.
Currently, an Upload can accept at most 8 GB in total and expires after an
hour after you create it.

Once you complete the Upload, we will create a
[File](https://platform.openai.com/docs/api-reference/files/object) object that contains all the parts
you uploaded. This File is usable in the rest of our platform as a regular
File object.

For certain `purpose` values, the correct `mime_type` must be specified.
Please refer to documentation for the
[supported MIME types for your use case](https://platform.openai.com/docs/assistants/tools/file-search#supported-files).

For guidance on the proper filename extensions for each purpose, please
follow the documentation on [creating a
File](https://platform.openai.com/docs/api-reference/files/create).

Returns the Upload object with status `pending`.

##### ParametersExpand Collapse

UploadCreateParams params

long bytes

The number of bytes in the file you are uploading.

String filename

The name of the file to upload.

String mimeType

The MIME type of the file.

This must fall within the supported MIME types for your file purpose. See
the supported MIME types for assistants and vision.

[FilePurpose](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) purpose

The intended purpose of the uploaded file.

See the [documentation on File
purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).

Optional<ExpiresAfter> expiresAfter

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

JsonValue; anchor "created\_at"constant"created\_at"constant

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

long seconds

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

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

### Create upload

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
import com.openai.models.files.FilePurpose;
import com.openai.models.uploads.Upload;
import com.openai.models.uploads.UploadCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UploadCreateParams params = UploadCreateParams.builder()
            .bytes(0L)
            .filename("filename")
            .mimeType("mime_type")
            .purpose(FilePurpose.ASSISTANTS)
            .build();
        Upload upload = client.uploads().create(params);

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "pending",
  "expires_at": 1719127296

##### Returns Examples

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "pending",
  "expires_at": 1719127296
