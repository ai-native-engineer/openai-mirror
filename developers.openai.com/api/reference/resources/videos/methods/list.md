<!-- source: https://developers.openai.com/api/reference/resources/videos/methods/list/ -->

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

# List videos

GET/videos

List recently generated videos for the current project.

##### Query ParametersExpand Collapse

after: optional string

Identifier for the last item from the previous pagination request

limit: optional number

Number of items to retrieve

minimum0

maximum100

order: optional "asc" or "desc"

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

data: array of [Video](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

A list of items

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

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

### List videos

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
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "data": [
      "id": "video_123",
      "object": "video",
      "model": "sora-2",
      "status": "completed"
  ],
  "object": "list"

##### Returns Examples

  "data": [
      "id": "video_123",
      "object": "video",
      "model": "sora-2",
      "status": "completed"
  ],
  "object": "list"
