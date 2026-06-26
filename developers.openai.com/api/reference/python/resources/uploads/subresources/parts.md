<!-- source: https://developers.openai.com/api/reference/python/resources/uploads/subresources/parts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Uploads](/api/reference/python/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Parts

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
