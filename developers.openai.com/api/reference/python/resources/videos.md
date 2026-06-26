<!-- source: https://developers.openai.com/api/reference/python/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/python/resources/videos/methods/create)

videos.create(VideoCreateParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/python/resources/videos/methods/edit)

videos.edit(VideoEditParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/python/resources/videos/methods/extend)

videos.extend(VideoExtendParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/python/resources/videos/methods/create_character)

videos.create\_character(VideoCreateCharacterParams\*\*kwargs)  -> [VideoCreateCharacterResponse](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema))

POST/videos/characters

##### [Fetch a character.](/api/reference/python/resources/videos/methods/get_character)

videos.get\_character(strcharacter\_id)  -> [VideoGetCharacterResponse](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema))

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/python/resources/videos/methods/list)

videos.list(VideoListParams\*\*kwargs)  -> SyncConversationCursorPage[[Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))]

GET/videos

##### [Retrieve video](/api/reference/python/resources/videos/methods/retrieve)

videos.retrieve(strvideo\_id)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

GET/videos/{video\_id}

##### [Delete video](/api/reference/python/resources/videos/methods/delete)

videos.delete(strvideo\_id)  -> [VideoDeleteResponse](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema))

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/python/resources/videos/methods/remix)

videos.remix(strvideo\_id, VideoRemixParams\*\*kwargs)  -> [Video](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/python/resources/videos/methods/download_content)

videos.download\_content(strvideo\_id, VideoDownloadContentParams\*\*kwargs)  -> BinaryResponseContent

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

class ImageInputReferenceParam: …

file\_id: Optional[str]

image\_url: Optional[str]

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

class Video: …

Structured information describing a generated video job.

id: str

Unique identifier for the video job.

completed\_at: Optional[int]

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

created\_at: int

Unix timestamp (seconds) for when the job was created.

formatunixtime

error: Optional[VideoCreateError]

Error payload that explains why generation failed, if applicable.

expires\_at: Optional[int]

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

object: Literal["video"]

The object type, which is always `video`.

progress: int

Approximate completion percentage for the generation task.

prompt: Optional[str]

The prompt that was used to generate the video.

remixed\_from\_video\_id: Optional[str]

Identifier of the source video if this video is a remix.

seconds: Union[str, [VideoSeconds](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))]

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

One of the following:

str

Literal["4", "8", "12"]

One of the following:

"4"

"8"

"12"

size: [VideoSize](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

status: Literal["queued", "in\_progress", "completed", "failed"]

Current lifecycle status of the video job.

One of the following:

"queued"

"in\_progress"

"completed"

"failed"

class VideoCreateError: …

An error that occurred while generating the response.

code: str

A machine-readable error code that was returned.

message: str

A human-readable description of the error that was returned.

Union[str, Literal["sora-2", "sora-2-pro", "sora-2-2025-10-06", 2 more]]

One of the following:

str

Literal["sora-2", "sora-2-pro", "sora-2-2025-10-06", 2 more]

One of the following:

"sora-2"

"sora-2-pro"

"sora-2-2025-10-06"

"sora-2-pro-2025-10-06"

"sora-2-2025-12-08"

Literal["4", "8", "12"]

One of the following:

"4"

"8"

"12"

Literal["720x1280", "1280x720", "1024x1792", "1792x1024"]

One of the following:

"720x1280"

"1280x720"

"1024x1792"

"1792x1024"

class VideoCreateCharacterResponse: …

id: Optional[str]

Identifier for the character creation cameo.

created\_at: int

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: Optional[str]

Display name for the character.

class VideoGetCharacterResponse: …

id: Optional[str]

Identifier for the character creation cameo.

created\_at: int

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: Optional[str]

Display name for the character.

class VideoDeleteResponse: …

Confirmation payload returned after deleting a video.

id: str

Identifier of the deleted video.

deleted: bool

Indicates that the video resource was deleted.

object: Literal["video.deleted"]

The object type that signals the deletion response.
