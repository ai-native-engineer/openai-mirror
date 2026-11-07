<!-- source: https://developers.openai.com/api/reference/typescript/resources/audio/subresources/voices/methods/delete/ -->

## Delete voice

`client.audio.voices.delete(stringvoiceID, RequestOptionsoptions?): VoiceDeleted`

**delete** `/audio/voices/{voice_id}`

Deletes a voice created from a text prompt or an audio sample.

Requires voice write permission and access to the voice's project. Access to voices created from recordings is limited to eligible customers. See the [custom voices guide](https://developers.openai.com/api/docs/guides/custom-voices).

Deleting a voice does not delete its consent recording. Deleting an already deleted voice returns a 404 error.

- `voiceID: string`

- `VoiceDeleted`

  - `id: string`

    The voice identifier.

  - `deleted: boolean`

    Whether the voice was deleted.

  - `object: "audio.voice.deleted"`

    The object type, which is always `audio.voice.deleted`.

    - `"audio.voice.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const voiceDeleted = await client.audio.voices.delete('voice_id');

console.log(voiceDeleted.id);

  "id": "voice_1234",
  "deleted": true,
  "object": "audio.voice.deleted"
