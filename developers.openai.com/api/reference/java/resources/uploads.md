<!-- source: https://developers.openai.com/api/reference/java/resources/uploads/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Uploads

Use Uploads to upload large files in multiple parts.

##### [Create upload](/api/reference/java/resources/uploads/methods/create)

[Upload](/api/reference/java/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) uploads().create(UploadCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads

##### [Complete upload](/api/reference/java/resources/uploads/methods/complete)

[Upload](/api/reference/java/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) uploads().complete(UploadCompleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads/{upload\_id}/complete

##### [Cancel upload](/api/reference/java/resources/uploads/methods/cancel)

[Upload](/api/reference/java/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) uploads().cancel(UploadCancelParamsparams = UploadCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads/{upload\_id}/cancel

##### ModelsExpand Collapse

class Upload:

The Upload object can accept byte chunks in the form of Parts.

String id

The Upload unique identifier, which can be referenced in API endpoints.

long bytes

The intended number of bytes to be uploaded.

long createdAt

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

long expiresAt

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

String filename

The name of the file to be uploaded.

JsonValue; object\_ "upload"constant"upload"constant

The object type, which is always “upload”.

String purpose

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

Status status

The status of the Upload.

One of the following:

PENDING("pending")

COMPLETED("completed")

CANCELLED("cancelled")

EXPIRED("expired")

Optional<[FileObject](/api/reference/java/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema))> file

The `File` object represents a document that has been uploaded to OpenAI.

#### UploadsParts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/java/resources/uploads/subresources/parts/methods/create)

[UploadPart](/api/reference/java/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)) uploads().parts().create(PartCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

class UploadPart:

The upload Part represents a chunk of bytes we can add to an Upload object.

String id

The upload Part unique identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

JsonValue; object\_ "upload.part"constant"upload.part"constant

The object type, which is always `upload.part`.

String uploadId

The ID of the Upload object that this Part was added to.
