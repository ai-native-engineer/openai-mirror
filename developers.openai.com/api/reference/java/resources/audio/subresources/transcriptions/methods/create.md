<!-- source: https://developers.openai.com/api/reference/java/resources/audio/subresources/transcriptions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Audio](/api/reference/java/resources/audio)

[Transcriptions](/api/reference/java/resources/audio/subresources/transcriptions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create transcription

[TranscriptionCreateResponse](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20TranscriptionCreateResponse%20%3E%20(schema)) audio().transcriptions().create(TranscriptionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/audio/transcriptions

Transcribes audio into the input language.

Returns a transcription object in `json`, `diarized_json`, or `verbose_json`
format, or a stream of transcript events.

##### ParametersExpand Collapse

TranscriptionCreateParams params

InputStream file

The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[AudioModel](/api/reference/java/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) model

ID of the model to use. The options are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `whisper-1` (which is powered by our open source Whisper V2 model), and `gpt-4o-transcribe-diarize`.

Optional<ChunkingStrategy> chunkingStrategy

Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block. Required when using `gpt-4o-transcribe-diarize` for inputs longer than 30 seconds.

JsonValue;

class VadConfig:

Type type

Must be set to `server_vad` to enable manual chunking using server side VAD.

Optional<Long> prefixPaddingMs

Amount of audio to include before the VAD detected speech (in
milliseconds).

Optional<Long> silenceDurationMs

Duration of silence to detect speech stop (in milliseconds).
With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Optional<Double> threshold

Sensitivity threshold (0.0 to 1.0) for voice activity detection. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

Optional<List<[TranscriptionInclude](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_include%20%3E%20(schema))>> include

Additional information to include in the transcription response.
`logprobs` will return the log probabilities of the tokens in the
response to understand the model’s confidence in the transcription.
`logprobs` only works with response\_format set to `json` and only with
the models `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `gpt-4o-mini-transcribe-2025-12-15`. This field is not supported when using `gpt-4o-transcribe-diarize`.

LOGPROBS("logprobs")

Optional<List<String>> knownSpeakerNames

Optional list of speaker names that correspond to the audio samples provided in `known_speaker_references[]`. Each entry should be a short identifier (for example `customer` or `agent`). Up to 4 speakers are supported.

Optional<List<String>> knownSpeakerReferences

Optional list of audio samples (as [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)) that contain known speaker references matching `known_speaker_names[]`. Each sample must be between 2 and 10 seconds, and can use any of the same input audio formats supported by `file`.

Optional<String> language

The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.

Optional<String> prompt

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language. This field is not supported when using `gpt-4o-transcribe-diarize`.

Optional<[AudioResponseFormat](/api/reference/java/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema))> responseFormat

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

Optional<Double> temperature

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

Optional<List<TimestampGranularity>> timestampGranularities

The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
This option is not available for `gpt-4o-transcribe-diarize`.

WORD("word")

SEGMENT("segment")

##### ReturnsExpand Collapse

class TranscriptionCreateResponse: A class that can be one of several variants.union

Represents a transcription response returned by model, based on the provided input.

class Transcription:

Represents a transcription response returned by model, based on the provided input.

String text

The transcribed text.

Optional<List<Logprob>> logprobs

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

Optional<String> token

The token in the transcription.

Optional<List<Double>> bytes

The bytes of the token.

Optional<Double> logprob

The log probability of the token.

Optional<Usage> usage

Token usage statistics for the request.

One of the following:

class Tokens:

Usage statistics for models billed by token usage.

long inputTokens

Number of input tokens billed for this request.

long outputTokens

Number of output tokens generated.

long totalTokens

Total number of tokens used (input + output).

JsonValue; type "tokens"constant"tokens"constant

The type of the usage object. Always `tokens` for this variant.

Optional<InputTokenDetails> inputTokenDetails

Details about the input tokens billed for this request.

Optional<Long> audioTokens

Number of audio tokens billed for this request.

Optional<Long> textTokens

Number of text tokens billed for this request.

class Duration:

Usage statistics for models billed by audio input duration.

double seconds

Duration of the input audio in seconds.

formatdouble

JsonValue; type "duration"constant"duration"constant

The type of the usage object. Always `duration` for this variant.

class TranscriptionDiarized:

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

double duration

Duration of the input audio in seconds.

formatdouble

List<[TranscriptionDiarizedSegment](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema))> segments

Segments of the transcript annotated with timestamps and speaker labels.

String id

Unique identifier for the segment.

double end

End timestamp of the segment in seconds.

formatdouble

String speaker

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

double start

Start timestamp of the segment in seconds.

formatdouble

String text

Transcript text for this segment.

JsonValue; type "transcript.text.segment"constant"transcript.text.segment"constant

The type of the segment. Always `transcript.text.segment`.

JsonValue; task "transcribe"constant"transcribe"constant

The type of task that was run. Always `transcribe`.

String text

The concatenated transcript text for the entire audio input.

Optional<Usage> usage

Token or duration usage statistics for the request.

One of the following:

class Tokens:

Usage statistics for models billed by token usage.

long inputTokens

Number of input tokens billed for this request.

long outputTokens

Number of output tokens generated.

long totalTokens

Total number of tokens used (input + output).

JsonValue; type "tokens"constant"tokens"constant

The type of the usage object. Always `tokens` for this variant.

Optional<InputTokenDetails> inputTokenDetails

Details about the input tokens billed for this request.

Optional<Long> audioTokens

Number of audio tokens billed for this request.

Optional<Long> textTokens

Number of text tokens billed for this request.

class Duration:

Usage statistics for models billed by audio input duration.

double seconds

Duration of the input audio in seconds.

formatdouble

JsonValue; type "duration"constant"duration"constant

The type of the usage object. Always `duration` for this variant.

class TranscriptionVerbose:

Represents a verbose json transcription response returned by model, based on the provided input.

double duration

The duration of the input audio.

formatdouble

String language

The language of the input audio.

String text

The transcribed text.

Optional<List<[TranscriptionSegment](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))>> segments

Segments of the transcribed text and their corresponding details.

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

Optional<Usage> usage

Usage statistics for models billed by audio input duration.

double seconds

Duration of the input audio in seconds.

formatdouble

JsonValue; type "duration"constant"duration"constant

The type of the usage object. Always `duration` for this variant.

Optional<List<[TranscriptionWord](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema))>> words

Extracted words and their corresponding timestamps.

double end

End time of the word in seconds.

formatdouble

double start

Start time of the word in seconds.

formatdouble

String word

The text content of the word.

class TranscriptionStreamEvent: A class that can be one of several variants.union

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

class TranscriptionTextSegmentEvent:

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

String id

Unique identifier for the segment.

double end

End timestamp of the segment in seconds.

formatdouble

String speaker

Speaker label for this segment.

double start

Start timestamp of the segment in seconds.

formatdouble

String text

Transcript text for this segment.

JsonValue; type "transcript.text.segment"constant"transcript.text.segment"constant

The type of the event. Always `transcript.text.segment`.

class TranscriptionTextDeltaEvent:

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

String delta

The text delta that was additionally transcribed.

JsonValue; type "transcript.text.delta"constant"transcript.text.delta"constant

The type of the event. Always `transcript.text.delta`.

Optional<List<Logprob>> logprobs

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

Optional<String> token

The token that was used to generate the log probability.

Optional<List<Long>> bytes

The bytes that were used to generate the log probability.

Optional<Double> logprob

The log probability of the token.

Optional<String> segmentId

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

class TranscriptionTextDoneEvent:

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

String text

The text that was transcribed.

JsonValue; type "transcript.text.done"constant"transcript.text.done"constant

The type of the event. Always `transcript.text.done`.

Optional<List<Logprob>> logprobs

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

Optional<String> token

The token that was used to generate the log probability.

Optional<List<Long>> bytes

The bytes that were used to generate the log probability.

Optional<Double> logprob

The log probability of the token.

Optional<Usage> usage

Usage statistics for models billed by token usage.

long inputTokens

Number of input tokens billed for this request.

long outputTokens

Number of output tokens generated.

long totalTokens

Total number of tokens used (input + output).

JsonValue; type "tokens"constant"tokens"constant

The type of the usage object. Always `tokens` for this variant.

Optional<InputTokenDetails> inputTokenDetails

Details about the input tokens billed for this request.

Optional<Long> audioTokens

Number of audio tokens billed for this request.

Optional<Long> textTokens

Number of text tokens billed for this request.

### Create transcription

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
import com.openai.models.audio.transcriptions.TranscriptionCreateParams;
import com.openai.models.audio.transcriptions.TranscriptionCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TranscriptionCreateParams params = TranscriptionCreateParams.builder()
            .file(new ByteArrayInputStream("Example data".getBytes()))
            .model(AudioModel.GPT_4O_TRANSCRIBE)
            .build();
        TranscriptionCreateResponse transcription = client.audio().transcriptions().create(params);

  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that.",
  "usage": {
    "type": "tokens",
    "input_tokens": 14,
    "input_token_details": {
      "text_tokens": 0,
      "audio_tokens": 14
    "output_tokens": 45,
    "total_tokens": 59

##### Returns Examples

  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that.",
  "usage": {
    "type": "tokens",
    "input_tokens": 14,
    "input_token_details": {
      "text_tokens": 0,
      "audio_tokens": 14
    "output_tokens": 45,
    "total_tokens": 59
