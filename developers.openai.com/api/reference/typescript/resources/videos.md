<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/typescript/resources/videos/methods/create)

client.videos.create(VideoCreateParams { prompt, input\_reference, model, 2 more } body, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/typescript/resources/videos/methods/edit)

client.videos.edit(VideoEditParams { prompt, video } body, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/typescript/resources/videos/methods/extend)

client.videos.extend(VideoExtendParams { prompt, seconds, video } body, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/typescript/resources/videos/methods/create_character)

client.videos.createCharacter(VideoCreateCharacterParams { name, video } body, RequestOptionsoptions?): [VideoCreateCharacterResponse](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)) { id, created\_at, name }

POST/videos/characters

##### [Fetch a character.](/api/reference/typescript/resources/videos/methods/get_character)

client.videos.getCharacter(stringcharacterID, RequestOptionsoptions?): [VideoGetCharacterResponse](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)) { id, created\_at, name }

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/typescript/resources/videos/methods/list)

client.videos.list(VideoListParams { after, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more } >

GET/videos

##### [Retrieve video](/api/reference/typescript/resources/videos/methods/retrieve)

client.videos.retrieve(stringvideoID, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

GET/videos/{video\_id}

##### [Delete video](/api/reference/typescript/resources/videos/methods/delete)

client.videos.delete(stringvideoID, RequestOptionsoptions?): [VideoDeleteResponse](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/typescript/resources/videos/methods/remix)

client.videos.remix(stringvideoID, VideoRemixParams { prompt } body, RequestOptionsoptions?): [Video](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/typescript/resources/videos/methods/download_content)

client.videos.downloadContent(stringvideoID, VideoDownloadContentParams { variant } query?, RequestOptionsoptions?): Response

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

ImageInputReferenceParam { file\_id, image\_url }

file\_id?: string

image\_url?: string

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

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

expires\_at: number | null

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

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

status: "queued" | "in\_progress" | "completed" | "failed"

Current lifecycle status of the video job.

One of the following:

"queued"

"in\_progress"

"completed"

"failed"

VideoCreateError { code, message }

An error that occurred while generating the response.

code: string

A machine-readable error code that was returned.

message: string

A human-readable description of the error that was returned.

VideoModel = (string & {}) | "sora-2" | "sora-2-pro" | "sora-2-2025-10-06" | 2 more

One of the following:

(string & {})

"sora-2" | "sora-2-pro" | "sora-2-2025-10-06" | 2 more

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

VideoSeconds = "4" | "8" | "12"

One of the following:

"4"

"8"

"12"

VideoSize = "720x1280" | "1280x720" | "1024x1792" | "1792x1024"

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

VideoCreateCharacterResponse { id, created\_at, name }

id: string | null

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string | null

Display name for the character.

VideoGetCharacterResponse { id, created\_at, name }

id: string | null

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string | null

Display name for the character.

VideoDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a video.

id: string

Identifier of the deleted video.

deleted: boolean

Indicates that the video resource was deleted.

object: "video.deleted"

The object type that signals the deletion response.
