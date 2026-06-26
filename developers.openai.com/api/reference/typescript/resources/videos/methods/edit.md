<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/methods/edit/ -->

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

# Create a new video generation job by editing a source video or existing generated video.

client.videos.edit(VideoEditParams { prompt, video } body, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/edits

Create a new video generation job by editing a source video or existing generated video.

##### ParametersExpand Collapse

body: VideoEditParams { prompt, video }

prompt: string

Text prompt that describes how to edit the source video.

maxLength32000

minLength1

video: Uploadable | VideoReferenceInputParam { id }

Reference to the completed video to edit.

One of the following:

Uploadable

VideoReferenceInputParam { id }

Reference to the completed video to edit.

id: string

The identifier of the completed video.

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

### Create a new video generation job by editing a source video or existing generated video.

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

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const video = await client.videos.edit({ prompt: 'x', video: fs.createReadStream('path/to/file') });

console.log(video.id);

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
