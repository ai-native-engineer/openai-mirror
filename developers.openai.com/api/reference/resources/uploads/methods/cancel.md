<!-- source: https://developers.openai.com/api/reference/resources/uploads/methods/cancel/ -->

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

# Cancel upload

POST/uploads/{upload\_id}/cancel

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

##### Path ParametersExpand Collapse

upload\_id: string

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

### Cancel upload

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/uploads/upload_abc123/cancel

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
