<!-- source: https://developers.openai.com/api/reference/cli/resources/uploads/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Uploads

Use Uploads to upload large files in multiple parts.

##### [Create upload](/api/reference/cli/resources/uploads/methods/create)

$ openai uploads create

POST/uploads

##### [Complete upload](/api/reference/cli/resources/uploads/methods/complete)

$ openai uploads complete

POST/uploads/{upload\_id}/complete

##### [Cancel upload](/api/reference/cli/resources/uploads/methods/cancel)

$ openai uploads cancel

POST/uploads/{upload\_id}/cancel

##### ModelsExpand Collapse

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

#### UploadsParts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/cli/resources/uploads/subresources/parts/methods/create)

$ openai uploads:parts create

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

upload\_part: object { id, created\_at, object, upload\_id }

The upload Part represents a chunk of bytes we can add to an Upload object.

id: string

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the Part was created.

object: "upload.part"

The object type, which is always `upload.part`.

upload\_id: string

The ID of the Upload object that this Part was added to.
