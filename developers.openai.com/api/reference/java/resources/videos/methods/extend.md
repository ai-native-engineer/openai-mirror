<!-- source: https://developers.openai.com/api/reference/java/resources/videos/methods/extend/ -->

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

# Create an extension of a completed video.

[Video](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video%20%3E%20(schema)) videos().extend(VideoExtendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos/extensions

Create an extension of a completed video.

##### ParametersExpand Collapse

VideoExtendParams params

String prompt

Updated text prompt that directs the extension generation.

maxLength32000

minLength1

[VideoSeconds](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) seconds

Length of the newly generated extension segment in seconds (allowed values: 4, 8, 12, 16, 20).

Video video

Reference to the completed video to extend.

String

class VideoReferenceInputParam:

Reference to the completed video.

String id

The identifier of the completed video.

##### ReturnsExpand Collapse

class Video:

Structured information describing a generated video job.

String id

Unique identifier for the video job.

Optional<Long> completedAt

Unix timestamp (seconds) for when the job completed, if finished.

formatunixtime

long createdAt

Unix timestamp (seconds) for when the job was created.

formatunixtime

Optional<[VideoCreateError](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_error%20%3E%20(schema))> error

Error payload that explains why generation failed, if applicable.

String code

A machine-readable error code that was returned.

String message

A human-readable description of the error that was returned.

Optional<Long> expiresAt

Unix timestamp (seconds) for when the downloadable assets expire, if set.

formatunixtime

VideoModel model

The video generation model that produced the job.

One of the following:

SORA\_2("sora-2")

SORA\_2\_PRO("sora-2-pro")

SORA\_2\_2025\_10\_06("sora-2-2025-10-06")

SORA\_2\_PRO\_2025\_10\_06("sora-2-pro-2025-10-06")

SORA\_2\_2025\_12\_08("sora-2-2025-12-08")

JsonValue; object\_ "video"constant"video"constant

The object type, which is always `video`.

long progress

Approximate completion percentage for the generation task.

Optional<String> prompt

The prompt that was used to generate the video.

Optional<String> remixedFromVideoId

Identifier of the source video if this video is a remix.

[VideoSeconds](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_seconds%20%3E%20(schema)) seconds

Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

One of the following:

\_4("4")

\_8("8")

\_12("12")

[VideoSize](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20video_size%20%3E%20(schema)) size

The resolution of the generated video.

One of the following:

\_720X1280("720x1280")

\_1280X720("1280x720")

\_1024X1792("1024x1792")

\_1792X1024("1792x1024")

Status status

Current lifecycle status of the video job.

One of the following:

QUEUED("queued")

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

FAILED("failed")

### Create an extension of a completed video.

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
import com.openai.models.videos.Video;
import com.openai.models.videos.VideoExtendParams;
import com.openai.models.videos.VideoSeconds;
import java.io.ByteArrayInputStream;
import java.io.InputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoExtendParams params = VideoExtendParams.builder()
            .prompt("x")
            .seconds(VideoSeconds._4)
            .video(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        Video video = client.videos().extend(params);

200 example

  "id": "id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  "expires_at": 0,
  "model": "sora-2",
  "object": "video",
  "progress": 0,
  "prompt": "prompt",
  "remixed_from_video_id": "remixed_from_video_id",
  "seconds": "4",
  "size": "720x1280",
  "status": "queued"

##### Returns Examples

200 example

  "id": "id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  "expires_at": 0,
  "model": "sora-2",
  "object": "video",
  "progress": 0,
  "prompt": "prompt",
  "remixed_from_video_id": "remixed_from_video_id",
  "seconds": "4",
  "size": "720x1280",
  "status": "queued"
