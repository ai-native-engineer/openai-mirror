<!-- source: https://developers.openai.com/api/reference/python/resources/uploads/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Uploads

Use Uploads to upload large files in multiple parts.

##### [Create upload](/api/reference/python/resources/uploads/methods/create)

uploads.create(UploadCreateParams\*\*kwargs)  -> [Upload](/api/reference/python/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema))

POST/uploads

##### [Complete upload](/api/reference/python/resources/uploads/methods/complete)

uploads.complete(strupload\_id, UploadCompleteParams\*\*kwargs)  -> [Upload](/api/reference/python/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema))

POST/uploads/{upload\_id}/complete

##### [Cancel upload](/api/reference/python/resources/uploads/methods/cancel)

uploads.cancel(strupload\_id)  -> [Upload](/api/reference/python/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema))

POST/uploads/{upload\_id}/cancel

##### ModelsExpand Collapse

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

#### UploadsParts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/python/resources/uploads/subresources/parts/methods/create)

uploads.parts.create(strupload\_id, PartCreateParams\*\*kwargs)  -> [UploadPart](/api/reference/python/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema))

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

class UploadPart: …

The upload Part represents a chunk of bytes we can add to an Upload object.

id: str

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

object: Literal["upload.part"]

The object type, which is always `upload.part`.

upload\_id: str

The ID of the Upload object that this Part was added to.
