<!-- source: https://developers.openai.com/api/reference/go/resources/videos/methods/list/ -->

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

# List videos

client.Videos.List(ctx, query) (\*ConversationCursorPage[[Video](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema))], error)

GET/videos

List recently generated videos for the current project.

##### ParametersExpand Collapse

query VideoListParams

After param.Field[string]Optional

Identifier for the last item from the previous pagination request

Limit param.Field[int64]Optional

Number of items to retrieve

minimum0

maximum100

Order param.Field[[VideoListParamsOrder](/api/reference/go/resources/videos/methods/list#(resource)%20videos%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

const VideoListParamsOrderAsc [VideoListParamsOrder](/api/reference/go/resources/videos/methods/list#(resource)%20videos%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const VideoListParamsOrderDesc [VideoListParamsOrder](/api/reference/go/resources/videos/methods/list#(resource)%20videos%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

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

### List videos

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
  page, err := client.Videos.List(context.TODO(), openai.VideoListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
