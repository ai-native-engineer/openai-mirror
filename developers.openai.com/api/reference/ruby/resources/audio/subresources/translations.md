<!-- source: https://developers.openai.com/api/reference/ruby/resources/audio/subresources/translations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Audio](/api/reference/ruby/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Translations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/ruby/resources/audio/subresources/translations/methods/create)

audio.translations.create(\*\*kwargs) -> [TranslationCreateResponse](/api/reference/ruby/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

POST/audio/translations

##### ModelsExpand Collapse

class Translation { text }

text: String

class TranslationVerbose { duration, language, text, segments }

duration: Float

The duration of the input audio.

formatdouble

language: String

The language of the output translation (always `english`).

text: String

The translated text.

segments: Array[[TranscriptionSegment](/api/reference/ruby/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } ]

Segments of the translated text and their corresponding details.

id: Integer

Unique identifier of the segment.

avg\_logprob: Float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: Float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end\_: Float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: Float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: Integer

Seek offset of the segment.

start: Float

Start time of the segment in seconds.

formatdouble

temperature: Float

Temperature parameter used for generating the segment.

formatfloat

text: String

Text content of the segment.

tokens: Array[Integer]

Array of token IDs for the text content.

TranslationCreateResponse = [Translation](/api/reference/ruby/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)) { text }  | [TranslationVerbose](/api/reference/ruby/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)) { duration, language, text, segments }

One of the following:

class Translation { text }

text: String

class TranslationVerbose { duration, language, text, segments }

duration: Float

The duration of the input audio.

formatdouble

language: String

The language of the output translation (always `english`).

text: String

The translated text.

segments: Array[[TranscriptionSegment](/api/reference/ruby/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } ]

Segments of the translated text and their corresponding details.

id: Integer

Unique identifier of the segment.

avg\_logprob: Float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: Float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end\_: Float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: Float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: Integer

Seek offset of the segment.

start: Float

Start time of the segment in seconds.

formatdouble

temperature: Float

Temperature parameter used for generating the segment.

formatfloat

text: String

Text content of the segment.

tokens: Array[Integer]

Array of token IDs for the text content.
