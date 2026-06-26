<!-- source: https://developers.openai.com/api/reference/java/resources/audio/subresources/translations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Audio](/api/reference/java/resources/audio)

[Translations](/api/reference/java/resources/audio/subresources/translations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create translation

[TranslationCreateResponse](/api/reference/java/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20TranslationCreateResponse%20%3E%20(schema)) audio().translations().create(TranslationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/audio/translations

Translates audio into English.

##### ParametersExpand Collapse

TranslationCreateParams params

InputStream file

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[AudioModel](/api/reference/java/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) model

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

Optional<String> prompt

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

Optional<ResponseFormat> responseFormat

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

JSON("json")

TEXT("text")

SRT("srt")

VERBOSE\_JSON("verbose\_json")

VTT("vtt")

Optional<Double> temperature

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

##### ReturnsExpand Collapse

class TranslationCreateResponse: A class that can be one of several variants.union

class Translation:

String text

class TranslationVerbose:

double duration

The duration of the input audio.

formatdouble

String language

The language of the output translation (always `english`).

String text

The translated text.

Optional<List<[TranscriptionSegment](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))>> segments

Segments of the translated text and their corresponding details.

long id

Unique identifier of the segment.

double avgLogprob

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

double compressionRatio

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

double end

End time of the segment in seconds.

formatdouble

double noSpeechProb

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

long seek

Seek offset of the segment.

double start

Start time of the segment in seconds.

formatdouble

double temperature

Temperature parameter used for generating the segment.

formatfloat

String text

Text content of the segment.

List<long> tokens

Array of token IDs for the text content.

### Create translation

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
import com.openai.models.audio.AudioModel;
import com.openai.models.audio.translations.TranslationCreateParams;
import com.openai.models.audio.translations.TranslationCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TranslationCreateParams params = TranslationCreateParams.builder()
            .file(new ByteArrayInputStream("Example data".getBytes()))
            .model(AudioModel.WHISPER_1)
            .build();
        TranslationCreateResponse translation = client.audio().translations().create(params);

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"

##### Returns Examples

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
