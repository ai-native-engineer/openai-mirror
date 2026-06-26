<!-- source: https://developers.openai.com/api/reference/typescript/resources/audio/subresources/translations/ -->

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

# Translations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/typescript/resources/audio/subresources/translations/methods/create)

client.audio.translations.create(TranslationCreateParams { file, model, prompt, 2 more } body, RequestOptionsoptions?): [TranslationCreateResponse](/api/reference/typescript/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

POST/audio/translations

##### ModelsExpand Collapse

Translation { text }

text: string

TranslationVerbose { duration, language, text, segments }

duration: number

The duration of the input audio.

formatdouble

language: string

The language of the output translation (always `english`).

text: string

The translated text.

segments?: Array<[TranscriptionSegment](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } >

Segments of the translated text and their corresponding details.

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

TranslationCreateResponse = [Translation](/api/reference/typescript/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)) { text }  | [TranslationVerbose](/api/reference/typescript/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)) { duration, language, text, segments }

One of the following:

Translation { text }

text: string

TranslationVerbose { duration, language, text, segments }

duration: number

The duration of the input audio.

formatdouble

language: string

The language of the output translation (always `english`).

text: string

The translated text.

segments?: Array<[TranscriptionSegment](/api/reference/typescript/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } >

Segments of the translated text and their corresponding details.

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
