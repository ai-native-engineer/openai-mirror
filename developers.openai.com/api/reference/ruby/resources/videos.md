<!-- source: https://developers.openai.com/api/reference/ruby/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/ruby/resources/videos/methods/create)

videos.create(\*\*kwargs) -> [Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/ruby/resources/videos/methods/edit)

videos.edit(\*\*kwargs) -> [Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/ruby/resources/videos/methods/extend)

videos.extend\_(\*\*kwargs) -> [Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/ruby/resources/videos/methods/create_character)

videos.create\_character(\*\*kwargs) -> [VideoCreateCharacterResponse](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)) { id, created\_at, name }

POST/videos/characters

##### [Fetch a character.](/api/reference/ruby/resources/videos/methods/get_character)

videos.get\_character(character\_id) -> [VideoGetCharacterResponse](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)) { id, created\_at, name }

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/ruby/resources/videos/methods/list)

videos.list(\*\*kwargs) -> ConversationCursorPage<[Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more } >

GET/videos

##### [Retrieve video](/api/reference/ruby/resources/videos/methods/retrieve)

videos.retrieve(video\_id) -> [Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

GET/videos/{video\_id}

##### [Delete video](/api/reference/ruby/resources/videos/methods/delete)

videos.delete(video\_id) -> [VideoDeleteResponse](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/ruby/resources/videos/methods/remix)

videos.remix(video\_id, \*\*kwargs) -> [Video](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) { id, completed\_at, created\_at, 10 more }

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/ruby/resources/videos/methods/download_content)

videos.download\_content(video\_id, \*\*kwargs) -> StringIO

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

class ImageInputReferenceParam { file\_id, image\_url }

file\_id: String

image\_url: String

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

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

expires\_at: Integer

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

model: [VideoModel](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_model%20%3E%20(schema))

The video generation model that produced the job.

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

status: :queued | :in\_progress | :completed | :failed

Current lifecycle status of the video job.

One of the following:

:queued

:in\_progress

:completed

:failed

class VideoCreateError { code, message }

An error that occurred while generating the response.

code: String

A machine-readable error code that was returned.

message: String

A human-readable description of the error that was returned.

VideoModel = String | :"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more

One of the following:

String = String

VideoModel = :"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more

One of the following:

:"sora-2"

:"sora-2-pro"

:"sora-2-2025-10-06"

:"sora-2-pro-2025-10-06"

:"sora-2-2025-12-08"

VideoSeconds = :"4" | :"8" | :"12"

One of the following:

:"4"

:"8"

:"12"

VideoSize = :"720x1280" | :"1280x720" | :"1024x1792" | :"1792x1024"

One of the following:

:"720x1280"

:"1280x720"

:"1024x1792"

:"1792x1024"

class VideoCreateCharacterResponse { id, created\_at, name }

id: String

Identifier for the character creation cameo.

created\_at: Integer

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: String

Display name for the character.

class VideoGetCharacterResponse { id, created\_at, name }

id: String

Identifier for the character creation cameo.

created\_at: Integer

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: String

Display name for the character.

class VideoDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a video.

id: String

Identifier of the deleted video.

deleted: bool

Indicates that the video resource was deleted.

object: :"video.deleted"

The object type that signals the deletion response.
