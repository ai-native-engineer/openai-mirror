<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/voices/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Voices

Turn audio into text or text into audio.

##### [Create voice](/api/reference/resources/audio/subresources/voices/methods/create)

POST/audio/voices

##### ModelsExpand Collapse

VoiceCreateResponse object { id, created\_at, name, object }

A custom voice that can be used for audio output.

id: string

The voice identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the voice was created.

formatunixtime

name: string

The name of the voice.

object: "audio.voice"

The object type, which is always `audio.voice`.
