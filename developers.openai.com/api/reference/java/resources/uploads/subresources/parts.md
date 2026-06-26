<!-- source: https://developers.openai.com/api/reference/java/resources/uploads/subresources/parts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Uploads](/api/reference/java/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Parts

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
