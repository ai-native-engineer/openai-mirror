<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/methods/download_content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Videos](/api/reference/cli/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video content

$ openai videos download-content

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### ParametersExpand Collapse

--video-id: string

The identifier of the video whose media to download.

--variant: optional "video" or "thumbnail" or "spritesheet"

Which downloadable asset to return. Defaults to the MP4 video.

##### ReturnsExpand Collapse

unnamed\_schema\_6: file path

### Retrieve video content

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai videos download-content \
  --api-key 'My API Key' \
  --video-id video_123

##### Returns Examples
