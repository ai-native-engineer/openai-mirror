<!-- source: https://developers.openai.com/api/reference/java/resources/videos/methods/create_character/ -->

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

# Create a character from an uploaded video.

[VideoCreateCharacterResponse](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoCreateCharacterResponse%20%3E%20(schema)) videos().createCharacter(VideoCreateCharacterParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/videos/characters

Create a character from an uploaded video.

##### ParametersExpand Collapse

VideoCreateCharacterParams params

String name

Display name for this API character.

maxLength80

minLength1

InputStream video

Video file used to create a character.

##### ReturnsExpand Collapse

class VideoCreateCharacterResponse:

Optional<String> id

Identifier for the character creation cameo.

long createdAt

Unix timestamp (in seconds) when the character was created.

formatunixtime

Optional<String> name

Display name for the character.

### Create a character from an uploaded video.

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
import com.openai.models.videos.VideoCreateCharacterParams;
import com.openai.models.videos.VideoCreateCharacterResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoCreateCharacterParams params = VideoCreateCharacterParams.builder()
            .name("x")
            .video(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        VideoCreateCharacterResponse response = client.videos().createCharacter(params);

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
