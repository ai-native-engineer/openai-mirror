<!-- source: https://developers.openai.com/api/reference/python/resources/uploads/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Uploads](/api/reference/python/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create upload

uploads.create(UploadCreateParams\*\*kwargs)  -> [Upload](/api/reference/python/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema))

POST/uploads

Creates an intermediate [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object
that you can add [Parts](https://platform.openai.com/docs/api-reference/uploads/part-object) to.
Currently, an Upload can accept at most 8 GB in total and expires after an
hour after you create it.

Once you complete the Upload, we will create a
[File](https://platform.openai.com/docs/api-reference/files/object) object that contains all the parts
you uploaded. This File is usable in the rest of our platform as a regular
File object.

For certain `purpose` values, the correct `mime_type` must be specified.
Please refer to documentation for the
[supported MIME types for your use case](https://platform.openai.com/docs/assistants/tools/file-search#supported-files).

For guidance on the proper filename extensions for each purpose, please
follow the documentation on [creating a
File](https://platform.openai.com/docs/api-reference/files/create).

Returns the Upload object with status `pending`.

##### ParametersExpand Collapse

bytes: int

The number of bytes in the file you are uploading.

filename: str

The name of the file to upload.

mime\_type: str

The MIME type of the file.

This must fall within the supported MIME types for your file purpose. See
the supported MIME types for assistants and vision.

purpose: [FilePurpose](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema))

The intended purpose of the uploaded file.

See the [documentation on File
purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).

One of the following:

"assistants"

"batch"

"fine-tune"

"vision"

"user\_data"

"evals"

expires\_after: Optional[[ExpiresAfter](/api/reference/python/resources/uploads/methods/create#(resource)%20uploads%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]

The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

anchor: Literal["created\_at"]

Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

seconds: int

The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

formatint64

minimum3600

maximum2592000

##### ReturnsExpand Collapse

class Upload: …

The Upload object can accept byte chunks in the form of Parts.

id: str

The Upload unique identifier, which can be referenced in API endpoints.

bytes: int

The intended number of bytes to be uploaded.

created\_at: int

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

expires\_at: int

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

filename: str

The name of the file to be uploaded.

object: Literal["upload"]

The object type, which is always “upload”.

purpose: str

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

status: Literal["pending", "completed", "cancelled", "expired"]

The status of the Upload.

One of the following:

"pending"

"completed"

"cancelled"

"expired"

file: Optional[FileObject]

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

### Create upload

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
upload = client.uploads.create(
    bytes=0,
    filename="filename",
    mime_type="mime_type",
    purpose="assistants",
print(upload.id)

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
