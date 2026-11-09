<!-- source: https://developers.openai.com/api/reference/go/resources/audio/subresources/voices/methods/delete/ -->

## Delete voice

`client.Audio.Voices.Delete(ctx, voiceID) (*VoiceDeleted, error)`

**delete** `/audio/voices/{voice_id}`

Deletes a voice created from a text prompt or an audio sample.

Requires voice write permission and access to the voice's project. Access to voices created from recordings is limited to eligible customers. See the [custom voices guide](https://developers.openai.com/api/docs/guides/custom-voices).

Deleting a voice does not delete its consent recording. Deleting an already deleted voice returns a 404 error.

- `voiceID string`

- `type VoiceDeleted struct{…}`

  - `ID string`

    The voice identifier.

  - `Deleted bool`

    Whether the voice was deleted.

  - `Object AudioVoiceDeleted`

    The object type, which is always `audio.voice.deleted`.

    - `const AudioVoiceDeletedAudioVoiceDeleted AudioVoiceDeleted = "audio.voice.deleted"`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  voiceDeleted, err := client.Audio.Voices.Delete(context.TODO(), "voice_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", voiceDeleted.ID)

  "id": "voice_1234",
  "deleted": true,
  "object": "audio.voice.deleted"
