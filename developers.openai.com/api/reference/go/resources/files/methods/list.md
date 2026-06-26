<!-- source: https://developers.openai.com/api/reference/go/resources/files/methods/list/ -->

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

# List files

client.Files.List(ctx, query) (\*CursorPage[[FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))], error)

GET/files

Returns a list of files.

##### ParametersExpand Collapse

query FileListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

Order param.Field[[FileListParamsOrder](/api/reference/go/resources/files/methods/list#(resource)%20files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const FileListParamsOrderAsc [FileListParamsOrder](/api/reference/go/resources/files/methods/list#(resource)%20files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const FileListParamsOrderDesc [FileListParamsOrder](/api/reference/go/resources/files/methods/list#(resource)%20files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

Purpose param.Field[string]Optional

Only return files with the given purpose.

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

### List files

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
  page, err := client.Files.List(context.TODO(), openai.FileListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "expires_at": 1677614202,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
      "id": "file-abc456",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "expires_at": 1677614202,
      "filename": "puppy.jsonl",
      "purpose": "fine-tune",
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "expires_at": 1677614202,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
      "id": "file-abc456",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "expires_at": 1677614202,
      "filename": "puppy.jsonl",
      "purpose": "fine-tune",
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false
