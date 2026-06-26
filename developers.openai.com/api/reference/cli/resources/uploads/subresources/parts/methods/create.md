<!-- source: https://developers.openai.com/api/reference/cli/resources/uploads/subresources/parts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Uploads](/api/reference/cli/resources/uploads)

[Parts](/api/reference/cli/resources/uploads/subresources/parts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add upload part

$ openai uploads:parts create

POST/uploads/{upload\_id}/parts

Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

##### ParametersExpand Collapse

--upload-id: string

The ID of the Upload.

--data: file path

The chunk of bytes for this Part.

##### ReturnsExpand Collapse

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

### Add upload part

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai uploads:parts create \
  --api-key 'My API Key' \
  --upload-id upload_abc123 \
  --data 'Example data'

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"

##### Returns Examples

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"
