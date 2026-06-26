<!-- source: https://developers.openai.com/api/reference/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/resources/videos/methods/create)

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/resources/videos/methods/edit)

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/resources/videos/methods/extend)

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/resources/videos/methods/create_character)

POST/videos/characters

##### [Fetch a character.](/api/reference/resources/videos/methods/get_character)

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/resources/videos/methods/list)

GET/videos

##### [Retrieve video](/api/reference/resources/videos/methods/retrieve)

GET/videos/{video\_id}

##### [Delete video](/api/reference/resources/videos/methods/delete)

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/resources/videos/methods/remix)

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/resources/videos/methods/download_content)

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

ImageInputReferenceParam object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

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

expires\_at: number

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

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

status: "queued" or "in\_progress" or "completed" or "failed"

Current lifecycle status of the video job.

One of the following:

"queued"

"in\_progress"

"completed"

"failed"

VideoCreateError object { code, message }

An error that occurred while generating the response.

code: string

A machine-readable error code that was returned.

message: string

A human-readable description of the error that was returned.

VideoModel = string or "sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

string

"sora-2" or "sora-2-pro" or "sora-2-2025-10-06" or 2 more

One of the following:

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

VideoSeconds = "4" or "8" or "12"

One of the following:

"4"

"8"

"12"

VideoSize = "720x1280" or "1280x720" or "1024x1792" or "1792x1024"

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

VideoCreateCharacterResponse object { id, created\_at, name }

id: string

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string

Display name for the character.

VideoGetCharacterResponse object { id, created\_at, name }

id: string

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string

Display name for the character.

VideoDeleteResponse object { id, deleted, object }

Confirmation payload returned after deleting a video.

id: string

Identifier of the deleted video.

deleted: boolean

Indicates that the video resource was deleted.

object: "video.deleted"

The object type that signals the deletion response.
