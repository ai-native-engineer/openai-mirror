<!-- source: https://developers.openai.com/api/reference/cli/resources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

##### [List files](/api/reference/cli/resources/files/methods/list)

$ openai files list

GET/files

##### [Upload file](/api/reference/cli/resources/files/methods/create)

$ openai files create

POST/files

##### [Delete file](/api/reference/cli/resources/files/methods/delete)

$ openai files delete

DELETE/files/{file\_id}

##### [Retrieve file](/api/reference/cli/resources/files/methods/retrieve)

$ openai files retrieve

GET/files/{file\_id}

##### [Retrieve file content](/api/reference/cli/resources/files/methods/content)

$ openai files content

GET/files/{file\_id}/content

##### ModelsExpand Collapse

file\_content: string

file\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: "file"

file\_object: object { id, bytes, created\_at, 6 more }

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

file\_purpose: "assistants" or "batch" or "fine-tune" or 3 more

The intended purpose of the uploaded file. One of:

* `assistants`: Used in the Assistants API
* `batch`: Used in the Batch API
* `fine-tune`: Used for fine-tuning
* `vision`: Images used for vision fine-tuning
* `user_data`: Flexible file type for any purpose
* `evals`: Used for eval data sets

"assistants"

"batch"

"fine-tune"

"vision"

"user\_data"

"evals"
