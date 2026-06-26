<!-- source: https://developers.openai.com/api/reference/ruby/resources/uploads/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Uploads

Use Uploads to upload large files in multiple parts.

##### [Create upload](/api/reference/ruby/resources/uploads/methods/create)

uploads.create(\*\*kwargs) -> [Upload](/api/reference/ruby/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

POST/uploads

##### [Complete upload](/api/reference/ruby/resources/uploads/methods/complete)

uploads.complete(upload\_id, \*\*kwargs) -> [Upload](/api/reference/ruby/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

POST/uploads/{upload\_id}/complete

##### [Cancel upload](/api/reference/ruby/resources/uploads/methods/cancel)

uploads.cancel(upload\_id) -> [Upload](/api/reference/ruby/resources/uploads#(resource)%20uploads%20%3E%20(model)%20upload%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

POST/uploads/{upload\_id}/cancel

##### ModelsExpand Collapse

class Upload { id, bytes, created\_at, 6 more }

The Upload object can accept byte chunks in the form of Parts.

id: String

The Upload unique identifier, which can be referenced in API endpoints.

bytes: Integer

The intended number of bytes to be uploaded.

created\_at: Integer

The Unix timestamp (in seconds) for when the Upload was created.

formatunixtime

expires\_at: Integer

The Unix timestamp (in seconds) for when the Upload will expire.

formatunixtime

filename: String

The name of the file to be uploaded.

object: :upload

The object type, which is always “upload”.

purpose: String

The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

status: :pending | :completed | :cancelled | :expired

The status of the Upload.

One of the following:

:pending

:completed

:cancelled

:expired

file: [FileObject](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

#### UploadsParts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/ruby/resources/uploads/subresources/parts/methods/create)

uploads.parts.create(upload\_id, \*\*kwargs) -> [UploadPart](/api/reference/ruby/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)) { id, created\_at, object, upload\_id }

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

class UploadPart { id, created\_at, object, upload\_id }

The upload Part represents a chunk of bytes we can add to an Upload object.

id: String

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

object: :"upload.part"

The object type, which is always `upload.part`.

upload\_id: String

The ID of the Upload object that this Part was added to.
