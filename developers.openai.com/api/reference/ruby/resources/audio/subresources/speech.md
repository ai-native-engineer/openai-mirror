<!-- source: https://developers.openai.com/api/reference/ruby/resources/audio/subresources/speech/ -->

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

# Speech

Turn audio into text or text into audio.

##### [Create speech](/api/reference/ruby/resources/audio/subresources/speech/methods/create)

audio.speech.create(\*\*kwargs) -> StringIO

POST/audio/speech

##### ModelsExpand Collapse

SpeechModel = :"tts-1" | :"tts-1-hd" | :"gpt-4o-mini-tts" | :"gpt-4o-mini-tts-2025-12-15"

One of the following:

:"tts-1"

:"tts-1-hd"

:"gpt-4o-mini-tts"

:"gpt-4o-mini-tts-2025-12-15"
