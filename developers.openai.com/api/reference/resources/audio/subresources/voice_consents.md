<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/ -->

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

# Voice Consents

Turn audio into text or text into audio.

##### [List voice consents](/api/reference/resources/audio/subresources/voice_consents/methods/list)

GET/audio/voice\_consents

##### [Create voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/create)

POST/audio/voice\_consents

##### [Retrieve voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/retrieve)

GET/audio/voice\_consents/{consent\_id}

##### [Update voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/update)

POST/audio/voice\_consents/{consent\_id}

##### [Delete voice consent](/api/reference/resources/audio/subresources/voice_consents/methods/delete)

DELETE/audio/voice\_consents/{consent\_id}

##### ModelsExpand Collapse

VoiceConsentListResponse object { id, created\_at, language, 2 more }

A consent recording used to authorize creation of a custom voice.

id: string

The consent recording identifier.

created\_at: number

The Unix timestamp (in seconds) for when the consent recording was created.

formatunixtime

language: string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

name: string

The label provided when the consent recording was uploaded.

object: "audio.voice\_consent"

The object type, which is always `audio.voice_consent`.

VoiceConsentCreateResponse object { id, created\_at, language, 2 more }

A consent recording used to authorize creation of a custom voice.

id: string

The consent recording identifier.

created\_at: number

The Unix timestamp (in seconds) for when the consent recording was created.

formatunixtime

language: string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

name: string

The label provided when the consent recording was uploaded.

object: "audio.voice\_consent"

The object type, which is always `audio.voice_consent`.

VoiceConsentRetrieveResponse object { id, created\_at, language, 2 more }

A consent recording used to authorize creation of a custom voice.

id: string

The consent recording identifier.

created\_at: number

The Unix timestamp (in seconds) for when the consent recording was created.

formatunixtime

language: string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

name: string

The label provided when the consent recording was uploaded.

object: "audio.voice\_consent"

The object type, which is always `audio.voice_consent`.

VoiceConsentUpdateResponse object { id, created\_at, language, 2 more }

A consent recording used to authorize creation of a custom voice.

id: string

The consent recording identifier.

created\_at: number

The Unix timestamp (in seconds) for when the consent recording was created.

formatunixtime

language: string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

name: string

The label provided when the consent recording was uploaded.

object: "audio.voice\_consent"

The object type, which is always `audio.voice_consent`.

VoiceConsentDeleteResponse object { id, deleted, object }

id: string

The consent recording identifier.

deleted: boolean

object: "audio.voice\_consent"
