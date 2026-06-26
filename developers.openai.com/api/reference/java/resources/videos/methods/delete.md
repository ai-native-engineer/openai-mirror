<!-- source: https://developers.openai.com/api/reference/java/resources/videos/methods/delete/ -->

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

# Delete video

[VideoDeleteResponse](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoDeleteResponse%20%3E%20(schema)) videos().delete(VideoDeleteParamsparams = VideoDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/videos/{video\_id}

Permanently delete a completed or failed video and its stored assets.

##### ParametersExpand Collapse

VideoDeleteParams params

Optional<String> videoId

##### ReturnsExpand Collapse

class VideoDeleteResponse:

Confirmation payload returned after deleting a video.

String id

Identifier of the deleted video.

boolean deleted

Indicates that the video resource was deleted.

JsonValue; object\_ "video.deleted"constant"video.deleted"constant

The object type that signals the deletion response.

### Delete video

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
import com.openai.models.videos.VideoDeleteParams;
import com.openai.models.videos.VideoDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoDeleteResponse video = client.videos().delete("video_123");

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "video.deleted"
