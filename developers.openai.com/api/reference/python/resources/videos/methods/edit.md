<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/edit/ -->

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

# Create a new video generation job by editing a source video or existing generated video.

videos.edit(VideoEditParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos/edits

Create a new video generation job by editing a source video or existing generated video.

##### ParametersExpand Collapse

prompt: str

Text prompt that describes how to edit the source video.

maxLength32000

minLength1

video: [Video](/api/reference/python/resources/videos/methods/edit#(resource)%20videos%20%3E%20(method)%20edit%20%3E%20(params)%20default%20%3E%20(param)%20video%20%3E%20(schema))

Reference to the completed video to edit.

One of the following:

FileTypes

Reference to the completed video to edit.

class VideoVideoReferenceInputParam: …

Reference to the completed video to edit.

id: str

The identifier of the completed video.

##### ReturnsExpand Collapse

class Video: …

Structured information describing a generated video job.

id: str

Unique identifier for the video job.

completed\_at: Optional[int]

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

created\_at: int

Unix timestamp (seconds) for when the job was created.

formatunixtime

error: Optional[VideoCreateError]

Error payload that explains why generation failed, if applicable.

code: str

A machine-readable error code that was returned.

message: str

A human-readable description of the error that was returned.

expires\_at: Optional[int]

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

One of the following:

str

Literal["sora-2", "sora-2-pro", "sora-2-2025-10-06", 2 more]

One of the following:

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

object: Literal["video"]

The object type, which is always `video`.

progress: int

Approximate completion percentage for the generation task.

prompt: Optional[str]

The prompt that was used to generate the video.

remixed\_from\_video\_id: Optional[str]

Identifier of the source video if this video is a remix.

seconds: Union[str, [VideoSeconds](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))]

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

One of the following:

str

Literal["4", "8", "12"]

One of the following:

"4"

"8"

"12"

size: [VideoSize](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

status: Literal["queued", "in\_progress", "completed", "failed"]

Current lifecycle status of the video job.

One of the following:

"queued"

"in\_progress"

"completed"

"failed"

### Create a new video generation job by editing a source video or existing generated video.

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
video = client.videos.edit(
    prompt="x",
    video=b"Example data",
print(video.id)

200 example

  "id": "id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  "expires_at": 0,
  "model": "sora-2",
  "object": "video",
  "progress": 0,
  "prompt": "prompt",
  "remixed_from_video_id": "remixed_from_video_id",
  "seconds": "4",
  "size": "720x1280",
  "status": "queued"

##### Returns Examples

200 example

  "id": "id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  "expires_at": 0,
  "model": "sora-2",
  "object": "video",
  "progress": 0,
  "prompt": "prompt",
  "remixed_from_video_id": "remixed_from_video_id",
  "seconds": "4",
  "size": "720x1280",
  "status": "queued"
