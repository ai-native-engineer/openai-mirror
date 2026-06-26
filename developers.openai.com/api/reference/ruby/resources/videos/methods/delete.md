<!-- source: https://developers.openai.com/api/reference/ruby/resources/videos/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Videos](/api/reference/ruby/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete video

videos.delete(video\_id) -> [VideoDeleteResponse](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/videos/{video\_id}

Permanently delete a completed or failed video and its stored assets.

##### ParametersExpand Collapse

video\_id: String

##### ReturnsExpand Collapse

class VideoDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a video.

id: String

Identifier of the deleted video.

deleted: bool

Indicates that the video resource was deleted.

object: :"video.deleted"

The object type that signals the deletion response.

### Delete video

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new

video = openai.videos.delete("video_123")

puts(video)

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"
