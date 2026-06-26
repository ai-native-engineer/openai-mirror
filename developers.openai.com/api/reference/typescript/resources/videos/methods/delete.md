<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Videos](/api/reference/typescript/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete video

client.videos.delete(stringvideoID, RequestOptionsoptions?): [VideoDeleteResponse](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/videos/{video\_id}

Permanently delete a completed or failed video and its stored assets.

##### ParametersExpand Collapse

videoID: string

##### ReturnsExpand Collapse

VideoDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a video.

id: string

Identifier of the deleted video.

deleted: boolean

Indicates that the video resource was deleted.

object: "video.deleted"

The object type that signals the deletion response.

### Delete video

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI();

const video = await client.videos.delete('video_123');

console.log(video.id);

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"
