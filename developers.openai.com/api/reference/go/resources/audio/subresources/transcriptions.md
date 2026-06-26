<!-- source: https://developers.openai.com/api/reference/go/resources/audio/subresources/transcriptions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Audio](/api/reference/go/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Transcriptions

Turn audio into text or text into audio.

##### [Create transcription](/api/reference/go/resources/audio/subresources/transcriptions/methods/create)

client.Audio.Transcriptions.New(ctx, body) (\*[AudioTranscriptionNewResponseUnion](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20AudioTranscriptionNewResponse%20%3E%20(schema)), error)

POST/audio/transcriptions

##### ModelsExpand Collapse

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

type TranscriptionDiarized struct{…}

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

Duration float64

Duration of the input audio in seconds.

formatdouble

Segments [][TranscriptionDiarizedSegment](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema))

Segments of the transcript annotated with timestamps and speaker labels.

ID string

Unique identifier for the segment.

End float64

End timestamp of the segment in seconds.

formatdouble

Speaker string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

Start float64

Start timestamp of the segment in seconds.

formatdouble

Text string

Transcript text for this segment.

Type TranscriptTextSegment

The type of the segment. Always `transcript.text.segment`.

Task Transcribe

The type of task that was run. Always `transcribe`.

Text string

The concatenated transcript text for the entire audio input.

Usage TranscriptionDiarizedUsageUnionOptional

Token or duration usage statistics for the request.

One of the following:

TranscriptionDiarizedUsageTokens

InputTokens int64

Number of input tokens billed for this request.

OutputTokens int64

Number of output tokens generated.

TotalTokens int64

Total number of tokens used (input + output).

Type Tokens

The type of the usage object. Always `tokens` for this variant.

InputTokenDetails TranscriptionDiarizedUsageTokensInputTokenDetailsOptional

Details about the input tokens billed for this request.

AudioTokens int64Optional

Number of audio tokens billed for this request.

TextTokens int64Optional

Number of text tokens billed for this request.

TranscriptionDiarizedUsageDuration

Seconds float64

Duration of the input audio in seconds.

formatdouble

Type Duration

The type of the usage object. Always `duration` for this variant.

type TranscriptionDiarizedSegment struct{…}

A segment of diarized transcript text with speaker metadata.

ID string

Unique identifier for the segment.

End float64

End timestamp of the segment in seconds.

formatdouble

Speaker string

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

Start float64

Start timestamp of the segment in seconds.

formatdouble

Text string

Transcript text for this segment.

Type TranscriptTextSegment

The type of the segment. Always `transcript.text.segment`.

type TranscriptionInclude string

type TranscriptionSegment struct{…}

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

type TranscriptionWord struct{…}

End float64

End time of the word in seconds.

formatdouble

Start float64

Start time of the word in seconds.

formatdouble

Word string

The text content of the word.
