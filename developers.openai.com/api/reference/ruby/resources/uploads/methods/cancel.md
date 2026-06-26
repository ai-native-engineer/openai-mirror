<!-- source: https://developers.openai.com/api/reference/ruby/resources/uploads/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Uploads](/api/reference/ruby/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel upload

uploads.cancel(upload\_id) -> [Upload](/api/reference/ruby/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

POST/uploads/{upload\_id}/cancel

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

##### ParametersExpand Collapse

upload\_id: String

##### ReturnsExpand Collapse

class Upload { id, bytes, created\_at, 6 more }

The Upload object can accept byte chunks in the form of Parts.

id: String

The Upload unique identifier, which can be referenced in API endpoints.

bytes: Integer

The intended number of bytes to be uploaded.

created\_at: Integer

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

filename: String

The name of the file to be uploaded.

object: :upload

The object type, which is always “upload”.

purpose: String

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

status: :pending | :completed | :cancelled | :expired

The status of the Upload.

One of the following:

:pending

:completed

:cancelled

:expired

file: [FileObject](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

id: String

The file identifier, which can be referenced in the API endpoints.

bytes: Integer

The size of the file, in bytes.

created\_at: Integer

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

filename: String

The name of the file.

object: :file

The object type, which is always `file`.

purpose: :assistants | :assistants\_output | :batch | 5 more

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

:assistants

:assistants\_output

:batch

:batch\_output

:"fine-tune"

:"fine-tune-results"

:vision

:user\_data

Deprecatedstatus: :uploaded | :processed | :error

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

:uploaded

:processed

:error

expires\_at: Integer

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

Deprecatedstatus\_details: String

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Cancel upload

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

upload = openai.uploads.cancel("upload_abc123")

puts(upload)

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
