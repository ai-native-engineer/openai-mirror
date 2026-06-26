<!-- source: https://developers.openai.com/api/reference/ruby/resources/videos/methods/download_content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Videos](/api/reference/ruby/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video content

videos.download\_content(video\_id, \*\*kwargs) -> StringIO

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### ParametersExpand Collapse

video\_id: String

variant: :video | :thumbnail | :spritesheet

Which downloadable asset to return. Defaults to the MP4 video.

One of the following:

:video

:thumbnail

:spritesheet

##### ReturnsExpand Collapse

StringIO

### Retrieve video content

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new

response = openai.videos.download_content("video_123")

puts(response)

##### Returns Examples
