<!-- source: https://developers.openai.com/api/reference/go/resources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

##### [List files](/api/reference/go/resources/files/methods/list)

client.Files.List(ctx, query) (\*CursorPage[[FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))], error)

GET/files

##### [Upload file](/api/reference/go/resources/files/methods/create)

client.Files.New(ctx, body) (\*[FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)), error)

POST/files

##### [Delete file](/api/reference/go/resources/files/methods/delete)

client.Files.Delete(ctx, fileID) (\*[FileDeleted](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)), error)

DELETE/files/{file\_id}

##### [Retrieve file](/api/reference/go/resources/files/methods/retrieve)

client.Files.Get(ctx, fileID) (\*[FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)), error)

GET/files/{file\_id}

##### [Retrieve file content](/api/reference/go/resources/files/methods/content)

client.Files.Content(ctx, fileID) (\*Response, error)

GET/files/{file\_id}/content

##### ModelsExpand Collapse

type FileContent string

type FileDeleted struct{…}

ID string

Deleted bool

Object File

type FileObject struct{…}

The `File` object represents a document that has been uploaded to OpenAI.

ID string

The file identifier, which can be referenced in the API endpoints.

Bytes int64

The size of the file, in bytes.

CreatedAt int64

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

Filename string

The name of the file.

Object File

The object type, which is always `file`.

Purpose FileObjectPurpose

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

const FileObjectPurposeAssistants FileObjectPurpose = "assistants"

const FileObjectPurposeAssistantsOutput FileObjectPurpose = "assistants\_output"

const FileObjectPurposeBatch FileObjectPurpose = "batch"

const FileObjectPurposeBatchOutput FileObjectPurpose = "batch\_output"

const FileObjectPurposeFineTune FileObjectPurpose = "fine-tune"

const FileObjectPurposeFineTuneResults FileObjectPurpose = "fine-tune-results"

const FileObjectPurposeVision FileObjectPurpose = "vision"

const FileObjectPurposeUserData FileObjectPurpose = "user\_data"

DeprecatedStatus FileObjectStatus

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

const FileObjectStatusUploaded FileObjectStatus = "uploaded"

const FileObjectStatusProcessed FileObjectStatus = "processed"

const FileObjectStatusError FileObjectStatus = "error"

ExpiresAt int64Optional

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

DeprecatedStatusDetails stringOptional

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

type FilePurpose string

The intended purpose of the uploaded file. One of:

* `assistants`: Used in the Assistants API
* `batch`: Used in the Batch API
* `fine-tune`: Used for fine-tuning
* `vision`: Images used for vision fine-tuning
* `user_data`: Flexible file type for any purpose
* `evals`: Used for eval data sets

One of the following:

const FilePurposeAssistants [FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) = "assistants"

const FilePurposeBatch [FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) = "batch"

const FilePurposeFineTune [FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) = "fine-tune"

const FilePurposeVision [FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) = "vision"

const FilePurposeUserData [FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) = "user\_data"

const FilePurposeEvals [FilePurpose](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_purpose%20%3E%20(schema)) = "evals"
