<!-- source: https://developers.openai.com/api/reference/resources/videos/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Videos](/api/reference/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create video

POST/videos

Create a new video generation job from a prompt and optional reference assets.

##### Body ParametersJSONExpand Collapse

prompt: string

Text prompt that describes the video to generate.

maxLength32000

minLength1

input\_reference: optional [ImageInputReferenceParam](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)) { file\_id, image\_url }

Optional reference object that guides generation. Provide exactly one of `image_url` or `file_id`.

file\_id: optional string

image\_url: optional string

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

model: optional [VideoModel](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

One of the following:

string

"sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

seconds: optional [VideoSeconds](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

One of the following:

"4"

"8"

"12"

size: optional [VideoSize](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

##### ReturnsExpand Collapse

Video object { id, completed\_at, created\_at, 10 more }

Structured information describing a generated video job.

id: string

Unique identifier for the video job.

completed\_at: number

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

created\_at: number

Unix timestamp (seconds) for when the job was created.

formatunixtime

error: [VideoCreateError](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)) { code, message }

Error payload that explains why generation failed, if applicable.

code: string

A machine-readable error code that was returned.

message: string

A human-readable description of the error that was returned.

expires\_at: number

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

One of the following:

string

"sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

object: "video"

The object type, which is always `video`.

progress: number

Approximate completion percentage for the generation task.

prompt: string

The prompt that was used to generate the video.

remixed\_from\_video\_id: string

Identifier of the source video if this video is a remix.

seconds: string

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

size: [VideoSize](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

status: "queued" or "in\_progress" or "completed" or "failed"

Current lifecycle status of the video job.

One of the following:

"queued"

"in\_progress"

"completed"

"failed"

### Create video

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/videos \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "model=sora-2" \
  -F "prompt=A calico cat playing a piano on stage"

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
