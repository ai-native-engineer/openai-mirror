<!-- source: https://developers.openai.com/api/reference/java/resources/audio/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Audio

##### ModelsExpand Collapse

enum AudioModel:

WHISPER\_1("whisper-1")

GPT\_4O\_TRANSCRIBE("gpt-4o-transcribe")

GPT\_4O\_MINI\_TRANSCRIBE("gpt-4o-mini-transcribe")

GPT\_4O\_MINI\_TRANSCRIBE\_2025\_12\_15("gpt-4o-mini-transcribe-2025-12-15")

GPT\_4O\_TRANSCRIBE\_DIARIZE("gpt-4o-transcribe-diarize")

enum AudioResponseFormat:

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

JSON("json")

TEXT("text")

SRT("srt")

VERBOSE\_JSON("verbose\_json")

VTT("vtt")

DIARIZED\_JSON("diarized\_json")

#### AudioTranscriptions

Turn audio into text or text into audio.

##### [Create transcription](/api/reference/java/resources/audio/subresources/transcriptions/methods/create)

[TranscriptionCreateResponse](/api/reference/java/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20TranscriptionCreateResponse%20%3E%20(schema)) audio().transcriptions().create(TranscriptionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/audio/transcriptions

##### ModelsExpand Collapse

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

class TranscriptionDiarizedSegment:

A segment of diarized transcript text with speaker metadata.

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

enum TranscriptionInclude:

LOGPROBS("logprobs")

class TranscriptionSegment:

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

class TranscriptionWord:

double end

End time of the word in seconds.

formatdouble

double start

Start time of the word in seconds.

formatdouble

String word

The text content of the word.

#### AudioTranslations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/java/resources/audio/subresources/translations/methods/create)

[TranslationCreateResponse](/api/reference/java/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20TranslationCreateResponse%20%3E%20(schema)) audio().translations().create(TranslationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/audio/translations

##### ModelsExpand Collapse

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

#### AudioSpeech

Turn audio into text or text into audio.

##### [Create speech](/api/reference/java/resources/audio/subresources/speech/methods/create)

HttpResponse audio().speech().create(SpeechCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/audio/speech

##### ModelsExpand Collapse

enum SpeechModel:

TTS\_1("tts-1")

TTS\_1\_HD("tts-1-hd")

GPT\_4O\_MINI\_TTS("gpt-4o-mini-tts")

GPT\_4O\_MINI\_TTS\_2025\_12\_15("gpt-4o-mini-tts-2025-12-15")

#### AudioVoices

Turn audio into text or text into audio.

#### AudioVoice Consents

Turn audio into text or text into audio.
