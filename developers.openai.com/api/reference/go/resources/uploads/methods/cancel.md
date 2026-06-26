<!-- source: https://developers.openai.com/api/reference/go/resources/uploads/methods/cancel/ -->

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

# Cancel upload

client.Uploads.Cancel(ctx, uploadID) (\*[Upload](/api/reference/go/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)), error)

POST/uploads/{upload\_id}/cancel

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

##### ParametersExpand Collapse

uploadID string

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

### Cancel upload

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
  upload, err := client.Uploads.Cancel(context.TODO(), "upload_abc123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", upload.ID)

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
