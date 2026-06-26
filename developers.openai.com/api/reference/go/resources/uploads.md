<!-- source: https://developers.openai.com/api/reference/go/resources/uploads/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Uploads

Use Uploads to upload large files in multiple parts.

##### [Create upload](/api/reference/go/resources/uploads/methods/create)

client.Uploads.New(ctx, body) (\*[Upload](/api/reference/go/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)), error)

POST/uploads

##### [Complete upload](/api/reference/go/resources/uploads/methods/complete)

client.Uploads.Complete(ctx, uploadID, body) (\*[Upload](/api/reference/go/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)), error)

POST/uploads/{upload\_id}/complete

##### [Cancel upload](/api/reference/go/resources/uploads/methods/cancel)

client.Uploads.Cancel(ctx, uploadID) (\*[Upload](/api/reference/go/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)), error)

POST/uploads/{upload\_id}/cancel

##### ModelsExpand Collapse

type Upload struct{…}

The Upload object can accept byte chunks in the form of Parts.

ID string

The Upload unique identifier, which can be referenced in API endpoints.

Bytes int64

The intended number of bytes to be uploaded.

CreatedAt int64

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

Filename string

The name of the file to be uploaded.

Object Upload

The object type, which is always “upload”.

Purpose string

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

Status UploadStatus

The status of the Upload.

One of the following:

const UploadStatusPending UploadStatus = "pending"

const UploadStatusCompleted UploadStatus = "completed"

const UploadStatusCancelled UploadStatus = "cancelled"

const UploadStatusExpired UploadStatus = "expired"

File [FileObject](/api/reference/go/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))Optional

The `File` object represents a document that has been uploaded to OpenAI.

#### UploadsParts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/go/resources/uploads/subresources/parts/methods/create)

client.Uploads.Parts.New(ctx, uploadID, body) (\*[UploadPart](/api/reference/go/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)), error)

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

type UploadPart struct{…}

The upload Part represents a chunk of bytes we can add to an Upload object.

ID string

The upload Part unique identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

Object UploadPart

The object type, which is always `upload.part`.

UploadID string

The ID of the Upload object that this Part was added to.
