<!-- source: https://developers.openai.com/api/reference/python/resources/audio/subresources/translations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Audio](/api/reference/python/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Translations

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
