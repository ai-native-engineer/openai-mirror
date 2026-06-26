<!-- source: https://developers.openai.com/api/reference/go/resources/uploads/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Uploads](/api/reference/go/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create upload

client.Uploads.New(ctx, body) (\*[Upload](/api/reference/go/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)), error)

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

body UploadNewParams

Bytes param.Field[int64]

The number of bytes in the file you are uploading.

Filename param.Field[string]

The name of the file to upload.

MimeType param.Field[string]

The MIME type of the file.

This must fall within the supported MIME types for your file purpose. See
the supported MIME types for assistants and vision.

Purpose param.Field[[FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema))]

The intended purpose of the uploaded file.

See the [documentation on File
purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).

ExpiresAfter param.Field[[UploadNewParamsExpiresAfter](/api/reference/go/resources/uploads/methods/create#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]Optional

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

Anchor CreatedAt

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

Seconds int64

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

type Upload struct{…}

The Upload object can accept byte chunks in the form of Parts.

ID string

The Upload unique identifier, which can be referenced in API endpoints.

Bytes int64

The intended number of bytes to be uploaded.

CreatedAt int64

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

Filename string

The name of the file to be uploaded.

Object Upload

The object type, which is always “upload”.

Purpose string

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

Status UploadStatus

The status of the Upload.

One of the following:

const UploadStatusPending UploadStatus = "pending"

const UploadStatusCompleted UploadStatus = "completed"

const UploadStatusCancelled UploadStatus = "cancelled"

const UploadStatusExpired UploadStatus = "expired"

File [FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))Optional

The `File` object represents a document that has been uploaded to OpenAI.

ID string

The file identifier, which can be referenced in the API endpoints.

Bytes int64

The size of the file, in bytes.

CreatedAt int64

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

Filename string

The name of the file.

Object File

The object type, which is always `file`.

Purpose FileObjectPurpose

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

const FileObjectPurposeAssistants FileObjectPurpose = "assistants"

const FileObjectPurposeAssistantsOutput FileObjectPurpose = "assistants\_output"

const FileObjectPurposeBatch FileObjectPurpose = "batch"

const FileObjectPurposeBatchOutput FileObjectPurpose = "batch\_output"

const FileObjectPurposeFineTune FileObjectPurpose = "fine-tune"

const FileObjectPurposeFineTuneResults FileObjectPurpose = "fine-tune-results"

const FileObjectPurposeVision FileObjectPurpose = "vision"

const FileObjectPurposeUserData FileObjectPurpose = "user\_data"

DeprecatedStatus FileObjectStatus

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

const FileObjectStatusUploaded FileObjectStatus = "uploaded"

const FileObjectStatusProcessed FileObjectStatus = "processed"

const FileObjectStatusError FileObjectStatus = "error"

ExpiresAt int64Optional

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

DeprecatedStatusDetails stringOptional

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Create upload

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  upload, err := client.Uploads.New(context.TODO(), openai.UploadNewParams{
    Bytes: 0,
    Filename: "filename",
    MimeType: "mime_type",
    Purpose: openai.FilePurposeAssistants,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", upload.ID)

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
