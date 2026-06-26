<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/remix/ -->

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

# Remix video

videos.remix(strvideo\_id, VideoRemixParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos/{video\_id}/remix

Create a remix of a completed video using a refreshed prompt.

##### ParametersExpand Collapse

video\_id: str

prompt: str

Updated text prompt that directs the remix generation.

maxLength32000

minLength1

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

### Remix video

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
video = client.videos.remix(
    video_id="video_123",
    prompt="Extend the scene with the cat taking a bow to the cheering audience",
print(video.id)

  "id": "video_456",
  "object": "video",
  "model": "sora-2",
  "status": "queued",
  "progress": 0,
  "created_at": 1712698600,
  "size": "720x1280",
  "seconds": "8",
  "remixed_from_video_id": "video_123"

##### Returns Examples

  "id": "video_456",
  "object": "video",
  "model": "sora-2",
  "status": "queued",
  "progress": 0,
  "created_at": 1712698600,
  "size": "720x1280",
  "seconds": "8",
  "remixed_from_video_id": "video_123"
