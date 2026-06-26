<!-- source: https://developers.openai.com/api/reference/typescript/resources/audio/subresources/transcriptions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Audio](/api/reference/typescript/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Transcriptions

Turn audio into text or text into audio.

##### [Create transcription](/api/reference/typescript/resources/audio/subresources/transcriptions/methods/create)

client.audio.transcriptions.create(TranscriptionCreateParamsbody, RequestOptionsoptions?): [TranscriptionCreateResponse](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_create_response%20%3E%20(schema)) | Stream<[TranscriptionStreamEvent](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_stream_event%20%3E%20(schema))>

POST/audio/transcriptions

##### ModelsExpand Collapse

Transcription { text, logprobs, usage }

Represents a transcription response returned by model, based on the provided input.

text: string

The transcribed text.

logprobs?: Array<Logprob>

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token?: string

The token in the transcription.

bytes?: Array<number>

The bytes of the token.

logprob?: number

The log probability of the token.

usage?: Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }  | Duration { seconds, type }

Token usage statistics for the request.

One of the following:

Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details?: InputTokenDetails { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens?: number

Number of audio tokens billed for this request.

text\_tokens?: number

Number of text tokens billed for this request.

Duration { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

formatdouble

type: "duration"

The type of the usage object. Always `duration` for this variant.

TranscriptionDiarized { duration, segments, task, 2 more }

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration: number

Duration of the input audio in seconds.

formatdouble

segments: Array<[TranscriptionDiarizedSegment](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)) { id, end, speaker, 3 more } >

Segments of the transcript annotated with timestamps and speaker labels.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

formatdouble

speaker: string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: number

Start timestamp of the segment in seconds.

formatdouble

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

task: "transcribe"

The type of task that was run. Always `transcribe`.

text: string

The concatenated transcript text for the entire audio input.

usage?: Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }  | Duration { seconds, type }

Token or duration usage statistics for the request.

One of the following:

Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details?: InputTokenDetails { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens?: number

Number of audio tokens billed for this request.

text\_tokens?: number

Number of text tokens billed for this request.

Duration { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

formatdouble

type: "duration"

The type of the usage object. Always `duration` for this variant.

TranscriptionDiarizedSegment { id, end, speaker, 3 more }

A segment of diarized transcript text with speaker metadata.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

formatdouble

speaker: string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: number

Start timestamp of the segment in seconds.

formatdouble

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

TranscriptionInclude = "logprobs"

TranscriptionSegment { id, avg\_logprob, compression\_ratio, 7 more }

id: number

Unique identifier of the segment.

avg\_logprob: number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: number

End time of the segment in seconds.

formatdouble

no\_speech\_prob: number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: number

Seek offset of the segment.

start: number

Start time of the segment in seconds.

formatdouble

temperature: number

Temperature parameter used for generating the segment.

formatfloat

text: string

Text content of the segment.

tokens: Array<number>

Array of token IDs for the text content.

TranscriptionStreamEvent = [TranscriptionTextSegmentEvent](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_segment_event%20%3E%20(schema)) { id, end, speaker, 3 more }  | [TranscriptionTextDeltaEvent](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_delta_event%20%3E%20(schema)) { delta, type, logprobs, segment\_id }  | [TranscriptionTextDoneEvent](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_text_done_event%20%3E%20(schema)) { text, type, logprobs, usage }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

One of the following:

TranscriptionTextSegmentEvent { id, end, speaker, 3 more }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

formatdouble

speaker: string

Speaker label for this segment.

start: number

Start timestamp of the segment in seconds.

formatdouble

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the event. Always `transcript.text.segment`.

TranscriptionTextDeltaEvent { delta, type, logprobs, segment\_id }

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta: string

The text delta that was additionally transcribed.

type: "transcript.text.delta"

The type of the event. Always `transcript.text.delta`.

logprobs?: Array<Logprob>

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token?: string

The token that was used to generate the log probability.

bytes?: Array<number>

The bytes that were used to generate the log probability.

logprob?: number

The log probability of the token.

segment\_id?: string

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

TranscriptionTextDoneEvent { text, type, logprobs, usage }

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text: string

The text that was transcribed.

type: "transcript.text.done"

The type of the event. Always `transcript.text.done`.

logprobs?: Array<Logprob>

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token?: string

The token that was used to generate the log probability.

bytes?: Array<number>

The bytes that were used to generate the log probability.

logprob?: number

The log probability of the token.

usage?: Usage { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details?: InputTokenDetails { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens?: number

Number of audio tokens billed for this request.

text\_tokens?: number

Number of text tokens billed for this request.

TranscriptionTextDeltaEvent { delta, type, logprobs, segment\_id }

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta: string

The text delta that was additionally transcribed.

type: "transcript.text.delta"

The type of the event. Always `transcript.text.delta`.

logprobs?: Array<Logprob>

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token?: string

The token that was used to generate the log probability.

bytes?: Array<number>

The bytes that were used to generate the log probability.

logprob?: number

The log probability of the token.

segment\_id?: string

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

TranscriptionTextDoneEvent { text, type, logprobs, usage }

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text: string

The text that was transcribed.

type: "transcript.text.done"

The type of the event. Always `transcript.text.done`.

logprobs?: Array<Logprob>

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token?: string

The token that was used to generate the log probability.

bytes?: Array<number>

The bytes that were used to generate the log probability.

logprob?: number

The log probability of the token.

usage?: Usage { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details?: InputTokenDetails { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens?: number

Number of audio tokens billed for this request.

text\_tokens?: number

Number of text tokens billed for this request.

TranscriptionTextSegmentEvent { id, end, speaker, 3 more }

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

formatdouble

speaker: string

Speaker label for this segment.

start: number

Start timestamp of the segment in seconds.

formatdouble

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the event. Always `transcript.text.segment`.

TranscriptionVerbose { duration, language, text, 3 more }

Represents a verbose json transcription response returned by model, based on the provided input.

duration: number

The duration of the input audio.

formatdouble

language: string

The language of the input audio.

text: string

The transcribed text.

segments?: Array<[TranscriptionSegment](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } >

Segments of the transcribed text and their corresponding details.

id: number

Unique identifier of the segment.

avg\_logprob: number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: number

End time of the segment in seconds.

formatdouble

no\_speech\_prob: number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: number

Seek offset of the segment.

start: number

Start time of the segment in seconds.

formatdouble

temperature: number

Temperature parameter used for generating the segment.

formatfloat

text: string

Text content of the segment.

tokens: Array<number>

Array of token IDs for the text content.

usage?: Usage { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

formatdouble

type: "duration"

The type of the usage object. Always `duration` for this variant.

words?: Array<[TranscriptionWord](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)) { end, start, word } >

Extracted words and their corresponding timestamps.

end: number

End time of the word in seconds.

formatdouble

start: number

Start time of the word in seconds.

formatdouble

word: string

The text content of the word.

TranscriptionWord { end, start, word }

end: number

End time of the word in seconds.

formatdouble

start: number

Start time of the word in seconds.

formatdouble

word: string

The text content of the word.

TranscriptionCreateResponse = [Transcription](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription%20%3E%20(schema)) { text, logprobs, usage }  | [TranscriptionDiarized](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized%20%3E%20(schema)) { duration, segments, task, 2 more }  | [TranscriptionVerbose](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_verbose%20%3E%20(schema)) { duration, language, text, 3 more }

Represents a transcription response returned by model, based on the provided input.

One of the following:

Transcription { text, logprobs, usage }

Represents a transcription response returned by model, based on the provided input.

text: string

The transcribed text.

logprobs?: Array<Logprob>

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token?: string

The token in the transcription.

bytes?: Array<number>

The bytes of the token.

logprob?: number

The log probability of the token.

usage?: Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }  | Duration { seconds, type }

Token usage statistics for the request.

One of the following:

Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details?: InputTokenDetails { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens?: number

Number of audio tokens billed for this request.

text\_tokens?: number

Number of text tokens billed for this request.

Duration { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

formatdouble

type: "duration"

The type of the usage object. Always `duration` for this variant.

TranscriptionDiarized { duration, segments, task, 2 more }

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration: number

Duration of the input audio in seconds.

formatdouble

segments: Array<[TranscriptionDiarizedSegment](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema)) { id, end, speaker, 3 more } >

Segments of the transcript annotated with timestamps and speaker labels.

id: string

Unique identifier for the segment.

end: number

End timestamp of the segment in seconds.

formatdouble

speaker: string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: number

Start timestamp of the segment in seconds.

formatdouble

text: string

Transcript text for this segment.

type: "transcript.text.segment"

The type of the segment. Always `transcript.text.segment`.

task: "transcribe"

The type of task that was run. Always `transcribe`.

text: string

The concatenated transcript text for the entire audio input.

usage?: Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }  | Duration { seconds, type }

Token or duration usage statistics for the request.

One of the following:

Tokens { input\_tokens, output\_tokens, total\_tokens, 2 more }

Usage statistics for models billed by token usage.

input\_tokens: number

Number of input tokens billed for this request.

output\_tokens: number

Number of output tokens generated.

total\_tokens: number

Total number of tokens used (input + output).

type: "tokens"

The type of the usage object. Always `tokens` for this variant.

input\_token\_details?: InputTokenDetails { audio\_tokens, text\_tokens }

Details about the input tokens billed for this request.

audio\_tokens?: number

Number of audio tokens billed for this request.

text\_tokens?: number

Number of text tokens billed for this request.

Duration { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

formatdouble

type: "duration"

The type of the usage object. Always `duration` for this variant.

TranscriptionVerbose { duration, language, text, 3 more }

Represents a verbose json transcription response returned by model, based on the provided input.

duration: number

The duration of the input audio.

formatdouble

language: string

The language of the input audio.

text: string

The transcribed text.

segments?: Array<[TranscriptionSegment](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } >

Segments of the transcribed text and their corresponding details.

id: number

Unique identifier of the segment.

avg\_logprob: number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: number

End time of the segment in seconds.

formatdouble

no\_speech\_prob: number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: number

Seek offset of the segment.

start: number

Start time of the segment in seconds.

formatdouble

temperature: number

Temperature parameter used for generating the segment.

formatfloat

text: string

Text content of the segment.

tokens: Array<number>

Array of token IDs for the text content.

usage?: Usage { seconds, type }

Usage statistics for models billed by audio input duration.

seconds: number

Duration of the input audio in seconds.

formatdouble

type: "duration"

The type of the usage object. Always `duration` for this variant.

words?: Array<[TranscriptionWord](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema)) { end, start, word } >

Extracted words and their corresponding timestamps.

end: number

End time of the word in seconds.

formatdouble

start: number

Start time of the word in seconds.

formatdouble

word: string

The text content of the word.
