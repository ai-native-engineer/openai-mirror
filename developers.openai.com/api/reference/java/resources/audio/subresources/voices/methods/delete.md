<!-- source: https://developers.openai.com/api/reference/java/resources/audio/subresources/voices/methods/delete/ -->

## Delete voice

`VoiceDeleted audio().voices().delete(VoiceDeleteParamsparams = VoiceDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/audio/voices/{voice_id}`

Deletes a voice created from a text prompt or an audio sample.

Requires voice write permission and access to the voice's project. Access to voices created from recordings is limited to eligible customers. See the [custom voices guide](https://developers.openai.com/api/docs/guides/custom-voices).

Deleting a voice does not delete its consent recording. Deleting an already deleted voice returns a 404 error.

- `VoiceDeleteParams params`

  - `Optional<String> voiceId`

- `class VoiceDeleted:`

  - `String id`

    The voice identifier.

  - `boolean deleted`

    Whether the voice was deleted.

  - `JsonValue; object_ "audio.voice.deleted"constant`

    The object type, which is always `audio.voice.deleted`.

    - `AUDIO_VOICE_DELETED("audio.voice.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.audio.voices.VoiceDeleteParams;
import com.openai.models.audio.voices.VoiceDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VoiceDeleted voiceDeleted = client.audio().voices().delete("voice_id");

  "id": "voice_1234",
  "deleted": true,
  "object": "audio.voice.deleted"
