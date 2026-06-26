<!-- source: https://developers.openai.com/api/reference/java/resources/files/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

##### [List files](/api/reference/java/resources/files/methods/list)

FileListPage files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/files

##### [Upload file](/api/reference/java/resources/files/methods/create)

[FileObject](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) files().create(FileCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/files

##### [Delete file](/api/reference/java/resources/files/methods/delete)

[FileDeleted](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_deleted%20%3E%20(schema)) files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/files/{file\_id}

##### [Retrieve file](/api/reference/java/resources/files/methods/retrieve)

[FileObject](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) files().retrieve(FileRetrieveParamsparams = FileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/files/{file\_id}

##### [Retrieve file content](/api/reference/java/resources/files/methods/content)

HttpResponse files().content(FileContentParamsparams = FileContentParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/files/{file\_id}/content

##### ModelsExpand Collapse

class FileDeleted:

String id

boolean deleted

JsonValue; object\_ "file"constant"file"constant

class FileObject:

The `File` object represents a document that has been uploaded to OpenAI.

String id

The file identifier, which can be referenced in the API endpoints.

long bytes

The size of the file, in bytes.

long createdAt

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

String filename

The name of the file.

JsonValue; object\_ "file"constant"file"constant

The object type, which is always `file`.

Purpose purpose

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

ASSISTANTS("assistants")

ASSISTANTS\_OUTPUT("assistants\_output")

BATCH("batch")

BATCH\_OUTPUT("batch\_output")

FINE\_TUNE("fine-tune")

FINE\_TUNE\_RESULTS("fine-tune-results")

VISION("vision")

USER\_DATA("user\_data")

DeprecatedStatus status

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

UPLOADED("uploaded")

PROCESSED("processed")

ERROR("error")

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

DeprecatedOptional<String> statusDetails

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

enum FilePurpose:

The intended purpose of the uploaded file. One of:

* `assistants`: Used in the Assistants API
* `batch`: Used in the Batch API
* `fine-tune`: Used for fine-tuning
* `vision`: Images used for vision fine-tuning
* `user_data`: Flexible file type for any purpose
* `evals`: Used for eval data sets

ASSISTANTS("assistants")

BATCH("batch")

FINE\_TUNE("fine-tune")

VISION("vision")

USER\_DATA("user\_data")

EVALS("evals")
