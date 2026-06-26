<!-- source: https://developers.openai.com/api/reference/go/resources/audio/subresources/transcriptions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Audio](/api/reference/go/resources/audio)

[Transcriptions](/api/reference/go/resources/audio/subresources/transcriptions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create transcription

client.Audio.Transcriptions.New(ctx, body) (\*[AudioTranscriptionNewResponseUnion](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20AudioTranscriptionNewResponse%20%3E%20(schema)), error)

POST/audio/transcriptions

Transcribes audio into the input language.

Returns a transcription object in `json`, `diarized_json`, or `verbose_json`
format, or a stream of transcript events.

##### ParametersExpand Collapse

body AudioTranscriptionNewParams

File param.Field[[Reader](/api/reference/go/resources/audio/subresources/transcriptions/methods/create#(resource)%20audio.transcriptions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20file%20%3E%20(schema))]

The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

Model param.Field[[AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))]

ID of the model to use. The options are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `whisper-1` (which is powered by our open source Whisper V2 model), and `gpt-4o-transcribe-diarize`.

string

type AudioModel string

One of the following:

const AudioModelWhisper1 [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "whisper-1"

const AudioModelGPT4oTranscribe [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-transcribe"

const AudioModelGPT4oMiniTranscribe [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-mini-transcribe"

const AudioModelGPT4oMiniTranscribe2025\_12\_15 [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-mini-transcribe-2025-12-15"

const AudioModelGPT4oTranscribeDiarize [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-transcribe-diarize"

ChunkingStrategy param.Field[[AudioTranscriptionNewParamsChunkingStrategyUnion](/api/reference/go/resources/audio/subresources/transcriptions/methods/create#(resource)%20audio.transcriptions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20chunking_strategy%20%3E%20(schema))]Optional

Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block. Required when using `gpt-4o-transcribe-diarize` for inputs longer than 30 seconds.

Auto

AudioTranscriptionNewParamsChunkingStrategyVadConfig

Type string

Must be set to `server_vad` to enable manual chunking using server side VAD.

PrefixPaddingMs int64Optional

Amount of audio to include before the VAD detected speech (in
milliseconds).

SilenceDurationMs int64Optional

Duration of silence to detect speech stop (in milliseconds).
With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Threshold float64Optional

Sensitivity threshold (0.0 to 1.0) for voice activity detection. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

Include param.Field[[][TranscriptionInclude](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_include%20%3E%20(schema))]Optional

Additional information to include in the transcription response.
`logprobs` will return the log probabilities of the tokens in the
response to understand the model’s confidence in the transcription.
`logprobs` only works with response\_format set to `json` and only with
the models `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `gpt-4o-mini-transcribe-2025-12-15`. This field is not supported when using `gpt-4o-transcribe-diarize`.

const TranscriptionIncludeLogprobs [TranscriptionInclude](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_include%20%3E%20(schema)) = "logprobs"

KnownSpeakerNames param.Field[[]string]Optional

Optional list of speaker names that correspond to the audio samples provided in `known_speaker_references[]`. Each entry should be a short identifier (for example `customer` or `agent`). Up to 4 speakers are supported.

KnownSpeakerReferences param.Field[[]string]Optional

Optional list of audio samples (as [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)) that contain known speaker references matching `known_speaker_names[]`. Each sample must be between 2 and 10 seconds, and can use any of the same input audio formats supported by `file`.

Language param.Field[string]Optional

The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.

Prompt param.Field[string]Optional

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language. This field is not supported when using `gpt-4o-transcribe-diarize`.

ResponseFormat param.Field[[AudioResponseFormat](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_response_format%20%3E%20(schema))]Optional

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

Temperature param.Field[float64]Optional

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

TimestampGranularities param.Field[[]string]Optional

The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
This option is not available for `gpt-4o-transcribe-diarize`.

const AudioTranscriptionNewParamsTimestampGranularityWord AudioTranscriptionNewParamsTimestampGranularity = "word"

const AudioTranscriptionNewParamsTimestampGranularitySegment AudioTranscriptionNewParamsTimestampGranularity = "segment"

##### ReturnsExpand Collapse

type AudioTranscriptionNewResponseUnion interface{…}

Represents a transcription response returned by model, based on the provided input.

One of the following:

type Transcription struct{…}

Represents a transcription response returned by model, based on the provided input.

Text string

The transcribed text.

Logprobs []TranscriptionLogprobOptional

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

Token stringOptional

The token in the transcription.

Bytes []float64Optional

The bytes of the token.

Logprob float64Optional

The log probability of the token.

Usage TranscriptionUsageUnionOptional

Token usage statistics for the request.

One of the following:

type TranscriptionUsageTokens struct{…}

Usage statistics for models billed by token usage.

InputTokens int64

Number of input tokens billed for this request.

OutputTokens int64

Number of output tokens generated.

TotalTokens int64

Total number of tokens used (input + output).

Type Tokens

The type of the usage object. Always `tokens` for this variant.

InputTokenDetails TranscriptionUsageTokensInputTokenDetailsOptional

Details about the input tokens billed for this request.

AudioTokens int64Optional

Number of audio tokens billed for this request.

TextTokens int64Optional

Number of text tokens billed for this request.

type TranscriptionUsageDuration struct{…}

Usage statistics for models billed by audio input duration.

Seconds float64

Duration of the input audio in seconds.

formatdouble

Type Duration

The type of the usage object. Always `duration` for this variant.

type TranscriptionVerbose struct{…}

Represents a verbose json transcription response returned by model, based on the provided input.

Duration float64

The duration of the input audio.

formatdouble

Language string

The language of the input audio.

Text string

The transcribed text.

Segments [][TranscriptionSegment](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))Optional

Segments of the transcribed text and their corresponding details.

ID int64

Unique identifier of the segment.

AvgLogprob float64

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

CompressionRatio float64

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

End float64

End time of the segment in seconds.

formatdouble

NoSpeechProb float64

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

Seek int64

Seek offset of the segment.

Start float64

Start time of the segment in seconds.

formatdouble

Temperature float64

Temperature parameter used for generating the segment.

formatfloat

Text string

Text content of the segment.

Tokens []int64

Array of token IDs for the text content.

Usage TranscriptionVerboseUsageOptional

Usage statistics for models billed by audio input duration.

Seconds float64

Duration of the input audio in seconds.

formatdouble

Type Duration

The type of the usage object. Always `duration` for this variant.

Words [][TranscriptionWord](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema))Optional

Extracted words and their corresponding timestamps.

End float64

End time of the word in seconds.

formatdouble

Start float64

Start time of the word in seconds.

formatdouble

Word string

The text content of the word.

type TranscriptionStreamEventUnion interface{…}

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

One of the following:

type TranscriptionTextSegmentEvent struct{…}

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

ID string

Unique identifier for the segment.

End float64

End timestamp of the segment in seconds.

formatdouble

Speaker string

Speaker label for this segment.

Start float64

Start timestamp of the segment in seconds.

formatdouble

Text string

Transcript text for this segment.

Type TranscriptTextSegment

The type of the event. Always `transcript.text.segment`.

type TranscriptionTextDeltaEvent struct{…}

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

Delta string

The text delta that was additionally transcribed.

Type TranscriptTextDelta

The type of the event. Always `transcript.text.delta`.

Logprobs []TranscriptionTextDeltaEventLogprobOptional

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

Token stringOptional

The token that was used to generate the log probability.

Bytes []int64Optional

The bytes that were used to generate the log probability.

Logprob float64Optional

The log probability of the token.

SegmentID stringOptional

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

type TranscriptionTextDoneEvent struct{…}

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

Text string

The text that was transcribed.

Type TranscriptTextDone

The type of the event. Always `transcript.text.done`.

Logprobs []TranscriptionTextDoneEventLogprobOptional

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

Token stringOptional

The token that was used to generate the log probability.

Bytes []int64Optional

The bytes that were used to generate the log probability.

Logprob float64Optional

The log probability of the token.

Usage TranscriptionTextDoneEventUsageOptional

Usage statistics for models billed by token usage.

InputTokens int64

Number of input tokens billed for this request.

OutputTokens int64

Number of output tokens generated.

TotalTokens int64

Total number of tokens used (input + output).

Type Tokens

The type of the usage object. Always `tokens` for this variant.

InputTokenDetails TranscriptionTextDoneEventUsageInputTokenDetailsOptional

Details about the input tokens billed for this request.

AudioTokens int64Optional

Number of audio tokens billed for this request.

TextTokens int64Optional

Number of text tokens billed for this request.

### Create transcription

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  transcription, err := client.Audio.Transcriptions.New(context.TODO(), openai.AudioTranscriptionNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    Model: openai.AudioModelGPT4oTranscribe,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", transcription)

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
