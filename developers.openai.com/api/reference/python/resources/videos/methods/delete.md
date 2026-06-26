<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Videos](/api/reference/python/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete video

videos.delete(strvideo\_id)  -> [VideoDeleteResponse](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema))

DELETE/videos/{video\_id}

Permanently delete a completed or failed video and its stored assets.

##### ParametersExpand Collapse

video\_id: str

##### ReturnsExpand Collapse

class VideoDeleteResponse: …

Confirmation payload returned after deleting a video.

id: str

Identifier of the deleted video.

deleted: bool

Indicates that the video resource was deleted.

object: Literal["video.deleted"]

The object type that signals the deletion response.

### Delete video

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI

client = OpenAI()
video = client.videos.delete(
    "video_123",
print(video.id)

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"
