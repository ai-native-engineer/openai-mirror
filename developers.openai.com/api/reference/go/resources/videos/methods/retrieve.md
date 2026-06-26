<!-- source: https://developers.openai.com/api/reference/go/resources/videos/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Videos](/api/reference/go/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video

client.Videos.Get(ctx, videoID) (\*[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)), error)

GET/videos/{video\_id}

Fetch the latest metadata for a generated video.

##### ParametersExpand Collapse

videoID string

##### ReturnsExpand Collapse

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

Code string

A machine-readable error code that was returned.

Message string

A human-readable description of the error that was returned.

ExpiresAt int64

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

Model VideoModel

The video generation model that produced the job.

One of the following:

string

type VideoModel string

One of the following:

const VideoModelSora2 VideoModel = "sora-2"

const VideoModelSora2Pro VideoModel = "sora-2-pro"

const VideoModelSora2\_2025\_10\_06 VideoModel = "sora-2-2025-10-06"

const VideoModelSora2Pro2025\_10\_06 VideoModel = "sora-2-pro-2025-10-06"

const VideoModelSora2\_2025\_12\_08 VideoModel = "sora-2-2025-12-08"

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

One of the following:

const VideoSize720x1280 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "720x1280"

const VideoSize1280x720 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "1280x720"

const VideoSize1024x1792 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "1024x1792"

const VideoSize1792x1024 [VideoSize](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) = "1792x1024"

Status VideoStatus

Current lifecycle status of the video job.

One of the following:

const VideoStatusQueued VideoStatus = "queued"

const VideoStatusInProgress VideoStatus = "in\_progress"

const VideoStatusCompleted VideoStatus = "completed"

const VideoStatusFailed VideoStatus = "failed"

### Retrieve video

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"

func main() {
  client := openai.NewClient()
  video, err := client.Videos.Get(context.TODO(), "video_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", video.ID)

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
