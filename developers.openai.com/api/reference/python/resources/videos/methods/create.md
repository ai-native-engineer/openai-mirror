<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/create/ -->

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

# Create video

videos.create(VideoCreateParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos

Create a new video generation job from a prompt and optional reference assets.

##### ParametersExpand Collapse

prompt: str

Text prompt that describes the video to generate.

maxLength32000

minLength1

input\_reference: Optional[[InputReference](/api/reference/python/resources/videos/methods/create#(resource)%20videos%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20input_reference%20%3E%20(schema))]

Optional reference asset upload or reference object that guides generation.

One of the following:

FileTypes

Optional reference asset upload or reference object that guides generation.

class ImageInputReferenceParam: …

file\_id: Optional[str]

image\_url: Optional[str]

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

model: Optional[[VideoModelParam](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))]

The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

One of the following:

str

Literal["sora-2", "sora-2-pro", "sora-2-2025-10-06", 2 more]

One of the following:

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

seconds: Optional[[VideoSeconds](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))]

Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

One of the following:

"4"

"8"

"12"

size: Optional[[VideoSize](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))]

Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

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

### Create video

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
video = client.videos.create(
    prompt="A calico cat playing a piano on stage",
print(video.id)

  "id": "video_123",
  "object": "video",
  "model": "sora-2",
  "status": "queued",
  "progress": 0,
  "created_at": 1712697600,
  "size": "1024x1792",
  "seconds": "8",
  "quality": "standard"

##### Returns Examples

  "id": "video_123",
  "object": "video",
  "model": "sora-2",
  "status": "queued",
  "progress": 0,
  "created_at": 1712697600,
  "size": "1024x1792",
  "seconds": "8",
  "quality": "standard"
