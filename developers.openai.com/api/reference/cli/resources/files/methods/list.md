<!-- source: https://developers.openai.com/api/reference/cli/resources/files/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Files](/api/reference/cli/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List files

$ openai files list

GET/files

Returns a list of files.

##### ParametersExpand Collapse

--after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

--limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

--order: optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

--purpose: optional string

Only return files with the given purpose.

##### ReturnsExpand Collapse

ListFilesResponse: object { data, first\_id, has\_more, 2 more }

data: array of [FileObject](/api/reference/cli/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

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

first\_id: string

has\_more: boolean

last\_id: string

object: string

### List files

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai files list \
  --api-key 'My API Key'

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
