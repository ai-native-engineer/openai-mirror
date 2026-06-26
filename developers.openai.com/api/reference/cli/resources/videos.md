<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/cli/resources/videos/methods/create)

$ openai videos create

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/cli/resources/videos/methods/edit)

$ openai videos edit

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/cli/resources/videos/methods/extend)

$ openai videos extend

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/cli/resources/videos/methods/create_character)

$ openai videos create-character

POST/videos/characters

##### [Fetch a character.](/api/reference/cli/resources/videos/methods/get_character)

$ openai videos get-character

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/cli/resources/videos/methods/list)

$ openai videos list

GET/videos

##### [Retrieve video](/api/reference/cli/resources/videos/methods/retrieve)

$ openai videos retrieve

GET/videos/{video\_id}

##### [Delete video](/api/reference/cli/resources/videos/methods/delete)

$ openai videos delete

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/cli/resources/videos/methods/remix)

$ openai videos remix

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/cli/resources/videos/methods/download_content)

$ openai videos download-content

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

image\_input\_reference\_param: object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

A fully qualified URL or base64-encoded data URL.

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

video\_create\_error: object { code, message }

An error that occurred while generating the response.

code: string

A machine-readable error code that was returned.

message: string

A human-readable description of the error that was returned.

video\_seconds: "4" or "8" or "12"

"4"

"8"

"12"

video\_size: "720x1280" or "1280x720" or "1024x1792" or "1792x1024"

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"
