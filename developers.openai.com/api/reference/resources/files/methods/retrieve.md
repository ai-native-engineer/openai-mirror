<!-- source: https://developers.openai.com/api/reference/resources/files/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Files](/api/reference/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve file

GET/files/{file\_id}

Returns information about a specific file.

##### Path ParametersExpand Collapse

file\_id: string

##### ReturnsExpand Collapse

FileObject object { id, bytes, created\_at, 6 more }

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

### Retrieve file

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/files/file-abc123 \
  -H "Authorization: Bearer $OPENAI_API_KEY"

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
