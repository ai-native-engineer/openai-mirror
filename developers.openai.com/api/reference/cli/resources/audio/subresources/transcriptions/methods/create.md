<!-- source: https://developers.openai.com/api/reference/cli/resources/audio/subresources/transcriptions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Audio](/api/reference/cli/resources/audio)

[Transcriptions](/api/reference/cli/resources/audio/subresources/transcriptions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create transcription

$ openai audio:transcriptions create

POST/audio/transcriptions

Transcribes audio into the input language.

Returns a transcription object in `json`, `diarized_json`, or `verbose_json`
format, or a stream of transcript events.

##### ParametersExpand Collapse

--file: file path

The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

--model: string or [AudioModel](/api/reference/cli/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))

ID of the model to use. The options are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `whisper-1` (which is powered by our open source Whisper V2 model), and `gpt-4o-transcribe-diarize`.

--chunking-strategy: optional "auto" or object { type, prefix\_padding\_ms, silence\_duration\_ms, threshold }

Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block. Required when using `gpt-4o-transcribe-diarize` for inputs longer than 30 seconds.

--include: optional array of [TranscriptionInclude](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_include%20%3E%20(schema))

Additional information to include in the transcription response.
`logprobs` will return the log probabilities of the tokens in the
response to understand the model’s confidence in the transcription.
`logprobs` only works with response\_format set to `json` and only with
the models `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `gpt-4o-mini-transcribe-2025-12-15`. This field is not supported when using `gpt-4o-transcribe-diarize`.

--known-speaker-name: optional array of string

Optional list of speaker names that correspond to the audio samples provided in `known_speaker_references[]`. Each entry should be a short identifier (for example `customer` or `agent`). Up to 4 speakers are supported.

--known-speaker-reference: optional array of string

Optional list of audio samples (as [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)) that contain known speaker references matching `known_speaker_names[]`. Each sample must be between 2 and 10 seconds, and can use any of the same input audio formats supported by `file`.

--language: optional string

The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.

--prompt: optional string

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language. This field is not supported when using `gpt-4o-transcribe-diarize`.

--response-format: optional "json" or "text" or "srt" or 3 more

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

--temperature: optional number

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

--timestamp-granularity: optional array of "word" or "segment"

The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
This option is not available for `gpt-4o-transcribe-diarize`.

##### ReturnsExpand Collapse

AudioTranscriptionNewResponse: [Transcription](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)) { text, logprobs, usage }  or [TranscriptionDiarized](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)) { duration, segments, task, 2 more }  or [TranscriptionVerbose](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)) { duration, language, text, 3 more }

Represents a transcription response returned by model, based on the provided input.

transcription: object { text, logprobs, usage }

Represents a transcription response returned by model, based on the provided input.

text: string

The transcribed text.

logprobs: optional array of object { token, bytes, logprob }

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token: optional string

The token in the transcription.

bytes: optional array of number

The bytes of the token.

logprob: optional number

The log probability of the token.

usage: optional object { input\_tokens, output\_tokens, total\_tokens, 2 more }  or object { seconds, type }

Token usage statistics for the request.

tokens: object { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: optional object { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens: optional number

Number of audio tokens billed for this request.

text\_tokens: optional number

Number of text tokens billed for this request.

duration: object { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

type: "duration"

The type of the usage object. Always `duration` for this variant.

transcription\_diarized: object { duration, segments, task, 2 more }

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration: number

Duration of the input audio in seconds.

segments: array of [TranscriptionDiarizedSegment](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)) { id, end, speaker, 3 more }

Segments of the transcript annotated with timestamps and speaker labels.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

speaker: string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: number

Start timestamp of the segment in seconds.

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

task: "transcribe"

The type of task that was run. Always `transcribe`.

text: string

The concatenated transcript text for the entire audio input.

usage: optional object { input\_tokens, output\_tokens, total\_tokens, 2 more }  or object { seconds, type }

Token or duration usage statistics for the request.

tokens: object { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: optional object { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens: optional number

Number of audio tokens billed for this request.

text\_tokens: optional number

Number of text tokens billed for this request.

duration: object { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

type: "duration"

The type of the usage object. Always `duration` for this variant.

transcription\_verbose: object { duration, language, text, 3 more }

Represents a verbose json transcription response returned by model, based on the provided input.

duration: number

The duration of the input audio.

language: string

The language of the input audio.

text: string

The transcribed text.

segments: optional array of [TranscriptionSegment](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more }

Segments of the transcribed text and their corresponding details.

id: number

Unique identifier of the segment.

avg\_logprob: number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

compression\_ratio: number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

end: number

End time of the segment in seconds.

no\_speech\_prob: number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

seek: number

Seek offset of the segment.

start: number

Start time of the segment in seconds.

temperature: number

Temperature parameter used for generating the segment.

text: string

Text content of the segment.

tokens: array of number

Array of token IDs for the text content.

usage: optional object { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

type: "duration"

The type of the usage object. Always `duration` for this variant.

words: optional array of [TranscriptionWord](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)) { end, start, word }

Extracted words and their corresponding timestamps.

end: number

End time of the word in seconds.

start: number

Start time of the word in seconds.

word: string

The text content of the word.

transcription\_stream\_event: [TranscriptionTextSegmentEvent](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)) { id, end, speaker, 3 more }  or [TranscriptionTextDeltaEvent](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)) { delta, type, logprobs, segment\_id }  or [TranscriptionTextDoneEvent](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)) { text, type, logprobs, usage }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

transcription\_text\_segment\_event: object { id, end, speaker, 3 more }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

speaker: string

Speaker label for this segment.

start: number

Start timestamp of the segment in seconds.

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the event. Always `transcript.text.segment`.

transcription\_text\_delta\_event: object { delta, type, logprobs, segment\_id }

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta: string

The text delta that was additionally transcribed.

type: "transcript.text.delta"

The type of the event. Always `transcript.text.delta`.

logprobs: optional array of object { token, bytes, logprob }

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token: optional string

The token that was used to generate the log probability.

bytes: optional array of number

The bytes that were used to generate the log probability.

logprob: optional number

The log probability of the token.

segment\_id: optional string

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

transcription\_text\_done\_event: object { text, type, logprobs, usage }

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text: string

The text that was transcribed.

type: "transcript.text.done"

The type of the event. Always `transcript.text.done`.

logprobs: optional array of object { token, bytes, logprob }

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token: optional string

The token that was used to generate the log probability.

bytes: optional array of number

The bytes that were used to generate the log probability.

logprob: optional number

The log probability of the token.

usage: optional object { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: optional object { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens: optional number

Number of audio tokens billed for this request.

text\_tokens: optional number

Number of text tokens billed for this request.

### Create transcription

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai audio:transcriptions create \
  --api-key 'My API Key' \
  --file 'Example data' \
  --model gpt-4o-transcribe

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
