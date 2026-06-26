<!-- source: https://developers.openai.com/api/reference/cli/resources/uploads/subresources/parts/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Uploads](/api/reference/cli/resources/uploads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Parts

Use Uploads to upload large files in multiple parts.

##### [Add upload part](/api/reference/cli/resources/uploads/subresources/parts/methods/create)

$ openai uploads:parts create

POST/uploads/{upload\_id}/parts

##### ModelsExpand Collapse

upload\_part: object { id, created\_at, object, upload\_id }

The upload Part represents a chunk of bytes we can add to an Upload object.

id: string

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the Part was created.

object: "upload.part"

The object type, which is always `upload.part`.

upload\_id: string

The ID of the Upload object that this Part was added to.
