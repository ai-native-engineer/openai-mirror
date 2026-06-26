<!-- source: https://developers.openai.com/api/reference/go/resources/files/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Files](/api/reference/go/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Upload file

client.Files.New(ctx, body) (\*[FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)), error)

POST/files

Upload a file that can be used across various endpoints. Individual files
can be up to 512 MB, and each project can store up to 2.5 TB of files in
total. There is no organization-wide storage limit. Uploads to this
endpoint are rate-limited to 1,000 requests per minute per authenticated
user.

* The Assistants API supports files up to 2 million tokens and of specific
  file types. See the [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools) for
  details.
* The Fine-tuning API only supports `.jsonl` files. The input also has
  certain required formats for fine-tuning
  [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input) or
  [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) models.
* The Batch API only supports `.jsonl` files up to 200 MB in size. The input
  also has a specific required
  [format](https://platform.openai.com/docs/api-reference/batch/request-input).
* For Retrieval or `file_search` ingestion, upload files here first. If
  you need to attach multiple uploaded files to the same vector store, use
  [`/vector_stores/{vector_store_id}/file_batches`](https://platform.openai.com/docs/api-reference/vector-stores-file-batches/createBatch)
  instead of attaching them one by one. Vector store attachment has separate
  limits from file upload, including 2,000 attached files per minute per
  organization.

Please [contact us](https://help.openai.com/) if you need to increase these
storage limits.

##### ParametersExpand Collapse

body FileNewParams

File param.Field[[Reader](/api/reference/go/resources/files/methods/create#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20file%20%3E%20(schema))]

The File object (not file name) to be uploaded.

Purpose param.Field[[FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema))]

The intended purpose of the uploaded file. One of:

* `assistants`: Used in the Assistants API
* `batch`: Used in the Batch API
* `fine-tune`: Used for fine-tuning
* `vision`: Images used for vision fine-tuning
* `user_data`: Flexible file type for any purpose
* `evals`: Used for eval data sets

ExpiresAfter param.Field[[FileNewParamsExpiresAfter](/api/reference/go/resources/files/methods/create#(resource)%20files%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]Optional

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

Anchor CreatedAt

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

Seconds int64

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

type FileObject struct{…}

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

### Upload file

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
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  fileObject, err := client.Files.New(context.TODO(), openai.FileNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    Purpose: openai.FilePurposeAssistants,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", fileObject.ID)

  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "expires_at": 1677614202,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",

##### Returns Examples

  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "expires_at": 1677614202,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",
