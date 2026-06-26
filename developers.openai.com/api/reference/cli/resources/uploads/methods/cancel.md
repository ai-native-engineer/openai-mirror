<!-- source: https://developers.openai.com/api/reference/cli/resources/uploads/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Uploads](/api/reference/cli/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel upload

$ openai uploads cancel

POST/uploads/{upload\_id}/cancel

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

##### ParametersExpand Collapse

--upload-id: string

The ID of the Upload.

##### ReturnsExpand Collapse

upload: object { id, bytes, created\_at, 6 more }

The Upload object can accept byte chunks in the form of Parts.

id: string

The Upload unique identifier, which can be referenced in API endpoints.

bytes: number

The intended number of bytes to be uploaded.

created\_at: number

The Unix timestamp (in seconds) for when the Upload was created.

expires\_at: number

The Unix timestamp (in seconds) for when the Upload will expire.

filename: string

The name of the file to be uploaded.

object: "upload"

The object type, which is always “upload”.

purpose: string

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

status: "pending" or "completed" or "cancelled" or "expired"

The status of the Upload.

"pending"

"completed"

"cancelled"

"expired"

file: optional object { id, bytes, created\_at, 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

id: string

The file identifier, which can be referenced in the API endpoints.

bytes: number

The size of the file, in bytes.

created\_at: number

The Unix timestamp (in seconds) for when the file was created.

filename: string

The name of the file.

object: "file"

The object type, which is always `file`.

purpose: "assistants" or "assistants\_output" or "batch" or 5 more

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

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

"uploaded"

"processed"

"error"

expires\_at: optional number

The Unix timestamp (in seconds) for when the file will expire.

Deprecatedstatus\_details: optional string

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Cancel upload

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai uploads cancel \
  --api-key 'My API Key' \
  --upload-id upload_abc123

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
