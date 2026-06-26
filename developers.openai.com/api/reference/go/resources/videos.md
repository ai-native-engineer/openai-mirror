<!-- source: https://developers.openai.com/api/reference/go/resources/videos/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Videos

##### [Create video](/api/reference/go/resources/videos/methods/create)

client.Videos.New(ctx, body) (\*[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)), error)

POST/videos

##### [Create a new video generation job by editing a source video or existing generated video.](/api/reference/go/resources/videos/methods/edit)

client.Videos.Edit(ctx, body) (\*[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)), error)

POST/videos/edits

##### [Create an extension of a completed video.](/api/reference/go/resources/videos/methods/extend)

client.Videos.Extend(ctx, body) (\*[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)), error)

POST/videos/extensions

##### [Create a character from an uploaded video.](/api/reference/go/resources/videos/methods/create_character)

client.Videos.NewCharacter(ctx, body) (\*[VideoNewCharacterResponse](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoNewCharacterResponse%20%3E%20(schema)), error)

POST/videos/characters

##### [Fetch a character.](/api/reference/go/resources/videos/methods/get_character)

client.Videos.GetCharacter(ctx, characterID) (\*[VideoGetCharacterResponse](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoGetCharacterResponse%20%3E%20(schema)), error)

GET/videos/characters/{character\_id}

##### [List videos](/api/reference/go/resources/videos/methods/list)

client.Videos.List(ctx, query) (\*ConversationCursorPage[[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))], error)

GET/videos

##### [Retrieve video](/api/reference/go/resources/videos/methods/retrieve)

client.Videos.Get(ctx, videoID) (\*[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)), error)

GET/videos/{video\_id}

##### [Delete video](/api/reference/go/resources/videos/methods/delete)

client.Videos.Delete(ctx, videoID) (\*[VideoDeleteResponse](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoDeleteResponse%20%3E%20(schema)), error)

DELETE/videos/{video\_id}

##### [Remix video](/api/reference/go/resources/videos/methods/remix)

client.Videos.Remix(ctx, videoID, body) (\*[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)), error)

POST/videos/{video\_id}/remix

##### [Retrieve video content](/api/reference/go/resources/videos/methods/download_content)

client.Videos.DownloadContent(ctx, videoID, query) (\*Response, error)

GET/videos/{video\_id}/content

##### ModelsExpand Collapse

type ImageInputReferenceParamResp struct{…}

FileID stringOptional

ImageURL stringOptional

A fully qualified URL or base64-encoded data URL.

maxLength20971520

formaturi

type Video struct{…}

Structured information describing a generated video job.

ID string

Unique identifier for the video job.

CompletedAt int64

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

CreatedAt int64

Unix timestamp (seconds) for when the job was created.

formatunixtime

Error [VideoCreateError](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema))

Error payload that explains why generation failed, if applicable.

ExpiresAt int64

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

Model VideoModel

The video generation model that produced the job.

Object Video

The object type, which is always `video`.

Progress int64

Approximate completion percentage for the generation task.

Prompt string

The prompt that was used to generate the video.

RemixedFromVideoID string

Identifier of the source video if this video is a remix.

Seconds [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema))

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

One of the following:

string

type VideoSeconds string

One of the following:

const VideoSeconds4 [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) = "4"

const VideoSeconds8 [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) = "8"

const VideoSeconds12 [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) = "12"

Size [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema))

The resolution of the generated video.

Status VideoStatus

Current lifecycle status of the video job.

One of the following:

const VideoStatusQueued VideoStatus = "queued"

const VideoStatusInProgress VideoStatus = "in\_progress"

const VideoStatusCompleted VideoStatus = "completed"

const VideoStatusFailed VideoStatus = "failed"

type VideoCreateError struct{…}

An error that occurred while generating the response.

Code string

A machine-readable error code that was returned.

Message string

A human-readable description of the error that was returned.

type VideoModel interface{…}

One of the following:

string

type VideoModel string

One of the following:

const VideoModelSora2 VideoModel = "sora-2"

const VideoModelSora2Pro VideoModel = "sora-2-pro"

const VideoModelSora2\_2025\_10\_06 VideoModel = "sora-2-2025-10-06"

const VideoModelSora2Pro2025\_10\_06 VideoModel = "sora-2-pro-2025-10-06"

const VideoModelSora2\_2025\_12\_08 VideoModel = "sora-2-2025-12-08"

type VideoSeconds string

One of the following:

const VideoSeconds4 [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) = "4"

const VideoSeconds8 [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) = "8"

const VideoSeconds12 [VideoSeconds](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) = "12"

type VideoSize string

One of the following:

const VideoSize720x1280 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "720x1280"

const VideoSize1280x720 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "1280x720"

const VideoSize1024x1792 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "1024x1792"

const VideoSize1792x1024 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "1792x1024"
