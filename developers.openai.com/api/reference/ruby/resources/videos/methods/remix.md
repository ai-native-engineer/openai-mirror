<!-- source: https://developers.openai.com/api/reference/ruby/resources/videos/methods/remix/ -->

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

# Remix video

videos.remix(video\_id, \*\*kwargs) -> [Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/{video\_id}/remix

Create a remix of a completed video using a refreshed prompt.

##### ParametersExpand Collapse

video\_id: String

prompt: String

Updated text prompt that directs the remix generation.

maxLength32000

minLength1

##### ReturnsExpand Collapse

class Video { id, completed\_at, created\_at, 10 more }

Structured information describing a generated video job.

id: String

Unique identifier for the video job.

completed\_at: Integer

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

created\_at: Integer

Unix timestamp (seconds) for when the job was created.

formatunixtime

error: [VideoCreateError](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema)) { code, message }

Error payload that explains why generation failed, if applicable.

code: String

A machine-readable error code that was returned.

message: String

A human-readable description of the error that was returned.

expires\_at: Integer

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

One of the following:

String = String

VideoModel = :"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more

One of the following:

:"sora-2"

:"sora-2-pro"

:"sora-2-2025-10-06"

:"sora-2-pro-2025-10-06"

:"sora-2-2025-12-08"

object: :video

The object type, which is always `video`.

progress: Integer

Approximate completion percentage for the generation task.

prompt: String

The prompt that was used to generate the video.

remixed\_from\_video\_id: String

Identifier of the source video if this video is a remix.

seconds: String | [VideoSeconds](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

One of the following:

String = String

VideoSeconds = :"4" | :"8" | :"12"

One of the following:

:"4"

:"8"

:"12"

size: [VideoSize](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

One of the following:

:"720x1280"

:"1280x720"

:"1024x1792"

:"1792x1024"

status: :queued | :in\_progress | :completed | :failed

Current lifecycle status of the video job.

One of the following:

:queued

:in\_progress

:completed

:failed

### Remix video

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

video = openai.videos.remix("video_123", prompt: "Extend the scene with the cat taking a bow to the cheering audience")

puts(video)

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
