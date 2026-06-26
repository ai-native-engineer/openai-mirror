<!-- source: https://developers.openai.com/api/reference/java/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/java/resources/videos/methods/create)

[Video](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) videos().create(VideoCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/java/resources/videos/methods/edit)

[Video](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) videos().edit(VideoEditParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/java/resources/videos/methods/extend)

[Video](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) videos().extend(VideoExtendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/java/resources/videos/methods/create_character)

[VideoCreateCharacterResponse](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoCreateCharacterResponse%20%3E%20(schema)) videos().createCharacter(VideoCreateCharacterParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos/characters

##### [Fetch a character.](/api/reference/java/resources/videos/methods/get_character)

[VideoGetCharacterResponse](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoGetCharacterResponse%20%3E%20(schema)) videos().getCharacter(VideoGetCharacterParamsparams = VideoGetCharacterParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/java/resources/videos/methods/list)

VideoListPage videos().list(VideoListParamsparams = VideoListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/videos

##### [Retrieve video](/api/reference/java/resources/videos/methods/retrieve)

[Video](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) videos().retrieve(VideoRetrieveParamsparams = VideoRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/videos/{video\_id}

##### [Delete video](/api/reference/java/resources/videos/methods/delete)

[VideoDeleteResponse](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoDeleteResponse%20%3E%20(schema)) videos().delete(VideoDeleteParamsparams = VideoDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/java/resources/videos/methods/remix)

[Video](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) videos().remix(VideoRemixParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/java/resources/videos/methods/download_content)

HttpResponse videos().downloadContent(VideoDownloadContentParamsparams = VideoDownloadContentParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

class ImageInputReferenceParam:

Optional<String> fileId

Optional<String> imageUrl

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

class Video:

Structured information describing a generated video job.

String id

Unique identifier for the video job.

Optional<Long> completedAt

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

long createdAt

Unix timestamp (seconds) for when the job was created.

formatunixtime

Optional<[VideoCreateError](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema))> error

Error payload that explains why generation failed, if applicable.

Optional<Long> expiresAt

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

VideoModel model

The video generation model that produced the job.

JsonValue; object\_ "video"constant"video"constant

The object type, which is always `video`.

long progress

Approximate completion percentage for the generation task.

Optional<String> prompt

The prompt that was used to generate the video.

Optional<String> remixedFromVideoId

Identifier of the source video if this video is a remix.

[VideoSeconds](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) seconds

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

[VideoSize](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) size

The resolution of the generated video.

Status status

Current lifecycle status of the video job.

One of the following:

QUEUED("queued")

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

FAILED("failed")

class VideoCreateError:

An error that occurred while generating the response.

String code

A machine-readable error code that was returned.

String message

A human-readable description of the error that was returned.

enum VideoModel:

SORA\_2("sora-2")

SORA\_2\_PRO("sora-2-pro")

SORA\_2\_2025\_10\_06("sora-2-2025-10-06")

SORA\_2\_PRO\_2025\_10\_06("sora-2-pro-2025-10-06")

SORA\_2\_2025\_12\_08("sora-2-2025-12-08")

enum VideoSeconds:

\_4("4")

\_8("8")

\_12("12")

enum VideoSize:

\_720X1280("720x1280")

\_1280X720("1280x720")

\_1024X1792("1024x1792")

\_1792X1024("1792x1024")
