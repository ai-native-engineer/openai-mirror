<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Videos](/api/reference/cli/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete video

$ openai videos delete

DELETE/videos/{video\_id}

Permanently delete a completed or failed video and its stored assets.

##### ParametersExpand Collapse

--video-id: string

The identifier of the video to delete.

##### ReturnsExpand Collapse

VideoDeleteResponse: object { id, deleted, object }

Confirmation payload returned after deleting a video.

id: string

Identifier of the deleted video.

deleted: boolean

Indicates that the video resource was deleted.

object: "video.deleted"

The object type that signals the deletion response.

### Delete video

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai videos delete \
  --api-key 'My API Key' \
  --video-id video_123

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"
