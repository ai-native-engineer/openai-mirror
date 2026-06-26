<!-- source: https://developers.openai.com/api/reference/cli/resources/audio/subresources/translations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Audio](/api/reference/cli/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Translations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/cli/resources/audio/subresources/translations/methods/create)

$ openai audio:translations create

POST/audio/translations

##### ModelsExpand Collapse

translation: object { text }

text: string

translation\_verbose: object { duration, language, text, segments }

duration: number

The duration of the input audio.

language: string

The language of the output translation (always `english`).

text: string

The translated text.

segments: optional array of [TranscriptionSegment](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more }

Segments of the translated text and their corresponding details.

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
