<!-- source: https://developers.openai.com/api/reference/resources/videos/methods/download_content/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Videos](/api/reference/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video content

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### Path ParametersExpand Collapse

video\_id: string

##### Query ParametersExpand Collapse

variant: optional "video" or "thumbnail" or "spritesheet"

Which downloadable asset to return. Defaults to the MP4 video.

One of the following:

"video"

"thumbnail"

"spritesheet"

### Retrieve video content

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/videos/$VIDEO_ID/content \
    -H "Authorization: Bearer $OPENAI_API_KEY"

##### Returns Examples
