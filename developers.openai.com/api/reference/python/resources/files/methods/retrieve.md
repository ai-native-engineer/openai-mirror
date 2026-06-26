<!-- source: https://developers.openai.com/api/reference/python/resources/files/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Files](/api/reference/python/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve file

files.retrieve(strfile\_id)  -> [FileObject](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))

GET/files/{file\_id}

Returns information about a specific file.

##### ParametersExpand Collapse

file\_id: str

##### ReturnsExpand Collapse

class FileObject: …

The `File` object represents a document that has been uploaded to OpenAI.

id: str

The file identifier, which can be referenced in the API endpoints.

bytes: int

The size of the file, in bytes.

created\_at: int

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

filename: str

The name of the file.

object: Literal["file"]

The object type, which is always `file`.

purpose: Literal["assistants", "assistants\_output", "batch", 5 more]

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

Deprecatedstatus: Literal["uploaded", "processed", "error"]

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

"uploaded"

"processed"

"error"

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

Deprecatedstatus\_details: Optional[str]

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Retrieve file

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

client.files.retrieve("file-abc123")

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
