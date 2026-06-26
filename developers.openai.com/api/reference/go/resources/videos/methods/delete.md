<!-- source: https://developers.openai.com/api/reference/go/resources/videos/methods/delete/ -->

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

# Delete video

client.Videos.Delete(ctx, videoID) (\*[VideoDeleteResponse](/api/reference/go/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoDeleteResponse%20%3E%20(schema)), error)

DELETE/videos/{video\_id}

Permanently delete a completed or failed video and its stored assets.

##### ParametersExpand Collapse

videoID string

##### ReturnsExpand Collapse

type VideoDeleteResponse struct{…}

Confirmation payload returned after deleting a video.

ID string

Identifier of the deleted video.

Deleted bool

Indicates that the video resource was deleted.

Object VideoDeleted

The object type that signals the deletion response.

### Delete video

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
  video, err := client.Videos.Delete(context.TODO(), "video_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", video.ID)

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"
