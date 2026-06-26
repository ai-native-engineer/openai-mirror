<!-- source: https://developers.openai.com/api/reference/python/resources/uploads/methods/complete/ -->

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

# Complete upload

uploads.complete(strupload\_id, UploadCompleteParams\*\*kwargs)  -> [Upload](/api/reference/python/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema))

POST/uploads/{upload\_id}/complete

Completes the [Upload](https://platform.openai.com/docs/api-reference/uploads/object).

Within the returned Upload object, there is a nested [File](https://platform.openai.com/docs/api-reference/files/object) object that is ready to use in the rest of the platform.

You can specify the order of the Parts by passing in an ordered list of the Part IDs.

The number of bytes uploaded upon completion must match the number of bytes initially specified when creating the Upload object. No Parts may be added after an Upload is completed.
Returns the Upload object with status `completed`, including an additional `file` property containing the created usable File object.

##### ParametersExpand Collapse

upload\_id: str

part\_ids: Sequence[str]

The ordered list of Part IDs.

md5: Optional[str]

The optional md5 checksum for the file contents to verify if the bytes uploaded matches what you expect.

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

### Complete upload

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
upload = client.uploads.complete(
    upload_id="upload_abc123",
    part_ids=["string"],
print(upload.id)

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "completed",
  "expires_at": 1719127296,
  "file": {
    "id": "file-xyz321",
    "object": "file",
    "bytes": 2147483648,
    "created_at": 1719186911,
    "expires_at": 1719127296,
    "filename": "training_examples.jsonl",
    "purpose": "fine-tune",

##### Returns Examples

  "id": "upload_abc123",
  "object": "upload",
  "bytes": 2147483648,
  "created_at": 1719184911,
  "filename": "training_examples.jsonl",
  "purpose": "fine-tune",
  "status": "completed",
  "expires_at": 1719127296,
  "file": {
    "id": "file-xyz321",
    "object": "file",
    "bytes": 2147483648,
    "created_at": 1719186911,
    "expires_at": 1719127296,
    "filename": "training_examples.jsonl",
    "purpose": "fine-tune",
