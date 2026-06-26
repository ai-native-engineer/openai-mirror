<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/methods/remix/ -->

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

# Remix video

client.videos.remix(stringvideoID, VideoRemixParams { prompt } body, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/{video\_id}/remix

Create a remix of a completed video using a refreshed prompt.

##### ParametersExpand Collapse

videoID: string

body: VideoRemixParams { prompt }

prompt: string

Updated text prompt that directs the remix generation.

maxLength32000

minLength1

##### ReturnsExpand Collapse

Video { id, completed\_at, created\_at, 10 more }

Structured information describing a generated video job.

id: string

Unique identifier for the video job.

completed\_at: number | null

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

created\_at: number

Unix timestamp (seconds) for when the job was created.

formatunixtime

error: [VideoCreateError](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)) { code, message }  | null

Error payload that explains why generation failed, if applicable.

code: string

A machine-readable error code that was returned.

message: string

A human-readable description of the error that was returned.

expires\_at: number | null

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

One of the following:

(string & {})

"sora-2" | "sora-2-pro" | "sora-2-2025-10-06" | 2 more

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

object: "video"

The object type, which is always `video`.

progress: number

Approximate completion percentage for the generation task.

prompt: string | null

The prompt that was used to generate the video.

remixed\_from\_video\_id: string | null

Identifier of the source video if this video is a remix.

seconds: (string & {}) | [VideoSeconds](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

One of the following:

(string & {})

VideoSeconds = "4" | "8" | "12"

One of the following:

"4"

"8"

"12"

size: [VideoSize](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

status: "queued" | "in\_progress" | "completed" | "failed"

Current lifecycle status of the video job.

One of the following:

"queued"

"in\_progress"

"completed"

"failed"

### Remix video

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

const video = await client.videos.remix('video_123', { prompt: 'Extend the scene with the cat taking a bow to the cheering audience' });

console.log(video.id);

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
