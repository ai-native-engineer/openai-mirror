<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/methods/download_content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Videos](/api/reference/typescript/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video content

client.videos.downloadContent(stringvideoID, VideoDownloadContentParams { variant } query?, RequestOptionsoptions?): Response

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### ParametersExpand Collapse

videoID: string

query: VideoDownloadContentParams { variant }

variant?: "video" | "thumbnail" | "spritesheet"

Which downloadable asset to return. Defaults to the MP4 video.

One of the following:

"video"

"thumbnail"

"spritesheet"

##### ReturnsExpand Collapse

unnamed\_schema\_12 = Response

### Retrieve video content

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI();

const response = await client.videos.downloadContent('video_123');

console.log(response);

const content = await response.blob();
console.log(content);

##### Returns Examples
