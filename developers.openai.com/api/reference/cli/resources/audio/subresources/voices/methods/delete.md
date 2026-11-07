<!-- source: https://developers.openai.com/api/reference/cli/resources/audio/subresources/voices/methods/delete/ -->

## Delete voice

`$ openai audio:voices delete`

**delete** `/audio/voices/{voice_id}`

Deletes a voice created from a text prompt or an audio sample.

Requires voice write permission and access to the voice's project. Access to voices created from recordings is limited to eligible customers. See the [custom voices guide](https://developers.openai.com/api/docs/guides/custom-voices).

Deleting a voice does not delete its consent recording. Deleting an already deleted voice returns a 404 error.

- `--voice-id: string`

  The ID of the voice to delete.

- `voice_deleted: object { id, deleted, object }`

  - `id: string`

    The voice identifier.

  - `deleted: boolean`

    Whether the voice was deleted.

  - `object: "audio.voice.deleted"`

    The object type, which is always `audio.voice.deleted`.

```cli
openai audio:voices delete \
  --api-key 'My API Key' \
  --voice-id voice_id

  "id": "voice_1234",
  "deleted": true,
  "object": "audio.voice.deleted"
