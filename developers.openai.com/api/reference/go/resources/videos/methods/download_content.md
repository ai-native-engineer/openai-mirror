<!-- source: https://developers.openai.com/api/reference/go/resources/videos/methods/download_content/ -->

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

# Retrieve video content

client.Videos.DownloadContent(ctx, videoID, query) (\*Response, error)

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### ParametersExpand Collapse

videoID string

query VideoDownloadContentParams

Variant param.Field[[VideoDownloadContentParamsVariant](/api/reference/go/resources/videos/methods/download_content#(resource)%20videos%20%3E%20(method)%20download_content%20%3E%20(params)%20default%20%3E%20(param)%20variant%20%3E%20(schema))]Optional

Which downloadable asset to return. Defaults to the MP4 video.

const VideoDownloadContentParamsVariantVideo [VideoDownloadContentParamsVariant](/api/reference/go/resources/videos/methods/download_content#(resource)%20videos%20%3E%20(method)%20download_content%20%3E%20(params)%20default%20%3E%20(param)%20variant%20%3E%20(schema)) = "video"

const VideoDownloadContentParamsVariantThumbnail [VideoDownloadContentParamsVariant](/api/reference/go/resources/videos/methods/download_content#(resource)%20videos%20%3E%20(method)%20download_content%20%3E%20(params)%20default%20%3E%20(param)%20variant%20%3E%20(schema)) = "thumbnail"

const VideoDownloadContentParamsVariantSpritesheet [VideoDownloadContentParamsVariant](/api/reference/go/resources/videos/methods/download_content#(resource)%20videos%20%3E%20(method)%20download_content%20%3E%20(params)%20default%20%3E%20(param)%20variant%20%3E%20(schema)) = "spritesheet"

##### ReturnsExpand Collapse

type VideoDownloadContentResponse interface{…}

### Retrieve video content

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
  response, err := client.Videos.DownloadContent(
    context.TODO(),
    "video_123",
    openai.VideoDownloadContentParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response)

##### Returns Examples
