<!-- source: https://developers.openai.com/api/reference/python/resources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

##### [List files](/api/reference/python/resources/files/methods/list)

files.list(FileListParams\*\*kwargs)  -> SyncCursorPage[[FileObject](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))]

GET/files

##### [Upload file](/api/reference/python/resources/files/methods/create)

files.create(FileCreateParams\*\*kwargs)  -> [FileObject](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))

POST/files

##### [Delete file](/api/reference/python/resources/files/methods/delete)

files.delete(strfile\_id)  -> [FileDeleted](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema))

DELETE/files/{file\_id}

##### [Retrieve file](/api/reference/python/resources/files/methods/retrieve)

files.retrieve(strfile\_id)  -> [FileObject](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))

GET/files/{file\_id}

##### [Retrieve file content](/api/reference/python/resources/files/methods/content)

files.content(strfile\_id)  -> BinaryResponseContent

GET/files/{file\_id}/content

##### [Retrieve file content](/api/reference/python/resources/files/methods/retrieve_content)

Deprecated

files.retrieve\_content(strfile\_id)  -> [FileContent](/api/reference/python/resources/files#(resource)%20files%20%3E%20(model)%20file_content%20%3E%20(schema))

GET/files/{file\_id}/content

##### ModelsExpand Collapse

str

class FileDeleted: …

id: str

deleted: bool

object: Literal["file"]

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

Literal["assistants", "batch", "fine-tune", 3 more]

The intended purpose of the uploaded file. One of:

* `assistants`: Used in the Assistants API
* `batch`: Used in the Batch API
* `fine-tune`: Used for fine-tuning
* `vision`: Images used for vision fine-tuning
* `user_data`: Flexible file type for any purpose
* `evals`: Used for eval data sets

One of the following:

"assistants"

"batch"

"fine-tune"

"vision"

"user\_data"

"evals"
