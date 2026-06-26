<!-- source: https://developers.openai.com/api/reference/java/resources/videos/methods/get_character/ -->

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

# Fetch a character.

[VideoGetCharacterResponse](/api/reference/java/resources/videos#(resource)%20videos%20%3E%20(model)%20VideoGetCharacterResponse%20%3E%20(schema)) videos().getCharacter(VideoGetCharacterParamsparams = VideoGetCharacterParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/videos/characters/{character\_id}

Fetch a character.

##### ParametersExpand Collapse

VideoGetCharacterParams params

Optional<String> characterId

##### ReturnsExpand Collapse

class VideoGetCharacterResponse:

Optional<String> id

Identifier for the character creation cameo.

long createdAt

Unix timestamp (in seconds) when the character was created.

formatunixtime

Optional<String> name

Display name for the character.

### Fetch a character.

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
import com.openai.models.videos.VideoGetCharacterParams;
import com.openai.models.videos.VideoGetCharacterResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoGetCharacterResponse response = client.videos().getCharacter("char_123");

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
