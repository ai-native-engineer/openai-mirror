<!-- source: https://developers.openai.com/api/reference/java/resources/audio/subresources/translations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Audio](/api/reference/java/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Translations

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
