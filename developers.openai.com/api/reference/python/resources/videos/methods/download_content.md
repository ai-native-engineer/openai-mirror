<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/download_content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Videos](/api/reference/python/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video content

videos.download\_content(strvideo\_id, VideoDownloadContentParams\*\*kwargs)  -> BinaryResponseContent

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### ParametersExpand Collapse

video\_id: str

variant: Optional[Literal["video", "thumbnail", "spritesheet"]]

Which downloadable asset to return. Defaults to the MP4 video.

One of the following:

"video"

"thumbnail"

"spritesheet"

##### ReturnsExpand Collapse

BinaryResponseContent

### Retrieve video content

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI

client = OpenAI()
response = client.videos.download_content(
    video_id="video_123",
print(response)
content = response.read()
print(content)

##### Returns Examples
