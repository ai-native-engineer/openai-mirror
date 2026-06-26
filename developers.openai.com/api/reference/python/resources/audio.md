<!-- source: https://developers.openai.com/api/reference/python/resources/audio/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Audio

##### ModelsExpand Collapse

Literal["whisper-1", "gpt-4o-transcribe", "gpt-4o-mini-transcribe", 2 more]

One of the following:

"whisper-1"

"gpt-4o-transcribe"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe-diarize"

Literal["json", "text", "srt", 3 more]

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

One of the following:

"json"

"text"

"srt"

"verbose\_json"

"vtt"

"diarized\_json"

#### AudioTranscriptions

Turn audio into text or text into audio.

##### [Create transcription](/api/reference/python/resources/audio/subresources/transcriptions/methods/create)

audio.transcriptions.create(TranscriptionCreateParams\*\*kwargs)  -> [TranscriptionCreateResponse](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_create_response%20%3E%20(schema))

POST/audio/transcriptions

##### ModelsExpand Collapse

class Transcription: …

Represents a transcription response returned by model, based on the provided input.

text: str

The transcribed text.

logprobs: Optional[List[Logprob]]

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token: Optional[str]

The token in the transcription.

bytes: Optional[List[float]]

The bytes of the token.

logprob: Optional[float]

The log probability of the token.

usage: Optional[Usage]

Token usage statistics for the request.

One of the following:

class UsageTokens: …

Usage statistics for models billed by token usage.

input\_tokens: int

Number of input tokens billed for this request.

output\_tokens: int

Number of output tokens generated.

total\_tokens: int

Total number of tokens used (input + output).

type: Literal["tokens"]

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: Optional[UsageTokensInputTokenDetails]

Details about the input tokens billed for this request.

audio\_tokens: Optional[int]

Number of audio tokens billed for this request.

text\_tokens: Optional[int]

Number of text tokens billed for this request.

class UsageDuration: …

Usage statistics for models billed by audio input duration.

seconds: float

Duration of the input audio in seconds.

formatdouble

type: Literal["duration"]

The type of the usage object. Always `duration` for this variant.

class TranscriptionDiarized: …

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration: float

Duration of the input audio in seconds.

formatdouble

segments: List[[TranscriptionDiarizedSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema))]

Segments of the transcript annotated with timestamps and speaker labels.

id: str

Unique identifier for the segment.

end: float

End timestamp of the segment in seconds.

formatdouble

speaker: str

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: float

Start timestamp of the segment in seconds.

formatdouble

text: str

Transcript text for this segment.

type: Literal["transcript.text.segment"]

The type of the segment. Always `transcript.text.segment`.

task: Literal["transcribe"]

The type of task that was run. Always `transcribe`.

text: str

The concatenated transcript text for the entire audio input.

usage: Optional[Usage]

Token or duration usage statistics for the request.

One of the following:

class UsageTokens: …

Usage statistics for models billed by token usage.

input\_tokens: int

Number of input tokens billed for this request.

output\_tokens: int

Number of output tokens generated.

total\_tokens: int

Total number of tokens used (input + output).

type: Literal["tokens"]

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: Optional[UsageTokensInputTokenDetails]

Details about the input tokens billed for this request.

audio\_tokens: Optional[int]

Number of audio tokens billed for this request.

text\_tokens: Optional[int]

Number of text tokens billed for this request.

class UsageDuration: …

Usage statistics for models billed by audio input duration.

seconds: float

Duration of the input audio in seconds.

formatdouble

type: Literal["duration"]

The type of the usage object. Always `duration` for this variant.

class TranscriptionDiarizedSegment: …

A segment of diarized transcript text with speaker metadata.

id: str

Unique identifier for the segment.

end: float

End timestamp of the segment in seconds.

formatdouble

speaker: str

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: float

Start timestamp of the segment in seconds.

formatdouble

text: str

Transcript text for this segment.

type: Literal["transcript.text.segment"]

The type of the segment. Always `transcript.text.segment`.

Literal["logprobs"]

class TranscriptionSegment: …

id: int

Unique identifier of the segment.

avg\_logprob: float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: int

Seek offset of the segment.

start: float

Start time of the segment in seconds.

formatdouble

temperature: float

Temperature parameter used for generating the segment.

formatfloat

text: str

Text content of the segment.

tokens: List[int]

Array of token IDs for the text content.

[TranscriptionStreamEvent](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_stream_event%20%3E%20(schema))

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

One of the following:

class TranscriptionTextSegmentEvent: …

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id: str

Unique identifier for the segment.

end: float

End timestamp of the segment in seconds.

formatdouble

speaker: str

Speaker label for this segment.

start: float

Start timestamp of the segment in seconds.

formatdouble

text: str

Transcript text for this segment.

type: Literal["transcript.text.segment"]

The type of the event. Always `transcript.text.segment`.

class TranscriptionTextDeltaEvent: …

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta: str

The text delta that was additionally transcribed.

type: Literal["transcript.text.delta"]

The type of the event. Always `transcript.text.delta`.

logprobs: Optional[List[Logprob]]

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token: Optional[str]

The token that was used to generate the log probability.

bytes: Optional[List[int]]

The bytes that were used to generate the log probability.

logprob: Optional[float]

The log probability of the token.

segment\_id: Optional[str]

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

class TranscriptionTextDoneEvent: …

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text: str

The text that was transcribed.

type: Literal["transcript.text.done"]

The type of the event. Always `transcript.text.done`.

logprobs: Optional[List[Logprob]]

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token: Optional[str]

The token that was used to generate the log probability.

bytes: Optional[List[int]]

The bytes that were used to generate the log probability.

logprob: Optional[float]

The log probability of the token.

usage: Optional[Usage]

Usage statistics for models billed by token usage.

input\_tokens: int

Number of input tokens billed for this request.

output\_tokens: int

Number of output tokens generated.

total\_tokens: int

Total number of tokens used (input + output).

type: Literal["tokens"]

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: Optional[UsageInputTokenDetails]

Details about the input tokens billed for this request.

audio\_tokens: Optional[int]

Number of audio tokens billed for this request.

text\_tokens: Optional[int]

Number of text tokens billed for this request.

class TranscriptionTextDeltaEvent: …

Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

delta: str

The text delta that was additionally transcribed.

type: Literal["transcript.text.delta"]

The type of the event. Always `transcript.text.delta`.

logprobs: Optional[List[Logprob]]

The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token: Optional[str]

The token that was used to generate the log probability.

bytes: Optional[List[int]]

The bytes that were used to generate the log probability.

logprob: Optional[float]

The log probability of the token.

segment\_id: Optional[str]

Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

class TranscriptionTextDoneEvent: …

Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

text: str

The text that was transcribed.

type: Literal["transcript.text.done"]

The type of the event. Always `transcript.text.done`.

logprobs: Optional[List[Logprob]]

The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

token: Optional[str]

The token that was used to generate the log probability.

bytes: Optional[List[int]]

The bytes that were used to generate the log probability.

logprob: Optional[float]

The log probability of the token.

usage: Optional[Usage]

Usage statistics for models billed by token usage.

input\_tokens: int

Number of input tokens billed for this request.

output\_tokens: int

Number of output tokens generated.

total\_tokens: int

Total number of tokens used (input + output).

type: Literal["tokens"]

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: Optional[UsageInputTokenDetails]

Details about the input tokens billed for this request.

audio\_tokens: Optional[int]

Number of audio tokens billed for this request.

text\_tokens: Optional[int]

Number of text tokens billed for this request.

class TranscriptionTextSegmentEvent: …

Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

id: str

Unique identifier for the segment.

end: float

End timestamp of the segment in seconds.

formatdouble

speaker: str

Speaker label for this segment.

start: float

Start timestamp of the segment in seconds.

formatdouble

text: str

Transcript text for this segment.

type: Literal["transcript.text.segment"]

The type of the event. Always `transcript.text.segment`.

class TranscriptionVerbose: …

Represents a verbose json transcription response returned by model, based on the provided input.

duration: float

The duration of the input audio.

formatdouble

language: str

The language of the input audio.

text: str

The transcribed text.

segments: Optional[List[[TranscriptionSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))]]

Segments of the transcribed text and their corresponding details.

id: int

Unique identifier of the segment.

avg\_logprob: float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: int

Seek offset of the segment.

start: float

Start time of the segment in seconds.

formatdouble

temperature: float

Temperature parameter used for generating the segment.

formatfloat

text: str

Text content of the segment.

tokens: List[int]

Array of token IDs for the text content.

usage: Optional[Usage]

Usage statistics for models billed by audio input duration.

seconds: float

Duration of the input audio in seconds.

formatdouble

type: Literal["duration"]

The type of the usage object. Always `duration` for this variant.

words: Optional[List[[TranscriptionWord](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema))]]

Extracted words and their corresponding timestamps.

end: float

End time of the word in seconds.

formatdouble

start: float

Start time of the word in seconds.

formatdouble

word: str

The text content of the word.

class TranscriptionWord: …

end: float

End time of the word in seconds.

formatdouble

start: float

Start time of the word in seconds.

formatdouble

word: str

The text content of the word.

[TranscriptionCreateResponse](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_create_response%20%3E%20(schema))

Represents a transcription response returned by model, based on the provided input.

One of the following:

class Transcription: …

Represents a transcription response returned by model, based on the provided input.

text: str

The transcribed text.

logprobs: Optional[List[Logprob]]

The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

token: Optional[str]

The token in the transcription.

bytes: Optional[List[float]]

The bytes of the token.

logprob: Optional[float]

The log probability of the token.

usage: Optional[Usage]

Token usage statistics for the request.

One of the following:

class UsageTokens: …

Usage statistics for models billed by token usage.

input\_tokens: int

Number of input tokens billed for this request.

output\_tokens: int

Number of output tokens generated.

total\_tokens: int

Total number of tokens used (input + output).

type: Literal["tokens"]

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: Optional[UsageTokensInputTokenDetails]

Details about the input tokens billed for this request.

audio\_tokens: Optional[int]

Number of audio tokens billed for this request.

text\_tokens: Optional[int]

Number of text tokens billed for this request.

class UsageDuration: …

Usage statistics for models billed by audio input duration.

seconds: float

Duration of the input audio in seconds.

formatdouble

type: Literal["duration"]

The type of the usage object. Always `duration` for this variant.

class TranscriptionDiarized: …

Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

duration: float

Duration of the input audio in seconds.

formatdouble

segments: List[[TranscriptionDiarizedSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_diarized_segment%20%3E%20(schema))]

Segments of the transcript annotated with timestamps and speaker labels.

id: str

Unique identifier for the segment.

end: float

End timestamp of the segment in seconds.

formatdouble

speaker: str

Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, …).

start: float

Start timestamp of the segment in seconds.

formatdouble

text: str

Transcript text for this segment.

type: Literal["transcript.text.segment"]

The type of the segment. Always `transcript.text.segment`.

task: Literal["transcribe"]

The type of task that was run. Always `transcribe`.

text: str

The concatenated transcript text for the entire audio input.

usage: Optional[Usage]

Token or duration usage statistics for the request.

One of the following:

class UsageTokens: …

Usage statistics for models billed by token usage.

input\_tokens: int

Number of input tokens billed for this request.

output\_tokens: int

Number of output tokens generated.

total\_tokens: int

Total number of tokens used (input + output).

type: Literal["tokens"]

The type of the usage object. Always `tokens` for this variant.

input\_token\_details: Optional[UsageTokensInputTokenDetails]

Details about the input tokens billed for this request.

audio\_tokens: Optional[int]

Number of audio tokens billed for this request.

text\_tokens: Optional[int]

Number of text tokens billed for this request.

class UsageDuration: …

Usage statistics for models billed by audio input duration.

seconds: float

Duration of the input audio in seconds.

formatdouble

type: Literal["duration"]

The type of the usage object. Always `duration` for this variant.

class TranscriptionVerbose: …

Represents a verbose json transcription response returned by model, based on the provided input.

duration: float

The duration of the input audio.

formatdouble

language: str

The language of the input audio.

text: str

The transcribed text.

segments: Optional[List[[TranscriptionSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))]]

Segments of the transcribed text and their corresponding details.

id: int

Unique identifier of the segment.

avg\_logprob: float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: int

Seek offset of the segment.

start: float

Start time of the segment in seconds.

formatdouble

temperature: float

Temperature parameter used for generating the segment.

formatfloat

text: str

Text content of the segment.

tokens: List[int]

Array of token IDs for the text content.

usage: Optional[Usage]

Usage statistics for models billed by audio input duration.

seconds: float

Duration of the input audio in seconds.

formatdouble

type: Literal["duration"]

The type of the usage object. Always `duration` for this variant.

words: Optional[List[[TranscriptionWord](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_word%20%3E%20(schema))]]

Extracted words and their corresponding timestamps.

end: float

End time of the word in seconds.

formatdouble

start: float

Start time of the word in seconds.

formatdouble

word: str

The text content of the word.

#### AudioTranslations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/python/resources/audio/subresources/translations/methods/create)

audio.translations.create(TranslationCreateParams\*\*kwargs)  -> [TranslationCreateResponse](/api/reference/python/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

POST/audio/translations

##### ModelsExpand Collapse

class Translation: …

text: str

class TranslationVerbose: …

duration: float

The duration of the input audio.

formatdouble

language: str

The language of the output translation (always `english`).

text: str

The translated text.

segments: Optional[List[[TranscriptionSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))]]

Segments of the translated text and their corresponding details.

id: int

Unique identifier of the segment.

avg\_logprob: float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: int

Seek offset of the segment.

start: float

Start time of the segment in seconds.

formatdouble

temperature: float

Temperature parameter used for generating the segment.

formatfloat

text: str

Text content of the segment.

tokens: List[int]

Array of token IDs for the text content.

[TranslationCreateResponse](/api/reference/python/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

One of the following:

class Translation: …

text: str

class TranslationVerbose: …

duration: float

The duration of the input audio.

formatdouble

language: str

The language of the output translation (always `english`).

text: str

The translated text.

segments: Optional[List[[TranscriptionSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))]]

Segments of the translated text and their corresponding details.

id: int

Unique identifier of the segment.

avg\_logprob: float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: int

Seek offset of the segment.

start: float

Start time of the segment in seconds.

formatdouble

temperature: float

Temperature parameter used for generating the segment.

formatfloat

text: str

Text content of the segment.

tokens: List[int]

Array of token IDs for the text content.

#### AudioSpeech

Turn audio into text or text into audio.

##### [Create speech](/api/reference/python/resources/audio/subresources/speech/methods/create)

audio.speech.create(SpeechCreateParams\*\*kwargs)  -> BinaryResponseContent

POST/audio/speech

##### ModelsExpand Collapse

Literal["tts-1", "tts-1-hd", "gpt-4o-mini-tts", "gpt-4o-mini-tts-2025-12-15"]

One of the following:

"tts-1"

"tts-1-hd"

"gpt-4o-mini-tts"

"gpt-4o-mini-tts-2025-12-15"

#### AudioVoices

Turn audio into text or text into audio.

#### AudioVoice Consents

Turn audio into text or text into audio.
