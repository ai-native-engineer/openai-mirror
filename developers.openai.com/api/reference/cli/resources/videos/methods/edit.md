<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/methods/edit/ -->

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

# Create a new video generation job by editing a source video or existing generated video.

$ openai videos edit

POST/videos/edits

Create a new video generation job by editing a source video or existing generated video.

##### ParametersExpand Collapse

--prompt: string

Text prompt that describes how to edit the source video.

--video: string or object { id }

Reference to the completed video to edit.

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

### Create a new video generation job by editing a source video or existing generated video.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai videos edit \
  --api-key 'My API Key' \
  --prompt x \
  --video 'Example data'

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
