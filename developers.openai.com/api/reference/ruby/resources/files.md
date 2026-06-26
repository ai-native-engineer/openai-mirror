<!-- source: https://developers.openai.com/api/reference/ruby/resources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

##### [List files](/api/reference/ruby/resources/files/methods/list)

files.list(\*\*kwargs) -> CursorPage<[FileObject](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more } >

GET/files

##### [Upload file](/api/reference/ruby/resources/files/methods/create)

files.create(\*\*kwargs) -> [FileObject](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

POST/files

##### [Delete file](/api/reference/ruby/resources/files/methods/delete)

files.delete(file\_id) -> [FileDeleted](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/files/{file\_id}

##### [Retrieve file](/api/reference/ruby/resources/files/methods/retrieve)

files.retrieve(file\_id) -> [FileObject](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

GET/files/{file\_id}

##### [Retrieve file content](/api/reference/ruby/resources/files/methods/content)

files.content(file\_id) -> StringIO

GET/files/{file\_id}/content

##### ModelsExpand Collapse

FileContent = String

class FileDeleted { id, deleted, object }

id: String

deleted: bool

object: :file

class FileObject { id, bytes, created\_at, 6 more }

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

FilePurpose = :assistants | :batch | :"fine-tune" | 3 more

The intended purpose of the uploaded file. One of:

* `assistants`: Used in the Assistants API
* `batch`: Used in the Batch API
* `fine-tune`: Used for fine-tuning
* `vision`: Images used for vision fine-tuning
* `user_data`: Flexible file type for any purpose
* `evals`: Used for eval data sets

One of the following:

:assistants

:batch

:"fine-tune"

:vision

:user\_data

:evals
