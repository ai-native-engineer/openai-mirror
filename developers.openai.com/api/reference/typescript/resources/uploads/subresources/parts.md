<!-- source: https://developers.openai.com/api/reference/typescript/resources/uploads/subresources/parts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Uploads](/api/reference/typescript/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Parts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/typescript/resources/uploads/subresources/parts/methods/create)

client.uploads.parts.create(stringuploadID, PartCreateParams { data } body, RequestOptionsoptions?): [UploadPart](/api/reference/typescript/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)) { id, created\_at, object, upload\_id }

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

UploadPart { id, created\_at, object, upload\_id }

The upload Part represents a chunk of bytes we can add to an Upload object.

id: string

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

object: "upload.part"

The object type, which is always `upload.part`.

upload\_id: string

The ID of the Upload object that this Part was added to.
