<!-- source: https://developers.openai.com/api/reference/ruby/resources/audio/subresources/voices/methods/delete/ -->

## Delete voice

`audio.voices.delete(voice_id) -> VoiceDeleted`

**delete** `/audio/voices/{voice_id}`

Deletes a voice created from a text prompt or an audio sample.

Requires voice write permission and access to the voice's project. Access to voices created from recordings is limited to eligible customers. See the [custom voices guide](https://developers.openai.com/api/docs/guides/custom-voices).

Deleting a voice does not delete its consent recording. Deleting an already deleted voice returns a 404 error.

- `voice_id: String`

- `class VoiceDeleted`

  - `id: String`

    The voice identifier.

  - `deleted: bool`

    Whether the voice was deleted.

  - `object: :"audio.voice.deleted"`

    The object type, which is always `audio.voice.deleted`.

    - `:"audio.voice.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

voice_deleted = openai.audio.voices.delete("voice_id")

puts(voice_deleted)

  "id": "voice_1234",
  "deleted": true,
  "object": "audio.voice.deleted"
