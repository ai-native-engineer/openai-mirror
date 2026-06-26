<!-- source: https://developers.openai.com/api/reference/go/resources/audio/subresources/translations/ -->

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

# Translations

Turn audio into text or text into audio.

##### [Create translation](/api/reference/go/resources/audio/subresources/translations/methods/create)

client.Audio.Translations.New(ctx, body) (\*[Translation](/api/reference/go/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)), error)

POST/audio/translations

##### ModelsExpand Collapse

type Translation struct{…}

Text string

type TranslationVerbose struct{…}

Duration float64

The duration of the input audio.

formatdouble

Language string

The language of the output translation (always `english`).

Text string

The translated text.

Segments [][TranscriptionSegment](/api/reference/go/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))Optional

Segments of the translated text and their corresponding details.

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
