<!-- source: https://developers.openai.com/api/reference/java/resources/videos/methods/download_content/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Videos](/api/reference/java/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve video content

HttpResponse videos().downloadContent(VideoDownloadContentParamsparams = VideoDownloadContentParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/videos/{video\_id}/content

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

##### ParametersExpand Collapse

VideoDownloadContentParams params

Optional<String> videoId

Optional<[Variant](/api/reference/java/resources/videos/methods/download_content#(resource)%20videos%20%3E%20(method)%20download_content%20%3E%20(params)%20default%20%3E%20(param)%20variant%20%3E%20(schema))> variant

Which downloadable asset to return. Defaults to the MP4 video.

VIDEO("video")

THUMBNAIL("thumbnail")

SPRITESHEET("spritesheet")

### Retrieve video content

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.videos.VideoDownloadContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse response = client.videos().downloadContent("video_123");

##### Returns Examples
