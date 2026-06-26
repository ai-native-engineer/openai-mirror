<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/methods/create/ -->

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

# Create video

$ openai videos create

POST/videos

Create a new video generation job from a prompt and optional reference assets.

##### ParametersExpand Collapse

--prompt: string

Text prompt that describes the video to generate.

--input-reference: optional string or [ImageInputReferenceParam](/api/reference/cli/resources/videos#(resource)%20videos%20%3E%20(model)%20image_input_reference_param%20%3E%20(schema)) { file\_id, image\_url }

Optional reference asset upload or reference object that guides generation.

--model: optional string or "sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

--seconds: optional "4" or "8" or "12"

Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

--size: optional "720x1280" or "1280x720" or "1024x1792" or "1792x1024"

Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

##### ReturnsExpand Collapse

video: object { id, completed\_at, created\_at, 10 more }

Structured information describing a generated video job.

id: string

Unique identifier for the video job.

completed\_at: number

Unix timestamp (seconds) for when the job completed, if finished.

created\_at: number

Unix timestamp (seconds) for when the job was created.

error: object { code, message }

Error payload that explains why generation failed, if applicable.

code: string

A machine-readable error code that was returned.

message: string

A human-readable description of the error that was returned.

expires\_at: number

Unix timestamp (seconds) for when the downloadable assets expire, if set.

model: string or "sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

The video generation model that produced the job.

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

seconds: string or [VideoSeconds](/api/reference/cli/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

"4"

"8"

"12"

size: "720x1280" or "1280x720" or "1024x1792" or "1792x1024"

The resolution of the generated video.

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

status: "queued" or "in\_progress" or "completed" or "failed"

Current lifecycle status of the video job.

"queued"

"in\_progress"

"completed"

"failed"

### Create video

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai videos create \
  --api-key 'My API Key' \
  --prompt x

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
