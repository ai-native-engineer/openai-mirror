<!-- source: https://developers.openai.com/api/reference/java/resources/audio/subresources/speech/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Audio](/api/reference/java/resources/audio)

[Speech](/api/reference/java/resources/audio/subresources/speech)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create speech

HttpResponse audio().speech().create(SpeechCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/audio/speech

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

##### ParametersExpand Collapse

SpeechCreateParams params

String input

The text to generate audio for. The maximum length is 4096 characters.

maxLength4096

[SpeechModel](/api/reference/java/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)) model

One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

Voice voice

The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

String

enum UnionMember1:

ALLOY("alloy")

ASH("ash")

BALLAD("ballad")

CORAL("coral")

ECHO("echo")

SAGE("sage")

SHIMMER("shimmer")

VERSE("verse")

MARIN("marin")

CEDAR("cedar")

class Id:

Custom voice reference.

String id

The custom voice ID, e.g. `voice_1234`.

Optional<String> instructions

Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

maxLength4096

Optional<ResponseFormat> responseFormat

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

MP3("mp3")

OPUS("opus")

AAC("aac")

FLAC("flac")

WAV("wav")

PCM("pcm")

Optional<Double> speed

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

minimum0.25

maximum4

Optional<StreamFormat> streamFormat

The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

SSE("sse")

AUDIO("audio")

### Create speech

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
import com.openai.models.audio.speech.SpeechCreateParams;
import com.openai.models.audio.speech.SpeechModel;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpeechCreateParams params = SpeechCreateParams.builder()
            .input("input")
            .model(SpeechModel.TTS_1)
            .voice(SpeechCreateParams.Voice.UnionMember1.ALLOY)
            .build();
        HttpResponse speech = client.audio().speech().create(params);

##### Returns Examples
