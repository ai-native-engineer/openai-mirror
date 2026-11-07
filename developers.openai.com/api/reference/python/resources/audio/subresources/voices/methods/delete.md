<!-- source: https://developers.openai.com/api/reference/python/resources/audio/subresources/voices/methods/delete/ -->

## Delete voice

`audio.voices.delete(strvoice_id)  -> VoiceDeleted`

**delete** `/audio/voices/{voice_id}`

Deletes a voice created from a text prompt or an audio sample.

Requires voice write permission and access to the voice's project. Access to voices created from recordings is limited to eligible customers. See the [custom voices guide](https://developers.openai.com/api/docs/guides/custom-voices).

Deleting a voice does not delete its consent recording. Deleting an already deleted voice returns a 404 error.

- `voice_id: str`

- `class VoiceDeleted: …`

  - `id: str`

    The voice identifier.

  - `deleted: bool`

    Whether the voice was deleted.

  - `object: Literal["audio.voice.deleted"]`

    The object type, which is always `audio.voice.deleted`.

    - `"audio.voice.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
voice_deleted = client.audio.voices.delete(
    "voice_id",
print(voice_deleted.id)

  "id": "voice_1234",
  "deleted": true,
  "object": "audio.voice.deleted"
