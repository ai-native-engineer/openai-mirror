<!-- source: https://developers.openai.com/api/reference/resources/uploads/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Uploads](/api/reference/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create upload

POST/uploads

Creates an intermediate [Upload](/docs/api-reference/uploads/object) object
that you can add [Parts](/docs/api-reference/uploads/part-object) to.
Currently, an Upload can accept at most 8 GB in total and expires after an
hour after you create it.

Once you complete the Upload, we will create a
[File](/docs/api-reference/files/object) object that contains all the parts
you uploaded. This File is usable in the rest of our platform as a regular
File object.

For certain `purpose` values, the correct `mime_type` must be specified.
Please refer to documentation for the
[supported MIME types for your use case](/docs/assistants/tools/file-search#supported-files).

For guidance on the proper filename extensions for each purpose, please
follow the documentation on [creating a
File](/docs/api-reference/files/create).

Returns the Upload object with status `pending`.

##### Body ParametersJSONExpand Collapse

bytes: number

The number of bytes in the file you are uploading.

filename: string

The name of the file to upload.

mime\_type: string

The MIME type of the file.

This must fall within the supported MIME types for your file purpose. See
the supported MIME types for assistants and vision.

purpose: "assistants" or "batch" or "fine-tune" or "vision"

The intended purpose of the uploaded file.

See the [documentation on File
purposes](/docs/api-reference/files/create#files-create-purpose).

One of the following:

"assistants"

"batch"

"fine-tune"

"vision"

expires\_after: optional object { anchor, seconds }

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

anchor: "created\_at"

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

seconds: number

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

Upload object { id, bytes, created\_at, 6 more }

The Upload object can accept byte chunks in the form of Parts.

id: string

The Upload unique identifier, which can be referenced in API endpoints.

bytes: number

The intended number of bytes to be uploaded.

created\_at: number

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

expires\_at: number

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

filename: string

The name of the file to be uploaded.

purpose: string

The intended purpose of the file. [Please refer here](/docs/api-reference/files/object#files/object-purpose) for acceptable values.

status: "pending" or "completed" or "cancelled" or "expired"

The status of the Upload.

One of the following:

"pending"

"completed"

"cancelled"

"expired"

file: optional [FileObject](/api/reference/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

id: string

The file identifier, which can be referenced in the API endpoints.

bytes: number

The size of the file, in bytes.

created\_at: number

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

filename: string

The name of the file.

object: "file"

The object type, which is always `file`.

purpose: "assistants" or "assistants\_output" or "batch" or 5 more

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

"assistants"

"assistants\_output"

"batch"

"batch\_output"

"fine-tune"

"fine-tune-results"

"vision"

"user\_data"

Deprecatedstatus: "uploaded" or "processed" or "error"

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

"uploaded"

"processed"

"error"

expires\_at: optional number

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

Deprecatedstatus\_details: optional string

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

object: optional "upload"

The object type, which is always “upload”.

### Create upload

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/uploads \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "purpose": "fine-tune",
    "filename": "training_examples.jsonl",
    "bytes": 2147483648,
    "mime_type": "text/jsonl",
    "expires_after": {
      "anchor": "created_at",
      "seconds": 3600
  }'

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
